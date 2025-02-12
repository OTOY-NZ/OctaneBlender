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


class OctaneDistortedMeshUVRotation(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVRotation"
    bl_label = "Rotation"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ROTATION
    octane_pin_name = "rotation"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Amount of rotation applied to the UV, normalized to the rotation range.\nA value of 0 rotates the UV by the minimum value in the range, a value of 1 rotates the UV by the maximum value in the range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUVRotationRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVRotationRange"
    bl_label = "Rotation range"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ROTATION_RANGE
    octane_pin_name = "rotationRange"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 360.000000), update=OctaneBaseSocket.update_node_tree, description="Range of rotation, in degrees", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUVScale(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVScale"
    bl_label = "Scale"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_SCALE
    octane_pin_name = "scale"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Amount of scaling applied to the UV, normalized to the scale range.\nA value of 0 scales the UV by the minimum value in the range, a value of 1 scales the UV by the maximum value in the range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUVScaleRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVScaleRange"
    bl_label = "Scale range"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SCALE_RANGE
    octane_pin_name = "scaleRange"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 10.000000), update=OctaneBaseSocket.update_node_tree, description="Range of scaling", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1.000000, subtype="NONE", precision=3, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUVTranslation(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVTranslation"
    bl_label = "Translation"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TRANSLATION
    octane_pin_name = "translation"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Amount of translation applied to the UV, normalized to the translation range.\nA value of 0 translates the UV by the minimum value in the range, a value of 1 translates the UV by the maximum value in the range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUVTranslationRange(OctaneBaseSocket):
    bl_idname = "OctaneDistortedMeshUVTranslationRange"
    bl_label = "Translation range"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TRANSLATION_RANGE
    octane_pin_name = "translationRange"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Range of translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneDistortedMeshUV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDistortedMeshUV"
    bl_label = "Distorted mesh UV Projection"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneDistortedMeshUVRotation, OctaneDistortedMeshUVRotationRange, OctaneDistortedMeshUVScale, OctaneDistortedMeshUVScaleRange, OctaneDistortedMeshUVTranslation, OctaneDistortedMeshUVTranslationRange, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_PROJ_DISTORTED_MESH_UV
    octane_socket_list = ["Rotation", "Rotation range", "Scale", "Scale range", "Translation", "Translation range", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 6

    def init(self, context):  # noqa
        self.inputs.new("OctaneDistortedMeshUVRotation", OctaneDistortedMeshUVRotation.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVRotationRange", OctaneDistortedMeshUVRotationRange.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVScale", OctaneDistortedMeshUVScale.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVScaleRange", OctaneDistortedMeshUVScaleRange.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVTranslation", OctaneDistortedMeshUVTranslation.bl_label).init()
        self.inputs.new("OctaneDistortedMeshUVTranslationRange", OctaneDistortedMeshUVTranslationRange.bl_label).init()
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneDistortedMeshUVRotation,
    OctaneDistortedMeshUVRotationRange,
    OctaneDistortedMeshUVScale,
    OctaneDistortedMeshUVScaleRange,
    OctaneDistortedMeshUVTranslation,
    OctaneDistortedMeshUVTranslationRange,
    OctaneDistortedMeshUV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
