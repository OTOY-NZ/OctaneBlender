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

#include "blender_session.h"

#include "environment.h"
#include "camera.h"
#include "server.h"
#include "render/scene.h"
#include "session.h"

#include "util_progress.h"
#include "util_time.h"

#include "blender_sync.h"
#include "blender_util.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Pass::add(PassType type, vector<Pass>& passes) {
    Pass pass;

    pass.type = type;
    switch(type) {
	    case PASS_NONE:
		    pass.components = 0;
		    break;
	    case PASS_COMBINED:
		    pass.components = 4;
		    break;
	    case PASS_DEPTH:
		    pass.components = 1;
		    break;
	    case PASS_GEO_NORMALS:
		    pass.components = 4;
		    break;
	    case PASS_TEX_COORD:
		    pass.components = 4;
		    break;
	    case PASS_MATERIAL_ID:
		    pass.components = 1;
		    break;
	    default:
		    pass.components = 0;
		    break;
    }
    passes.push_back(pass);
} //Pass::add()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Non-Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)
								: b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(PointerRNA_NULL), b_rv3d(PointerRNA_NULL) {

    BL::RenderSettings r = b_scene.render();
    motion_blur          = r.use_motion_blur();
    shuttertime          = r.motion_blur_shutter();
    mb_samples           = r.motion_blur_samples();
    mb_cur_sample        = 0;
    mb_sample_in_work    = 0;

    for(int i=0; i < NUM_PASSES; ++i) {
        if(pass_buffers[i]) pass_buffers[i] = 0;
    }
    for(int i=0; i < NUM_PASSES; ++i) {
        if(mb_pass_buffers[i]) mb_pass_buffers[i] = 0;
    }
    // Offline render
	width   = b_engine.resolution_x();
	height  = b_engine.resolution_y();

	interactive         = false;
	last_redraw_time    = 0.0f;

	create_session(PASS_COMBINED);
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)
								: b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(b_v3d_), b_rv3d(b_rv3d_) {
    motion_blur = false;

    for(int i=0; i < NUM_PASSES; ++i) {
        if(pass_buffers[i]) pass_buffers[i] = 0;
    }
    for(int i=0; i < NUM_PASSES; ++i) {
        if(mb_pass_buffers[i]) mb_pass_buffers[i] = 0;
    }
	// 3d view render
	width   = width_;
	height  = height_;

	interactive         = true;
	last_redraw_time    = 0.0f;

	create_session(PASS_COMBINED);
    sync->sync_data(PASS_COMBINED, b_v3d, b_engine.camera_override());
	session->start("Interactive", false);
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::~BlenderSession() {
    session->set_pause(false);
	free_session();
} //~BlenderSession()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Create the Blender session and all Octane session data structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::create_session(PassType pass_type) {
	SessionParams session_params    = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    session_params.width            = width;
    session_params.height           = height;

	// Reset status/progress
	last_status		= "";
	last_progress	= -1.0f;

	// Create session
	string cur_path = blender_absolute_path(b_data, b_scene, b_scene.render().filepath().c_str());
    cur_path += "/alembic_export.abc";
	session = new Session(session_params, cur_path.c_str());
	session->set_blender_session(this);
	session->set_pause(BlenderSync::get_session_pause_state(b_scene, interactive));

	// Create scene
    scene = new Scene(session, interactive || !b_engine.is_animation() ? true : (b_scene.frame_current() == b_scene.frame_start()));
	session->scene = scene;

    scene->server = session->server;

	// Create sync
	sync = new BlenderSync(b_engine, b_data, b_scene, scene, interactive, session->progress);

	if(b_rv3d)
		sync->sync_view(b_v3d, b_rv3d, width, height);
	else
		sync->sync_camera(b_engine.camera_override(), width, height);

	// Set buffer parameters
	BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);

    if(interactive || !b_engine.is_animation() || b_scene.frame_current() == b_scene.frame_start())
	    session->reset(buffer_params, session_params.samples);
} //create_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reset_session(BL::BlendData b_data_, BL::Scene b_scene_) {
	b_data = b_data_;
	//b_render = b_engine.render();
	b_scene = b_scene_;

    session->set_pause(false);

    SessionParams session_params = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    session_params.width  = width;
    session_params.height = height;
	BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
	session->reset(buffer_params, session_params.samples);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reload the scene
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reload_session() {
	free_session();
    last_redraw_time = 0.0f;
    create_session(PASS_COMBINED);
    sync->sync_data(PASS_COMBINED, b_v3d, b_engine.camera_override());
    if(interactive) session->start("Combined pass", false);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Free Blender session and all Octane session data structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::free_session() {
    for(int i=0; i < NUM_PASSES; ++i) {
        if(pass_buffers[i]) {
            delete[] pass_buffers[i];
            pass_buffers[i] = 0;
        }
        if(mb_pass_buffers[i]) {
            delete[] mb_pass_buffers[i];
            mb_pass_buffers[i] = 0;
        }
    }
	delete sync;
	delete session;
} //free_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Blender render-pass type translated to Octane pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PassType get_pass_type(BL::RenderPass b_pass) {
	switch(b_pass.type()) {
		case BL::RenderPass::type_COMBINED:
			return PASS_COMBINED;

		case BL::RenderPass::type_Z:
			return PASS_DEPTH;
		case BL::RenderPass::type_NORMAL:
			return PASS_GEO_NORMALS;
		case BL::RenderPass::type_UV:
			return PASS_TEX_COORD;
		case BL::RenderPass::type_MATERIAL_INDEX:
			return PASS_MATERIAL_ID;

		case BL::RenderPass::type_VECTOR:
		case BL::RenderPass::type_EMIT:
		case BL::RenderPass::type_ENVIRONMENT:
		case BL::RenderPass::type_AO:
		case BL::RenderPass::type_SHADOW:
		case BL::RenderPass::type_DIFFUSE_COLOR:
		case BL::RenderPass::type_GLOSSY_COLOR:
		case BL::RenderPass::type_TRANSMISSION_COLOR:
		case BL::RenderPass::type_DIFFUSE_INDIRECT:
		case BL::RenderPass::type_GLOSSY_INDIRECT:
		case BL::RenderPass::type_TRANSMISSION_INDIRECT:
		case BL::RenderPass::type_DIFFUSE_DIRECT:
		case BL::RenderPass::type_GLOSSY_DIRECT:
		case BL::RenderPass::type_TRANSMISSION_DIRECT:
		case BL::RenderPass::type_OBJECT_INDEX:
		case BL::RenderPass::type_DIFFUSE:
		case BL::RenderPass::type_COLOR:
		case BL::RenderPass::type_REFRACTION:
		case BL::RenderPass::type_SPECULAR:
		case BL::RenderPass::type_REFLECTION:
		case BL::RenderPass::type_MIST:
			return PASS_NONE;
        default:
			return PASS_NONE;
	}
	return PASS_NONE;
} //get_pass_type()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static BL::RenderResult begin_render_result(BL::RenderEngine b_engine, int x, int y, int w, int h, const char *layername) {
	return b_engine.begin_result(x, y, w, h, layername);
} //begin_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void end_render_result(BL::RenderEngine b_engine, BL::RenderResult b_rr, bool cancel, bool do_merge_results) {
	b_engine.end_result(b_rr, (int)cancel, (int)do_merge_results);
} //end_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the rendered image, with or without passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::do_write_update_render_img(bool do_update_only) {
	int x = 0;
	int y = 0;
	int w = width;
	int h = height;

	// Get render result
	BL::RenderResult b_rr = begin_render_result(b_engine, x, y, w, h, b_rlay_name.c_str());

	// Can happen if the intersected rectangle gives 0 width or height
	if (!b_rr.ptr.data) return;

	BL::RenderResult::layers_iterator b_single_rlay;
	b_rr.layers.begin(b_single_rlay);
	BL::RenderLayer b_rlay = *b_single_rlay;

    if(do_update_only) {
		// Update only needed
		update_render_result(b_rr, b_rlay);
		end_render_result(b_engine, b_rr, true, true);
	}
	else {
		// Write result
		write_render_result(b_rr, b_rlay);
		end_render_result(b_engine, b_rr, false, true);
	}
} //do_write_update_render_img()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the rendered image with passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::write_render_img() {
	do_write_update_render_img(false);
} //write_render_img()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the rendered image without passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::update_render_img() {
	if (!b_engine.is_preview())
	    do_write_update_render_img(true);
    else {
        if(cur_pass_type != PASS_COMBINED) return;
	    do_write_update_render_img(false);
    }
} //update_render_img()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render image, with passes if needed
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::do_write_update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay, bool do_update_only) {
	if(!do_update_only || motion_blur) {
		// Copy each pass
		BL::RenderLayer::passes_iterator b_iter;

		for(b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter) {
			BL::RenderPass b_pass(*b_iter);

			// Find matching pass type
			int components = b_pass.channels();
            int buf_size = width * height * components;

            PassType pass_type = get_pass_type(b_pass);
            if(pass_type == PASS_NONE) {
                if(!do_update_only) {
	                float* pixels  = new float[buf_size];
                    memset(pixels, 0, sizeof(float) * buf_size);
			        b_pass.rect(pixels);
                    delete[] pixels;
                }
                continue;
            }

            register int i = -1;
            for(register int cur_pass_idx = pass_type; cur_pass_idx; cur_pass_idx >>= 1, ++i);

    	    float* pixels  = pass_buffers[i];
            if(!pixels) {
	            pixels = new float[buf_size];
                pass_buffers[i] = pixels;
            }
            float* mb_pixels = mb_pass_buffers[i];
            if(motion_blur && !mb_pixels) {
                mb_pixels = new float[buf_size];
                mb_pass_buffers[i] = mb_pixels;
            }

            // Copy pixels
            if(pass_type == cur_pass_type) {
                if(motion_blur && mb_cur_sample > 1) {
                    if(!do_update_only) {
                        for(unsigned int k = 0; k < buf_size; ++k)
                            pixels[k] = (pixels[k] * (mb_cur_sample - 1) + mb_pixels[k]) / (float)mb_cur_sample;
                    }
                    else {
                        if(mb_cur_sample > 2 && mb_cur_sample > mb_sample_in_work) {
                            mb_sample_in_work = mb_cur_sample;
                            for(unsigned int k = 0; k < buf_size; ++k)
                                pixels[k] = (pixels[k] * (mb_cur_sample - 2) + mb_pixels[k]) / (float)(mb_cur_sample - 1);
                        }
                        session->server->get_pass_rect(pass_type, components, mb_pixels, width, height);
                    }
                    b_pass.rect(pixels);
                }
                else {
                    if(session->server->get_pass_rect(pass_type, components, pixels, width, height))
			            b_pass.rect(pixels);
                }
            }
            else b_pass.rect(pixels);
		}
	}

    int buf_size = width * height * 4;
    float* pixels = pass_buffers[0];
    if(!pixels) {
        pixels = new float[buf_size];
        pass_buffers[0] = pixels;
    }
    float* mb_pixels = mb_pass_buffers[0];
    if(motion_blur && !mb_pixels) {
        mb_pixels = new float[buf_size];
        mb_pass_buffers[0] = mb_pixels;
    }

    if(cur_pass_type != PASS_COMBINED)
		b_rlay.rect(pixels);
    else if(motion_blur && mb_cur_sample > 1) {
        if(!do_update_only) {
            for(unsigned int k = 0; k < buf_size; ++k)
                pixels[k] = (pixels[k] * (mb_cur_sample - 1) + mb_pixels[k]) / (float)mb_cur_sample;
        }
        else {
            if(mb_cur_sample > 2 && mb_cur_sample > mb_sample_in_work) {
                mb_sample_in_work = mb_cur_sample;
                for(unsigned int k = 0; k < buf_size; ++k)
                    pixels[k] = (pixels[k] * (mb_cur_sample - 2) + mb_pixels[k]) / (float)(mb_cur_sample - 1);
            }
            session->server->get_pass_rect(PASS_COMBINED, 4, mb_pixels, width, height);
        }
  		b_rlay.rect(pixels);
    }
    else if(session->server->get_pass_rect(PASS_COMBINED, 4, pixels, width, height))
		b_rlay.rect(pixels);

	// Tag result as updated
	b_engine.update_result(b_rr);
} //do_write_update_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render image with passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::write_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay) {
	do_write_update_render_result(b_rr, b_rlay, false);
} //write_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render image, without passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay) {
	do_write_update_render_result(b_rr, b_rlay, true);
} //update_render_result()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Collect needed render-passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int BlenderSession::get_render_passes(vector<Pass> &passes) {
	// Temporary render result to find needed passes
	BL::RenderResult b_rr = begin_render_result(b_engine, 0, 0, 1, 1, b_rlay_name.c_str());
	BL::RenderResult::layers_iterator b_single_rlay;
	b_rr.layers.begin(b_single_rlay);

	// Layer will be missing if it was disabled in the UI
	if(b_single_rlay == b_rr.layers.end()) {
		end_render_result(b_engine, b_rr, true, false);
		return -1;
	}

	BL::RenderLayer b_rlay = *b_single_rlay;

	// Add passes
	// Loop over passes
	BL::RenderLayer::passes_iterator b_pass_iter;
	for(b_rlay.passes.begin(b_pass_iter); b_pass_iter != b_rlay.passes.end(); ++b_pass_iter) {
		BL::RenderPass b_pass(*b_pass_iter);
		PassType pass_type = get_pass_type(b_pass);

		if(pass_type != PASS_NONE) Pass::add(pass_type, passes);
	}
	// Free result without merging
	end_render_result(b_engine, b_rr, true, false);
    return passes.size();
} //get_render_passes()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "render" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::render() {
	// Get buffer parameters
	SessionParams	session_params	= BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    if(session_params.export_alembic) {
	    session->update_scene_to_server();
        session->server->start_render(width, height, 0);

        if(b_engine.test_break() || b_scene.frame_current() >= b_scene.frame_end()) {
    		session->progress.set_status("Transferring alembic file...");
            session->server->stop_render(session_params.fps);
        }
        return;
    }
	BufferParams	buffer_params	= BlenderSync::get_display_buffer_params(scene->camera, width, height);

	// Render each layer
	BL::RenderSettings render = b_scene.render();
	BL::RenderSettings::layers_iterator b_iter;

    if(motion_blur && mb_samples > 1)
        session->params.samples = session->params.samples / mb_samples;
    if(session->params.samples < 1) session->params.samples = 1;
	
    bool stop_render = false;
	for(render.layers.begin(b_iter); b_iter != render.layers.end(); ++b_iter) {
		b_rlay_name = b_iter->name();

		// Add passes
        vector<Pass> passes;
		if(session_params.use_passes) num_passes = get_render_passes(passes) + 1;
        else num_passes = 1;
        if(num_passes < 0) continue;
        ready_passes = 0;

        for(int i=0; i < NUM_PASSES; ++i) {
            if(pass_buffers[i]) {
                delete[] pass_buffers[i];
                pass_buffers[i] = 0;
            }
            if(mb_pass_buffers[i]) {
                delete[] mb_pass_buffers[i];
                mb_pass_buffers[i] = 0;
            }
        }
        cur_pass_type = PASS_COMBINED;

        // Render
        if(motion_blur && mb_samples > 1) {
            mb_sample_in_work = 0;
            float subframe = 0;
            int cur_frame = b_scene.frame_current();
            for(mb_cur_sample = 1; mb_cur_sample <= mb_samples; ++mb_cur_sample) {
                session->start("Combined pass", true);
                session->params.image_stat.cur_samples = 0;

                subframe += shuttertime / (mb_samples - 1);
                if(subframe < 1.0f)
        		    b_scene.frame_set(cur_frame, subframe);

                sync->sync_data(PASS_COMBINED, b_v3d, b_engine.camera_override());
        		sync->sync_camera(b_engine.camera_override(), width, height);

                if(session->progress.get_cancel()) {
                    stop_render = true;
                    break;
                }
            }
      		b_scene.frame_set(cur_frame, 0);
        }
        else {
            if(motion_blur) motion_blur = false;
            mb_cur_sample = 0;
            session->start("Combined pass", true);
            session->params.image_stat.cur_samples = 0;
        }
        ready_passes = 1;
        write_render_img();

        vector<Pass>::const_iterator it;
        for(it = passes.begin(); it != passes.end(); ++it) {
            cur_pass_type = it->type;

            char* cur_message;
            switch(cur_pass_type) {
                case PASS_DEPTH:
                    cur_message = "Depth pass";
                    break;
                case PASS_GEO_NORMALS:
                    cur_message = "Geo normals pass";
                    break;
                case PASS_TEX_COORD:
                    cur_message = "UV pass";
                    break;
                case PASS_MATERIAL_ID:
                    cur_message = "MatID pass";
                    break;
                case PASS_SHADING_NORMALS:
                    cur_message = "Shading normals pass";
                    break;
                case PASS_POSITION:
                    cur_message = "Position pass";
                    break;
                default:
                    continue;
                    break;
            }

	        // Render
            if(motion_blur && mb_samples > 1) {
                sync->sync_data(cur_pass_type, b_v3d, b_engine.camera_override());
        		sync->sync_camera(b_engine.camera_override(), width, height);

                mb_sample_in_work = 0;
                float subframe = 0;
                int cur_frame = b_scene.frame_current();
                for(mb_cur_sample = 1; mb_cur_sample <= mb_samples; ++mb_cur_sample) {
                    session->start(cur_message, true);
                    session->params.image_stat.cur_samples = 0;

                    subframe += shuttertime / (mb_samples - 1);
                    if(subframe < 1.0f)
        		        b_scene.frame_set(cur_frame, subframe);

                    sync->sync_data(cur_pass_type, b_v3d, b_engine.camera_override());
            		sync->sync_camera(b_engine.camera_override(), width, height);

                    if(session->progress.get_cancel()) {
                        stop_render = true;
                        break;
                    }
                }
      		    b_scene.frame_set(cur_frame, 0);
            }
            else {
                if(motion_blur) motion_blur = false;

                sync->sync_kernel(cur_pass_type);
		        session->update_scene_to_server();
	            BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
                session->update(buffer_params, session_params.samples);
                mb_cur_sample = 0;
                session->start(cur_message, true);
                session->params.image_stat.cur_samples = 0;
            }
            ++ready_passes;
            write_render_img();

            if(session->progress.get_cancel()) {
                stop_render = true;
                break;
            }
        }
        if(session->progress.get_cancel()) {
            stop_render = true;
            break;
        }
	} //for(r.layers.begin(b_iter); b_iter != r.layers.end(); ++b_iter)
    for(int i=0; i < NUM_PASSES; ++i) {
        if(pass_buffers[i]) {
            delete[] pass_buffers[i];
            pass_buffers[i] = 0;
        }
        if(mb_pass_buffers[i]) {
            delete[] mb_pass_buffers[i];
            mb_pass_buffers[i] = 0;
        }
    }
    num_passes   = -1;
    ready_passes = -1;

    if(stop_render || !b_engine.is_animation() || b_scene.frame_current() >= b_scene.frame_end())
        session->server->stop_render(session_params.fps);
} //render()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "sync" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::synchronize() {
    if(num_passes < 0) num_passes   = 0;
    if(ready_passes < 0) ready_passes = 0;
    SessionParams session_params;

    session_params = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    if(session->params.modified(session_params)) {
        reload_session();
		return;
	}

	// Increase samples, but never decrease
	session->set_samples(session_params.samples);
	session->set_pause(BlenderSync::get_session_pause_state(b_scene, interactive));

	// Copy recalc flags, outside of mutex so we can decide to do the real
	// synchronization at a later time to not block on running updates
	sync->sync_recalc();

	// Try to acquire mutex. if we don't want to or can't, come back later
	if(!session->ready_to_reset() || !session->scene->mutex.try_lock()) {
		tag_update();
		return;
	}

	// Data synchronize
	sync->sync_data(PASS_COMBINED, b_v3d, b_engine.camera_override());

	// Camera synchronize
	if(b_rv3d)
		sync->sync_view(b_v3d, b_rv3d, width, height);
	else
		sync->sync_camera(b_engine.camera_override(), width, height);

	// Unlock
	session->scene->mutex.unlock();

	// Reset if needed
	if(scene->need_reset()) {
		BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
        session->update(buffer_params, session_params.samples);
	}
} //synchronize()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "draw" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSession::draw(int w, int h) {
    BufferParams    buffer_params;
    bool            reset = false;

	// Before drawing, we verify camera and viewport size changes, because
	// we do not get update callbacks for those, we must detect them here
	if(session->ready_to_reset()) {
		// Try to acquire mutex. If we can't, come back later.
        if(!session->scene->mutex.try_lock())
            tag_redraw();
		else {
			sync->sync_view(b_v3d, b_rv3d, w, h);
			session->scene->mutex.unlock();
		}

		// If dimensions changed, reset
		if(width != w || height != h) {
			width   = w;
			height  = h;
			reset   = true;
		}

		// Reset if requested
        if(reset) {
			SessionParams session_params = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
			buffer_params = BlenderSync::get_display_buffer_params(scene->camera, w, h);

            session->update(buffer_params, session_params.samples);
		}
	}

	// Update status and progress for 3d view draw
	update_status_progress();

	// Draw
    if(!reset) buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
    if(!session->draw(buffer_params)) {
    	SessionParams session_params  = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
        session->update(buffer_params, session_params.samples);
        if(!session->draw(buffer_params)) tag_redraw();
    }
    return true;
} //draw()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane session progress status
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::get_status(string& status, string& substatus) {
	session->progress.get_status(status, substatus);
} //get_status()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get progress koefficient
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::get_progress(float& progress, double& total_time) {
	session->progress.get_time(total_time);
    if(!motion_blur) {
        if(session->params.samples * num_passes == 0)
            progress = 0;
        else
	        progress = ((ready_passes * (float)session->params.samples + (float)session->params.image_stat.cur_samples) / ((float)session->params.samples * num_passes));
    }
    else {
        if(session->params.samples * mb_samples * num_passes == 0)
            progress = 0;
        else
	        progress = ((ready_passes * (float)session->params.samples * mb_samples + (float)session->params.samples * (mb_sample_in_work - 1) + (float)session->params.image_stat.cur_samples) / ((float)session->params.samples * mb_samples * num_passes));
    }
} //get_progress()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update the status and progress on Blender UI
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::update_status_progress() {
	string  timestatus, status, substatus;
	float   progress;
	double  total_time;
	char    time_str[128];

	get_status(status, substatus);
	get_progress(progress, total_time);

	timestatus = b_scene.name();
	if(b_rlay_name != "") timestatus += ", " + b_rlay_name;
	timestatus += " | ";

	BLI_timestr(total_time, time_str, 60);
	timestatus += "Elapsed: " + string(time_str) + " | ";

	if(substatus.size() > 0)
		status += " | " + substatus;

	if(status != last_status) {
		b_engine.update_stats("", (timestatus + status).c_str());
        //TODO: Add the memory usage statistics here
		//b_engine.update_memory_stats(mem_used, mem_peak);
		last_status = status;
	}
	if(progress > last_progress) {
		b_engine.update_progress(progress);
		last_progress = progress;
	}
} //update_status_progress()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag this session needs update later
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::tag_update() {
	// Tell blender that we want to get another update callback
    b_engine.tag_update();
} //tag_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tell Blender engine that we want to redraw
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::tag_redraw() {
	if(!interactive) {
		// Update stats and progress, only for background here because in 3d view we do it in draw for thread safety reasons
		update_status_progress();

		// Offline render, redraw if timeout passed
		if(time_dt() - last_redraw_time > 1.0) {
            b_engine.tag_redraw();
			last_redraw_time = time_dt();
		}
	}
	else {
		// Tell blender that we want to redraw
        b_engine.tag_redraw();
	}
} //tag_redraw()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test if we must cancel (from non-interactive render)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::test_cancel() {
	// Test if we need to cancel rendering
	if(!interactive)
		if(b_engine.test_break()) session->progress.set_cancel("Cancelled");
} //test_cancel()

OCT_NAMESPACE_END

