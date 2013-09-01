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

#ifndef __BLENDER_SESSION_H__
#define __BLENDER_SESSION_H__

#include <cstdlib>
#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

#include "util_string.h"

OCT_NAMESPACE_BEGIN

class Scene;
class Session;
class BlenderSync;

typedef enum PassType {
    PASS_NONE               = 0,
    PASS_COMBINED           = 1,
    PASS_DEPTH              = 2,
    PASS_GEO_NORMALS        = 4,
    PASS_SHADING_NORMALS    = 8,
    PASS_MATERIAL_ID        = 16,
    PASS_POSITION           = 32,
    PASS_TEX_COORD          = 64
} PassType;
#define NUM_PASSES 7

class Pass {
public:
	PassType type;
	int components;

	static void add(PassType type, vector<Pass>& passes);
	static bool equals(const vector<Pass>& A, const vector<Pass>& B);
	static bool contains(const vector<Pass>& passes, PassType);
};

class BlenderSession {
public:
	BlenderSession(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::BlendData b_data, BL::Scene b_scene);
	BlenderSession(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::BlendData b_data, BL::Scene b_scene,
		           BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height);

	~BlenderSession();

	// session
	void create_session(PassType pass_type);
	void free_session();

    void reset_session(BL::BlendData b_data, BL::Scene b_scene);
	void reload_session();

	// offline render
	void render();

	void write_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay);
	void write_render_img();

	// update functions are used to update display buffer only after sample was rendered
	// only needed for better visual feedback
	void update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay);
	void update_render_img();

	// interactive updates
	void synchronize();

	// drawing
	bool draw(int w, int h);
	void tag_redraw();
	void tag_update();
	void get_status(string& status, string& substatus);
	void get_progress(float& progress, double& total_time);
	void test_cancel();
	void update_status_progress();

	bool        interactive;
	Session     *session;
	Scene       *scene;
	BlenderSync *sync;
	double      last_redraw_time;
    PassType    cur_pass_type;
    int         num_passes;
    int         ready_passes;
    float*      pass_buffers[NUM_PASSES];

	BL::RenderEngine    b_engine;
	BL::UserPreferences b_userpref;
	BL::BlendData       b_data;
	BL::Scene           b_scene;
	BL::SpaceView3D     b_v3d;
	BL::RegionView3D    b_rv3d;
	string              b_rlay_name;

	string  last_status;
	float   last_progress;

	int width, height;

protected:
	void do_write_update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay, bool do_update_only);
	void do_write_update_render_img(bool do_update_only);
};

OCT_NAMESPACE_END

#endif /* __BLENDER_SESSION_H__ */
