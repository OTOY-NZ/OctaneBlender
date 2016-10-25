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
                description="",
                type=cls,
                )
# ################################################################################################
# OCTANE RENDER PASSES
# ################################################################################################
        cls.use_passes = BoolProperty(
                name="Render passes",
                description="",
                default=False,
                )

        cls.reflection_pass_subtype = EnumProperty(
                name="Subtype",
                description="",
                items=types.pass_refl_subtype,
                default='0',
                )
        cls.normal_pass_subtype = EnumProperty(
                name="Subtype",
                description="",
                items=types.pass_normal_subtype,
                default='0',
                )
        cls.shadows_pass_subtype = EnumProperty(
                name="Subtype",
                description="",
                items=types.pass_shadows_subtype,
                default='0',
                )

        cls.pass_max_samples = IntProperty(
                name="Max samples",
                description="The maximum number of samples for the info passes (excluding AO)",
                min=1, max=1024,
                default=128,
                )
        cls.pass_distributed_tracing = BoolProperty(
                name="Distributed ray tracing",
                description="Enable motion blur and depth of field",
                default=False,
                )
        cls.pass_z_depth_max = FloatProperty(
                name="Z-depth max",
                description="Z-depth value mapped to white (0 is mapped to black)",
                min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
                default=5.0,
                step=10,
                precision=4,
                )
        cls.pass_uv_max = FloatProperty(
                name="UV max",
                description="UV coordinate value mapped to maximum intensity",
                min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=10,
                precision=5,
                )
        cls.pass_max_speed = FloatProperty(
                name="Max speed",
                description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
                min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
                default=1.0,
                step=10,
                precision=5,
                )
        cls.pass_ao_distance = FloatProperty(
                name="AO distance",
                description="Ambient occlusion distance",
                min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
                default=3.0,
                step=10,
                precision=2,
                )
        cls.pass_alpha_shadows = BoolProperty(
                name="AO alpha shadows",
                description="Take into account alpha maps when calculating ambient occlusion",
                default=False,
                )
        cls.pass_raw = BoolProperty(
                name="Raw",
                description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray",
                default=False,
                )
        cls.pass_pp_env = BoolProperty(
                name="Include environment",
                description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled",
                default=False,
                )
        cls.pass_bump = BoolProperty(
                name="Bump and normal mapping",
                description="Take bump and normal mapping into account for shading normal output and wireframe shading",
                default=True,
                )
        cls.pass_opacity_threshold = FloatProperty(
                name="Opacity threshold",
                description="Geometry with opacity higher or equal to this value is treated as totally opaque",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=10,
                precision=3,
                )

        cls.cur_pass_type = EnumProperty(
                name="Preview pass type",
                description="Pass used for preview rendering",
                items=types.pass_types,
                default='0',
                )


# ################################################################################################
# OCTANE LAYERS
# ################################################################################################
        cls.layers_enable = BoolProperty(
                name="Enable",
                description="Tick to enable Octane render layers",
                default=False,
                )
        cls.layers_current = IntProperty(
                name="Active layer ID",
                description="ID of the active render layer",
                min=1, max=100,
                default=1,
                )
        cls.layers_invert = BoolProperty(
                name="Invert",
                description="All the non-active render layers become the active render layer and the active render layer becomes inactive",
                default=False,
                )
        cls.layers_mode = EnumProperty(
                name="Mode",
                description="The render mode that should be used to render layers:\n"
                    "\n"
                    "'Normal':"
                    " The beauty passes contain the active layer only and the render layer passes (shadows,"
                    " reflections...) record the side-effects of the active render layer for those samples/pixels"
                    " that are not obstructed by the active render layer.\n"
                    "Beauty passes will be transparent for those pixels which are covered by objects on the"
                    " inactive layers, even if there is an object on the active layer behind the foreground"
                    " object.\n"
                    "\n"
                    "'Hide inactive layers':"
                    " All geometry that is not on an active layer will be made invisible. No side effects"
                    " will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n"
                    "\n"
                    "'Only side effects':"
                    " Similar to 'normal', with the exception that the active layer will be made invisible"
                    " to the camera, i.e. the beauty passes will be empty. The render layer passes"
                    " (shadows, reflections...) still record the side-effects of the active render layer.\n"
                    "This is useful to capture all side-effects without having the active layer obstructing"
                    " those",
                items=types.layer_modes,
                default='0',
                )


# ################################################################################################
# OCTANE OUT OF CORE
# ################################################################################################
        cls.out_of_core_enable = BoolProperty(
                name="Enable out of core",
                description="Tick to enable Octane out of core",
                default=False,
                )
        cls.out_of_core_limit = IntProperty(
                name="Out of core memory limit (MB)",
                description="Maximal amount of memory to be used for out-of-core textures",
                min=1,
                default=4096,
                )
        cls.out_of_core_gpu_headroom = IntProperty(
                name="GPU headroom (MB)",
                description="To run the render kernels successfully, there needs to be some amount of free GPU memory. This setting determines how much GPU memory the render engine will leave available when uploading the images. The default value should work for most scenes",
                min=1,
                default=300,
                )


# ################################################################################################
# OCTANE COMMON
# ################################################################################################
        cls.viewport_hide = BoolProperty(
                name="Viewport hide priority",
                description="Hide from final render objects hidden in viewport",
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
                description="Optimize animation rendering speed (use in conjunction with Octane mesh types, see the manual)",
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
        cls.stand_login = StringProperty(
                name="Stand",
                description="Octane standalone login",
                default="",
                maxlen=128,
                )
        cls.stand_pass = StringProperty(
                name="",
                description="Octane standalone password",
                default="",
                maxlen=128,
                )
        cls.server_login = StringProperty(
                name="Plugin",
                description="Octane render-server login",
                default="",
                maxlen=128,
                )
        cls.server_pass = StringProperty(
                name="",
                description="Octane render-server password",
                default="",
                maxlen=128,
                )

        cls.mb_type = EnumProperty(
                name="Motion blur type",
                description="",
                items=types.mb_types,
                default='1',
                )
        cls.mb_direction = EnumProperty(
                name="Motion blur direction",
                description="",
                items=types.mb_directions,
                default='0',
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
                description="Film splatting width (to reduce aliasing)",
                min=1.0, soft_min=1.0, max=16.0, soft_max=16.0,
                default=1.2,
                step=10,
                precision=2,
                )
        cls.ray_epsilon = FloatProperty(
                name="Ray epsilon",
                description="Shadow ray offset distance to avoid self-intersection",
                min=0.000001, soft_min=0.000001, max=0.1, soft_max=0.1,
                default=0.0001,
                step=10,
                precision=6,
                )
        cls.alpha_channel = BoolProperty(
                name="Alpha channel",
                description="Enables a compositing alpha channel",
                default=False,
                )
        cls.alpha_shadows = BoolProperty(
                name="Alpha shadows",
                description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled",
                default=True,
                )
        cls.keep_environment = BoolProperty(
                name="Keep environment",
                description="Keeps environment with enabled alpha channel",
                default=False,
                )

        cls.caustic_blur = FloatProperty(
                name="Caustic blur",
                description="Caustic blur for noise reduction",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=3,
                )
        cls.parallelism = IntProperty(
                name="Parallelism",
                description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed",
                min=1, max=4,
                default=4,
                )

        cls.specular_depth = IntProperty(
                name="Specular depth",
                description="The maximum path depth for which specular reflections/refractions are allowed",
                min=1, max=1024,
                default=5,
                )
        cls.glossy_depth = IntProperty(
                name="Glossy depth",
                description="The maximum path depth for which glossy reflections are allowed",
                min=1, max=1024,
                default=2,
                )
        cls.ao_dist = FloatProperty(
                name="AOdist",
                description="Maximum distance for environment ambient occlusion",
                min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
                default=3.0,
                step=1,
                precision=2,
                )
        cls.ao_texture = StringProperty(
                name="AO ambient texture",
                description="Ambient occlusion environment texture, which is used for AO rays. If not specified, the environment will be used instead",
                default="",
                maxlen=512,
                )
        cls.gi_mode = EnumProperty(
                name="GImode",
                description="Determines how global illumination is approximated",
                items=types.gi_modes,
                default='3',
                )
        cls.gi_clamp = FloatProperty(
                name="GI clamp",
                description="GI clamp reducing fireflies",
                min=0.001, soft_min=0.001, max=1000000.0, soft_max=1000000.0,
                default=1000000.0,
                step=1,
                precision=3,
                )
        cls.diffuse_depth = IntProperty(
                name="Diffuse depth",
                description="The maximum path depth for which diffuse reflections are allowed",
                min=1, max=8,
                default=2,
                )
        cls.max_diffuse_depth = IntProperty(
                name="Max. diffuse depth",
                description="The maximum path depth for which diffuse reflections are allowed",
                min=1, max=2048,
                default=8,
                )
        cls.max_glossy_depth = IntProperty(
                name="Max. glossy depth",
                description="The maximum path depth for which specular reflections/refractions are allowed",
                min=1, max=2048,
                default=24,
                )
        cls.parallel_samples = IntProperty(
                name="Parallel samples",
                description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed",
                min=1, max=16,
                default=8,
                )
        cls.max_tile_samples = IntProperty(
                name="Max. tile samples",
                description="The maximum samples we calculate until we switch to a new tile",
                min=1, max=32,
                default=16,
                )
        cls.minimize_net_traffic = BoolProperty(
                name="Minimize net traffic",
                description="If enabled, the work is distributed to the network render slaves in such a way to minimize the amount of data that is sent to the network render master",
                default=True,
                )
        cls.deep_image = BoolProperty(
                name="Deep image",
                description="Render and save deep image file into output folder after frame render is finished",
                default=False,
                )
        cls.max_depth_samples = IntProperty(
                name="Max. depth samples",
                description="Maximum number of depth samples per pixels",
                min=1, max=32,
                default=8,
                )
        cls.depth_tolerance = FloatProperty(
                name="Depth tolerance",
                description="Depth samples whose relative depth difference falls below the tolerance value are merged together",
                min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
                default=0.05,
                step=1,
                precision=3,
                )
        cls.work_chunk_size = IntProperty(
                name="Work chunk size",
                description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value increases the memory usage on the system, but doesn't affect memory usage on the system and may increase render speed",
                min=1, max=32,
                default=8,
                )
        cls.ao_alpha_shadows = BoolProperty(
                name="AO alpha shadows",
                description="Take into account alpha maps when calculating ambient occlusion",
                default=False,
                )
        cls.opacity_threshold = FloatProperty(
                name="Opacity threshold",
                description="Geometry with opacity higher or equal to this value is treated as totally opaque",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=1,
                precision=3,
                )

        cls.exploration = FloatProperty(
                name="Exploration strength",
                description="Effort on investigating good paths",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.7,
                step=10,
                precision=2,
                )
        cls.direct_light_importance = FloatProperty(
                name="Direct light imp.",
                description="Computational effort on direct lighting",
                min=0.01, soft_min=0.01, max=1.0, soft_max=1.0,
                default=0.1,
                step=1,
                precision=2,
                )
        cls.max_rejects = IntProperty(
                name="Max. rejects",
                description="Maximum number of consecutive rejects",
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
                description="UV coordinate value mapped to maximum intensity",
                min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=1,
                precision=5,
                )
        cls.distributed_tracing = BoolProperty(
                name="Distributed ray tracing",
                description="Enable depth of field and motion blur",
                default=True,
                )
        cls.max_speed = FloatProperty(
                name="Max speed",
                description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
                min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
                default=1.0,
                step=100,
                precision=3,
                )

        cls.bump_normal_mapping = BoolProperty(
                name="Bump and normal mapping",
                description="Take bump and normal mapping into account for shading normal output and wireframe shading",
                default=False,
                )
        cls.wf_bkface_hl = BoolProperty(
                name="Wireframe backface highlighting",
                description="Show faces seen from the backside of the face normal in a different color in wireframe mode",
                default=False,
                )
        cls.path_term_power = FloatProperty(
                name="Path term. power",
                description="Path may get terminated when ray power is less then this value",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.3,
                step=10,
                precision=2,
                )
        cls.coherent_ratio = FloatProperty(
                name="Coherent ratio",
                description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.static_noise = BoolProperty(
                name="Static noise",
                description="If enabled, the noise patterns are kept stable between frames",
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
        cls.hdr_tonemap_enable = BoolProperty(
                name="Enable HDR tonemapping",
                description="Tick to enable Octane HDR tonemapping",
                default=False,
                )

#        cls.hdr_tonemapped = BoolProperty(
#                name="Tonemapped HDR",
#                description="",
#                default=True,
#                )

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
                description="The panoramic projection that should be used",
                items=types.camera_pan_modes,
                default='SPHERE',
                )
        cls.fov_x = FloatProperty(
                name="FOV X",
                description="Horizontal field of view in degrees. Will be ignored if cube mapping is used",
                min=1.0, soft_min=1.0, max=360.0, soft_max=360.0,
                default=360.0,
                step=10,
                precision=3,
                )
        cls.fov_y = FloatProperty(
                name="FOV Y",
                description="Vertical field of view in degrees. Will be ignored if cube mapping is used",
                min=1.0, soft_min=1.0, max=180.0, soft_max=180.0,
                default=360.0,
                step=10,
                precision=3,
                )
        cls.persp_corr = BoolProperty(
                name="Persp. correction",
                description="Perspective correction keeps vertical lines parallel if up-vector is vertical",
                default=False,
                )
        cls.stereo_mode = EnumProperty(
                name="Stereo mode",
                description="The modus operandi for stereo rendering",
                items=types.camera_stereo_modes,
                default='1',
                )
        cls.stereo_out = EnumProperty(
                name="Stereo output",
                description="The output rendered in stereo mode",
                items=types.camera_stereo_outs,
                default='0',
                )
        cls.stereo_dist = FloatProperty(
                name="Stereo distance",
                description="Distance between the left and right eye in stereo mode [m]",
                min=0.001, soft_min=0.001, max=2.0, soft_max=2.0,
                default=0.02,
                step=10,
                precision=3,
                )
        cls.stereo_dist_falloff = FloatProperty(
                name="Stereo dist. falloff",
                description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1"
                    " will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces"
                    " to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce"
                    " the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude"
                    " to something < 90 degrees",
                min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.stereo_swap_eyes = BoolProperty(
                name="Swap eyes",
                description="Swaps left and right eye positions when stereo mode is showing both",
                default=False,
                )
        cls.left_filter = FloatVectorProperty(
                name="Left filter",
                description="Left eye filter color",
                min=0.0, max=1.0,
                default=(1.0, 0.0, 0.812),
                subtype='COLOR',
                )
        cls.right_filter = FloatVectorProperty(
                name="Right filter",
                description="Right eye filter color",
                min=0.0, max=1.0,
                default=(0.0, 1.0, 0.188),
                subtype='COLOR',
                )
        cls.use_fstop = BoolProperty(
                name="Use F-Stop",
                description="Use F-Stop setting inside of aperture",
                default=False,
                )
        cls.aperture = FloatProperty(
                name="Aperture",
                description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
                min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.fstop = FloatProperty(
                name="F-Stop",
                description="Aperture to focal length ratio",
                min=0.5, soft_min=1.4, max=64.0, soft_max=16.0,
                default=2.8,
                step=10,
                precision=1,
                )
        cls.aperture_edge = FloatProperty(
                name="Aperture edge",
                description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
                min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.distortion = FloatProperty(
                name="Distortion",
                description="The amount of spherical distortion",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.autofocus = BoolProperty(
                name="Autofocus",
                description="If enabled, the focus will be kept on the closest visible surface at the center of the image",
                default=True,
                )
        cls.pixel_aspect = FloatProperty(
                name="Pixel aspect",
                description="The X:Y aspect ratio of pixels",
                min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.aperture_aspect = FloatProperty(
                name="Aperture aspect",
                description="The X:Y aspect ratio of the aperture",
                min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.keep_upright = BoolProperty(
                name="Keep upright",
                description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical",
                default=False,
                )
        cls.blackout_lat = FloatProperty(
                name="Pano blackout lat.",
                description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be"
                    " blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out",
                min=1.0, soft_min=1.0, max=90.0, soft_max=90.0,
                default=90.0,
                step=10,
                precision=3,
                )

        cls.baking_camera = BoolProperty(
                name="Baking camera",
                description="Use as baking camera",
                default=False,
                )
        cls.baking_revert = BoolProperty(
                name="Revert baking",
                description="If enabled, camera rays are flipped, which allows using the geometry as a lens",
                default=False,
                )
        cls.baking_use_position = BoolProperty(
                name="Use baking position",
                description="Use the provided position for baking position-dependent artifacts",
                default=False,
                )
        cls.baking_bkface_culling = BoolProperty(
                name="Backface culling",
                description="When using a baking position, tells whether to bake back geometry faces",
                default=True,
                )
        cls.baking_tolerance = FloatProperty(
                name="Edge noise tolerance",
                description="Specifies the tolerance to either keep or discard edge noise",
                min=0.0, max=1.0,
                default=0.5,
                step=10,
                precision=2,
                )
        cls.baking_uvbox_min_x = FloatProperty(
                name="UV box min. X",
                description="Coordinates in UV space of the the origin of the bounding region for baking",
                default=0.0,
                step=10,
                precision=2,
                )
        cls.baking_uvbox_min_y = FloatProperty(
                name="UV box min. Y",
                description="Coordinates in UV space of the the origin of the bounding region for baking",
                default=0.0,
                step=10,
                precision=2,
                )
        cls.baking_uvbox_size_x = FloatProperty(
                name="UV box size X",
                description="Size in UV space of the bounding region for baking",
                min=0.0001,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.baking_uvbox_size_y = FloatProperty(
                name="UV box size Y",
                description="Size in UV space of the bounding region for baking",
                min=0.0001,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.baking_group_id = IntProperty(
                name="Baking group ID",
                description="Specifies which baking group ID should be baked",
                min=1, max=65535,
                default=1,
                )
        cls.baking_padding = IntProperty(
                name="Size",
                description="Number of pixels added to the UV map edges",
                min=0, max=16,
                default=4,
                )
        cls.baking_uv_set = IntProperty(
                name="UV set",
                description="Determines which set of UV coordinates to use for baking camera",
                min=1, max=3,
                default=1,
                )

        cls.white_balance = FloatVectorProperty(
                name="White balance",
                description="White point color",
                min=0.0, max=1.0,
                default=(1.0, 1.0, 1.0),
                subtype='COLOR',
                )
        cls.response_type = EnumProperty(
                name="Response type",
                description="Camera response curve",
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
        cls.gamma = FloatProperty(
                name="Gamma",
                description="Output gamma correction",
                min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.vignetting = FloatProperty(
                name="Vignetting",
                description="Amount of lens vignetting",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.3,
                step=1,
                precision=2,
                )
        cls.saturation = FloatProperty(
                name="Saturation",
                description="Amount of saturation",
                min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.hot_pix = FloatProperty(
                name="Hotpixel removal",
                description="Luminance threshold for firefly reduction",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.premultiplied_alpha = BoolProperty(
                name="Premultiplied alpha",
                description="If enabled, we pre-multiply an alpha value",
                default=False,
                )
        cls.min_display_samples = IntProperty(
                name="Min. display samples",
                description="Minumum number of samples before the first image is displayed",
                min=1, max=32,
                default=1,
                )
        cls.dithering = BoolProperty(
                name="Dithering",
                description="Enables dithering to remove banding",
                default=False,
                )
        cls.white_saturation = FloatProperty(
                name="White saturation",
                description="Controls if clipping is done per channel or not",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )
        cls.highlight_compression = FloatProperty(
                name="Highlight compression",
                description="Reduces burned out highlights by compressing them and reducing their contrast",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )
        cls.neutral_response = BoolProperty(
                name="Neutral response",
                description="If enabled, the camera response curve will not affect the colors",
                default=False,
                )
        cls.max_tonemap_interval = IntProperty(
                name="Max. tonemap interval",
                description="Maximum interval between tonemaps (in seconds)",
                min=1, max=120,
                default=20,
                )
        cls.disable_partial_alpha = BoolProperty(
                name="Disable partial alpha",
                description="Make pixels that are partially transparent (alpha > 0) fully opaque",
                default=False,
                )

        cls.postprocess = BoolProperty(
                name="Postprocess",
                description="Enable post processing",
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

        cls.use_fstop = BoolProperty(
                name="Use F-Stop",
                description="Use F-Stop setting inside of aperture",
                default=False,
                )
        cls.aperture = FloatProperty(
                name="Aperture",
                description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
                min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
                default=0.0,
                step=10,
                precision=2,
                )
        cls.fstop = FloatProperty(
                name="F-Stop",
                description="Aperture to focal length ratio",
                min=0.5, soft_min=1.4, max=64.0, soft_max=16.0,
                default=2.8,
                step=10,
                precision=1,
                )
        cls.aperture_edge = FloatProperty(
                name="Aperture edge",
                description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
                min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.distortion = FloatProperty(
                name="Distortion",
                description="The amount of spherical distortion",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=2,
                )

        cls.white_balance = FloatVectorProperty(
                name="White balance",
                description="White point color",
                min=0.0, max=1.0,
                default=(1.0, 1.0, 1.0),
                subtype='COLOR',
                )
        cls.response_type = EnumProperty(
                name="Response type",
                description="Camera response curve",
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
        cls.gamma = FloatProperty(
                name="Gamma",
                description="Output gamma correction",
                min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
                default=1.0,
                step=10,
                precision=2,
                )
        cls.vignetting = FloatProperty(
                name="Vignetting",
                description="Amount of lens vignetting",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.3,
                step=1,
                precision=2,
                )
        cls.saturation = FloatProperty(
                name="Saturation",
                description="Amount of saturation",
                min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.hot_pix = FloatProperty(
                name="Hotpixel removal",
                description="Luminance threshold for firefly reduction",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=1,
                precision=2,
                )
        cls.premultiplied_alpha = BoolProperty(
                name="Premultiplied alpha",
                description="If enabled, we pre-multiply an alpha value",
                default=False,
                )
        cls.min_display_samples = IntProperty(
                name="Min. display samples",
                description="Minumum number of samples before the first image is displayed",
                min=1, max=32,
                default=1,
                )
        cls.dithering = BoolProperty(
                name="Dithering",
                description="Enables dithering to remove banding",
                default=False,
                )
        cls.white_saturation = FloatProperty(
                name="White saturation",
                description="Controls if clipping is done per channel or not",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )
        cls.highlight_compression = FloatProperty(
                name="Highlight compression",
                description="Reduces burned out highlights by compressing them and reducing their contrast",
                min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=1,
                precision=2,
                )
        cls.neutral_response = BoolProperty(
                name="Neutral response",
                description="If enabled, the camera response curve will not affect the colors",
                default=False,
                )
        cls.max_tonemap_interval = IntProperty(
                name="Max. tonemap interval",
                description="Maximum interval between tonemaps (in seconds)",
                min=1, max=120,
                default=20,
                )
        cls.disable_partial_alpha = BoolProperty(
                name="Disable partial alpha",
                description="Make pixels that are partially transparent (alpha > 0) fully opaque",
                default=False,
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
                description="Environment texture",
                default="",
                maxlen=512,
                )
        cls.env_power = FloatProperty(
                name="Power",
                description="Scale factor that is applied to the sun and sky",
                min=0.001, soft_min=0.001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.env_importance_sampling = BoolProperty(
                name="Importance sampling",
                description="Use importance sampling for image textures",
                default=True,
                )
        cls.env_daylight_type = EnumProperty(
                name="Daylight type",
                description="",
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
                description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light",
                min=2.0, soft_min=2.0, max=6.0, soft_max=6.0,
                default=2.2,
                step=10,
                precision=3,
                )
        cls.env_northoffset = FloatProperty(
                name="North offset",
                description="Additional rotation offset on longitude",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.env_model = EnumProperty(
                name="Model",
                description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
                items=types.environment_daylight_models,
                default='1',
                )
        cls.env_sky_color = FloatVectorProperty(
                name="Sky color",
                description="Base color of the sky, which works only with the new daylight model",
                min=0.0, max=1.0,
                default=(0.05, 0.3, 1.0),
                subtype='COLOR',
                )
        cls.env_sunset_color = FloatVectorProperty(
                name="Sunset color",
                description="Color of the sky and sun at sunset, which works only with the new daylight model",
                min=0.0, max=1.0,
                default=(0.6, 0.12, 0.02),
                subtype='COLOR',
                )
        cls.env_sun_size = FloatProperty(
                name="Sun size",
                description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
                min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
                default=1.0,
                step=10,
                precision=4,
                )
        cls.env_longitude = FloatProperty(
                name="Longitude",
                description="Longitude of the location",
                min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
                default=4.4667,
                step=1,
                precision=4,
                )
        cls.env_latitude = FloatProperty(
                name="Latitude",
                description="Latitude of the location",
                min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
                default=50.7667,
                step=1,
                precision=4,
                )
        cls.env_day = IntProperty(
                name="Day",
                description="Day of the month of the time the sun direction should be calculated for",
                min=1, max=31,
                default=1,
                )
        cls.env_month = IntProperty(
                name="Month",
                description="Month of the time the sun direction should be calculated for",
                min=1, max=12,
                default=3,
                )
        cls.env_gmtoffset = IntProperty(
                name="GMT offset",
                description="The time zone as offset to GMT",
                min=-12, max=12,
                default=0,
                )
        cls.env_hour = FloatProperty(
                name="Local time",
                description="The local time as hours since 0:00",
                min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
                default=14,
                step=100,
                precision=1,
                )
        cls.env_med_radius = FloatProperty(
                name="Medium radius",
                description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius",
                min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
                default=1.0,
                step=3,
                precision=4,
                )
        cls.env_medium = StringProperty(
                name="Medium",
                description="The medium in the environment (free space). Ignored when this environment is used as a the visible environment",
                default="",
                maxlen=512,
                )


        cls.use_vis_env = BoolProperty(
                name="Use visible environment",
                description="",
                default=False,
                )
        cls.env_vis_type = EnumProperty(
                name="Environment type",
                description="",
                items=types.environment_types,
                default='1',
                )
        cls.env_vis_texture = StringProperty(
                name="Texture",
                description="Environment texture",
                default="",
                maxlen=512,
                )
        cls.env_vis_power = FloatProperty(
                name="Power",
                description="Scale factor that is applied to the sun and sky",
                min=0.001, soft_min=0.001, max=1000.0, soft_max=1000.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.env_vis_importance_sampling = BoolProperty(
                name="Octane importance sampling",
                description="Use importance sampling for image textures",
                default=True,
                )
        cls.env_vis_daylight_type = EnumProperty(
                name="Daylight type",
                description="",
                items=types.environment_daylight_types,
                default='1',
                )
        cls.env_vis_sundir_x = FloatProperty(
                name="Sun direction X",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.env_vis_sundir_y = FloatProperty(
                name="Sun direction Y",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=1.0,
                step=10,
                precision=3,
                )
        cls.env_vis_sundir_z = FloatProperty(
                name="Sun direction Z",
                description="",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=-0.0,
                step=10,
                precision=3,
                )
        cls.env_vis_turbidity = FloatProperty(
                name="Turbidity",
                description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light",
                min=2.0, soft_min=2.0, max=6.0, soft_max=6.0,
                default=2.2,
                step=10,
                precision=3,
                )
        cls.env_vis_northoffset = FloatProperty(
                name="North offset",
                description="Additional rotation offset on longitude",
                min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
                default=0.0,
                step=10,
                precision=3,
                )
        cls.env_vis_model = EnumProperty(
                name="Model",
                description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
                items=types.environment_daylight_models,
                default='1',
                )
        cls.env_vis_sky_color = FloatVectorProperty(
                name="Sky color",
                description="Base color of the sky, which works only with the new daylight model",
                min=0.0, max=1.0,
                default=(0.05, 0.3, 1.0),
                subtype='COLOR',
                )
        cls.env_vis_sunset_color = FloatVectorProperty(
                name="Sunset color",
                description="Color of the sky and sun at sunset, which works only with the new daylight model",
                min=0.0, max=1.0,
                default=(0.6, 0.12, 0.02),
                subtype='COLOR',
                )
        cls.env_vis_sun_size = FloatProperty(
                name="Sun size",
                description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
                min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
                default=1.0,
                step=10,
                precision=4,
                )
        cls.env_vis_longitude = FloatProperty(
                name="Longitude",
                description="Longitude of the location",
                min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
                default=4.4667,
                step=1,
                precision=4,
                )
        cls.env_vis_latitude = FloatProperty(
                name="Latitude",
                description="Latitude of the location",
                min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
                default=50.7667,
                step=1,
                precision=4,
                )
        cls.env_vis_day = IntProperty(
                name="Day",
                description="Day of the month of the time the sun direction should be calculated for",
                min=1, max=31,
                default=1,
                )
        cls.env_vis_month = IntProperty(
                name="Month",
                description="Month of the time the sun direction should be calculated for",
                min=1, max=12,
                default=3,
                )
        cls.env_vis_gmtoffset = IntProperty(
                name="GMT offset",
                description="The time zone as offset to GMT",
                min=-12, max=12,
                default=0,
                )
        cls.env_vis_hour = FloatProperty(
                name="Local time",
                description="The local time as hours since 0:00",
                min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
                default=14,
                step=100,
                precision=1,
                )
        cls.env_vis_med_radius = FloatProperty(
                name="Medium radius",
                description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius",
                min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
                default=1.0,
                step=3,
                precision=4,
                )
        cls.env_vis_medium = StringProperty(
                name="Medium",
                description="The medium in the environment (free space). Ignored when this environment is used as a the visible environment",
                default="",
                maxlen=512,
                )
        cls.env_vis_backplate = BoolProperty(
                name="Backplate",
                description="When used as a visible environment, this environment will behave as a backplate image",
                default=False,
                )
        cls.env_vis_reflections = BoolProperty(
                name="Reflections",
                description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)",
                default=False,
                )
        cls.env_vis_refractions = BoolProperty(
                name="Refractions",
                description="When used as a visible environment, this environment will be visible in refractions",
                default=False,
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
                description="",
                type=cls,
                )
        bpy.types.Curve.octane = PointerProperty(
                name="OctaneRender Curve Settings",
                description="",
                type=cls,
                )
        bpy.types.MetaBall.octane = PointerProperty(
                name="OctaneRender MetaBall Settings",
                description="",
                type=cls,
                )

        cls.winding_order = EnumProperty(
                name="Winding order",
                description="May be usable if you need to correct some Octane's triangulation artifacts. Alembic export requires clockwise order",
                items=types.winding_orders,
                default='0',
                )
        cls.mesh_type = EnumProperty(
                name="Mesh type",
                description="Used for rendering speed optimization, see the manual",
                items=types.mesh_types,
                default='0',
                )
        cls.open_subd_enable = BoolProperty(
                name="Enable OpenSubDiv",
                description="Subdivide mesh before rendering",
                default=False,
                )
        cls.open_subd_scheme = EnumProperty(
                name="Scheme",
                description="",
                items=types.subd_scheme,
                default='1',
                )
        cls.open_subd_level = IntProperty(
                name="Subd level",
                description="",
                min=0, max=10,
                default=0,
                )
        cls.open_subd_sharpness = FloatProperty(
                name="Sharpness",
                description="",
                min=0.0, max=11.0, soft_max=11.0,
                default=0.0,
                )
        cls.open_subd_bound_interp = EnumProperty(
                name="Boundary interp.",
                description="",
                items=types.bound_interp,
                default='3',
                )
        cls.vis_general = FloatProperty(
                name="General visibility",
                description="",
                min=0.0, max=1.0, soft_max=1.0,
                default=1.0,
                )
        cls.vis_cam = BoolProperty(
                name="Camera visibility",
                description="",
                default=True,
                )
        cls.vis_shadow = BoolProperty(
                name="Shadow visibility",
                description="",
                default=True,
                )
        cls.rand_color_seed = IntProperty(
                name="Random color seed",
                description="",
                min=0, max=65535,
                default=0,
                )
        cls.layer_number = IntProperty(
                name="Layer number",
                description="",
                min=1, max=255,
                default=1,
                )
        cls.baking_group_id = IntProperty(
                name="Baking group",
                description="",
                min=1, max=65535,
                default=1,
                )

        cls.vdb_iso = FloatProperty(
                name="ISO",
                description="Isovalue used for when rendering openvdb level sets",
                min=0.0,
                default=0.04,
                )
        cls.vdb_abs_scale = FloatProperty(
                name="Absorption scale",
                description="This scalar value scales the grid value used for absorption",
                min=0.0,
                default=1.0,
                )
        cls.vdb_emiss_scale = FloatProperty(
                name="Emission scale",
                description="This scalar value scales the grid value used for temperature. Use this when temperature information in a grid is too low",
                min=0.0,
                default=1.0,
                )
        cls.vdb_scatter_scale = FloatProperty(
                name="Scatter scale",
                description="This scalar value scales the grid value used for scattering",
                min=0.0,
                default=1.0,
                )
        cls.vdb_vel_scale = FloatProperty(
                name="Velocity scale",
                description="This scalar value linearly scales velocity vectors in the velocity grid",
                min=0.0,
                default=1.0,
                )
        cls.hair_interpolation = EnumProperty(
                name="Hair W interpolation",
                description="Specifies the hair interpolation type. If \"Use hair Ws\" is chosen - you need to explicitly set the hairs root/tip W coordinates in Octane's part of particle settings",
                items=types.hair_interpolations,
                default='0',
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Mesh.octane
        del bpy.types.Curve.octane
        del bpy.types.MetaBall.octane


class OctaneHairSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.ParticleSettings.octane = PointerProperty(
                name="Octane Hair Settings",
                description="Octane hair settings",
                type=cls,
                )
        cls.root_width = FloatProperty(
                name="Root thickness",
                description="Hair thickness at root",
                min=0.0, max=1000.0,
                default=0.001,
                )
        cls.tip_width = FloatProperty(
                name="Tip thickness",
                description="Hair thickness at tip",
                min=0.0, max=1000.0,
                default=0.001,
                )
        cls.min_curvature = FloatProperty(
                name="Minimal curvature (deg.)",
                description="Hair points having angle deviation from previous point less than this value will be skipped",
                min=0.0, max=180.0,
                default=0.0001,
                )
        cls.w_min = FloatProperty(
                name="Min. W",
                description="W coordinate of the root of a hair: it represents a position on a color gradient for roots of all hairs of this particle system",
                min=0.0, max=1.0,
                default=0.0,
                )
        cls.w_max = FloatProperty(
                name="Max. W",
                description="W coordinate of the tip of a hair: it represents a position on a color gradient for tips of all hairs of this particle system",
                min=0.0, max=1.0,
                default=1.0,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.ParticleSettings.octane


def register():
    bpy.utils.register_class(OctaneRenderSettings)
    bpy.utils.register_class(OctaneCameraSettings)
    bpy.utils.register_class(OctaneSpaceDataSettings)
    bpy.utils.register_class(OctaneMaterialSettings)
    bpy.utils.register_class(OctaneLampSettings)
    bpy.utils.register_class(OctaneWorldSettings)
    bpy.utils.register_class(OctaneObjPropertiesSettings)
    bpy.utils.register_class(OctaneMeshSettings)
    bpy.utils.register_class(OctaneHairSettings)


def unregister():
    bpy.utils.unregister_class(OctaneRenderSettings)
    bpy.utils.unregister_class(OctaneCameraSettings)
    bpy.utils.unregister_class(OctaneSpaceDataSettings)
    bpy.utils.unregister_class(OctaneMaterialSettings)
    bpy.utils.unregister_class(OctaneLampSettings)
    bpy.utils.unregister_class(OctaneWorldSettings)
    bpy.utils.unregister_class(OctaneMeshSettings)
    bpy.utils.unregister_class(OctaneObjPropertiesSettings)
    bpy.utils.unregister_class(OctaneHairSettings)
