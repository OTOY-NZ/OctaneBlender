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
        "octane.filter_size",
        "octane.ray_epsilon",
        "octane.max_depth",
        "octane.caustic_blur",
        "octane.specular_depth",
        "octane.glossy_depth",
        "octane.ao_dist",
        "octane.gi_mode",
        "octane.diffuse_depth",
        "octane.exploration",
        "octane.direct_light_importance",
        "octane.max_rejects",
        "octane.info_channel_type",
        "octane.zdepth_max",
        "octane.uv_max"
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
        "octane.env_rotation_x",
        "octane.env_rotation_y",
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
        "octane.env_hour"
    ]

    preset_subdir = "octane/environment"


def register():
    pass


def unregister():
    pass

if __name__ == "__main__":
    register()
