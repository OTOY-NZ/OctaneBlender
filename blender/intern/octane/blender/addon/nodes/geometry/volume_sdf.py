##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumeSDFMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneVolumeSDFMaterial1"
    bl_label = "Material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeSDFObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneVolumeSDFObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeSDF(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeSDF"
    bl_label = "Volume SDF"
    octane_node_type: IntProperty(name="Octane Node Type", default=134)
    octane_socket_list: StringProperty(name="Socket List", default="Material;Object layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumeSDFMaterial1", OctaneVolumeSDFMaterial1.bl_label)
        self.inputs.new("OctaneVolumeSDFObjectLayer", OctaneVolumeSDFObjectLayer.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneVolumeSDFMaterial1)
    register_class(OctaneVolumeSDFObjectLayer)
    register_class(OctaneVolumeSDF)

def unregister():
    unregister_class(OctaneVolumeSDF)
    unregister_class(OctaneVolumeSDFObjectLayer)
    unregister_class(OctaneVolumeSDFMaterial1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
