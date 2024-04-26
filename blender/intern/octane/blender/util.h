/*
 * Copyright 2011-2013 Blender Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __BLENDER_UTIL_H__
#define __BLENDER_UTIL_H__

#include "DNA_mesh_types.h"
#include "DNA_meshdata_types.h"
#include "MEM_guardedalloc.h"
#include "RNA_access.hh"
#include "RNA_blender_cpp.h"
#include "RNA_types.hh"
#include "render/mesh.h"
#include "render/osl.h"

#include "BKE_mesh.h"
#include "util/algorithm.h"
#include "util/array.h"
#include "util/map.h"
#include "util/path.h"
#include "util/projection.h"
#include "util/set.h"
#include "util/transform.h"
#include "util/types.h"
#include "util/vector.h"

/* Hacks to hook into Blender API
 * todo: clean this up ... */

extern "C" {
size_t BLI_timecode_string_from_time_simple(char *str, size_t maxlen, double time_seconds);
void BLI_path_split_dir_part(const char *filepath, char *dir, const size_t dir_maxncpy);
bool BLI_path_frame(char *path, size_t path_maxncpy, int frame, int digits);
const char *BLI_path_extension(const char *filepath);
void BKE_image_user_frame_calc(void *ima, void *iuser, int cfra);
void BKE_image_user_file_path(void *iuser, void *ima, char *path);
unsigned char *BKE_image_get_pixels_for_frame(void *image, int frame, int tile);
float *BKE_image_get_float_pixels_for_frame(void *image, int frame, int tile);
struct Image *BKE_image_load_exists(struct Main *bmain, const char *filepath);
}

OCT_NAMESPACE_BEGIN

void python_thread_state_save(void **python_thread_state);
void python_thread_state_restore(void **python_thread_state);

struct BObjectInfo {
  /* Object directly provided by the depsgraph iterator. This object is only valid during one
   * iteration and must not be accessed afterwards. Transforms and visibility should be checked on
   * this object. */
  BL::Object iter_object;

  /* This object remains alive even after the object iterator is done. It corresponds to one
   * original object. It is the object that owns the object data below. */
  BL::Object real_object;

  /* The object-data referenced by the iter object. This is still valid after the depsgraph
   * iterator is done. It might have a different type compared to real_object.data(). */
  BL::ID object_data;

  /* True when the current geometry is the data of the referenced object. False when it is a
   * geometry instance that does not have a 1-to-1 relationship with an object. */
  bool is_real_object_data() const
  {
    return const_cast<BL::Object &>(real_object).data() == object_data;
  }
};

static inline BL::Mesh object_to_mesh(BL::BlendData & /*data*/,
                                      BL::Object &object,
                                      BL::Depsgraph & /*depsgraph*/,
                                      bool /*calc_undeformed*/,
                                      bool use_octane_subdivision,
                                      Mesh::SubdivisionType subdivision_type)
{
  bool enable_subdivision = use_octane_subdivision || subdivision_type != Mesh::SUBDIVISION_NONE;
  /* TODO: make this work with copy-on-write, modifiers are already evaluated. */
#if 0
  bool subsurf_mod_show_render = false;
  bool subsurf_mod_show_viewport = false;

  if (subdivision_type != Mesh::SUBDIVISION_NONE) {
    BL::Modifier subsurf_mod = object.modifiers[object.modifiers.length() - 1];

    subsurf_mod_show_render = subsurf_mod.show_render();
    subsurf_mod_show_viewport = subsurf_mod.show_viewport();

    subsurf_mod.show_render(false);
    subsurf_mod.show_viewport(false);
  }
#endif

  BL::Mesh mesh(PointerRNA_NULL);
  if (object.type() == BL::Object::type_MESH) {
    /* TODO: calc_undeformed is not used. */
    mesh = BL::Mesh(object.data());

    /* Make a copy to split faces if we use autosmooth, otherwise not needed.
     * Also in edit mode do we need to make a copy, to ensure data layers like
     * UV are not empty. */
    if (mesh.is_editmode() || (mesh.use_auto_smooth() && !enable_subdivision)) {
      BL::Depsgraph depsgraph(PointerRNA_NULL);
      mesh = object.to_mesh(false, depsgraph);
    }
  }
  else {
    BL::Depsgraph depsgraph(PointerRNA_NULL);
    mesh = object.to_mesh(false, depsgraph);
  }

#if 0
  if (subdivision_type != Mesh::SUBDIVISION_NONE) {
    BL::Modifier subsurf_mod = object.modifiers[object.modifiers.length() - 1];

    subsurf_mod.show_render(subsurf_mod_show_render);
    subsurf_mod.show_viewport(subsurf_mod_show_viewport);
  }
#endif

  if ((bool)mesh && !enable_subdivision) {
    if (mesh.use_auto_smooth()) {
      mesh.calc_normals_split();
      mesh.split_faces();
    }

    mesh.calc_loop_triangles();
  }

  return mesh;
}

static std::string generate_mesh_tag(BL::Depsgraph &b_depsgraph,
                                     BL::Object &b_ob,
                                     std::vector<Shader *> &shaders)
{
  // using milli = std::chrono::milliseconds;
  // auto start = std::chrono::high_resolution_clock::now();
  std::string result = "";
  static int SAMPLE_NUMBER = 5;
  bool is_edit_mode = b_ob.mode() == b_ob.mode_EDIT;
  if (b_ob.type() == BL::Object::type_MESH) {
    BL::Mesh b_mesh(b_ob.data());
    if (is_edit_mode) {
      BL::Depsgraph depsgraph(PointerRNA_NULL);
      b_mesh = b_ob.to_mesh(false, depsgraph);
    }
    ::Mesh *me = (::Mesh *)(b_mesh.ptr.data);
    std::stringstream ss;
    if (b_mesh.use_auto_smooth()) {
      ss << b_mesh.auto_smooth_angle() << "|";
    }
    ss << b_mesh.vertices.length() << "|" << b_mesh.polygons.length() << "|"
       << b_mesh.edges.length() << "|" << b_mesh.loops.length() << "|"
       << b_mesh.loop_triangles.length() << "|";
    int delta = std::max(1, b_mesh.vertices.length() / SAMPLE_NUMBER);
    for (int i = 0; i < b_mesh.vertices.length(); i += delta) {
      ss << (b_mesh.vertices[i].co()[0] + b_mesh.vertices[i].co()[1] +
             b_mesh.vertices[i].co()[2]) /
                3
         << "|";
      ss << (b_mesh.vertices[i].normal()[0] + b_mesh.vertices[i].normal()[1] +
             b_mesh.vertices[i].normal()[2]) /
                3
         << "|";
      if (b_mesh.uv_layers.length() != 0) {
        BL::Mesh::uv_layers_iterator l;
        for (b_mesh.uv_layers.begin(l); l != b_mesh.uv_layers.end(); ++l) {
          if (l->ptr.data != NULL) {
            if (i < l->data.length()) {
              ss << l->data[i].uv()[0] + l->data[i].uv()[1] / 2 << "|";
            }
          }
        }
      }
    }
    if (is_edit_mode) {
      /* Free mesh if we didn't just use the existing one. */
      if (b_ob.data().ptr.data != b_mesh.ptr.data) {
        b_ob.to_mesh_clear();
      }
    }
    ss << me->flag << "|";
    result = ss.str();
  }
  for (int i = 0; i < shaders.size(); ++i) {
    if (shaders[i]) {
      result += shaders[i]->name;
    }
  }
  // auto finish = std::chrono::high_resolution_clock::now();
  // stringstream profile;
  // profile << "generate_mesh_tag() took "
  //        << std::chrono::duration_cast<milli>(finish - start).count() << " milliseconds\n";
  // fprintf(stderr, "%s", profile.str().c_str());
  return result;
}

static inline void free_object_to_mesh(BL::BlendData & /*data*/,
                                       BL::Object &object,
                                       BL::Mesh &mesh)
{
  /* Free mesh if we didn't just use the existing one. */
  if (object.data().ptr.data != mesh.ptr.data) {
    object.to_mesh_clear();
  }
}

static inline void colorramp_to_array(BL::ColorRamp &ramp,
                                      array<float3> &ramp_color,
                                      array<float> &ramp_alpha,
                                      int size)
{
  ramp_color.resize(size);
  ramp_alpha.resize(size);

  for (int i = 0; i < size; i++) {
    float color[4];

    ramp.evaluate((float)i / (float)(size - 1), color);
    ramp_color[i] = make_float3(color[0], color[1], color[2]);
    ramp_alpha[i] = color[3];
  }
}

static inline void curvemap_minmax_curve(/*const*/ BL::CurveMap &curve, float *min_x, float *max_x)
{
  *min_x = min(*min_x, curve.points[0].location()[0]);
  *max_x = max(*max_x, curve.points[curve.points.length() - 1].location()[0]);
}

static inline void curvemapping_minmax(/*const*/ BL::CurveMapping &cumap,
                                       bool rgb_curve,
                                       float *min_x,
                                       float *max_x)
{
  /* const int num_curves = cumap.curves.length(); */ /* Gives linking error so far. */
  const int num_curves = rgb_curve ? 4 : 3;
  *min_x = FLT_MAX;
  *max_x = -FLT_MAX;
  for (int i = 0; i < num_curves; ++i) {
    BL::CurveMap map(cumap.curves[i]);
    curvemap_minmax_curve(map, min_x, max_x);
  }
}

static inline void curvemapping_to_array(BL::CurveMapping &cumap, array<float> &data, int size)
{
  cumap.update();
  BL::CurveMap curve = cumap.curves[0];
  data.resize(size);
  for (int i = 0; i < size; i++) {
    float t = (float)i / (float)(size - 1);
    data[i] = cumap.evaluate(curve, t);
  }
}

static inline void curvemapping_color_to_array(BL::CurveMapping &cumap,
                                               array<float3> &data,
                                               int size,
                                               bool rgb_curve)
{
  float min_x = 0.0f, max_x = 1.0f;

  /* TODO(sergey): There is no easy way to automatically guess what is
   * the range to be used here for the case when mapping is applied on
   * top of another mapping (i.e. R curve applied on top of common
   * one).
   *
   * Using largest possible range form all curves works correct for the
   * cases like vector curves and should be good enough heuristic for
   * the color curves as well.
   *
   * There might be some better estimations here tho.
   */
  curvemapping_minmax(cumap, rgb_curve, &min_x, &max_x);

  const float range_x = max_x - min_x;

  cumap.update();

  BL::CurveMap mapR = cumap.curves[0];
  BL::CurveMap mapG = cumap.curves[1];
  BL::CurveMap mapB = cumap.curves[2];

  data.resize(size);

  if (rgb_curve) {
    BL::CurveMap mapI = cumap.curves[3];
    for (int i = 0; i < size; i++) {
      const float t = min_x + (float)i / (float)(size - 1) * range_x;
      data[i] = make_float3(cumap.evaluate(mapR, cumap.evaluate(mapI, t)),
                            cumap.evaluate(mapG, cumap.evaluate(mapI, t)),
                            cumap.evaluate(mapB, cumap.evaluate(mapI, t)));
    }
  }
  else {
    for (int i = 0; i < size; i++) {
      float t = min_x + (float)i / (float)(size - 1) * range_x;
      data[i] = make_float3(
          cumap.evaluate(mapR, t), cumap.evaluate(mapG, t), cumap.evaluate(mapB, t));
    }
  }
}

static inline bool BKE_object_is_modified(BL::Object &self, BL::Scene &scene, bool preview)
{
  return self.is_modified(scene, (preview) ? (1 << 0) : (1 << 1)) ? true : false;
}

static inline bool BKE_object_is_deform_modified(BL::Object &self, BL::Scene &scene, bool preview)
{
  return self.is_deform_modified(scene, (preview) ? (1 << 0) : (1 << 1)) ? true : false;
}

static inline int render_resolution_x(BL::RenderSettings &b_render)
{
  return b_render.resolution_x() * b_render.resolution_percentage() / 100;
}

static inline int render_resolution_y(BL::RenderSettings &b_render)
{
  return b_render.resolution_y() * b_render.resolution_percentage() / 100;
}

static inline string image_user_file_path(BL::ImageUser &iuser,
                                          BL::Image &ima,
                                          int cfra,
                                          bool load_tiled)
{
  char filepath[1024];
  if (!load_tiled) {
    iuser.tile(0);
  }
  BKE_image_user_frame_calc(ima.ptr.data, iuser.ptr.data, cfra);
  BKE_image_user_file_path(iuser.ptr.data, ima.ptr.data, filepath);

  string filepath_str = std::string(filepath);
#ifdef WIN32
  if (path_is_relative(filepath)) {
    filepath_str = ensure_abs_path(ima.filepath_raw(), filepath_str);
  }
#endif
  // if (load_tiled && ima.source() == BL::Image::source_TILED) {
  //  string_replace(filepath_str, "1001", "<UDIM>");
  //}
  return filepath_str;
}

static inline int image_user_frame_number(BL::ImageUser &iuser, BL::Image &ima, int cfra)
{
  BKE_image_user_frame_calc(ima.ptr.data, iuser.ptr.data, cfra);
  return iuser.frame_current();
}

static inline unsigned char *image_get_pixels_for_frame(BL::Image &image, int frame, int tile)
{
  return BKE_image_get_pixels_for_frame(image.ptr.data, frame, tile);
}

static inline float *image_get_float_pixels_for_frame(BL::Image &image, int frame, int tile)
{
  return BKE_image_get_float_pixels_for_frame(image.ptr.data, frame, tile);
}

static inline void render_add_metadata(BL::RenderResult &b_rr, string name, string value)
{
  b_rr.stamp_data_add_field(name.c_str(), value.c_str());
}

/* Utilities */

static inline Transform get_transform(const BL::Array<float, 16> &array)
{
  ProjectionTransform projection;

  /* We assume both types to be just 16 floats, and transpose because blender
   * use column major matrix order while we use row major. */
  memcpy((void *)&projection, &array, sizeof(float) * 16);
  projection = projection_transpose(projection);

  /* Drop last row, matrix is assumed to be affine transform. */
  return projection_to_transform(projection);
}

static inline float2 get_float2(const BL::Array<float, 2> &array)
{
  return make_float2(array[0], array[1]);
}

static inline float3 get_float3(const BL::Array<float, 2> &array)
{
  return make_float3(array[0], array[1], 0.0f);
}

static inline float3 get_float3(const BL::Array<float, 3> &array)
{
  return make_float3(array[0], array[1], array[2]);
}

static inline float3 get_float3(const BL::Array<float, 4> &array)
{
  return make_float3(array[0], array[1], array[2]);
}

static inline OctaneDataTransferObject::float_3 get_octane_float3(
    const BL::Array<float, 2> &array, bool use_octane_coordinate = false)
{
  if (use_octane_coordinate) {
    return OctaneDataTransferObject::float_3(array[0], 0.0f, -array[1]);
  }
  else {
    return OctaneDataTransferObject::float_3(array[0], array[1], 0.0f);
  }
}

static inline OctaneDataTransferObject::float_3 get_octane_float3(
    const BL::Array<float, 3> &array, bool use_octane_coordinate = false)
{
  if (use_octane_coordinate) {
    return OctaneDataTransferObject::float_3(array[0], array[2], -array[1]);
  }
  else {
    return OctaneDataTransferObject::float_3(array[0], array[1], array[2]);
  }
}

static inline OctaneDataTransferObject::float_3 get_octane_float3(
    const BL::Array<float, 4> &array, bool use_octane_coordinate = false)
{
  if (use_octane_coordinate) {
    return OctaneDataTransferObject::float_3(array[0], array[2], -array[1]);
  }
  else {
    return OctaneDataTransferObject::float_3(array[0], array[1], array[2]);
  }
}

static inline float4 get_float4(const BL::Array<float, 4> &array)
{
  return make_float4(array[0], array[1], array[2], array[3]);
}

static inline int3 get_int3(const BL::Array<int, 3> &array)
{
  return make_int3(array[0], array[1], array[2]);
}

static inline int4 get_int4(const BL::Array<int, 4> &array)
{
  return make_int4(array[0], array[1], array[2], array[3]);
}

static inline uint get_layer(const BL::Array<bool, 20> &array)
{
  uint layer = 0;

  for (uint i = 0; i < 20; i++)
    if (array[i])
      layer |= (1 << i);

  return layer;
}

static inline uint get_layer(const BL::Array<bool, 20> &array,
                             const BL::Array<bool, 8> &local_array,
                             bool is_light = false,
                             uint view_layers = (1 << 20) - 1)
{
  uint layer = 0;

  for (uint i = 0; i < 20; i++)
    if (array[i])
      layer |= (1 << i);

  if (is_light) {
    /* Consider light is visible if it was visible without layer
     * override, which matches behavior of Blender Internal.
     */
    if (layer & view_layers) {
      for (uint i = 0; i < 8; i++)
        layer |= (1 << (20 + i));
    }
  }
  else {
    for (uint i = 0; i < 8; i++)
      if (local_array[i])
        layer |= (1 << (20 + i));
  }

  return layer;
}

static inline float3 get_float3(PointerRNA &ptr, const char *name)
{
  float3 result;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  bool is_array = (prop != NULL) && RNA_property_array_check(prop);
  if (is_array) {
    int len = RNA_property_array_length(&ptr, prop);
    RNA_float_get_array(&ptr, name, &result.x);
    for (int i = len; i < 3; ++i) {
      result[i] = 0.f;
    }
  }
  else {
    float f = RNA_float_get(&ptr, name);
    result.x = result.y = result.z = f;
  }
  return result;
}

static inline void set_float3(PointerRNA &ptr, const char *name, float3 value)
{
  RNA_float_set_array(&ptr, name, &value.x);
}

static inline float4 get_float4(PointerRNA &ptr, const char *name)
{
  float4 result;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  bool is_array = (prop != NULL) && RNA_property_array_check(prop);
  if (is_array) {
    int len = RNA_property_array_length(&ptr, prop);
    RNA_float_get_array(&ptr, name, &result.x);
    for (int i = len; i < 4; ++i) {
      result[i] = 0.f;
    }
  }
  else {
    float f = RNA_float_get(&ptr, name);
    result.x = result.y = result.z = result.w = f;
  }
  return result;
}

static inline void set_float4(PointerRNA &ptr, const char *name, float4 value)
{
  RNA_float_set_array(&ptr, name, &value.x);
}

static inline bool get_boolean(PointerRNA &ptr, const char *name)
{
  return RNA_boolean_get(&ptr, name) ? true : false;
}

static inline void set_boolean(PointerRNA &ptr, const char *name, bool value)
{
  RNA_boolean_set(&ptr, name, (int)value);
}

static inline float get_float(PointerRNA &ptr, const char *name)
{
  float result;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  bool is_array = (prop != NULL) && RNA_property_array_check(prop);
  if (is_array) {
    float4 f4;
    RNA_float_get_array(&ptr, name, &f4.x);
    result = f4.x;
  }
  else {
    result = RNA_float_get(&ptr, name);
  }
  return result;
}

static inline bool is_percentage_subtype(PointerRNA &ptr, const char *name)
{
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  if (prop) {
    PropertySubType subtype = RNA_property_subtype(prop);
    return (subtype == PROP_PERCENTAGE);
  }
  return false;
}

static inline void set_float(PointerRNA &ptr, const char *name, float value)
{
  RNA_float_set(&ptr, name, value);
}

static inline int get_int(PointerRNA &ptr, const char *name)
{
  int result;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  bool is_array = (prop != NULL) && RNA_property_array_check(prop);
  if (is_array) {
    int4 i4;
    RNA_int_get_array(&ptr, name, &i4.x);
    result = i4.x;
  }
  else {
    result = RNA_int_get(&ptr, name);
  }
  return result;
}

static inline void set_int(PointerRNA &ptr, const char *name, int value)
{
  RNA_int_set(&ptr, name, value);
}

/* Get a RNA enum value with sanity check: if the RNA value is above num_values
 * the function will return a fallback default value.
 *
 * NOTE: This function assumes that RNA enum values are a continuous sequence
 * from 0 to num_values-1. Be careful to use it with enums where some values are
 * deprecated!
 */
static inline int get_enum(PointerRNA &ptr,
                           const char *name,
                           int num_values = -1,
                           int default_value = -1)
{
  int value = RNA_enum_get(&ptr, name);
  if (num_values != -1 && value >= num_values) {
    assert(default_value != -1);
    value = default_value;
  }
  return value;
}

static inline string get_enum_identifier(PointerRNA &ptr, const char *name)
{
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  const char *identifier = "";
  int value = RNA_property_enum_get(&ptr, prop);

  RNA_property_enum_identifier(NULL, &ptr, prop, value, &identifier);

  return string(identifier);
}

static inline void set_enum(PointerRNA &ptr, const char *name, int value)
{
  RNA_enum_set(&ptr, name, value);
}

static inline void set_enum(PointerRNA &ptr, const char *name, const string &identifier)
{
  RNA_enum_set_identifier(NULL, &ptr, name, identifier.c_str());
}

static inline string get_string(PointerRNA &ptr, const char *name)
{
  char cstrbuf[1024];
  char *cstr = RNA_string_get_alloc(&ptr, name, cstrbuf, sizeof(cstrbuf), NULL);
  string str(cstr);
  if (cstr != cstrbuf)
    MEM_freeN(cstr);

  return str;
}

static inline void set_string(PointerRNA &ptr, const char *name, const string &value)
{
  RNA_string_set(&ptr, name, value.c_str());
}

/* Relative Paths */

static inline string blender_absolute_path(BL::BlendData &b_data, BL::ID &b_id, const string &path)
{
  if (path.size() >= 2 && path[0] == '/' && path[1] == '/') {
    string dirname;

    if (b_id.library()) {
      BL::ID b_library_id(b_id.library());
      dirname = blender_absolute_path(b_data, b_library_id, b_id.library().filepath());
    }
    else
      dirname = b_data.filepath();

    return path_join(path_dirname(dirname), path.substr(2));
  }

  return path;
}

static inline string blender_path_frame(const string &path, int frame, int digits)
{
  char converted_path[1024];
  strcpy(converted_path, path.c_str());
  BLI_path_frame(converted_path, 1024, frame, digits);
  return string(converted_path);
}

static inline string blender_path_extension(const string &path)
{
  const char *extension = BLI_path_extension(path.c_str());
  string result;
  if (extension) {
    result = string(result);
  }
  return result;
}

static inline string get_text_datablock_content(const PointerRNA &ptr)
{
  if (ptr.data == NULL) {
    return "";
  }

  string content;
  BL::Text::lines_iterator iter;
  for (iter.begin(ptr); iter; ++iter) {
    content += iter->body() + "\n";
  }

  return content;
}

/* Texture Space */

static inline void mesh_texture_space(BL::Mesh &b_mesh, float3 &loc, float3 &size)
{
  loc = get_float3(b_mesh.texspace_location());
  size = get_float3(b_mesh.texspace_size());

  if (size.x != 0.0f)
    size.x = 0.5f / size.x;
  if (size.y != 0.0f)
    size.y = 0.5f / size.y;
  if (size.z != 0.0f)
    size.z = 0.5f / size.z;

  loc = loc * size - make_float3(0.5f, 0.5f, 0.5f);
}

/* Object motion steps, returns 0 if no motion blur needed. */
static inline uint object_motion_steps(BL::Object &b_parent, BL::Object &b_ob)
{
  /* Get motion enabled and steps from object itself. */
  PointerRNA octane_object = RNA_pointer_get(&b_ob.ptr, "octane");
  bool use_motion = get_boolean(octane_object, "use_motion_blur");
  if (!use_motion) {
    return 0;
  }

  uint steps = max(1, get_int(octane_object, "motion_steps"));

  /* Also check parent object, so motion blur and steps can be
   * controlled by dupligroup duplicator for linked groups. */
  if (b_parent.ptr.data != nullptr && b_parent.ptr.data != b_ob.ptr.data) {
    PointerRNA parent_octane_object = RNA_pointer_get(&b_parent.ptr, "octane");
    use_motion &= get_boolean(parent_octane_object, "use_motion_blur");

    if (!use_motion) {
      return 0;
    }

    steps = max((int)steps, get_int(parent_octane_object, "motion_steps"));
  }

  /* Use uneven number of steps so we get one keyframe at the current frame,
   * and use 2^(steps - 1) so objects with more/fewer steps still have samples
   * at the same times, to avoid sampling at many different times. */
  return (2 << (steps - 1)) + 1;
}

/* object uses deformation motion blur */
static inline bool object_use_deform_motion(BL::Object &b_parent, BL::Object &b_ob)
{
  PointerRNA octane_object = RNA_pointer_get(&b_ob.ptr, "octane");
  bool use_deform_motion = get_boolean(octane_object, "use_deform_motion");
  /* If motion blur is enabled for the object we also check
   * whether it's enabled for the parent object as well.
   *
   * This way we can control motion blur from the dupligroup
   * duplicator much easier.
   */
  if (use_deform_motion && b_parent.ptr.data != b_ob.ptr.data) {
    PointerRNA parent_octane_object = RNA_pointer_get(&b_parent.ptr, "octane");
    use_deform_motion &= get_boolean(parent_octane_object, "use_deform_motion");
  }
  return use_deform_motion;
}

static inline BL::FluidDomainSettings object_fluid_domain_find(BL::Object &b_ob)
{
  BL::Object::modifiers_iterator b_mod;

  for (b_ob.modifiers.begin(b_mod); b_mod != b_ob.modifiers.end(); ++b_mod) {
    if (b_mod->is_a(&RNA_FluidModifier)) {
      BL::FluidModifier b_mmd(*b_mod);

      if (b_mmd.fluid_type() == BL::FluidModifier::fluid_type_DOMAIN)
        return b_mmd.domain_settings();
    }
  }

  return BL::FluidDomainSettings(PointerRNA_NULL);
}

static inline BL::FluidDomainSettings object_fluid_gas_domain_find(BL::Object &b_ob)
{
  for (BL::Modifier &b_mod : b_ob.modifiers) {
    if (b_mod.is_a(&RNA_FluidModifier)) {
      BL::FluidModifier b_mmd(b_mod);

      if (b_mmd.fluid_type() == BL::FluidModifier::fluid_type_DOMAIN &&
          b_mmd.domain_settings().domain_type() == BL::FluidDomainSettings::domain_type_GAS)
      {
        return b_mmd.domain_settings();
      }
    }
  }

  return BL::FluidDomainSettings(PointerRNA_NULL);
}

static inline Mesh::SubdivisionType object_subdivision_type(BL::Object &b_ob,
                                                            bool preview,
                                                            bool experimental)
{
  PointerRNA obj = RNA_pointer_get(&b_ob.ptr, "octane");

  if (obj.data && b_ob.modifiers.length() > 0 && experimental) {
    BL::Modifier mod = b_ob.modifiers[b_ob.modifiers.length() - 1];
    bool enabled = preview ? mod.show_viewport() : mod.show_render();

    if (enabled && mod.type() == BL::Modifier::type_SUBSURF) {
      BL::SubsurfModifier subsurf(mod);

      if (subsurf.subdivision_type() == BL::SubsurfModifier::subdivision_type_CATMULL_CLARK) {
        return Mesh::SUBDIVISION_CATMULL_CLARK;
      }
      else {
        return Mesh::SUBDIVISION_LINEAR;
      }
    }
  }

  return Mesh::SUBDIVISION_NONE;
}

/* ID Map
 *
 * Utility class to keep in sync with blender data.
 * Used for objects, meshes, lights and shaders. */

template<typename K, typename T> class id_map {
 public:
  id_map(vector<T *> *scene_data_)
  {
    scene_data = scene_data_;
  }

  T *find(const BL::ID &id)
  {
    return find(id.ptr.owner_id);
  }

  T *find(const K &key)
  {
    if (b_map.find(key) != b_map.end()) {
      T *data = b_map[key];
      return data;
    }

    return NULL;
  }

  void set_recalc(const BL::ID &id)
  {
    b_recalc.insert(id.ptr.data);
  }

  void set_recalc(void *id_ptr)
  {
    b_recalc.insert(id_ptr);
  }

  bool has_recalc()
  {
    return !(b_recalc.empty());
  }

  void pre_sync()
  {
    used_set.clear();
  }

  bool sync(T **r_data, const BL::ID &id)
  {
    return sync(r_data, id, id, id.ptr.owner_id);
  }

  bool sync(T **r_data, const BL::ID &id, const BL::ID &parent, const K &key)
  {
    T *data = find(key);
    bool recalc;

    if (!data) {
      /* add data if it didn't exist yet */
      data = new T();
      scene_data->push_back(data);
      b_map[key] = data;
      recalc = true;
    }
    else {
      recalc = (b_recalc.find(id.ptr.data) != b_recalc.end());
      if (parent.ptr.data)
        recalc = recalc || (b_recalc.find(parent.ptr.data) != b_recalc.end());
    }

    used(data);

    *r_data = data;
    return recalc;
  }

  bool is_used(const K &key)
  {
    T *data = find(key);
    return (data) ? used_set.find(data) != used_set.end() : false;
  }

  void used(T *data)
  {
    /* tag data as still in use */
    used_set.insert(data);
  }

  void set_default(T *data)
  {
    b_map[NULL] = data;
  }

  bool post_sync(bool do_delete = true)
  {
    /* remove unused data */
    vector<T *> new_scene_data;
    typename vector<T *>::iterator it;
    bool deleted = false;

    for (it = scene_data->begin(); it != scene_data->end(); it++) {
      T *data = *it;

      if (do_delete && used_set.find(data) == used_set.end()) {
        delete data;
        deleted = true;
      }
      else
        new_scene_data.push_back(data);
    }

    *scene_data = new_scene_data;

    /* update mapping */
    map<K, T *> new_map;
    typedef pair<const K, T *> TMapPair;
    typename map<K, T *>::iterator jt;

    for (jt = b_map.begin(); jt != b_map.end(); jt++) {
      TMapPair &pair = *jt;

      if (used_set.find(pair.second) != used_set.end())
        new_map[pair.first] = pair.second;
    }

    used_set.clear();
    b_recalc.clear();
    b_map = new_map;

    return deleted;
  }

  const map<K, T *> &key_to_scene_data()
  {
    return b_map;
  }

 protected:
  vector<T *> *scene_data;
  map<K, T *> b_map;
  set<T *> used_set;
  set<void *> b_recalc;
};

/* Object Key
 *
 * To uniquely identify instances, we use the parent, object and persistent instance ID.
 * We also export separate object for a mesh and its particle hair. */

enum { OBJECT_PERSISTENT_ID_SIZE = 8 /* MAX_DUPLI_RECUR in Blender. */ };

struct ObjectKey {
  void *parent;
  int id[OBJECT_PERSISTENT_ID_SIZE];
  void *ob;
  bool use_particle_hair;

  ObjectKey(void *parent_, int id_[OBJECT_PERSISTENT_ID_SIZE], void *ob_, bool use_particle_hair_)
      : parent(parent_), ob(ob_), use_particle_hair(use_particle_hair_)
  {
    if (id_)
      memcpy(id, id_, sizeof(id));
    else
      memset(id, 0, sizeof(id));
  }

  bool operator<(const ObjectKey &k) const
  {
    if (ob < k.ob) {
      return true;
    }
    else if (ob == k.ob) {
      if (parent < k.parent) {
        return true;
      }
      else if (parent == k.parent) {
        if (use_particle_hair < k.use_particle_hair) {
          return true;
        }
        else if (use_particle_hair == k.use_particle_hair) {
          return memcmp(id, k.id, sizeof(id)) < 0;
        }
      }
    }

    return false;
  }
};

/* Particle System Key */

struct ParticleSystemKey {
  void *ob;
  int id[OBJECT_PERSISTENT_ID_SIZE];

  ParticleSystemKey(void *ob_, int id_[OBJECT_PERSISTENT_ID_SIZE]) : ob(ob_)
  {
    if (id_)
      memcpy(id, id_, sizeof(id));
    else
      memset(id, 0, sizeof(id));
  }

  bool operator<(const ParticleSystemKey &k) const
  {
    /* first id is particle index, we don't compare that */
    if (ob < k.ob)
      return true;
    else if (ob == k.ob)
      return memcmp(id + 1, k.id + 1, sizeof(int) * (OBJECT_PERSISTENT_ID_SIZE - 1)) < 0;

    return false;
  }
};

class EdgeMap {
 public:
  EdgeMap() {}

  void clear()
  {
    edges_.clear();
  }

  void insert(int v0, int v1)
  {
    get_sorted_verts(v0, v1);
    edges_.insert(std::pair<int, int>(v0, v1));
  }

  bool exists(int v0, int v1)
  {
    get_sorted_verts(v0, v1);
    return edges_.find(std::pair<int, int>(v0, v1)) != edges_.end();
  }

 protected:
  void get_sorted_verts(int &v0, int &v1)
  {
    if (v0 > v1) {
      swap(v0, v1);
    }
  }

  set<std::pair<int, int>> edges_;
};

static inline int4 get_int4(PointerRNA &ptr, const char *name)
{
  int4 result;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
  bool is_array = (prop != NULL) && RNA_property_array_check(prop);
  if (is_array) {
    int len = RNA_property_array_length(&ptr, prop);
    RNA_int_get_array(&ptr, name, &result.x);
    for (int i = len; i < 4; ++i) {
      result[i] = 0;
    }
  }
  else {
    int i = RNA_int_get(&ptr, name);
    result.x = result.y = result.z = result.w = i;
  }
  return result;
}

static inline void set_int4(PointerRNA &ptr, const char *name, int4 value)
{
  RNA_int_set_array(&ptr, name, &value.x);
}

static inline bool set_blender_node(::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr,
                                    PointerRNA &ptr,
                                    bool is_socket = false,
                                    bool is_custom_node = false)
{
  if (!base_dto_ptr || !ptr.data)
    return false;

  int4 i;
  float4 f;
  const char *name = ((is_socket && base_dto_ptr->type != OctaneDataTransferObject::DTO_ENUM) ?
                          "default_value" :
                          base_dto_ptr->sName.c_str());
  if (is_custom_node) {
    PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
    if (!prop) {
      name = "default_value";
    }
  }
  switch (base_dto_ptr->type) {
    case OctaneDataTransferObject::DTO_ENUM:
      set_enum(ptr, name, ((::OctaneDataTransferObject::OctaneDTOInt *)base_dto_ptr)->iVal);
      break;
    case OctaneDataTransferObject::DTO_BOOL:
      set_boolean(ptr, name, ((::OctaneDataTransferObject::OctaneDTOBool *)base_dto_ptr)->bVal);
      break;
    case OctaneDataTransferObject::DTO_INT:
      set_int(ptr, name, ((::OctaneDataTransferObject::OctaneDTOInt *)base_dto_ptr)->iVal);
      break;
    case OctaneDataTransferObject::DTO_INT_2:
      i.x = ((::OctaneDataTransferObject::OctaneDTOInt2 *)base_dto_ptr)->iVal.x;
      i.y = ((::OctaneDataTransferObject::OctaneDTOInt2 *)base_dto_ptr)->iVal.y;
      set_int4(ptr, name, i);
      break;
    case OctaneDataTransferObject::DTO_INT_3:
      i.x = ((::OctaneDataTransferObject::OctaneDTOInt3 *)base_dto_ptr)->iVal.x;
      i.y = ((::OctaneDataTransferObject::OctaneDTOInt3 *)base_dto_ptr)->iVal.y;
      i.z = ((::OctaneDataTransferObject::OctaneDTOInt3 *)base_dto_ptr)->iVal.z;
      set_int4(ptr, name, i);
      break;
    case OctaneDataTransferObject::DTO_FLOAT:
      set_float(ptr, name, ((::OctaneDataTransferObject::OctaneDTOFloat *)base_dto_ptr)->fVal);
      break;
    case OctaneDataTransferObject::DTO_FLOAT_2:
      f.x = ((::OctaneDataTransferObject::OctaneDTOFloat2 *)base_dto_ptr)->fVal.x;
      f.y = ((::OctaneDataTransferObject::OctaneDTOFloat2 *)base_dto_ptr)->fVal.y;
      f.z = f.w = 1.f;
      set_float4(ptr, name, f);
      break;
    case OctaneDataTransferObject::DTO_FLOAT_3:
      f.x = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.x;
      f.y = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.y;
      f.z = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.z;
      f.w = 1.f;
      set_float4(ptr, name, f);
      break;
    case OctaneDataTransferObject::DTO_STR:
      set_string(ptr, name, ((::OctaneDataTransferObject::OctaneDTOString *)base_dto_ptr)->sVal);
      break;
    case OctaneDataTransferObject::DTO_RGB:
      f.x = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.x;
      f.y = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.y;
      f.z = ((::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr)->fVal.z;
      f.w = 1.f;
      set_float4(ptr, name, f);
      break;
    default:
      break;
  }
  return true;
}

static inline bool need_upgrade_float_to_color(
    ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr,
    PointerRNA &ptr,
    float4 &color,
    bool is_socket = false,
    int32_t addon_data_type = -1)
{
  if (!base_dto_ptr || !ptr.data)
    return false;
  int32_t dto_type = base_dto_ptr->type;
  if (addon_data_type != -1) {
    dto_type = addon_data_type;
  }
  const char *name = ((is_socket && dto_type != OctaneDataTransferObject::DTO_ENUM) ?
                          "default_value" :
                          base_dto_ptr->sName.c_str());
  if (dto_type == OctaneDataTransferObject::DTO_FLOAT) {
    PropertyRNA *prop = RNA_struct_find_property(&ptr, name);
    bool is_array = (prop != NULL) && RNA_property_array_check(prop);
    if (is_array) {
      RNA_float_get_array(&ptr, name, &color.x);
      return true;
    }
  }
  return false;
}

static inline bool set_octane_data_transfer_object(
    ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr,
    PointerRNA &ptr,
    bool is_socket = false,
    int32_t addon_data_type = -1)
{
  if (!base_dto_ptr || !ptr.data)
    return false;

  int4 i;
  float4 f;
  PropertyRNA *prop;
  int32_t dto_type = base_dto_ptr->type;
  if (addon_data_type != -1) {
    dto_type = addon_data_type;
  }
  const char *name = ((is_socket && dto_type != OctaneDataTransferObject::DTO_ENUM) ?
                          "default_value" :
                          base_dto_ptr->sName.c_str());
  switch (dto_type) {
    case OctaneDataTransferObject::DTO_ENUM:
      prop = RNA_struct_find_property(&ptr, name);
      if (prop != NULL) {
        // Old style
        *(::OctaneDataTransferObject::OctaneDTOInt *)base_dto_ptr = get_enum(ptr, name);
      }
      else {
        *(::OctaneDataTransferObject::OctaneDTOEnum *)base_dto_ptr = get_enum(ptr,
                                                                              "default_value");
      }
      break;
    case OctaneDataTransferObject::DTO_BOOL:
      *(::OctaneDataTransferObject::OctaneDTOBool *)base_dto_ptr = get_boolean(ptr, name);
      break;
    case OctaneDataTransferObject::DTO_INT:
      prop = RNA_struct_find_property(&ptr, name);
      if (RNA_property_type(prop) == PROP_ENUM) {
        *(::OctaneDataTransferObject::OctaneDTOInt *)base_dto_ptr = get_enum(ptr, name);
      }
      else {
        *(::OctaneDataTransferObject::OctaneDTOInt *)base_dto_ptr = get_int(ptr, name);
      }
      break;
    case OctaneDataTransferObject::DTO_INT_2:
      i = get_int4(ptr, name);
      *(::OctaneDataTransferObject::OctaneDTOInt2 *)base_dto_ptr =
          ::OctaneDataTransferObject::int32_2(i[0], i[1]);
      break;
    case OctaneDataTransferObject::DTO_INT_3:
      i = get_int4(ptr, name);
      *(::OctaneDataTransferObject::OctaneDTOInt3 *)base_dto_ptr =
          ::OctaneDataTransferObject::int32_3(i[0], i[1], i[2]);
      break;
    case OctaneDataTransferObject::DTO_FLOAT:
      if (is_percentage_subtype(ptr, name)) {
        *(::OctaneDataTransferObject::OctaneDTOFloat *)base_dto_ptr = get_float(ptr, name) / 100.0;
      }
      else {
        *(::OctaneDataTransferObject::OctaneDTOFloat *)base_dto_ptr = get_float(ptr, name);
      }
      break;
    case OctaneDataTransferObject::DTO_FLOAT_2:
      f = get_float4(ptr, name);
      *(::OctaneDataTransferObject::OctaneDTOFloat2 *)base_dto_ptr =
          ::OctaneDataTransferObject::float_2(f[0], f[1]);
      break;
    case OctaneDataTransferObject::DTO_FLOAT_3:
      f = get_float4(ptr, name);
      *(::OctaneDataTransferObject::OctaneDTOFloat3 *)base_dto_ptr =
          ::OctaneDataTransferObject::float_3(f[0], f[1], f[2]);
      break;
    case OctaneDataTransferObject::DTO_STR:
      *(::OctaneDataTransferObject::OctaneDTOString *)base_dto_ptr = get_string(ptr, name);
      break;
    case OctaneDataTransferObject::DTO_RGB:
      f = get_float4(ptr, name);
      *(::OctaneDataTransferObject::OctaneDTORGB *)base_dto_ptr =
          ::OctaneDataTransferObject::float_3(f[0], f[1], f[2]);
      break;
    default:
      break;
  }
  return true;
}

struct OctaneDataTransferObjectVisitor : BaseVisitor {

  void handle(const std::string &name, ::OctaneDataTransferObject::OctaneDTOBase *base_dto_ptr)
  {
    if (base_dto_ptr && base_dto_ptr->sName.size()) {
      if (!base_dto_ptr->bUseSocket) {
        set_octane_data_transfer_object(base_dto_ptr, target, false);
      }
    }
  }

  PointerRNA &target;
  OctaneDataTransferObjectVisitor(PointerRNA &target) : target(target) {}
};

static int32_t get_light_ids_mask(PointerRNA &ptr)
{
  int32_t iLightIDsMask = (get_boolean(ptr, "light_id_sunlight") & 1) << 0 |
                          (get_boolean(ptr, "light_id_env") & 1) << 1 |
                          (get_boolean(ptr, "light_id_pass_1") & 1) << 2 |
                          (get_boolean(ptr, "light_id_pass_2") & 1) << 3 |
                          (get_boolean(ptr, "light_id_pass_3") & 1) << 4 |
                          (get_boolean(ptr, "light_id_pass_4") & 1) << 5 |
                          (get_boolean(ptr, "light_id_pass_5") & 1) << 6 |
                          (get_boolean(ptr, "light_id_pass_6") & 1) << 7 |
                          (get_boolean(ptr, "light_id_pass_7") & 1) << 8 |
                          (get_boolean(ptr, "light_id_pass_8") & 1) << 9;
  PropertyRNA *prop = RNA_struct_find_property(&ptr, "light_id_pass_9");
  if (prop != NULL) {
    iLightIDsMask = iLightIDsMask | (get_boolean(ptr, "light_id_pass_9") & 1) << 10 |
                    (get_boolean(ptr, "light_id_pass_10") & 1) << 11 |
                    (get_boolean(ptr, "light_id_pass_11") & 1) << 12 |
                    (get_boolean(ptr, "light_id_pass_12") & 1) << 13 |
                    (get_boolean(ptr, "light_id_pass_13") & 1) << 14 |
                    (get_boolean(ptr, "light_id_pass_14") & 1) << 15 |
                    (get_boolean(ptr, "light_id_pass_15") & 1) << 16 |
                    (get_boolean(ptr, "light_id_pass_16") & 1) << 17 |
                    (get_boolean(ptr, "light_id_pass_17") & 1) << 18 |
                    (get_boolean(ptr, "light_id_pass_18") & 1) << 19 |
                    (get_boolean(ptr, "light_id_pass_19") & 1) << 20 |
                    (get_boolean(ptr, "light_id_pass_20") & 1) << 21;
  }

  return iLightIDsMask;
}

static int32_t get_light_ids_invert_mask(PointerRNA &ptr)
{
  int32_t iLightLinkingInvertMask = (get_boolean(ptr, "light_id_sunlight_invert") & 1) << 0 |
                                    (get_boolean(ptr, "light_id_env_invert") & 1) << 1 |
                                    (get_boolean(ptr, "light_id_pass_1_invert") & 1) << 2 |
                                    (get_boolean(ptr, "light_id_pass_2_invert") & 1) << 3 |
                                    (get_boolean(ptr, "light_id_pass_3_invert") & 1) << 4 |
                                    (get_boolean(ptr, "light_id_pass_4_invert") & 1) << 5 |
                                    (get_boolean(ptr, "light_id_pass_5_invert") & 1) << 6 |
                                    (get_boolean(ptr, "light_id_pass_6_invert") & 1) << 7 |
                                    (get_boolean(ptr, "light_id_pass_7_invert") & 1) << 8 |
                                    (get_boolean(ptr, "light_id_pass_8_invert") & 1) << 9;
  return iLightLinkingInvertMask;
}

static void resolve_object_layer(PointerRNA &octane_object,
                                 OctaneDataTransferObject::OctaneObjectLayer &object_layer)
{
  visit_each(object_layer, OctaneDataTransferObjectVisitor(octane_object));
  object_layer.iLightPassMask = get_light_ids_mask(octane_object);
  object_layer.i3Color.iVal.x = int(object_layer.f3Color.fVal.x * 255.f);
  object_layer.i3Color.iVal.y = int(object_layer.f3Color.fVal.y * 255.f);
  object_layer.i3Color.iVal.z = int(object_layer.f3Color.fVal.z * 255.f);
  object_layer.oBakingTransform.fRotation.fVal.x = 0;
  object_layer.oBakingTransform.fRotation.fVal.y = 0;
  object_layer.oBakingTransform.fRotation.fVal.z = object_layer.fRotationZ.fVal;
  object_layer.oBakingTransform.fScale.fVal.x = object_layer.fScaleX.fVal;
  object_layer.oBakingTransform.fScale.fVal.y = object_layer.fScaleY.fVal;
  object_layer.oBakingTransform.fScale.fVal.z = 0;
  object_layer.oBakingTransform.fTranslation.fVal.x = object_layer.fTranslationX.fVal;
  object_layer.oBakingTransform.fTranslation.fVal.y = object_layer.fTranslationY.fVal;
  object_layer.oBakingTransform.fTranslation.fVal.z = 0;
}

static void resolve_volume_attributes(PointerRNA &octane_volume,
                                      OctaneDataTransferObject::OctaneVolume &object_volume)
{
  visit_each(object_volume, OctaneDataTransferObjectVisitor(octane_volume));
}

static std::string resolve_octane_name(BL::ID &b_ob_data,
                                       std::string modifier_object_tag,
                                       std::string tag)
{
  std::string lib_prefix = (b_ob_data.ptr.data && b_ob_data.library().ptr.data) ?
                               (b_ob_data.library().name() + ".") :
                               "";
  if (modifier_object_tag.length()) {
    modifier_object_tag += ".";
  }
  return lib_prefix + modifier_object_tag + (b_ob_data.ptr.data ? b_ob_data.name() : "") + tag;
}

static inline std::string split_dir_part(std::string path)
{
  char dir[256];
  BLI_path_split_dir_part(path.c_str(), dir, sizeof(dir));
  return std::string(dir);
}

static inline std::string join_dir_file(std::string dir, std::string file)
{
  return path_join(dir, file);
}

static std::string resolve_octane_vdb_path(PointerRNA &oct_mesh,
                                           BL::BlendData &b_data,
                                           BL::Scene &b_scene)
{
  int start_playing_at = RNA_int_get(&oct_mesh, "openvdb_frame_start_playing_at");
  int current_frame = b_scene.frame_current();
  int current_frame_for_vdb = std::max(0, current_frame - start_playing_at);
  int start_frame = RNA_int_get(&oct_mesh, "openvdb_frame_start");
  int end_frame = RNA_int_get(&oct_mesh, "openvdb_frame_end");
  float openvdb_frame_speed_mutiplier = RNA_float_get(&oct_mesh, "openvdb_frame_speed_mutiplier");
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
  return blender_absolute_path(b_data, b_scene, vdbFileStr);
}

static bool osl_node_configuration(Main *main,
                                   BL::ShaderNode &b_node,
                                   OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo)
{
  /* add new sockets from parameters */
  set<void *> used_sockets;
  for (int i = 0; i < oslNodeInfo.mPinInfo.size(); ++i) {
    /* determine socket type */
    string socket_type;
    BL::NodeSocket::type_enum data_type = BL::NodeSocket::type_VALUE;
    float4 default_float4 = make_float4(0.0f, 0.0f, 0.0f, 1.0f);
    float default_float = 0.0f;
    int default_int = 0;
    int default_enum = 0;
    bool default_bool = false;
    string default_string = "";

    const OctaneDataTransferObject::ApiNodePinInfo &pinInfo = oslNodeInfo.mPinInfo.get_param(i);
    string socket_name = pinInfo.mLabelName;
    string identifier = pinInfo.mName;

    switch (pinInfo.mType) {
      case Octane::PT_TRANSFORM:
      case Octane::PT_PROJECTION:
        socket_type = "NodeSocketShader";
        data_type = BL::NodeSocket::type_SHADER;
        break;
      case Octane::PT_TEXTURE:
        socket_type = "NodeSocketFloat";
        data_type = BL::NodeSocket::type_VALUE;
        default_float = pinInfo.mFloatInfo.mDefaultValue.x;
        break;
      case Octane::PT_STRING:
        socket_type = "NodeSocketString";
        data_type = BL::NodeSocket::type_STRING;
        default_string = pinInfo.mStringInfo.mDefaultValue;
        break;
      case Octane::PT_BOOL:
        socket_type = "NodeSocketBool";
        data_type = BL::NodeSocket::type_BOOLEAN;
        default_bool = pinInfo.mBoolInfo.mDefaultValue;
        break;
      case Octane::PT_ENUM:
        socket_type = "NodeSocketInt";
        data_type = BL::NodeSocket::type_INT;
        default_enum = pinInfo.mEnumInfo.mDefaultValue;
        break;
      case Octane::PT_FLOAT:
        if (pinInfo.mFloatInfo.mIsColor) {
          socket_type = "NodeSocketColor";
          data_type = BL::NodeSocket::type_RGBA;
          default_float4[0] = pinInfo.mFloatInfo.mDefaultValue.x;
          default_float4[1] = pinInfo.mFloatInfo.mDefaultValue.y;
          default_float4[2] = pinInfo.mFloatInfo.mDefaultValue.z;
        }
        else if (pinInfo.mFloatInfo.mDimCount > 1) {
          socket_type = "NodeSocketVector";
          data_type = BL::NodeSocket::type_VECTOR;
          default_float4[0] = pinInfo.mFloatInfo.mDefaultValue.x;
          default_float4[1] = pinInfo.mFloatInfo.mDefaultValue.y;
          default_float4[2] = pinInfo.mFloatInfo.mDefaultValue.z;
        }
        else {
          socket_type = "NodeSocketFloat";
          data_type = BL::NodeSocket::type_VALUE;
          default_float = pinInfo.mFloatInfo.mDefaultValue.x;
        }
        break;
      case Octane::PT_INT:
        if (pinInfo.mIntInfo.mIsColor) {
          socket_type = "NodeSocketColor";
          data_type = BL::NodeSocket::type_RGBA;
          default_float4[0] = pinInfo.mIntInfo.mDefaultValue.x;
          default_float4[1] = pinInfo.mIntInfo.mDefaultValue.y;
          default_float4[2] = pinInfo.mIntInfo.mDefaultValue.z;
        }
        else if (pinInfo.mIntInfo.mDimCount > 1) {
          socket_type = "NodeSocketVector";
          data_type = BL::NodeSocket::type_VECTOR;
          default_float4[0] = pinInfo.mIntInfo.mDefaultValue.x;
          default_float4[1] = pinInfo.mIntInfo.mDefaultValue.y;
          default_float4[2] = pinInfo.mIntInfo.mDefaultValue.z;
        }
        else {
          socket_type = "NodeSocketInt";
          data_type = BL::NodeSocket::type_INT;
          default_int = pinInfo.mIntInfo.mDefaultValue.x;
        }
        break;
      default:
        continue;
    }
    /* find socket socket */
    BL::NodeSocket b_sock(PointerRNA_NULL);
    if (pinInfo.mIsOutput) {
      b_sock = b_node.outputs[socket_name];
      // LEGACY ISSUES
      // Before 16.3.2, blender uses mName as socket name.
      // After 16.3.2, blender uses mLabelName as socket name.
      // To solve the backward compatibility issue, server send both
      // therefore, client can solve backward compatibility issues
      if (!b_sock) {
        b_sock = b_node.outputs[identifier];
        if (b_sock && socket_name.size() > 0) {
          b_sock.name(socket_name);
        }
      }
      /* remove if type no longer matches */
      if (b_sock && b_sock.bl_idname() != socket_type) {
        b_node.outputs.remove(main, b_sock);
        b_sock = BL::NodeSocket(PointerRNA_NULL);
      }
    }
    else {
      b_sock = b_node.inputs[socket_name];
      if (!b_sock) {
        b_sock = b_node.inputs[identifier];
        if (b_sock && socket_name.size() > 0) {
          b_sock.name(socket_name);
        }
      }
      /* remove if type no longer matches */
      if (b_sock && b_sock.bl_idname() != socket_type) {
        b_node.inputs.remove(main, b_sock);
        b_sock = BL::NodeSocket(PointerRNA_NULL);
      }
    }

    if (!b_sock) {
      /* create new socket */
      if (pinInfo.mIsOutput)
        b_sock = b_node.outputs.create(
            main, socket_type.c_str(), socket_name.c_str(), identifier.c_str());
      else
        b_sock = b_node.inputs.create(
            main, socket_type.c_str(), socket_name.c_str(), identifier.c_str());

      /* set default value */
      if (data_type == BL::NodeSocket::type_VALUE) {
        set_float(b_sock.ptr, "default_value", default_float);
      }
      else if (data_type == BL::NodeSocket::type_INT) {
        set_int(b_sock.ptr, "default_value", default_int);
      }
      else if (data_type == BL::NodeSocket::type_RGBA) {
        set_float4(b_sock.ptr, "default_value", default_float4);
      }
      else if (data_type == BL::NodeSocket::type_VECTOR) {
        set_float3(b_sock.ptr, "default_value", float4_to_float3(default_float4));
      }
      else if (data_type == BL::NodeSocket::type_STRING) {
        set_string(b_sock.ptr, "default_value", default_string);
      }
    }

    used_sockets.insert(b_sock.ptr.data);
  }

  /* remove unused parameters */
  bool removed;

  do {
    BL::Node::inputs_iterator b_input;
    BL::Node::outputs_iterator b_output;

    removed = false;

    for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
      if (used_sockets.find(b_input->ptr.data) == used_sockets.end()) {
        b_node.inputs.remove(main, *b_input);
        removed = true;
        break;
      }
    }

  } while (removed);

  return true;
}

static bool is_blender_internal_vdb_format(int format)
{
  // FLUID_DOMAIN_FILE_UNI = (1 << 0),
  // FLUID_DOMAIN_FILE_OPENVDB = (1 << 1)
  return format == (1 << 1) || format == (1 << 0);
}

static std::string resolve_octane_geometry_node(PointerRNA &obj)
{
  PointerRNA octane_object = RNA_pointer_get(&obj, "octane");
  std::string sScriptGeoName;
  char scriptGeoMaterialName[512];
  char scriptGeoNodeName[512];
  RNA_string_get(&octane_object, "node_graph_tree", scriptGeoMaterialName);
  RNA_string_get(&octane_object, "osl_geo_node", scriptGeoNodeName);
  std::string scriptGeoMaterialNameStr(scriptGeoMaterialName);
  std::string scriptGeoNodeNameStr(scriptGeoNodeName);
  if (scriptGeoMaterialNameStr.size() && scriptGeoNodeNameStr.size()) {
    sScriptGeoName = scriptGeoMaterialNameStr + "_" + scriptGeoNodeNameStr;
  }
  return sScriptGeoName;
}

static void resolve_octane_ocio_view_params(std::string &display, std::string &display_view)
{
  if (display == "sRGB" && display_view == "Raw") {
    display = "";
    display_view == "None";
  }
}

static void resolve_octane_ocio_look_params(std::string &look)
{
  if (look == " None ") {
    look = "";
  }
  else if (look == " Use view look(s) ") {
    look = "Use view look(s)";
  }
}

OCT_NAMESPACE_END

#endif /* __BLENDER_UTIL_H__ */
