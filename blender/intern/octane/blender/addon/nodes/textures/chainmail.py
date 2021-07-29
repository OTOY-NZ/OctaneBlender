##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneChainmailRadius(OctaneBaseSocket):
    bl_idname = "OctaneChainmailRadius"
    bl_label = "Ring radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.470000, description="Ring radius", min=0.000000, max=2.000000, soft_min=0.000000, soft_max=2.000000, step=1, subtype="FACTOR")

class OctaneChainmailLineWidth(OctaneBaseSocket):
    bl_idname = "OctaneChainmailLineWidth"
    bl_label = "Ring width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=714)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.080000, description="Ring width", min=0.000000, max=0.200000, soft_min=0.000000, soft_max=0.200000, step=1, subtype="FACTOR")

class OctaneChainmailTransform(OctaneBaseSocket):
    bl_idname = "OctaneChainmailTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneChainmailProjection(OctaneBaseSocket):
    bl_idname = "OctaneChainmailProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneChainmail(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneChainmail"
    bl_label = "Chainmail"
    octane_node_type: IntProperty(name="Octane Node Type", default=263)
    octane_socket_list: StringProperty(name="Socket List", default="Ring radius;Ring width;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneChainmailRadius", OctaneChainmailRadius.bl_label)
        self.inputs.new("OctaneChainmailLineWidth", OctaneChainmailLineWidth.bl_label)
        self.inputs.new("OctaneChainmailTransform", OctaneChainmailTransform.bl_label)
        self.inputs.new("OctaneChainmailProjection", OctaneChainmailProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneChainmailRadius)
    register_class(OctaneChainmailLineWidth)
    register_class(OctaneChainmailTransform)
    register_class(OctaneChainmailProjection)
    register_class(OctaneChainmail)

def unregister():
    unregister_class(OctaneChainmail)
    unregister_class(OctaneChainmailProjection)
    unregister_class(OctaneChainmailTransform)
    unregister_class(OctaneChainmailLineWidth)
    unregister_class(OctaneChainmailRadius)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
