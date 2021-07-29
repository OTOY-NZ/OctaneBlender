/*
 * Copyright 2011-2016 Blender Foundation
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

#ifndef __GRAPH_H__
#define __GRAPH_H__

#include "graph/node.h"
#include "graph/node_type.h"

#include "util/util_list.h"
#include "util/util_map.h"
#include "util/util_param.h"
#include "util/util_set.h"
#include "util/util_types.h"
#include "util/util_vector.h"

#include "blender/server/OctaneClient.h"

OCT_NAMESPACE_BEGIN

class ShaderInput;
class ShaderOutput;
class ShaderNode;
class ShaderGraph;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Socket Type
// Data type for inputs and outputs
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
enum ShaderSocketType {
  SHADER_SOCKET_BOOL,
  SHADER_SOCKET_INT,
  SHADER_SOCKET_FLOAT,
  SHADER_SOCKET_COLOR,
  SHADER_SOCKET_STRING,
  SHADER_SOCKET_SHADER
};  // ShaderSocketType

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Input
// Input socket for a shader node. May be linked to an output or not. If not
// linked, it will either get a fixed default value, or e.g. a texture coordinate.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderInput {
 public:
  ShaderInput(ShaderNode *parent, const char *name, ShaderSocketType type);
  void set(const float3 &v)
  {
    value = v;
  }
  void set(float f)
  {
    value = make_float3(f, 0, 0);
  }

  const char *name;
  ShaderSocketType type;

  ShaderNode *parent;
  ShaderOutput *link;

  float3 value;
};  // ShaderInput

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Output
// Output socket for a shader node.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderOutput {
 public:
  ShaderOutput(ShaderNode *parent, const char *name, ShaderSocketType type);

  const char *name;
  ShaderNode *parent;
  ShaderSocketType type;

  vector<ShaderInput *> links;
};  // ShaderOutput

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Node
// Shader node in graph, with input and output sockets. This is the virtual base class for all node
// types.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderNode {
 public:
  ShaderNode(::OctaneDataTransferObject::OctaneNodeBase *node_);
  virtual ~ShaderNode();

  ShaderInput *input(const char *name);
  ShaderOutput *output(const char *name);

  virtual void load_to_server(::OctaneEngine::OctaneClient *server)
  {
    if (oct_node)
      server->uploadNode(oct_node);
  }
  virtual void delete_from_server(::OctaneEngine::OctaneClient *server)
  {
    if (oct_node)
      server->deleteNode(oct_node);
  }

  vector<ShaderInput *> inputs;
  vector<ShaderOutput *> outputs;

  // std::string name; // name, not required to be unique
  int id;  // index in graph node array
  int pass_id;

  ::OctaneDataTransferObject::OctaneNodeBase *oct_node;
};  // ShaderNode

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Graph
// Shader graph of nodes. Also does graph manipulations for default inputs,
// bump mapping from displacement, and possibly other things in the future.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderGraph {
 public:
  ShaderGraph();
  ~ShaderGraph();

  ShaderNode *add(ShaderNode *node);
  ShaderNode *output();

  list<ShaderNode *> nodes;

 protected:
};  // ShaderGraph

OCT_NAMESPACE_END

#endif /* __GRAPH_H__ */
