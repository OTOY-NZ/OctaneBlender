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

#include "environment.h"
#include "server.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Environment::Environment() {
    type                = 0;
    rotation.x          = 0;
    rotation.y          = 0;
    texture             = "";
    importance_sampling = 1;
    daylight_type       = 0;
    sun_vector.x        = 0;
    sun_vector.y        = 1;
    sun_vector.z        = 0;
    power               = 1.0f;
    longitude           = 4.4667f;
    latitude            = 50.7667f;
    hour                = 14;
    month               = 3;
    day                 = 1;
    gmtoffset           = 0;
    turbidity           = 2.2f;
    northoffset         = 0;
    model               = 1;
    sun_size            = 1.0f;

    sky_color.x         = 0.05f;
    sky_color.y         = 0.3f;
    sky_color.z         = 1.0f;

    sunset_color.x      = 0.6f;
    sunset_color.y      = 0.12f;
    sunset_color.z      = 0.02;

	use_background      = true;
	transparent         = false;
	need_update         = true;
} //Environment()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Environment::~Environment() {
} //~Environment()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Environment::server_update(RenderServer *server, Scene *scene) {
	if(!need_update) return;
	
    server->load_environment(this);
	need_update = false;
} //server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Environment::modified(const Environment& environment) {
	return !(
        type == environment.type &&
		rotation == environment.rotation &&
		texture == environment.texture &&
		importance_sampling == environment.importance_sampling &&
		daylight_type == environment.daylight_type &&
		sun_vector == environment.sun_vector &&
		power == environment.power &&
		longitude == environment.longitude &&
		latitude == environment.latitude &&
		hour == environment.hour &&
		month == environment.month &&
		day == environment.day &&
		gmtoffset == environment.gmtoffset &&
		turbidity == environment.turbidity &&
		northoffset == environment.northoffset &&
		model == environment.model &&
		sun_size == environment.sun_size &&
		sky_color == environment.sky_color &&
		sunset_color == environment.sunset_color);
} //modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Environment::tag_update(Scene *scene) {
	need_update = true;
} //tag_update()

OCT_NAMESPACE_END

