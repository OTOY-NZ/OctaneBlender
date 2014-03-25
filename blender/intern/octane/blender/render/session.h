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

#ifndef __SESSION_H__
#define __SESSION_H__

#include "buffers.h"
#include "server.h"
#include "mesh.h"

#include "util_progress.h"
#include "util_thread.h"

OCT_NAMESPACE_BEGIN

class Progress;
class Scene;
class BlenderSession;

enum AnimationMode {
    FULL = 0,
    MOVABLE_PROXIES,
    CAM_ONLY
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Session Parameters
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class SessionParams {
public:
	SessionParams() {
		interactive     = true;
		output_path     = "";
        use_passes      = false;
        meshes_type     = Mesh::AS_IS;
		samples		    = INT_MAX;
        export_alembic  = false;
        anim_mode       = FULL;
        fps             = 24.0f;
	}

	bool modified(const SessionParams& params) {
		return !(
            anim_mode == params.anim_mode
			&& interactive == params.interactive
			&& meshes_type == params.meshes_type
			&& use_viewport_hide == params.use_viewport_hide
			&& use_passes == params.use_passes
			&& output_path == params.output_path);
	}

	RenderServerInfo    server;
    string              login;
    string              pass;
    string              stand_login;
    string              stand_pass;
	bool		        interactive;
	string		        output_path;

	int		        samples;
    ImageStatistics image_stat;

    AnimationMode   anim_mode;
    int             width;
    int             height;
	bool            use_passes;
	bool            use_viewport_hide;
	Mesh::MeshType  meshes_type;
	bool            export_alembic;
    float           fps;
}; //SessionParams

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Session
// This is the class that contains the session thread, running the render control loop.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Session {
public:
    Session(const SessionParams& params, const char *_out_path);
	~Session();

	void start(const char* pass_name_, bool synchronous);
	bool draw(BufferParams& params);
	void wait();

	bool ready_to_reset();
	void reset(BufferParams& params, int samples);
	void set_samples(int samples);
	void set_pause(bool pause);
    void set_blender_session(BlenderSession *b_session_);

    void update(BufferParams& params, int samples);
    void update_params(SessionParams& session_params);
	void update_scene_to_server();

	RenderServer	*server;
	Scene			*scene;
	DisplayBuffer	*display;//Only for INTERACTIVE session
	Progress		progress;
	SessionParams	params;
    BlenderSession  *b_session;

protected:
	void run();
	void update_status_time(bool show_pause = false, bool show_done = false);

	void update_render_buffer();
	void reset_parameters(BufferParams& buffer_params, int samples);

	void run_cpu();
	bool draw_cpu(BufferParams& params);
	void reset_cpu(BufferParams& params, int samples);

	void run_render();
	void update_img_sample(void);

	thread          *session_thread;
	volatile bool   display_outdated;

	bool            pause;
	thread_mutex    pause_mutex;
	thread_mutex    img_mutex;
	thread_mutex    render_buffer_mutex;
	thread_mutex    display_mutex;
	thread_condition_variable pause_cond;

	double start_time;
	double reset_time;
	double paused_time;
    double last_update_time;

    const char* pass_name;
}; //Session

OCT_NAMESPACE_END

#endif /* __SESSION_H__ */

