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


class OctaneSDFSubtractSize(OctaneBaseSocket):
    bl_idname = "OctaneSDFSubtractSize"
    bl_label = "Bounds"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SIZE
    octane_pin_name = "size"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(10.000000, 10.000000, 10.000000), update=OctaneBaseSocket.update_node_tree, description="Bounds of the geometry in meters", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 12000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFSubtractInput1(OctaneBaseSocket):
    bl_idname = "OctaneSDFSubtractInput1"
    bl_label = "Input 1"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_INPUT1
    octane_pin_name = "input1"
    octane_pin_type = consts.PinType.PT_GEOMETRY
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFSubtractInput2(OctaneBaseSocket):
    bl_idname = "OctaneSDFSubtractInput2"
    bl_label = "Input 2"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_INPUT2
    octane_pin_name = "input2"
    octane_pin_type = consts.PinType.PT_GEOMETRY
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFSubtractRadius(OctaneBaseSocket):
    bl_idname = "OctaneSDFSubtractRadius"
    bl_label = "Radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RADIUS
    octane_pin_name = "radius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 12000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFSubtractTransferMaterial(OctaneBaseSocket):
    bl_idname = "OctaneSDFSubtractTransferMaterial"
    bl_label = "Transfer material"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_TRANSFER_MATERIAL
    octane_pin_name = "transferMaterial"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value = False
    octane_min_version = 12000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFSubtract(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSDFSubtract"
    bl_label = "Subtract"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSDFSubtractSize, OctaneSDFSubtractInput1, OctaneSDFSubtractInput2, OctaneSDFSubtractRadius, OctaneSDFSubtractTransferMaterial, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_GEO_SDF_SUBTRACT
    octane_socket_list = ["Bounds", "Input 1", "Input 2", "Radius", "Transfer material", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 5

    def init(self, context):  # noqa
        self.inputs.new("OctaneSDFSubtractSize", OctaneSDFSubtractSize.bl_label).init()
        self.inputs.new("OctaneSDFSubtractInput1", OctaneSDFSubtractInput1.bl_label).init()
        self.inputs.new("OctaneSDFSubtractInput2", OctaneSDFSubtractInput2.bl_label).init()
        self.inputs.new("OctaneSDFSubtractRadius", OctaneSDFSubtractRadius.bl_label).init()
        self.inputs.new("OctaneSDFSubtractTransferMaterial", OctaneSDFSubtractTransferMaterial.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSDFSubtractSize,
    OctaneSDFSubtractInput1,
    OctaneSDFSubtractInput2,
    OctaneSDFSubtractRadius,
    OctaneSDFSubtractTransferMaterial,
    OctaneSDFSubtract,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
