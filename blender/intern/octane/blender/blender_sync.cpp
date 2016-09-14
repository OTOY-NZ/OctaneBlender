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
#include "render/kernel.h"

#include "blender_sync.h"
#include "blender_session.h"
#include "blender_util.h"

OCT_NAMESPACE_BEGIN

static ::Octane::InfoChannelType channel_translator[] = {
    ::Octane::IC_TYPE_GEOMETRIC_NORMAL,
    ::Octane::IC_TYPE_SHADING_NORMAL,
    ::Octane::IC_TYPE_POSITION,
    ::Octane::IC_TYPE_Z_DEPTH,
    ::Octane::IC_TYPE_MATERIAL_ID,
    ::Octane::IC_TYPE_UV_COORD,
    ::Octane::IC_TYPE_WIREFRAME,
    ::Octane::IC_TYPE_VERTEX_NORMAL
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

    passes->oct_node->bUsePasses = get_boolean(oct_scene, "use_passes");
    if(passes->oct_node->bUsePasses) {
        passes->oct_node->curPassType = Passes::pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];

        passes->oct_node->iMaxSamples           = get_int(oct_scene, "pass_max_samples");
        passes->oct_node->bDistributedTracing   = get_boolean(oct_scene, "pass_distributed_tracing");
        passes->oct_node->fZdepthMax            = get_float(oct_scene, "pass_z_depth_max");
        passes->oct_node->fUVMax                = get_float(oct_scene, "pass_uv_max");
        passes->oct_node->fMaxSpeed             = get_float(oct_scene, "pass_max_speed");
        passes->oct_node->fAODistance           = get_float(oct_scene, "pass_ao_distance");
        passes->oct_node->bAoAlphaShadows       = get_boolean(oct_scene, "pass_alpha_shadows");
        passes->oct_node->bPassesRaw            = get_boolean(oct_scene, "pass_raw");
        passes->oct_node->bPostProcEnvironment  = get_boolean(oct_scene, "pass_pp_env");
        passes->oct_node->bBump                 = get_boolean(oct_scene, "pass_bump");
        passes->oct_node->fOpacityThreshold     = get_float(oct_scene, "pass_opacity_threshold");

        if(!interactive) {
            passes->oct_node->bBeautyPass             = get_boolean(rlayer, "use_pass_combined");
            passes->oct_node->bEmittersPass           = get_boolean(rlayer, "use_pass_emit");
            passes->oct_node->bEnvironmentPass        = get_boolean(rlayer, "use_pass_environment");
            passes->oct_node->bDiffuseDirectPass      = get_boolean(rlayer, "use_pass_diffuse_direct");
            passes->oct_node->bDiffuseIndirectPass    = get_boolean(rlayer, "use_pass_diffuse_indirect");

            bool cur_use = get_boolean(rlayer, "use_pass_reflection");
            int  subtype = RNA_enum_get(&oct_scene, "reflection_pass_subtype");
            passes->oct_node->bReflectionDirectPass   = cur_use && (subtype == 0);
            passes->oct_node->bReflectionIndirectPass = cur_use && (subtype == 1);
            passes->oct_node->bLayerReflectionsPass   = cur_use && (subtype == 1);

            passes->oct_node->bRefractionPass         = get_boolean(rlayer, "use_pass_refraction");
            passes->oct_node->bTransmissionPass       = get_boolean(rlayer, "use_pass_transmission_color");
            passes->oct_node->bSubsurfScatteringPass  = get_boolean(rlayer, "use_pass_subsurface_color");
            passes->oct_node->bPostProcessingPass     = false;

            cur_use = get_boolean(rlayer, "use_pass_normal");
            subtype = RNA_enum_get(&oct_scene, "normal_pass_subtype");
            passes->oct_node->bGeomNormalsPass    = cur_use && (subtype == 0);
            passes->oct_node->bShadingNormalsPass = cur_use && (subtype == 1);
            passes->oct_node->bVertexNormalsPass  = cur_use && (subtype == 2);

            passes->oct_node->bPositionPass       = false;
            passes->oct_node->bZdepthPass         = get_boolean(rlayer, "use_pass_z");
            passes->oct_node->bMaterialIdPass     = get_boolean(rlayer, "use_pass_material_index");
            passes->oct_node->bUVCoordinatesPass  = get_boolean(rlayer, "use_pass_uv");
            passes->oct_node->bTangentsPass       = false;
            passes->oct_node->bWireframePass      = false;
            passes->oct_node->bObjectIdPass       = get_boolean(rlayer, "use_pass_object_index");
            passes->oct_node->bAOPass             = get_boolean(rlayer, "use_pass_ambient_occlusion");
            passes->oct_node->bMotionVectorPass   = false;

            cur_use = get_boolean(rlayer, "use_pass_shadow");
            subtype = RNA_enum_get(&oct_scene, "shadows_pass_subtype");
            passes->oct_node->bLayerShadowsPass       = cur_use && (subtype == 0);
            passes->oct_node->bLayerBlackShadowsPass  = cur_use && (subtype == 1);
            passes->oct_node->bLayerColorShadowsPass  = cur_use && (subtype == 2);

            passes->oct_node->bLayerIdPass            = false;
            passes->oct_node->bLayerMaskPass          = false;
            passes->oct_node->bLightPassIdPass        = false;

            passes->oct_node->bAmbientLightPass       = false;
            passes->oct_node->bSunlightPass           = false;
            passes->oct_node->bLight1Pass             = false;
            passes->oct_node->bLight2Pass             = false;
            passes->oct_node->bLight3Pass             = false;
            passes->oct_node->bLight4Pass             = false;
            passes->oct_node->bLight5Pass             = false;
            passes->oct_node->bLight6Pass             = false;
            passes->oct_node->bLight7Pass             = false;
            passes->oct_node->bLight8Pass             = false;
        }
        else {
            passes->oct_node->bBeautyPass             = false;

            passes->oct_node->bEmittersPass           = false;
            passes->oct_node->bEnvironmentPass        = false;
            passes->oct_node->bDiffuseDirectPass      = false;
            passes->oct_node->bDiffuseIndirectPass    = false;
            passes->oct_node->bReflectionDirectPass   = false;
            passes->oct_node->bReflectionIndirectPass = false;
            passes->oct_node->bRefractionPass         = false;
            passes->oct_node->bTransmissionPass       = false;
            passes->oct_node->bSubsurfScatteringPass  = false;
            passes->oct_node->bPostProcessingPass     = false;

            passes->oct_node->bLayerShadowsPass       = false;
            passes->oct_node->bLayerBlackShadowsPass  = false;
            passes->oct_node->bLayerColorShadowsPass  = false;
            passes->oct_node->bLayerReflectionsPass   = false;

            passes->oct_node->bAmbientLightPass       = false;
            passes->oct_node->bSunlightPass           = false;
            passes->oct_node->bLight1Pass             = false;
            passes->oct_node->bLight2Pass             = false;
            passes->oct_node->bLight3Pass             = false;
            passes->oct_node->bLight4Pass             = false;
            passes->oct_node->bLight5Pass             = false;
            passes->oct_node->bLight6Pass             = false;
            passes->oct_node->bLight7Pass             = false;
            passes->oct_node->bLight8Pass             = false;

            passes->oct_node->bGeomNormalsPass        = false;
            passes->oct_node->bShadingNormalsPass     = false;
            passes->oct_node->bVertexNormalsPass      = false;
            passes->oct_node->bPositionPass           = false;
            passes->oct_node->bZdepthPass             = false;
            passes->oct_node->bMaterialIdPass         = false;
            passes->oct_node->bUVCoordinatesPass      = false;
            passes->oct_node->bTangentsPass           = false;
            passes->oct_node->bWireframePass          = false;
            passes->oct_node->bMotionVectorPass       = false;
            passes->oct_node->bObjectIdPass           = false;
            passes->oct_node->bLayerIdPass            = false;
            passes->oct_node->bLayerMaskPass          = false;
            passes->oct_node->bLightPassIdPass        = false;

            passes->oct_node->bAOPass                 = false;

            switch(passes->oct_node->curPassType) {
            case ::Octane::RenderPassId::RENDER_PASS_BEAUTY:
                passes->oct_node->bBeautyPass = true;
                break;

            case ::Octane::RenderPassId::RENDER_PASS_EMIT:
                passes->oct_node->bEmittersPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_ENVIRONMENT:
                passes->oct_node->bEnvironmentPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_DIRECT:
                passes->oct_node->bDiffuseDirectPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_DIFFUSE_INDIRECT:
                passes->oct_node->bDiffuseIndirectPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_DIRECT:
                passes->oct_node->bReflectionDirectPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_REFLECTION_INDIRECT:
                passes->oct_node->bReflectionIndirectPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_REFRACTION:
                passes->oct_node->bRefractionPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_TRANSMISSION:
                passes->oct_node->bTransmissionPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_SSS:
                passes->oct_node->bSubsurfScatteringPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_POST_PROC:
                passes->oct_node->bPostProcessingPass = true;
                break;

            case ::Octane::RenderPassId::RENDER_PASS_LAYER_SHADOWS:
                passes->oct_node->bLayerShadowsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LAYER_BLACK_SHADOWS:
                passes->oct_node->bLayerBlackShadowsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LAYER_COLOR_SHADOWS:
                passes->oct_node->bLayerColorShadowsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LAYER_REFLECTIONS:
                passes->oct_node->bLayerReflectionsPass = true;
                break;

            case ::Octane::RenderPassId::RENDER_PASS_AMBIENT_LIGHT:
                passes->oct_node->bAmbientLightPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_SUNLIGHT:
                passes->oct_node->bSunlightPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_1:
                passes->oct_node->bLight1Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_2:
                passes->oct_node->bLight2Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_3:
                passes->oct_node->bLight3Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_4:
                passes->oct_node->bLight4Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_5:
                passes->oct_node->bLight5Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_6:
                passes->oct_node->bLight6Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_7:
                passes->oct_node->bLight7Pass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_8:
                passes->oct_node->bLight8Pass = true;
                break;

            case ::Octane::RenderPassId::RENDER_PASS_GEOMETRIC_NORMAL:
                passes->oct_node->bGeomNormalsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_SHADING_NORMAL:
                passes->oct_node->bShadingNormalsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_VERTEX_NORMAL:
                passes->oct_node->bVertexNormalsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_POSITION:
                passes->oct_node->bPositionPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_Z_DEPTH:
                passes->oct_node->bZdepthPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_MATERIAL_ID:
                passes->oct_node->bMaterialIdPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_UV_COORD:
                passes->oct_node->bUVCoordinatesPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_TANGENT_U:
                passes->oct_node->bTangentsPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_WIREFRAME:
                passes->oct_node->bWireframePass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_OBJECT_ID:
                passes->oct_node->bObjectIdPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_MOTION_VECTOR:
                passes->oct_node->bMotionVectorPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_ID:
                passes->oct_node->bLayerIdPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_RENDER_LAYER_MASK:
                passes->oct_node->bLayerMaskPass = true;
                break;
            case ::Octane::RenderPassId::RENDER_PASS_LIGHT_PASS_ID:
                passes->oct_node->bLightPassIdPass = true;
                break;

            case ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION:
                passes->oct_node->bAOPass = true;
                break;

            default:
                passes->oct_node->bBeautyPass = true;
                break;
            }
        }
    } //if(passes->oct_node->use_passes)
    
    if(passes->modified(prevpasses)) passes->tag_update();
} //sync_passes()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get additional Octane scene settings.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_kernel() {
    PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");

    Kernel *kernel = scene->kernel;
    Kernel prevkernel = *kernel;

    BL::RenderSettings r = b_scene.render();
    if(r.use_motion_blur()) {
        float fps                                           = (float)b_scene.render().fps() / b_scene.render().fps_base();
        float shuttertime                                   = r.motion_blur_shutter();
        BlenderSession::MotionBlurType mb_type              = static_cast<BlenderSession::MotionBlurType>(RNA_enum_get(&oct_scene, "mb_type"));
        float mb_frame_time_sampling                        = mb_type == BlenderSession::INTERNAL ? 1.0f / fps : 0.0f;
        kernel->oct_node->fShutterTime                      = mb_frame_time_sampling != 0.0f ? shuttertime / mb_frame_time_sampling : 0.0f;
        BlenderSession::MotionBlurDirection mb_direction    = static_cast<BlenderSession::MotionBlurDirection>(RNA_enum_get(&oct_scene, "mb_direction"));
        switch(mb_direction) {
            case BlenderSession::BEFORE:
                kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::BEFORE;
                break;
            case BlenderSession::AFTER:
                kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::AFTER;
                break;
            case BlenderSession::SYMMETRIC:
                kernel->oct_node->mbAlignment = ::OctaneEngine::Kernel::SYMMETRIC;
                break;
            default:
                break;
        }
    }
    else kernel->oct_node->fShutterTime = 0.0f;

    kernel->oct_node->type = static_cast< ::OctaneEngine::Kernel::KernelType>(RNA_enum_get(&oct_scene, "kernel_type"));
    kernel->oct_node->infoChannelType = channel_translator[RNA_enum_get(&oct_scene, "info_channel_type")];

    ::Octane::RenderPassId cur_pass_type = Passes::pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];
    if(cur_pass_type == ::Octane::RenderPassId::RENDER_PASS_BEAUTY) {
        kernel->oct_node->iMaxSamples = interactive ? get_int(oct_scene, "max_preview_samples") : get_int(oct_scene, "max_samples");
        //kernel->oct_node->iMaxPreviewSamples = get_int(oct_scene, "max_preview_samples");
        //if(kernel->oct_node->iMaxPreviewSamples == 0) kernel->oct_node->iMaxPreviewSamples = 16000;
    }
    else if(cur_pass_type == ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION) {
        kernel->oct_node->iMaxSamples = get_int(oct_scene, "pass_ao_max_samples");
        //kernel->oct_node->iMaxPreviewSamples = kernel->oct_node->iMaxSamples;
    }
    else {
        kernel->oct_node->iMaxSamples = get_int(oct_scene, "pass_max_samples");
        //kernel->oct_node->iMaxPreviewSamples = kernel->oct_node->iMaxSamples;
    }
    if(scene->session->b_session && scene->session->b_session->motion_blur && scene->session->b_session->mb_type == BlenderSession::SUBFRAME && scene->session->b_session->mb_samples > 1)
        kernel->oct_node->iMaxSamples = kernel->oct_node->iMaxSamples / scene->session->b_session->mb_samples;
    if(kernel->oct_node->iMaxSamples < 1) kernel->oct_node->iMaxSamples = 1;

    kernel->oct_node->fFilterSize = get_float(oct_scene, "filter_size");
    kernel->oct_node->fRayEpsilon = get_float(oct_scene, "ray_epsilon");
    kernel->oct_node->bAlphaChannel = get_boolean(oct_scene, "alpha_channel");
    kernel->oct_node->bAlphaShadows = get_boolean(oct_scene, "alpha_shadows");
    kernel->oct_node->bBumpNormalMapping = get_boolean(oct_scene, "bump_normal_mapping");
    kernel->oct_node->bBkFaceHighlight = get_boolean(oct_scene, "wf_bkface_hl");
    kernel->oct_node->fPathTermPower = get_float(oct_scene, "path_term_power");

    kernel->oct_node->bKeepEnvironment = get_boolean(oct_scene, "keep_environment");

    kernel->oct_node->fCausticBlur = get_float(oct_scene, "caustic_blur");
    kernel->oct_node->iMaxDiffuseDepth = get_int(oct_scene, "max_diffuse_depth");
    kernel->oct_node->iMaxGlossyDepth = get_int(oct_scene, "max_glossy_depth");

    kernel->oct_node->fCoherentRatio = get_float(oct_scene, "coherent_ratio");
    kernel->oct_node->bStaticNoise = get_boolean(oct_scene, "static_noise");

    kernel->oct_node->iSpecularDepth = get_int(oct_scene, "specular_depth");
    kernel->oct_node->iGlossyDepth = get_int(oct_scene, "glossy_depth");
    kernel->oct_node->fAODist = get_float(oct_scene, "ao_dist");
    kernel->oct_node->GIMode = static_cast< ::OctaneEngine::Kernel::DirectLightMode>(RNA_enum_get(&oct_scene, "gi_mode"));
    kernel->oct_node->iDiffuseDepth = get_int(oct_scene, "diffuse_depth");

    kernel->oct_node->fExploration = get_float(oct_scene, "exploration");
    kernel->oct_node->fGIClamp = get_float(oct_scene, "gi_clamp");
    kernel->oct_node->fDLImportance = get_float(oct_scene, "direct_light_importance");
    kernel->oct_node->iMaxRejects = get_int(oct_scene, "max_rejects");
    kernel->oct_node->iParallelism = get_int(oct_scene, "parallelism");

    kernel->oct_node->fZdepthMax = get_float(oct_scene, "zdepth_max");
    kernel->oct_node->fUVMax = get_float(oct_scene, "uv_max");
    kernel->oct_node->bDistributedTracing = get_boolean(oct_scene, "distributed_tracing");
    kernel->oct_node->fMaxSpeed = get_float(oct_scene, "max_speed");

    kernel->oct_node->bLayersEnable = get_boolean(oct_scene, "layers_enable");
    kernel->oct_node->iLayersCurrent = get_int(oct_scene, "layers_current");
    kernel->oct_node->bLayersInvert = get_boolean(oct_scene, "layers_invert");

    kernel->oct_node->iParallelSamples = get_int(oct_scene, "parallel_samples");
    kernel->oct_node->iMaxTileSamples = get_int(oct_scene, "max_tile_samples");
    kernel->oct_node->bMinimizeNetTraffic = get_boolean(oct_scene, "minimize_net_traffic");
    kernel->oct_node->bDeepImageEnable = get_boolean(oct_scene, "deep_image");
    kernel->oct_node->iMaxDepthSamples = get_int(oct_scene, "max_depth_samples");
    kernel->oct_node->fDepthTolerance = get_float(oct_scene, "depth_tolerance");
    kernel->oct_node->iWorkChunkSize = get_int(oct_scene, "work_chunk_size");
    kernel->oct_node->bAoAlphaShadows = get_boolean(oct_scene, "ao_alpha_shadows");
    kernel->oct_node->fOpacityThreshold = get_float(oct_scene, "opacity_threshold");

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

	// Interactive
	params.interactive = interactive;

	// Samples
    ::Octane::RenderPassId cur_pass_type = Passes::pass_type_translator[RNA_enum_get(&oct_scene, "cur_pass_type")];
    if(cur_pass_type == ::Octane::RenderPassId::RENDER_PASS_BEAUTY) {
        if(!interactive) {
            params.samples = get_int(oct_scene, "max_samples");
        }
	    else {
		    params.samples = get_int(oct_scene, "max_preview_samples");
		    if(params.samples == 0) params.samples = 16000;
	    }
    }
    else if(cur_pass_type == ::Octane::RenderPassId::RENDER_PASS_AMBIENT_OCCLUSION) {
        params.samples = get_int(oct_scene, "pass_ao_max_samples");
    }
    else {
        params.samples = get_int(oct_scene, "pass_max_samples");
    }

    params.anim_mode            = static_cast<AnimationMode>(RNA_enum_get(&oct_scene, "anim_mode"));
    params.export_scene         = interactive ? ::OctaneEngine::OctaneClient::SceneExportTypes::NONE : static_cast< ::OctaneEngine::OctaneClient::SceneExportTypes::SceneExportTypesEnum>(get_enum(oct_scene, "export_scene"));

    params.deep_image           = get_boolean(oct_scene, "deep_image");
    params.use_passes           = get_boolean(oct_scene, "use_passes");
    params.meshes_type          = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_scene, "meshes_type"));
    if(params.export_scene != ::OctaneEngine::OctaneClient::SceneExportTypes::NONE && params.meshes_type == Mesh::GLOBAL)
        params.meshes_type = Mesh::RESHAPABLE_PROXY;
    params.use_viewport_hide    = get_boolean(oct_scene, "viewport_hide");
    params.hdr_tonemapped       = false;//get_boolean(oct_scene, "hdr_tonemapped");
	
    params.fps = (float)b_scene.render().fps() / b_scene.render().fps_base();

    params.out_of_core_enabled = get_boolean(oct_scene, "out_of_core_enable");
    params.out_of_core_mem_limit = get_int(oct_scene, "out_of_core_limit");
    params.out_of_core_gpu_headroom = get_int(oct_scene, "out_of_core_gpu_headroom");

	PointerRNA render_settings = RNA_pointer_get(&b_scene.ptr, "render");
    params.output_path = get_string(render_settings, "filepath");
    const char *cur_path = params.output_path.c_str();
    size_t len = params.output_path.length();
    if(len > 0 && cur_path[len - 1] != '/' && cur_path[len - 1] != '\\')
        params.output_path += "/";

	return params;
} //get_session_params()

OCT_NAMESPACE_END

