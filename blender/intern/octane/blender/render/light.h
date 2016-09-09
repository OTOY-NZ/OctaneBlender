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

#ifndef __LIGHT_H__
#define __LIGHT_H__

#include "util_types.h"
#include "util_lists.h"
#include "util_string.h"

#include "memleaks_check.h"

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class Mesh;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Light {
public:
	Light();
    ~Light();

	void tag_update(Scene *scene);

    typedef enum LightType {
        LIGHT_POINT,
        LIGHT_DISTANT,
        LIGHT_BACKGROUND,
        LIGHT_AREA,
        LIGHT_AO,
        LIGHT_SPOT
    } LightType;

    string      name;
    string      nice_name;
    LightType   type;
	float       size;

    Mesh  *mesh;
    bool  need_update;

	float sizeu;
	float sizev;

	float spot_angle;
	float spot_smooth;

    bool enable;
}; //Light

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class LightManager {
public:
	LightManager();
	~LightManager();

    void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, Progress& progress, uint32_t frame_idx, uint32_t total_frames);
	void tag_update(Scene *scene);

	bool need_update;
}; //LightManager

OCT_NAMESPACE_END

#endif /* __LIGHT_H__ */

