##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumeMedium(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMedium"
    bl_label = "Volume medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneVolumeObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolume(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolume"
    bl_label = "Volume"
    octane_node_type: IntProperty(name="Octane Node Type", default=91)
    octane_socket_list: StringProperty(name="Socket List", default="Volume medium;Object layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumeMedium", OctaneVolumeMedium.bl_label)
        self.inputs.new("OctaneVolumeObjectLayer", OctaneVolumeObjectLayer.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneVolumeMedium)
    register_class(OctaneVolumeObjectLayer)
    register_class(OctaneVolume)

def unregister():
    unregister_class(OctaneVolume)
    unregister_class(OctaneVolumeObjectLayer)
    unregister_class(OctaneVolumeMedium)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
