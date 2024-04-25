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


class OctaneMixTextureAmount(OctaneBaseSocket):
    bl_idname = "OctaneMixTextureAmount"
    bl_label = "Amount"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_AMOUNT
    octane_pin_name = "amount"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Mix amount", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMixTextureTexture1(OctaneBaseSocket):
    bl_idname = "OctaneMixTextureTexture1"
    bl_label = "First texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE1
    octane_pin_name = "texture1"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMixTextureTexture2(OctaneBaseSocket):
    bl_idname = "OctaneMixTextureTexture2"
    bl_label = "Second texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE2
    octane_pin_name = "texture2"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneMixTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMixTexture"
    bl_label = "Mix texture"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneMixTextureAmount, OctaneMixTextureTexture1, OctaneMixTextureTexture2, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_MIX
    octane_socket_list = ["Amount", "First texture", "Second texture", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneMixTextureAmount", OctaneMixTextureAmount.bl_label).init()
        self.inputs.new("OctaneMixTextureTexture1", OctaneMixTextureTexture1.bl_label).init()
        self.inputs.new("OctaneMixTextureTexture2", OctaneMixTextureTexture2.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneMixTextureAmount,
    OctaneMixTextureTexture1,
    OctaneMixTextureTexture2,
    OctaneMixTexture,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
