##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCryptomatteAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteAOVSubType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_SUB_TYPE
    octane_pin_name="subType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Material node", "Material node", "", 0),
        ("Material node name", "Material node name", "", 1),
        ("Material pin name", "Material pin name", "", 2),
        ("Object node", "Object node", "", 3),
        ("Object node name", "Object node name", "", 4),
        ("Object pin name", "Object pin name", "", 5),
        ("Instance", "Instance", "", 6),
        ("Geometry node name", "Geometry node name", "", 7),
        ("Render layer", "Render layer", "", 8),
        ("User instance ID", "User instance ID", "", 9),
    ]
    default_value: EnumProperty(default="Material node", update=OctaneBaseSocket.update_node_tree, description="The type of the Cryptomatte AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCryptomatteAOV"
    bl_label="Cryptomatte AOV"
    bl_width_default=200
    octane_render_pass_id={0: 2006, 1: 2001, 2: 2002, 3: 2004, 4: 2003, 5: 2007, 6: 2005, 7: 2008, 8: 2009, 9: 2010, }
    octane_render_pass_name={0: "Crypto material node", 1: "Crypto material node name", 2: "Crypto material pin name", 3: "Crypto object node", 4: "Crypto object node name", 5: "Crypto object pin name", 6: "Crypto instance ID", 7: "Crypto geometry node name", 8: "Crypto render layer", 9: "Crypto user instance ID", }
    octane_render_pass_short_name={0: "cm-Mn", 1: "cm-Mnn", 2: "cm-MPn", 3: "cm-On", 4: "cm-Onn", 5: "cm-Opn", 6: "cm-Ii", 7: "cm-Gnn", 8: "cm-RL", 9: "cm-UID", }
    octane_render_pass_description={0: "Cryptomatte channels using distinct material nodes. Note: This cannot generate stable matte IDs", 1: "Cryptomatte channels using material node names", 2: "Cryptomatte channels using material pin names", 3: "Cryptomatte channels using distinct object layer nodes. Note: This cannot generate stable matte IDs", 4: "Cryptomatte channels using object layer node names", 5: "Cryptomatte channels using object layer pin names", 6: "Cryptomatte channels for instances. Note: This cannot generate stable matte IDs", 7: "Cryptomatte channels using geometry node names", 8: "Cryptomatte channels using render layers", 9: "Cryptomatte channels using user instance ID", }
    octane_render_pass_sub_type_name="Type"
    octane_socket_class_list=[OctaneCryptomatteAOVEnabled,OctaneCryptomatteAOVSubType,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_CRYPTOMATTE
    octane_socket_list=["Enabled", "Type", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneCryptomatteAOVEnabled", OctaneCryptomatteAOVEnabled.bl_label).init()
        self.inputs.new("OctaneCryptomatteAOVSubType", OctaneCryptomatteAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCryptomatteAOVEnabled,
    OctaneCryptomatteAOVSubType,
    OctaneCryptomatteAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
