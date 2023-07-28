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
#include "DNA_curve_types.h"
#include "DNA_curves_types.h"

#include "BKE_curve_legacy_convert.hh"
#include "BKE_curves.hh"

#include "render/graph.h"
#include "render/mesh.h"
#include "render/scene.h"

#include "blender_sync.h"
#include "blender_util.h"

#include <openvdb/Grid.h>
#include <openvdb/io/Stream.h>
#include <openvdb/openvdb.h>
#include <openvdb/tools/Dense.h>
#include <openvdb/tools/GridTransformer.h>
#include <openvdb/tools/Morphology.h>

#include <chrono>
#include <fstream>
#include <iostream>

openvdb::GridBase::ConstPtr BKE_volume_grid_openvdb_for_read(const struct Volume *volume,
                                                             const struct VolumeGrid *grid);

#include "RNA_blender_cpp.h"

OCT_NAMESPACE_BEGIN

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

static void create_curve_hair(Scene *scene,
                              BL::Depsgraph &b_depsgraph,
                              BL::Object &b_ob,
                              Mesh *mesh,
                              PointerRNA &oct_mesh,
                              const std::vector<Shader *> &used_shaders,                              
                              bool motion,
                              float motion_time)
{
  // BL::Curve b_curve = BL::Curve(b_ob.data());
  BL::Curve b_curve = b_ob.to_curve(b_depsgraph, true);
  int hair_num = b_curve.splines.length();
  if (hair_num == 0) {
    mesh->octane_mesh.oMeshData.Clear();
    mesh->octane_mesh.oMeshData.iSamplesNum = 1;
    mesh->empty = true;
    return;
  }
  float root_width = get_float(oct_mesh, "hair_root_width");
  float tip_width = get_float(oct_mesh, "hair_tip_width");
  if (!motion) {
    mesh->empty = false;
    mesh->octane_mesh.oMeshData.iSamplesNum = 1;
    mesh->octane_mesh.oMeshData.f3HairPoints.clear();
    mesh->octane_mesh.oMeshData.iVertexPerHair.clear();
    mesh->octane_mesh.oMeshData.fHairThickness.clear();
    mesh->octane_mesh.oMeshData.iHairMaterialIndices.clear();
  }
  else {
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].clear();
  }
  ::Curve *curve = (::Curve *)b_curve.ptr.data;
  if (curve && curve->curve_eval) {
    Curves *curves_id = blender::bke::curve_legacy_to_curves(*curve);
    blender::bke::CurvesGeometry &curves = curves_id->geometry.wrap();
    const blender::Span<blender::float3> positions = curves.evaluated_positions();
    auto offsets = curves.evaluated_points_by_curve();
    for (int32_t i = 0; i < curves.curves_num(); ++i) {      
      const auto index_range = offsets[i];
      float cur_thickness = root_width;
      size_t step_num = index_range.size();
      float thickness_step = step_num > 1 ? (tip_width - root_width) / (step_num - 1) : 0;
      if (!motion) {
        for (size_t j = 0; j < step_num; ++j) {
          size_t k = j + index_range.start();
          float3 cur_point = make_float3(positions[k][0], positions[k][1], positions[k][2]);
          mesh->octane_mesh.oMeshData.f3HairPoints.push_back(
              OctaneDataTransferObject::float_3(cur_point.x, cur_point.y, cur_point.z));
          mesh->octane_mesh.oMeshData.fHairThickness.push_back(cur_thickness);
          cur_thickness += thickness_step;
        }
        mesh->octane_mesh.oMeshData.iVertexPerHair.push_back(step_num);
        int shader_idx = b_curve.splines[0].material_index() - 1;
        int shader = clamp(shader_idx, 0, used_shaders.size() - 1);
        mesh->octane_mesh.oMeshData.iHairMaterialIndices.push_back(shader);
      }
      else {
        if (step_num == mesh->octane_mesh.oMeshData.iVertexPerHair[i]) {
          for (size_t j = 0; j < step_num; ++j) {
            size_t k = j + index_range.start();
            float3 cur_point = make_float3(positions[k][0], positions[k][1], positions[k][2]);
            mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].push_back(
                OctaneDataTransferObject::float_3(cur_point.x, cur_point.y, cur_point.z));
          }
        }
        else {
          mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time] =
              mesh->octane_mesh.oMeshData.f3HairPoints;
        }
      }
    }
  }
  else {
    BL::Curve::splines_iterator s;
    int32_t i = 0;
    for (b_curve.splines.begin(s); s != b_curve.splines.end(); ++s, ++i) {
      float cur_thickness = root_width;
      size_t step_num = s->points.length();
      float thickness_step = step_num > 1 ? (tip_width - root_width) / (step_num - 1) : 0;
      if (!motion) {
        for (size_t step = 0; step < step_num; ++step) {
          const BL::Array<float, 4> array = s->points[step].co();
          float3 cur_point = make_float3(array[0], array[1], array[2]);
          mesh->octane_mesh.oMeshData.f3HairPoints.push_back(
              OctaneDataTransferObject::float_3(cur_point.x, cur_point.y, cur_point.z));
          mesh->octane_mesh.oMeshData.fHairThickness.push_back(cur_thickness);
          cur_thickness += thickness_step;
        }
        mesh->octane_mesh.oMeshData.iVertexPerHair.push_back(step_num);
        int shader = clamp(s->material_index() - 1, 0, used_shaders.size() - 1);
        mesh->octane_mesh.oMeshData.iHairMaterialIndices.push_back(shader);
      }
      else {
        if (step_num == mesh->octane_mesh.oMeshData.iVertexPerHair[i]) {
          for (size_t step = 0; step < step_num; ++step) {
            const BL::Array<float, 4> array = s->points[step].co();
            float3 cur_point = make_float3(array[0], array[1], array[2]);
            mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].push_back(
                OctaneDataTransferObject::float_3(cur_point.x, cur_point.y, cur_point.z));
          }
        }
        else {
          mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time] =
              mesh->octane_mesh.oMeshData.f3HairPoints;
        }
      }
    }
  }
  mesh->octane_mesh.oMeshData.bShowVertexData = false;
  mesh->octane_mesh.oMeshData.bUpdate = true;
  if (!motion) {
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[0] = mesh->octane_mesh.oMeshData.f3HairPoints;
  }
  if (b_ob.data().ptr.data != b_curve.ptr.data) {
    b_ob.to_curve_clear();
  }
}

static std::optional<BL::FloatAttribute> find_curves_radius_attribute(BL::Curves b_curves)
{
  for (BL::Attribute &b_attribute : b_curves.attributes) {
    if (b_attribute.name() != "radius") {
      continue;
    }
    if (b_attribute.domain() != BL::Attribute::domain_POINT) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_FLOAT) {
      continue;
    }
    return BL::FloatAttribute{b_attribute};
  }
  return std::nullopt;
}

static BL::FloatVectorAttribute find_curves_position_attribute(BL::Curves b_curves)
{
  for (BL::Attribute &b_attribute : b_curves.attributes) {
    if (b_attribute.name() != "position") {
      continue;
    }
    if (b_attribute.domain() != BL::Attribute::domain_POINT) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_FLOAT_VECTOR) {
      continue;
    }
    return BL::FloatVectorAttribute{b_attribute};
  }
  /* The position attribute must exist. */
  assert(false);
  return BL::FloatVectorAttribute{b_curves.attributes[0]};
}

static std::optional<BL::Float2Attribute> find_curves_uv_attribute(BL::Curves b_curves)
{
  for (BL::Attribute &b_attribute : b_curves.attributes) {
    if (b_attribute.name() != "surface_uv_coordinate") {
      continue;
    }
    if (b_attribute.domain() != BL::Attribute::domain_CURVE) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_FLOAT2) {
      continue;
    }
    return BL::Float2Attribute{b_attribute};
  }
  return std::nullopt;
}

static std::optional<BL::FloatColorAttribute> find_vertex_color_float_color_attribute(
    BL::Mesh b_mesh)
{
  for (BL::Attribute &b_attribute : b_mesh.attributes) {
    if (b_attribute.domain() != BL::Attribute::domain_POINT) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_FLOAT_COLOR) {
      continue;
    }
    return BL::FloatColorAttribute{b_attribute};
  }
  return std::nullopt;
}

static std::optional<BL::ByteColorAttribute> find_vertex_color_byte_color_attribute(
    BL::Mesh b_mesh)
{
  for (BL::Attribute &b_attribute : b_mesh.attributes) {
    if (b_attribute.domain() != BL::Attribute::domain_POINT) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_BYTE_COLOR) {
      continue;
    }
    return BL::ByteColorAttribute{b_attribute};
  }
  return std::nullopt;
}

static float4 hair_point_as_float4(BL::FloatVectorAttribute b_attr_position,
                                   std::optional<BL::FloatAttribute> b_attr_radius,
                                   const int index)
{
  float4 mP = float3_to_float4(get_float3(b_attr_position.data[index].vector()));
  mP.w = b_attr_radius ? b_attr_radius->data[index].value() : 0.005f;
  return mP;
}

static float4 interpolate_hair_points(BL::FloatVectorAttribute b_attr_position,
                                      std::optional<BL::FloatAttribute> b_attr_radius,
                                      const int first_point_index,
                                      const int num_points,
                                      const float step)
{
  const float curve_t = step * (num_points - 1);
  const int point_a = clamp((int)curve_t, 0, num_points - 1);
  const int point_b = min(point_a + 1, num_points - 1);
  const float t = curve_t - (float)point_a;
  return lerp(hair_point_as_float4(b_attr_position, b_attr_radius, first_point_index + point_a),
              hair_point_as_float4(b_attr_position, b_attr_radius, first_point_index + point_b),
              t);
}

static void create_curves_hair(
    Scene *scene, BL::Object &b_ob, Mesh *mesh, bool motion, float motion_time)
{
  if (b_ob.type() != BL::Object::type_CURVES) {
    return;
  }
  BL::Curves b_curves(b_ob.data());
  const int num_keys = b_curves.points.length();
  const int num_curves = b_curves.curves.length();
  BL::ID b_ob_data = b_ob.data();
  PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");
  bool use_octane_radius_setting = false;
  float octane_root_radius = 0.005f, octane_tip_radius = 0.005f;
  if (oct_mesh.data != NULL) {
    use_octane_radius_setting = get_boolean(oct_mesh, "use_octane_radius_setting");
    octane_root_radius = get_float(oct_mesh, "hair_root_width");
    octane_tip_radius = get_float(oct_mesh, "hair_tip_width");
  }
  if (!motion) {
    mesh->empty = false;
    mesh->octane_mesh.oMeshData.iSamplesNum = 1;
    mesh->octane_mesh.oMeshData.f3HairPoints.resize(num_keys);
    mesh->octane_mesh.oMeshData.iVertexPerHair.resize(num_curves);
    mesh->octane_mesh.oMeshData.fHairThickness.resize(num_keys);
    mesh->octane_mesh.oMeshData.iHairMaterialIndices.resize(num_curves);
  }
  else {
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time].resize(
        mesh->octane_mesh.oMeshData.f3HairPoints.size());
  }
  BL::FloatVectorAttribute b_attr_position = find_curves_position_attribute(b_curves);
  std::optional<BL::FloatAttribute> b_attr_radius = find_curves_radius_attribute(b_curves);
  std::optional<BL::Float2Attribute> b_attr_uv = find_curves_uv_attribute(b_curves);
  if (b_attr_uv) {
    if (!motion) {
      mesh->octane_mesh.oMeshData.f2HairUVs.resize(num_curves);
    }
  }
  /* Export curves and points. */
  size_t motion_blur_first_point_index = 0;
  for (int i = 0; i < num_curves; i++) {
    const int first_point_index = b_curves.curve_offset_data[i].value();
    const int num_points = b_curves.curve_offset_data[i + 1].value() - first_point_index;
    /* Position and radius. */
    if (!motion) {
      float octane_radius = octane_root_radius;
      float radius_step = num_points > 1 ?
                              (octane_tip_radius - octane_root_radius) / (num_points - 1) :
                              0;
      for (int j = 0; j < num_points; j++) {
        const int point_offset = first_point_index + j;
        const float3 co = get_float3(b_attr_position.data[point_offset].vector());
        float radius = b_attr_radius ? b_attr_radius->data[point_offset].value() : 0.005f;
        mesh->octane_mesh.oMeshData.f3HairPoints[point_offset] = OctaneDataTransferObject::float_3(
            co.x, co.y, co.z);
        mesh->octane_mesh.oMeshData.fHairThickness[point_offset] = use_octane_radius_setting ?
                                                                       octane_radius :
                                                                       radius;
        octane_radius += radius_step;
      }
      if (b_attr_uv) {
        const float2 uv = get_float2(b_attr_uv->data[i].vector());
        mesh->octane_mesh.oMeshData.f2HairUVs[i] = OctaneDataTransferObject::float_2(uv.x, uv.y);
      }
      mesh->octane_mesh.oMeshData.iVertexPerHair[i] = num_points;
      mesh->octane_mesh.oMeshData.iHairMaterialIndices[i] = 0;
    }
    else {
      if (num_points == mesh->octane_mesh.oMeshData.iVertexPerHair[i]) {
        for (int j = 0; j < num_points; j++) {
          const int point_offset = first_point_index + j;
          const int motion_blur_point_offset = motion_blur_first_point_index + j;
          const float3 co = get_float3(b_attr_position.data[point_offset].vector());
          mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time][motion_blur_point_offset] =
              OctaneDataTransferObject::float_3(co.x, co.y, co.z);
        }
      }
      else {
        /* Number of keys has changed. Generate an interpolated version
         * to preserve motion blur. */
        const int num_keys = mesh->octane_mesh.oMeshData.iVertexPerHair[i];
        const float step_size = num_keys > 1 ? 1.0f / (num_keys - 1) : 0.0f;
        for (int j = 0; j < num_keys; j++) {
          const float step = j * step_size;
          const int motion_blur_point_offset = motion_blur_first_point_index + j;
          const float4 lerp_data = interpolate_hair_points(
              b_attr_position, b_attr_radius, first_point_index, num_points, step);
          mesh->octane_mesh.oMeshData.oMotionf3HairPoints[motion_time][motion_blur_point_offset] =
              OctaneDataTransferObject::float_3(lerp_data.x, lerp_data.y, lerp_data.z);
        }
      }
      motion_blur_first_point_index += mesh->octane_mesh.oMeshData.iVertexPerHair[i];
    }
  }
  if (!motion) {
    mesh->octane_mesh.oMeshData.bShowVertexData = false;
    mesh->octane_mesh.oMeshData.bUpdate = true;
    mesh->octane_mesh.oMeshData.oMotionf3HairPoints[0] = mesh->octane_mesh.oMeshData.f3HairPoints;
  }
}

static std::optional<BL::IntAttribute> find_material_index_attribute(BL::Mesh b_mesh)
{
  for (BL::Attribute &b_attribute : b_mesh.attributes) {
    if (b_attribute.domain() != BL::Attribute::domain_FACE) {
      continue;
    }
    if (b_attribute.data_type() != BL::Attribute::data_type_INT) {
      continue;
    }
    if (b_attribute.name() != "material_index") {
      continue;
    }
    return BL::IntAttribute{b_attribute};
  }
  return std::nullopt;
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
  bool use_octane_coordinate = mesh->is_octane_coordinate_used();
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
      mesh->octane_mesh.oMeshData.f3SphereCenters.push_back(
          get_octane_float3(v->co(), use_octane_coordinate));
    }
    return;
  }

  if (numverts == 0 || numfaces == 0) {
    mesh->octane_mesh.oMeshData.Clear();
    mesh->octane_mesh.oMeshData.iSamplesNum = 1;
    mesh->octane_mesh.oMeshData.bUpdate = true;
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
    mesh->octane_mesh.oMeshData.f3Points.push_back(
        get_octane_float3(v->co(), use_octane_coordinate));
    mesh->octane_mesh.oMeshData.f3Normals.push_back(
        get_octane_float3(v->normal(), use_octane_coordinate));
  }
  mesh->octane_mesh.oMeshData.oMotionf3Points[0] = mesh->octane_mesh.oMeshData.f3Points;

  std::optional<BL::IntAttribute> material_indices = find_material_index_attribute(b_mesh);
  auto get_material_index = [&](const int poly_index) -> int {
    if (material_indices) {
      return clamp(material_indices->data[poly_index].value(), 0, used_shaders.size() - 1);
    }
    return 0;
  };

  /* create faces */
  const MPoly *polys = static_cast<const MPoly *>(b_mesh.polygons[0].ptr.data);
  if (!subdivision) {
    vector<int> vi3;
    vi3.resize(3);
    for (BL::MeshLoopTriangle &t : b_mesh.loop_triangles) {
      const int poly_index = t.polygon_index();
      const MPoly &b_poly = polys[poly_index];

      int3 vi = get_int3(t.vertices());
      for (int i = 0; i < 3; ++i) {
        vi3[i] = vi[i];
      }

      int shader = get_material_index(poly_index);
      bool smooth = (b_poly.flag & ME_SMOOTH) || use_loop_normals;

      if (use_loop_normals) {
        BL::Array<float, 9> loop_normals = t.split_normals();
        for (int i = 0; i < 3; i++) {
          if (use_octane_coordinate) {
            mesh->octane_mesh.oMeshData.f3Normals[vi[i]] = OctaneDataTransferObject::float_3(
                loop_normals[i * 3], loop_normals[i * 3 + 2], -loop_normals[i * 3 + 1]);
          }
          else {
            mesh->octane_mesh.oMeshData.f3Normals[vi[i]] = OctaneDataTransferObject::float_3(
                loop_normals[i * 3], loop_normals[i * 3 + 1], loop_normals[i * 3 + 2]);
          }
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
    const MLoop *loops = static_cast<const MLoop *>(b_mesh.loops[0].ptr.data);
    vector<int> vi;

    for (int i = 0; i < numfaces; i++) {
      const MPoly &b_poly = polys[i];
      int n = b_poly.totloop;
      int shader = get_material_index(i);
      bool smooth = (b_poly.flag & ME_SMOOTH) || use_loop_normals;

      vi.resize(n);
      for (int i = 0; i < n; i++) {
        /* NOTE: Autosmooth is already taken care about. */
        vi[i] = loops[b_poly.loopstart + i].v;
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
  int vertex_colors_count = std::min(MAX_OCTANE_COLOR_VERTEX_SETS,
                                     b_mesh.color_attributes.length());
  int tessface_vertex_colors_count = b_mesh.color_attributes.length();
  int inactive_count = MAX_OCTANE_COLOR_VERTEX_SETS - 1;
  std::string active_color_name = b_mesh.attributes.active_color_name();
  BL::Mesh::color_attributes_iterator l;
  for (b_mesh.color_attributes.begin(l); l != b_mesh.color_attributes.end(); ++l) {
    bool active_render = (l->name() == active_color_name);
    if (inactive_count == 0 && !active_render) {
      continue;
    }
    if (l->domain() != BL::Attribute::domain_POINT) {
      continue;
    }
    if (!active_render) {
      inactive_count--;
    }
    mesh->octane_mesh.oMeshData.sVertexColorNames.emplace_back(l->name());
    mesh->octane_mesh.oMeshData.f3VertexColors.emplace_back(
        std::vector<OctaneDataTransferObject::float_3>());
    std::vector<OctaneDataTransferObject::float_3> &colorVertex =
        mesh->octane_mesh.oMeshData
            .f3VertexColors[mesh->octane_mesh.oMeshData.f3VertexColors.size() - 1];
    std::vector<int32_t> &iPointIndices = mesh->octane_mesh.oMeshData.iPointIndices;
    colorVertex.resize(numverts);
    std::optional<BL::FloatColorAttribute> b_attr_float_color;
    std::optional<BL::ByteColorAttribute> b_attr_byte_color;
    BL::Attribute::data_type_enum data_type = l->data_type();
    size_t data_size;
    if (data_type == BL::Attribute::data_type_FLOAT_COLOR) {
      b_attr_float_color = BL::FloatColorAttribute(*l);
      data_size = b_attr_float_color->data.length();
    }
    else if (data_type == BL::Attribute::data_type_BYTE_COLOR) {
      b_attr_byte_color = BL::ByteColorAttribute(*l);
      data_size = b_attr_byte_color->data.length();
    }
    size_t currentPointIdx = 0;
    if (!subdivision) {
      BL::Mesh::loop_triangles_iterator t;
      for (b_mesh.loop_triangles.begin(t); t != b_mesh.loop_triangles.end(); ++t) {
        int3 li = get_int3(t->loops());
        for (int j = 0, k = 2; j < 3; ++j, --k) {
          int indices_idx = li[winding_order == Mesh::CLOCKWISE ? j : k];
          int vertices_idx = iPointIndices[currentPointIdx++];
          if (data_type == BL::Attribute::data_type_FLOAT_COLOR) {
            colorVertex[vertices_idx] = get_octane_float3(
                b_attr_float_color->data[vertices_idx].color());
          }
          else if (data_type == BL::Attribute::data_type_BYTE_COLOR) {
            colorVertex[vertices_idx] = get_octane_float3(
                b_attr_byte_color->data[vertices_idx].color());
          }
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
          if (data_type == BL::Attribute::data_type_FLOAT_COLOR) {
            colorVertex[vertices_idx] = get_octane_float3(
                b_attr_float_color->data[vertices_idx].color());
          }
          else if (data_type == BL::Attribute::data_type_BYTE_COLOR) {
            colorVertex[vertices_idx] = get_octane_float3(
                b_attr_byte_color->data[vertices_idx].color());
          }
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
      if (i < mesh->octane_mesh.oMeshData.f3UVs.size()) {
        mesh->octane_mesh.oMeshData.f2SphereUVs[j].x = mesh->octane_mesh.oMeshData.f3UVs[i].x;
        mesh->octane_mesh.oMeshData.f2SphereUVs[j].y = mesh->octane_mesh.oMeshData.f3UVs[i].y;
      }
      else {
        mesh->octane_mesh.oMeshData.f2SphereUVs[j].x = 0;
        mesh->octane_mesh.oMeshData.f2SphereUVs[j].y = 0;
      }
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
        int index = i * grid_offset;
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
    if (!mesh->empty) {
      mesh->octane_mesh.oMeshData.Clear();
      mesh->octane_mesh.oMeshData.iSamplesNum = 1;
      mesh->empty = true;
      fprintf(stderr, "Octane: The vdb volume \"%s\" is empty\n", b_ob.data().name().c_str());
    }
  }
}  // create_openvdb_volume()

static void sync_mesh_fluid_motion(BL::Object &b_ob, Scene *scene, BL::Mesh &b_mesh, Mesh *mesh)
{
  bool use_octane_transform = false;
  static const ustring u_velocity("velocity");
  for (BL::Attribute &b_attribute : b_mesh.attributes) {
    const ustring name{b_attribute.name().c_str()};
    if (name == u_velocity) {
      BL::FloatVectorAttribute b_vector_attribute(b_attribute);
      if (mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable) {
        mesh->octane_mesh.oMeshData.f3SphereSpeeds.resize(
            mesh->octane_mesh.oMeshData.f3SphereCenters.size());
        for (int i = 0; i < mesh->octane_mesh.oMeshData.f3SphereSpeeds.size(); i++) {
          mesh->octane_mesh.oMeshData.f3SphereSpeeds[i] = get_octane_float3(
              b_vector_attribute.data[i].vector(), use_octane_transform);
        }
      }
      else {
        mesh->octane_mesh.oMeshData.f3Velocities.resize(
            mesh->octane_mesh.oMeshData.f3Points.size());
        for (int i = 0; i < mesh->octane_mesh.oMeshData.f3Velocities.size(); i++) {
          mesh->octane_mesh.oMeshData.f3Velocities[i] = get_octane_float3(
              b_vector_attribute.data[i].vector(), use_octane_transform);
        }
      }
      break;
    }
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

void BlenderSync::find_used_shaders(BL::Object &b_ob,
                                    std::vector<Shader *> &used_shaders,
                                    bool &use_octane_vertex_displacement_subdvision,
                                    bool &use_default_shader)
{
  BL::Material material_override = view_layer.material_override;
  BL::Object::material_slots_iterator slot;
  for (b_ob.material_slots.begin(slot); slot != b_ob.material_slots.end(); ++slot) {
    if (material_override) {
      find_shader(material_override, used_shaders, scene->default_surface);
    }
    else {
      BL::ID b_material(slot->material());
      find_shader(b_material, used_shaders, scene->default_surface);
    }
    use_default_shader = false;
  }

  if (used_shaders.size() == 0) {
    use_default_shader = true;
    if (material_override)
      find_shader(material_override, used_shaders, scene->default_surface);
    else
      used_shaders.push_back(scene->default_surface);
  }

  for (auto used_shader : used_shaders) {
    if (used_shader->graph && used_shader->need_update_paint) {
      used_shader->need_update_paint = false;
    }
  }

  for (auto used_shader : used_shaders) {
    if (used_shader->graph && used_shader->graph->need_subdivision) {
      use_octane_vertex_displacement_subdvision = true;
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
  bool is_instance = (b_ob == b_ob_instance);
  BL::ID key = (BKE_object_is_modified(b_ob) && !is_instance) ? b_ob_data : b_ob_instance;
  bool is_edit_mode_modified = false;
  /* find shader indices */
  std::vector<Shader *> used_shaders;
  bool use_octane_vertex_displacement_subdvision = false;
  bool use_default_shader = false;
  find_used_shaders(
      b_ob, used_shaders, use_octane_vertex_displacement_subdvision, use_default_shader);

  Mesh *octane_mesh;
  bool is_modified = BKE_object_is_modified(b_ob);
  PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");
  if (oct_mesh.data == NULL) {
    BL::ID b_ob_instance_data = b_ob_instance.data();
    oct_mesh = RNA_pointer_get(&b_ob_instance_data.ptr, "octane");
  }
  if (is_modified) {
    for (auto &obj : b_depsgraph.scene().objects) {
      if (obj.name() == b_ob.name()) {
        BL::ID obj_data = obj.data();
        oct_mesh = RNA_pointer_get(&obj_data.ptr, "octane");
        if (use_default_shader) {
          BL::Material material_override = view_layer.material_override;
          BL::Object::material_slots_iterator slot;
          if (obj.material_slots.length()) {
            used_shaders.clear();
            for (obj.material_slots.begin(slot); slot != obj.material_slots.end(); ++slot) {
              if (material_override) {
                find_shader(material_override, used_shaders, scene->default_surface);
              }
              else {
                BL::ID b_material(slot->material());
                find_shader_by_id_and_name(b_material, used_shaders, scene->default_surface);
              }
              use_default_shader = false;
            }
          }
        }
        break;
      }
    }
  }

  bool use_geometry_node_modifier = false;
  BL::Object::modifiers_iterator b_mod;
  for (b_ob.modifiers.begin(b_mod); b_mod != b_ob.modifiers.end(); ++b_mod) {
    if (b_mod->type() == BL::Modifier::type_NODES) {
      use_geometry_node_modifier = true;
      break;
    }
  }
  std::string modifier_object_tag = is_modified ? b_ob.name_full() : "";
  if (is_instance && use_geometry_node_modifier) {
    modifier_object_tag += "[Instance]";
  }
  std::string b_ob_name = b_ob.name();
  std::string b_ob_data_name = b_ob_data.name();
  std::string post_tag = b_ob.type() == BL::Object::type_CURVE ? "[Curve]" : MESH_TAG;
  std::string mesh_name = resolve_octane_name(b_ob_data, modifier_object_tag, post_tag);
  if (b_ob.mode() == b_ob.mode_EDIT) {
    mesh_name += "[EDIT_MODE]";
  }
  synced_object_to_octane_mesh_name_map[b_ob_name].insert(mesh_name);
  if (b_ob.mode() == b_ob.mode_EDIT) {
    for (auto &it : synced_object_to_octane_mesh_name_map[b_ob_name]) {
      if (it != mesh_name) {
        edited_mesh_names.insert(it);
      }
    }
  }
  bool is_mesh_data_updated = mesh_map.sync(&octane_mesh, key);
  if (edited_mesh_names.find(mesh_name) != edited_mesh_names.end()) {
    is_mesh_data_updated = true;
    unsync_resource_to_octane_manager(mesh_name, OctaneResourceType::GEOMETRY);
    edited_mesh_names.erase(mesh_name);
    if (resource_cache_data.find(mesh_name) != resource_cache_data.end()) {
      resource_cache_data.erase(mesh_name);
    }
  }
  std::string new_mesh_tag = generate_mesh_tag(b_depsgraph, b_ob, used_shaders);
  if (b_ob.type() == BL::Object::type_MESH) {
    std::string coordinate_mode = std::to_string(
        RNA_enum_get(&oct_mesh, "primitive_coordinate_mode"));
    std::string infinite_plane = std::to_string(RNA_boolean_get(&oct_mesh, "infinite_plane"));
    new_mesh_tag += ("|" + coordinate_mode + infinite_plane);
  }

  std::string new_octane_prop_tag = "";

  bool bHideOriginalMesh = false;
  if (b_ob.type() == BL::Object::type_MESH) {
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = get_boolean(
        oct_mesh, "octane_enable_sphere_attribute");
    bHideOriginalMesh = get_boolean(oct_mesh, "octane_hide_original_mesh");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius = get_float(
        oct_mesh, "octane_sphere_radius");
    bool use_randomized_radius = get_boolean(oct_mesh, "octane_use_randomized_radius");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed =
        use_randomized_radius ? get_int(oct_mesh, "octane_sphere_randomized_radius_seed") : -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius = get_float(
        oct_mesh, "octane_sphere_randomized_radius_min");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius = get_float(
        oct_mesh, "octane_sphere_randomized_radius_max");

    octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable =
        get_boolean(oct_mesh, "open_subd_enable") || use_octane_vertex_displacement_subdvision;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = get_enum(oct_mesh,
                                                                             "open_subd_scheme");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = get_int(oct_mesh,
                                                                           "open_subd_level");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = get_float(
        oct_mesh, "open_subd_sharpness");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp = get_enum(
        oct_mesh, "open_subd_bound_interp");
  }
  else {
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = false;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed = -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius = 0.f;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable = false;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = 1;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = 0;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = 0;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp = 3;
  }

  if (b_ob.type() == BL::Object::type_MESH) {
    BL::Mesh b_mesh = BL::Mesh(b_ob.data());
    const auto &oMeshSphereAttribute = octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute;
    const auto &oMeshOpenSubdivision = octane_mesh->octane_mesh.oMeshOpenSubdivision;
    std::string octane_mesh_setting_tag =
        std::to_string(oMeshSphereAttribute.bEnable) + std::to_string(bHideOriginalMesh) +
        std::to_string(oMeshSphereAttribute.fRadius) +
        std::to_string(oMeshSphereAttribute.iRandomSeed) +
        std::to_string(oMeshSphereAttribute.fMinRandomizedRadius) +
        std::to_string(oMeshSphereAttribute.fMaxRandomizedRadius) +
        std::to_string(oMeshOpenSubdivision.bOpenSubdEnable) +
        std::to_string(oMeshOpenSubdivision.iOpenSubdLevel) +
        std::to_string(oMeshOpenSubdivision.fOpenSubdSharpness) +
        std::to_string(oMeshOpenSubdivision.iOpenSubdBoundInterp);
    new_mesh_tag += ("|" + octane_mesh_setting_tag);
    new_octane_prop_tag += ("|" + octane_mesh_setting_tag);
  }
  else if (b_ob.type() == BL::Object::type_CURVE) {
    new_octane_prop_tag += ("|" + std::to_string(get_float(oct_mesh, "hair_root_width")) + "|" +
                            std::to_string(get_float(oct_mesh, "hair_tip_width")));
    BL::Curve b_curve = BL::Curve(b_ob.data());
    BL::Curve::splines_iterator s;
    for (b_curve.splines.begin(s); s != b_curve.splines.end(); ++s) {
      size_t step_num = s->points.length();
      size_t delta = std::max(static_cast<size_t>(step_num / 3), static_cast<size_t>(1));
      for (size_t step = 0; step < step_num; step += delta) {
        const BL::Array<float, 4> array = s->points[step].co();
        float sum = array[0] + array[1] + array[2];
        new_octane_prop_tag += ("|" + std::to_string(sum));
      }
      step_num = s->bezier_points.length();
      delta = std::max(static_cast<size_t>(step_num / 3), static_cast<size_t>(1));
      for (size_t step = 0; step < step_num; step += delta) {
        const BL::Array<float, 3> array = s->bezier_points[step].co();
        float sum = array[0] + array[1] + array[2];
        new_octane_prop_tag += ("|" + std::to_string(sum));
      }
    }
  }
  else if (b_ob.type() == BL::Object::type_CURVES) {
    new_octane_prop_tag += ("|" +
                            std::to_string(get_boolean(oct_mesh, "use_octane_radius_setting")) +
                            std::to_string(get_float(oct_mesh, "hair_root_width")) + "|" +
                            std::to_string(get_float(oct_mesh, "hair_tip_width")));
  }

  bool is_mesh_tag_data_updated = octane_mesh->mesh_tag != new_mesh_tag;
  bool is_octane_property_update = octane_mesh->octane_property_tag != new_octane_prop_tag;

  if (b_ob.mode() == b_ob.mode_EDIT || b_ob.mode() == b_ob.mode_VERTEX_PAINT ||
      b_ob.mode() == b_ob.mode_WEIGHT_PAINT) {
    if (!is_mesh_tag_data_updated) {
      if (b_depsgraph.id_type_updated(BL::DriverTarget::id_type_MESH)) {
        is_mesh_tag_data_updated = true;
      }
    }
  }
  if (b_ob.mode() == b_ob.mode_SCULPT_CURVES) {
    if (!is_mesh_tag_data_updated) {
      if (b_depsgraph.id_type_updated(BL::DriverTarget::id_type_CURVES)) {
        is_mesh_tag_data_updated = true;
      }
    }
  }

  octane_mesh->is_volume_to_mesh = false;
  octane_mesh->is_mesh_to_volume = false;
  stringstream mesh_to_volume_tag, volume_displace_tag;
  for (b_ob.modifiers.begin(b_mod); b_mod != b_ob.modifiers.end(); ++b_mod) {
    if (b_mod->type() == BL::Modifier::type_VOLUME_TO_MESH) {
      octane_mesh->is_volume_to_mesh = true;
    }
    if (b_mod->type() == BL::Modifier::type_MESH_TO_VOLUME) {
      BL::MeshToVolumeModifier mesh_to_volume_mod(*b_mod);
      mesh_to_volume_tag << mesh_to_volume_mod.object().ptr.data << mesh_to_volume_mod.density()
                         << mesh_to_volume_mod.use_fill_volume()
                         << mesh_to_volume_mod.exterior_band_width()
                         << mesh_to_volume_mod.interior_band_width()
                         << mesh_to_volume_mod.resolution_mode()
                         << mesh_to_volume_mod.voxel_amount();
      octane_mesh->is_mesh_to_volume = true;
    }
    if (b_mod->type() == BL::Modifier::type_VOLUME_DISPLACE) {
      octane_mesh->is_mesh_to_volume = true;
      BL::VolumeDisplaceModifier volume_displace_mod(*b_mod);
      volume_displace_tag << volume_displace_mod.texture().ptr.data
                          << volume_displace_mod.texture_map_mode()
                          << volume_displace_mod.strength()
                          << volume_displace_mod.texture_sample_radius()
                          << volume_displace_mod.texture_mid_level().data[0]
                          << volume_displace_mod.texture_mid_level().data[1]
                          << volume_displace_mod.texture_mid_level().data[2];
    }
  }

  std::string volume_modifier_tag = mesh_to_volume_tag.str() + volume_displace_tag.str();
  bool is_volume_data_modified = octane_mesh->volume_modifier_tag != volume_modifier_tag;
  octane_mesh->volume_modifier_tag = volume_modifier_tag;

  octane_mesh->nice_name = mesh_name;
  octane_mesh->name = mesh_name;
  octane_mesh->octane_mesh.sMeshName = mesh_name;
  // The mesh can be shared among objects with different mesh_type, so we only upgrade mesh_type
  // here. E.g. a mesh is shared by two objects: one is SCATTER type and the other is RESHARPABLE.
  // The final mesh type of the mesh will be RESHARPABLE.
  if (octane_mesh->mesh_type == MeshType::AUTO || mesh_type >= octane_mesh->mesh_type) {
    octane_mesh->mesh_type = mesh_type;
  }
  octane_mesh->use_octane_coordinate = RNA_enum_get(&oct_mesh, "primitive_coordinate_mode") ==
                                       OBJECT_DATA_NODE_TARGET_COORDINATE_OCTANE;

  if (b_ob.type() == BL::Object::type_CURVE) {
    bool use_curve_as_octane_hair = RNA_boolean_get(&oct_mesh, "render_curve_as_octane_hair");
    if (use_curve_as_octane_hair) {
      int current_frame = b_scene.frame_current();
      is_mesh_data_updated = octane_mesh->last_vdb_frame != b_scene.frame_current();
      octane_mesh->last_vdb_frame = current_frame;
    }
  }
  else if (b_ob.type() == BL::Object::type_CURVES) {
    int current_frame = b_scene.frame_current();
    is_mesh_data_updated = octane_mesh->last_vdb_frame != b_scene.frame_current();
    octane_mesh->last_vdb_frame = current_frame;
  }

  if (b_ob.type() == BL::Object::type_VOLUME) {
    if (mesh_synced.find(octane_mesh) != mesh_synced.end()) {
      return octane_mesh;
    }
    if (use_geometry_node_modifier && b_ob_data_name == "Volume") {
      octane_mesh->is_mesh_to_volume = true;
    }
    BL::Volume b_volume = BL::Volume(b_ob.data());
    b_volume.grids.load(b_data.ptr.data);
    octane_mesh->is_octane_volume = true;
    int current_frame = b_scene.frame_current();
    octane_mesh->need_update = is_mesh_data_updated ||
                               octane_mesh->last_vdb_frame != b_scene.frame_current();
    octane_mesh->last_vdb_frame = current_frame;
    octane_mesh->used_shaders = used_shaders;
    octane_mesh->mesh_tag = new_mesh_tag;
    octane_mesh->octane_property_tag = new_octane_prop_tag;
    octane_mesh->octane_mesh.bInfinitePlane = false;
    octane_mesh->octane_mesh.oMeshVolumeSDF.Clear();
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
    if (RNA_struct_find_property(&oct_mesh, "apply_import_scale_to_blender_transfrom") != NULL) {
      bool apply_import_scale_to_blender_transfrom = RNA_boolean_get(
          &oct_mesh, "apply_import_scale_to_blender_transfrom");
      if (apply_import_scale_to_blender_transfrom) {
        octane_mesh->octane_volume.iImportScale = 4;  // Default meters
      }
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

    if (octane_mesh->is_mesh_to_volume) {
      BL::Volume::grids_iterator b_grid_iter;
      for (b_volume.grids.begin(b_grid_iter); b_grid_iter != b_volume.grids.end(); ++b_grid_iter) {
        BL::VolumeGrid b_volume_grid(*b_grid_iter);
        if (b_volume_grid.name() == "density") {
          ::Volume *volume = (::Volume *)b_volume.ptr.data;
          VolumeGrid *volume_grid = (VolumeGrid *)b_volume_grid.ptr.data;
          openvdb::GridBase::ConstPtr const_grid = BKE_volume_grid_openvdb_for_read(volume,
                                                                                    volume_grid);
          if (const_grid->isType<openvdb::FloatGrid>()) {
            openvdb::FloatGrid::Ptr density_grid = openvdb::gridPtrCast<openvdb::FloatGrid>(
                const_grid->deepCopyGrid());
            size_t active_count = density_grid->activeVoxelCount();
            auto dim = density_grid->evalActiveVoxelDim();
            auto bbox = density_grid->evalActiveVoxelBoundingBox();
            if (octane_mesh->octane_volume.f3Resolution.x != dim.x() ||
                octane_mesh->octane_volume.f3Resolution.y != dim.y() ||
                octane_mesh->octane_volume.f3Resolution.z != dim.z()) {
              is_volume_data_modified = true;
            }

            octane_mesh->octane_volume.f3Resolution.x = dim.x();
            octane_mesh->octane_volume.f3Resolution.y = dim.y();
            octane_mesh->octane_volume.f3Resolution.z = dim.z();
            size_t total_count = dim.x() * dim.y() * dim.z();
            if (total_count > 0) {
              octane_mesh->octane_volume.fRegularGridData.resize(total_count);
              openvdb::tools::Dense<float, openvdb::tools::LayoutXYZ> dense(
                  bbox, (float *)octane_mesh->octane_volume.fRegularGridData.data());
              openvdb::tools::copyToDense(
                  *openvdb::gridConstPtrCast<openvdb::FloatGrid>(density_grid), dense);
              openvdb::Coord begin_coord;
              auto begin = bbox.beginXYZ();
              begin_coord.setX((*begin).asVec3d()[0]);
              begin_coord.setY((*begin).asVec3d()[1]);
              begin_coord.setZ((*begin).asVec3d()[2]);
              auto offset = density_grid->transform().indexToWorld(begin_coord);
              openvdb::math::Mat4f grid_matrix =
                  density_grid->transform().baseMap()->getAffineMap()->getMat4();
              Transform index_to_object;
              for (int col = 0; col < 4; col++) {
                for (int row = 0; row < 3; row++) {
                  index_to_object[row][col] = (float)grid_matrix[col][row];
                }
              }
              index_to_object.x.w = offset[0];
              index_to_object.y.w = offset[1];
              index_to_object.z.w = offset[2];
              set_octane_matrix(octane_mesh->octane_volume.oMatrix, index_to_object);
              octane_mesh->octane_volume.iAbsorptionOffset = 0;
              octane_mesh->need_update = is_mesh_data_updated || is_volume_data_modified;
            }
          }
          break;
        }
      }
    }
    mesh_synced.insert(octane_mesh);
    if (octane_mesh->need_update) {
      octane_mesh->tag_update(scene);
    }
    return octane_mesh;
  }

  octane_mesh->octane_mesh.bInfinitePlane = RNA_boolean_get(&oct_mesh, "infinite_plane");
  octane_mesh->octane_mesh.oMeshVolumeSDF.bEnable = RNA_boolean_get(&oct_mesh,
                                                                    "enable_mesh_volume_sdf");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fVoxelSize = RNA_float_get(&oct_mesh,
                                                                     "mesh_volume_sdf_voxel_size");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fBorderThicknessInside = RNA_float_get(
      &oct_mesh, "mesh_volume_sdf_border_thickness_inside");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fBorderThicknessOutside = RNA_float_get(
      &oct_mesh, "mesh_volume_sdf_border_thickness_outside");
  octane_mesh->octane_mesh.sScriptGeoName = resolve_octane_geometry_node(b_ob.ptr);
  octane_mesh->octane_mesh.sOrbxPath = resolve_orbx_proxy_path(oct_mesh, b_data, b_scene);
  MeshType final_mesh_type = resolve_mesh_type(mesh_name, b_ob.type(), octane_mesh->mesh_type);
  octane_mesh->octane_mesh.bReshapeable = (final_mesh_type == MeshType::RESHAPABLE_PROXY ||
                                           final_mesh_type == MeshType::GLOBAL);

  bool use_curve_as_octane_hair = b_ob.type() == BL::Object::type_CURVE &&
                                  RNA_boolean_get(&oct_mesh, "render_curve_as_octane_hair");
  bool use_curves_as_octane_hair = b_ob.type() == BL::Object::type_CURVES;
  bool octane_vdb_force_update_flag = RNA_boolean_get(&oct_mesh, "octane_vdb_helper") &&
                                      octane_mesh &&
                                      octane_mesh->last_vdb_frame != b_scene.frame_current();
  bool octane_subdivision_need_update = (use_octane_vertex_displacement_subdvision &&
                                         !octane_mesh->is_subdivision());
  bool need_update = preview ? (is_mesh_data_updated || is_mesh_tag_data_updated ||
                                octane_vdb_force_update_flag || octane_subdivision_need_update ||
                                is_octane_property_update) :
                               is_octane_geometry_required(
                                   mesh_name, b_ob.type(), oct_mesh, octane_mesh, mesh_type);
  bool need_recreate_mesh = false;
  if (preview) {
    bool is_synced = is_resource_synced_in_octane_manager(mesh_name, OctaneResourceType::GEOMETRY);
    if (is_synced) {
      // In isolation mode, blender will clear the mesh_map when objects are hidden. That makes the
      // is_mesh_shader_data_updated may be false-positive in such cases
      // We use the synced_mesh_shader_tags to fix it
      if (is_mesh_tag_data_updated) {
        if (synced_mesh_tags.find(mesh_name) != synced_mesh_tags.end()) {
          is_mesh_tag_data_updated = synced_mesh_tags[mesh_name] != new_mesh_tag;
        }
      }
      if (b_ob.type() == BL::Object::type_CURVE) {
        need_update |= is_octane_property_update;
        is_mesh_tag_data_updated |= is_octane_property_update;
      }
      synced_mesh_tags[mesh_name] = new_mesh_tag;
      bool paint_mode = b_ob.mode() == b_ob.mode_VERTEX_PAINT ||
                        b_ob.mode() == b_ob.mode_WEIGHT_PAINT ||
                        b_ob.mode() == b_ob.mode_TEXTURE_PAINT;
      if (paint_mode) {
        for (auto used_shader : used_shaders) {
          if (used_shader->graph && used_shader->graph->need_subdivision) {
            used_shader->need_sync_object = true;
          }
        }
      }
      if (paint_mode || b_ob.mode() == b_ob.mode_EDIT || is_mesh_tag_data_updated || is_modified) {
        need_recreate_mesh = need_update || is_modified;
        for (auto used_shader : used_shaders) {
          used_shader->need_update_paint = paint_mode;
        }
      }
      else {
        need_recreate_mesh = is_octane_geometry_required(
                                 mesh_name, b_ob.type(), oct_mesh, octane_mesh, mesh_type) ||
                             octane_mesh->is_volume_to_mesh;
      }
    }
    else {
      bool is_resource_dirty = dirty_resources.find(b_ob_data.name()) != dirty_resources.end() ||
                               b_ob.mode() == b_ob.mode_EDIT;
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
  octane_mesh->mesh_tag = new_mesh_tag;
  octane_mesh->octane_property_tag = new_octane_prop_tag;

  octane_mesh->enable_offset_transform = RNA_boolean_get(&oct_mesh,
                                                         "enable_octane_offset_transform");
  octane_mesh->use_octane_coordinate = RNA_enum_get(&oct_mesh, "primitive_coordinate_mode") ==
                                       OBJECT_DATA_NODE_TARGET_COORDINATE_OCTANE;
  if (octane_mesh->enable_offset_transform) {
    float3 translate, euler, scale;
    int mode = RNA_enum_get(&oct_mesh, "octane_offset_rotation_order");
    RNA_float_get_array(
        &oct_mesh, "octane_offset_translation", reinterpret_cast<float *>(&translate));
    RNA_float_get_array(&oct_mesh, "octane_offset_rotation", reinterpret_cast<float *>(&euler));
    RNA_float_get_array(&oct_mesh, "octane_offset_scale", reinterpret_cast<float *>(&scale));
    octane_mesh->offset_transform = make_transform(translate, euler, mode, scale);
  }
  octane_mesh->octane_mesh.oObjectLayer = object_layer;
  octane_mesh->octane_mesh.bInfinitePlane = RNA_boolean_get(&oct_mesh, "infinite_plane");
  octane_mesh->octane_mesh.oMeshVolumeSDF.bEnable = RNA_boolean_get(&oct_mesh,
                                                                    "enable_mesh_volume_sdf");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fVoxelSize = RNA_float_get(&oct_mesh,
                                                                     "mesh_volume_sdf_voxel_size");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fBorderThicknessInside = RNA_float_get(
      &oct_mesh, "mesh_volume_sdf_border_thickness_inside");
  octane_mesh->octane_mesh.oMeshVolumeSDF.fBorderThicknessOutside = RNA_float_get(
      &oct_mesh, "mesh_volume_sdf_border_thickness_outside");
  octane_mesh->is_scatter_group_source = RNA_boolean_get(&oct_mesh, "is_scatter_group_source");
  octane_mesh->scatter_group_id = RNA_int_get(&oct_mesh, "scatter_group_id");
  octane_mesh->scatter_instance_id = RNA_int_get(&oct_mesh, "scatter_instance_id");
  if (b_ob.type() == BL::Object::type_MESH) {
    BL::Mesh b_mesh = BL::Mesh(b_ob.data());
    if (b_mesh.use_auto_smooth() || RNA_boolean_get(&oct_mesh, "force_load_vertex_normals")) {
      octane_mesh->octane_mesh.fMaxSmoothAngle = b_mesh.auto_smooth_angle() / M_PI * 180;
    }
    else {
      octane_mesh->octane_mesh.fMaxSmoothAngle = -1.0f;
    }
  }
  else {
    octane_mesh->octane_mesh.fMaxSmoothAngle = -1.0f;
  }
  octane_mesh->octane_mesh.iHairInterpolations = RNA_enum_get(&oct_mesh, "hair_interpolation");
  octane_mesh->final_visibility = !(preview ? b_ob.hide_viewport() : b_ob.hide_render());

  if (b_ob.type() == BL::Object::type_MESH) {
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = get_boolean(
        oct_mesh, "octane_enable_sphere_attribute");
    bHideOriginalMesh = get_boolean(oct_mesh, "octane_hide_original_mesh");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius = get_float(
        oct_mesh, "octane_sphere_radius");
    bool use_randomized_radius = get_boolean(oct_mesh, "octane_use_randomized_radius");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed =
        use_randomized_radius ? get_int(oct_mesh, "octane_sphere_randomized_radius_seed") : -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius = get_float(
        oct_mesh, "octane_sphere_randomized_radius_min");
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius = get_float(
        oct_mesh, "octane_sphere_randomized_radius_max");

    octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable =
        get_boolean(oct_mesh, "open_subd_enable") || use_octane_vertex_displacement_subdvision;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = get_enum(oct_mesh,
                                                                             "open_subd_scheme");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = get_int(oct_mesh,
                                                                           "open_subd_level");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = get_float(
        oct_mesh, "open_subd_sharpness");
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp = get_enum(
        oct_mesh, "open_subd_bound_interp");
  }
  else {
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.bEnable = false;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.iRandomSeed = -1;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMinRandomizedRadius = 0.f;
    octane_mesh->octane_mesh.oMeshData.oMeshSphereAttribute.fMaxRandomizedRadius = 0.f;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable = false;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdScheme = 1;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdLevel = 0;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.fOpenSubdSharpness = 0;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.iOpenSubdBoundInterp = 3;
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
    octane_mesh->subdivision_type = object_subdivision_type(b_ob, preview, false);
  }

  bool use_octane_subdivision = use_octane_vertex_displacement_subdvision ||
                                (octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable);

  if (need_recreate_mesh) {
    if (use_curve_as_octane_hair) {
      create_curve_hair(scene, b_depsgraph, b_ob, octane_mesh, oct_mesh, used_shaders, false, 0);
    }
    else if (use_curves_as_octane_hair) {
      create_curves_hair(scene, b_ob, octane_mesh, false, 0);
    }
    else {
      BL::Mesh b_mesh = object_to_mesh(b_data,
                                       b_ob,
                                       b_depsgraph,
                                       true,
                                       use_octane_subdivision,
                                       octane_mesh ? octane_mesh->subdivision_type :
                                                     Mesh::SUBDIVISION_NONE);
      if (b_mesh) {
        BL::FluidDomainSettings b_domain = object_fluid_domain_find(b_ob);
        bool is_blender_internal_liquid_vdb =
            b_domain && is_blender_internal_vdb_format(int(b_domain.cache_data_format())) &&
            b_domain.domain_type() == BL::FluidDomainSettings::domain_type_LIQUID;
        if (!b_domain || is_blender_internal_liquid_vdb || is_octane_vdb) {
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
            create_mesh(
                scene, b_ob, octane_mesh, b_mesh, octane_mesh->used_shaders, winding_order);
          }
          /* mesh fluid motion mantaflow */
          sync_mesh_fluid_motion(b_ob, scene, b_mesh, octane_mesh);
          if (!octane_mesh->empty) {
            sync_hair(octane_mesh, b_mesh, b_ob, false);
          }
          free_object_to_mesh(b_data, b_ob, b_mesh);
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
        octane_mesh->octane_mesh.oMeshData.Clear();
        octane_mesh->octane_mesh.oMeshData.iSamplesNum = 1;
      }
      if (RNA_boolean_get(&oct_mesh, "external_alembic_mesh_tag")) {
        octane_mesh->empty = true;
        octane_mesh->octane_mesh.oMeshData.Clear();
        octane_mesh->octane_mesh.oMeshData.iSamplesNum = 1;
      }
      sync_mesh_particles(b_ob, octane_mesh, !preview);
    }
  }
  else {
    octane_mesh->octane_mesh.oMeshData.bUpdate = false;
    octane_mesh->octane_mesh.oMeshOpenSubdivision.bUpdate =
        octane_mesh->octane_mesh.oMeshOpenSubdivision.bOpenSubdEnable;
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

  /* fluid gas domain motion is skipped here */
  BL::FluidDomainSettings b_fluid_domain = object_fluid_gas_domain_find(b_ob);
  if (b_fluid_domain.ptr.data != NULL)
    return;

  if (b_ob.type() == BL::Object::type_CURVE) {
    /* find shader indices */
    std::vector<Shader *> used_shaders;
    bool use_octane_vertex_displacement_subdvision = false;
    bool use_default_shader = false;
    find_used_shaders(
        b_ob, used_shaders, use_octane_vertex_displacement_subdvision, use_default_shader);
    BL::ID b_ob_data = b_ob.data();
    PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");
    create_curve_hair(scene, b_depsgraph, b_ob, mesh, oct_mesh, used_shaders, true, motion_time);
    return;
  }

  // if (b_ob.type() == BL::Object::type_CURVES) {
  //  create_curves_hair(scene, b_ob, mesh, true, motion_time);
  //  return;
  //}

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
