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

#ifndef __SHADER_H__
#define __SHADER_H__

#include "util_string.h"

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

class RenderServer;
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

    string      name;
	int         pass_id;
	ShaderGraph *graph;
	bool        need_update;
}; //Shader

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ShaderManager {
public:
	ShaderManager();

	static ShaderManager *create(Scene *scene);

	void        server_update(RenderServer *server, Scene *scene, Progress& progress);
	static void add_default(Scene *scene);

	bool need_update;
}; //ShaderManager

OCT_NAMESPACE_END

#endif /* __SHADER_H__ */

