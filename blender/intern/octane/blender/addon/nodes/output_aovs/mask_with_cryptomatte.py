##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsMaskWithCryptomatteEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithCryptomatteEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsMaskWithCryptomatteCryptomatteType(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithCryptomatteCryptomatteType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_TYPE
    octane_pin_name="cryptomatteType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Material node", "Material node", "", 2006),
        ("Material node name", "Material node name", "", 2001),
        ("Material pin name", "Material pin name", "", 2002),
        ("Object node", "Object node", "", 2004),
        ("Object node name", "Object node name", "", 2003),
        ("Object pin name", "Object pin name", "", 2007),
        ("Instance", "Instance", "", 2005),
        ("Geometry node name", "Geometry node name", "", 2008),
        ("Render layer", "Render layer", "", 2009),
        ("User instance ID", "User instance ID", "", 2010),
    ]
    default_value: EnumProperty(default="Material node", update=OctaneBaseSocket.update_node_tree, description="The type of Cryptomatte render AOV from which to extract mattes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes"
    bl_label="Mattes"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_MATTES
    octane_pin_name="cryptomatteMattes"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="List of selected matte names, one per line.\n\nSome characters have special meaning:\n    * is a wildcard that matches any sequence of characters.\n    - at the start of a line excludes any mattes matched by that line.\n    ? on a line by itself matches mattes with blank names.\n    \ prevents the next character being treated as a special character.\n\nBlank lines are ignored. When a matte name is included by one line and excluded by another, whichever line comes last takes precedence. For example,\n    Car_*\n    -*dirt*\n    Car_wheel_dirt\nwill include \"Car_windows\" and \"Car_wheel_dirt\", but not \"Ground\" or \"Car_door_dirt\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly"
    bl_label="Affect occlusion only"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_AFFECT_OCCLUSION_ONLY
    octane_pin_name="affectOcclusionOnly"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, scale only the alpha channel, to control how much the image blocks light from beneath it without changing how much additional light the image contributes. If disabled, scale the (premultiplied) RGB channels too, to also control how much additional light the image contributes.\n\nThis should be disabled for a normal/SDR image masking scenario where the image is thought of as a colored sheet with an alpha mask, and enabled for an emissive/HDR image where occlusion (alpha) and emission (RGB) are considered separately")
    octane_hide_value=False
    octane_min_version=13000200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsMaskWithCryptomatte(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsMaskWithCryptomatte"
    bl_label="Mask with Cryptomatte"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsMaskWithCryptomatteEnabled,OctaneOutputAOVsMaskWithCryptomatteCryptomatteType,OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes,OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_MASK_WITH_CRYPTOMATTE
    octane_socket_list=["Enabled", "Type", "Mattes", "Affect occlusion only", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsMaskWithCryptomatteEnabled", OctaneOutputAOVsMaskWithCryptomatteEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsMaskWithCryptomatteCryptomatteType", OctaneOutputAOVsMaskWithCryptomatteCryptomatteType.bl_label).init()
        self.inputs.new("OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes", OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes.bl_label).init()
        self.inputs.new("OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly", OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsMaskWithCryptomatteEnabled,
    OctaneOutputAOVsMaskWithCryptomatteCryptomatteType,
    OctaneOutputAOVsMaskWithCryptomatteCryptomatteMattes,
    OctaneOutputAOVsMaskWithCryptomatteAffectOcclusionOnly,
    OctaneOutputAOVsMaskWithCryptomatte,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneOutputAOVsMaskWithCryptomatte_Override(OctaneOutputAOVsMaskWithCryptomatte):

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.column().operator("octane.cryptomatte_picker_add_matte", icon="ADD", text="")
        row.column().operator("octane.cryptomatte_picker_remove_matte", icon="REMOVE", text="")

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        socket = self.inputs["Mattes"]
        mattes =  socket.default_value
        mattes = mattes.replace(";", "\n")
        octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, socket.octane_pin_index, socket.octane_pin_name, socket.octane_socket_type, socket.octane_pin_type, socket.octane_default_node_type, False, "", mattes)

utility.override_class(_CLASSES, OctaneOutputAOVsMaskWithCryptomatte, OctaneOutputAOVsMaskWithCryptomatte_Override)