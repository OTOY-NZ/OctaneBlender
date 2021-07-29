##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCustomAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneCustomAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneCustomAOVSubType(OctaneBaseSocket):
    bl_idname = "OctaneCustomAOVSubType"
    bl_label = "ID"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Custom 1", "Custom 1", "", 0),
        ("Custom 2", "Custom 2", "", 1),
        ("Custom 3", "Custom 3", "", 2),
        ("Custom 4", "Custom 4", "", 3),
        ("Custom 5", "Custom 5", "", 4),
        ("Custom 6", "Custom 6", "", 5),
        ("Custom 7", "Custom 7", "", 6),
        ("Custom 8", "Custom 8", "", 7),
        ("Custom 9", "Custom 9", "", 8),
        ("Custom 10", "Custom 10", "", 9),
    ]
    default_value: EnumProperty(default="Custom 1", description="The ID or index of the custom AOV", items=items)

class OctaneCustomAOVSecondaryRays(OctaneBaseSocket):
    bl_idname = "OctaneCustomAOVSecondaryRays"
    bl_label = "Visible after"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=631)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None - primary rays only", "None - primary rays only", "", 0),
        ("Reflections", "Reflections", "", 1),
        ("Refractions", "Refractions", "", 2),
        ("Reflections and refractions", "Reflections and refractions", "", 3),
    ]
    default_value: EnumProperty(default="None - primary rays only", description="Determines whether secondary bounces should contribute to the custom AOV or not", items=items)

class OctaneCustomAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCustomAOV"
    bl_label = "Custom AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=186)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;Visible after;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCustomAOVEnabled", OctaneCustomAOVEnabled.bl_label)
        self.inputs.new("OctaneCustomAOVSubType", OctaneCustomAOVSubType.bl_label)
        self.inputs.new("OctaneCustomAOVSecondaryRays", OctaneCustomAOVSecondaryRays.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneCustomAOVEnabled)
    register_class(OctaneCustomAOVSubType)
    register_class(OctaneCustomAOVSecondaryRays)
    register_class(OctaneCustomAOV)

def unregister():
    unregister_class(OctaneCustomAOV)
    unregister_class(OctaneCustomAOVSecondaryRays)
    unregister_class(OctaneCustomAOVSubType)
    unregister_class(OctaneCustomAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
