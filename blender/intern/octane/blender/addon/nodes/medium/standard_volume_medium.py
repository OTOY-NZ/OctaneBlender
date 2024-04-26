# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneStandardVolumeMediumDensity(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumDensity"
    bl_label = "Density"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_DENSITY
    octane_pin_name = "density"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The density of the volume, which is further scaled by the density channel", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=100.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumDensityChannel(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumDensityChannel"
    bl_label = "Density channel"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_DENSITY_CHANNEL
    octane_pin_name = "densityChannel"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="density", update=OctaneBaseSocket.update_node_tree, description="A channel that provides density values across the voxels of the volume, which are multiplied with the density input")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumInterpolationType(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumInterpolationType"
    bl_label = "Interpolation"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_INTERPOLATION_TYPE
    octane_pin_name = "interpolationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Closest", "Closest", "", 0),
        ("Trilinear", "Trilinear", "", 1),
        ("Tricubic", "Tricubic", "", 2),
    ]
    default_value: EnumProperty(default="Trilinear", update=OctaneBaseSocket.update_node_tree, description="The interpolation mode used when reading voxel data from the channel inputs", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumRayMarchStepPercent(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumRayMarchStepPercent"
    bl_label = "Volume step %"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RAYMARCH_STEP_PERCENT
    octane_pin_name = "rayMarchStepPercent"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Ray-marching step length, specified as a percentage of the voxel size", min=0.010000, max=1000000.000000, soft_min=50.000000, soft_max=1000.000000, step=1.000000, precision=4, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 14000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumShadowRayMarchStepPercent(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumShadowRayMarchStepPercent"
    bl_label = "Vol. shadow ray step %"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SHADOW_RAY_MARCH_STEP_PERCENT
    octane_pin_name = "shadowRayMarchStepPercent"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Shadow ray-marching step length, specified as a percentage of the voxel size", min=0.010000, max=1000000.000000, soft_min=50.000000, soft_max=1000.000000, step=1.000000, precision=4, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 14000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumUseRayStepLengthForShadowRays"
    bl_label = "Use 'Volume step length' for shadow rays"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_RAY_STEP_LENGTH_FOR_SHADOW_RAYS
    octane_pin_name = "useRayStepLengthForShadowRays"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Use the value from 'Volume step length' for the 'Shadow ray step length'")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumSingleScatterFactor(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumSingleScatterFactor"
    bl_label = "Single scatter amount"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SINGLE_SCATTER_FACTOR
    octane_pin_name = "singleScatterFactor"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Determines how often we calculate direct light in volumes, as a ratio of scatter events", min=1.000000, max=1000.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 12000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumDisplacement"
    bl_label = "Sample position displacement"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISPLACEMENT
    octane_pin_name = "displacement"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumVolumePadding(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumVolumePadding"
    bl_label = "Volume padding"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_VOLUME_PADDING
    octane_pin_name = "volumePadding"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Expands the volume bounding box by the given percentage in all 6 directions, but only if sample position displacement is being used", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value = False
    octane_min_version = 14000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumScatterWeight(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumScatterWeight"
    bl_label = "Scatter weight"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_SCATTER_WEIGHT
    octane_pin_name = "scatterWeight"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The scatter weight", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumScatterColor(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumScatterColor"
    bl_label = "Scatter color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_SCATTER_COLOR
    octane_pin_name = "scatterColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The scatter color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumScatterChannel(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumScatterChannel"
    bl_label = "Scatter color channel"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_SCATTER_CHANNEL
    octane_pin_name = "scatterChannel"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="A channel that provides scatter colors across the voxels of the volume, which act as a multiplier to the scatter color input")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumAnisotropy(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumAnisotropy"
    bl_label = "Scatter anisotropy"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ANISOTROPY
    octane_pin_name = "anisotropy"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Light scattering direction: negative values produce backward scattering, 0 produces equal scattering in all directions (isotropic), and positive values produce forward scattering", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTransparentWeight(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTransparentWeight"
    bl_label = "Transparency weight"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TRANSPARENT_WEIGHT
    octane_pin_name = "transparentWeight"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.368000, 0.368000, 0.368000), update=OctaneBaseSocket.update_node_tree, description="Additional control over the density of the volume, to tint the color of objects seen through the volume", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTransparentDepth(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTransparentDepth"
    bl_label = "Transparency depth"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_TRANSPARENT_DEPTH
    octane_pin_name = "transparentDepth"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Additional control over the density of the volume", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTransparentChannel(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTransparentChannel"
    bl_label = "Transparency channel"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_TRANSPARENT_CHANNEL
    octane_pin_name = "transparentChannel"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="A channel that provides transparency values across the voxels of the volume, which act as a multiplier to the transparency color input")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumEmissionType(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumEmissionType"
    bl_label = "Emission mode"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_EMISSION_TYPE
    octane_pin_name = "emissionType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("None", "None", "", 0),
        ("Channel", "Channel", "", 1),
        ("Density", "Density", "", 2),
        ("Black body", "Black body", "", 3),
    ]
    default_value: EnumProperty(default="Black body", update=OctaneBaseSocket.update_node_tree, description="The supported emission modes", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumEmissionWeight(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumEmissionWeight"
    bl_label = "Emission weight"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_EMISSION_WEIGHT
    octane_pin_name = "emissionWeight"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scales the emission of the volume", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumEmissionColor(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumEmissionColor"
    bl_label = "Emission color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_EMISSION_COLOR
    octane_pin_name = "emissionColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The emission color is multiplied with the emission values produced by the selected emission mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumEmissionChannel(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumEmissionChannel"
    bl_label = "Emission channel"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_EMISSION_CHANNEL
    octane_pin_name = "emissionChannel"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="heat", update=OctaneBaseSocket.update_node_tree, description="A channel that provides emission values across the voxels of the volume, which act as a multiplier to the emission color input")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumLightPassId(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumLightPassId"
    bl_label = "Light pass ID"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_LIGHT_PASS_ID
    octane_pin_name = "lightPassId"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the light pass that captures the contribution of this emitter", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTemperatureScale(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTemperatureScale"
    bl_label = "Temperature"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_TEMPERATURE_SCALE
    octane_pin_name = "temperatureScale"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="If a temperature channel is connected, then this scales the values read from it. Otherwise, it is the source of the temperature values, which are usually in the range [0..1]", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTemperatureChannel(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTemperatureChannel"
    bl_label = "Temperature channel"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_STRING
    octane_default_node_name = "OctaneStringValue"
    octane_pin_id = consts.PinID.P_TEMPERATURE_CHANNEL
    octane_pin_name = "temperatureChannel"
    octane_pin_type = consts.PinType.PT_STRING
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_STRING
    default_value: StringProperty(default="temperature", update=OctaneBaseSocket.update_node_tree, description="A channel that provides temperature values across the voxels of the volume. These are expected to be in the range [0..1]. 'Auto scale temperature channel' can be enabled to scale them to this range if necessary")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTemperature(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTemperature"
    bl_label = "Black body kelvin"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_TEMPERATURE
    octane_pin_name = "temperature"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5000.000000, update=OctaneBaseSocket.update_node_tree, description="Scales the unitless temperature values read from the temperature channel or temperature input, which are usually stored in [0..1], to a temperature specified in kelvin", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=20000.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumEmissionIntensity(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumEmissionIntensity"
    bl_label = "Black body intensity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_EMISSION_INTENSITY
    octane_pin_name = "emissionIntensity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scales the intensity of the black body emission", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=100.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumTemperatureChannelAutoScale(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumTemperatureChannelAutoScale"
    bl_label = "Auto scale temperature channel"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_TEMPERATURE_CHANNEL_AUTO_SCALE
    octane_pin_name = "temperatureChannelAutoScale"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Scales the temperature values so the maximum value in the channel is mapped to the black body temperature specified in Kelvin")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneStandardVolumeMediumRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumRayMarchStepLength"
    bl_label = "[Deprecated]Volume step length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RAYMARCH_STEP_LENGTH
    octane_pin_name = "rayMarchStepLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 12000000
    octane_end_version = 14000000
    octane_deprecated = True


class OctaneStandardVolumeMediumShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneStandardVolumeMediumShadowRayMarchStepLength"
    bl_label = "[Deprecated]Vol. shadow ray step length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SHADOW_RAY_MARCH_STEP_LENGTH
    octane_pin_name = "shadowRayMarchStepLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 12000000
    octane_end_version = 14000000
    octane_deprecated = True


class OctaneStandardVolumeMediumGroupVolume(OctaneGroupTitleSocket):
    bl_idname = "OctaneStandardVolumeMediumGroupVolume"
    bl_label = "[OctaneGroupTitle]Volume"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Density;Density channel;Interpolation;Volume step %;Vol. shadow ray step %;Use 'Volume step length' for shadow rays;Single scatter amount;Sample position displacement;Volume padding;Volume step length;")


class OctaneStandardVolumeMediumGroupScatter(OctaneGroupTitleSocket):
    bl_idname = "OctaneStandardVolumeMediumGroupScatter"
    bl_label = "[OctaneGroupTitle]Scatter"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Scatter weight;Scatter color;Scatter color channel;Scatter anisotropy;")


class OctaneStandardVolumeMediumGroupTransparency(OctaneGroupTitleSocket):
    bl_idname = "OctaneStandardVolumeMediumGroupTransparency"
    bl_label = "[OctaneGroupTitle]Transparency"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Transparency weight;Transparency depth;Transparency channel;")


class OctaneStandardVolumeMediumGroupEmission(OctaneGroupTitleSocket):
    bl_idname = "OctaneStandardVolumeMediumGroupEmission"
    bl_label = "[OctaneGroupTitle]Emission"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emission mode;Emission weight;Emission color;Emission channel;Light pass ID;")


class OctaneStandardVolumeMediumGroupTemperature(OctaneGroupTitleSocket):
    bl_idname = "OctaneStandardVolumeMediumGroupTemperature"
    bl_label = "[OctaneGroupTitle]Temperature"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Temperature;Temperature channel;Black body kelvin;Black body intensity;Auto scale temperature channel;")


class OctaneStandardVolumeMedium(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneStandardVolumeMedium"
    bl_label = "Standard volume medium"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneStandardVolumeMediumGroupVolume, OctaneStandardVolumeMediumDensity, OctaneStandardVolumeMediumDensityChannel, OctaneStandardVolumeMediumInterpolationType, OctaneStandardVolumeMediumRayMarchStepPercent, OctaneStandardVolumeMediumShadowRayMarchStepPercent, OctaneStandardVolumeMediumUseRayStepLengthForShadowRays, OctaneStandardVolumeMediumSingleScatterFactor, OctaneStandardVolumeMediumDisplacement, OctaneStandardVolumeMediumVolumePadding, OctaneStandardVolumeMediumRayMarchStepLength, OctaneStandardVolumeMediumGroupScatter, OctaneStandardVolumeMediumScatterWeight, OctaneStandardVolumeMediumScatterColor, OctaneStandardVolumeMediumScatterChannel, OctaneStandardVolumeMediumAnisotropy, OctaneStandardVolumeMediumGroupTransparency, OctaneStandardVolumeMediumTransparentWeight, OctaneStandardVolumeMediumTransparentDepth, OctaneStandardVolumeMediumTransparentChannel, OctaneStandardVolumeMediumGroupEmission, OctaneStandardVolumeMediumEmissionType, OctaneStandardVolumeMediumEmissionWeight, OctaneStandardVolumeMediumEmissionColor, OctaneStandardVolumeMediumEmissionChannel, OctaneStandardVolumeMediumLightPassId, OctaneStandardVolumeMediumGroupTemperature, OctaneStandardVolumeMediumTemperatureScale, OctaneStandardVolumeMediumTemperatureChannel, OctaneStandardVolumeMediumTemperature, OctaneStandardVolumeMediumEmissionIntensity, OctaneStandardVolumeMediumTemperatureChannelAutoScale, OctaneStandardVolumeMediumShadowRayMarchStepLength, ]
    octane_min_version = 12000000
    octane_node_type = consts.NodeType.NT_MED_STANDARD_VOLUME
    octane_socket_list = ["Density", "Density channel", "Interpolation", "Volume step %", "Vol. shadow ray step %", "Use 'Volume step length' for shadow rays", "Single scatter amount", "Sample position displacement", "Volume padding", "Scatter weight", "Scatter color", "Scatter color channel", "Scatter anisotropy", "Transparency weight", "Transparency depth", "Transparency channel", "Emission mode", "Emission weight", "Emission color", "Emission channel", "Light pass ID", "Temperature", "Temperature channel", "Black body kelvin", "Black body intensity", "Auto scale temperature channel", "[Deprecated]Volume step length", "[Deprecated]Vol. shadow ray step length", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 26

    compatibility_mode_infos = [
        ("Latest (2024.1)", "Latest (2024.1)", """(null)""", 14000000),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """The volume ray marching step length is an absolute length and the voxel size is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2024.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000002, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneStandardVolumeMediumGroupVolume", OctaneStandardVolumeMediumGroupVolume.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumDensity", OctaneStandardVolumeMediumDensity.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumDensityChannel", OctaneStandardVolumeMediumDensityChannel.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumInterpolationType", OctaneStandardVolumeMediumInterpolationType.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumRayMarchStepPercent", OctaneStandardVolumeMediumRayMarchStepPercent.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumShadowRayMarchStepPercent", OctaneStandardVolumeMediumShadowRayMarchStepPercent.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumUseRayStepLengthForShadowRays", OctaneStandardVolumeMediumUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumSingleScatterFactor", OctaneStandardVolumeMediumSingleScatterFactor.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumDisplacement", OctaneStandardVolumeMediumDisplacement.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumVolumePadding", OctaneStandardVolumeMediumVolumePadding.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumRayMarchStepLength", OctaneStandardVolumeMediumRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumGroupScatter", OctaneStandardVolumeMediumGroupScatter.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumScatterWeight", OctaneStandardVolumeMediumScatterWeight.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumScatterColor", OctaneStandardVolumeMediumScatterColor.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumScatterChannel", OctaneStandardVolumeMediumScatterChannel.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumAnisotropy", OctaneStandardVolumeMediumAnisotropy.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumGroupTransparency", OctaneStandardVolumeMediumGroupTransparency.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTransparentWeight", OctaneStandardVolumeMediumTransparentWeight.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTransparentDepth", OctaneStandardVolumeMediumTransparentDepth.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTransparentChannel", OctaneStandardVolumeMediumTransparentChannel.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumGroupEmission", OctaneStandardVolumeMediumGroupEmission.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumEmissionType", OctaneStandardVolumeMediumEmissionType.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumEmissionWeight", OctaneStandardVolumeMediumEmissionWeight.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumEmissionColor", OctaneStandardVolumeMediumEmissionColor.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumEmissionChannel", OctaneStandardVolumeMediumEmissionChannel.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumLightPassId", OctaneStandardVolumeMediumLightPassId.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumGroupTemperature", OctaneStandardVolumeMediumGroupTemperature.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTemperatureScale", OctaneStandardVolumeMediumTemperatureScale.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTemperatureChannel", OctaneStandardVolumeMediumTemperatureChannel.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTemperature", OctaneStandardVolumeMediumTemperature.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumEmissionIntensity", OctaneStandardVolumeMediumEmissionIntensity.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumTemperatureChannelAutoScale", OctaneStandardVolumeMediumTemperatureChannelAutoScale.bl_label).init()
        self.inputs.new("OctaneStandardVolumeMediumShadowRayMarchStepLength", OctaneStandardVolumeMediumShadowRayMarchStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneStandardVolumeMediumDensity,
    OctaneStandardVolumeMediumDensityChannel,
    OctaneStandardVolumeMediumInterpolationType,
    OctaneStandardVolumeMediumRayMarchStepPercent,
    OctaneStandardVolumeMediumShadowRayMarchStepPercent,
    OctaneStandardVolumeMediumUseRayStepLengthForShadowRays,
    OctaneStandardVolumeMediumSingleScatterFactor,
    OctaneStandardVolumeMediumDisplacement,
    OctaneStandardVolumeMediumVolumePadding,
    OctaneStandardVolumeMediumScatterWeight,
    OctaneStandardVolumeMediumScatterColor,
    OctaneStandardVolumeMediumScatterChannel,
    OctaneStandardVolumeMediumAnisotropy,
    OctaneStandardVolumeMediumTransparentWeight,
    OctaneStandardVolumeMediumTransparentDepth,
    OctaneStandardVolumeMediumTransparentChannel,
    OctaneStandardVolumeMediumEmissionType,
    OctaneStandardVolumeMediumEmissionWeight,
    OctaneStandardVolumeMediumEmissionColor,
    OctaneStandardVolumeMediumEmissionChannel,
    OctaneStandardVolumeMediumLightPassId,
    OctaneStandardVolumeMediumTemperatureScale,
    OctaneStandardVolumeMediumTemperatureChannel,
    OctaneStandardVolumeMediumTemperature,
    OctaneStandardVolumeMediumEmissionIntensity,
    OctaneStandardVolumeMediumTemperatureChannelAutoScale,
    OctaneStandardVolumeMediumRayMarchStepLength,
    OctaneStandardVolumeMediumShadowRayMarchStepLength,
    OctaneStandardVolumeMediumGroupVolume,
    OctaneStandardVolumeMediumGroupScatter,
    OctaneStandardVolumeMediumGroupTransparency,
    OctaneStandardVolumeMediumGroupEmission,
    OctaneStandardVolumeMediumGroupTemperature,
    OctaneStandardVolumeMedium,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
