##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneShadowAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneShadowAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneShadowAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneShadowAOV"
    bl_label = "Shadow AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=237)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneShadowAOVEnabled", OctaneShadowAOVEnabled.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneShadowAOVEnabled)
    register_class(OctaneShadowAOV)

def unregister():
    unregister_class(OctaneShadowAOV)
    unregister_class(OctaneShadowAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
