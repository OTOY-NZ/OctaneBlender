##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneHagelslagDensity(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagDensity"
    bl_label = "Density"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=713)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="Density", min=1, max=7, soft_min=1, soft_max=7, step=1, subtype="FACTOR")

class OctaneHagelslagRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagRandomSeed"
    bl_label = "Random seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=42, description="Random number seed", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")

class OctaneHagelslagRadius(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagRadius"
    bl_label = "Sprinkle radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.050000, description="Sprinkle radius", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneHagelslagSize(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagSize"
    bl_label = "Sprinkle length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Sprinkle length", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneHagelslagTexture(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagTexture"
    bl_label = "Mask texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Texture map from which to pick sprinkle colors", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneHagelslagTransform(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneHagelslagProjection(OctaneBaseSocket):
    bl_idname = "OctaneHagelslagProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneHagelslag(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneHagelslag"
    bl_label = "Hagelslag"
    octane_node_type: IntProperty(name="Octane Node Type", default=269)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Random seed;Sprinkle radius;Sprinkle length;Mask texture;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneHagelslagDensity", OctaneHagelslagDensity.bl_label)
        self.inputs.new("OctaneHagelslagRandomSeed", OctaneHagelslagRandomSeed.bl_label)
        self.inputs.new("OctaneHagelslagRadius", OctaneHagelslagRadius.bl_label)
        self.inputs.new("OctaneHagelslagSize", OctaneHagelslagSize.bl_label)
        self.inputs.new("OctaneHagelslagTexture", OctaneHagelslagTexture.bl_label)
        self.inputs.new("OctaneHagelslagTransform", OctaneHagelslagTransform.bl_label)
        self.inputs.new("OctaneHagelslagProjection", OctaneHagelslagProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneHagelslagDensity)
    register_class(OctaneHagelslagRandomSeed)
    register_class(OctaneHagelslagRadius)
    register_class(OctaneHagelslagSize)
    register_class(OctaneHagelslagTexture)
    register_class(OctaneHagelslagTransform)
    register_class(OctaneHagelslagProjection)
    register_class(OctaneHagelslag)

def unregister():
    unregister_class(OctaneHagelslag)
    unregister_class(OctaneHagelslagProjection)
    unregister_class(OctaneHagelslagTransform)
    unregister_class(OctaneHagelslagTexture)
    unregister_class(OctaneHagelslagSize)
    unregister_class(OctaneHagelslagRadius)
    unregister_class(OctaneHagelslagRandomSeed)
    unregister_class(OctaneHagelslagDensity)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
