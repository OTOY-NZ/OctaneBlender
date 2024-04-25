# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneWavePatternAxis(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternAxis"
    bl_label = "Axis"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_AXIS
    octane_pin_name = "axis"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("X", "X", "", 0),
        ("Y", "Y", "", 1),
        ("Z", "Z", "", 2),
    ]
    default_value: EnumProperty(default="X", update=OctaneBaseSocket.update_node_tree, description="The coordinate axis along which the wave undulates", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternShape(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternShape"
    bl_label = "Shape"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_SHAPE
    octane_pin_name = "shape"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Sine", "Sine", "", 0),
        ("Square", "Square", "", 1),
        ("Saw", "Saw", "", 2),
    ]
    default_value: EnumProperty(default="Sine", update=OctaneBaseSocket.update_node_tree, description="The waveform", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternAmplitude(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternAmplitude"
    bl_label = "Amplitude"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AMPLITUDE
    octane_pin_name = "amplitude"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternAmplitudeShift(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternAmplitudeShift"
    bl_label = "Amplitude shift"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AMPLITUDE_SHIFT
    octane_pin_name = "amplitudeShift"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternTexture1(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternTexture1"
    bl_label = "Color 1"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE1
    octane_pin_name = "texture1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.800000, 0.200000, 0.200000), update=OctaneBaseSocket.update_node_tree, description="First texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternTexture2(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternTexture2"
    bl_label = "Color 2"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE2
    octane_pin_name = "texture2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.200000, 0.200000, 0.800000), update=OctaneBaseSocket.update_node_tree, description="Second texture input", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternTransform(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternTransform"
    bl_label = "UVW transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePatternProjection(OctaneBaseSocket):
    bl_idname = "OctaneWavePatternProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name = "OctaneXYZToUVW"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneWavePattern(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneWavePattern"
    bl_label = "Wave pattern"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneWavePatternAxis, OctaneWavePatternShape, OctaneWavePatternAmplitude, OctaneWavePatternAmplitudeShift, OctaneWavePatternTexture1, OctaneWavePatternTexture2, OctaneWavePatternTransform, OctaneWavePatternProjection, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_WAVE_PATTERN
    octane_socket_list = ["Axis", "Shape", "Amplitude", "Amplitude shift", "Color 1", "Color 2", "UVW transform", "Projection", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 8

    def init(self, context):  # noqa
        self.inputs.new("OctaneWavePatternAxis", OctaneWavePatternAxis.bl_label).init()
        self.inputs.new("OctaneWavePatternShape", OctaneWavePatternShape.bl_label).init()
        self.inputs.new("OctaneWavePatternAmplitude", OctaneWavePatternAmplitude.bl_label).init()
        self.inputs.new("OctaneWavePatternAmplitudeShift", OctaneWavePatternAmplitudeShift.bl_label).init()
        self.inputs.new("OctaneWavePatternTexture1", OctaneWavePatternTexture1.bl_label).init()
        self.inputs.new("OctaneWavePatternTexture2", OctaneWavePatternTexture2.bl_label).init()
        self.inputs.new("OctaneWavePatternTransform", OctaneWavePatternTransform.bl_label).init()
        self.inputs.new("OctaneWavePatternProjection", OctaneWavePatternProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneWavePatternAxis,
    OctaneWavePatternShape,
    OctaneWavePatternAmplitude,
    OctaneWavePatternAmplitudeShift,
    OctaneWavePatternTexture1,
    OctaneWavePatternTexture2,
    OctaneWavePatternTransform,
    OctaneWavePatternProjection,
    OctaneWavePattern,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
