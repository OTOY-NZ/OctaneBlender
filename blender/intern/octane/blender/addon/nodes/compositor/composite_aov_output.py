##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCompositeAOVOutputImager(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputImager"
    bl_label = "Enable imager"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, The imager settings is applied on the final AOV output. Otherwise ignored  Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")

class OctaneCompositeAOVOutputPostproc(OctaneBaseSocket):
    bl_idname = "OctaneCompositeAOVOutputPostproc"
    bl_label = "Enable post processing"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, The post processing settings is applied on the final AOV output. Otherwise ignored Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")

class OctaneCompositeAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCompositeAOVOutput"
    bl_label = "Composite AOV output"
    octane_node_type: IntProperty(name="Octane Node Type", default=166)
    octane_socket_list: StringProperty(name="Socket List", default="Enable imager;Enable post processing;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCompositeAOVOutputImager", OctaneCompositeAOVOutputImager.bl_label)
        self.inputs.new("OctaneCompositeAOVOutputPostproc", OctaneCompositeAOVOutputPostproc.bl_label)
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out")


def register():
    register_class(OctaneCompositeAOVOutputImager)
    register_class(OctaneCompositeAOVOutputPostproc)
    register_class(OctaneCompositeAOVOutput)

def unregister():
    unregister_class(OctaneCompositeAOVOutput)
    unregister_class(OctaneCompositeAOVOutputPostproc)
    unregister_class(OctaneCompositeAOVOutputImager)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
