##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCryptomatteAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteAOVSubType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Material node", "Material node", "", 0),
        ("Material node name", "Material node name", "", 1),
        ("Material pin name", "Material pin name", "", 2),
        ("Object node", "Object node", "", 3),
        ("Object node name", "Object node name", "", 4),
        ("Object pin name", "Object pin name", "", 5),
        ("Instance", "Instance", "", 6),
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
    octane_render_pass_id={0: 2006, 1: 2001, 2: 2002, 3: 2004, 4: 2003, 5: 2007, 6: 2005, }
    octane_render_pass_name={0: "Crypto material node", 1: "Crypto material node name", 2: "Crypto material pin name", 3: "Crypto object node", 4: "Crypto object node name", 5: "Crypto object pin name", 6: "Crypto instance ID", }
    octane_render_pass_short_name={0: "cm-Mn", 1: "cm-Mnn", 2: "cm-MPn", 3: "cm-On", 4: "cm-Onn", 5: "cm-Opn", 6: "cm-Ii", }
    octane_render_pass_description={0: "Cryptomatte channels using distinct material nodes. Note: This cannot generate stable matte IDs", 1: "Cryptomatte channels using material node names", 2: "Cryptomatte channels using material pin names", 3: "Cryptomatte channels using distinct object layer nodes. Note: This cannot generate stable matte IDs", 4: "Cryptomatte channels using object layer node names", 5: "Cryptomatte channels using object layer pin names", 6: "Cryptomatte channels for instances. Note: This cannot generate stable matte IDs", }
    octane_render_pass_sub_type_name="Type"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=185)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Type;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneCryptomatteAOVEnabled", OctaneCryptomatteAOVEnabled.bl_label).init()
        self.inputs.new("OctaneCryptomatteAOVSubType", OctaneCryptomatteAOVSubType.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneCryptomatteAOVEnabled,
    OctaneCryptomatteAOVSubType,
    OctaneCryptomatteAOV,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
