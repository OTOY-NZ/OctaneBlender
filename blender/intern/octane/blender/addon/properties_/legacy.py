# <pep8 compliant>

import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, \
    FloatVectorProperty
from bpy.utils import register_class, unregister_class


#############################################
# LEGACY OctaneLegacyWorldPropertyGroup
# For the legacy versions which are older than 20.x
#############################################


class OctaneLegacyWorldPropertyGroup(bpy.types.PropertyGroup):
    environment_types = (
        ('0', "Texture", ""),
        ('1', "Daylight", ""),
        ('2', "Planetary", ""),
    )
    env_type: EnumProperty(
        name="Environment type",
        description="",
        items=environment_types,
        default='1',
    )
    # LEGACY COMPATIBILITY
    env_texture: StringProperty(
        name="Texture",
        description="LEGACY COMPATIBILITY",
        default="",
        maxlen=512,
    )
    env_texture_ptr: PointerProperty(
        name="Texture",
        description="Environment texture pointer",
        type=bpy.types.Texture,
    )

    env_power: FloatProperty(
        name="Power",
        description="Scale factor that is applied to the sun and sky",
        min=0, soft_min=0, max=1000.0, soft_max=1000.0,
        default=1.0,
        step=10,
        precision=3,
    )
    env_importance_sampling: BoolProperty(
        name="Importance sampling",
        description="Use importance sampling for image textures",
        default=True,
    )
    environment_daylight_types = (
        ('0', "Direction", ""),
        ('1', "Daylight system", ""),
    )
    env_daylight_type: EnumProperty(
        name="Daylight type",
        description="",
        items=environment_daylight_types,
        default='1',
    )
    env_sundir_x: FloatProperty(
        name="Sun direction X",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    env_sundir_y: FloatProperty(
        name="Sun direction Y",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    env_sundir_z: FloatProperty(
        name="Sun direction Z",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=-0.0,
        step=10,
        precision=3,
    )
    env_turbidity: FloatProperty(
        name="Turbidity",
        description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the "
                    "contrast between objects in the shadow and in sun light",
        min=2.0, soft_min=2.0, max=15.0, soft_max=15.0,
        default=2.2,
        step=10,
        precision=3,
    )
    env_northoffset: FloatProperty(
        name="North offset",
        description="Additional rotation offset on longitude",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    environment_daylight_models = (
        ('0', "Old", ""),
        ('1', "New", ""),
        ('2', "Nishita", ""),
    )
    env_model: EnumProperty(
        name="Model",
        description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
        items=environment_daylight_models,
        default='1',
    )
    env_sky_color: FloatVectorProperty(
        name="Sky color",
        description="Base color of the sky, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.05, 0.3, 1.0),
        subtype='COLOR',
    )
    env_sunset_color: FloatVectorProperty(
        name="Sunset color",
        description="Color of the sky and sun at sunset, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.6, 0.12, 0.02),
        subtype='COLOR',
    )
    env_ground_color: FloatVectorProperty(
        name="Ground color",
        description="Base color of the ground, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.0, 0.0, 0.0),
        subtype='COLOR',
    )
    env_ground_start_angle: FloatProperty(
        name="Ground start angle",
        description="The angle (in degrees) below the horizon where the transition to the ground color starts",
        min=0.0, max=90.0,
        default=90.0,
        step=10,
        precision=4,
    )
    env_ground_blend_angle: FloatProperty(
        name="Ground blend angle",
        description="The angle over which the sky color transitions to the ground color",
        min=1.0, max=90.0,
        default=5.0,
        step=10,
        precision=4,
    )
    env_sun_size: FloatProperty(
        name="Sun size",
        description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
        min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
        default=1.0,
        step=10,
        precision=4,
    )
    env_longitude: FloatProperty(
        name="Longitude",
        description="Longitude of the location",
        min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
        default=4.4667,
        step=1,
        precision=4,
    )
    env_latitude: FloatProperty(
        name="Latitude",
        description="Latitude of the location",
        min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
        default=50.7667,
        step=1,
        precision=4,
    )
    env_day: IntProperty(
        name="Day",
        description="Day of the month of the time the sun direction should be calculated for",
        min=1, max=31,
        default=1,
    )
    env_month: IntProperty(
        name="Month",
        description="Month of the time the sun direction should be calculated for",
        min=1, max=12,
        default=3,
    )
    env_gmtoffset: IntProperty(
        name="GMT offset",
        description="The time zone as offset to GMT",
        min=-12, max=12,
        default=0,
    )
    env_hour: FloatProperty(
        name="Local time",
        description="The local time as hours since 0:00",
        min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
        default=14,
        step=100,
        precision=1,
    )
    env_med_radius: FloatProperty(
        name="Medium radius",
        description="Radius of the environment medium. The environment medium acts as a sphere around the camera "
                    "position with the specified radius",
        min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
        default=1.0,
        step=3,
        precision=4,
    )
    # LEGACY COMPATIBILITY
    env_medium: StringProperty(
        name="Medium",
        description="LEGACY COMPATIBILITY",
        default="",
        maxlen=512,
    )
    env_medium_ptr: PointerProperty(
        name="Medium",
        description="The medium in the environment (free space). Ignored when this environment is used as a the "
                    "visible environment",
        type=bpy.types.Texture,
    )
    env_altitude: FloatProperty(
        name="Altitude",
        description="The camera altitude",
        min=0.1, soft_min=0.1, max=10000000000, soft_max=10000000000,
        default=1.0,
        step=3,
        precision=3,
    )
    env_star_field: PointerProperty(
        name="Star field",
        description="Star fields behind the planet",
        type=bpy.types.Texture,
    )
    env_ground_albedo: PointerProperty(
        name="Ground albedo",
        description="Surface texture map on the planet",
        type=bpy.types.Texture,
    )
    env_ground_reflection: PointerProperty(
        name="Ground reflection",
        description="Specular texture map on the planet",
        type=bpy.types.Texture,
    )
    env_ground_glossiness: PointerProperty(
        name="Ground glossiness",
        description="The planetary glossiness",
        type=bpy.types.Texture,
    )
    env_ground_emission: PointerProperty(
        name="Ground emission",
        description="Surface texture map on the planet at night time",
        type=bpy.types.Texture,
    )
    env_ground_normal_map: PointerProperty(
        name="Ground normal map",
        description="Normal map on the planet",
        type=bpy.types.Texture,
    )
    env_ground_elevation: PointerProperty(
        name="Ground elevation",
        description="Elevation map on the planet",
        type=bpy.types.Texture,
    )
    env_planetary_axis: FloatVectorProperty(
        name="Planetary axis",
        description="The rotational axis of the planet running through the North and South pole",
        min=-1.0, max=1.0,
        default=(0.0, 0.0, 1.0),
        subtype='XYZ',
    )
    env_planetary_angle: FloatProperty(
        name="Planetary angle",
        description="The rotation around the planetary axis",
        min=-3.1415923, soft_min=-3.1415923, max=3.1415923, soft_max=3.1415923,
        default=0.0,
        step=4,
        precision=4,
    )
    use_vis_env: BoolProperty(
        name="Use visible environment",
        description="",
        default=False,
    )
    env_vis_type: EnumProperty(
        name="Environment type",
        description="",
        items=environment_types,
        default='1',
    )
    # LEGACY COMPATIBILITY
    env_vis_texture: StringProperty(
        name="Texture",
        description="LEGACY COMPATIBILITY",
        default="",
        maxlen=512,
    )
    env_vis_texture_ptr: PointerProperty(
        name="Texture",
        description="Environment texture",
        type=bpy.types.Texture,
    )
    env_vis_power: FloatProperty(
        name="Power",
        description="Scale factor that is applied to the sun and sky",
        min=0, soft_min=0, max=1000.0, soft_max=1000.0,
        default=1.0,
        step=10,
        precision=3,
    )
    env_vis_importance_sampling: BoolProperty(
        name="Octane importance sampling",
        description="Use importance sampling for image textures",
        default=True,
    )
    env_vis_daylight_type: EnumProperty(
        name="Daylight type",
        description="",
        items=environment_daylight_types,
        default='1',
    )
    env_vis_sundir_x: FloatProperty(
        name="Sun direction X",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    env_vis_sundir_y: FloatProperty(
        name="Sun direction Y",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    env_vis_sundir_z: FloatProperty(
        name="Sun direction Z",
        description="",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=-0.0,
        step=10,
        precision=3,
    )
    env_vis_turbidity: FloatProperty(
        name="Turbidity",
        description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the "
                    "contrast between objects in the shadow and in sun light",
        min=2.0, soft_min=2.0, max=6.0, soft_max=6.0,
        default=2.2,
        step=10,
        precision=3,
    )
    env_vis_northoffset: FloatProperty(
        name="North offset",
        description="Additional rotation offset on longitude",
        min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=3,
    )
    env_vis_model: EnumProperty(
        name="Model",
        description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
        items=environment_daylight_models,
        default='1',
    )
    env_vis_sky_color: FloatVectorProperty(
        name="Sky color",
        description="Base color of the sky, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.05, 0.3, 1.0),
        subtype='COLOR',
    )
    env_vis_sunset_color: FloatVectorProperty(
        name="Sunset color",
        description="Color of the sky and sun at sunset, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.6, 0.12, 0.02),
        subtype='COLOR',
    )
    env_vis_ground_color: FloatVectorProperty(
        name="Ground color",
        description="Base color of the ground, which works only with the new daylight model",
        min=0.0, max=1.0,
        default=(0.0, 0.0, 0.0),
        subtype='COLOR',
    )
    env_vis_ground_start_angle: FloatProperty(
        name="Ground start angle",
        description="The angle (in degrees) below the horizon where the transition to the ground color starts",
        min=0.0, max=90.0,
        default=90.0,
        step=10,
        precision=4,
    )
    env_vis_ground_blend_angle: FloatProperty(
        name="Ground blend angle",
        description="The angle over which the sky color transitions to the ground color",
        min=1.0, max=90.0,
        default=5.0,
        step=10,
        precision=4,
    )
    env_vis_sun_size: FloatProperty(
        name="Sun size",
        description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
        min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
        default=1.0,
        step=10,
        precision=4,
    )
    env_vis_longitude: FloatProperty(
        name="Longitude",
        description="Longitude of the location",
        min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
        default=4.4667,
        step=1,
        precision=4,
    )
    env_vis_latitude: FloatProperty(
        name="Latitude",
        description="Latitude of the location",
        min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
        default=50.7667,
        step=1,
        precision=4,
    )
    env_vis_day: IntProperty(
        name="Day",
        description="Day of the month of the time the sun direction should be calculated for",
        min=1, max=31,
        default=1,
    )
    env_vis_month: IntProperty(
        name="Month",
        description="Month of the time the sun direction should be calculated for",
        min=1, max=12,
        default=3,
    )
    env_vis_gmtoffset: IntProperty(
        name="GMT offset",
        description="The time zone as offset to GMT",
        min=-12, max=12,
        default=0,
    )
    env_vis_hour: FloatProperty(
        name="Local time",
        description="The local time as hours since 0:00",
        min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
        default=14,
        step=100,
        precision=1,
    )
    env_vis_med_radius: FloatProperty(
        name="Medium radius",
        description="Radius of the environment medium. The environment medium acts as a sphere around the camera "
                    "position with the specified radius",
        min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
        default=1.0,
        step=3,
        precision=4,
    )
    # LEGACY COMPATIBILITY
    env_vis_medium: StringProperty(
        name="Medium",
        description="LEGACY COMPATIBILITY",
        default="",
        maxlen=512,
    )
    env_vis_medium_ptr: PointerProperty(
        name="Medium",
        description="The medium in the environment (free space). Ignored when this environment is used as a the "
                    "visible environment",
        type=bpy.types.Texture,
    )
    env_vis_altitude: FloatProperty(
        name="Altitude",
        description="The camera altitude",
        min=0.1, soft_min=0.1, max=10000000000, soft_max=10000000000,
        default=1.0,
        step=3,
        precision=3,
    )
    env_vis_star_field: PointerProperty(
        name="Star field",
        description="Star fields behind the planet",
        type=bpy.types.Texture,
    )
    env_vis_ground_albedo: PointerProperty(
        name="Ground albedo",
        description="Surface texture map on the planet",
        type=bpy.types.Texture,
    )
    env_vis_ground_reflection: PointerProperty(
        name="Ground reflection",
        description="Specular texture map on the planet",
        type=bpy.types.Texture,
    )
    env_vis_ground_glossiness: PointerProperty(
        name="Ground glossiness",
        description="The planetary glossiness",
        type=bpy.types.Texture,
    )
    env_vis_ground_emission: PointerProperty(
        name="Ground emission",
        description="Surface texture map on the planet at night time",
        type=bpy.types.Texture,
    )
    env_vis_ground_normal_map: PointerProperty(
        name="Ground normal map",
        description="Normal map on the planet",
        type=bpy.types.Texture,
    )
    env_vis_ground_elevation: PointerProperty(
        name="Ground elevation",
        description="Elevation map on the planet",
        type=bpy.types.Texture,
    )
    env_vis_planetary_axis: FloatVectorProperty(
        name="Planetary axis",
        description="The rotational axis of the planet running through the North and South pole",
        min=-1.0, max=1.0,
        default=(0.0, 0.0, 1.0),
        subtype='XYZ',
    )
    env_vis_planetary_angle: FloatProperty(
        name="Planetary angle",
        description="The rotation around the planetary axis",
        min=-3.1415923, soft_min=-3.1415923, max=3.1415923, soft_max=3.1415923,
        default=0.0,
        step=4,
        precision=4,
    )
    env_vis_backplate: BoolProperty(
        name="Backplate",
        description="When used as a visible environment, this environment will behave as a backplate image",
        default=False,
    )
    env_vis_reflections: BoolProperty(
        name="Reflections",
        description="When used as a visible environment, this environment will be visible in reflections (specular "
                    "and glossy materials)",
        default=False,
    )
    env_vis_refractions: BoolProperty(
        name="Refractions",
        description="When used as a visible environment, this environment will be visible in refractions",
        default=False,
    )


#############################################
# LEGACY OctaneLegacyAIUpSamplerPropertyGroup
#############################################


class OctaneLegacyAIUpSamplerPropertyGroup(bpy.types.PropertyGroup):
    up_sample_modes = (
        ('No upsampling', "No upsampling", "", 1),
        ('2x2 upsampling', "2x2 upsampling", "", 2),
        ('4x4 upsampling', "4x4 upsampling", "", 4),
    )
    sample_mode: EnumProperty(
        name="Upsampling mode",
        description="The up-sample mode that should be used for rendering",
        items=up_sample_modes,
        default='No upsampling',
    )
    enable_ai_up_sampling: BoolProperty(
        name="Enable AI up-sampling",
        description="Enables the AI up-sampling when the sampling mode is one of the up-samples, and this toggle is "
                    "on. Otherwise we just trivially scale up the frame",
        default=True,
    )
    up_sampling_on_completion: BoolProperty(
        name="Up-sampling on completion",
        description="If enabled, beauty passes will be up-sampled only once at the end of a render",
        default=True,
    )
    min_up_sampler_samples: IntProperty(
        name="Min. up-sampler samples",
        description="Minimum number of samples per pixel until up-sampler kicks in. Only valid when the the sampling "
                    "mode is any of up-sampling",
        min=1, max=100000,
        default=10,
    )
    max_up_sampler_interval: IntProperty(
        name="Max. up-sampler interval",
        description="Maximum interval between up-sampler runs (in seconds). Only valid when the the sampling mode is "
                    "any of up-sampling",
        min=1, max=120,
        default=10,
    )


_CLASSES = [
    OctaneLegacyWorldPropertyGroup,
    OctaneLegacyAIUpSamplerPropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
