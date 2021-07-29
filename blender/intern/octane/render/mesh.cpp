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
#include "shader.h"
#include "light.h"
#include "object.h"
#include "scene.h"
#include "session.h"
#include "kernel.h"

#include "util/util_progress.h"

#include <algorithm>

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Mesh::Mesh() : vdb_regular_grid(nullptr), vdb_grid_size(0)
{
  is_octane_volume = false;
  vdb_file_path = "";
  last_vdb_frame = 0;
  vdb_resolution.x = 0.0f;
  vdb_resolution.y = 0.0f;
  vdb_resolution.z = 0.0f;
  vdb_absorption_offset = -1;
  vdb_emission_offset = -1;
  vdb_scatter_offset = -1;
  vdb_velocity_x_offset = -1;
  vdb_velocity_y_offset = -1;
  vdb_velocity_z_offset = -1;

  empty = false;
  mesh_type = GLOBAL;
  octane_mesh.oMeshData.bUpdate = false;
  octane_mesh.oMeshOpenSubdivision.bUpdate = false;
  need_update = true;
  final_visibility = true;
}  // Mesh()

Mesh::~Mesh()
{
  if (vdb_regular_grid)
    delete[] vdb_regular_grid;
}  //~Mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Clear all mesh data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Mesh::clear()
{
  if (vdb_regular_grid) {
    delete[] vdb_regular_grid;
    vdb_regular_grid = nullptr;
  }
  is_octane_volume = false;
  vdb_file_path = "";
  vdb_resolution.x = 0.0f;
  vdb_resolution.y = 0.0f;
  vdb_resolution.z = 0.0f;
  vdb_grid_size = 0;
  vdb_absorption_offset = -1;
  vdb_emission_offset = -1;
  vdb_scatter_offset = -1;
  vdb_velocity_x_offset = -1;
  vdb_velocity_y_offset = -1;
  vdb_velocity_z_offset = -1;

  octane_mesh.Clear();

  used_shaders.clear();

}  // clear()

bool Mesh::is_global_mesh_type(Scene *scene)
{
  if (scene) {
    return scene->meshes_type == Mesh::GLOBAL ||
           (scene->meshes_type == Mesh::AS_IS && mesh_type == Mesh::GLOBAL);
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

  m_scatter_helper.reset();

  if (need_global_update) {
    global_update = need_global_update;
    need_global_update = false;
  }
  vector<Mesh *>::iterator it;
  for (it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
    Mesh *mesh = *it;
    // record every mesh in current scene for following scatter node check
    m_scatter_helper.record(mesh, scene);
    if (mesh->empty) {
      if (mesh->need_update)
        mesh->need_update = false;
      continue;
    }
    else if (scene->meshes_type == Mesh::GLOBAL ||
             (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL)) {
      if (mesh->vdb_regular_grid || mesh->is_octane_volume)
        ++ulLocalVdbCnt;
      else if (total_frames <= 1 && (scene->first_frame || scene->anim_mode == FULL)) {
        ++ulGlobalCnt;
        if (mesh->need_update && !global_update)
          global_update = true;
      }
      continue;
    }
    if (!mesh->need_update ||
        (!scene->first_frame &&
         (scene->anim_mode == CAM_ONLY ||
          (scene->anim_mode == MOVABLE_PROXIES && scene->meshes_type != Mesh::RESHAPABLE_PROXY &&
           (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY)))))
      continue;

    if (mesh->vdb_regular_grid || mesh->is_octane_volume)
      ++ulLocalVdbCnt;
    else
      ++ulLocalCnt;

    if (progress.get_cancel())
      return;
  }

  bool interrupted = false;

  if (ulLocalCnt) {
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    uint64_t *used_shaders_size = new uint64_t[ulLocalCnt];
    uint64_t *used_objects_size = new uint64_t[ulLocalCnt];
    vector<string> *shader_names = new vector<string>[ulLocalCnt];
    vector<string> *object_names = new vector<string>[ulLocalCnt];

    uint64_t i = 0;
    vector<Mesh *>::iterator it;
    for (it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
      Mesh *mesh = *it;
      if (!m_scatter_helper.need_upload(mesh))
        continue;
      if (mesh->vdb_regular_grid || mesh->is_octane_volume)
        continue;
      if (mesh->empty || !mesh->need_update ||
          (scene->meshes_type == Mesh::GLOBAL ||
           (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::GLOBAL)) ||
          (!scene->first_frame &&
           (scene->anim_mode == CAM_ONLY ||
            (scene->anim_mode == MOVABLE_PROXIES && scene->meshes_type != Mesh::RESHAPABLE_PROXY &&
             (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY)))))
        continue;

      if (scene->meshes_type == Mesh::SCATTER ||
          (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::SCATTER)) {
        progress.set_status("Loading Meshes to render-server",
                            string("Scatter: ") + mesh->nice_name.c_str());
      }
      else if (scene->meshes_type == Mesh::MOVABLE_PROXY ||
               (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::MOVABLE_PROXY))
        progress.set_status("Loading Meshes to render-server",
                            string("Movable: ") + mesh->nice_name.c_str());
      else if (scene->meshes_type == Mesh::RESHAPABLE_PROXY ||
               (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))
        progress.set_status("Loading Meshes to render-server",
                            string("Reshapable: ") + mesh->nice_name.c_str());

      used_shaders_size[i] = mesh->used_shaders.size();
      for (size_t n = 0; n < used_shaders_size[i]; ++n) {
        shader_names[i].push_back(mesh->used_shaders[n]->name);
      }

      used_objects_size[i] = 1;
      object_names[i].push_back("__" + mesh->name);

      mesh->octane_mesh.bReshapeable = (scene->meshes_type == Mesh::RESHAPABLE_PROXY ||
                                        (scene->meshes_type == Mesh::AS_IS &&
                                         mesh->mesh_type == Mesh::RESHAPABLE_PROXY));

      if (mesh->need_update && (total_frames <= 1 || !mesh->octane_mesh.bReshapeable))
        mesh->need_update = false;
      if (progress.get_cancel()) {
        interrupted = true;
        break;
      }

      bool is_motion_blur_valid = mesh->octane_mesh.oMeshData.iSamplesNum ==
                                  mesh->octane_mesh.oMeshData.oMotionf3Points.size();
      if (is_motion_blur_valid && mesh->octane_mesh.oMeshData.iSamplesNum > 1) {
        int vertices_num = mesh->octane_mesh.oMeshData.f3Points.size();
        mesh->octane_mesh.oMeshData.f3Points.clear();
        mesh->octane_mesh.oMeshData.f3Points.resize(vertices_num *
                                                    mesh->octane_mesh.oMeshData.iSamplesNum);
        int frame_idx = 0;
        for (auto it : mesh->octane_mesh.oMeshData.oMotionf3Points) {
          if (it.second.size() != vertices_num) {
            is_motion_blur_valid = false;
            break;
          }
          for (int vertex_idx = 0; vertex_idx < vertices_num; ++vertex_idx) {
            mesh->octane_mesh.oMeshData
                .f3Points[vertex_idx * mesh->octane_mesh.oMeshData.iSamplesNum + frame_idx] =
                it.second[vertex_idx];
          }
          frame_idx++;
        }
      }
      if (!is_motion_blur_valid) {
        fprintf(stderr, "Octane: WARNING: Octane doesn't support mesh with varied vertices!\n");
        continue;
      }

      mesh->octane_mesh.sShaderNames = shader_names[i];
      mesh->octane_mesh.sObjectNames = object_names[i];
      octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);

      ++i;
    }
    if (i && !interrupted) {
      progress.set_status("Loading Meshes to render-server", "Transferring...");
      octaneMeshes.bGlobal = false;
      octaneMeshes.iCurrentFrameIdx = frame_idx;
      octaneMeshes.iTotalFrameIdx = total_frames;

      server->uploadOctaneMesh(octaneMeshes);
    }
    delete[] used_shaders_size;
    delete[] used_objects_size;
    delete[] shader_names;
    delete[] object_names;
  }

  if (ulLocalVdbCnt && !interrupted) {
    uint64_t i = 0;
    vector<Mesh *>::iterator it;
    for (it = scene->meshes.begin(); it != scene->meshes.end(); ++it) {
      Mesh *mesh = *it;
      if (!mesh->vdb_regular_grid && !mesh->is_octane_volume)
        continue;
      if (mesh->empty ||
          !mesh->need_update
          //|| (scene->meshes_type == Mesh::GLOBAL || (scene->meshes_type == Mesh::AS_IS &&
          // mesh->mesh_type == Mesh::GLOBAL))
          ||
          (!scene->first_frame &&
           (scene->anim_mode == CAM_ONLY ||
            (scene->anim_mode == MOVABLE_PROXIES && scene->meshes_type != Mesh::RESHAPABLE_PROXY &&
             (scene->meshes_type != Mesh::AS_IS || mesh->mesh_type != Mesh::RESHAPABLE_PROXY)))))
        continue;

      if (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::GLOBAL ||
          scene->meshes_type == Mesh::GLOBAL ||
          (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::SCATTER))
        progress.set_status("Loading Volumes to render-server",
                            string("Scatter: ") + mesh->nice_name.c_str());
      else if (scene->meshes_type == Mesh::MOVABLE_PROXY ||
               (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::MOVABLE_PROXY))
        progress.set_status("Loading Volumes to render-server",
                            string("Movable: ") + mesh->nice_name.c_str());
      else if (scene->meshes_type == Mesh::RESHAPABLE_PROXY ||
               (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))
        progress.set_status("Loading Volumes to render-server",
                            string("Reshapable: ") + mesh->nice_name.c_str());

      ::OctaneDataTransferObject::OctaneVolume volume;

      volume.sName = mesh->name;
      volume.pfRegularGrid = mesh->vdb_regular_grid;
      volume.iGridSize = mesh->vdb_grid_size;
      volume.f3Resolution = {
          mesh->vdb_resolution.x, mesh->vdb_resolution.y, mesh->vdb_resolution.z};
      volume.gridMatrix = mesh->vdb_grid_matrix;
      volume.fISO = mesh->vdb_iso;
      volume.iAbsorptionOffset = mesh->vdb_absorption_offset;
      volume.fAbsorptionScale = mesh->vdb_absorption_scale;
      volume.iEmissionOffset = mesh->vdb_emission_offset;
      volume.fEmissionScale = mesh->vdb_emission_scale;
      volume.iScatterOffset = mesh->vdb_scatter_offset;
      volume.fScatterScale = mesh->vdb_scatter_scale;
      volume.iVelocityOffsetX = mesh->vdb_velocity_x_offset;
      volume.iVelocityOffsetY = mesh->vdb_velocity_y_offset;
      volume.iVelocityOffsetZ = mesh->vdb_velocity_z_offset;
      volume.fVelocityScale = mesh->vdb_velocity_scale;
      volume.bSDF = mesh->vdb_sdf;

      volume.sFileName = mesh->is_octane_volume ? mesh->vdb_file_path : "";

      if (mesh->used_shaders.size())
        volume.sMedium = mesh->used_shaders[0]->name;

      if (mesh->need_update &&
          (total_frames <= 1 ||
           !(scene->meshes_type == Mesh::RESHAPABLE_PROXY ||
             (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type == Mesh::RESHAPABLE_PROXY))))
        mesh->need_update = false;
      if (progress.get_cancel()) {
        interrupted = true;
        break;
      }
      ++i;

      progress.set_status("Loading Volumes to render-server", "Transferring...");
      server->uploadVolume(&volume);
    }
  }

  if (global_update && !interrupted) {
    OctaneDataTransferObject::OctaneMeshes octaneMeshes;
    // Generate Global Mesh
    OctaneDataTransferObject::OctaneMesh &globalMesh = octaneMeshes.oGlobalMesh;
    globalMesh.Clear();
    globalMesh.sName = octaneMeshes.sGlobalMeshName;
    globalMesh.bInfinitePlane = false;
    globalMesh.iCurrentActiveUVSetIdx = 0;
    globalMesh.bReshapeable = false;
    globalMesh.fMaxSmoothAngle = -1.f;
    globalMesh.oMeshData.bUpdate = true;
    globalMesh.oMeshOpenSubdivision.bUpdate = true;

    progress.set_status("Loading global Mesh to render-server", "");
    uint64_t obj_cnt = 0;
    for (vector<Object *>::const_iterator obj_it = scene->objects.begin();
         obj_it != scene->objects.end();
         ++obj_it) {
      Mesh *mesh = (*obj_it)->mesh;
      if (mesh->vdb_regular_grid || mesh->is_octane_volume)
        continue;

      if (!mesh || mesh->empty || (!scene->first_frame && scene->anim_mode != FULL) ||
          (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY ||
           scene->meshes_type == Mesh::RESHAPABLE_PROXY) ||
          (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type != Mesh::GLOBAL))
        continue;

      if (!(*obj_it)->visibility)
        continue;

      ++obj_cnt;
    }
    char *name = "__global";
    if (obj_cnt > 0) {
      uint64_t *used_shaders_size = new uint64_t[obj_cnt];
      uint64_t *used_objects_size = new uint64_t[obj_cnt];
      vector<string> *shader_names = new vector<string>[obj_cnt];
      vector<string> *object_names = new vector<string>[obj_cnt];

      obj_cnt = 0;
      bool hair_present = false;
      for (vector<Object *>::const_iterator obj_it = scene->objects.begin();
           obj_it != scene->objects.end();
           ++obj_it) {
        Mesh *mesh = (*obj_it)->mesh;
        if (mesh->vdb_regular_grid || mesh->is_octane_volume)
          continue;

        if (!mesh || mesh->empty || (!scene->first_frame && scene->anim_mode != FULL) ||
            (scene->meshes_type == Mesh::SCATTER || scene->meshes_type == Mesh::MOVABLE_PROXY ||
             scene->meshes_type == Mesh::RESHAPABLE_PROXY) ||
            (scene->meshes_type == Mesh::AS_IS && mesh->mesh_type != oct::Mesh::GLOBAL))
          continue;

        Object *mesh_object = (*obj_it);
        if (!mesh_object->visibility)
          continue;

        Transform &tfm = mesh_object->transform;

        used_shaders_size[obj_cnt] = mesh->used_shaders.size();
        for (size_t n = 0; n < used_shaders_size[obj_cnt]; ++n) {
          shader_names[obj_cnt].push_back(mesh->used_shaders[n]->name);
        }

        used_objects_size[obj_cnt] = 1;
        object_names[obj_cnt].push_back("__" + mesh->name);

        if (mesh->need_update)
          mesh->need_update = false;
        if (progress.get_cancel()) {
          interrupted = true;
          break;
        }

        mesh->octane_mesh.sShaderNames = shader_names[obj_cnt];
        mesh->octane_mesh.sObjectNames = object_names[obj_cnt];
        mesh->octane_mesh.bReshapeable = false;

        octaneMeshes.oMeshes.emplace_back(mesh->octane_mesh);
        OctaneDataTransferObject::OctaneMeshData &currentMeshData =
            octaneMeshes.oMeshes[octaneMeshes.oMeshes.size() - 1].oMeshData;

        for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Points.size(); ++ptr_idx) {
          float3 transformed_point = transform_point(
              &tfm,
              make_float3(currentMeshData.f3Points[ptr_idx].x,
                          currentMeshData.f3Points[ptr_idx].y,
                          currentMeshData.f3Points[ptr_idx].z));
          currentMeshData.f3Points[ptr_idx] = OctaneDataTransferObject::float_3(
              transformed_point.x, transformed_point.y, transformed_point.z);
        }
        for (int ptr_idx = 0; ptr_idx < currentMeshData.f3Normals.size(); ++ptr_idx) {
          float3 transformed_point = transform_direction(
              &tfm,
              make_float3(currentMeshData.f3Normals[ptr_idx].x,
                          currentMeshData.f3Normals[ptr_idx].y,
                          currentMeshData.f3Normals[ptr_idx].z));
          currentMeshData.f3Normals[ptr_idx] = OctaneDataTransferObject::float_3(
              transformed_point.x, transformed_point.y, transformed_point.z);
        }

        ++obj_cnt;

        if (!hair_present && mesh->octane_mesh.oMeshData.f3HairPoints.size())
          hair_present = true;
      }
      if (obj_cnt && !interrupted) {
        if (hair_present)
          fprintf(stderr, "Octane: WARNING: hair can't be rendered on \"Global\" mesh\n");

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
        globalMesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.reserve(
            iOpenSubdCreasesIndicesSize);
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
        server->uploadOctaneMesh(octaneMeshes);
      }
      delete[] used_shaders_size;
      delete[] used_objects_size;
      delete[] shader_names;
      delete[] object_names;
    }
    else
      ulGlobalCnt = 0;
  }
  std::string cur_name("__global");
  if (!ulGlobalCnt && scene->anim_mode == FULL)
    server->deleteMesh(true, cur_name);
  // need_update = false;
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
  return (p_scene->meshes_type == Mesh::SCATTER ||
          (p_scene->meshes_type == Mesh::AS_IS && p_mesh->mesh_type == Mesh::SCATTER)) &&
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
