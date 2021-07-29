##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePlaneUvTransform(OctaneBaseSocket):
    bl_idname = "OctanePlaneUvTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=362)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlaneGroundColor(OctaneBaseSocket):
    bl_idname = "OctanePlaneGroundColor"
    bl_label = "Plane material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=331)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlaneObjectLayer(OctaneBaseSocket):
    bl_idname = "OctanePlaneObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePlane(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePlane"
    bl_label = "Plane"
    octane_node_type: IntProperty(name="Octane Node Type", default=110)
    octane_socket_list: StringProperty(name="Socket List", default="UV transform;Plane material;Object layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePlaneUvTransform", OctanePlaneUvTransform.bl_label)
        self.inputs.new("OctanePlaneGroundColor", OctanePlaneGroundColor.bl_label)
        self.inputs.new("OctanePlaneObjectLayer", OctanePlaneObjectLayer.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctanePlaneUvTransform)
    register_class(OctanePlaneGroundColor)
    register_class(OctanePlaneObjectLayer)
    register_class(OctanePlane)

def unregister():
    unregister_class(OctanePlane)
    unregister_class(OctanePlaneObjectLayer)
    unregister_class(OctanePlaneGroundColor)
    unregister_class(OctanePlaneUvTransform)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
