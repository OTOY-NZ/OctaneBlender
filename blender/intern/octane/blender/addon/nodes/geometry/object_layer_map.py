##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneObjectLayerMapGeometry(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerMapGeometry"
    bl_label = "Geometry"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneObjectLayerMap(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneObjectLayerMap"
    bl_label = "Object layer map"
    octane_node_type: IntProperty(name="Octane Node Type", default=64)
    octane_socket_list: StringProperty(name="Socket List", default="Geometry;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneObjectLayerMapGeometry", OctaneObjectLayerMapGeometry.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneObjectLayerMapGeometry)
    register_class(OctaneObjectLayerMap)

def unregister():
    unregister_class(OctaneObjectLayerMap)
    unregister_class(OctaneObjectLayerMapGeometry)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
