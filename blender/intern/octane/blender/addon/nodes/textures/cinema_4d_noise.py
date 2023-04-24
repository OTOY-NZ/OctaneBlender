##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCinema4DNoisePower(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoisePower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="power")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000014
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseNoiseType(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseNoiseType"
    bl_label="Noise type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=117)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="noiseType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="BoxNoise", update=OctaneBaseSocket.update_node_tree, description="Noise type (Cinema4dNoiseType)", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseOctaves(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="octaves")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=0.000000, max=15.000000, soft_min=0.000000, soft_max=15.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseLacunarity(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseLacunarity"
    bl_label="Lacunarity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=90)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="lacunarity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.100000, update=OctaneBaseSocket.update_node_tree, description="Lacunarity", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseGain(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseGain"
    bl_label="Gain"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=568)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="gain")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.250000, update=OctaneBaseSocket.update_node_tree, description="Gain", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseTransform(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=67
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transform")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseProjection(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=75
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="projection")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseTime(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseTime"
    bl_label="T"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="time")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="4th dimension input", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseAbsolute(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseAbsolute"
    bl_label="Absolute"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=567)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="absolute")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Absolute")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseUse4d(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseUse4d"
    bl_label="Use 4D noise"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=570)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="use4d")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Switch between 2D and 4D noise")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseSampleRadius(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseSampleRadius"
    bl_label="Sample radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=569)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sampleRadius")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Sample radius", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoiseRandomSeed(OctaneBaseSocket):
    bl_idname="OctaneCinema4DNoiseRandomSeed"
    bl_label="Random seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="randomSeed")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Seed for noise", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCinema4DNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCinema4DNoise"
    bl_label="Cinema 4D noise"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=162)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Noise type;Octaves;Lacunarity;Gain;UVW transform;Projection;T;Absolute;Use 4D noise;Sample radius;Random seed;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=12)

    def init(self, context):
        self.inputs.new("OctaneCinema4DNoisePower", OctaneCinema4DNoisePower.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseNoiseType", OctaneCinema4DNoiseNoiseType.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseOctaves", OctaneCinema4DNoiseOctaves.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseLacunarity", OctaneCinema4DNoiseLacunarity.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseGain", OctaneCinema4DNoiseGain.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseTransform", OctaneCinema4DNoiseTransform.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseProjection", OctaneCinema4DNoiseProjection.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseTime", OctaneCinema4DNoiseTime.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseAbsolute", OctaneCinema4DNoiseAbsolute.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseUse4d", OctaneCinema4DNoiseUse4d.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseSampleRadius", OctaneCinema4DNoiseSampleRadius.bl_label).init()
        self.inputs.new("OctaneCinema4DNoiseRandomSeed", OctaneCinema4DNoiseRandomSeed.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneCinema4DNoisePower,
    OctaneCinema4DNoiseNoiseType,
    OctaneCinema4DNoiseOctaves,
    OctaneCinema4DNoiseLacunarity,
    OctaneCinema4DNoiseGain,
    OctaneCinema4DNoiseTransform,
    OctaneCinema4DNoiseProjection,
    OctaneCinema4DNoiseTime,
    OctaneCinema4DNoiseAbsolute,
    OctaneCinema4DNoiseUse4d,
    OctaneCinema4DNoiseSampleRadius,
    OctaneCinema4DNoiseRandomSeed,
    OctaneCinema4DNoise,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
