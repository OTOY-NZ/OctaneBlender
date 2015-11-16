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

#include "scene.h"
#include "session.h"

#include "blender_sync.h"
#include "blender_session.h"
#include "blender_util.h"

OCT_NAMESPACE_BEGIN

static Kernel::ChannelType channel_translator[] = {
    Kernel::CHANNEL_GEOMETRICNORMALS,
    Kernel::CHANNEL_SHADINGNORMALS,
    Kernel::CHANNEL_POSITION,
    Kernel::CHANNEL_ZDEPTH,
    Kernel::CHANNEL_MATERIALID,
    Kernel::CHANNEL_TEXTURESCOORDINATES,
    Kernel::CHANNEL_WIREFRAME,
    Kernel::CHANNEL_VERTEXNORMAL
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BlenderSync::BlenderSync(BL::RenderEngine b_engine_, BL::BlendData b_data_, BL::Scene b_scene_, Scene *scene_, bool interactive_, Progress &progress_)
                            : b_engine(b_engine_),
                              b_data(b_data_), b_scene(b_scene_),
                              shader_map(&scene_->shaders),
                              object_map(scene_, &scene_->objects),
                              mesh_map(&scene_->meshes),
                              light_object_map(scene_, &scene_->light_objects),
                              light_map(&scene_->lights),
                              world_map(NULL),
                              world_recalc(false),
                              progress(progress_) {
	scene = scene_;
	interactive = interactive_;
} //BlenderSync()

BlenderSync::~BlenderSync() {
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Sync recalc flags from blender to OctaneRender. Actual update is done separate,
// so we can do it later on if doing it immediate is not suitable.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::sync_recalc() {
	BL::BlendData::materials_iterator b_mat;
	for(b_data.materials.begin(b_mat); b_mat != b_data.materials.end(); ++b_mat)
		if(b_mat->is_updated() || (b_mat->node_tree() && b_mat->node_tree().is_updated()))
			shader_map.set_recalc(*b_mat);

	//FIXME: Perhaps not needed...
	BL::BlendData::textures_iterator b_tex;
	for(b_data.textures.begin(b_tex); b_tex != b_data.textures.end(); ++b_tex)
		if(b_tex->is_updated() || (b_tex->node_tree() && b_tex->node_tree().is_updated()))
			shader_map.set_recalc(*b_tex);

    BL::BlendData::lamps_iterator b_lamp;
	for(b_data.lamps.begin(b_lamp); b_lamp != b_data.lamps.end(); ++b_lamp)
		if(b_lamp->is_updated() || (b_lamp->node_tree() && b_lamp->node_tree().is_updated()))
			shader_map.set_recalc(*b_lamp);

	BL::BlendData::objects_iterator b_ob;
	for(b_data.objects.begin(b_ob); b_ob != b_data.objects.end(); ++b_ob) {
		if(b_ob->is_updated()) {
			if(object_is_light(*b_ob)) light_object_map.set_recalc(*b_ob);
			else object_map.set_recalc(*b_ob);
		}

		if(object_is_mesh(*b_ob)) {
			if(b_ob->is_updated_data() || b_ob->data().is_updated()) {
				BL::ID key = BKE_object_is_modified(*b_ob) ? *b_ob : b_ob->data();
				mesh_map.set_recalc(key);
			}
		}
		else if(object_is_light(*b_ob)) {
			if(b_ob->is_updated_data() || b_ob->data().is_updated())
				light_map.set_recalc(b_ob->data());
		}
	}

	BL::BlendData::meshes_iterator b_mesh;
	for(b_data.meshes.begin(b_mesh); b_mesh != b_data.meshes.end(); ++b_mesh)
		if(b_mesh->is_updated())
			mesh_map.set_recalc(*b_mesh);

	BL::BlendData::worlds_iterator b_world;
	for(b_data.worlds.begin(b_world); b_world != b_data.worlds.end(); ++b_world) {
		if(world_map == b_world->ptr.data && (b_world->is_updated() || (b_world->node_tree() && b_world->node_tree().is_updated()))) {
			world_recalc = true;
		}
	}

	bool recalc =
		shader_map.has_recalc() ||
		object_map.has_recalc() ||
		light_map.has_recalc() ||
		mesh_map.has_recalc() ||
		BlendDataObjects_is_updated_get(&b_data.ptr) ||
		world_recalc;

	return recalc;
} //sync_recalc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Syncronise all scene data
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_data(BL::SpaceView3D b_v3d, BL::Object b_override, BL::RenderLayer *layer, int motion) {
    sync_render_layers(b_v3d, layer ? layer->name().c_str() : 0);
    sync_passes(layer);
	sync_kernel();
	sync_shaders(); //Environment here so far...
	sync_objects(b_v3d, motion);
} //sync_data()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane render passes settings.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_passes(BL::RenderLayer *layer) {
	PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

    PointerRNA rlayer;
    if(layer)
        rlayer = layer->ptr;
    else {
        BL::RenderLayer b_rlay = static_cast<BL::RenderLayer>(b_scene.render().layers.active());
        rlayer = b_rlay.ptr;
    }

	Passes *passes      = scene->passes;
    Passes prevpasses   = *passes;

    passes->use_passes = get_boolean(oct_scene, "use_passes");
    if(passes->use_passes) {
        passes->cur_pass_type = pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];

        passes->pass_max_samples            = get_int(oct_scene, "pass_max_samples");
        passes->pass_ao_max_samples         = get_int(oct_scene, "pass_ao_max_samples");
        passes->pass_distributed_tracing    = get_boolean(oct_scene, "pass_distributed_tracing");
        passes->pass_filter_size            = get_float(oct_scene, "pass_filter_size");
        passes->pass_z_depth_max            = get_float(oct_scene, "pass_z_depth_max");
        passes->pass_uv_max                 = get_float(oct_scene, "pass_uv_max");
        passes->pass_max_speed              = get_float(oct_scene, "pass_max_speed");
        passes->pass_ao_distance            = get_float(oct_scene, "pass_ao_distance");
        passes->pass_alpha_shadows          = get_boolean(oct_scene, "pass_alpha_shadows");

        if(!interactive) {
            passes->combined_pass               = get_boolean(rlayer, "use_pass_combined");
            passes->emitters_pass               = get_boolean(rlayer, "use_pass_emit");
            passes->environment_pass            = get_boolean(rlayer, "use_pass_environment");
            passes->diffuse_direct_pass         = get_boolean(rlayer, "use_pass_diffuse_direct");
            passes->diffuse_indirect_pass       = get_boolean(rlayer, "use_pass_diffuse_indirect");

            bool cur_use = get_boolean(rlayer, "use_pass_reflection");
            int  subtype = RNA_enum_get(&oct_scene, "reflection_pass_subtype");
            passes->reflection_direct_pass      = cur_use && (subtype == 0);
            passes->reflection_indirect_pass    = cur_use && (subtype == 1);
            passes->layer_reflections_pass      = cur_use && (subtype == 1);

            passes->refraction_pass             = get_boolean(rlayer, "use_pass_refraction");
            passes->transmission_pass           = get_boolean(rlayer, "use_pass_transmission_color");
            passes->subsurf_scattering_pass     = get_boolean(rlayer, "use_pass_subsurface_color");
            passes->post_processing_pass        = false;

            cur_use = get_boolean(rlayer, "use_pass_normal");
            subtype = RNA_enum_get(&oct_scene, "normal_pass_subtype");
            passes->geom_normals_pass           = cur_use && (subtype == 0);
            passes->shading_normals_pass        = cur_use && (subtype == 1);
            passes->vertex_normals_pass         = cur_use && (subtype == 2);

            passes->position_pass               = false;
            passes->z_depth_pass                = get_boolean(rlayer, "use_pass_z");
            passes->material_id_pass            = get_boolean(rlayer, "use_pass_material_index");
            passes->uv_coordinates_pass         = get_boolean(rlayer, "use_pass_uv");
            passes->tangents_pass               = false;
            passes->wireframe_pass              = false;
            passes->object_id_pass              = get_boolean(rlayer, "use_pass_object_index");
            passes->ao_pass                     = get_boolean(rlayer, "use_pass_ambient_occlusion");
            passes->motion_vector_pass          = false;

            cur_use = get_boolean(rlayer, "use_pass_shadow");
            subtype = RNA_enum_get(&oct_scene, "shadows_pass_subtype");
            passes->layer_shadows_pass          = cur_use && (subtype == 0);
            passes->layer_black_shadows_pass    = cur_use && (subtype == 1);
            passes->layer_color_shadows_pass    = cur_use && (subtype == 2);

            passes->layer_id_pass               = false;
            passes->layer_mask_pass             = false;
            passes->light_pass_id_pass          = false;

            passes->ambient_light_pass          = false;
            passes->sunlight_pass               = false;
            passes->light1_pass                 = false;
            passes->light2_pass                 = false;
            passes->light3_pass                 = false;
            passes->light4_pass                 = false;
            passes->light5_pass                 = false;
            passes->light6_pass                 = false;
            passes->light7_pass                 = false;
            passes->light8_pass                 = false;
        }
        else {
            passes->combined_pass               = false;

            passes->emitters_pass               = false;
            passes->environment_pass            = false;
            passes->diffuse_direct_pass         = false;
            passes->diffuse_indirect_pass       = false;
            passes->reflection_direct_pass      = false;
            passes->reflection_indirect_pass    = false;
            passes->refraction_pass             = false;
            passes->transmission_pass           = false;
            passes->subsurf_scattering_pass     = false;
            passes->post_processing_pass        = false;

            passes->layer_shadows_pass          = false;
            passes->layer_black_shadows_pass    = false;
            passes->layer_color_shadows_pass    = false;
            passes->layer_reflections_pass      = false;

            passes->ambient_light_pass          = false;
            passes->sunlight_pass               = false;
            passes->light1_pass                 = false;
            passes->light2_pass                 = false;
            passes->light3_pass                 = false;
            passes->light4_pass                 = false;
            passes->light5_pass                 = false;
            passes->light6_pass                 = false;
            passes->light7_pass                 = false;
            passes->light8_pass                 = false;

            passes->geom_normals_pass           = false;
            passes->shading_normals_pass        = false;
            passes->vertex_normals_pass         = false;
            passes->position_pass               = false;
            passes->z_depth_pass                = false;
            passes->material_id_pass            = false;
            passes->uv_coordinates_pass         = false;
            passes->tangents_pass               = false;
            passes->wireframe_pass              = false;
            passes->motion_vector_pass          = false;
            passes->object_id_pass              = false;
            passes->layer_id_pass               = false;
            passes->layer_mask_pass             = false;
            passes->light_pass_id_pass          = false;

            passes->ao_pass                     = false;

            switch(passes->cur_pass_type) {
            case Passes::COMBINED:
                passes->combined_pass = true;
                break;

            case Passes::EMIT:
                passes->emitters_pass = true;
                break;
            case Passes::ENVIRONMENT:
                passes->environment_pass = true;
                break;
            case Passes::DIFFUSE_DIRECT:
                passes->diffuse_direct_pass = true;
                break;
            case Passes::DIFFUSE_INDIRECT:
                passes->diffuse_indirect_pass = true;
                break;
            case Passes::REFLECTION_DIRECT:
                passes->reflection_direct_pass = true;
                break;
            case Passes::REFLECTION_INDIRECT:
                passes->reflection_indirect_pass = true;
                break;
            case Passes::REFRACTION:
                passes->refraction_pass = true;
                break;
            case Passes::TRANSMISSION:
                passes->transmission_pass = true;
                break;
            case Passes::SSS:
                passes->subsurf_scattering_pass = true;
                break;
            case Passes::POST_PROC:
                passes->post_processing_pass = true;
                break;

            case Passes::LAYER_SHADOWS:
                passes->layer_shadows_pass = true;
                break;
            case Passes::LAYER_BLACK_SHADOWS:
                passes->layer_black_shadows_pass = true;
                break;
            case Passes::LAYER_COLOR_SHADOWS:
                passes->layer_color_shadows_pass = true;
                break;
            case Passes::LAYER_REFLECTIONS:
                passes->layer_reflections_pass = true;
                break;

            case Passes::AMBIENT_LIGHT:
                passes->ambient_light_pass = true;
                break;
            case Passes::SUNLIGHT:
                passes->sunlight_pass = true;
                break;
            case Passes::LIGHT1:
                passes->light1_pass = true;
                break;
            case Passes::LIGHT2:
                passes->light2_pass = true;
                break;
            case Passes::LIGHT3:
                passes->light3_pass = true;
                break;
            case Passes::LIGHT4:
                passes->light4_pass = true;
                break;
            case Passes::LIGHT5:
                passes->light5_pass = true;
                break;
            case Passes::LIGHT6:
                passes->light6_pass = true;
                break;
            case Passes::LIGHT7:
                passes->light7_pass = true;
                break;
            case Passes::LIGHT8:
                passes->light8_pass = true;
                break;

            case Passes::GEOMETRIC_NORMAL:
                passes->geom_normals_pass = true;
                break;
            case Passes::SHADING_NORMAL:
                passes->shading_normals_pass = true;
                break;
            case Passes::VERTEX_NORMAL:
                passes->vertex_normals_pass = true;
                break;
            case Passes::POSITION:
                passes->position_pass = true;
                break;
            case Passes::Z_DEPTH:
                passes->z_depth_pass = true;
                break;
            case Passes::MATERIAL_ID:
                passes->material_id_pass = true;
                break;
            case Passes::UV_COORD:
                passes->uv_coordinates_pass = true;
                break;
            case Passes::TANGENT_U:
                passes->tangents_pass = true;
                break;
            case Passes::WIREFRAME:
                passes->wireframe_pass = true;
                break;
            case Passes::OBJECT_ID:
                passes->object_id_pass = true;
                break;
            case Passes::MOTION_VECTOR:
                passes->motion_vector_pass = true;
                break;
            case Passes::LAYER_ID:
                passes->layer_id_pass = true;
                break;
            case Passes::LAYER_MASK:
                passes->layer_mask_pass = true;
                break;
            case Passes::LIGHT_PASS_ID:
                passes->light_pass_id_pass = true;
                break;

            case Passes::AMBIENT_OCCLUSION:
                passes->ao_pass = true;
                break;

            default:
                passes->combined_pass = true;
                break;
            }
        }
    } //if(passes->use_passes)
    
    if(passes->modified(prevpasses)) passes->tag_update();
} //sync_passes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get additional Octane scene settings.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_kernel() {
    PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

    Kernel *kernel = scene->kernel;
    Kernel prevkernel = *kernel;

    kernel->kernel_type = static_cast<Kernel::KernelType>(RNA_enum_get(&oct_scene, "kernel_type"));
    kernel->info_channel_type = channel_translator[RNA_enum_get(&oct_scene, "info_channel_type")];

    Passes::PassTypes cur_pass_type = pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];
    if(cur_pass_type == Passes::COMBINED) {
        kernel->max_samples = get_int(oct_scene, "max_samples");
        kernel->max_preview_samples = get_int(oct_scene, "max_preview_samples");
        if(kernel->max_preview_samples == 0) kernel->max_preview_samples = 16000;
    }
    else if(cur_pass_type == Passes::AMBIENT_OCCLUSION) {
        kernel->max_samples = get_int(oct_scene, "pass_ao_max_samples");
        kernel->max_preview_samples = kernel->max_samples;
    }
    else {
        kernel->max_samples = get_int(oct_scene, "pass_max_samples");
        kernel->max_preview_samples = kernel->max_samples;
    }
    if(scene->session->b_session && scene->session->b_session->motion_blur && scene->session->b_session->mb_type == BlenderSession::SUBFRAME && scene->session->b_session->mb_samples > 1)
        kernel->max_samples = kernel->max_samples / scene->session->b_session->mb_samples;
    if(kernel->max_samples < 1) kernel->max_samples = 1;

    kernel->filter_size = get_float(oct_scene, "filter_size");
    kernel->ray_epsilon = get_float(oct_scene, "ray_epsilon");
    kernel->alpha_channel = get_boolean(oct_scene, "alpha_channel");
    kernel->alpha_shadows = get_boolean(oct_scene, "alpha_shadows");
    kernel->keep_environment = get_boolean(oct_scene, "keep_environment");
    kernel->bump_normal_mapping = get_boolean(oct_scene, "bump_normal_mapping");
    kernel->wf_bktrace_hl = get_boolean(oct_scene, "wf_bktrace_hl");
    kernel->path_term_power = get_float(oct_scene, "path_term_power");

    kernel->caustic_blur = get_float(oct_scene, "caustic_blur");
    kernel->max_diffuse_depth = get_int(oct_scene, "max_diffuse_depth");
    kernel->max_glossy_depth = get_int(oct_scene, "max_glossy_depth");

    kernel->coherent_ratio = get_float(oct_scene, "coherent_ratio");
    kernel->static_noise = get_boolean(oct_scene, "static_noise");

    kernel->specular_depth = get_int(oct_scene, "specular_depth");
    kernel->glossy_depth = get_int(oct_scene, "glossy_depth");
    kernel->ao_dist = get_float(oct_scene, "ao_dist");
    kernel->gi_mode = static_cast<Kernel::GIType>(RNA_enum_get(&oct_scene, "gi_mode"));
    kernel->diffuse_depth = get_int(oct_scene, "diffuse_depth");

    kernel->exploration = get_float(oct_scene, "exploration");
    kernel->gi_clamp = get_float(oct_scene, "gi_clamp");
    kernel->direct_light_importance = get_float(oct_scene, "direct_light_importance");
    kernel->max_rejects = get_int(oct_scene, "max_rejects");
    kernel->parallelism = get_int(oct_scene, "parallelism");

    kernel->zdepth_max = get_float(oct_scene, "zdepth_max");
    kernel->uv_max = get_float(oct_scene, "uv_max");
    kernel->distributed_tracing = get_boolean(oct_scene, "distributed_tracing");
    kernel->max_speed = get_float(oct_scene, "max_speed");

    kernel->layers_enable = get_boolean(oct_scene, "layers_enable");
    kernel->layers_current = get_int(oct_scene, "layers_current");
    kernel->layers_invert = get_boolean(oct_scene, "layers_invert");

    BL::RenderSettings r = b_scene.render();
    kernel->shuttertime = r.motion_blur_shutter();

    if(kernel->modified(prevkernel)) kernel->tag_update();

    // GPUs
    int iValues[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    RNA_boolean_get_array(&oct_scene, "devices", iValues);
    kernel->uiGPUs = 0;
    for(int i = 0; i < 8; ++i)
        if(iValues[i]) kernel->uiGPUs |= 0x01 << i;

    if(kernel->uiGPUs != prevkernel.uiGPUs) kernel->tag_updateGPUs();
} //sync_kernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get render layer (by name, or first one if name is NULL)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_render_layers(BL::SpaceView3D b_v3d, const char *layer) {
	string layername;

	// 3d view
	if(b_v3d) {
		PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

		if(RNA_boolean_get(&oct_scene, "preview_active_layer")) {
			BL::RenderLayers layers(b_scene.render().ptr);
			layername   = layers.active().name();
			layer       = layername.c_str();
		}
		else {
			render_layer.use_localview              = (b_v3d.local_view() ? true : false);
			render_layer.scene_layer                = get_layer(b_v3d.layers(), b_v3d.layers_local_view(), render_layer.use_localview);
			render_layer.layer                      = render_layer.scene_layer;
			render_layer.holdout_layer              = 0;
			render_layer.material_override          = PointerRNA_NULL;
			render_layer.use_background             = true;
			render_layer.use_viewport_visibility    = true;
			render_layer.samples                    = 0;
			return;
		}
	}

	// Render layer
	BL::RenderSettings r = b_scene.render();
	BL::RenderSettings::layers_iterator b_rlay;
	bool first_layer = true;
	uint layer_override = get_layer(b_engine.layer_override());
	uint scene_layers = layer_override ? layer_override : get_layer(b_scene.layers());

	for(r.layers.begin(b_rlay); b_rlay != r.layers.end(); ++b_rlay) {
		if((!layer && first_layer) || (layer && b_rlay->name() == layer)) {
			render_layer.name                       = b_rlay->name();
			render_layer.holdout_layer              = get_layer(b_rlay->layers_zmask());
			render_layer.exclude_layer              = get_layer(b_rlay->layers_exclude());
			render_layer.scene_layer                = scene_layers & ~render_layer.exclude_layer;
			render_layer.scene_layer                |= render_layer.exclude_layer & render_layer.holdout_layer;
            render_layer.layer                      = get_layer(b_rlay->layers());
			render_layer.layer                      |= render_layer.holdout_layer;
			render_layer.material_override          = b_rlay->material_override();
			render_layer.use_background             = b_rlay->use_sky();
            render_layer.use_viewport_visibility    = (b_v3d ? false : scene->use_viewport_hide);//false;
			render_layer.use_localview              = false;
			render_layer.samples                    = b_rlay->samples();
		}
		first_layer = false;
	}
} //sync_render_layers()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get current render session pause state (pause is pressed or not)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::get_session_pause_state(BL::Scene b_scene, bool interactive) {
	PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
	return (!interactive) ? false : get_boolean(oct_scene, "preview_pause");
} //get_session_pause_state()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Set current render session pause state
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::set_session_pause_state(BL::Scene b_scene, bool state) {
	PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
	set_boolean(oct_scene, "preview_pause", state);
} //get_session_pause_state()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get Octane common settings
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SessionParams BlenderSync::get_session_params(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::Scene b_scene, bool interactive) {
	SessionParams params;
	PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

	// Render-server address
	params.server = RenderServer::get_info();
    string server_addr = get_string(oct_scene, "server_address");
    if(server_addr.length() > 0)
        ::strcpy(params.server.net_address, server_addr.c_str());

    string login        = get_string(oct_scene, "server_login");
    string pass         = get_string(oct_scene, "server_pass");
    string stand_login  = get_string(oct_scene, "stand_login");
    string stand_pass   = get_string(oct_scene, "stand_pass");
    if(stand_login.length() > 0 || stand_pass.length() > 0 || login.length() > 0 || pass.length() > 0) {
        fprintf(stderr, "Octane: WARNING: you can't use the server activation form during active rendering session.\n");
        RNA_string_set(&oct_scene, "stand_login", "");
        RNA_string_set(&oct_scene, "stand_pass", "");
        RNA_string_set(&oct_scene, "server_login", "");
        RNA_string_set(&oct_scene, "server_pass", "");
    }

	// Interactive
	params.interactive = interactive;

	// Samples
    Passes::PassTypes cur_pass_type = pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];
    if(cur_pass_type == Passes::COMBINED) {
        if(!interactive) {
            params.samples = get_int(oct_scene, "max_samples");
        }
	    else {
		    params.samples = get_int(oct_scene, "max_preview_samples");
		    if(params.samples == 0) params.samples = 16000;
	    }
    }
    else if(cur_pass_type == Passes::AMBIENT_OCCLUSION) {
        params.samples = get_int(oct_scene, "pass_ao_max_samples");
    }
    else {
        params.samples = get_int(oct_scene, "pass_max_samples");
    }

    params.anim_mode            = static_cast<AnimationMode>(RNA_enum_get(&oct_scene, "anim_mode"));
    params.export_scene         = interactive ? 0 : get_enum(oct_scene, "export_scene");

    params.use_passes           = get_boolean(oct_scene, "use_passes");
    params.meshes_type          = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_scene, "meshes_type"));
    if(params.export_scene && params.meshes_type == Mesh::GLOBAL)
        params.meshes_type = Mesh::RESHAPABLE_PROXY;
    params.use_viewport_hide    = get_boolean(oct_scene, "viewport_hide");
    params.hdr_tonemapped       = get_boolean(oct_scene, "hdr_tonemapped");
	
    params.fps = (float)b_scene.render().fps() / b_scene.render().fps_base();

    params.out_of_core_enabled = get_boolean(oct_scene, "out_of_core_enable");
    params.out_of_core_mem_limit = get_int(oct_scene, "out_of_core_limit");
    params.out_of_core_gpu_headroom = get_int(oct_scene, "out_of_core_gpu_headroom");

	return params;
} //get_session_params()

OCT_NAMESPACE_END

