# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneCinema4DNoisePower(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoisePower"
    bl_label = "Power"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_POWER
    octane_pin_name = "power"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000014
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseNoiseType(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseNoiseType"
    bl_label = "Noise type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_NOISE_TYPE
    octane_pin_name = "noiseType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Box", "Box", "", 0),
        ("Blistered Turbulence", "Blistered Turbulence", "", 1),
        ("Buya", "Buya", "", 2),
        ("Cell Noise", "Cell Noise", "", 3),
        ("Cranal", "Cranal", "", 4),
        ("Dents", "Dents", "", 5),
        ("Displaced Turbulence", "Displaced Turbulence", "", 6),
        ("FBM", "FBM", "", 7),
        ("Hama", "Hama", "", 8),
        ("Luka", "Luka", "", 9),
        ("Mod Noise", "Mod Noise", "", 10),
        ("Naki", "Naki", "", 11),
        ("Noise", "Noise", "", 12),
        ("Nutous", "Nutous", "", 13),
        ("Ober", "Ober", "", 14),
        ("Pezo", "Pezo", "", 15),
        ("Poxo", "Poxo", "", 16),
        ("Sema", "Sema", "", 17),
        ("Stupl", "Stupl", "", 18),
        ("Turbulence", "Turbulence", "", 19),
        ("VL Noise", "VL Noise", "", 20),
        ("Wavy Turbulence", "Wavy Turbulence", "", 21),
        ("Cell Voronoi", "Cell Voronoi", "", 22),
        ("Displaced Voronoi", "Displaced Voronoi", "", 23),
        ("Voronoi 1", "Voronoi 1", "", 24),
        ("Voronoi 2", "Voronoi 2", "", 25),
        ("Voronoi 3", "Voronoi 3", "", 26),
        ("Zada", "Zada", "", 27),
        ("Fire", "Fire", "", 28),
        ("Electric", "Electric", "", 29),
        ("Gaseous", "Gaseous", "", 30),
        ("Ridged Multi Fractal", "Ridged Multi Fractal", "", 31),
    ]
    default_value: EnumProperty(default="Box", update=OctaneBaseSocket.update_node_tree, description="Noise type (Cinema4dNoiseType)", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseOctaves(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseOctaves"
    bl_label = "Octaves"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_OCTAVES
    octane_pin_name = "octaves"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=0.000000, max=15.000000, soft_min=0.000000, soft_max=15.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseLacunarity(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseLacunarity"
    bl_label = "Lacunarity"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_LACUNARITY
    octane_pin_name = "lacunarity"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.100000, update=OctaneBaseSocket.update_node_tree, description="Lacunarity", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseGain(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseGain"
    bl_label = "Gain"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GAIN
    octane_pin_name = "gain"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.250000, update=OctaneBaseSocket.update_node_tree, description="Gain", min=-10.000000, max=10.000000, soft_min=-10.000000, soft_max=10.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseTransform(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseTransform"
    bl_label = "UVW transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseProjection(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name = "OctaneXYZToUVW"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseTime(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseTime"
    bl_label = "T"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TIME
    octane_pin_name = "time"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="4th dimension input", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseAbsolute(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseAbsolute"
    bl_label = "Absolute"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ABSOLUTE
    octane_pin_name = "absolute"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Absolute")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseUse4d(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseUse4d"
    bl_label = "Use 4D noise"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_4D
    octane_pin_name = "use4d"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Switch between 2D and 4D noise")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseSampleRadius(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseSampleRadius"
    bl_label = "Sample radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SAMPLE_RADIUS
    octane_pin_name = "sampleRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Sample radius", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoiseRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneCinema4DNoiseRandomSeed"
    bl_label = "Random seed"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_RANDOM_SEED
    octane_pin_name = "randomSeed"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Seed for noise", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCinema4DNoise(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCinema4DNoise"
    bl_label = "Cinema 4D noise"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneCinema4DNoisePower, OctaneCinema4DNoiseNoiseType, OctaneCinema4DNoiseOctaves, OctaneCinema4DNoiseLacunarity, OctaneCinema4DNoiseGain, OctaneCinema4DNoiseTransform, OctaneCinema4DNoiseProjection, OctaneCinema4DNoiseTime, OctaneCinema4DNoiseAbsolute, OctaneCinema4DNoiseUse4d, OctaneCinema4DNoiseSampleRadius, OctaneCinema4DNoiseRandomSeed, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_C4D_NOISE
    octane_socket_list = ["Power", "Noise type", "Octaves", "Lacunarity", "Gain", "UVW transform", "Projection", "T", "Absolute", "Use 4D noise", "Sample radius", "Random seed", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 12

    def init(self, context):  # noqa
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

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
