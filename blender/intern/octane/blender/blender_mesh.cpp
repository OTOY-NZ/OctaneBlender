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
#include "render/graph.h"
#include "render/mesh.h"
#include "render/scene.h"

#include "blender_sync.h"
#include "blender_util.h"

#include "RNA_blender_cpp.h"

OCT_NAMESPACE_BEGIN

static std::string resolve_octane_geometry_node(PointerRNA &oct_mesh)
{
  std::string sScriptGeoName;
  PointerRNA octane_geo_node_collections = RNA_pointer_get(&oct_mesh,
                                                           "octane_geo_node_collections");
  char scriptGeoMaterialName[512];
  char scriptGeoNodeName[512];
  RNA_string_get(&octane_geo_node_collections, "node_graph_tree", scriptGeoMaterialName);
  RNA_string_get(&octane_geo_node_collections, "osl_geo_node", scriptGeoNodeName);
  std::string scriptGeoMaterialNameStr(scriptGeoMaterialName);
  std::string scriptGeoNodeNameStr(scriptGeoNodeName);
  if (scriptGeoMaterialNameStr.size() && scriptGeoNodeNameStr.size()) {
    sScriptGeoName = scriptGeoMaterialNameStr + "_" + scriptGeoNodeNameStr;
  }
  return sScriptGeoName;
}

static std::string resolve_orbx_proxy_path(PointerRNA &oct_mesh,
                                           BL::BlendData &b_data,
                                           BL::Scene &b_scene)
{
  std::string sOrbxPath;
  char orbxFilePath[512];
  RNA_string_get(&oct_mesh, "imported_orbx_file_path", orbxFilePath);
  std::string orbxFilePathStr(orbxFilePath);
  if (orbxFilePathStr.size()) {
    sOrbxPath = blender_absolute_path(b_data, b_scene, orbxFilePath);
  }
  return sOrbxPath;
}

static void add_face(Mesh *mesh,
                     Mesh::WindingOrder winding_order,
                     const vector<int> &vi,
                     int material_idx,
                     bool with_uv)
{
  int current_index = mesh->octane_mesh.oMeshData.iPointIndices.size();
  for (int i = 0, j = vi.size() - 1; i < vi.size(); ++i, --j) {
    if (winding_order == Mesh::CLOCKWISE) {
      mesh->octane_mesh.oMeshData.iPointIndices.push_back(vi[i]);
    }
    else {
      mesh->octane_mesh.oMeshData.iPointIndices.push_back(vi[j]);
    }
    if (with_uv) {
      if (winding_order == Mesh::CLOCKWISE) {
        mesh->octane_mesh.oMeshData.iUVIndices.push_back(current_index + i);
      }
      else {
        mesh->octane_mesh.oMeshData.iUVIndices.push_back(current_index + j);
      }
    }
  }
  mesh->octane_mesh.oMeshData.iVertexPerPoly.push_back(vi.size());
  mesh->octane_mesh.oMeshData.iPolyMaterialIndex.push_back(material_idx);
  mesh->octane_mesh.oMeshData.iPolyObjectIndex.push_back(0);
}

static void create_mesh(Scene *scene,
                        BL::Object &b_ob,
                        Mesh *mesh,
                        BL::Mesh &b_mesh,
                        const std::vector<Shader *> &used_shaders,
                        Mesh::WindingOrder winding_order,
                        bool subdivision = false,
                        bool subdivide_uvs = true)
{
  mesh->octane_mesh.oMeshData.bUpdate = true;
  /* count vertices and faces */
  int numverts = b_mesh.vertices.length();
  int numfaces = (!subdivision) ? b_mesh.loop_triangles.length() : b_mesh.polygons.length();
  int numtris = 0;
  int numcorners = 0;
  int numngons = 0;
  bool use_loop_normals = b_mesh.use_auto_smooth() &&
                          (mesh->subdivision_type != Mesh::SUBDIVISION_CATMULL_CLARK);
  bool use_uv = numfaces != 0 && b_mesh.uv_layers.length() != 0;

  if (mesh->octane_mesh.sOrbxPath.length() > 0) {
    mesh->empty = false;
    return;
  }

  if (mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable && numfaces == 0) {
    mesh->octane_mesh.oMeshData.f3Points.reserve(numverts);
    BL::Mesh::vertices_iterator v;
    for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v) {
      mesh->octane_mesh.oMeshData.f3SphereCenters.push_back(get_octane_float3(v->co()));
    }
    return;
  }

  if (numverts == 0 || numfaces == 0) {
    if (!mesh->empty)
      mesh->empty = true;
    fprintf(stderr, "Octane: The mesh \"%s\" is empty\n", b_ob.data().name().c_str());
    return;
  }

  if (!subdivision) {
    numtris = numfaces;
  }
  else {
    BL::Mesh::polygons_iterator p;
    for (b_mesh.polygons.begin(p); p != b_mesh.polygons.end(); ++p) {
      numngons += (p->loop_total() == 4) ? 0 : 1;
      numcorners += p->loop_total();
    }
  }

  mesh->empty = false;
  mesh->octane_mesh.oMeshOpenSubdivision.bUpdate = true;
  mesh->octane_mesh.oMeshData.iSamplesNum = 1;
  mesh->octane_mesh.oMeshData.f3Points.reserve(numverts);
  mesh->octane_mesh.oMeshData.f3Normals.reserve(numverts);
  mesh->octane_mesh.oMeshData.iVertexPerPoly.reserve(numfaces);
  mesh->octane_mesh.oMeshData.iPolyMaterialIndex.reserve(numfaces);
  mesh->octane_mesh.oMeshData.iPolyObjectIndex.reserve(numfaces);

  int max_numindices = numfaces * 4;
  mesh->octane_mesh.oMeshData.iPointIndices.reserve(max_numindices);
  mesh->octane_mesh.oMeshData.iUVIndices.reserve(max_numindices);

  /* create vertex coordinates and normals */
  BL::Mesh::vertices_iterator v;
  for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v) {
    mesh->octane_mesh.oMeshData.f3Points.push_back(get_octane_float3(v->co()));
    mesh->octane_mesh.oMeshData.f3Normals.push_back(get_octane_float3(v->normal()));
  }
  mesh->octane_mesh.oMeshData.oMotionf3Points[0] = mesh->octane_mesh.oMeshData.f3Points;

  /* create faces */
  if (!subdivision) {
    BL::Mesh::loop_triangles_iterator t;
    vector<int> vi3;
    vi3.resize(3);

    for (b_mesh.loop_triangles.begin(t); t != b_mesh.loop_triangles.end(); ++t) {
      BL::MeshPolygon p = b_mesh.polygons[t->polygon_index()];
      int3 vi = get_int3(t->vertices());
      for (int i = 0; i < 3; ++i) {
        vi3[i] = vi[i];
      }

      int shader = clamp(p.material_index(), 0, used_shaders.size() - 1);
      bool smooth = p.use_smooth() || use_loop_normals;

      if (use_loop_normals) {
        BL::Array<float, 9> loop_normals = t->split_normals();
        for (int i = 0; i < 3; i++) {
          mesh->octane_mesh.oMeshData.f3Normals[vi[i]] = OctaneDataTransferObject::float_3(
              loop_normals[i * 3], loop_normals[i * 3 + 1], loop_normals[i * 3 + 2]);
        }
      }

      /* Create triangles.
       *
       * NOTE: Autosmooth is already taken care about.
       */
      add_face(mesh, winding_order, vi3, shader, use_uv);
    }
  }
  else {
    BL::Mesh::polygons_iterator p;
    vector<int> vi;

    for (b_mesh.polygons.begin(p); p != b_mesh.polygons.end(); ++p) {
      int n = p->loop_total();
      int shader = clamp(p->material_index(), 0, used_shaders.size() - 1);
      bool smooth = p->use_smooth() || use_loop_normals;

      vi.resize(n);
      for (int i = 0; i < n; i++) {
        /* NOTE: Autosmooth is already taken care about. */
        vi[i] = b_mesh.loops[p->loop_start() + i].vertex_index();
      }

      /* create subd faces */
      add_face(mesh, winding_order, vi, shader, use_uv);
    }
  }

  mesh->octane_mesh.oMeshData.iNormalIndices = mesh->octane_mesh.oMeshData.iPointIndices;

  /* create uvs */
  unsigned long numindices = mesh->octane_mesh.oMeshData.iPointIndices.size();
  mesh->octane_mesh.iCurrentActiveUVSetIdx = 0;
  mesh->octane_mesh.oMeshData.f3CandidateUVs.resize(MAX_OCTANE_UV_SETS);
  mesh->octane_mesh.oMeshData.iCandidateUVIndices.resize(MAX_OCTANE_UV_SETS);

  if (use_uv) {
    int candidate_uv_set_idx = 0;
    BL::Mesh::uv_layers_iterator l;
    for (b_mesh.uv_layers.begin(l); l != b_mesh.uv_layers.end(); ++l) {
      if (candidate_uv_set_idx >= MAX_OCTANE_UV_SETS) {
        break;
      }

      std::vector<OctaneDataTransferObject::float_3> &f3CandidateUV =
          mesh->octane_mesh.oMeshData.f3CandidateUVs[candidate_uv_set_idx];
      f3CandidateUV.clear();
      f3CandidateUV.reserve(max_numindices);
      if (!subdivision) {
        BL::Mesh::loop_triangles_iterator t;
        for (b_mesh.loop_triangles.begin(t); t != b_mesh.loop_triangles.end(); ++t) {
          int3 li = get_int3(t->loops());
          for (int j = 0; j < 3; ++j) {
            f3CandidateUV.push_back(get_octane_float3(l->data[li[j]].uv()));
          }
        }
      }
      else {
        BL::Mesh::polygons_iterator p;
        for (b_mesh.polygons.begin(p); p != b_mesh.polygons.end(); ++p) {
          int n = p->loop_total();
          for (int j = 0; j < n; j++) {
            f3CandidateUV.push_back(get_octane_float3(l->data[p->loop_start() + j].uv()));
          }
        }
      }

      if (l->active_render()) {
        mesh->octane_mesh.iCurrentActiveUVSetIdx = candidate_uv_set_idx;
        mesh->octane_mesh.oMeshData.f3UVs = f3CandidateUV;
      }
      mesh->octane_mesh.oMeshData.iCandidateUVIndices[candidate_uv_set_idx] =
          mesh->octane_mesh.oMeshData.iUVIndices;
      ++candidate_uv_set_idx;
    }
  }
  else {
    mesh->octane_mesh.oMeshData.f3UVs.push_back(OctaneDataTransferObject::float_3(0, 0, 0));
    mesh->octane_mesh.oMeshData.iUVIndices = std::vector<int32_t>(numindices, 0);
    for (int uv_set_idx = 0; uv_set_idx < MAX_OCTANE_UV_SETS; ++uv_set_idx) {
      mesh->octane_mesh.oMeshData.f3CandidateUVs[uv_set_idx].push_back(
          OctaneDataTransferObject::float_3(0, 0, 0));
      mesh->octane_mesh.oMeshData.iCandidateUVIndices[uv_set_idx] = std::vector<int32_t>(
          numindices, 0);
    }
  }

  /* create vertex float data */
  int vertex_float_count = std::min(MAX_OCTANE_FLOAT_VERTEX_SETS, b_ob.vertex_groups.length());
  std::unordered_map<int, int> vertex_group_index_map;
  mesh->octane_mesh.oMeshData.fVertexFloats.clear();
  for (int vertex_group_idx = 0; vertex_group_idx < vertex_float_count; ++vertex_group_idx) {
    mesh->octane_mesh.oMeshData.sVertexFloatNames.emplace_back(
        b_ob.vertex_groups[vertex_group_idx].name());
    mesh->octane_mesh.oMeshData.fVertexFloats.emplace_back(std::vector<float>());
    mesh->octane_mesh.oMeshData.fVertexFloats[vertex_group_idx].resize(numverts, 0);
    vertex_group_index_map[b_ob.vertex_groups[vertex_group_idx].index()] = vertex_group_idx;
  }
  unsigned long vert_idx = 0;
  for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v, ++vert_idx) {
    for (int cur_group_idx = 0; cur_group_idx < v->groups.length(); ++cur_group_idx) {
      int group_id = v->groups[cur_group_idx].group();
      float weight = v->groups[cur_group_idx].weight();
      if (vertex_group_index_map.find(group_id) != vertex_group_index_map.end()) {
        mesh->octane_mesh.oMeshData.fVertexFloats[vertex_group_index_map[group_id]][vert_idx] =
            weight;
      }
    }
  }

  /* create vertex color data */
  int vertex_colors_count = std::min(MAX_OCTANE_COLOR_VERTEX_SETS, b_mesh.vertex_colors.length());
  int tessface_vertex_colors_count = b_mesh.vertex_colors.length();
  int inactive_count = MAX_OCTANE_COLOR_VERTEX_SETS - 1;
  BL::Mesh::vertex_colors_iterator l;
  for (b_mesh.vertex_colors.begin(l); l != b_mesh.vertex_colors.end(); ++l) {
    if (inactive_count == 0 && !l->active_render())
      continue;
    if (!l->active_render())
      inactive_count--;
    mesh->octane_mesh.oMeshData.sVertexColorNames.emplace_back(l->name());
    mesh->octane_mesh.oMeshData.f3VertexColors.emplace_back(
        std::vector<OctaneDataTransferObject::float_3>());
    std::vector<OctaneDataTransferObject::float_3> &colorVertex =
        mesh->octane_mesh.oMeshData
            .f3VertexColors[mesh->octane_mesh.oMeshData.f3VertexColors.size() - 1];
    std::vector<int32_t> &iPointIndices = mesh->octane_mesh.oMeshData.iPointIndices;
    colorVertex.resize(numverts);
    size_t currentPointIdx = 0;
    if (!subdivision) {
      BL::Mesh::loop_triangles_iterator t;
      for (b_mesh.loop_triangles.begin(t); t != b_mesh.loop_triangles.end(); ++t) {
        int3 li = get_int3(t->loops());
        for (int j = 0, k = 2; j < 3; ++j, --k) {
          int indices_idx = li[winding_order == Mesh::CLOCKWISE ? j : k];
          int vertices_idx = iPointIndices[currentPointIdx++];
          colorVertex[vertices_idx] = get_octane_float3(l->data[indices_idx].color());
        }
      }
    }
    else {
      BL::Mesh::polygons_iterator p;
      for (b_mesh.polygons.begin(p); p != b_mesh.polygons.end(); ++p) {
        int n = p->loop_total();
        for (int j = 0, k = n - 1; j < n; j++, --k) {
          int indices_idx = p->loop_start() + (winding_order == Mesh::CLOCKWISE ? j : k);
          int vertices_idx = iPointIndices[currentPointIdx++];
          colorVertex[vertices_idx] = get_octane_float3(l->data[indices_idx].color());
        }
      }
    }
    if (mesh->octane_mesh.oMeshData.sVertexColorNames.size() >= MAX_OCTANE_COLOR_VERTEX_SETS)
      break;
  }

  if (mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable) {
    mesh->octane_mesh.oMeshData.f3SphereCenters = mesh->octane_mesh.oMeshData.f3Points;
    mesh->octane_mesh.oMeshData.f2SphereUVs.resize(
        mesh->octane_mesh.oMeshData.f3SphereCenters.size());
    for (int i = 0; i < mesh->octane_mesh.oMeshData.f2SphereUVs.size(); ++i) {
      size_t j =
          mesh->octane_mesh.oMeshData.iPointIndices[mesh->octane_mesh.oMeshData.iUVIndices[i]];
      mesh->octane_mesh.oMeshData.f2SphereUVs[j].x = mesh->octane_mesh.oMeshData.f3UVs[i].x;
      mesh->octane_mesh.oMeshData.f2SphereUVs[j].y = mesh->octane_mesh.oMeshData.f3UVs[i].y;
    }
    mesh->octane_mesh.oMeshData.sSphereVertexColorNames =
        mesh->octane_mesh.oMeshData.sVertexColorNames;
    mesh->octane_mesh.oMeshData.sSphereVertexFloatNames =
        mesh->octane_mesh.oMeshData.sVertexFloatNames;
    mesh->octane_mesh.oMeshData.f3SphereVertexColors = mesh->octane_mesh.oMeshData.f3VertexColors;
    mesh->octane_mesh.oMeshData.fSphereVertexFloats = mesh->octane_mesh.oMeshData.fVertexFloats;
  }
}

static void create_subd_mesh(Scene *scene,
                             BL::Object &b_ob,
                             Mesh *mesh,
                             BL::Mesh &b_mesh,
                             const std::vector<Shader *> &used_shaders,
                             Mesh::WindingOrder winding_order)
{
  bool subdivide_uvs = false;
  if (b_ob.modifiers.length()) {
    BL::SubsurfModifier subsurf_mod(b_ob.modifiers[b_ob.modifiers.length() - 1]);
    subdivide_uvs = subsurf_mod.uv_smooth() != BL::SubsurfModifier::uv_smooth_NONE;
  }

  create_mesh(scene, b_ob, mesh, b_mesh, used_shaders, winding_order, true, subdivide_uvs);

  mesh->octane_mesh.oMeshOpenSubdivision.bUpdate = true;

  /* export creases */
  size_t num_creases = 0;
  BL::Mesh::edges_iterator e;

  for (b_mesh.edges.begin(e); e != b_mesh.edges.end(); ++e) {
    if (e->crease() != 0.0f) {
      num_creases++;
    }
  }

  mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.resize(num_creases * 2);
  mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.resize(num_creases);

  if (num_creases) {
    int *crease_indices = mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.data();
    float *crease_sharpnesses =
        mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.data();

    for (b_mesh.edges.begin(e); e != b_mesh.edges.end(); ++e) {
      if (e->crease() != 0.0f) {
        crease_indices[0] = e->vertices()[0];
        crease_indices[1] = e->vertices()[1];
        *crease_sharpnesses = e->crease();

        crease_indices += 2;
        ++crease_sharpnesses;
      }
    }
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Fill Octane mesh object with OpenVDB data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void create_openvdb_volume(BL::FluidDomainSettings &b_domain,
                                  Scene *scene,
                                  BL::Object b_ob,
                                  Mesh *mesh,
                                  BL::Mesh b_mesh,
                                  PointerRNA *oct_mesh,
                                  const std::vector<Shader *> &used_shaders)
{
  BL::Array<int, 3> res = b_domain.domain_resolution();
  int length, amplify = (b_domain.use_noise()) ? b_domain.noise_scale() : 1;

  int width = mesh->octane_volume.f3Resolution.x = res[0] * amplify;
  int height = mesh->octane_volume.f3Resolution.y = res[1] * amplify;
  int depth = mesh->octane_volume.f3Resolution.z = res[2] * amplify;
  int32_t num_pixels = width * height * depth;

  if (num_pixels) {
    if (mesh->mesh_type == MeshType::GLOBAL)
      mesh->mesh_type = MeshType::SCATTER;

    float *density = new float[num_pixels];
    float *flame = new float[num_pixels];
    // float *color = new float[num_pixels * 4];

    int grid_offset = 0;

    FluidDomainSettings_density_grid_get_length(&b_domain.ptr, &length);
    if (length == num_pixels) {
      FluidDomainSettings_density_grid_get(&b_domain.ptr, (float *)density);
      mesh->octane_volume.iAbsorptionOffset = grid_offset++;
      mesh->octane_volume.iScatterOffset = mesh->octane_volume.iAbsorptionOffset;
    }
    /* this is in range 0..1, and interpreted by the OpenGL smoke viewer
     * as 1500..3000 K with the first part faded to zero density */
    FluidDomainSettings_flame_grid_get_length(&b_domain.ptr, &length);
    if (length == num_pixels) {
      FluidDomainSettings_flame_grid_get(&b_domain.ptr, (float *)flame);
      mesh->octane_volume.iEmissionOffset = grid_offset++;
    }
    /* the RGB is "premultiplied" by density for better interpolation results */
    // SmokeDomainSettings_color_grid_get_length(&b_domain.ptr, &length);
    // if(length == num_pixels * 4) {
    //    SmokeDomainSettings_color_grid_get(&b_domain.ptr, (float*)color);
    //    mesh->vdb_emission_offset = grid_offset++;
    //}

    if (grid_offset > 0) {
      mesh->octane_volume.fRegularGridData.resize(num_pixels * grid_offset);
      mesh->octane_volume.f3Resolution.x = width;
      mesh->octane_volume.f3Resolution.y = height;
      mesh->octane_volume.f3Resolution.z = depth;

      float3 max_bound{-FLT_MAX, -FLT_MAX, -FLT_MAX}, min_bound{FLT_MAX, FLT_MAX, FLT_MAX};
      if (b_mesh.vertices.length() > 0) {
        BL::Mesh::vertices_iterator v;
        for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v) {
          float3 point = get_float3(v->co());
          if (min_bound.x > point.x)
            min_bound.x = point.x;
          if (min_bound.y > point.y)
            min_bound.y = point.y;
          if (min_bound.z > point.z)
            min_bound.z = point.z;
          if (max_bound.x < point.x)
            max_bound.x = point.x;
          if (max_bound.y < point.y)
            max_bound.y = point.y;
          if (max_bound.z < point.z)
            max_bound.z = point.z;
        }

        mesh->octane_volume.oMatrix.m[0] = {
            (max_bound.x - min_bound.x) / width, 0.0f, 0.0f, min_bound.x};
        mesh->octane_volume.oMatrix.m[1] = {
            0.0f, (max_bound.y - min_bound.y) / height, 0.0f, min_bound.y};
        mesh->octane_volume.oMatrix.m[2] = {
            0.0f, 0.0f, (max_bound.z - min_bound.z) / depth, min_bound.z};
      }
      else {
        mesh->octane_volume.oMatrix.m[0] = {0.0f, 0.0f, 0.0f, 0.0f};
        mesh->octane_volume.oMatrix.m[1] = {0.0f, 0.0f, 0.0f, 0.0f};
        mesh->octane_volume.oMatrix.m[2] = {0.0f, 0.0f, 0.0f, 0.0f};
      }

      for (int i = 0; i < num_pixels; ++i) {
        register int index = i * grid_offset;
        if (mesh->octane_volume.iAbsorptionOffset >= 0)
          mesh->octane_volume.fRegularGridData[index + mesh->octane_volume.iAbsorptionOffset] =
              density[i];
        // if(mesh->vdb_scatter_offset >= 0)       mesh->vdb_regular_grid[index +
        // mesh->vdb_scatter_offset]    = dencity[i];
        if (mesh->octane_volume.iEmissionOffset >= 0)
          mesh->octane_volume.fRegularGridData[index + mesh->octane_volume.iEmissionOffset] =
              flame[i];
      }
    }
    delete[] density;
    delete[] flame;
    // delete[] color;
  }
  else {
    if (!mesh->empty)
      mesh->empty = true;
    fprintf(stderr, "Octane: The vdb volume \"%s\" is empty\n", b_ob.data().name().c_str());
  }
}  // create_openvdb_volume()

static void sync_mesh_fluid_motion(BL::Object &b_ob, Scene *scene, Mesh *mesh)
{
  mesh->octane_mesh.oMeshData.f3Velocities.clear();
  BL::FluidDomainSettings b_fluid_domain = object_fluid_domain_find(b_ob);

  if (!b_fluid_domain)
    return;

  /* If the mesh has modifiers following the fluid domain we can't export motion. */
  if (b_fluid_domain.mesh_vertices.length() != mesh->octane_mesh.oMeshData.f3Points.size())
    return;

  BL::FluidDomainSettings::mesh_vertices_iterator svi;
  int i = 0;
  mesh->octane_mesh.oMeshData.f3Velocities.resize(mesh->octane_mesh.oMeshData.f3Points.size());
  for (b_fluid_domain.mesh_vertices.begin(svi); svi != b_fluid_domain.mesh_vertices.end();
       ++svi, ++i) {
    mesh->octane_mesh.oMeshData.f3Velocities[i] = get_octane_float3(svi->velocity());
  }
}

static void sync_mesh_particles(BL::Object &b_ob, Mesh *mesh, bool background)
{
  if (!mesh) {
    return;
  }
  BL::Object::modifiers_iterator b_mod;
  for (b_ob.modifiers.begin(b_mod); b_mod != b_ob.modifiers.end(); ++b_mod) {
    if ((b_mod->type() == b_mod->type_PARTICLE_SYSTEM) &&
        (background ? b_mod->show_render() : b_mod->show_viewport())) {
      BL::ParticleSystemModifier psmd((const PointerRNA)b_mod->ptr);
      BL::ParticleSystem b_psys((const PointerRNA)psmd.particle_system().ptr);
      BL::ParticleSettings b_part((const PointerRNA)b_psys.settings().ptr);

      PointerRNA particle_settings = b_part.ptr;
      PointerRNA oct_settings = RNA_pointer_get(&b_part.ptr, "octane");
      bool use_as_octane_sphere_primitive =
          get_boolean(particle_settings, "use_as_octane_sphere_primitive") &&
          (b_part.render_type() != BL::ParticleSettings::render_type_COLLECTION &&
           b_part.render_type() != BL::ParticleSettings::render_type_OBJECT);
      float octane_velocity_multiplier = get_float(particle_settings,
                                                   "octane_velocity_multiplier");
      float octane_sphere_size_multiplier = get_float(particle_settings,
                                                      "octane_sphere_size_multiplier");
      int material_idx = b_part.material() - 1;
      if (use_as_octane_sphere_primitive) {
        mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = true;
        mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed = -1;
        size_t num = mesh->octane_mesh.oMeshData.f3SphereCenters.size() +
                     b_psys.particles.length();
        mesh->octane_mesh.oMeshData.fSphereRadiuses.reserve(num);
        mesh->octane_mesh.oMeshData.f3SphereCenters.reserve(num);
        mesh->octane_mesh.oMeshData.f3SphereSpeeds.reserve(num);
        mesh->octane_mesh.oMeshData.iSphereMaterialIndices.reserve(num);
        Transform tfm = get_transform(b_ob.matrix_world());
        Transform rotation_tfm = euler_to_transform(get_float3(b_ob.rotation_euler()));
        Transform itfm = transform_quick_inverse(tfm);
        Transform irotation_tfm = transform_quick_inverse(rotation_tfm);
        BL::ParticleSystem::particles_iterator b_pa;
        b_psys.particles.begin(b_pa);
        for (; b_pa != b_psys.particles.end(); ++b_pa) {
          if (b_pa->is_exist() && b_pa->is_visible() &&
              b_pa->alive_state() == BL::Particle::alive_state_ALIVE) {
            oct::float3 location = get_float3(b_pa->location());
            location = transform_point(&itfm, location);
            oct::float3 velocity = get_float3(b_pa->velocity());
            velocity = transform_point(&irotation_tfm, velocity);
            velocity *= octane_velocity_multiplier;
            mesh->octane_mesh.oMeshData.fSphereRadiuses.emplace_back(
                b_pa->size() * octane_sphere_size_multiplier);
            mesh->octane_mesh.oMeshData.f3SphereCenters.emplace_back(
                OctaneDataTransferObject::float_3(location.x, location.y, location.z));
            mesh->octane_mesh.oMeshData.f3SphereSpeeds.emplace_back(
                OctaneDataTransferObject::float_3(velocity.x, velocity.y, velocity.z));
            mesh->octane_mesh.oMeshData.iSphereMaterialIndices.emplace_back(material_idx);
          }
        }
      }
    }
  }
}

Mesh *BlenderSync::sync_mesh(BL::Depsgraph &b_depsgraph,
                             BL::Object &b_ob,
                             BL::Object &b_ob_instance,
                             bool object_updated,
                             bool show_self,
                             bool show_particles,
                             OctaneDataTransferObject::OctaneObjectLayer &object_layer,
                             MeshType mesh_type)
{
  BL::ID b_ob_data = b_ob.data();
  BL::ID key = (BKE_object_is_modified(b_ob)) ? b_ob_instance : b_ob_data;
  BL::Material material_override = view_layer.material_override;

  /* find shader indices */
  std::vector<Shader *> used_shaders;

  BL::Object::material_slots_iterator slot;
  for (b_ob.material_slots.begin(slot); slot != b_ob.material_slots.end(); ++slot) {
    if (material_override) {
      find_shader(material_override, used_shaders, scene->default_surface);
    }
    else {
      BL::ID b_material(slot->material());
      find_shader(b_material, used_shaders, scene->default_surface);
    }
  }

  if (used_shaders.size() == 0) {
    if (material_override)
      find_shader(material_override, used_shaders, scene->default_surface);
    else
      used_shaders.push_back(scene->default_surface);
  }

  bool use_octane_vertex_displacement_subdvision = false;
  for (auto used_shader : used_shaders) {
    if (used_shader->graph && used_shader->graph->need_subdivision) {
      use_octane_vertex_displacement_subdvision = true;
    }
  }

  Mesh *octane_mesh;
  PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");

  bool is_modified = BKE_object_is_modified(b_ob);
  std::string mesh_name = resolve_octane_name(
      b_ob_data, is_modified ? b_ob.name_full() : "", MESH_TAG);

  bool is_mesh_data_updated = mesh_map.sync(&octane_mesh, key);
  bool is_mesh_shader_data_updated = octane_mesh->shaders_tag !=
                                     Mesh::generate_shader_tag(used_shaders);

  octane_mesh->nice_name = mesh_name;
  octane_mesh->name = mesh_name;
  octane_mesh->octane_mesh.sMeshName = mesh_name;
  // The mesh can be shared among objects with different mesh_type, so we only upgrade mesh_type
  // here. E.g. a mesh is shared by two objects: one is SCATTER type and the other is RESHARPABLE.
  // The final mesh type of the mesh will be RESHARPABLE.
  if (octane_mesh->mesh_type == MeshType::AUTO || mesh_type >= octane_mesh->mesh_type) {
    octane_mesh->mesh_type = mesh_type;
  }

  if (b_ob.type() == BL::Object::type_VOLUME) {
    if (mesh_synced.find(octane_mesh) != mesh_synced.end()) {
      return octane_mesh;
    }
    BL::Volume b_volume = BL::Volume(b_ob.data());
    b_volume.grids.load(b_data.ptr.data);
    octane_mesh->is_octane_volume = true;
    int current_frame = b_scene.frame_current();
    octane_mesh->need_update = is_mesh_data_updated ||
                               octane_mesh->last_vdb_frame != b_scene.frame_current();
    octane_mesh->last_vdb_frame = current_frame;
    octane_mesh->used_shaders = used_shaders;
    octane_mesh->shaders_tag = Mesh::generate_shader_tag(used_shaders);
    octane_mesh->octane_mesh.bInfinitePlane = false;
    std::string selected_grid_name;
    if (b_volume.grids.is_loaded()) {
      if (b_volume.grids.length()) {
        BL::Volume::grids_iterator grid;
        int grid_idx = 0, active_idx = b_volume.grids.active_index();
        for (b_volume.grids.begin(grid); grid != b_volume.grids.end(); ++grid, ++grid_idx) {
          if (grid->is_loaded() && active_idx == grid_idx) {
            selected_grid_name = grid->name();
            break;
          }
        }
      }
      std::string volume_path = b_volume.grids.frame_filepath();
      octane_mesh->octane_volume.sVolumePath = blender_absolute_path(b_data, b_scene, volume_path);
    }
    resolve_volume_attributes(oct_mesh, octane_mesh->octane_volume);
    bool apply_import_scale_to_blender_transfrom = RNA_boolean_get(
        &oct_mesh, "apply_import_scale_to_blender_transfrom");
    if (apply_import_scale_to_blender_transfrom) {
      octane_mesh->octane_volume.iImportScale = 4;  // Default meters
    }
    if (selected_grid_name.length()) {
      if (octane_mesh->octane_volume.sAbsorptionGridId.sVal.length() == 0) {
        octane_mesh->octane_volume.sAbsorptionGridId = selected_grid_name;
      }
      if (octane_mesh->octane_volume.sEmissionGridId.sVal.length() == 0) {
        octane_mesh->octane_volume.sEmissionGridId = selected_grid_name;
      }
      if (octane_mesh->octane_volume.sScatterGridId.sVal.length() == 0) {
        octane_mesh->octane_volume.sScatterGridId = selected_grid_name;
      }
      if (octane_mesh->octane_volume.sVelocityGridId.sVal.length() == 0) {
        octane_mesh->octane_volume.sVelocityGridId = selected_grid_name;
        octane_mesh->octane_volume.sVelocityGridId = selected_grid_name;
        octane_mesh->octane_volume.sVelocityGridId = selected_grid_name;
      }
    }
    octane_mesh->enable_offset_transform = RNA_boolean_get(&oct_mesh,
                                                           "enable_octane_offset_transform");
    if (octane_mesh->enable_offset_transform) {
      float3 translate, euler, scale;
      int mode = RNA_enum_get(&oct_mesh, "octane_offset_rotation_order");
      RNA_float_get_array(
          &oct_mesh, "octane_offset_translation", reinterpret_cast<float *>(&translate));
      RNA_float_get_array(&oct_mesh, "octane_offset_rotation", reinterpret_cast<float *>(&euler));
      RNA_float_get_array(&oct_mesh, "octane_offset_scale", reinterpret_cast<float *>(&scale));
      octane_mesh->offset_transform = make_transform(translate, euler, mode, scale);
    }

    mesh_synced.insert(octane_mesh);
    if (octane_mesh->need_update) {
      octane_mesh->tag_update(scene);
    }
    return octane_mesh;
  }

  octane_mesh->octane_mesh.bInfinitePlane = RNA_boolean_get(&oct_mesh, "infinite_plane");
  octane_mesh->octane_mesh.sScriptGeoName = resolve_octane_geometry_node(oct_mesh);
  octane_mesh->octane_mesh.sOrbxPath = resolve_orbx_proxy_path(oct_mesh, b_data, b_scene);
  octane_mesh->octane_mesh.bReshapeable = resolve_mesh_type(
                                              mesh_name, b_ob.type(), octane_mesh->mesh_type) ==
                                          MeshType::RESHAPABLE_PROXY;

  bool octane_vdb_force_update_flag = RNA_boolean_get(&oct_mesh, "octane_vdb_helper") &&
                                      octane_mesh &&
                                      octane_mesh->last_vdb_frame != b_scene.frame_current();
  bool octane_subdivision_need_update = use_octane_vertex_displacement_subdvision &&
                                        !octane_mesh->is_subdivision();
  bool need_update = preview ? (is_mesh_data_updated || is_mesh_shader_data_updated ||
                                octane_vdb_force_update_flag || octane_subdivision_need_update) :
                               is_octane_geometry_required(
                                   mesh_name, b_ob.type(), oct_mesh, octane_mesh, mesh_type);
  bool need_recreate_mesh = false;
  if (preview) {
    bool is_synced = is_resource_synced_in_octane_manager(mesh_name, OctaneResourceType::GEOMETRY);
    if (is_synced) {
      bool paint_mode = b_ob.mode() == b_ob.mode_VERTEX_PAINT || b_ob.mode_WEIGHT_PAINT ||
                        b_ob.mode_TEXTURE_PAINT;
      if (paint_mode) {
        for (auto used_shader : used_shaders) {
          if (used_shader->graph && used_shader->graph->need_subdivision) {
            used_shader->has_object_dependency = true;
            used_shader->need_sync_object = true;
          }
        }
	  }
      if (paint_mode || b_ob.mode() == b_ob.mode_EDIT || is_mesh_shader_data_updated || is_modified) {
        need_recreate_mesh = need_update;
      }
      else {
        need_recreate_mesh = is_octane_geometry_required(
            mesh_name, b_ob.type(), oct_mesh, octane_mesh, mesh_type);
      }
    }
    else {
      bool is_resource_dirty = dirty_resources.find(b_ob_data.name()) != dirty_resources.end();
      bool is_mesh_cached = !is_resource_dirty && !octane_mesh->octane_mesh.bReshapeable &&
                            resource_cache_data.find(mesh_name) != resource_cache_data.end() &&
                            resource_cache_data[mesh_name] == OctaneDataTransferObject::GEOMETRY;
      if (is_mesh_cached) {
        sync_resource_to_octane_manager(mesh_name, OctaneResourceType::GEOMETRY);
        need_recreate_mesh = false;
      }
      else {
        need_recreate_mesh = is_octane_geometry_required(
            mesh_name, b_ob.type(), oct_mesh, octane_mesh, mesh_type);
      }
    }
  }
  else {
    need_recreate_mesh = need_update;
  }

  octane_mesh->need_update |= need_update;

  if (!need_update) {
    return octane_mesh;
  }

  if (mesh_synced.find(octane_mesh) != mesh_synced.end()) {
    return octane_mesh;
  }
  mesh_synced.insert(octane_mesh);

  octane_mesh->clear();
  octane_mesh->used_shaders = used_shaders;
  octane_mesh->shaders_tag = Mesh::generate_shader_tag(used_shaders);

  octane_mesh->enable_offset_transform = RNA_boolean_get(&oct_mesh,
                                                         "enable_octane_offset_transform");
  if (octane_mesh->enable_offset_transform) {
    float3 translate, euler, scale;
    int mode = RNA_enum_get(&oct_mesh, "octane_offset_rotation_order");
    RNA_float_get_array(
        &oct_mesh, "octane_offset_translation", reinterpret_cast<float *>(&translate));
    RNA_float_get_array(&oct_mesh, "octane_offset_rotation", reinterpret_cast<float *>(&euler));
    RNA_float_get_array(&oct_mesh, "octane_offset_scale", reinterpret_cast<float *>(&scale));
    octane_mesh->offset_transform = make_transform(translate, euler, mode, scale);
  }

  octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable =
      RNA_boolean_get(&oct_mesh, "open_subd_enable") || use_octane_vertex_displacement_subdvision;
  octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = RNA_enum_get(&oct_mesh,
                                                                               "open_subd_scheme");
  octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = RNA_int_get(&oct_mesh,
                                                                             "open_subd_level");
  octane_mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = RNA_float_get(
      &oct_mesh, "open_subd_sharpness");
  octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp = RNA_enum_get(
      &oct_mesh, "open_subd_bound_interp");
  octane_mesh->octane_mesh.oObjectLayer = object_layer;
  octane_mesh->octane_mesh.bInfinitePlane = RNA_boolean_get(&oct_mesh, "infinite_plane");
  octane_mesh->is_scatter_group_source = RNA_boolean_get(&oct_mesh, "is_scatter_group_source");
  octane_mesh->scatter_group_id = RNA_int_get(&oct_mesh, "scatter_group_id");
  octane_mesh->scatter_instance_id = RNA_int_get(&oct_mesh, "scatter_instance_id");
  if (RNA_boolean_get(&oct_mesh, "use_auto_smooth") &&
      !RNA_boolean_get(&oct_mesh, "force_load_vertex_normals"))
    octane_mesh->octane_mesh.fMaxSmoothAngle = RNA_float_get(&oct_mesh, "auto_smooth_angle") /
                                               M_PI * 180;
  else
    octane_mesh->octane_mesh.fMaxSmoothAngle = -1.0f;
  octane_mesh->octane_mesh.iHairInterpolations = RNA_enum_get(&oct_mesh, "hair_interpolation");
  octane_mesh->final_visibility = !(preview ? b_ob.hide_viewport() : b_ob.hide_render());

  bool bHideOriginalMesh = false;
  if (b_ob.type() == BL::Object::type_MESH) {
    BL::Mesh b_mesh = BL::Mesh(b_ob.data());
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable =
        b_mesh.octane_enable_sphere_attribute();
    bHideOriginalMesh = b_mesh.octane_hide_original_mesh();
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius =
        b_mesh.octane_sphere_radius();
    bool use_randomized_radius = b_mesh.octane_use_randomized_radius();
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed =
        use_randomized_radius ? b_mesh.octane_sphere_randomized_radius_seed() : -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius =
        b_mesh.octane_sphere_randomized_radius_min();
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius =
        b_mesh.octane_sphere_randomized_radius_max();
  }
  else {
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = false;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed = -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius = 0.f;
  }

  bool is_octane_vdb = RNA_boolean_get(&oct_mesh, "is_octane_vdb");
  octane_mesh->is_octane_volume = is_octane_vdb;
  if (is_octane_vdb) {
    int current_frame = b_scene.frame_current();
    octane_mesh->last_vdb_frame = current_frame;
    octane_mesh->octane_volume.sVolumePath = resolve_octane_vdb_path(oct_mesh, b_data, b_scene);
    resolve_volume_attributes(oct_mesh, octane_mesh->octane_volume);
  }

  if (octane_mesh) {
    octane_mesh->subdivision_type = object_subdivision_type(b_ob, preview, true);
  }

  bool use_octane_subdivision = use_octane_vertex_displacement_subdvision ||
                                (octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable &&
                                 octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel > 0);

  if (need_recreate_mesh) {

    BL::Mesh b_mesh = object_to_mesh(b_data,
                                     b_ob,
                                     b_depsgraph,
                                     true,
                                     use_octane_subdivision,
                                     octane_mesh ? octane_mesh->subdivision_type :
                                                   Mesh::SUBDIVISION_NONE);

    if (b_mesh) {
      BL::FluidDomainSettings b_domain = object_fluid_domain_find(b_ob);
      BL::FluidDomainSettings::cache_data_format_NONE;
      bool is_openvdb = b_domain && is_vdb_format(int(b_domain.cache_data_format()));
      if (!is_openvdb || is_octane_vdb) {
        Mesh::WindingOrder winding_order = static_cast<Mesh::WindingOrder>(
            RNA_enum_get(&oct_mesh, "winding_order"));

        if (use_octane_subdivision || octane_mesh->subdivision_type != Mesh::SUBDIVISION_NONE) {
          if (use_octane_vertex_displacement_subdvision) {
            create_subd_mesh(
                scene, b_ob, octane_mesh, b_mesh, octane_mesh->used_shaders, winding_order);
          }
          else if (octane_mesh->subdivision_type == Mesh::SUBDIVISION_NONE) {
            create_mesh(scene,
                        b_ob,
                        octane_mesh,
                        b_mesh,
                        octane_mesh->used_shaders,
                        winding_order,
                        true,
                        false);
          }
          else {
            create_subd_mesh(
                scene, b_ob, octane_mesh, b_mesh, octane_mesh->used_shaders, winding_order);
          }
        }
        else {
          create_mesh(scene, b_ob, octane_mesh, b_mesh, octane_mesh->used_shaders, winding_order);
        }
        if (!octane_mesh->empty) {
          sync_hair(octane_mesh, b_mesh, b_ob, false);
        }
      }
      else {
        create_openvdb_volume(
            b_domain, scene, b_ob, octane_mesh, b_mesh, &oct_mesh, octane_mesh->used_shaders);
        resolve_volume_attributes(oct_mesh, octane_mesh->octane_volume);
        tag_resharpable_candidate(mesh_name);
      }
    }
    else {
      octane_mesh->empty = true;
    }
    if (RNA_boolean_get(&oct_mesh, "external_alembic_mesh_tag")) {
      octane_mesh->empty = true;
	}
    /* mesh fluid motion mantaflow */
    sync_mesh_fluid_motion(b_ob, scene, octane_mesh);
    sync_mesh_particles(b_ob, octane_mesh, !preview);
  }
  else {
    octane_mesh->octane_mesh.oMeshData.bUpdate = false;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.bUpdate = false;
  }

  octane_mesh->octane_mesh.iHairWsSize =
      octane_mesh->octane_mesh.iHairInterpolations ==
              (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ?
          octane_mesh->octane_mesh.oMeshData.f2HairWs.size() :
          0;
  octane_mesh->octane_mesh.iHairInterpolations =
      octane_mesh->octane_mesh.iHairInterpolations ==
              (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_NONE ?
          (int32_t)::Octane::HairInterpolationType::HAIR_INTERP_DEFAULT :
          octane_mesh->octane_mesh.iHairInterpolations;

  if (bHideOriginalMesh && octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable) {
    octane_mesh->octane_mesh.oMeshData.bShowVertexData = false;
  }
  else if (octane_mesh->octane_mesh.oMeshData.f3HairPoints.size()) {
    octane_mesh->octane_mesh.oMeshData.bShowVertexData = show_self;
  }
  else {
    octane_mesh->octane_mesh.oMeshData.bShowVertexData = true;
  }

  octane_mesh->tag_update(scene);
  return octane_mesh;
}

void BlenderSync::sync_mesh_motion(BL::Depsgraph &b_depsgraph,
                                   BL::Object &b_ob,
                                   Object *object,
                                   float motion_time)
{
  /* ensure we only sync instanced meshes once */
  Mesh *mesh = object->mesh;

  if (!mesh || mesh->octane_mesh.oMeshData.iSamplesNum <= 1)
    return;

  if (mesh_motion_synced.find(mesh) != mesh_motion_synced.end())
    return;

  mesh_motion_synced.insert(mesh);

  /* skip objects without deforming modifiers. this is not totally reliable,
   * would need a more extensive check to see which objects are animated */
  BL::Mesh b_mesh(PointerRNA_NULL);

  /* fluid motion is exported immediate with mesh, skip here */
  BL::FluidDomainSettings b_fluid_domain = object_fluid_domain_find(b_ob);
  if (b_fluid_domain)
    return;

  b_mesh = object_to_mesh(b_data, b_ob, b_depsgraph, false, false, Mesh::SUBDIVISION_NONE);

  if (!b_mesh)
    return;

  int base_vert_cnt = mesh->octane_mesh.oMeshData.f3Points.size();

  int vert_cnt = b_mesh.vertices.length();

  float last_valid_motion_time = 0;
  float last_absolute_dt = abs(motion_time);

  // Find the closest motion data
  for (auto it : mesh->octane_mesh.oMeshData.oMotionf3Points) {
    if (it.first * motion_time >= 0) {
      float current_absolute_dt = abs(abs(it.first) - abs(motion_time));
      if (current_absolute_dt < last_absolute_dt) {
        last_absolute_dt = current_absolute_dt;
        last_valid_motion_time = it.first;
      }
    }
  }

  mesh->octane_mesh.oMeshData.oMotionf3Points[motion_time] =
      mesh->octane_mesh.oMeshData.oMotionf3Points[last_valid_motion_time];
  if (base_vert_cnt == vert_cnt) {
    // Create vertices
    unsigned long vert_idx = 0;
    BL::Mesh::vertices_iterator v;
    for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v, ++vert_idx) {
      if (vert_idx >= base_vert_cnt) {
        continue;
      }
      mesh->octane_mesh.oMeshData.oMotionf3Points[motion_time][vert_idx] =
          OctaneDataTransferObject::float_3(v->co()[0], v->co()[1], v->co()[2]);
    }
  }
  else {
    fprintf(
        stderr,
        "Octane: WARNING: Topology differs, discarding motion blur for object %s at time %f!\n",
        b_ob.name_full().c_str(),
        motion_time);
  }

  sync_hair(mesh, b_mesh, b_ob, true, motion_time);

  std::vector<OctaneDataTransferObject::float_3> hairMotionData =
      mesh->octane_mesh.oMeshData.oMotionf3HairPoints[last_valid_motion_time];
  for (int idx = 0; idx < hairMotionData.size(); ++idx) {
    if (idx < mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].size()) {
      hairMotionData[idx] = mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time][idx];
	}
  }
  mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time] = hairMotionData;

  /* free derived mesh */
  free_object_to_mesh(b_data, b_ob, b_mesh);
}

OCT_NAMESPACE_END
