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
from bpy.props import (BoolProperty,
                       BoolVectorProperty,
                       EnumProperty,
                       FloatProperty,
                       IntProperty,
                       PointerProperty,
                       FloatVectorProperty,
                       StringProperty)
from bpy.types import (Texture,
                       Material)

import math

from . import types


class OctaneRenderSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.octane = PointerProperty(
                name="OctaneRender Settings",
                description="OctaneRender settings",
                type=cls,
                )

        cls.use_passes = BoolProperty(
                name="Render passes",
                description="",
                default=False,
                )
        cls.viewport_hide = BoolProperty(
                name="Viewport hide priority",
                description="Hide from final render objects hidden in viewport",
                default=False,
                )
        cls.export_alembic = BoolProperty(
                name="Export alembic",
                description="Export alembic file instead of rendering",
                default=False,
                )
        cls.meshes_type = EnumProperty(
                name="Render all meshes as",
                description="Override all meshes type by this type during rendering",
                items=types.meshes_render_types,
                default='4',
                )
        cls.anim_mode = EnumProperty(
                name="Animation mode",
                description="",
                items=types.anim_modes,
                default='0',
                )
        cls.devices = BoolVectorProperty(
                name="GPU",
                description="Devices to use for rendering",
                default=(True, False, False, False, False, False, False, False),
                size=8,
                )
        cls.server_address = StringProperty(
                name="Server address",
                description="Octane render-server address",
                default="127.0.0.1",
                maxlen=255,
                )
        cls.server_login = StringProperty(
                name="Login",
                description="Octane render-server login",
                default="",
                maxlen=128,
                )
        cls.server_pass = StringProperty(
                name="Password",
                description="Octane render-server password",
                default="",
                maxlen=128,
                )

        cls.kernel_type = EnumProperty(
                name="Kernel type",
                description="",
                items=types.kernel_types,
                default='1',
                )

        cls.max_samples = IntProperty(
                name="Max. samples",
                description="Number of samples to render for each pixel",
                min=1, max=64000,
                default=500,
                )
        cls.max_preview_samples = IntProperty(
                name="Max. preview samples",
                description="Number of samples to render for each pixel for preview",
                min=1, max=64000,
                default=100,
                )
        cls.filter_size = FloatProperty(
                name="Filter size",
                description="",
                min=1.0, soft_min=1.0, max=16.0, soft_max=16.0,
                default=1.2,
                step=10,
                precision=2,
                )
        cls.ray_epsilon = FloatProperty(
                name="Ray epsilon",
                description="",
                min=0.000001, soft_min=0.000001, max=0.1, soft_max=0.1,
                default=0.0001,
                step=10,
                precision=6,
                )
        cls.rrprob = FloatProperty(
                name="RRprob",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=4,
                )
        cls.alpha_channel = BoolProperty(
                name="Alpha channel",
                description="",
                default=False,
                )
        cls.keep_environment = BoolProperty(
                name="Keep environment",
                description="",
                default=False,
                )
        cls.alpha_shadows = BoolProperty(
                name="Alpha shadows",
                description="",
                default=True,
                )

        cls.max_depth = IntProperty(
                name="Max. depth",
                description="",
                min=1, max=2048,
                default=16,
                )
        cls.caustic_blur = FloatProperty(
                name="Caustic blur",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=3,
                )
        cls.parallelism = IntProperty(
                name="Parallelism",
                description="",
                min=1, max=4,
                default=4,
                )

        cls.specular_depth = IntProperty(
                name="Specular depth",
                description="",
                min=1, max=1024,
                default=5,
                )
        cls.glossy_depth = IntProperty(
                name="Glossy depth",
                description="",
                min=1, max=1024,
                default=2,
                )
        cls.ao_dist = FloatProperty(
                name="AOdist",
                description="",
                min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
                default=3.0,
                step=1,
                precision=2,
                )
        cls.gi_mode = EnumProperty(
                name="GImode",
                description="",
                items=types.gi_modes,
                default='3',
                )
        cls.diffuse_depth = IntProperty(
                name="Diffuse depth",
                description="",
                min=1, max=8,
                default=2,
                )

        cls.exploration = FloatProperty(
                name="Exploration",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.7,
                step=10,
                precision=2,
                )
        cls.direct_light_importance = FloatProperty(
                name="Direct light imp.",
                description="",
                min=0.01, soft_min=0.01, max=1.0, soft_max=1.0,
                default=0.1,
                step=1,
                precision=2,
                )
        cls.max_rejects = IntProperty(
                name="Max. rejects",
                description="",
                min=100, max=10000,
                default=500,
                )

        cls.info_channel_type = EnumProperty(
                name="Info-channel type",
                description="",
                items=types.info_channel_types,
                default='0',
                )
        cls.zdepth_max = FloatProperty(
                name="Z-Depth max.",
                description="",
                min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
                default=5.0,
                step=100,
                precision=3,
                )
        cls.uv_max = FloatProperty(
                name="UV max.",
                description="",
                min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=1,
                precision=5,
                )

        cls.bump_normal_mapping = BoolProperty(
                name="Bump and normal mapping",
                description="",
                default=False,
                )
        cls.wf_bktrace_hl = BoolProperty(
                name="Wireframe backtrace highlighting",
                description="",
                default=False,
                )

        cls.progressive = BoolProperty(
                name="Progressive",
                description="Use progressive sampling of lighting",
                default=True,
                )

        cls.preview_pause = BoolProperty(
                name="Pause Preview",
                description="Pause viewport preview",
                default=False,
                )
        cls.preview_active_layer = BoolProperty(
                name="Preview Active Layer",
                description="Preview active render layer in viewport",
                default=False,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.octane


class OctaneCameraSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Camera.octane = PointerProperty(
                name="OctaneRender Camera Settings",
                description="OctaneRender camera settings",
                type=cls,
                options={'HIDDEN'},
                )

        cls.pan_mode = EnumProperty(
                name="Pan mode",
#                description="",
                items=types.camera_pan_modes,
                default='SPHERE',
                )
        cls.fov_x = FloatProperty(
                name="FOV X",
#                description="",
                min=1.0, soft_min=1.0, max=360.0, soft_max=360.0,
                default=360.0,
                step=10,
                precision=3,
                )
        cls.fov_y = FloatProperty(
                name="FOV Y",
#                description="",
                min=1.0, soft_min=1.0, max=180.0, soft_max=180.0,
                default=360.0,
                step=10,
                precision=3,
                )
        cls.stereo = BoolProperty(
                name="Stereo",
#                description="",
                default=False,
                )
        cls.stereo_dist = FloatProperty(
                name="Stereo distance",
#                description="",
                min=0.001, soft_min=0.001, max=2.0, soft_max=2.0,
                default=0.02,
                step=10,
                precision=3,
                )
        cls.left_filter = FloatVectorProperty(
                name="Left filter",
#                description="",
                min=0.0, max=1.0,
                default=(1.0, 0.0, 0.812),
                subtype='COLOR',
                )
        cls.right_filter = FloatVectorProperty(
                name="Right filter",
#                description="",
                min=0.0, max=1.0,
                default=(0.0, 1.0, 0.188),
                subtype='COLOR',
                )
        cls.aperture = FloatProperty(
                name="Aperture",
                description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
                min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.aperture_edge = FloatProperty(
                name="Aperture edge",
#                description="Aperture edge",
                min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.distortion = FloatProperty(
                name="Distortion",
#                description="Distortion",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.autofocus = BoolProperty(
                name="Autofocus",
#                description="",
                default=False,
                )

        cls.white_balance = FloatVectorProperty(
                name="White balance",
#                description="",
                min=0.0, max=1.0,
                default=(1.0, 1.0, 1.0),
                subtype='COLOR',
                )
        cls.response_type = EnumProperty(
                name="Response type",
#                description="",
                items=types.response_types,
                default='105',
                )
        cls.exposure = FloatProperty(
                name="Exposure",
                description="",
                min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.fstop = FloatProperty(
                name="F-Stop",
                description="",
                min=1.0, soft_min=1.0, max=64.0, soft_max=64.0,
                default=2.8,
                step=10,
                precision=1,
                )
        cls.iso = FloatProperty(
                name="ISO",
                description="",
                min=1.0, soft_min=1.0, max=800.0, soft_max=800.0,
                default=100.0,
                step=100,
                precision=1,
                )
        cls.gamma = FloatProperty(
                name="Gamma",
                description="",
                min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.vignetting = FloatProperty(
                name="Vignetting",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.3,
                step=1,
                precision=2,
                )
        cls.saturation = FloatProperty(
                name="Saturation",
                description="",
                min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.hot_pix = FloatProperty(
                name="hot_pix",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.premultiplied_alpha = BoolProperty(
                name="Premultiplied alpha",
#                description="",
                default=False,
                )
        cls.min_display_samples = IntProperty(
                name="Min. display samples",
                description="",
                min=1, max=32,
                default=1,
                )
        cls.dithering = BoolProperty(
                name="Dithering",
#                description="",
                default=False,
                )
        cls.white_saturation = FloatProperty(
                name="White saturation",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )

        cls.postprocess = BoolProperty(
                name="Postprocess",
#                description="",
                default=False,
                )
        cls.bloom_power = FloatProperty(
                name="Bloom power",
                description="",
                min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
                default=1.0,
                step=1,
                precision=3,
                )
        cls.glare_power = FloatProperty(
                name="Glare power",
                description="",
                min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
                default=0.01,
                step=1,
                precision=3,
                )
        cls.glare_ray_count = IntProperty(
                name="Glare ray count",
                description="",
                min=1, max=8,
                default=3,
                )
        cls.glare_angle = FloatProperty(
                name="Glare angle",
                description="",
                min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
                default=15.0,
                step=10,
                precision=1,
                )
        cls.glare_blur = FloatProperty(
                name="Glare blur",
                description="",
                min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
                default=0.001,
                step=0.1,
                precision=3,
                )
        cls.spectral_intencity = FloatProperty(
                name="Spectral intencity",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.spectral_shift = FloatProperty(
                name="Spectral shift",
                description="",
                min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
                default=2.0,
                step=100,
                precision=3,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Camera.octane


class OctaneSpaceDataSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.oct_view_cam = PointerProperty(
                name="OctaneRender Camera Settings",
                description="OctaneRender camera settings",
                type=cls,
                options={'HIDDEN'},
                )

        cls.aperture = FloatProperty(
                name="Aperture",
                description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
                min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.aperture_edge = FloatProperty(
                name="Aperture edge",
#                description="Aperture edge",
                min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.distortion = FloatProperty(
                name="Distortion",
#                description="Distortion",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=2,
                )

        cls.white_balance = FloatVectorProperty(
                name="White balance",
#                description="",
                min=0.0, max=1.0,
                default=(1.0, 1.0, 1.0),
                subtype='COLOR',
                )
        cls.response_type = EnumProperty(
                name="Response type",
#                description="",
                items=types.response_types,
                default='105',
                )
        cls.exposure = FloatProperty(
                name="Exposure",
                description="",
                min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.fstop = FloatProperty(
                name="F-Stop",
                description="",
                min=1.0, soft_min=1.0, max=64.0, soft_max=64.0,
                default=2.8,
                step=10,
                precision=1,
                )
        cls.iso = FloatProperty(
                name="ISO",
                description="",
                min=1.0, soft_min=1.0, max=800.0, soft_max=800.0,
                default=100.0,
                step=100,
                precision=1,
                )
        cls.gamma = FloatProperty(
                name="Gamma",
                description="",
                min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.vignetting = FloatProperty(
                name="Vignetting",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.3,
                step=1,
                precision=2,
                )
        cls.saturation = FloatProperty(
                name="Saturation",
                description="",
                min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.hot_pix = FloatProperty(
                name="hot_pix",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.premultiplied_alpha = BoolProperty(
                name="Premultiplied alpha",
#                description="",
                default=False,
                )
        cls.min_display_samples = IntProperty(
                name="Min. display samples",
                description="",
                min=1, max=32,
                default=1,
                )
        cls.dithering = BoolProperty(
                name="Dithering",
#                description="",
                default=False,
                )
        cls.white_saturation = FloatProperty(
                name="White saturation",
                description="",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.oct_view_cam


class OctaneMaterialSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Material.octane = PointerProperty(
                name="OctaneRender Material Settings",
                description="OctaneRender material settings",
                type=cls,
                )
        cls.homogeneous_volume = BoolProperty(
                name="Homogeneous Volume",
                description="When using volume rendering, assume volume has the same density everywhere, for faster rendering",
                default=False,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Material.octane


class OctaneLampSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Lamp.octane = PointerProperty(
                name="OctaneRender Lamp Settings",
                description="OctaneRender lamp settings",
                type=cls,
                )
        cls.enable = BoolProperty(
                name="Enable",
                description="Lamp casts shadows",
                default=True,
                )
        cls.mesh_type = EnumProperty(
                name="Mesh type",
                description="",
                items=types.mesh_types,
                default='0',
                )
#        cls.power = FloatProperty(
#                name="Power",
#                description="Octane lamp power",
#                min=0.001, soft_min=0.001, max=1000.0, soft_max=1000.0,
#                default=1.0,
#                step=10,
#                precision=3,
#                )

    @classmethod
    def unregister(cls):
        del bpy.types.Lamp.octane


class OctaneWorldSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.World.octane = PointerProperty(
                name="OctaneRender World Settings",
                description="OctaneRender world settings",
                type=cls,
                )
        cls.env_type = EnumProperty(
                name="Environment type",
                description="",
                items=types.environment_types,
                default='1',
                )
        cls.env_texture = StringProperty(
                name="Texture",
                description="Octane environment texture",
                default="",
                maxlen=512,
                )
        cls.env_power = FloatProperty(
                name="Power",
                description="Octane environment power",
                min=0.001, soft_min=0.001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.env_importance_sampling = BoolProperty(
                name="Octane importance sampling",
                description="",
                default=True,
                )
        cls.env_daylight_type = EnumProperty(
                name="Daylight type",
                description="Octane daylight type",
                items=types.environment_daylight_types,
                default='1',
                )
        cls.env_sundir_x = FloatProperty(
                name="Sun direction X",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.env_sundir_y = FloatProperty(
                name="Sun direction Y",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.env_sundir_z = FloatProperty(
                name="Sun direction Z",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=-0.0,
                step=10,
                precision=3,
                )
        cls.env_turbidity = FloatProperty(
                name="Turbidity",
                description="Octane environment turbidity",
                min=2.0, soft_min=2.0, max=6.0, soft_max=6.0,
                default=2.2,
                step=10,
                precision=3,
                )
        cls.env_northoffset = FloatProperty(
                name="North offset",
                description="Octane environment north offset",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.env_model = EnumProperty(
                name="Model",
                description="Octane daylight model",
                items=types.environment_daylight_models,
                default='1',
                )
        cls.env_sky_color = FloatVectorProperty(
                name="Sky color",
                description="Octane sky color",
                min=0.0, max=1.0,
                default=(0.05, 0.3, 1.0),
                subtype='COLOR',
                )
        cls.env_sunset_color = FloatVectorProperty(
                name="Sunset color",
                description="Octane sunset color",
                min=0.0, max=1.0,
                default=(0.6, 0.12, 0.02),
                subtype='COLOR',
                )
        cls.env_sun_size = FloatProperty(
                name="Sun size",
                description="Octane sun size",
                min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
                default=1.0,
                step=10,
                precision=4,
                )
        cls.env_longitude = FloatProperty(
                name="Longitude",
                description="Octane environment longitude",
                min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
                default=4.4667,
                step=1,
                precision=4,
                )
        cls.env_latitude = FloatProperty(
                name="Latitude",
                description="Octane environment latitude",
                min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
                default=50.7667,
                step=1,
                precision=4,
                )
        cls.env_day = IntProperty(
                name="Day",
                description="",
                min=1, max=31,
                default=1,
                )
        cls.env_month = IntProperty(
                name="Month",
                description="",
                min=1, max=12,
                default=3,
                )
        cls.env_gmtoffset = IntProperty(
                name="GMT offset",
                description="",
                min=-12, max=12,
                default=0,
                )
        cls.env_hour = FloatProperty(
                name="Longitude",
                description="Octane environment longitude",
                min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
                default=14,
                step=100,
                precision=1,
                )


    @classmethod
    def unregister(cls):
        del bpy.types.World.octane


class OctaneObjPropertiesSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Object.octane_properties = PointerProperty(
                name="OctaneRender Object Properties",
                description="OctaneRender object properties",
                type=cls,
                )

        cls.visibility = BoolProperty(
                name="Visibility",
                description="Object visibility for OctaneRender",
                default=True,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane_properties


class OctaneMeshSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Mesh.octane = PointerProperty(
                name="OctaneRender Mesh Settings",
                description="OctaneRender mesh settings",
                type=cls,
                )
        bpy.types.Curve.octane = PointerProperty(
                name="OctaneRender Curve Settings",
                description="OctaneRender mesh settings",
                type=cls,
                )
        bpy.types.MetaBall.octane = PointerProperty(
                name="OctaneRender MetaBall Settings",
                description="OctaneRender mesh settings",
                type=cls,
                )

        cls.mesh_type = EnumProperty(
                name="Mesh type",
                description="",
                items=types.mesh_types,
                default='0',
                )
        cls.use_subdivision = BoolProperty(
                name="Use Subdivision",
                description="Subdivide mesh for rendering",
                default=False,
                )
        cls.subdiv_divider = FloatProperty(
                name="Divider",
                description="",
                min=1.000, max=1000.0, soft_max=10.0,
                default=1.0,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Mesh.octane
        del bpy.types.Curve.octane
        del bpy.types.MetaBall.octane


def register():
    bpy.utils.register_class(OctaneRenderSettings)
    bpy.utils.register_class(OctaneCameraSettings)
    bpy.utils.register_class(OctaneSpaceDataSettings)
    bpy.utils.register_class(OctaneMaterialSettings)
    bpy.utils.register_class(OctaneLampSettings)
    bpy.utils.register_class(OctaneWorldSettings)
    bpy.utils.register_class(OctaneObjPropertiesSettings)
    bpy.utils.register_class(OctaneMeshSettings)


def unregister():
    bpy.utils.unregister_class(OctaneRenderSettings)
    bpy.utils.unregister_class(OctaneCameraSettings)
    bpy.utils.unregister_class(OctaneSpaceDataSettings)
    bpy.utils.unregister_class(OctaneMaterialSettings)
    bpy.utils.unregister_class(OctaneLampSettings)
    bpy.utils.unregister_class(OctaneWorldSettings)
    bpy.utils.unregister_class(OctaneMeshSettings)
    bpy.utils.unregister_class(OctaneObjPropertiesSettings)
