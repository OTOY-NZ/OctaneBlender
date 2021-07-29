##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneLightDirectAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneLightDirectAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneLightDirectAOVSubType(OctaneBaseSocket):
    bl_idname = "OctaneLightDirectAOVSubType"
    bl_label = "ID"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Sun", "Sun", "", 0),
        ("Environment", "Environment", "", 1),
        ("Light ID 1", "Light ID 1", "", 2),
        ("Light ID 2", "Light ID 2", "", 3),
        ("Light ID 3", "Light ID 3", "", 4),
        ("Light ID 4", "Light ID 4", "", 5),
        ("Light ID 5", "Light ID 5", "", 6),
        ("Light ID 6", "Light ID 6", "", 7),
        ("Light ID 7", "Light ID 7", "", 8),
        ("Light ID 8", "Light ID 8", "", 9),
    ]
    default_value: EnumProperty(default="Light ID 1", description="The ID of the direct light AOV", items=items)

class OctaneLightDirectAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneLightDirectAOV"
    bl_label = "Light direct AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=206)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneLightDirectAOVEnabled", OctaneLightDirectAOVEnabled.bl_label)
        self.inputs.new("OctaneLightDirectAOVSubType", OctaneLightDirectAOVSubType.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneLightDirectAOVEnabled)
    register_class(OctaneLightDirectAOVSubType)
    register_class(OctaneLightDirectAOV)

def unregister():
    unregister_class(OctaneLightDirectAOV)
    unregister_class(OctaneLightDirectAOVSubType)
    unregister_class(OctaneLightDirectAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
