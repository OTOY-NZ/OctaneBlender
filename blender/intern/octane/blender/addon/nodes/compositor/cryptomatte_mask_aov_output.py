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


class OctaneCryptomatteMaskAOVOutputCryptomatteType(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteMaskAOVOutputCryptomatteType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_TYPE
    octane_pin_name="cryptomatteType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
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
    default_value: EnumProperty(default="Material node", update=OctaneBaseSocket.update_node_tree, description="The type of cryptomatte render AOV from which to extract mattes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteMaskAOVOutputCryptomatteMattes(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteMaskAOVOutputCryptomatteMattes"
    bl_label="Mattes"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_MATTES
    octane_pin_name="cryptomatteMattes"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="List of selected matte names, one per line.\n\nSome characters have special meaning:\n    * is a wildcard that matches any sequence of characters.\n    - at the start of a line excludes any mattes matched by that line.\n    ? on a line by itself matches mattes with blank names.\n    \ prevents the next character being treated as a special character.\n\nBlank lines are ignored. When a matte name is included by one line and excluded by another, whichever line comes last takes precedence. For example,\n    Car_*\n    -*dirt*\n    Car_wheel_dirt\nwill include \"Car_windows\" and \"Car_wheel_dirt\", but not \"Ground\" or \"Car_door_dirt\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteMaskAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCryptomatteMaskAOVOutput"
    bl_label="Cryptomatte mask output AOV"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCryptomatteMaskAOVOutputCryptomatteType,OctaneCryptomatteMaskAOVOutputCryptomatteMattes,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_CRYPTOMATTE_MASK
    octane_socket_list=["Type", "Mattes", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneCryptomatteMaskAOVOutputCryptomatteType", OctaneCryptomatteMaskAOVOutputCryptomatteType.bl_label).init()
        self.inputs.new("OctaneCryptomatteMaskAOVOutputCryptomatteMattes", OctaneCryptomatteMaskAOVOutputCryptomatteMattes.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCryptomatteMaskAOVOutputCryptomatteType,
    OctaneCryptomatteMaskAOVOutputCryptomatteMattes,
    OctaneCryptomatteMaskAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneCryptomatteMaskAOVOutput_Override(OctaneCryptomatteMaskAOVOutput):

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.column().operator("octane.cryptomatte_picker_add_matte", icon="ADD", text="")
        row.column().operator("octane.cryptomatte_picker_remove_matte", icon="REMOVE", text="")


utility.override_class(_CLASSES, OctaneCryptomatteMaskAOVOutput, OctaneCryptomatteMaskAOVOutput_Override)