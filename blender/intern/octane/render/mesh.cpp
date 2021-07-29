/*
 * Copyright 2011, Blender Foundation.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

#include "mesh.h"
#include "kernel.h"
#include "light.h"
#include "object.h"
#include "scene.h"
#include "session.h"
#include "shader.h"

#include "util/util_progress.h"

#include <algorithm>

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Mesh::Mesh()
{
  is_octane_volume = false;

  empty = false;
  mesh_type = AUTO;
  octane_mesh.oMeshData.bUpdate = false;
  octane_mesh.oMeshOpenSubdivision.bUpdate = false;
  enable_offset_transform = false;
  need_update = false;
  final_visibility = true;
  mesh_tag = "";
  volume_modifier_tag = "";
  is_volume_to_mesh = false;
  is_mesh_to_volume = false;
}  // Mesh()

Mesh::~Mesh()
{
}  //~Mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Clear all mesh data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::clear()
{
  is_octane_volume = false;
  octane_mesh.Clear();
  octane_volume.Clear();
  used_shaders.clear();
}  // clear()

bool Mesh::is_subdivision()
{
  return subdivision_type != SUBDIVISION_NONE || octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable;
}

bool Mesh::is_volume()
{
  return is_octane_volume || octane_volume.fRegularGridData.size() > 0;
}

bool Mesh::is_global_mesh_type(Scene *scene)
{
  if (scene) {
    return scene->meshes_type == MeshType::GLOBAL ||
           (scene->meshes_type == MeshType::AS_IS && mesh_type == MeshType::GLOBAL);
  }
  return false;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag the mesh as "need update" (and "rebuild" if needed).
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::tag_update(Scene *scene)
{
  if (empty) {
    if (need_update)
      need_update = false;
    return;
  }

  need_update = true;

  scene->mesh_manager->need_update = true;
  scene->object_manager->need_update = true;
  scene->light_manager->need_update = true;
}  // tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MeshManager CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
MeshManager::MeshManager()
{
  need_update = true;
  need_global_update = false;
}  // MeshManager()

MeshManager::~MeshManager()
{
}  //~MeshManager()

inline void transform_octane_point(OctaneDataTransferObject::float_3 &a, Transform *t)
{
  a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z + t->x.w,
        a.x * t->y.x + a.y * t->y.y + a.z * t->y.z + t->y.w,
        a.x * t->z.x + a.y * t->z.y + a.z * t->z.z + t->z.w);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update all (already compiled) scene meshes on render-server (finally sends one LOAD_MESH packet
// for global mesh and one for each scattered mesh)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update_mesh(::OctaneEngine::OctaneClient *server,
                                     Scene *scene,
                                     Progress &progress,
                                     uint32_t frame_idx,
                                     uint32_t total_frames)
{
  if (!need_update)
    return;
  if (total_frames <= 1)
    need_update = false;
  progress.set_status("Loading Meshes to render-server", "");

  uint64_t ulGlobalCnt = 0;
  uint64_t ulLocalCnt = 0;
  uint64_t ulLocalVdbCnt = 0;
  bool global_update = false;

  if (need_global_update) {
    global_update = need_global_update;
    need_global_update = false;
  }
  vector<Mesh *>::iterator it;
  vector<Mesh *> local_mesh_collections;
  vector<Mesh *> volume_collections;
  for (it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
    Mesh *mesh = *it;
    if (!mesh) {
      continue;
    }
    if (mesh->empty || !mesh->need_update) {
      mesh->need_update = false;
    }
    else if (mesh->is_volume()) {
      volume_collections.emplace_back(mesh);
    }
    else {
      if (scene->meshes_type != GLOBAL && mesh->mesh_type != GLOBAL) {
        local_mesh_collections.emplace_back(mesh);
      }
    }
    if (progress.get_cancel())
      return;
  }

  if (local_mesh_collections.size() && !progress.get_cancel()) {
    int local_mesh_count = local_mesh_collections.size();
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    for (auto mesh : local_mesh_collections) {
      progress.set_status("Loading Meshes to render-server", mesh->nice_name.c_str());
      for (size_t n = 0; n < mesh->used_shaders.size(); ++n) {
        mesh->octane_mesh.sShaderNames.push_back(mesh->used_shaders[n]->name);
      }
      mesh->octane_mesh.sObjectNames.push_back("__" + mesh->name);

      bool is_velocity_motion_blur_valid = mesh->octane_mesh.oMeshData.f3Velocities.size() > 0 &&
                                           mesh->octane_mesh.oMeshData.f3Points.size() ==
                                               mesh->octane_mesh.oMeshData.f3Velocities.size();
      bool is_vertex_motion_blur_valid =
          mesh->octane_mesh.oMeshData.iSamplesNum ==
              mesh->octane_mesh.oMeshData.oMotionf3Points.size() ||
          mesh->octane_mesh.oMeshData.iSamplesNum ==
              mesh->octane_mesh.oMeshData.oMotionf3HairPoints.size();
      if (is_velocity_motion_blur_valid) {
        mesh->octane_mesh.oMeshData.iSamplesNum = 1;
      }
      else if (is_vertex_motion_blur_valid && mesh->octane_mesh.oMeshData.iSamplesNum > 1) {
        int vertices_num = mesh->octane_mesh.oMeshData.f3Points.size();
        mesh->octane_mesh.oMeshData.f3Points.clear();
        mesh->octane_mesh.oMeshData.f3Points.resize(vertices_num *
                                                    mesh->octane_mesh.oMeshData.iSamplesNum);
        int frame_idx = 0;
        for (auto it : mesh->octane_mesh.oMeshData.oMotionf3Points) {
          // if (it.second.size() != vertices_num) {
          //  fprintf(
          //      stderr,
          //      "Octane: WARNING: Octane doesn't support mesh with varied vertices!\n");
          //}
          int min_vertices_num = std::min(int(it.second.size()), vertices_num);
          for (int vertex_idx = 0; vertex_idx < min_vertices_num; ++vertex_idx) {
            mesh->octane_mesh.oMeshData
                .f3Points[vertex_idx * mesh->octane_mesh.oMeshData.iSamplesNum + frame_idx] =
                it.second[vertex_idx];
          }
          frame_idx++;
        }

        int hair_vertices_num = mesh->octane_mesh.oMeshData.f3HairPoints.size();
        mesh->octane_mesh.oMeshData.f3HairPoints.clear();
        mesh->octane_mesh.oMeshData.f3HairPoints.resize(hair_vertices_num *
                                                        mesh->octane_mesh.oMeshData.iSamplesNum);

        frame_idx = 0;
        for (auto it : mesh->octane_mesh.oMeshData.oMotionf3HairPoints) {
          if (it.second.size() != hair_vertices_num) {
            is_vertex_motion_blur_valid = false;
            break;
          }
          for (int vertex_idx = 0; vertex_idx < hair_vertices_num; ++vertex_idx) {
            mesh->octane_mesh.oMeshData
                .f3HairPoints[vertex_idx * mesh->octane_mesh.oMeshData.iSamplesNum + frame_idx] =
                it.second[vertex_idx];
          }
          frame_idx++;
        }
        if (!is_vertex_motion_blur_valid) {
          fprintf(stderr,
                  "Octane: WARNING: Octane doesn't support mesh with varied vertices or hairs!\n");
          continue;
        }
      }
      mesh->need_update = false;
      octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);
      octaneMeshes.oMeshes[octaneMeshes.oMeshes.size() - 1].oMeshData.bShowVertexData =
          mesh->octane_mesh.oMeshData.bShowVertexData;

      if (progress.get_cancel()) {
        break;
      }
    }
    if (octaneMeshes.oMeshes.size() && !progress.get_cancel()) {
      progress.set_status("Loading Meshes to render-server", "Transferring...");
      octaneMeshes.bGlobal = false;
      octaneMeshes.iCurrentFrameIdx = frame_idx;
      octaneMeshes.iTotalFrameIdx = total_frames;
      server->uploadOctaneMesh(octaneMeshes);
    }
  }

  if (volume_collections.size() && !progress.get_cancel()) {
    for (auto mesh : volume_collections) {
      progress.set_status("Loading Volumes to render-server", mesh->nice_name.c_str());
      mesh->octane_volume.sName = mesh->name;
      if (mesh->used_shaders.size()) {
        mesh->octane_volume.sShaderName = mesh->used_shaders[0]->name;
      }
      if (progress.get_cancel()) {
        break;
      }
      progress.set_status("Loading Volumes to render-server", "Transferring...");
      mesh->need_update = false;
      server->uploadVolume(&mesh->octane_volume);
    }
  }

  if (global_update && !progress.get_cancel()) {
    progress.set_status("Loading global Mesh to render-server", "");
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    // Generate Global Mesh
    OctaneDataTransferObject::OctaneMesh &globalMesh = octaneMeshes.oGlobalMesh;
    globalMesh.sName = octaneMeshes.sGlobalMeshName;
    globalMesh.bInfinitePlane = false;
    globalMesh.iCurrentActiveUVSetIdx = 0;
    globalMesh.bReshapeable = false;
    globalMesh.fMaxSmoothAngle = -1.f;
    globalMesh.sOrbxPath = "";
    globalMesh.sScriptGeoName = "";
    globalMesh.iHairWsSize = 0;
    globalMesh.iHairInterpolations = 0;
    globalMesh.oMeshData.iSamplesNum = 1;
    globalMesh.oMeshData.oMeshSphereAttribute.bEnable = false;
    globalMesh.oMeshData.bUpdate = true;
    globalMesh.oMeshOpenSubdivision.bUpdate = true;

    for (auto obj : scene->objects) {
      if (progress.get_cancel()) {
        break;
      }
      if (scene->meshes_type == MeshType::GLOBAL || obj->object_mesh_type == MeshType::GLOBAL) {
        if (!obj->visibility) {
          continue;
        }
        // Force to update every global object here
        obj->need_update = false;
        Mesh *mesh = obj->mesh;
        if (mesh && !mesh->empty && !mesh->is_volume() && mesh->final_visibility) {
          if (mesh->octane_mesh.oMeshData.f3HairPoints.size()) {
            fprintf(
                stderr,
                "Octane: WARNING: Skip hair mesh, which can't be rendered on \"Global\" mesh\n");
          }
          if (scene->meshes_type == MeshType::GLOBAL || mesh->mesh_type == MeshType::GLOBAL) {
            mesh->need_update = false;
          }
          octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);
          OctaneDataTransferObject::OctaneMesh &current_octane_mesh =
              octaneMeshes.oMeshes[octaneMeshes.oMeshes.size() - 1];
          Transform *t = &obj->transform;
          current_octane_mesh.sShaderNames.clear();
          current_octane_mesh.sObjectNames.clear();
          for (size_t n = 0; n < mesh->used_shaders.size(); ++n) {
            current_octane_mesh.sShaderNames.push_back(mesh->used_shaders[n]->name);
          }
          current_octane_mesh.sObjectNames.push_back("__" + mesh->name);
          current_octane_mesh.bReshapeable = false;
          OctaneDataTransferObject::OctaneMeshData &currentMeshData =
              current_octane_mesh.oMeshData;
          for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Points.size(); ++ptr_idx) {
            OctaneDataTransferObject::float_3 &a = currentMeshData.f3Points[ptr_idx];
            a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z + t->x.w,
                  a.x * t->y.x + a.y * t->y.y + a.z * t->y.z + t->y.w,
                  a.x * t->z.x + a.y * t->z.y + a.z * t->z.z + t->z.w);
          }
          for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Normals.size(); ++ptr_idx) {
            OctaneDataTransferObject::float_3 &a = currentMeshData.f3Normals[ptr_idx];
            a.set(a.x * t->x.x + a.y * t->x.y + a.z * t->x.z,
                  a.x * t->y.x + a.y * t->y.y + a.z * t->y.z,
                  a.x * t->z.x + a.y * t->z.y + a.z * t->z.z);
          }
        }
      }
    }

    if (!progress.get_cancel() && octaneMeshes.oMeshes.size()) {
      progress.set_status("Loading global Mesh to render-server", string("Transferring..."));
      octaneMeshes.bGlobal = true;
      octaneMeshes.sGlobalMeshName = GLOBAL_MESH_NAME;
      octaneMeshes.sGlobalLayerName = GLOBAL_MESH_LAYERMAP_NAME;
      octaneMeshes.iCurrentFrameIdx = frame_idx;
      octaneMeshes.iTotalFrameIdx = total_frames;
      if (octaneMeshes.oMeshes.size()) {
        globalMesh.fMaxSmoothAngle = 0.f;
        for (auto &mesh : octaneMeshes.oMeshes) {
          globalMesh.fMaxSmoothAngle += std::max(0.f, mesh.fMaxSmoothAngle);
        }
        globalMesh.fMaxSmoothAngle /= octaneMeshes.oMeshes.size();
      }
      else {
        globalMesh.fMaxSmoothAngle = -1.f;
      }
      size_t f3PointsSize = 0, f3NormalSize = 0, f3UVSize = 0, iPointIndicesSize = 0,
             iNormalIndicesSize = 0, iUVIndicesSize = 0, iVertexPerPolySize = 0,
             iPolyMaterialSize = 0, iPolyObjectIndexSize = 0, sShaderNamesSize = 0,
             sObjectNamesSize = 0, fOpenSubdCreasesSharpnessesSize = 0,
             iOpenSubdCreasesIndicesSize = 0;
      for (auto &mesh : octaneMeshes.oMeshes) {
        f3PointsSize += mesh.oMeshData.f3Points.size();
        f3NormalSize += mesh.oMeshData.f3Normals.size();
        f3UVSize += mesh.oMeshData.f3UVs.size();
        iPointIndicesSize += mesh.oMeshData.iPointIndices.size();
        iNormalIndicesSize += mesh.oMeshData.iNormalIndices.size();
        iUVIndicesSize += mesh.oMeshData.iUVIndices.size();
        iVertexPerPolySize += mesh.oMeshData.iVertexPerPoly.size();
        iPolyMaterialSize += mesh.oMeshData.iPolyMaterialIndex.size();
        iPolyObjectIndexSize += mesh.oMeshData.iPolyObjectIndex.size();
        sShaderNamesSize += mesh.sShaderNames.size();
        sObjectNamesSize += mesh.sObjectNames.size();
        fOpenSubdCreasesSharpnessesSize +=
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size();
        iOpenSubdCreasesIndicesSize += mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size();
      }
      globalMesh.oMeshData.f3Points.reserve(f3PointsSize);
      globalMesh.oMeshData.f3Normals.reserve(f3NormalSize);
      globalMesh.oMeshData.f3UVs.reserve(f3UVSize);
      globalMesh.oMeshData.iPointIndices.reserve(iPointIndicesSize);
      globalMesh.oMeshData.iNormalIndices.reserve(iNormalIndicesSize);
      globalMesh.oMeshData.iUVIndices.reserve(iUVIndicesSize);
      globalMesh.oMeshData.iVertexPerPoly.reserve(iVertexPerPolySize);
      globalMesh.oMeshData.iPolyMaterialIndex.reserve(iPolyMaterialSize);
      globalMesh.oMeshData.iPolyObjectIndex.reserve(iPolyObjectIndexSize);
      globalMesh.sShaderNames.reserve(sShaderNamesSize);
      globalMesh.sObjectNames.reserve(sObjectNamesSize);
      globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.reserve(
          fOpenSubdCreasesSharpnessesSize);
      globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.reserve(iOpenSubdCreasesIndicesSize);
      size_t currentPointIndicesOffset = 0, currentNormalIndicesOffset = 0,
             currentUVIndicesOffset = 0, currentPolyMaterialOffset = 0,
             currentPolyObjectOffset = 0;
      for (auto &mesh : octaneMeshes.oMeshes) {
        for (int idx = 0; idx < mesh.oMeshData.iPointIndices.size(); ++idx) {
          mesh.oMeshData.iPointIndices[idx] += currentPointIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iNormalIndices.size(); ++idx) {
          mesh.oMeshData.iNormalIndices[idx] += currentNormalIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iUVIndices.size(); ++idx) {
          mesh.oMeshData.iUVIndices[idx] += currentUVIndicesOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iPolyMaterialIndex.size(); ++idx) {
          mesh.oMeshData.iPolyMaterialIndex[idx] += currentPolyMaterialOffset;
        }
        for (int idx = 0; idx < mesh.oMeshData.iPolyObjectIndex.size(); ++idx) {
          mesh.oMeshData.iPolyObjectIndex[idx] += currentPolyObjectOffset;
        }
        currentPointIndicesOffset += mesh.oMeshData.f3Points.size();
        currentNormalIndicesOffset += mesh.oMeshData.f3Normals.size();
        currentUVIndicesOffset += mesh.oMeshData.f3UVs.size();
        currentPolyMaterialOffset += mesh.sShaderNames.size();
        currentPolyObjectOffset += mesh.sObjectNames.size();
      }
      for (auto &mesh : octaneMeshes.oMeshes) {
        globalMesh.oMeshData.f3Points.insert(globalMesh.oMeshData.f3Points.end(),
                                             mesh.oMeshData.f3Points.begin(),
                                             mesh.oMeshData.f3Points.end());
        globalMesh.oMeshData.f3Normals.insert(globalMesh.oMeshData.f3Normals.end(),
                                              mesh.oMeshData.f3Normals.begin(),
                                              mesh.oMeshData.f3Normals.end());
        globalMesh.oMeshData.f3UVs.insert(globalMesh.oMeshData.f3UVs.end(),
                                          mesh.oMeshData.f3UVs.begin(),
                                          mesh.oMeshData.f3UVs.end());
        globalMesh.oMeshData.iPointIndices.insert(globalMesh.oMeshData.iPointIndices.end(),
                                                  mesh.oMeshData.iPointIndices.begin(),
                                                  mesh.oMeshData.iPointIndices.end());
        globalMesh.oMeshData.iNormalIndices.insert(globalMesh.oMeshData.iNormalIndices.end(),
                                                   mesh.oMeshData.iNormalIndices.begin(),
                                                   mesh.oMeshData.iNormalIndices.end());
        globalMesh.oMeshData.iUVIndices.insert(globalMesh.oMeshData.iUVIndices.end(),
                                               mesh.oMeshData.iUVIndices.begin(),
                                               mesh.oMeshData.iUVIndices.end());
        globalMesh.oMeshData.iVertexPerPoly.insert(globalMesh.oMeshData.iVertexPerPoly.end(),
                                                   mesh.oMeshData.iVertexPerPoly.begin(),
                                                   mesh.oMeshData.iVertexPerPoly.end());
        globalMesh.oMeshData.iPolyMaterialIndex.insert(
            globalMesh.oMeshData.iPolyMaterialIndex.end(),
            mesh.oMeshData.iPolyMaterialIndex.begin(),
            mesh.oMeshData.iPolyMaterialIndex.end());
        globalMesh.oMeshData.iPolyObjectIndex.insert(globalMesh.oMeshData.iPolyObjectIndex.end(),
                                                     mesh.oMeshData.iPolyObjectIndex.begin(),
                                                     mesh.oMeshData.iPolyObjectIndex.end());
        globalMesh.sShaderNames.insert(
            globalMesh.sShaderNames.end(), mesh.sShaderNames.begin(), mesh.sShaderNames.end());
        globalMesh.sObjectNames.insert(
            globalMesh.sObjectNames.end(), mesh.sObjectNames.begin(), mesh.sObjectNames.end());
        globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.insert(
            globalMesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.end(),
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.begin(),
            mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.end());
        globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.insert(
            globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.end(),
            mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.begin(),
            mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.end());
      }
      if (!progress.get_cancel()) {
        server->uploadOctaneMesh(octaneMeshes);
      }
    }
  }
}  // server_update_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render-server (sends "LOAD_MESH" packets finally)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::server_update(::OctaneEngine::OctaneClient *server,
                                Scene *scene,
                                Progress &progress,
                                uint32_t frame_idx,
                                uint32_t total_frames)
{
  if (!need_update)
    return;

  server_update_mesh(server, scene, progress, frame_idx, total_frames);

  // need_update = false;
}  // server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag all meshes to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_update(Scene *scene)
{
  need_update = true;
  scene->object_manager->need_update = true;
}  // tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag global mesh to update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void MeshManager::tag_global_update()
{
  need_update = true;
  need_global_update = true;
}  // tag_global_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Scatter Helper
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool ScatterHelper::is_scatterable(Mesh *p_mesh, Scene *p_scene)
{
  if (!p_mesh || !p_scene)
    return false;
  return (p_scene->meshes_type == MeshType::SCATTER ||
          (p_scene->meshes_type == MeshType::AS_IS && p_mesh->mesh_type == MeshType::SCATTER)) &&
         p_mesh->scatter_group_id >= 0;
}

void ScatterHelper::record(Mesh *p_mesh, Scene *p_scene)
{
  if (is_scatterable(p_mesh, p_scene)) {
    if (m_data.find(p_mesh->scatter_group_id) == m_data.end()) {
      // init and record the first mesh as the data source
      m_data[p_mesh->scatter_group_id] = ScatterGroupData(p_mesh->scatter_group_id, p_mesh->name);
    }
    else if (p_mesh->is_scatter_group_source) {
      // replace the original source if current one it set as source
      m_data[p_mesh->scatter_group_id].m_source_mesh_name = p_mesh->name;
    }
  }
}

bool ScatterHelper::need_upload(Mesh *p_mesh)
{
  if (p_mesh && m_data.find(p_mesh->scatter_group_id) != m_data.end()) {
    return m_data[p_mesh->scatter_group_id].m_source_mesh_name.compare(p_mesh->name) == 0;
  }
  return true;
}

bool ScatterHelper::try_to_insert_instance_into_scatter(Scene *p_scene,
                                                        Mesh *p_mesh,
                                                        Object *p_object)
{
  if (p_scene && p_mesh && p_object && m_data.find(p_mesh->scatter_group_id) != m_data.end()) {
    ScatterGroupData &data = m_data[p_mesh->scatter_group_id];
    float *p_matrices = new float[12];
    ObjectManager::resolve_transform(p_mesh, p_object, p_matrices);
    data.m_matrices.reserve(data.m_matrices.size() + 12);
    for (int i = 0; i < 12; ++i) {
      data.m_matrices.emplace_back(p_matrices[i]);
    }
    data.m_instance_ids.emplace_back(p_mesh->scatter_instance_id);
    if (data.m_source_mesh_name.compare(p_mesh->name) == 0) {
      data.m_shader_names.clear();
      data.m_shader_names.reserve(p_mesh->used_shaders.size());
      for (std::vector<Shader *>::iterator it = p_mesh->used_shaders.begin();
           it != p_mesh->used_shaders.end();
           ++it) {
        data.m_shader_names.push_back((*it)->name);
      }
    }
    delete[] p_matrices;
    return true;
  }
  return false;
}

bool ScatterHelper::upload_scatters(::OctaneEngine::OctaneClient *server,
                                    uint32_t frame_idx,
                                    uint32_t total_frames)
{
  for (std::unordered_map<int32_t, ScatterGroupData>::iterator it = m_data.begin();
       it != m_data.end();
       ++it) {
    std::string cur_scatter_name = "Scatter__" + std::to_string(it->first);
    ScatterGroupData &data = it->second;
    int32_t instance_count = data.m_instance_ids.size();
    float *scatter_matrices = new float[data.m_matrices.size()];
    int32_t *scatter_instance_ids = new int32_t[instance_count];
    for (int scatter_matrices_i = 0; scatter_matrices_i < data.m_matrices.size();
         ++scatter_matrices_i) {
      scatter_matrices[scatter_matrices_i] = data.m_matrices[scatter_matrices_i];
    }
    for (int scatter_instance_i = 0; scatter_instance_i < instance_count; ++scatter_instance_i) {
      scatter_instance_ids[scatter_instance_i] = data.m_instance_ids[scatter_instance_i];
    }
    server->uploadScatter(cur_scatter_name,
                          data.m_source_mesh_name,
                          true,
                          scatter_matrices,
                          scatter_instance_ids,
                          instance_count,
                          false,
                          data.m_shader_names,
                          frame_idx,
                          total_frames);
    delete[] scatter_matrices;
    delete[] scatter_instance_ids;
  }
  return true;
}

OCT_NAMESPACE_END
