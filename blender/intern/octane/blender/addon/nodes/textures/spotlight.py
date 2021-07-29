##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSpotlightOrientation(OctaneBaseSocket):
    bl_idname = "OctaneSpotlightOrientation"
    bl_label = "Orientation"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=126)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Surface normal", "Surface normal", "", 1),
        ("Direction - world space", "Direction - world space", "", 2),
        ("Direction - object space", "Direction - object space", "", 3),
        ("Target point - world space", "Target point - world space", "", 4),
        ("Target point - object space", "Target point - object space", "", 5),
    ]
    default_value: EnumProperty(default="Direction - object space", description="Main axis for the emission cone", items=items)

class OctaneSpotlightTarget(OctaneBaseSocket):
    bl_idname = "OctaneSpotlightTarget"
    bl_label = "Direction or target"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, -1.000000, 0.000000), description="Specify the direction or target point. Ignored if orientation is set to surface normal", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneSpotlightConeAngle(OctaneBaseSocket):
    bl_idname = "OctaneSpotlightConeAngle"
    bl_label = "Cone angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=562)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=60.000000, description="Width of the cone angle in degrees", min=0.000000, max=180.000000, soft_min=0.000000, soft_max=180.000000, step=10, subtype="FACTOR")

class OctaneSpotlightHardness(OctaneBaseSocket):
    bl_idname = "OctaneSpotlightHardness"
    bl_label = "Hardness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=563)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="Controls how abruptly the emission pattern falls of at the edge", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSpotlightNormalize(OctaneBaseSocket):
    bl_idname = "OctaneSpotlightNormalize"
    bl_label = "Normalize power"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Keep the emitted power constant if the angle changes")

class OctaneSpotlight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSpotlight"
    bl_label = "Spotlight"
    octane_node_type: IntProperty(name="Octane Node Type", default=158)
    octane_socket_list: StringProperty(name="Socket List", default="Orientation;Direction or target;Cone angle;Hardness;Normalize power;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSpotlightOrientation", OctaneSpotlightOrientation.bl_label)
        self.inputs.new("OctaneSpotlightTarget", OctaneSpotlightTarget.bl_label)
        self.inputs.new("OctaneSpotlightConeAngle", OctaneSpotlightConeAngle.bl_label)
        self.inputs.new("OctaneSpotlightHardness", OctaneSpotlightHardness.bl_label)
        self.inputs.new("OctaneSpotlightNormalize", OctaneSpotlightNormalize.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneSpotlightOrientation)
    register_class(OctaneSpotlightTarget)
    register_class(OctaneSpotlightConeAngle)
    register_class(OctaneSpotlightHardness)
    register_class(OctaneSpotlightNormalize)
    register_class(OctaneSpotlight)

def unregister():
    unregister_class(OctaneSpotlight)
    unregister_class(OctaneSpotlightNormalize)
    unregister_class(OctaneSpotlightHardness)
    unregister_class(OctaneSpotlightConeAngle)
    unregister_class(OctaneSpotlightTarget)
    unregister_class(OctaneSpotlightOrientation)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
