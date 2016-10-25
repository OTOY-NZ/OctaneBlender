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

        "octane.filter_size",
        "octane.ray_epsilon",
        "octane.alpha_channel",
        "octane.alpha_shadows",
        "octane.keep_environment",
        "octane.bump_normal_mapping",
        "octane.wf_bktrace_hl",
        "octane.path_term_power",
        "octane.caustic_blur",
        "octane.max_diffuse_depth",
        "octane.max_glossy_depth",
        "octane.coherent_ratio",
        "octane.static_noise",
        "octane.specular_depth",
        "octane.glossy_depth",
        "octane.ao_dist",
        "octane.gi_mode",
        "octane.diffuse_depth",
        "octane.exploration",
        "octane.gi_clamp",
        "octane.direct_light_importance",
        "octane.max_rejects",
        "octane.parallelism",
        "octane.zdepth_max",
        "octane.uv_max",
        "octane.distributed_tracing",
        "octane.max_speed",
        "octane.info_channel_type",

        "octane.parallel_samples",
        "octane.max_tile_samples",
        "octane.minimize_net_traffic",
        "octane.deep_image",
        "octane.max_depth_samples",
        "octane.depth_tolerance",
        "octane.work_chunk_size",
        "octane.ao_alpha_shadows",
        "octane.opacity_threshold"
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
        "octane.response_type",
        "octane.white_balance",

        "octane.exposure",
        "octane.gamma",
        "octane.vignetting",
        "octane.saturation",
        "octane.white_saturation",
        "octane.hot_pix",
        "octane.min_display_samples",
        "octane.dithering",
        "octane.premultiplied_alpha",
        "octane.neutral_response",
        "octane.max_tonemap_interval",
        "octane.disable_partial_alpha"
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
        "octane.response_type",
        "octane.white_balance",

        "octane.exposure",
        "octane.fstop",
        "octane.iso",
        "octane.gamma",
        "octane.vignetting",
        "octane.saturation",
        "octane.white_saturation",
        "octane.hot_pix",
        "octane.min_display_samples",
        "octane.dithering",
        "octane.premultiplied_alpha",
        "octane.neutral_response",
        "octane.max_tonemap_interval",
        "octane.disable_partial_alpha"
    ]

    preset_subdir = "octane/3dimager_presets"


def register():
    pass


def unregister():
    pass

if __name__ == "__main__":
    register()
