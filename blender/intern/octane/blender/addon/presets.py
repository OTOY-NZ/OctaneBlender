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

from bl_operators.presets import AddPresetBase
from bpy.types import Operator


class AddPresetKernel(AddPresetBase, Operator):
    '''Add Octane kernel preset'''
    bl_idname = "render.octane_kernel_preset_add"
    bl_label = "Add kernel preset"
    preset_menu = "OCTANE_MT_kernel_presets"

    preset_defines = [
        "octane = bpy.context.scene.octane"
    ]

    preset_values = [
        "octane.devices",
        "octane.kernel_type",

        "octane.max_samples",
        "octane.max_preview_samples",

        "octane.gi_mode",
        "octane.clay_mode",
        "octane.ao_texture",
        "octane.info_channel_type",
        "octane.parallel_samples",
        "octane.max_tile_samples",
        "octane.zdepth_max",
        "octane.uv_max",
        "octane.max_speed",
        "octane.opacity_threshold",
        "octane.sampling_mode",
        "octane.max_diffuse_depth",
        "octane.max_glossy_depth",
        "octane.max_scatter_depth",
        "octane.caustic_blur",
        "octane.gi_clamp",
        "octane.alpha_channel",
        "octane.wf_bkface_hl",
        "octane.ao_alpha_shadows",
        "octane.minimize_net_traffic",
        "octane.emulate_old_volume_behavior",
        "octane.specular_depth",
        "octane.glossy_depth",
        "octane.diffuse_depth",
        "octane.ao_dist",
        "octane.filter_size",
        "octane.ray_epsilon",
        "octane.exploration",
        "octane.direct_light_importance",
        "octane.max_rejects",
        "octane.parallelism",
        "octane.work_chunk_size",
        "octane.coherent_ratio",
        "octane.max_depth_samples",
        "octane.depth_tolerance",
        "octane.static_noise",
        "octane.deep_image",
        "octane.path_term_power",
        "octane.keep_environment",
        "octane.irradiance_mode",
        "octane.ai_light_enable",
        "octane.ai_light_update",
        "octane.ai_light_strength",
        "octane.alpha_shadows",
        "octane.bump_normal_mapping",
    ]

    preset_subdir = "octane/kernel"

class AddPresetEnvironment(AddPresetBase, Operator):
    '''Add Octane environment preset'''
    bl_idname = "render.octane_environment_preset_add"
    bl_label = "Add environment preset"
    preset_menu = "OCTANE_MT_environment_presets"

    preset_defines = [
        "octane = bpy.context.world.octane"
    ]

    preset_values = [
        "octane.env_type",
        "octane.env_texture",
        "octane.env_power",
        "octane.env_importance_sampling",
        "octane.env_daylight_type",
        "octane.env_sundir_x",
        "octane.env_sundir_y",
        "octane.env_sundir_z",
        "octane.env_turbidity",
        "octane.env_northoffset",
        "octane.env_model",
        "octane.env_sky_color",
        "octane.env_sunset_color",
        "octane.env_sun_size",
        "octane.env_longitude",
        "octane.env_latitude",
        "octane.env_day",
        "octane.env_month",
        "octane.env_gmtoffset",
        "octane.env_hour",
        "octane.env_med_radius",
        "octane.env_medium",
    ]

    preset_subdir = "octane/environment"

class AddPresetVisEnvironment(AddPresetBase, Operator):
    '''Add Octane visible environment preset'''
    bl_idname = "render.octane_vis_environment_preset_add"
    bl_label = "Add visible environment preset"
    preset_menu = "OCTANE_MT_vis_environment_presets"

    preset_defines = [
        "octane = bpy.context.world.octane"
    ]

    preset_values = [
        "octane.env_vis_type",
        "octane.env_vis_texture",
        "octane.env_vis_power",
        "octane.env_vis_importance_sampling",
        "octane.env_vis_daylight_type",
        "octane.env_vis_sundir_x",
        "octane.env_vis_sundir_y",
        "octane.env_vis_sundir_z",
        "octane.env_vis_turbidity",
        "octane.env_vis_northoffset",
        "octane.env_vis_model",
        "octane.env_vis_sky_color",
        "octane.env_vis_sunset_color",
        "octane.env_vis_sun_size",
        "octane.env_vis_longitude",
        "octane.env_vis_latitude",
        "octane.env_vis_day",
        "octane.env_vis_month",
        "octane.env_vis_gmtoffset",
        "octane.env_vis_hour",
        "octane.env_vis_med_radius",
        "octane.env_vis_medium",
        "octane.env_vis_backplate",
        "octane.env_vis_reflections",
        "octane.env_vis_refractions"
    ]

    preset_subdir = "octane/vis_environment"

class AddPresetImager(AddPresetBase, Operator):
    '''Add Octane Imager preset'''
    bl_idname = "render.octane_imager_preset_add"
    bl_label = "Add imager preset"
    preset_menu = "OCTANE_MT_imager_presets"

    preset_defines = [
        "octane = bpy.context.camera.octane"
    ]

    preset_values = [
        "octane.camera_imager_order",
        "octane.response_type",
        "octane.white_balance",
        "octane.exposure",
        "octane.gamma",
        "octane.vignetting",
        "octane.saturation",
        "octane.white_saturation",
        "octane.hot_pix",
        "octane.min_display_samples",
        "octane.highlight_compression",
        "octane.max_tonemap_interval",
        "octane.dithering",
        "octane.premultiplied_alpha",
        "octane.neutral_response",        
        "octane.disable_partial_alpha",
        "octane.custom_lut",
        "octane.lut_strength"
    ]

    preset_subdir = "octane/imager_presets"

class AddPreset3dImager(AddPresetBase, Operator):
    '''Add Octane Imager preset for 3D-view'''
    bl_idname = "render.octane_3dimager_preset_add"
    bl_label = "Add imager preset for 3D-view"
    preset_menu = "OCTANE_MT_3dimager_presets"

    preset_defines = [
        "octane = bpy.context.scene.oct_view_cam"
    ]

    preset_values = [
        "octane.camera_imager_order",
        "octane.response_type",
        "octane.white_balance",
        "octane.exposure",        
        "octane.gamma",
        "octane.vignetting",
        "octane.saturation",
        "octane.white_saturation",
        "octane.hot_pix",
        "octane.min_display_samples",
        "octane.highlight_compression",
        "octane.max_tonemap_interval",
        "octane.dithering",
        "octane.premultiplied_alpha",
        "octane.neutral_response",        
        "octane.disable_partial_alpha"
        "octane.custom_lut",
        "octane.lut_strength"        
    ]

    preset_subdir = "octane/3dimager_presets"


classes = (
    AddPresetKernel,
    AddPresetEnvironment,
    AddPresetVisEnvironment,
    AddPresetImager,
    AddPreset3dImager,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
