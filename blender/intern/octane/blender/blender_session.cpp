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

#include "DNA_scene_types.h"
#include "BKE_scene.h"
#include "BKE_global.h"
#include "BKE_main.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Non-Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)
                                : b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(PointerRNA_NULL), b_rv3d(PointerRNA_NULL) {
    for(int i=0; i < Passes::NUM_PASSES; ++i) {
        if(pass_buffers[i]) pass_buffers[i] = 0;
    }
    for(int i=0; i < Passes::NUM_PASSES; ++i) {
        if(mb_pass_buffers[i]) mb_pass_buffers[i] = 0;
    }
    // Offline render
	width   = b_engine.resolution_x();
	height  = b_engine.resolution_y();

	interactive         = false;
	last_redraw_time    = 0.0f;

	create_session();
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)
                                : b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(b_v3d_), b_rv3d(b_rv3d_) {
    for(int i = 0; i < Passes::NUM_PASSES; ++i) {
        if(pass_buffers[i]) pass_buffers[i] = 0;
    }
    for(int i = 0; i < Passes::NUM_PASSES; ++i) {
        if(mb_pass_buffers[i]) mb_pass_buffers[i] = 0;
    }
	// 3d view render
	width   = width_;
	height  = height_;

	interactive         = true;
	last_redraw_time    = 0.0f;

    create_session();

    if(motion_blur && mb_type == INTERNAL) {
        bool stop_render;
        session->start("Interactive", false, load_internal_mb_sequence(stop_render), 0);
    }
    else {
		motion_blur = false;
        sync->sync_data(b_v3d, b_engine.camera_override());
        session->start("Interactive", false, 0, 0);
    }
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::~BlenderSession() {
    session->set_pause(false);
	free_session();
} //~BlenderSession()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Send the license info to OctaneServer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSession::activate(BL::Scene b_scene) {
    bool ret = false;

    PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

    // Render-server address
    RenderServerInfo &server_info = RenderServer::get_info();
    string server_addr = get_string(oct_scene, "server_address");
    if(server_addr.length() > 0)
        ::strcpy(server_info.net_address, server_addr.c_str());

    string login        = get_string(oct_scene, "server_login");
    string pass         = get_string(oct_scene, "server_pass");
    string stand_login  = get_string(oct_scene, "stand_login");
    string stand_pass   = get_string(oct_scene, "stand_pass");
    if(stand_login.length() > 0 && stand_pass.length() > 0 && login.length() > 0 && pass.length() > 0) {
        RenderServer *server = new RenderServer(server_info.net_address, "", false, true);

        if(server) {
            if(server->activate(stand_login, stand_pass, login, pass)) {
                RNA_string_set(&oct_scene, "stand_login", "");
                RNA_string_set(&oct_scene, "stand_pass", "");
                RNA_string_set(&oct_scene, "server_login", "");
                RNA_string_set(&oct_scene, "server_pass", "");
                fprintf(stdout, "Octane: server activation is completed successfully.\n");
                ret = true;
            }
            delete server;
        }
        else {
            fprintf(stderr, "Octane: ERROR during server activation.\n");
            ret = false;
        }
    }
    else {
        fprintf(stderr, "Octane: ERROR: login-password fields must be filled in before activation.\n");
        ret = false;
    }

    return ret;
} //activate()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Create the Blender session and all Octane session data structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::create_session() {
	SessionParams session_params    = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    session_params.width            = width;
    session_params.height           = height;

    BL::RenderSettings r    = b_scene.render();
    motion_blur             = r.use_motion_blur();
    shuttertime             = r.motion_blur_shutter();
    mb_samples              = r.motion_blur_samples();
    mb_cur_sample           = 0;
    mb_sample_in_work       = 0;

    PointerRNA oct_scene    = RNA_pointer_get(&b_scene.ptr, "octane");
    mb_type                 = static_cast<MotionBlurType>(RNA_enum_get(&oct_scene, "mb_type"));
    mb_direction            = static_cast<MotionBlurDirection>(RNA_enum_get(&oct_scene, "mb_direction"));
    mb_frame_time_sampling  = motion_blur && mb_type == INTERNAL ? 1.0f / session_params.fps : -1.0f;

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
        session->reset(buffer_params, mb_frame_time_sampling);
} //create_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reset_session(BL::BlendData b_data_, BL::Scene b_scene_) {
	b_data = b_data_;
	//b_render = b_engine.render();
	b_scene = b_scene_;

    session->set_pause(false);

	BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
    session->reset(buffer_params, mb_frame_time_sampling);
} //reset_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reload the scene
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reload_session() {
	free_session();
    last_redraw_time = 0.0f;
    create_session();

    if(motion_blur && mb_type == INTERNAL) {
        bool stop_render;
        session->start("Interactive", false, load_internal_mb_sequence(stop_render), 0);
    }
    else {
        sync->sync_data(b_v3d, b_engine.camera_override());
        if(interactive) session->start("Interactive", false, 0, 0);
    }
} //reload_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Free Blender session and all Octane session data structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::free_session() {
    clear_passes_buffers();
    delete sync;
	delete session;
} //free_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Returns: the current frame index inside the sequence
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int BlenderSession::load_internal_mb_sequence(bool &stop_render, BL::RenderLayer *layer) {
    stop_render = false;

    int     cur_frame = b_scene.frame_current();
    float   frames_cnt = shuttertime / mb_frame_time_sampling;
    int     first_frame, last_frame;

    if(mb_direction == AFTER) {
        first_frame = cur_frame;
        last_frame = static_cast<int>(ceilf(static_cast<float>(cur_frame)+frames_cnt));
    }
    else if(mb_direction == BEFORE) {
        first_frame = static_cast<int>(floorf(static_cast<float>(cur_frame)-frames_cnt));
        last_frame = cur_frame;
    }
    else if(mb_direction == SYMMETRIC) {
        first_frame = static_cast<int>(floorf(static_cast<float>(cur_frame)-frames_cnt / 2));
        last_frame = static_cast<int>(ceilf(static_cast<float>(cur_frame)+frames_cnt / 2));
    }
    CLAMP(first_frame, b_scene.frame_start(), b_scene.frame_end());
    CLAMP(last_frame, b_scene.frame_start(), b_scene.frame_end());

    double last_cfra;
    for(int cur_mb_frame = first_frame; cur_mb_frame <= last_frame; ++cur_mb_frame) {
        //b_scene.frame_set(cur_mb_frame, 0); //Crashes due to BPy_BEGIN_ALLOW_THREADS-BPy_END_ALLOW_THREADS block in rna_Scene_frame_set()
        last_cfra = (double)cur_mb_frame;
        CLAMP(last_cfra, MINAFRAME, MAXFRAME);
        BKE_scene_frame_set((::Scene *)b_scene.ptr.data, last_cfra);
        BKE_scene_update_for_newframe_ex(G.main->eval_ctx, G.main, (::Scene *)b_scene.ptr.data, (1 << 20) - 1, true);
        BKE_scene_camera_switch_update((::Scene *)b_scene.ptr.data);

        sync->sync_data(b_v3d, b_engine.camera_override(), layer);
        sync->sync_camera(b_engine.camera_override(), width, height);
        session->update_scene_to_server(cur_mb_frame - first_frame, last_frame - first_frame + 1);

        if(!interactive && session->progress.get_cancel()) {
            stop_render = true;
            break;
        }
    }
    //b_scene.frame_set(cur_frame, 0); //Crashes due to BPy_BEGIN_ALLOW_THREADS-BPy_END_ALLOW_THREADS block in rna_Scene_frame_set()
    double cfra = (double)cur_frame;
    CLAMP(cfra, MINAFRAME, MAXFRAME);
    if(last_cfra != cfra) {
        BKE_scene_frame_set((::Scene *)b_scene.ptr.data, cfra);
        BKE_scene_update_for_newframe_ex(G.main->eval_ctx, G.main, (::Scene *)b_scene.ptr.data, (1 << 20) - 1, true);
        BKE_scene_camera_switch_update((::Scene *)b_scene.ptr.data);
    }

    return cur_frame - first_frame;
} //load_internal_mb_sequence()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Blender render-pass type translated to Octane pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline Passes::PassTypes BlenderSession::get_octane_pass_type(BL::RenderPass b_pass) {
	switch(b_pass.type()) {
		case BL::RenderPass::type_COMBINED:
            return Passes::COMBINED;

        case BL::RenderPass::type_EMIT:
            return Passes::EMIT;
        case BL::RenderPass::type_ENVIRONMENT:
            return Passes::ENVIRONMENT;
        case BL::RenderPass::type_DIFFUSE_DIRECT:
            return Passes::DIFFUSE_DIRECT;
        case BL::RenderPass::type_DIFFUSE_INDIRECT:
            return Passes::DIFFUSE_INDIRECT;

        case BL::RenderPass::type_REFLECTION:
            if(scene->passes->reflection_direct_pass)
                return Passes::REFLECTION_DIRECT;
            else if(scene->passes->reflection_indirect_pass)
                return Passes::REFLECTION_INDIRECT;
            else
                return Passes::LAYER_REFLECTIONS;

        case BL::RenderPass::type_REFRACTION:
            return Passes::REFRACTION;
        case BL::RenderPass::type_TRANSMISSION_COLOR:
            return Passes::TRANSMISSION;
        case BL::RenderPass::type_SUBSURFACE_COLOR:
            return Passes::SSS;

        case BL::RenderPass::type_NORMAL:
            if(scene->passes->geom_normals_pass)
                return Passes::GEOMETRIC_NORMAL;
            else if(scene->passes->shading_normals_pass)
                return Passes::SHADING_NORMAL;
            else
                return Passes::VERTEX_NORMAL;

        case BL::RenderPass::type_Z:
            return Passes::Z_DEPTH;
        case BL::RenderPass::type_MATERIAL_INDEX:
            return Passes::MATERIAL_ID;
        case BL::RenderPass::type_UV:
            return Passes::UV_COORD;
        case BL::RenderPass::type_OBJECT_INDEX:
            return Passes::OBJECT_ID;
        case BL::RenderPass::type_AO:
            return Passes::AMBIENT_OCCLUSION;

        case BL::RenderPass::type_SHADOW:
            if(scene->passes->layer_shadows_pass)
                return Passes::LAYER_SHADOWS;
            else if(scene->passes->layer_black_shadows_pass)
                return Passes::LAYER_BLACK_SHADOWS;
            else
                return Passes::LAYER_COLOR_SHADOWS;

        case BL::RenderPass::type_VECTOR:
		case BL::RenderPass::type_DIFFUSE_COLOR:
		case BL::RenderPass::type_GLOSSY_COLOR:
		case BL::RenderPass::type_GLOSSY_INDIRECT:
		case BL::RenderPass::type_TRANSMISSION_INDIRECT:
		case BL::RenderPass::type_GLOSSY_DIRECT:
		case BL::RenderPass::type_TRANSMISSION_DIRECT:
		case BL::RenderPass::type_DIFFUSE:
		case BL::RenderPass::type_COLOR:
		case BL::RenderPass::type_SPECULAR:
		case BL::RenderPass::type_MIST:
            return Passes::PASS_NONE;
        default:
            return Passes::PASS_NONE;
	}
    return Passes::PASS_NONE;
} //get_octane_pass_type()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane render-pass type translated to Blender pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline BL::RenderPass::type_enum BlenderSession::get_blender_pass_type(Passes::PassTypes pass) {
    switch(pass) {
    case Passes::COMBINED:
        return BL::RenderPass::type_COMBINED;

    case Passes::EMIT:
        return BL::RenderPass::type_EMIT;
    case Passes::ENVIRONMENT:
        return BL::RenderPass::type_ENVIRONMENT;
    case Passes::DIFFUSE_DIRECT:
        return BL::RenderPass::type_DIFFUSE_DIRECT;
    case Passes::DIFFUSE_INDIRECT:
        return BL::RenderPass::type_DIFFUSE_INDIRECT;

    case Passes::REFLECTION_DIRECT:
    case Passes::REFLECTION_INDIRECT:
    case Passes::LAYER_REFLECTIONS:
        return BL::RenderPass::type_REFLECTION;

    case Passes::REFRACTION:
        return BL::RenderPass::type_REFRACTION;
    case Passes::TRANSMISSION:
        return BL::RenderPass::type_TRANSMISSION_COLOR;
    case Passes::SSS:
        return BL::RenderPass::type_SUBSURFACE_COLOR;

    case Passes::GEOMETRIC_NORMAL:
    case Passes::SHADING_NORMAL:
    case Passes::VERTEX_NORMAL:
        return BL::RenderPass::type_NORMAL;

    case Passes::Z_DEPTH:
        return BL::RenderPass::type_Z;
    case Passes::MATERIAL_ID:
        return BL::RenderPass::type_MATERIAL_INDEX;
    case Passes::UV_COORD:
        return BL::RenderPass::type_UV;
    case Passes::OBJECT_ID:
        return BL::RenderPass::type_OBJECT_INDEX;
    case Passes::AMBIENT_OCCLUSION:
        return BL::RenderPass::type_AO;

    case Passes::LAYER_SHADOWS:
    case Passes::LAYER_BLACK_SHADOWS:
    case Passes::LAYER_COLOR_SHADOWS:
        return BL::RenderPass::type_SHADOW;

    default:
        return BL::RenderPass::type_COMBINED;
    }
    return BL::RenderPass::type_COMBINED;
} //get_blender_pass_type()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Blender render-pass type translated to Octane pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int BlenderSession::get_pass_index(Passes::PassTypes pass) {
    switch(pass) {
    case Passes::COMBINED:
        return 0;

    case Passes::EMIT:
        return 1;
    case Passes::DIFFUSE_DIRECT:
        return 2;
    case Passes::DIFFUSE_INDIRECT:
        return 3;
    case Passes::REFLECTION_DIRECT:
        return 4;
    case Passes::REFLECTION_INDIRECT:
        return 5;
    case Passes::REFRACTION:
        return 6;
    case Passes::TRANSMISSION:
        return 7;
    case Passes::SSS:
        return 8;
    case Passes::POST_PROC:
        return 9;
    case Passes::LAYER_SHADOWS:
        return 10;
    case Passes::LAYER_BLACK_SHADOWS:
        return 11;
    case Passes::LAYER_COLOR_SHADOWS:
        return 12;
    case Passes::LAYER_REFLECTIONS:
        return 13;

    case Passes::GEOMETRIC_NORMAL:
        return 14;
    case Passes::SHADING_NORMAL:
        return 15;
    case Passes::POSITION:
        return 16;
    case Passes::Z_DEPTH:
        return 17;
    case Passes::MATERIAL_ID:
        return 18;
    case Passes::UV_COORD:
        return 19;
    case Passes::TANGENT_U:
        return 20;
    case Passes::WIREFRAME:
        return 21;
    case Passes::VERTEX_NORMAL:
        return 22;
    case Passes::OBJECT_ID:
        return 23;
    case Passes::AMBIENT_OCCLUSION:
        return 24;
    case Passes::MOTION_VECTOR:
        return 25;
    case Passes::LAYER_ID:
        return 26;
    case Passes::LAYER_MASK:
        return 27;
    case Passes::ENVIRONMENT:
        return 28;

    default:
        return 0;
    }
    return 0;
} //get_pass_index()

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
	    do_write_update_render_img(false);
    }
} //update_render_img()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Update render image, with passes if needed
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::do_write_update_render_result(BL::RenderResult b_rr, BL::RenderLayer b_rlay, bool do_update_only) {
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

    Passes::PassTypes cur_pass_type;
    if(scene->passes->use_passes)
        cur_pass_type = scene->passes->cur_pass_type;
    else
        cur_pass_type = Passes::COMBINED;

    if(scene->passes->use_passes && session->server->cur_pass_type != cur_pass_type)
        session->server->get_image_buffer(session->params.image_stat, interactive, cur_pass_type, session->progress);

    if(motion_blur && mb_type == SUBFRAME && mb_cur_sample > 1) {
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
            session->server->get_pass_rect(cur_pass_type, 4, mb_pixels, width, height,
                (scene->camera->use_border ? scene->camera->border.z - scene->camera->border.x : width), (scene->camera->use_border ? scene->camera->border.w - scene->camera->border.y : height));
        }
        b_rlay.rect(pixels);
    }
    else if(session->server->get_pass_rect(cur_pass_type, 4, pixels, width, height,
        (scene->camera->use_border ? scene->camera->border.z - scene->camera->border.x : width), (scene->camera->use_border ? scene->camera->border.w - scene->camera->border.y : height)))
        b_rlay.rect(pixels);

    if(scene->passes->use_passes && (!do_update_only || (motion_blur && mb_type == SUBFRAME && session->params.image_stat.cur_samples >= session->params.samples))) {
		// Copy each pass
		BL::RenderLayer::passes_iterator b_iter;
		for(b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter) {
			BL::RenderPass b_pass(*b_iter);

			int components = b_pass.channels();
            buf_size = width * height * components;

            // Find matching pass type
            Passes::PassTypes pass_type = get_octane_pass_type(b_pass);
            if(pass_type == Passes::COMBINED)
                continue;
            else if(pass_type == Passes::PASS_NONE || !session->server->get_image_buffer(session->params.image_stat, interactive, pass_type, session->progress)) {
                if(!do_update_only) {
	                float* pixels  = new float[buf_size];
                    memset(pixels, 0, sizeof(float) * buf_size);
			        b_pass.rect(pixels);
                    delete[] pixels;
                }
                continue;
            }
            int pass_idx = get_pass_index(pass_type);

            pixels = pass_buffers[pass_idx];
            if(!pixels) {
	            pixels = new float[buf_size];
                pass_buffers[pass_idx] = pixels;
            }
            mb_pixels = mb_pass_buffers[pass_idx];
            if(motion_blur && !mb_pixels) {
                mb_pixels = new float[buf_size];
                mb_pass_buffers[pass_idx] = mb_pixels;
            }

            if(motion_blur && mb_type == SUBFRAME && mb_cur_sample > 1) {
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
                    session->server->get_pass_rect(pass_type, components, mb_pixels, width, height,
                        (scene->camera->use_border ? scene->camera->border.z - scene->camera->border.x : width), (scene->camera->use_border ? scene->camera->border.w - scene->camera->border.y : height));
                }
                b_pass.rect(pixels);
            }
            else {
                if(session->server->get_pass_rect(pass_type, components, pixels, width, height,
                    (scene->camera->use_border ? scene->camera->border.z - scene->camera->border.x : width), (scene->camera->use_border ? scene->camera->border.w - scene->camera->border.y : height)))
			        b_pass.rect(pixels);
            }
		} //for(b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter)
	} //if(scene->passes->use_passes && (!do_update_only || motion_blur && mb_type == SUBFRAME))

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
// Clear all passes buffers
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::clear_passes_buffers() {
    for(int i = 0; i < Passes::NUM_PASSES; ++i) {
        if(pass_buffers[i]) {
            delete[] pass_buffers[i];
            pass_buffers[i] = 0;
        }
        if(mb_pass_buffers[i]) {
            delete[] mb_pass_buffers[i];
            mb_pass_buffers[i] = 0;
        }
    }
} //clear_passes_buffers()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "render" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::render() {
	// Get buffer parameters
	SessionParams	session_params	= BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    if(session_params.export_alembic) {
        session->update_scene_to_server(0, 0);
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

    if(motion_blur && mb_type == SUBFRAME && mb_samples > 1)
        session->params.samples = session->params.samples / mb_samples;
    if(session->params.samples < 1) session->params.samples = 1;

    bool stop_render = false;
    BL::RenderSettings::layers_iterator b_iter;
    for(render.layers.begin(b_iter); b_iter != render.layers.end(); ++b_iter) {
        clear_passes_buffers();
        BL::RenderLayer cur_layer(*b_iter);

        // Render
        if(motion_blur && mb_type == SUBFRAME && mb_samples > 1) {
            mb_sample_in_work = 0;
            float subframe = 0;
            int cur_frame = b_scene.frame_current();
            for(mb_cur_sample = 1; mb_cur_sample <= mb_samples; ++mb_cur_sample) {
                session->start("Final render", true, 0, 0);
                session->params.image_stat.cur_samples = 0;

                if(mb_cur_sample < mb_samples) {
                    subframe += shuttertime / (mb_samples - 1);
                    if(subframe < 1.0f) {
                        //b_scene.frame_set(cur_frame, subframe); //Crashes due to BPy_BEGIN_ALLOW_THREADS-BPy_END_ALLOW_THREADS block in rna_Scene_frame_set()
                        double cfra = (double)cur_frame + (double)subframe;
                        CLAMP(cfra, MINAFRAME, MAXFRAME);
                        BKE_scene_frame_set((::Scene *)b_scene.ptr.data, cfra);
                        BKE_scene_update_for_newframe_ex(G.main->eval_ctx, G.main, (::Scene *)b_scene.ptr.data, (1 << 20) - 1, true);
                        BKE_scene_camera_switch_update((::Scene *)b_scene.ptr.data);
                    }

                    sync->sync_data(b_v3d, b_engine.camera_override(), &cur_layer);
                    sync->sync_camera(b_engine.camera_override(), width, height);
                }

                if(session->progress.get_cancel()) {
                    stop_render = true;
                    break;
                }
            }
            //b_scene.frame_set(cur_frame, 0); //Crashes due to BPy_BEGIN_ALLOW_THREADS-BPy_END_ALLOW_THREADS block in rna_Scene_frame_set()
            double cfra = (double)cur_frame;
            CLAMP(cfra, MINAFRAME, MAXFRAME);
            BKE_scene_frame_set((::Scene *)b_scene.ptr.data, cfra);
            BKE_scene_update_for_newframe_ex(G.main->eval_ctx, G.main, (::Scene *)b_scene.ptr.data, (1 << 20) - 1, true);
            BKE_scene_camera_switch_update((::Scene *)b_scene.ptr.data);
        }
        else if(motion_blur && mb_type == INTERNAL) {
            int int_frame_idx = load_internal_mb_sequence(stop_render, &cur_layer);

            if(!stop_render) {
                session->start("Final render", true, int_frame_idx, 0);
                session->params.image_stat.cur_samples = 0;
            }
        }
        else {
            if(motion_blur) motion_blur = false;
            mb_cur_sample = 0;
            if(!stop_render) {
                session->start("Final render", true, 0, 0);
                session->params.image_stat.cur_samples = 0;
            }
        }

        write_render_img();

        if(session->progress.get_cancel()) {
            stop_render = true;
            break;
        }
	} //for(r.layers.begin(b_iter); b_iter != r.layers.end(); ++b_iter)

    clear_passes_buffers();

    if(stop_render || !b_engine.is_animation() || b_scene.frame_current() >= b_scene.frame_end())
        session->server->stop_render(session_params.fps);
} //render()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "sync" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::synchronize() {
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
	sync->sync_data(b_v3d, b_engine.camera_override());

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
        session->update(buffer_params);
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
			buffer_params = BlenderSync::get_display_buffer_params(scene->camera, w, h);

            session->update(buffer_params);
		}
	}

	// Update status and progress for 3d view draw
	update_status_progress();

	// Draw
    if(!reset) buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
    if(!session->draw(buffer_params)) {
        session->update(buffer_params);
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
        if(session->params.samples == 0)
            progress = 0;
        else
	        progress = (((float)session->params.samples + (float)session->params.image_stat.cur_samples) / (float)session->params.samples);
    }
    else {
        if(session->params.samples * mb_samples == 0)
            progress = 0;
        else
	        progress = (((float)session->params.samples * mb_samples + (float)session->params.samples * (mb_sample_in_work - 1) + (float)session->params.image_stat.cur_samples) / ((float)session->params.samples * mb_samples));
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

