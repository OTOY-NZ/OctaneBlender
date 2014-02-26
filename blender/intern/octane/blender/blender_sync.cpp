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

Kernel::ChannelType channel_translator[] = {
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
void BlenderSync::sync_data(PassType pass_type, BL::SpaceView3D b_v3d, BL::Object b_override, const char *layer) {
	sync_render_layers(b_v3d, layer);
	sync_kernel(pass_type);
	sync_shaders(); //Environment here so far...
	sync_objects(b_v3d);
} //sync_data()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get additional Octane scene settings.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_kernel(PassType pass_type) {
	PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

	Kernel *kernel      = scene->kernel;
	Kernel prevkernel   = *kernel;

    switch(pass_type) {
        case PASS_COMBINED:
            kernel->kernel_type         = static_cast<Kernel::KernelType>(RNA_enum_get(&oct_scene, "kernel_type"));
            kernel->info_channel_type   = channel_translator[RNA_enum_get(&oct_scene, "info_channel_type")];
            break;
        case PASS_DEPTH:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_ZDEPTH;
            break;
        case PASS_GEO_NORMALS:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_GEOMETRICNORMALS;
            break;
        case PASS_SHADING_NORMALS:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_SHADINGNORMALS;
            break;
        case PASS_MATERIAL_ID:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_MATERIALID;
            break;
        case PASS_POSITION:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_POSITION;
            break;
        case PASS_TEX_COORD:
            kernel->kernel_type         = Kernel::INFO_CHANNEL;
            kernel->info_channel_type   = Kernel::CHANNEL_TEXTURESCOORDINATES;
            break;
        default:
            kernel->kernel_type         = static_cast<Kernel::KernelType>(RNA_enum_get(&oct_scene, "kernel_type"));
            kernel->info_channel_type   = channel_translator[RNA_enum_get(&oct_scene, "info_channel_type")];
            break;
    }
    kernel->max_samples         = get_int(oct_scene, "max_samples");
    if(scene->session->b_session && scene->session->b_session->motion_blur && scene->session->b_session->mb_samples > 1)
        kernel->max_samples = kernel->max_samples / scene->session->b_session->mb_samples;
    if(kernel->max_samples < 1) kernel->max_samples = 1;

    kernel->max_preview_samples = get_int(oct_scene, "max_preview_samples");
    kernel->filter_size         = get_float(oct_scene, "filter_size");
    kernel->ray_epsilon         = get_float(oct_scene, "ray_epsilon");
    kernel->rrprob              = get_float(oct_scene, "rrprob");
    kernel->alpha_channel       = get_boolean(oct_scene, "alpha_channel");
    kernel->keep_environment    = get_boolean(oct_scene, "keep_environment");
    kernel->alpha_shadows       = get_boolean(oct_scene, "alpha_shadows");
    kernel->bump_normal_mapping = get_boolean(oct_scene, "bump_normal_mapping");
    kernel->wf_bktrace_hl       = get_boolean(oct_scene, "wf_bktrace_hl");

    kernel->max_depth       = get_int(oct_scene, "max_depth");
    kernel->caustic_blur    = get_float(oct_scene, "caustic_blur");

    kernel->specular_depth  = get_int(oct_scene, "specular_depth");
    kernel->glossy_depth    = get_int(oct_scene, "glossy_depth");
    kernel->ao_dist         = get_float(oct_scene, "ao_dist");
    kernel->gi_mode         = static_cast<Kernel::GIType>(RNA_enum_get(&oct_scene, "gi_mode"));
    kernel->diffuse_depth   = get_int(oct_scene, "diffuse_depth");

    kernel->exploration     = get_float(oct_scene, "exploration");
    kernel->direct_light_importance = get_float(oct_scene, "direct_light_importance");
    kernel->max_rejects     = get_int(oct_scene, "max_rejects");
    kernel->parallelism     = get_int(oct_scene, "parallelism");

    kernel->zdepth_max      = get_float(oct_scene, "zdepth_max");
    kernel->uv_max          = get_float(oct_scene, "uv_max");

	if(kernel->modified(prevkernel)) kernel->tag_update();

	// GPUs
    int iValues[8] = {0,0,0,0,0,0,0,0};
    RNA_boolean_get_array(&oct_scene, "devices", iValues);
    kernel->uiGPUs = 0;
    for(int i=0; i<8; ++i)
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

	for(r.layers.begin(b_rlay); b_rlay != r.layers.end(); ++b_rlay) {
		if((!layer && first_layer) || (layer && b_rlay->name() == layer)) {
			render_layer.name                       = b_rlay->name();
			render_layer.scene_layer                = get_layer(b_scene.layers()) & ~get_layer(b_rlay->layers_exclude());
			render_layer.layer                      = get_layer(b_rlay->layers());
			render_layer.holdout_layer              = get_layer(b_rlay->layers_zmask());
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
    string login = get_string(oct_scene, "server_login");
    if(login.length() > 0) {
        string pass = get_string(oct_scene, "server_pass");
        if(pass.length() > 0) {
            params.login = login;
            params.pass  = pass;
            RNA_string_set(&oct_scene, "server_login", "");
            RNA_string_set(&oct_scene, "server_pass", "");
        }
    }

	// Interactive
	params.interactive = interactive;

	// Samples
    if(!interactive) {
        params.samples = get_int(oct_scene, "max_samples");
    }
	else {
		params.samples = get_int(oct_scene, "max_preview_samples");
		if(params.samples == 0) params.samples = 16000;
	}

    params.export_alembic       = interactive ? false : get_boolean(oct_scene, "export_alembic");

    params.use_passes           = get_boolean(oct_scene, "use_passes");
    params.meshes_type          = static_cast<Mesh::MeshType>(params.export_alembic ? 2 : RNA_enum_get(&oct_scene, "meshes_type"));
    params.use_viewport_hide    = get_boolean(oct_scene, "viewport_hide");
	
	return params;
} //get_session_params()

OCT_NAMESPACE_END

