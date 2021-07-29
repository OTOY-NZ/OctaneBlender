##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneZDepthAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneZDepthAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneZDepthAOVZDepthMax(OctaneBaseSocket):
    bl_idname = "OctaneZDepthAOVZDepthMax"
    bl_label = "Maximum Z-depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=257)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=5.000000, description="The maximum Z-depth value. Background pixels will get this value and and any foreground depths will be clamped at this value. This applies with or without tone mapping, but tone mapping will map the maximum Z-depth to white (0 is mapped to black)", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, subtype="FACTOR")

class OctaneZDepthAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneZDepthAOV"
    bl_label = "Z-depth AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=255)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Maximum Z-depth;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneZDepthAOVEnabled", OctaneZDepthAOVEnabled.bl_label)
        self.inputs.new("OctaneZDepthAOVZDepthMax", OctaneZDepthAOVZDepthMax.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneZDepthAOVEnabled)
    register_class(OctaneZDepthAOVZDepthMax)
    register_class(OctaneZDepthAOV)

def unregister():
    unregister_class(OctaneZDepthAOV)
    unregister_class(OctaneZDepthAOVZDepthMax)
    unregister_class(OctaneZDepthAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
