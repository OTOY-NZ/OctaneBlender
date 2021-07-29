##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCryptomatteAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneCryptomatteAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneCryptomatteAOVSubType(OctaneBaseSocket):
    bl_idname = "OctaneCryptomatteAOVSubType"
    bl_label = "Type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Material node", "Material node", "", 0),
        ("Material node name", "Material node name", "", 1),
        ("Material pin name", "Material pin name", "", 2),
        ("Object node", "Object node", "", 3),
        ("Object node name", "Object node name", "", 4),
        ("Object pin name", "Object pin name", "", 5),
        ("Instance", "Instance", "", 6),
    ]
    default_value: EnumProperty(default="Material node", description="The type of the Cryptomatte AOV", items=items)

class OctaneCryptomatteAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCryptomatteAOV"
    bl_label = "Cryptomatte AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=185)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Type;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCryptomatteAOVEnabled", OctaneCryptomatteAOVEnabled.bl_label)
        self.inputs.new("OctaneCryptomatteAOVSubType", OctaneCryptomatteAOVSubType.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneCryptomatteAOVEnabled)
    register_class(OctaneCryptomatteAOVSubType)
    register_class(OctaneCryptomatteAOV)

def unregister():
    unregister_class(OctaneCryptomatteAOV)
    unregister_class(OctaneCryptomatteAOVSubType)
    unregister_class(OctaneCryptomatteAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
