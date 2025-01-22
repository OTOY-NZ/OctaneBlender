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

#include "render/shader.h"
#include "render/graph.h"
#include "render/scene.h"
#include <boost/algorithm/string.hpp>

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// SHADER NODE
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Shader::Shader()
{
  name = "";
  pass_id = 0;
  graph = 0;

  has_surface = false;
  has_volume = false;

  need_update = true;
  need_update_paint = false;
  need_update_mesh = false;
  need_sync_object = false;
  has_object_dependency = false;
  has_attribute_dependency = false;

  id = -1;
  used = false;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Shader::~Shader()
{
  delete graph;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Assign current graph
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Shader::set_graph(ShaderGraph *graph_)
{
  if (graph)
    delete graph;
  graph = graph_;
  has_object_dependency |= graph->has_object_dependency;
}  // set_graph()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Shader::tag_update(Scene *scene)
{
  need_update = true;
  scene->shader_manager->need_update = true;
}  // tag_update()

void Shader::tag_used(Scene *scene)
{
  /* if an unused shader suddenly gets used somewhere, it needs to be
   * recompiled because it was skipped for compilation before */
  if (!used) {
    need_update = true;
    scene->shader_manager->need_update = true;
  }
}

bool Shader::is_empty()
{
  if (graph && graph->nodes.size() == 1) {
    ShaderNode* node = graph->nodes.front();    
    if (node && node->oct_node) {
      std::string name = node->oct_node->sName;
      return boost::ends_with(name, "Material Output");
    }
  }
  return false;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// SHADER MANAGER
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ShaderManager::ShaderManager() : need_update(true) {}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ShaderManager *ShaderManager::create(Scene *scene)
{
  ShaderManager *manager = new ShaderManager();
  add_default(scene);

  return manager;
}  // create()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ShaderManager::server_update(::OctaneEngine::OctaneClient *server,
                                  Scene *scene,
                                  Progress &progress)
{
  if (!need_update)
    return;

  size_t cnt = scene->shaders.size();
  if (!cnt)
    return;

  for (size_t i = 0; i < cnt; ++i) {
    if (scene->is_addon_mode()) {
      break;
    }

    Shader *shader = scene->shaders[i];
    if (!shader->need_update)
      continue;
    if (!shader->graph)
      continue;

    for (list<ShaderNode *>::iterator it = shader->graph->nodes.begin();
         it != shader->graph->nodes.end();
         ++it)
    {
      ShaderNode *node = *it;
      if (node->input("Surface"))
        continue;
      if (node->oct_node && node->oct_node->sName.length()) {
        node->load_to_server(server);
      }
    }
    shader->used = true;
    shader->need_update = false;
  }
  need_update = false;
}  // server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Add default shaders to scene, to use as default for things that don't have any shader assigned
// explicitly
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void ShaderManager::add_default(Scene *scene)
{
  // Add default surface material
  ShaderGraph *graph = new ShaderGraph();
 
  Shader *shader = new Shader();
  shader->name = "default_surface";
  shader->graph = graph;
  scene->shaders.push_back(shader);
  scene->default_surface = shader;

  // Add default emission
  ShaderGraph *light_graph = new ShaderGraph();

  Shader *light_shader = new Shader();
  light_shader->name = "default_light";
  light_shader->graph = light_graph;
  scene->shaders.push_back(light_shader);
  scene->default_light = light_shader;

  ShaderGraph *environment_graph = new ShaderGraph();
  Shader *environment_shader = new Shader();
  environment_shader->name = "Environment";
  environment_shader->graph = environment_graph;
  scene->shaders.push_back(environment_shader);
  scene->default_environment = environment_shader;

  ShaderGraph *composite_graph = new ShaderGraph();
  Shader *composite_shader = new Shader();
  composite_shader->name = "Composite";
  composite_shader->graph = composite_graph;
  scene->shaders.push_back(composite_shader);
  scene->default_composite = composite_shader;

  ShaderGraph *render_aov_graph = new ShaderGraph();
  Shader *render_aov_shader = new Shader();
  render_aov_shader->name = "Composite";
  render_aov_shader->graph = render_aov_graph;
  scene->shaders.push_back(render_aov_shader);
  scene->default_render_aov_node_tree = render_aov_shader;

}  // add_default()

OCT_NAMESPACE_END
