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
#include "render/mesh.h"
#include "render/scene.h"

#include "blender_sync.h"
#include "blender_util.h"

#include "RNA_blender_cpp.h"

OCT_NAMESPACE_BEGIN

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
}

static void create_subd_mesh(Scene *scene,
                             BL::Object &b_ob,
                             Mesh *mesh,
                             BL::Mesh &b_mesh,
                             const std::vector<Shader *> &used_shaders,
                             Mesh::WindingOrder winding_order)
{
  BL::SubsurfModifier subsurf_mod(b_ob.modifiers[b_ob.modifiers.length() - 1]);
  bool subdivide_uvs = subsurf_mod.uv_smooth() != BL::SubsurfModifier::uv_smooth_NONE;

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
static void create_openvdb_volume(BL::SmokeDomainSettings &b_domain,
                                  Scene *scene,
                                  BL::Object b_ob,
                                  Mesh *mesh,
                                  BL::Mesh b_mesh,
                                  PointerRNA *oct_mesh,
                                  const std::vector<Shader *> &used_shaders)
{
  BL::Array<int, 3> res = b_domain.domain_resolution();
  int length, amplify = (b_domain.use_high_resolution()) ? b_domain.amplify() + 1 : 1;

  int width = mesh->vdb_resolution.x = res[0] * amplify;
  int height = mesh->vdb_resolution.y = res[1] * amplify;
  int depth = mesh->vdb_resolution.z = res[2] * amplify;
  int32_t num_pixels = width * height * depth;

  if (num_pixels) {
    mesh->mesh_type = static_cast<Mesh::MeshType>(RNA_enum_get(oct_mesh, "mesh_type"));
    if (mesh->mesh_type == Mesh::GLOBAL)
      mesh->mesh_type = Mesh::SCATTER;

    float *dencity = new float[num_pixels];
    float *flame = new float[num_pixels];
    // float *color = new float[num_pixels * 4];

    int grid_offset = 0;

    SmokeDomainSettings_density_grid_get_length(&b_domain.ptr, &length);
    if (length == num_pixels) {
      SmokeDomainSettings_density_grid_get(&b_domain.ptr, (float *)dencity);
      mesh->vdb_absorption_offset = grid_offset++;
      mesh->vdb_scatter_offset = mesh->vdb_absorption_offset;
    }
    /* this is in range 0..1, and interpreted by the OpenGL smoke viewer
     * as 1500..3000 K with the first part faded to zero density */
    SmokeDomainSettings_flame_grid_get_length(&b_domain.ptr, &length);
    if (length == num_pixels) {
      SmokeDomainSettings_flame_grid_get(&b_domain.ptr, (float *)flame);
      mesh->vdb_emission_offset = grid_offset++;
    }
    /* the RGB is "premultiplied" by density for better interpolation results */
    // SmokeDomainSettings_color_grid_get_length(&b_domain.ptr, &length);
    // if(length == num_pixels * 4) {
    //    SmokeDomainSettings_color_grid_get(&b_domain.ptr, (float*)color);
    //    mesh->vdb_emission_offset = grid_offset++;
    //}

    if (grid_offset > 0) {
      mesh->vdb_iso = RNA_float_get(oct_mesh, "vdb_iso");
      mesh->vdb_absorption_scale = RNA_float_get(oct_mesh, "vdb_abs_scale");
      mesh->vdb_emission_scale = RNA_float_get(oct_mesh, "vdb_emiss_scale");
      mesh->vdb_scatter_scale = RNA_float_get(oct_mesh, "vdb_scatter_scale");
      mesh->vdb_velocity_scale = RNA_float_get(oct_mesh, "vdb_vel_scale");
      mesh->vdb_sdf = RNA_boolean_get(oct_mesh, "vdb_sdf");

      mesh->vdb_regular_grid = new float[num_pixels * grid_offset];
      mesh->vdb_grid_size = num_pixels * grid_offset;
      mesh->vdb_resolution.x = width;
      mesh->vdb_resolution.y = height;
      mesh->vdb_resolution.z = depth;

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

        mesh->vdb_grid_matrix.m[0] = {
            (max_bound.x - min_bound.x) / width, 0.0f, 0.0f, min_bound.x};
        mesh->vdb_grid_matrix.m[1] = {
            0.0f, (max_bound.y - min_bound.y) / height, 0.0f, min_bound.y};
        mesh->vdb_grid_matrix.m[2] = {
            0.0f, 0.0f, (max_bound.z - min_bound.z) / depth, min_bound.z};
      }
      else {
        mesh->vdb_grid_matrix.m[0] = {0.0f, 0.0f, 0.0f, 0.0f};
        mesh->vdb_grid_matrix.m[1] = {0.0f, 0.0f, 0.0f, 0.0f};
        mesh->vdb_grid_matrix.m[2] = {0.0f, 0.0f, 0.0f, 0.0f};
      }

      for (int i = 0; i < num_pixels; ++i) {
        register int index = i * grid_offset;
        if (mesh->vdb_absorption_offset >= 0)
          mesh->vdb_regular_grid[index + mesh->vdb_absorption_offset] = dencity[i];
        // if(mesh->vdb_scatter_offset >= 0)       mesh->vdb_regular_grid[index +
        // mesh->vdb_scatter_offset]    = dencity[i];
        if (mesh->vdb_emission_offset >= 0)
          mesh->vdb_regular_grid[index + mesh->vdb_emission_offset] = flame[i];
      }
    }
    delete[] dencity;
    delete[] flame;
    // delete[] color;
  }
  else {
    if (!mesh->empty)
      mesh->empty = true;
    fprintf(stderr, "Octane: The vdb volume \"%s\" is empty\n", b_ob.data().name().c_str());
  }
}  // create_openvdb_volume()

Mesh *BlenderSync::sync_mesh(BL::Depsgraph &b_depsgraph,
                             BL::Object &b_ob,
                             BL::Object &b_ob_instance,
                             bool object_updated,
                             bool show_self,
                             bool show_particles,
                             OctaneDataTransferObject::OctaneObjectLayer &object_layer)
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

  Mesh *octane_mesh;
  PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");
  Mesh::MeshType mesh_type = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_mesh, "mesh_type"));

  std::string mesh_name = resolve_octane_name(
      b_ob_data, BKE_object_is_modified(b_ob) ? b_ob.name() : "", MESH_TAG);

  bool is_mesh_data_cached = false;
  bool octane_enable_mesh_upload_opt = false;
  bool is_mesh_data_updated = !octane_enable_mesh_upload_opt || !is_mesh_data_cached;

  bool is_recalculated = mesh_map.sync(&octane_mesh, key);

  if (is_recalculated &&
      (scene->meshes_type == Mesh::RESHAPABLE_PROXY || mesh_type == Mesh::RESHAPABLE_PROXY)) {
    is_mesh_data_updated = true;
  }

  bool octane_vdb_force_update_flag = RNA_boolean_get(&oct_mesh, "octane_vdb_helper") &&
                                      octane_mesh &&
                                      octane_mesh->last_vdb_frame != b_scene.frame_current();

  if (!octane_vdb_force_update_flag && !is_recalculated) {
    return octane_mesh;
  }

  if (mesh_synced.find(octane_mesh) != mesh_synced.end())
    return octane_mesh;
  mesh_synced.insert(octane_mesh);

  octane_mesh->clear();
  octane_mesh->used_shaders = used_shaders;

  octane_mesh->nice_name = mesh_name;
  octane_mesh->name = mesh_name;
  octane_mesh->octane_mesh.sMeshName = mesh_name;
  octane_mesh->mesh_type = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_mesh, "mesh_type"));
  octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable = RNA_boolean_get(
      &oct_mesh, "open_subd_enable");
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

  PointerRNA octane_geo_node_collections = RNA_pointer_get(&oct_mesh,
                                                           "octane_geo_node_collections");
  char scriptGeoMaterialName[512];
  char scriptGeoNodeName[512];
  RNA_string_get(&octane_geo_node_collections, "node_graph_tree", scriptGeoMaterialName);
  RNA_string_get(&octane_geo_node_collections, "osl_geo_node", scriptGeoNodeName);
  std::string scriptGeoMaterialNameStr(scriptGeoMaterialName);
  std::string scriptGeoNodeNameStr(scriptGeoNodeName);
  if (scriptGeoMaterialNameStr.size() && scriptGeoNodeNameStr.size()) {
    octane_mesh->octane_mesh.sScriptGeoName = scriptGeoMaterialNameStr + "_" +
                                              scriptGeoNodeNameStr;
  }
  else {
    octane_mesh->octane_mesh.sScriptGeoName = "";
  }

  char orbxFilePath[512];
  RNA_string_get(&oct_mesh, "imported_orbx_file_path", orbxFilePath);
  std::string orbxFilePathStr(orbxFilePath);
  if (orbxFilePathStr.size()) {
    octane_mesh->octane_mesh.sOrbxPath = blender_absolute_path(b_data, b_scene, orbxFilePath);
  }
  else {
    octane_mesh->octane_mesh.sOrbxPath = "";
  }

  bool is_octane_vdb = RNA_boolean_get(&oct_mesh, "is_octane_vdb");
  octane_mesh->is_octane_volume = is_octane_vdb;
  if (is_octane_vdb) {
    int current_frame = b_scene.frame_current();
    octane_mesh->last_vdb_frame = current_frame;
    int start_playing_at = RNA_int_get(&oct_mesh, "openvdb_frame_start_playing_at");
    int current_frame_for_vdb = std::max(0, current_frame - start_playing_at);
    int start_frame = RNA_int_get(&oct_mesh, "openvdb_frame_start");
    int end_frame = RNA_int_get(&oct_mesh, "openvdb_frame_end");
    float openvdb_frame_speed_mutiplier = RNA_float_get(&oct_mesh,
                                                        "openvdb_frame_speed_mutiplier");
    char vdbFilePath[512];
    RNA_string_get(&oct_mesh, "imported_openvdb_file_path", vdbFilePath);
    std::string vdbFileStr(vdbFilePath);
    std::size_t pos = vdbFileStr.find("F$");
    if (pos != std::string::npos) {
      int target_frame = std::min(
          int(start_frame + current_frame_for_vdb * openvdb_frame_speed_mutiplier), end_frame);
      if (vdbFileStr.find("$F$") != std::string::npos) {
        vdbFileStr = vdbFileStr.substr(0, pos - 1) + std::to_string(target_frame) +
                     vdbFileStr.substr(pos + 2);
      }
      else {
        std::string format_tmp = "%0";
        format_tmp += vdbFileStr[pos - 1];
        format_tmp += "d";
        char buffer[256];
        sprintf(buffer, format_tmp.c_str(), target_frame);
        vdbFileStr = vdbFileStr.substr(0, pos - 2) + std::string(buffer) +
                     vdbFileStr.substr(pos + 2);
      }
    }
    octane_mesh->vdb_file_path = blender_absolute_path(b_data, b_scene, vdbFileStr);
    octane_mesh->vdb_iso = RNA_float_get(&oct_mesh, "vdb_iso");
    octane_mesh->vdb_absorption_scale = RNA_float_get(&oct_mesh, "vdb_abs_scale");
    octane_mesh->vdb_emission_scale = RNA_float_get(&oct_mesh, "vdb_emiss_scale");
    octane_mesh->vdb_scatter_scale = RNA_float_get(&oct_mesh, "vdb_scatter_scale");
    octane_mesh->vdb_velocity_scale = RNA_float_get(&oct_mesh, "vdb_vel_scale");
    octane_mesh->vdb_sdf = RNA_boolean_get(&oct_mesh, "vdb_sdf");
  }

  if (octane_mesh) {
    octane_mesh->subdivision_type = object_subdivision_type(b_ob, preview, true);
  }

  bool use_octane_subdivision = octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable &&
                                octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel > 0;

  if (is_mesh_data_updated) {

    BL::Mesh b_mesh = object_to_mesh(b_data,
                                     b_ob,
                                     b_depsgraph,
                                     true,
                                     use_octane_subdivision,
                                     octane_mesh ? octane_mesh->subdivision_type :
                                                   Mesh::SUBDIVISION_NONE);

    if (b_mesh) {
      BL::SmokeDomainSettings b_domain = object_smoke_domain_find(b_ob);
      bool is_openvdb = b_domain && b_domain.cache_file_format() ==
                                        BL::SmokeDomainSettings::cache_file_format_OPENVDB;
      if (!is_openvdb || is_octane_vdb) {
        Mesh::WindingOrder winding_order = static_cast<Mesh::WindingOrder>(
            RNA_enum_get(&oct_mesh, "winding_order"));

        if (use_octane_subdivision || octane_mesh->subdivision_type != Mesh::SUBDIVISION_NONE) {
          if (octane_mesh->subdivision_type == Mesh::SUBDIVISION_NONE) {
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
        if (!octane_mesh->empty)
          sync_hair(octane_mesh, b_mesh, b_ob, false);
      }
      else {
        create_openvdb_volume(
            b_domain, scene, b_ob, octane_mesh, b_mesh, &oct_mesh, octane_mesh->used_shaders);
      }
    }
    else
      octane_mesh->empty = true;
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
  BL::DomainFluidSettings b_fluid_domain = object_fluid_domain_find(b_ob);
  if (b_fluid_domain)
    return;

  b_mesh = object_to_mesh(b_data, b_ob, b_depsgraph, false, false, Mesh::SUBDIVISION_NONE);

  if (!b_mesh)
    return;

  int vert_cnt = b_mesh.vertices.length();

  mesh->octane_mesh.oMeshData.oMotionf3Points[motion_time].resize(vert_cnt);
  // Create vertices
  unsigned long vert_idx = 0;
  BL::Mesh::vertices_iterator v;
  for (b_mesh.vertices.begin(v); v != b_mesh.vertices.end(); ++v, ++vert_idx) {
    mesh->octane_mesh.oMeshData.oMotionf3Points[motion_time][vert_idx] =
        OctaneDataTransferObject::float_3(v->co()[0], v->co()[1], v->co()[2]);
  }

  /* free derived mesh */
  free_object_to_mesh(b_data, b_ob, b_mesh);
}

OCT_NAMESPACE_END
