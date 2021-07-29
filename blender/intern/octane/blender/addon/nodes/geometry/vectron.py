##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVectronMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneVectronMaterial1"
    bl_label = "Geometry material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVectronSize(OctaneBaseSocket):
    bl_idname = "OctaneVectronSize"
    bl_label = "Bounds"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(10.000000, 10.000000, 10.000000), description="Bounds of the geometry in meters", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneVectron(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVectron"
    bl_label = "Vectron"
    octane_node_type: IntProperty(name="Octane Node Type", default=133)
    octane_socket_list: StringProperty(name="Socket List", default="Geometry material;Bounds;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVectronMaterial1", OctaneVectronMaterial1.bl_label)
        self.inputs.new("OctaneVectronSize", OctaneVectronSize.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneVectronMaterial1)
    register_class(OctaneVectronSize)
    register_class(OctaneVectron)

def unregister():
    unregister_class(OctaneVectron)
    unregister_class(OctaneVectronSize)
    unregister_class(OctaneVectronMaterial1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
