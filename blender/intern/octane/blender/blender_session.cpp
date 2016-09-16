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
#include "OctaneClient.h"
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
#include "BLI_utildefines.h"

#include <thread>
#include <chrono>

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Non-Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)
                                : b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(PointerRNA_NULL), b_rv3d(PointerRNA_NULL) {
    sync_mutex.lock();

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

    sync_mutex.unlock();
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Interactive render session constructor
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)
                                : b_engine(b_engine_), b_userpref(b_userpref_), b_data(b_data_), b_scene(b_scene_), b_v3d(b_v3d_), b_rv3d(b_rv3d_) {
    sync_mutex.lock();

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
        int total_frames;
        int cur_frame = load_internal_mb_sequence(stop_render, total_frames);
        session->start("Interactive", false, cur_frame, 0);
    }
    else {
        motion_blur = false;
        session->start("Interactive", false, 0, 1);
    }

    sync_mutex.unlock();
} //BlenderSession(BL::RenderEngine b_engine_, BL::UserPreferences b_userpref_, BL::BlendData b_data_, BL::Scene b_scene_, BL::SpaceView3D b_v3d_, BL::RegionView3D b_rv3d_, int width_, int height_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSession::~BlenderSession() {
    sync_mutex.lock();

    session->set_pause(false);
    free_session();

    sync_mutex.unlock();
} //~BlenderSession()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Send the license info to OctaneServer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSession::activate(BL::Scene b_scene) {
    bool ret = true;

    PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

    // Render-server address
    string server_addr = get_string(oct_scene, "server_address");
    if(!server_addr.length()) {
        fprintf(stderr, "Octane: no server address set.\n");
        return false;
    }

    //string login        = get_string(oct_scene, "server_login");
    //string pass         = get_string(oct_scene, "server_pass");
    //string stand_login  = get_string(oct_scene, "stand_login");
    //string stand_pass   = get_string(oct_scene, "stand_pass");
    //if(stand_login.length() > 0 && stand_pass.length() > 0 && login.length() > 0 && pass.length() > 0) {
        ::OctaneEngine::OctaneClient *server = newnt ::OctaneEngine::OctaneClient;
        if(server) {
            if(!server->connectToServer(server_addr.c_str())) {
                if(server->getFailReason() == ::OctaneEngine::OctaneClient::FailReasons::NOT_ACTIVATED)
                    fprintf(stdout, "Octane: current server activation state is: not activated.\n");
                else {
                    if(server->getFailReason() == ::OctaneEngine::OctaneClient::FailReasons::NO_CONNECTION) {
                        fprintf(stderr, "Octane: can't connect to Octane server.\n");
                        ret = false;
                    }
                    else if(server->getFailReason() == ::OctaneEngine::OctaneClient::FailReasons::WRONG_VERSION) {
                        fprintf(stderr, "Octane: wrong version of Octane server.\n");
                        ret = false;
                    }
                    else {
                        fprintf(stderr, "Octane: can't connect to Octane server.\n");
                        ret = false;
                    }
                }
            }

            if(ret && !server->activate("", "", "", "")) {
                //RNA_string_set(&oct_scene, "stand_login", "");
                //RNA_string_set(&oct_scene, "stand_pass", "");
                //RNA_string_set(&oct_scene, "server_login", "");
                //RNA_string_set(&oct_scene, "server_pass", "");
                ret = false;
            }
            //else fprintf(stdout, "Octane: server activation is completed successfully.\n");

            delete server;
        }
        else {
            fprintf(stderr, "Octane: unexpected ERROR during opening server activation state dialog.\n");
            ret = false;
        }
    //}
    //else {
    //    fprintf(stderr, "Octane: ERROR: login-password fields must be filled in before activation.\n");
    //    ret = false;
    //}

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
    cur_path += "/octane_export";
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
// Free Blender session and all Octane session data structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::free_session() {
    if(session->server && (interactive || !b_engine.is_animation() || b_scene.frame_current() == b_scene.frame_end()))
        session->server->clear();

    clear_passes_buffers();
    delete sync;
    delete session;
} //free_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reset_session(BL::BlendData b_data_, BL::Scene b_scene_) {
    sync_mutex.lock();

    b_data = b_data_;
    //b_render = b_engine.render();
    b_scene = b_scene_;

    session->set_pause(false);

    BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
    session->reset(buffer_params, mb_frame_time_sampling);

    sync_mutex.unlock();
} //reset_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reload the scene
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::reload_session() {
    sync_mutex.lock();

    free_session();
    last_redraw_time = 0.0f;
    create_session();

    if(motion_blur && mb_type == INTERNAL) {
        bool stop_render;
        int total_frames;
        int cur_frame = load_internal_mb_sequence(stop_render, total_frames);
        session->start("Interactive", false, cur_frame, 0);
    }
    else {
        if(interactive) {
            sync->sync_data(b_v3d, b_engine.camera_override());
            session->start("Interactive", false, 0, 1);
        }
    }

    sync_mutex.unlock();
} //reload_session()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Returns: the current frame index inside the sequence
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int BlenderSession::load_internal_mb_sequence(bool &stop_render, int &num_frames, BL::RenderLayer *layer, bool do_sync) {
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
    //int start_frame = std::min(b_scene.frame_start(), cur_frame);
    //int end_frame = std::max(b_scene.frame_end(), cur_frame);
    //CLAMP(first_frame, start_frame, end_frame);
    //CLAMP(last_frame, start_frame, end_frame);

    num_frames = last_frame - first_frame + 1;
    double last_cfra;
    int motion = 0;
    for(int cur_mb_frame = first_frame; cur_mb_frame <= last_frame; ++cur_mb_frame) {
        //if(cur_mb_frame == cur_frame) continue;

        //b_scene.frame_set(cur_mb_frame, 0); //Crashes due to BPy_BEGIN_ALLOW_THREADS-BPy_END_ALLOW_THREADS block in rna_Scene_frame_set()
        last_cfra = (double)cur_mb_frame;
        CLAMP(last_cfra, MINAFRAME, MAXFRAME);
        BKE_scene_frame_set((::Scene *)b_scene.ptr.data, last_cfra);
        BKE_scene_update_for_newframe_ex(G.main->eval_ctx, G.main, (::Scene *)b_scene.ptr.data, (1 << 20) - 1, true);
        BKE_scene_camera_switch_update((::Scene *)b_scene.ptr.data);

        sync->sync_data(b_v3d, b_engine.camera_override(), layer, motion);
        if(!do_sync) {
            if(b_rv3d)
                sync->sync_view(b_v3d, b_rv3d, width, height);
            else
                sync->sync_camera(b_engine.camera_override(), width, height);
        }
        session->update_scene_to_server(cur_mb_frame - first_frame, cur_mb_frame == last_frame ? 0 : num_frames, do_sync);

        if(!interactive && session->progress.get_cancel()) {
            stop_render = true;
            break;
        }
        if(!motion) motion = 1;
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
inline ::Octane::RenderPassId BlenderSession::get_octane_pass_type(BL::RenderPass b_pass) {
    switch(b_pass.type()) {
        case BL::RenderPass::type_COMBINED:
            return ::Octane::RenderPassId::RENDER_PASS_BEAUTY;

        case BL::RenderPass::type_EMIT:
            return ::Octane::RenderPassId::RENDER_PASS_EMIT;
        case BL::RenderPass::type_ENVIRONMENT:
            return ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT;
        case BL::RenderPass::type_DIFFUSE_DIRECT:
            return ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT;
        case BL::RenderPass::type_DIFFUSE_INDIRECT:
            return ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT;

        case BL::RenderPass::type_REFLECTION:
            if(scene->passes->oct_node->bReflectionDirectPass)
                return ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT;
            else if(scene->passes->oct_node->bReflectionIndirectPass)
                return ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT;
            else
                return ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS;

        case BL::RenderPass::type_REFRACTION:
            return ::Octane::RenderPassId::RENDER_PASS_REFRACTION;
        case BL::RenderPass::type_TRANSMISSION_COLOR:
            return ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION;
        case BL::RenderPass::type_SUBSURFACE_COLOR:
            return ::Octane::RenderPassId::RENDER_PASS_SSS;

        case BL::RenderPass::type_NORMAL:
            if(scene->passes->oct_node->bGeomNormalsPass)
                return ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL;
            else if(scene->passes->oct_node->bShadingNormalsPass)
                return ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL;
            else
                return ::Octane::RenderPassId::RENDER_PASS_VERTEX_NORMAL;

        case BL::RenderPass::type_Z:
            return ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH;
        case BL::RenderPass::type_MATERIAL_INDEX:
            return ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID;
        case BL::RenderPass::type_UV:
            return ::Octane::RenderPassId::RENDER_PASS_UV_COORD;
        case BL::RenderPass::type_OBJECT_INDEX:
            return ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID;
        case BL::RenderPass::type_AO:
            return ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION;

        case BL::RenderPass::type_SHADOW:
            if(scene->passes->oct_node->bLayerShadowsPass)
                return ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS;
            else if(scene->passes->oct_node->bLayerBlackShadowsPass)
                return ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS;
            else
                return ::Octane::RenderPassId::RENDER_PASS_LAYER_COLOR_SHADOWS;

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
            return ::Octane::RenderPassId::PASS_NONE;
        default:
            return ::Octane::RenderPassId::PASS_NONE;
    }
    return ::Octane::RenderPassId::PASS_NONE;
} //get_octane_pass_type()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane render-pass type translated to Blender pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline BL::RenderPass::type_enum BlenderSession::get_blender_pass_type(::Octane::RenderPassId pass) {
    switch(pass) {
    case ::Octane::RenderPassId::RENDER_PASS_BEAUTY:
        return BL::RenderPass::type_COMBINED;

    case ::Octane::RenderPassId::RENDER_PASS_EMIT:
        return BL::RenderPass::type_EMIT;
    case ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT:
        return BL::RenderPass::type_ENVIRONMENT;
    case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT:
        return BL::RenderPass::type_DIFFUSE_DIRECT;
    case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT:
        return BL::RenderPass::type_DIFFUSE_INDIRECT;

    case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT:
    case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT:
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS:
        return BL::RenderPass::type_REFLECTION;

    case ::Octane::RenderPassId::RENDER_PASS_REFRACTION:
        return BL::RenderPass::type_REFRACTION;
    case ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION:
        return BL::RenderPass::type_TRANSMISSION_COLOR;
    case ::Octane::RenderPassId::RENDER_PASS_SSS:
        return BL::RenderPass::type_SUBSURFACE_COLOR;

    case ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL:
    case ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL:
    case ::Octane::RenderPassId::RENDER_PASS_VERTEX_NORMAL:
        return BL::RenderPass::type_NORMAL;

    case ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH:
        return BL::RenderPass::type_Z;
    case ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID:
        return BL::RenderPass::type_MATERIAL_INDEX;
    case ::Octane::RenderPassId::RENDER_PASS_UV_COORD:
        return BL::RenderPass::type_UV;
    case ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID:
        return BL::RenderPass::type_OBJECT_INDEX;
    case ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION:
        return BL::RenderPass::type_AO;

    case ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS:
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS:
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_COLOR_SHADOWS:
        return BL::RenderPass::type_SHADOW;

    default:
        return BL::RenderPass::type_COMBINED;
    }
    return BL::RenderPass::type_COMBINED;
} //get_blender_pass_type()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Blender render-pass type translated to Octane pass type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int BlenderSession::get_pass_index(::Octane::RenderPassId pass) {
    switch(pass) {
    case ::Octane::RenderPassId::RENDER_PASS_BEAUTY:
        return 0;

    case ::Octane::RenderPassId::RENDER_PASS_EMIT:
        return 1;
    case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT:
        return 2;
    case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT:
        return 3;
    case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT:
        return 4;
    case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT:
        return 5;
    case ::Octane::RenderPassId::RENDER_PASS_REFRACTION:
        return 6;
    case ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION:
        return 7;
    case ::Octane::RenderPassId::RENDER_PASS_SSS:
        return 8;
    case ::Octane::RenderPassId::RENDER_PASS_POST_PROC:
        return 9;
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS:
        return 10;
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS:
        return 11;
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_COLOR_SHADOWS:
        return 12;
    case ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS:
        return 13;

    case ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL:
        return 14;
    case ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL:
        return 15;
    case ::Octane::RenderPassId::RENDER_PASS_POSITION:
        return 16;
    case ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH:
        return 17;
    case ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID:
        return 18;
    case ::Octane::RenderPassId::RENDER_PASS_UV_COORD:
        return 19;
    case ::Octane::RenderPassId::RENDER_PASS_TANGENT_U:
        return 20;
    case ::Octane::RenderPassId::RENDER_PASS_WIREFRAME:
        return 21;
    case ::Octane::RenderPassId::RENDER_PASS_VERTEX_NORMAL:
        return 22;
    case ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID:
        return 23;
    case ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION:
        return 24;
    case ::Octane::RenderPassId::RENDER_PASS_MOTION_VECTOR:
        return 25;
    case ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_ID:
        return 26;
    case ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_MASK:
        return 27;
    case ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT:
        return 28;

    default:
        return 0;
    }
    return 0;
} //get_pass_index()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static BL::RenderResult begin_render_result(BL::RenderEngine b_engine, int x, int y, int w, int h, const char *layername, const char *viewname) {
    return b_engine.begin_result(x, y, w, h, layername, viewname);
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
    BL::RenderResult b_rr = begin_render_result(b_engine, x, y, w, h, b_rlay_name.c_str(), b_rview_name.c_str());

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

    ::Octane::RenderPassId cur_pass_type;
    if(scene->passes->oct_node->bUsePasses)
        cur_pass_type = scene->passes->oct_node->curPassType;
    else
        cur_pass_type = ::Octane::RenderPassId::RENDER_PASS_BEAUTY;

    //if(scene->passes->oct_node->bUsePasses && session->server->currentPassType() != cur_pass_type) {
        session->server->checkImgBufferFloat(4, pixels, width, height,
            (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.z - scene->camera->oct_node->ui4Region.x : width), (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.w - scene->camera->oct_node->ui4Region.y : height), false);
        session->server->downloadImageBuffer(session->params.image_stat, session->params.interactive ? ::OctaneEngine::OctaneClient::IMAGE_8BIT : (session->params.hdr_tonemapped ? ::OctaneEngine::OctaneClient::IMAGE_FLOAT_TONEMAPPED : ::OctaneEngine::OctaneClient::IMAGE_FLOAT), cur_pass_type);
    //}

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
            session->server->getCopyImgBufferFloat(4, mb_pixels, width, height,
                (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.z - scene->camera->oct_node->ui4Region.x : width), (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.w - scene->camera->oct_node->ui4Region.y : height));
        }
        BL::RenderPass b_combined_pass(b_rlay.passes.find_by_type(BL::RenderPass::type_COMBINED, b_rview_name.c_str()));
        b_combined_pass.rect(pixels);
    }
    else if(session->server->getCopyImgBufferFloat(4, pixels, width, height,
            (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.z - scene->camera->oct_node->ui4Region.x : width), (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.w - scene->camera->oct_node->ui4Region.y : height))) {
        BL::RenderPass b_combined_pass(b_rlay.passes.find_by_type(BL::RenderPass::type_COMBINED, b_rview_name.c_str()));
        b_combined_pass.rect(pixels);
    }

    if(scene->passes->oct_node->bUsePasses && (!do_update_only || (motion_blur && mb_type == SUBFRAME && session->params.image_stat.uiCurSamples >= session->params.samples))) {
        // Copy each pass
        BL::RenderLayer::passes_iterator b_iter;
        for(b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter) {
            BL::RenderPass b_pass(*b_iter);

            int components = b_pass.channels();
            buf_size = width * height * components;

            if(session->progress.get_cancel()) break;

            // Find matching pass type
            ::Octane::RenderPassId pass_type = get_octane_pass_type(b_pass);
            if(pass_type == ::Octane::RenderPassId::RENDER_PASS_BEAUTY)
                continue;
            else if(pass_type == ::Octane::RenderPassId::PASS_NONE || !session->server->downloadImageBuffer(session->params.image_stat, session->params.interactive ? ::OctaneEngine::OctaneClient::IMAGE_8BIT : (session->params.hdr_tonemapped ? ::OctaneEngine::OctaneClient::IMAGE_FLOAT_TONEMAPPED : ::OctaneEngine::OctaneClient::IMAGE_FLOAT), pass_type)) {
                if(!do_update_only) {
                    float* pixels  = new float[buf_size];
                    memset(pixels, 0, sizeof(float) * buf_size);
                    b_pass.rect(pixels);
                    delete[] pixels;
                }
                continue;
            }
            int pass_idx = get_pass_index(pass_type);

            if(session->progress.get_cancel()) break;

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
                    session->server->getCopyImgBufferFloat(components, mb_pixels, width, height,
                        (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.z - scene->camera->oct_node->ui4Region.x : width), (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.w - scene->camera->oct_node->ui4Region.y : height));
                }
                b_pass.rect(pixels);
            }
            else {
                if(session->server->getCopyImgBufferFloat(components, pixels, width, height,
                    (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.z - scene->camera->oct_node->ui4Region.x : width), (scene->camera->oct_node->bUseRegion ? scene->camera->oct_node->ui4Region.w - scene->camera->oct_node->ui4Region.y : height)))
                    b_pass.rect(pixels);
            }
        } //for(b_rlay.passes.begin(b_iter); b_iter != b_rlay.passes.end(); ++b_iter)
    } //if(scene->passes->use_passes && (!do_update_only || (motion_blur && mb_type == SUBFRAME && session->params.image_stat.cur_samples >= session->params.samples)))

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
    if(session_params.export_scene != ::OctaneEngine::OctaneClient::SceneExportTypes::NONE) {
        sync->sync_data(b_v3d, b_engine.camera_override());
        sync->sync_camera(b_engine.camera_override(), width, height);

        session->update_scene_to_server(0, 1);
        session->server->startRender(width, height, ::OctaneEngine::OctaneClient::IMAGE_8BIT, session_params.out_of_core_enabled, session_params.out_of_core_mem_limit, session_params.out_of_core_gpu_headroom);

        if(b_engine.test_break() || b_scene.frame_current() >= b_scene.frame_end()) {
            session->progress.set_status("Transferring scene file...");
            session->server->stopRender(session_params.fps);
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
    BL::RenderSettings::layers_iterator b_layer_iter;
    BL::RenderResult::views_iterator    b_view_iter;
    for(render.layers.begin(b_layer_iter); b_layer_iter != render.layers.end(); ++b_layer_iter) {
        clear_passes_buffers();
        BL::RenderLayer cur_layer(*b_layer_iter);
        b_rlay_name = b_layer_iter->name();

        // Temporary render result to find needed passes and views.
        BL::RenderResult b_rr = begin_render_result(b_engine, 0, 0, 1, 1, b_rlay_name.c_str(), NULL);
        BL::RenderResult::layers_iterator b_single_rlay;
        b_rr.layers.begin(b_single_rlay);

        // Layer will be missing if it was disabled in the UI.
        if(b_single_rlay == b_rr.layers.end()) {
            end_render_result(b_engine, b_rr, true, false);
            continue;
        }

        std::vector<std::string> views;
        for(b_rr.views.begin(b_view_iter); b_view_iter != b_rr.views.end(); ++b_view_iter) {
            views.push_back(b_view_iter->name());
        }

        // Free result without merging.
        end_render_result(b_engine, b_rr, true, false);

        sync->sync_data(b_v3d, b_engine.camera_override(), &cur_layer);
        sync->sync_camera(b_engine.camera_override(), width, height);

        for(int i = 0; i < views.size(); ++i) {
            b_rview_name = views[i];

            // Set the current view.
            b_engine.active_view_set(b_rview_name.c_str());

            // Render
            if(motion_blur && mb_type == SUBFRAME && mb_samples > 1) {
                mb_sample_in_work = 0;
                float subframe = 0;
                int cur_frame = b_scene.frame_current();
                for(mb_cur_sample = 1; mb_cur_sample <= mb_samples; ++mb_cur_sample) {
                    session->start("Final render", true, 0, 1);
                    //session->params.image_stat.uiCurSamples = 0;

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
                int total_frames;
                int int_frame_idx = load_internal_mb_sequence(stop_render, total_frames, &cur_layer);

                if(!stop_render) {
                    session->start("Final render", true, int_frame_idx, 0);
                    //session->params.image_stat.uiCurSamples = 0;
                }
            }
            else {
                if(motion_blur) motion_blur = false;
                mb_cur_sample = 0;
                if(!stop_render) {
                    session->start("Final render", true, 0, 1);
                    //session->params.image_stat.uiCurSamples = 0;
                }
            }

            write_render_img();

            if(session->progress.get_cancel()) {
                stop_render = true;
                break;
            }
        }
    } //for(r.layers.begin(b_iter); b_iter != r.layers.end(); ++b_iter)

    clear_passes_buffers();

    if(stop_render || !b_engine.is_animation() || b_scene.frame_current() >= b_scene.frame_end())
        session->server->stopRender(session_params.fps);
} //render()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// "sync" python API function
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSession::synchronize() {
    if(!sync_mutex.try_lock()) return;

    SessionParams session_params;

    session_params = BlenderSync::get_session_params(b_engine, b_userpref, b_scene, interactive);
    if(session->params.modified(session_params)) {
        sync_mutex.unlock();
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
        sync_mutex.unlock();
        return;
    }

    // Data synchronize
    if(b_rv3d) {
        if(motion_blur && mb_type == INTERNAL) {
            bool stop_render;
            int total_frames;
            load_internal_mb_sequence(stop_render, total_frames, (BL::RenderLayer*)0, true);
        }
        else
            sync->sync_data(b_v3d, b_engine.camera_override());
    }

    // Camera synchronize
    if(b_rv3d)
        sync->sync_view(b_v3d, b_rv3d, width, height);
    //else
    //    sync->sync_camera(b_engine.camera_override(), width, height);

    // Unlock
    session->scene->mutex.unlock();

    // Reset if needed
    if(scene->need_reset()) {
        BufferParams buffer_params = BlenderSync::get_display_buffer_params(scene->camera, width, height);
        session->update(buffer_params);
    }

    sync_mutex.unlock();
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
            progress = (((float)session->params.samples + (float)session->params.image_stat.uiCurSamples) / (float)session->params.samples);
    }
    else {
        if(session->params.samples * mb_samples == 0)
            progress = 0;
        else
            progress = (((float)session->params.samples * mb_samples + (float)session->params.samples * (mb_sample_in_work - 1) + (float)session->params.image_stat.uiCurSamples) / ((float)session->params.samples * mb_samples));
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
    if(b_rview_name != "") timestatus += ", " + b_rview_name;
    timestatus += " | ";

    BLI_timecode_string_from_time_simple(time_str, 60, total_time);
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

