##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCinema4DNoiseNoiseType(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseNoiseType"
    bl_label = "Noise type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=117)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("BoxNoise", "BoxNoise", "", 0),
        ("BlistTurb", "BlistTurb", "", 1),
        ("Buya", "Buya", "", 2),
        ("CellNoise", "CellNoise", "", 3),
        ("Cranal", "Cranal", "", 4),
        ("Dents", "Dents", "", 5),
        ("DisplTurb", "DisplTurb", "", 6),
        ("Fbm", "Fbm", "", 7),
        ("Hama", "Hama", "", 8),
        ("Luka", "Luka", "", 9),
        ("ModNoise", "ModNoise", "", 10),
        ("Naki", "Naki", "", 11),
        ("Noise", "Noise", "", 12),
        ("Nutous", "Nutous", "", 13),
        ("Ober", "Ober", "", 14),
        ("Pezo", "Pezo", "", 15),
        ("Poxo", "Poxo", "", 16),
        ("Sema", "Sema", "", 17),
        ("Stupl", "Stupl", "", 18),
        ("Turbulence", "Turbulence", "", 19),
        ("VlNoise", "VlNoise", "", 20),
        ("WavyTurb", "WavyTurb", "", 21),
        ("CellVoronoi", "CellVoronoi", "", 22),
        ("DisplVoronoi", "DisplVoronoi", "", 23),
        ("Voronoi1", "Voronoi1", "", 24),
        ("Voronoi2", "Voronoi2", "", 25),
        ("Voronoi3", "Voronoi3", "", 26),
        ("Zada", "Zada", "", 27),
        ("Fire", "Fire", "", 28),
        ("Electric", "Electric", "", 29),
        ("Gaseous", "Gaseous", "", 30),
        ("Ridgedmulti", "Ridgedmulti", "", 31),
    ]
    default_value: EnumProperty(default="BoxNoise", description="Noise type (Cinema4dNoiseType)", items=items)

class OctaneCinema4DNoiseOctaves(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseOctaves"
    bl_label = "Octaves"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=5.000000, description="Number of octaves", min=0.000000, max=15.000000, soft_min=0.000000, soft_max=15.000000, step=1, subtype="FACTOR")

class OctaneCinema4DNoiseLacunarity(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseLacunarity"
    bl_label = "Lacunarity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=90)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=2.100000, description="Lacunarity", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneCinema4DNoiseGain(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseGain"
    bl_label = "Gain"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.250000, description="Gain", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneCinema4DNoiseTransform(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseTransform"
    bl_label = "UVW transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneCinema4DNoiseProjection(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneCinema4DNoiseTime(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseTime"
    bl_label = "T"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="4th dimension input", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneCinema4DNoiseAbsolute(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseAbsolute"
    bl_label = "Absolute"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=567)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Absolute")

class OctaneCinema4DNoiseUse4d(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseUse4d"
    bl_label = "Use 4D noise"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=570)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Switch between 2D and 4D noise")

class OctaneCinema4DNoiseSampleRadius(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseSampleRadius"
    bl_label = "Sample radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=569)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Sample radius", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneCinema4DNoiseRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseRandomSeed"
    bl_label = "Random seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Seed for noise", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")

class OctaneCinema4DNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCinema4DNoise"
    bl_label = "Cinema 4D noise"
    octane_node_type: IntProperty(name="Octane Node Type", default=162)
    octane_socket_list: StringProperty(name="Socket List", default="Noise type;Octaves;Lacunarity;Gain;UVW transform;Projection;T;Absolute;Use 4D noise;Sample radius;Random seed;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCinema4DNoiseNoiseType", OctaneCinema4DNoiseNoiseType.bl_label)
        self.inputs.new("OctaneCinema4DNoiseOctaves", OctaneCinema4DNoiseOctaves.bl_label)
        self.inputs.new("OctaneCinema4DNoiseLacunarity", OctaneCinema4DNoiseLacunarity.bl_label)
        self.inputs.new("OctaneCinema4DNoiseGain", OctaneCinema4DNoiseGain.bl_label)
        self.inputs.new("OctaneCinema4DNoiseTransform", OctaneCinema4DNoiseTransform.bl_label)
        self.inputs.new("OctaneCinema4DNoiseProjection", OctaneCinema4DNoiseProjection.bl_label)
        self.inputs.new("OctaneCinema4DNoiseTime", OctaneCinema4DNoiseTime.bl_label)
        self.inputs.new("OctaneCinema4DNoiseAbsolute", OctaneCinema4DNoiseAbsolute.bl_label)
        self.inputs.new("OctaneCinema4DNoiseUse4d", OctaneCinema4DNoiseUse4d.bl_label)
        self.inputs.new("OctaneCinema4DNoiseSampleRadius", OctaneCinema4DNoiseSampleRadius.bl_label)
        self.inputs.new("OctaneCinema4DNoiseRandomSeed", OctaneCinema4DNoiseRandomSeed.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneCinema4DNoiseNoiseType)
    register_class(OctaneCinema4DNoiseOctaves)
    register_class(OctaneCinema4DNoiseLacunarity)
    register_class(OctaneCinema4DNoiseGain)
    register_class(OctaneCinema4DNoiseTransform)
    register_class(OctaneCinema4DNoiseProjection)
    register_class(OctaneCinema4DNoiseTime)
    register_class(OctaneCinema4DNoiseAbsolute)
    register_class(OctaneCinema4DNoiseUse4d)
    register_class(OctaneCinema4DNoiseSampleRadius)
    register_class(OctaneCinema4DNoiseRandomSeed)
    register_class(OctaneCinema4DNoise)

def unregister():
    unregister_class(OctaneCinema4DNoise)
    unregister_class(OctaneCinema4DNoiseRandomSeed)
    unregister_class(OctaneCinema4DNoiseSampleRadius)
    unregister_class(OctaneCinema4DNoiseUse4d)
    unregister_class(OctaneCinema4DNoiseAbsolute)
    unregister_class(OctaneCinema4DNoiseTime)
    unregister_class(OctaneCinema4DNoiseProjection)
    unregister_class(OctaneCinema4DNoiseTransform)
    unregister_class(OctaneCinema4DNoiseGain)
    unregister_class(OctaneCinema4DNoiseLacunarity)
    unregister_class(OctaneCinema4DNoiseOctaves)
    unregister_class(OctaneCinema4DNoiseNoiseType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
