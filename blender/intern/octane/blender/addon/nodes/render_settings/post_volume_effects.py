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


class OctanePostVolumeEffectsPostFxLightBeamsEnabled(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxLightBeamsEnabled"
    bl_label = "Light beams"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_POSTFX_LIGHT_BEAMS_ENABLED
    octane_pin_name = "postFxLightBeamsEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables postfx light beams for all configured light sources in the scene")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxLightBeamsMediumDensity(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxLightBeamsMediumDensity"
    bl_label = "Medium density for postfx light beams"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_LIGHT_BEAMS_MEDIUM_DENSITY
    octane_pin_name = "postFxLightBeamsMediumDensity"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Medium density for postfx light beams", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogMediaEnabled(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogMediaEnabled"
    bl_label = "Fog"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_MEDIA_ENABLED
    octane_pin_name = "postFxFogMediaEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables postfx fog")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogExtinctionDistance(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogExtinctionDistance"
    bl_label = "Fog extinction distance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_EXTINCTION_DISTANCE
    octane_pin_name = "postFxFogExtinctionDistance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1000.000000, update=OctaneBaseSocket.update_node_tree, description="The distance where the primary ray's transmittance becomes 0 due to fog's density accumulation", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogBaseLevel(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogBaseLevel"
    bl_label = "Fog base level"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_BASE_LEVEL
    octane_pin_name = "postFxFogBaseLevel"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Base height in world space for post fog effects", min=-10000.000000, max=10000.000000, soft_min=-10000.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogHalfDensityHeight(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogHalfDensityHeight"
    bl_label = "Fog half density height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_HALF_DENSITY_HEIGHT
    octane_pin_name = "postFxFogHalfDensityHeight"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The height from the base level where post fog density halves", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogEnvContribution(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogEnvContribution"
    bl_label = "Fog environment contribution"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_ENV_CONTRIBUTION
    octane_pin_name = "postFxFogEnvContribution"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Controls how strong fog color is contributed from environment with a base of user selected color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsBaseColor(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsBaseColor"
    bl_label = "Base fog color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_BASE_COLOR
    octane_pin_name = "baseColor"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The base color for fog contribution", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsMediumRadius(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsMediumRadius"
    bl_label = "Medium radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_MEDIUM_RADIUS
    octane_pin_name = "mediumRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the post volume. The post volume acts as a sphere around the camera position with the specified radius", min=0.000100, max=100000.000000, soft_min=0.000100, soft_max=100000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePostVolumeEffectsPostFxFogStrength(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogStrength"
    bl_label = "[Deprecated]Fog strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_STRENGTH
    octane_pin_name = "postFxFogStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Fog strength. Only effective when postfx media option is true", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 13000007
    octane_deprecated = True


class OctanePostVolumeEffectsPostFxFogExponent(OctaneBaseSocket):
    bl_idname = "OctanePostVolumeEffectsPostFxFogExponent"
    bl_label = "[Deprecated]Fog height descend"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_POSTFX_FOG_EXPONENT
    octane_pin_name = "postFxFogExponent"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.050000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Fog height descending factor. Only effective when postfx media option is true", min=0.010000, max=10.000000, soft_min=0.010000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 13000000
    octane_end_version = 13000007
    octane_deprecated = True


class OctanePostVolumeEffects(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePostVolumeEffects"
    bl_label = "Post volume effects"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctanePostVolumeEffectsPostFxLightBeamsEnabled, OctanePostVolumeEffectsPostFxLightBeamsMediumDensity, OctanePostVolumeEffectsPostFxFogMediaEnabled, OctanePostVolumeEffectsPostFxFogExtinctionDistance, OctanePostVolumeEffectsPostFxFogBaseLevel, OctanePostVolumeEffectsPostFxFogHalfDensityHeight, OctanePostVolumeEffectsPostFxFogEnvContribution, OctanePostVolumeEffectsBaseColor, OctanePostVolumeEffectsMediumRadius, OctanePostVolumeEffectsPostFxFogStrength, OctanePostVolumeEffectsPostFxFogExponent, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_POST_VOLUME
    octane_socket_list = ["Light beams", "Medium density for postfx light beams", "Fog", "Fog extinction distance", "Fog base level", "Fog half density height", "Fog environment contribution", "Base fog color", "Medium radius", "[Deprecated]Fog strength", "[Deprecated]Fog height descend", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 9

    compatibility_mode_infos = [
        ("Latest (2024.1)", "Latest (2024.1)", """(null)""", 14000008),
        ("2023.1 compatibility mode", "2023.1 compatibility mode", """Incorrect alpha compositing is used for post volume effects. Fog base color is interpreted in the XYZ color space (with E white point), not linear sRGB.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2024.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000009, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctanePostVolumeEffectsPostFxLightBeamsEnabled", OctanePostVolumeEffectsPostFxLightBeamsEnabled.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxLightBeamsMediumDensity", OctanePostVolumeEffectsPostFxLightBeamsMediumDensity.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogMediaEnabled", OctanePostVolumeEffectsPostFxFogMediaEnabled.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogExtinctionDistance", OctanePostVolumeEffectsPostFxFogExtinctionDistance.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogBaseLevel", OctanePostVolumeEffectsPostFxFogBaseLevel.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogHalfDensityHeight", OctanePostVolumeEffectsPostFxFogHalfDensityHeight.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogEnvContribution", OctanePostVolumeEffectsPostFxFogEnvContribution.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsBaseColor", OctanePostVolumeEffectsBaseColor.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsMediumRadius", OctanePostVolumeEffectsMediumRadius.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogStrength", OctanePostVolumeEffectsPostFxFogStrength.bl_label).init()
        self.inputs.new("OctanePostVolumeEffectsPostFxFogExponent", OctanePostVolumeEffectsPostFxFogExponent.bl_label).init()
        self.outputs.new("OctanePostVolumeOutSocket", "Post volume out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctanePostVolumeEffectsPostFxLightBeamsEnabled,
    OctanePostVolumeEffectsPostFxLightBeamsMediumDensity,
    OctanePostVolumeEffectsPostFxFogMediaEnabled,
    OctanePostVolumeEffectsPostFxFogExtinctionDistance,
    OctanePostVolumeEffectsPostFxFogBaseLevel,
    OctanePostVolumeEffectsPostFxFogHalfDensityHeight,
    OctanePostVolumeEffectsPostFxFogEnvContribution,
    OctanePostVolumeEffectsBaseColor,
    OctanePostVolumeEffectsMediumRadius,
    OctanePostVolumeEffectsPostFxFogStrength,
    OctanePostVolumeEffectsPostFxFogExponent,
    OctanePostVolumeEffects,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
