##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneWCoordinateTranslation(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateTranslation"
    bl_label = "Translation"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneWCoordinateScale(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateScale"
    bl_label = "Scale"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Scale", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneWCoordinateBorderModeWCoord(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateBorderModeWCoord"
    bl_label = "Border mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=699)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 0),
        ("Wrap around", "Wrap around", "", 1),
        ("Mirror", "Mirror", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="None", description="Determines the lookup behavior when the W coordinate falls outside of [0,1]", items=items)

class OctaneWCoordinateInvert(OctaneBaseSocket):
    bl_idname = "OctaneWCoordinateInvert"
    bl_label = "Invert"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert")

class OctaneWCoordinate(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneWCoordinate"
    bl_label = "W coordinate"
    octane_node_type: IntProperty(name="Octane Node Type", default=104)
    octane_socket_list: StringProperty(name="Socket List", default="Translation;Scale;Border mode;Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneWCoordinateTranslation", OctaneWCoordinateTranslation.bl_label)
        self.inputs.new("OctaneWCoordinateScale", OctaneWCoordinateScale.bl_label)
        self.inputs.new("OctaneWCoordinateBorderModeWCoord", OctaneWCoordinateBorderModeWCoord.bl_label)
        self.inputs.new("OctaneWCoordinateInvert", OctaneWCoordinateInvert.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneWCoordinateTranslation)
    register_class(OctaneWCoordinateScale)
    register_class(OctaneWCoordinateBorderModeWCoord)
    register_class(OctaneWCoordinateInvert)
    register_class(OctaneWCoordinate)

def unregister():
    unregister_class(OctaneWCoordinate)
    unregister_class(OctaneWCoordinateInvert)
    unregister_class(OctaneWCoordinateBorderModeWCoord)
    unregister_class(OctaneWCoordinateScale)
    unregister_class(OctaneWCoordinateTranslation)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
