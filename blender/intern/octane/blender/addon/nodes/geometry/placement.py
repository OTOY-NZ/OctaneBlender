##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePlacementTransform(OctaneBaseSocket):
    bl_idname = "OctanePlacementTransform"
    bl_label = "Transformation"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlacementGeometry(OctaneBaseSocket):
    bl_idname = "OctanePlacementGeometry"
    bl_label = "Geometry"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlacement(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePlacement"
    bl_label = "Placement"
    octane_node_type: IntProperty(name="Octane Node Type", default=4)
    octane_socket_list: StringProperty(name="Socket List", default="Transformation;Geometry;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePlacementTransform", OctanePlacementTransform.bl_label)
        self.inputs.new("OctanePlacementGeometry", OctanePlacementGeometry.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctanePlacementTransform)
    register_class(OctanePlacementGeometry)
    register_class(OctanePlacement)

def unregister():
    unregister_class(OctanePlacement)
    unregister_class(OctanePlacementGeometry)
    unregister_class(OctanePlacementTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
