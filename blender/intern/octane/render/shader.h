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

#ifndef __SHADER_H__
#define __SHADER_H__

#include "graph/node.h"

#include "util/util_map.h"
#include "util/util_param.h"
#include "util/util_string.h"
#include "util/util_thread.h"
#include "util/util_types.h"

#include "blender/rpc/definitions/OctanePinInfo.h"
#include <unordered_map>

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class ShaderGraph;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Shader {
 public:
  Shader();
  ~Shader();

  void set_graph(ShaderGraph *graph);
  void tag_update(Scene *scene);
  void tag_used(Scene *scene);

  string name;
  int pass_id;
  ShaderGraph *graph;

  bool need_update;
  bool need_update_mesh;
  bool need_sync_object;

  /* information about shader after compiling */
  bool has_surface;
  bool has_volume;
  bool has_object_dependency;
  bool has_attribute_dependency;

  /* determined before compiling */
  uint id;
  bool used;
};  // Shader

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderManager {
 public:
  ShaderManager();

  static ShaderManager *create(Scene *scene);

  void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, Progress &progress);
  static void add_default(Scene *scene);

  bool need_update;

};  // ShaderManager

OCT_NAMESPACE_END

#endif /* __SHADER_H__ */
