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

#include <string.h>
#include <limits.h>

#include "session.h"
#include "buffers.h"
#include "server.h"
#include "scene.h"

#include "blender_session.h"

#include "util_math.h"
#include "util_opengl.h"
#include "util_time.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Session::Session(const SessionParams& params_, const char *_out_path) : params(params_) {
	server = RenderServer::create(params.server, params.export_alembic, _out_path, params.interactive);

    if(params.login.length() > 0 && params.pass.length() > 0) {
        if(server->activate(params.stand_login, params.stand_pass, params.login, params.pass)) {
            params.stand_login  = "";
            params.stand_pass   = "";
            params.login        = "";
            params.pass         = "";
        }
    }

	if(!params.interactive)
		display = NULL;
	else
		display = new DisplayBuffer(server);

	session_thread  = 0;
	scene           = 0;
    b_session       = 0;  

	start_time      = 0.0;
	reset_time      = 0.0;
	paused_time     = 0.0;

	display_outdated    = false;
	pause               = false;
} //Session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Session::~Session() {
	if(session_thread) {
		progress.set_cancel("Exiting");
		{
			thread_scoped_lock pause_lock(pause_mutex);
			pause = false;
		}
		pause_cond.notify_all();
		wait();
	}
	if(display && params.output_path != "") {
		progress.set_status("Writing Image", params.output_path);
		display->write(params.output_path);
	}
	if(display) delete display;
	if(scene) delete scene;

	delete server;
} //~Session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test the timeout to reset the session
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Session::ready_to_reset() {
    return true;
    //return ((time_dt() - reset_time) > 1.0); //params.reset_timeout
} //ready_to_reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Runs the new rendering loop
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::start(const char* pass_name_, bool synchronous) {
    pass_name = pass_name_;
    if(!synchronous)
        //FIXME: kill this boost here
        session_thread = new thread(boost::bind(&Session::run, this));
    else
        run();
} //start()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render loop
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::run_render() {
	reset_time          = start_time = time_dt();
	paused_time         = 0.0;
    bool bStarted       = false;

    if(params.interactive) progress.set_start_time(start_time);

	while(!progress.get_cancel()) {
		bool is_done = !params.interactive && (params.image_stat.cur_samples >= params.samples);

		if(!params.interactive) {
			// If no work left and in background mode, we can stop immediately
			if(is_done) {
            	update_status_time();
				progress.set_status(string(pass_name) + " finished");
				break;
			}
		} //if(!params.interactive)
		else {
			// If in interactive mode, and we are either paused or done for now,
			// wait for pause condition notify to wake up again
			thread_scoped_lock pause_lock(pause_mutex);
			if(pause || is_done) {
				update_status_time(pause, is_done);
				while(true) {
                    if(pause) server->pause_render(true);

					double pause_start = time_dt();
					pause_cond.wait(pause_lock);
					paused_time += time_dt() - pause_start;

				    progress.set_start_time(start_time + paused_time);
					update_status_time(pause, is_done);
					progress.set_update();

                    if(!pause) {
                        server->pause_render(false);
                        break;
                    }
				}
			} //if(pause || is_ready)
			if(progress.get_cancel()) break;
		} //if(!params.interactive), else

		if(!is_done) {
            time_sleep(0.01);

			// Update scene on the render-server - send all changed objects
			update_scene_to_server();
            if(!bStarted) {
                server->start_render(params.width, params.height, params.interactive ? 0 : 2); //FIXME: Perhaps the wrong place for it...
                bStarted = true;
            }
            if(!server->error_message().empty()) {
                progress.set_cancel("ERROR! Check console for detailed error messages.");
                server->clear_error_message();
            }
			if(progress.get_cancel()) break;

			// Buffers mutex is locked entirely while rendering each
			// sample, and released/reacquired on each iteration to allow
			// reset and draw in between
			thread_scoped_lock buffers_lock(render_buffer_mutex);

			// Update status and timing
			update_status_time();

            update_render_buffer();
            if(!server->error_message().empty()) {
                progress.set_cancel("ERROR! Check console for detailed error messages.");
                server->clear_error_message();
            }

			// Update status and timing
			update_status_time();
			progress.set_update();
		} //if(!is_done)
        else {
			thread_scoped_lock buffers_lock(render_buffer_mutex);
			// Update status and timing
			update_status_time();
            update_render_buffer();
        }
	} //while(!progress.get_cancel())
} //run_render()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Main Render function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::run() {
    progress.set_status("Waiting for render to start");

	if(!progress.get_cancel()) {
		progress.reset_cur_samples();
        run_render();
	}
	// Progress update
	if(progress.get_cancel())
		progress.set_status("Cancel", progress.get_cancel_message());
	else
		progress.set_update();
} //run()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Interactive drawing
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Session::draw(BufferParams& buffer_params) {
	// Block for display buffer access
	thread_scoped_lock display_lock(display_mutex);

    // First check we already rendered something
	// then verify the buffers have the expected size, so we don't
	// draw previous results in a resized window
	if(!buffer_params.modified(display->params)) {
		return display->draw(server);

		if(display_outdated)// && (time_dt() - reset_time) > params.text_timeout)
			return false;

		return true;
	}
	else return false;
} //draw()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::reset_parameters(BufferParams& buffer_params, int samples) {
    if(display) {
		if(buffer_params.modified(display->params)) {
			display->reset(buffer_params);
		}
	}
	start_time      = time_dt();
	paused_time     = 0.0;

    params.image_stat.cur_samples = 0;
	if(params.interactive) progress.set_start_time(start_time + paused_time);
} //reset_parameters()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reset all session data buffers
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::reset(BufferParams& buffer_params, int samples) {
	// Block for buffer acces and reset immediately. we can't do this
	// in the thread, because we need to allocate an OpenGL buffer, and
	// that only works in the main thread
	thread_scoped_lock display_lock(display_mutex);
	thread_scoped_lock render_buffer_lock(render_buffer_mutex);

	display_outdated    = true;
	reset_time          = time_dt();

	reset_parameters(buffer_params, samples);
    server->reset(scene->kernel->uiGPUs);
	pause_cond.notify_all();
} //reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render project on the render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update(BufferParams& buffer_params, int samples) {
	// Block for buffer acces and reset immediately. we can't do this
	// in the thread, because we need to allocate an OpenGL buffer, and
	// that only works in the main thread
	thread_scoped_lock display_lock(display_mutex);
	thread_scoped_lock render_buffer_lock(render_buffer_mutex);

	display_outdated    = true;
	reset_time          = time_dt();

	reset_parameters(buffer_params, samples);
    //server->update();
	pause_cond.notify_all();
} //update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Set max. samples value
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::set_samples(int samples) {
	if(samples != params.samples) {
		params.samples = samples;
		//{
		//	thread_scoped_lock pause_lock(pause_mutex);
        //  pause = false;
		//}
		//pause_cond.notify_all();
	}
} //set_samples()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Set current pause state
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::set_pause(bool pause_) {
	bool notify = false;
	{
		thread_scoped_lock pause_lock(pause_mutex);
		if(pause != pause_) {
			pause  = pause_;
			notify = true;
		}
	}
	if(notify) pause_cond.notify_all();
} //set_pause()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Wait for render thread finish...
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::wait() {
	session_thread->join();
	delete session_thread;

	session_thread = 0;
} //wait()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Set the parent blender session
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::set_blender_session(BlenderSession *b_session_) {
    if(!b_session_->interactive) b_session = b_session_;
	progress.set_blender_session(b_session_);
} //set_blender_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Updates the data on the render-server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_scene_to_server() {
	thread_scoped_lock scene_lock(scene->mutex);

	// Update camera if dimensions changed for progressive render. The camera
	// knows nothing about progressive or cropped rendering, it just gets the
	// image dimensions passed in
	Camera  *cam    = scene->camera;
	int     width   = params.width;
	int     height  = params.height;

	if(width != cam->width || height != cam->height) {
		cam->width  = width;
		cam->height = height;
		cam->tag_update();
	}

	// Update scene
	if(params.export_alembic || scene->need_update()) {
		progress.set_status("Updating Scene");
		scene->server_update(server, progress, params.interactive);
	}
} //update_scene_to_device()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update status string with current render info
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_status_time(bool show_pause, bool show_done) {
	string status, substatus;

    if(server->socket >= 0) {
        if(params.image_stat.cur_samples > 0) {
            char szSamples[16];
            unsigned long ulSPSdivider;
            if(params.image_stat.spp < 999999) {
                ulSPSdivider = 1000;
#ifndef WIN32
                ::sprintf(szSamples, "%.2f Ks/sec", params.image_stat.spp/ulSPSdivider);
#else
                ::sprintf_s(szSamples, 15, "%.2f Ks/sec", params.image_stat.spp/ulSPSdivider);
#endif
            }
            else {
                ulSPSdivider = 1000000;
#ifndef WIN32
                ::sprintf(szSamples, "%.2f Ms/sec", params.image_stat.spp/ulSPSdivider);
#else
                ::sprintf_s(szSamples, 15, "%.2f Ms/sec", params.image_stat.spp/ulSPSdivider);
#endif
            }

            if(params.samples == INT_MAX) {
                if(params.image_stat.net_gpus > 0)
                    substatus = string_printf("Sample %d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d ) | Net GPUs: %u/%u",
                        params.image_stat.cur_samples, szSamples, params.image_stat.used_vram/1000000, params.image_stat.free_vram/1000000, params.image_stat.total_vram/1000000, params.image_stat.meshes_cnt, params.image_stat.tri_cnt,
                        params.image_stat.rgb32_cnt, params.image_stat.rgb64_cnt, params.image_stat.grey8_cnt, params.image_stat.grey16_cnt, params.image_stat.used_net_gpus, params.image_stat.net_gpus);
                else
                    substatus = string_printf("Sample %d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d ) | No net GPUs",
                        params.image_stat.cur_samples, szSamples, params.image_stat.used_vram / 1000000, params.image_stat.free_vram / 1000000, params.image_stat.total_vram / 1000000, params.image_stat.meshes_cnt, params.image_stat.tri_cnt,
                        params.image_stat.rgb32_cnt, params.image_stat.rgb64_cnt, params.image_stat.grey8_cnt, params.image_stat.grey16_cnt);
            }
	        else {
                if(params.image_stat.net_gpus > 0)
                    substatus = string_printf("Sample %d/%d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d ) | Net GPUs: %u/%u",
                        params.image_stat.cur_samples, params.samples, szSamples, params.image_stat.used_vram/1000000, params.image_stat.free_vram/1000000, params.image_stat.total_vram/1000000, params.image_stat.meshes_cnt, params.image_stat.tri_cnt,
                        params.image_stat.rgb32_cnt, params.image_stat.rgb64_cnt, params.image_stat.grey8_cnt, params.image_stat.grey16_cnt, params.image_stat.used_net_gpus, params.image_stat.net_gpus);
                else
                    substatus = string_printf("Sample %d/%d, %s | Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: ( Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d ) | No net GPUs",
                        params.image_stat.cur_samples, params.samples, szSamples, params.image_stat.used_vram / 1000000, params.image_stat.free_vram / 1000000, params.image_stat.total_vram / 1000000, params.image_stat.meshes_cnt, params.image_stat.tri_cnt,
                        params.image_stat.rgb32_cnt, params.image_stat.rgb64_cnt, params.image_stat.grey8_cnt, params.image_stat.grey16_cnt);
            }
        }
        else
            substatus = "Waiting for image...";
    	
        if(b_session && !b_session->interactive) status = pass_name;
        else status = "Interactive";

        if(show_pause)
	        status += " - Paused";
        else if(show_done)
	        status += " - Done";
        else
	        status += " - Rendering";
    }
    else {
        status      = "Not connected";
        substatus   = string("No Render-server at address \"") + server->address + "\"";
    }
	progress.set_status(status, substatus);
	progress.refresh_cur_info();
} //update_status_time()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Refresh the render-buffer and render-view with the new image from server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_render_buffer() {
    if(progress.get_cancel()) return;

    if(!server->get_image_buffer(params.image_stat, params.interactive, b_session ? b_session->cur_pass_type : PASS_COMBINED, progress) && b_session) {
        if(!params.interactive) update_img_sample();
        server->get_image_buffer(params.image_stat, params.interactive, b_session ? b_session->cur_pass_type : PASS_COMBINED, progress);
    }
    if(!params.interactive) update_img_sample();
} //update_render_buffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Refresh the render-view with new image from render-buffer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Session::update_img_sample(void) {
    //Only for NON-INTERACTIVE session
	if(b_session) {
    	thread_scoped_lock img_lock(img_mutex);
		//TODO: optimize this by making it thread safe and removing lock
		b_session->update_render_img();
	}
	update_status_time();
} //update_img_sample()

OCT_NAMESPACE_END

