##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTriplanarMapBlendAngle(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapBlendAngle"
    bl_label = "Blend angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=345)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=5.000000, description="The angle on an edge to linearly blend two adjacent textures", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctaneTriplanarMapPositionType(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapPositionType"
    bl_label = "Coordinate space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=135)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
    ]
    default_value: EnumProperty(default="Object space", description="Coordinate space used when blending. ", items=items)

class OctaneTriplanarMapTransform(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTransform"
    bl_label = "Blend cube transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneTriplanarMapTexturePosX(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTexturePosX"
    bl_label = "Positive X axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=339)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMapTextureNegX(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTextureNegX"
    bl_label = "Negative X axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=342)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMapTexturePosY(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTexturePosY"
    bl_label = "Positive Y axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=340)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMapTextureNegY(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTextureNegY"
    bl_label = "Negative Y axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=343)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMapTexturePosZ(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTexturePosZ"
    bl_label = "Positive Z axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=341)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMapTextureNegZ(OctaneBaseSocket):
    bl_idname = "OctaneTriplanarMapTextureNegZ"
    bl_label = "Negative Z axis texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=344)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTriplanarMap(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTriplanarMap"
    bl_label = "Triplanar map"
    octane_node_type: IntProperty(name="Octane Node Type", default=109)
    octane_socket_list: StringProperty(name="Socket List", default="Blend angle;Coordinate space;Blend cube transform;Positive X axis texture;Negative X axis texture;Positive Y axis texture;Negative Y axis texture;Positive Z axis texture;Negative Z axis texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTriplanarMapBlendAngle", OctaneTriplanarMapBlendAngle.bl_label)
        self.inputs.new("OctaneTriplanarMapPositionType", OctaneTriplanarMapPositionType.bl_label)
        self.inputs.new("OctaneTriplanarMapTransform", OctaneTriplanarMapTransform.bl_label)
        self.inputs.new("OctaneTriplanarMapTexturePosX", OctaneTriplanarMapTexturePosX.bl_label)
        self.inputs.new("OctaneTriplanarMapTextureNegX", OctaneTriplanarMapTextureNegX.bl_label)
        self.inputs.new("OctaneTriplanarMapTexturePosY", OctaneTriplanarMapTexturePosY.bl_label)
        self.inputs.new("OctaneTriplanarMapTextureNegY", OctaneTriplanarMapTextureNegY.bl_label)
        self.inputs.new("OctaneTriplanarMapTexturePosZ", OctaneTriplanarMapTexturePosZ.bl_label)
        self.inputs.new("OctaneTriplanarMapTextureNegZ", OctaneTriplanarMapTextureNegZ.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneTriplanarMapBlendAngle)
    register_class(OctaneTriplanarMapPositionType)
    register_class(OctaneTriplanarMapTransform)
    register_class(OctaneTriplanarMapTexturePosX)
    register_class(OctaneTriplanarMapTextureNegX)
    register_class(OctaneTriplanarMapTexturePosY)
    register_class(OctaneTriplanarMapTextureNegY)
    register_class(OctaneTriplanarMapTexturePosZ)
    register_class(OctaneTriplanarMapTextureNegZ)
    register_class(OctaneTriplanarMap)

def unregister():
    unregister_class(OctaneTriplanarMap)
    unregister_class(OctaneTriplanarMapTextureNegZ)
    unregister_class(OctaneTriplanarMapTexturePosZ)
    unregister_class(OctaneTriplanarMapTextureNegY)
    unregister_class(OctaneTriplanarMapTexturePosY)
    unregister_class(OctaneTriplanarMapTextureNegX)
    unregister_class(OctaneTriplanarMapTexturePosX)
    unregister_class(OctaneTriplanarMapTransform)
    unregister_class(OctaneTriplanarMapPositionType)
    unregister_class(OctaneTriplanarMapBlendAngle)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
