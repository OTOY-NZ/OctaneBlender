##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumeToTextureGeometry(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureGeometry"
    bl_label = "VDB"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeToTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeToTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeToTextureGrid(OctaneBaseSocket):
    bl_idname = "OctaneVolumeToTextureGrid"
    bl_label = "Grid ID"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=705)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Scatter", "Scatter", "", 1),
        ("Absorption", "Absorption", "", 2),
        ("Emission", "Emission", "", 3),
        ("Velocity X", "Velocity X", "", 4),
        ("Velocity Y", "Velocity Y", "", 5),
        ("Velocity Z", "Velocity Z", "", 6),
    ]
    default_value: EnumProperty(default="Scatter", description="Which grid to read from the VDB", items=items)

class OctaneVolumeToTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeToTexture"
    bl_label = "Volume to texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=256)
    octane_socket_list: StringProperty(name="Socket List", default="VDB;UVW transform;Projection;Grid ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumeToTextureGeometry", OctaneVolumeToTextureGeometry.bl_label)
        self.inputs.new("OctaneVolumeToTextureTransform", OctaneVolumeToTextureTransform.bl_label)
        self.inputs.new("OctaneVolumeToTextureProjection", OctaneVolumeToTextureProjection.bl_label)
        self.inputs.new("OctaneVolumeToTextureGrid", OctaneVolumeToTextureGrid.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneVolumeToTextureGeometry)
    register_class(OctaneVolumeToTextureTransform)
    register_class(OctaneVolumeToTextureProjection)
    register_class(OctaneVolumeToTextureGrid)
    register_class(OctaneVolumeToTexture)

def unregister():
    unregister_class(OctaneVolumeToTexture)
    unregister_class(OctaneVolumeToTextureGrid)
    unregister_class(OctaneVolumeToTextureProjection)
    unregister_class(OctaneVolumeToTextureTransform)
    unregister_class(OctaneVolumeToTextureGeometry)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
