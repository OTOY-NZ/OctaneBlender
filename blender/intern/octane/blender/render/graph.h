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

#ifndef __GRAPH_H__
#define __GRAPH_H__

#include "util_lists.h"
#include "util_types.h"

OCT_NAMESPACE_BEGIN

class ShaderInput;
class ShaderOutput;
class ShaderNode;
class ShaderGraph;
class RenderServer;

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
}; //ShaderSocketType

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Input
// Input socket for a shader node. May be linked to an output or not. If not
// linked, it will either get a fixed default value, or e.g. a texture coordinate.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderInput {
public:
	ShaderInput(ShaderNode *parent, const char *name, ShaderSocketType type);
	void set(const float3& v) { value = v; }
	void set(float f) { value = make_float3(f, 0, 0); }

	const char          *name;
	ShaderSocketType    type;

	ShaderNode          *parent;
	ShaderOutput        *link;

	float3              value;
}; //ShaderInput

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Output
// Output socket for a shader node.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderOutput {
public:
	ShaderOutput(ShaderNode *parent, const char *name, ShaderSocketType type);

	const char          *name;
	ShaderNode          *parent;
	ShaderSocketType    type;

	vector<ShaderInput*> links;
}; //ShaderOutput

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Node
// Shader node in graph, with input and output sockets. This is the virtual base class for all node types.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderNode {
public:
	ShaderNode(const char *name);
	virtual ~ShaderNode();

	ShaderInput *input(const char *name);
	ShaderOutput *output(const char *name);

    virtual void load_to_server(RenderServer* server) = 0;

	vector<ShaderInput*>  inputs;
	vector<ShaderOutput*> outputs;

    std::string name; // name, not required to be unique
	int         id;   // index in graph node array
    int         pass_id;
}; //ShaderNode


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Node definition utility macros
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define SHADER_NODE_CLASS(type) \
	type(); \
    virtual void load_to_server(RenderServer* server); \

#define SHADER_NODE_NO_CLONE_CLASS(type) \
	type(); \
    virtual void load_to_server(RenderServer* server); \

#define SHADER_NODE_BASE_CLASS(type) \
    virtual void load_to_server(RenderServer* server); \

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

	list<ShaderNode*> nodes;

protected:
}; //ShaderGraph

OCT_NAMESPACE_END

#endif /* __GRAPH_H__ */

