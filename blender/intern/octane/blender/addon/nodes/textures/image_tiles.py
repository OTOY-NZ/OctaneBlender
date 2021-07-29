##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneImageTilesPower(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesPower"
    bl_label = "Power"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneImageTilesColorSpace(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesColorSpace"
    bl_label = "Color space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=36)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneImageTilesGamma(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesGamma"
    bl_label = "Legacy gamma"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Gamma value. Only used when the color space is set to 'Linear sRGB + legacy gamma'", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneImageTilesInvert(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert image")

class OctaneImageTilesLinearSpaceInvert(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesLinearSpaceInvert"
    bl_label = "Linear sRGB invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Invert image after conversion to the linear sRGB color space, not before")

class OctaneImageTilesTransform(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneImageTilesProjection(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneImageTilesEmptyTileColor(OctaneBaseSocket):
    bl_idname = "OctaneImageTilesEmptyTileColor"
    bl_label = "Empty tile color"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=441)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Color to use if no image is loaded for a tile", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneImageTiles(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneImageTiles"
    bl_label = "Image tiles"
    octane_node_type: IntProperty(name="Octane Node Type", default=131)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Color space;Legacy gamma;Invert;Linear sRGB invert;UV transform;Projection;Empty tile color;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneImageTilesPower", OctaneImageTilesPower.bl_label)
        self.inputs.new("OctaneImageTilesColorSpace", OctaneImageTilesColorSpace.bl_label)
        self.inputs.new("OctaneImageTilesGamma", OctaneImageTilesGamma.bl_label)
        self.inputs.new("OctaneImageTilesInvert", OctaneImageTilesInvert.bl_label)
        self.inputs.new("OctaneImageTilesLinearSpaceInvert", OctaneImageTilesLinearSpaceInvert.bl_label)
        self.inputs.new("OctaneImageTilesTransform", OctaneImageTilesTransform.bl_label)
        self.inputs.new("OctaneImageTilesProjection", OctaneImageTilesProjection.bl_label)
        self.inputs.new("OctaneImageTilesEmptyTileColor", OctaneImageTilesEmptyTileColor.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneImageTilesPower)
    register_class(OctaneImageTilesColorSpace)
    register_class(OctaneImageTilesGamma)
    register_class(OctaneImageTilesInvert)
    register_class(OctaneImageTilesLinearSpaceInvert)
    register_class(OctaneImageTilesTransform)
    register_class(OctaneImageTilesProjection)
    register_class(OctaneImageTilesEmptyTileColor)
    register_class(OctaneImageTiles)

def unregister():
    unregister_class(OctaneImageTiles)
    unregister_class(OctaneImageTilesEmptyTileColor)
    unregister_class(OctaneImageTilesProjection)
    unregister_class(OctaneImageTilesTransform)
    unregister_class(OctaneImageTilesLinearSpaceInvert)
    unregister_class(OctaneImageTilesInvert)
    unregister_class(OctaneImageTilesGamma)
    unregister_class(OctaneImageTilesColorSpace)
    unregister_class(OctaneImageTilesPower)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
