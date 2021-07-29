##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMotionVectorAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneMotionVectorAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneMotionVectorAOVMaxSpeed(OctaneBaseSocket):
    bl_idname = "OctaneMotionVectorAOVMaxSpeed"
    bl_label = "Max speed"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=109)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Upper limit of the motion vector which will become 1, when the motion vector pass is imaged. The unit of the motion vector is pixels", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneMotionVectorAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMotionVectorAOV"
    bl_label = "Motion vector AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=211)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Max speed;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMotionVectorAOVEnabled", OctaneMotionVectorAOVEnabled.bl_label)
        self.inputs.new("OctaneMotionVectorAOVMaxSpeed", OctaneMotionVectorAOVMaxSpeed.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneMotionVectorAOVEnabled)
    register_class(OctaneMotionVectorAOVMaxSpeed)
    register_class(OctaneMotionVectorAOV)

def unregister():
    unregister_class(OctaneMotionVectorAOV)
    unregister_class(OctaneMotionVectorAOVMaxSpeed)
    unregister_class(OctaneMotionVectorAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
