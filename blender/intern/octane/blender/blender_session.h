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
#include "passes.h"

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

class Scene;
class Session;
class BlenderSync;

class BlenderSession {
public:
    enum MotionBlurType {
        INTERNAL = 0,
        SUBFRAME
    };
    enum MotionBlurDirection {
        AFTER = 0,
        BEFORE,
        SYMMETRIC
    };

	BlenderSession(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::BlendData b_data, BL::Scene b_scene);
	BlenderSession(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::BlendData b_data, BL::Scene b_scene,
		           BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height);

	~BlenderSession();

    static bool activate(BL::Scene b_scene_);

	// session
    void create_session();
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

	bool                interactive;
	Session             *session;
	Scene               *scene;
	BlenderSync         *sync;
	double              last_redraw_time;
    float*              pass_buffers[Passes::NUM_PASSES];
    float*              mb_pass_buffers[Passes::NUM_PASSES];

    bool                motion_blur;
    int                 mb_samples;
    MotionBlurType      mb_type;
    MotionBlurDirection mb_direction;
    float               mb_frames_cnt, mb_frame_time_sampling;
    int                 mb_first_frame, mb_last_frame;

	BL::RenderEngine    b_engine;
	BL::UserPreferences b_userpref;
	BL::BlendData       b_data;
	BL::Scene           b_scene;
	BL::SpaceView3D     b_v3d;
	BL::RegionView3D    b_rv3d;
	string              b_rlay_name;
	string              b_rview_name;

	string  last_status;
	float   last_progress;

	int width, height;

protected:
	void        do_write_update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay, bool do_update_only);
	void        do_write_update_render_img(bool do_update_only);

    int         load_internal_mb_sequence(bool &stop_render, BL::RenderLayer *layer = 0, bool do_sync = false);

    float shuttertime;
    int   mb_cur_sample;
    int   mb_sample_in_work;

private:
    inline void                         clear_passes_buffers();
    inline Passes::PassTypes            get_octane_pass_type(BL::RenderPass b_pass);
    inline BL::RenderPass::type_enum    get_blender_pass_type(Passes::PassTypes pass);
    inline int                          get_pass_index(Passes::PassTypes pass);
};

OCT_NAMESPACE_END

#endif /* __BLENDER_SESSION_H__ */
