#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

import bpy

IS_RENDERING = False


def init():
    print("OctaneBlender Engine Init")        
    import os.path

    path = os.path.dirname(__file__)
    user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', path='')))

    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        _octane.init(path, user_path)    


def exit():
    print("OctaneBlender Engine Exit")            
    from octane import core
    from octane.core import resource_cache
    resource_cache.reset_resource_cache()
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        import _octane
        _octane.exit()


def create(engine, data, region=None, v3d=None, rv3d=None):
    print("OctaneBlender Engine Create")

    global IS_RENDERING
    IS_RENDERING = True

    from octane.utils import ocio    
    ocio.update_ocio_info()
    
    import bpy
    data = data.as_pointer()
    prefs = bpy.context.preferences.as_pointer()
    screen = 0

    from . import operators
    dirty_resources = operators.get_dirty_resources();

    if region:
        screen = region.id_data.as_pointer()
        region = region.as_pointer()
    if v3d:
        screen = screen or v3d.id_data.as_pointer()
        v3d = v3d.as_pointer()
    if rv3d:
        screen = screen or rv3d.id_data.as_pointer()
        rv3d = rv3d.as_pointer()

    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        engine.session = _octane.create(
                engine.as_pointer(), prefs, data, screen, region, v3d, rv3d, dirty_resources)


def free(engine):
    print("OctaneBlender Engine Free")
    if hasattr(engine, "session"):
        if engine.session:
            from octane import core
            if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:            
                import _octane
                _octane.free(engine.session)
        del engine.session    

    from . import operators
    try:
        operators.set_all_mesh_resource_cache_tags(False)
    except:
        pass

    global IS_RENDERING
    IS_RENDERING = False    


def render(engine, depsgraph):
    # print("OctaneBlender Engine Render")
    if engine.is_preview:
        return    
    scene = depsgraph.scene_eval
    register_render_aov_node_graph_passes(engine, scene)
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:    
        import _octane
        if hasattr(engine, "session"):
            _octane.render(engine.session, depsgraph.as_pointer())


def bake(engine, depsgraph, obj, pass_type, pass_filter, object_id, pixel_array, num_pixels, depth, result):
    # print("OctaneBlender Engine Bake")
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        session = getattr(engine, "session", None)
        import _octane        
        if session is not None:
            _octane.bake(engine.session, depsgraph.as_pointer(), obj.as_pointer(), pass_type, pass_filter, object_id, pixel_array.as_pointer(), num_pixels, depth, result.as_pointer())


def reset(engine, data, depsgraph):
    # print("OctaneBlender Engine Reset")    
    import bpy
    if engine.is_preview:
        return  
    data = data.as_pointer()
    depsgraph = depsgraph.as_pointer()
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        _octane.reset(engine.session, data, depsgraph)


def sync(engine, depsgraph, data):
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:    
        import _octane
        _octane.sync(engine.session, depsgraph.as_pointer())


def draw(engine, depsgraph, region, v3d, rv3d):
    # print("OctaneBlender Engine Draw")    
    depsgraph = depsgraph.as_pointer()
    v3d = v3d.as_pointer()
    rv3d = rv3d.as_pointer()
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        # draw render image
        _octane.draw(engine.session, depsgraph, v3d, rv3d)


PASS_DATA = {
    # Beauty Passes
    "use_pass_oct_beauty": "OctBeauty",
    "use_pass_oct_emitters": "OctEmitters",
    "use_pass_oct_env": "OctEnv",
    "use_pass_oct_diff": "OctDiff",
    "use_pass_oct_diff_dir": "OctDiffDir",
    "use_pass_oct_diff_indir": "OctDiffIndir",
    "use_pass_oct_diff_filter": "OctDiffFilter",
    "use_pass_oct_reflect": "OctReflect",
    "use_pass_oct_reflect_dir": "OctReflectDir",
    "use_pass_oct_reflect_indir": "OctReflectIndir",
    "use_pass_oct_reflect_filter": "OctReflectFilter",
    "use_pass_oct_refract": "OctRefract",
    "use_pass_oct_refract_filter": "OctRefractFilter",
    "use_pass_oct_transm": "OctTransm",
    "use_pass_oct_transm_filter": "OctTransmFilter",
    "use_pass_oct_sss": "OctSSS",
    "use_pass_oct_shadow": "OctShadow",
    "use_pass_oct_irradiance": "OctIrradiance",
    "use_pass_oct_light_dir": "OctLightDir",
    "use_pass_oct_volume": "OctVolume",
    "use_pass_oct_vol_mask": "OctVolMask",
    "use_pass_oct_vol_emission": "OctVolEmission",
    "use_pass_oct_vol_z_front": "OctVolZFront",
    "use_pass_oct_vol_z_back": "OctVolZBack",
    "use_pass_oct_noise": "OctNoise",
    # Denoise Passes
    "use_pass_oct_denoise_beauty": "OctDenoiserBeauty",
    "use_pass_oct_denoise_diff_dir": "OctDenoiserDiffDir",
    "use_pass_oct_denoise_diff_indir": "OctDenoiserDiffIndir",
    "use_pass_oct_denoise_reflect_dir": "OctDenoiserReflectDir",
    "use_pass_oct_denoise_reflect_indir": "OctDenoiserReflectIndir",
    "use_pass_oct_denoise_emission": "OctDenoiserEmission",
    "use_pass_oct_denoise_remainder": "OctDenoiserRemainder",
    "use_pass_oct_denoise_vol": "OctDenoiserVolume",
    "use_pass_oct_denoise_vol_emission": "OctDenoiserVolumeEmission",
    # Render Postprocess Passes
    "use_pass_oct_postprocess": "OctPostProcess",
    # Render Layer Passes
    "use_pass_oct_layer_shadows": "OctLayerShadows",
    "use_pass_oct_layer_black_shadow": "OctLayerBlackShadow",
    "use_pass_oct_layer_reflections": "OctLayerReflections",
    # Render Lighting Passesx
    "use_pass_oct_ambient_light": "OctAmbientLight",
    "use_pass_oct_ambient_light_dir": "OctAmbientLightDir",
    "use_pass_oct_ambient_light_indir": "OctAmbientLightIndir",
    "use_pass_oct_sunlight": "OctSunlight",
    "use_pass_oct_sunlight_dir": "OctSunLightDir",
    "use_pass_oct_sunlight_indir": "OctSunLightIndir",
    "use_pass_oct_light_pass_1": "OctLightPass1",
    "use_pass_oct_light_dir_pass_1": "OctLightDirPass1",
    "use_pass_oct_light_indir_pass_1": "OctLightIndirPass1",
    "use_pass_oct_light_pass_2": "OctLightPass2",
    "use_pass_oct_light_dir_pass_2": "OctLightDirPass2",
    "use_pass_oct_light_indir_pass_2": "OctLightIndirPass2",
    "use_pass_oct_light_pass_3": "OctLightPass3",
    "use_pass_oct_light_dir_pass_3": "OctLightDirPass3",
    "use_pass_oct_light_indir_pass_3": "OctLightIndirPass3",
    "use_pass_oct_light_pass_4": "OctLightPass4",
    "use_pass_oct_light_dir_pass_4": "OctLightDirPass4",
    "use_pass_oct_light_indir_pass_4": "OctLightIndirPass4",
    "use_pass_oct_light_pass_5": "OctLightPass5",
    "use_pass_oct_light_dir_pass_5": "OctLightDirPass5",
    "use_pass_oct_light_indir_pass_5": "OctLightIndirPass5",
    "use_pass_oct_light_pass_6": "OctLightPass6",
    "use_pass_oct_light_dir_pass_6": "OctLightDirPass6",
    "use_pass_oct_light_indir_pass_6": "OctLightIndirPass6",
    "use_pass_oct_light_pass_7": "OctLightPass7",
    "use_pass_oct_light_dir_pass_7": "OctLightDirPass7",
    "use_pass_oct_light_indir_pass_7": "OctLightIndirPass7",
    "use_pass_oct_light_pass_8": "OctLightPass8",
    "use_pass_oct_light_dir_pass_8": "OctLightDirPass8",
    "use_pass_oct_light_indir_pass_8": "OctLightIndirPass8",
    # Render Cryptomatte Passes
    "use_pass_oct_crypto_instance_id": "OctCryptoInstanceID",
    "use_pass_oct_crypto_mat_node_name": "OctCryptoMatNodeName",
    "use_pass_oct_crypto_mat_node": "OctCryptoMatNode",
    "use_pass_oct_crypto_mat_pin_node": "OctCryptoMatPinNode",
    "use_pass_oct_crypto_obj_node_name": "OctCryptoObjNodeName",
    "use_pass_oct_crypto_obj_node": "OctCryptoObjNode",
    "use_pass_oct_crypto_obj_pin_node": "OctCryptoObjPinNode",
    "use_pass_oct_crypto_render_layer": "CryptoRenderLayer",
    "use_pass_oct_crypto_geometry_node_name": "CryptoGeometryNodeName",
    "use_pass_oct_crypto_user_instance_id": "CryptoUserInstanceID",
    # Render Info Passes
    "use_pass_oct_info_geo_normal": "OctGeoNormal",
    "use_pass_oct_info_smooth_normal": "OctSmoothNormal",
    "use_pass_oct_info_shading_normal": "OctShadingNormal",
    "use_pass_oct_info_tangent_normal": "OctTangentNormal",
    "use_pass_oct_info_z_depth": "OctZDepth",
    "use_pass_oct_info_position": "OctPosition",
    "use_pass_oct_info_uv": "OctUV",
    "use_pass_oct_info_tex_tangent": "OctTexTangent",
    "use_pass_oct_info_motion_vector": "OctMotionVector",
    "use_pass_oct_info_mat_id": "OctMatID",
    "use_pass_oct_info_obj_id": "OctObjID",
    "use_pass_oct_info_obj_layer_color": "OctObjLayerColor",
    "use_pass_oct_info_baking_group_id": "OctBakingGroupID",
    "use_pass_oct_info_light_pass_id": "OctLightPassID",
    "use_pass_oct_info_render_layer_id": "OctRenderLayerID",
    "use_pass_oct_info_render_layer_mask": "OctRenderLayerMask",
    "use_pass_oct_info_wireframe": "OctWireframe",
    "use_pass_oct_info_ao": "OctAO",
    # Render Material Passes
    "use_pass_oct_mat_opacity": "OctOpacity",
    "use_pass_oct_mat_roughness": "OctRoughness",
    "use_pass_oct_mat_ior": "OctIOR",
    "use_pass_oct_mat_diff_filter_info": "OctDiffFilterInfo",
    "use_pass_oct_mat_reflect_filter_info": "OctReflectFilterInfo",
    "use_pass_oct_mat_refract_filter_info": "OctRefractFilterInfo",
    "use_pass_oct_mat_transm_filter_info": "OctTransmFilterInfo",
}

def octane_register_passes(engine, scene, srl):
    use_legacy_render_pass_mode = False
    for layer in scene.view_layers:
        if not layer.use:
            continue
        octane_view_layer = layer.octane
        if octane_view_layer.render_pass_style == "RENDER_PASSES":
            use_legacy_render_pass_mode = True
            break
    if use_legacy_render_pass_mode:
        engine.register_pass(scene, srl, "Combined", 4, "RGBA", 'COLOR')
        for attribute_name, pass_name in PASS_DATA.items():
            if getattr(srl, attribute_name, False):
                engine.register_pass(scene, srl, pass_name, 4, "RGBA", "COLOR")
    else:
        register_render_aov_node_graph_passes(engine, scene)


def register_render_aov_node_graph_passes(engine, scene):
    oct_scene = scene.octane
    oct_view_cam = scene.oct_view_cam
    oct_active_cam = scene.camera.data.octane
    enable_denoiser = False
    if oct_scene.use_preview_setting_for_camera_imager:
        enable_denoiser = oct_view_cam.imager.denoiser and oct_scene.hdr_tonemap_preview_enable
    else:
        enable_denoiser = oct_active_cam.imager.denoiser and oct_scene.hdr_tonemap_render_enable
    for layer in scene.view_layers:
        octane_view_layer = layer.octane
        if octane_view_layer.render_pass_style == "RENDER_PASSES":
            continue
        if layer.use:
            from octane.utils import utility
            utility.engine_add_layer_passes(scene, engine, layer, enable_denoiser)
