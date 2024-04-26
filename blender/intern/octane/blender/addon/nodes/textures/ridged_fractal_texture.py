# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneRidgedFractalTexturePower(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTexturePower"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOffset"
    bl_label = "Ridge height"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OFFSET
    octane_pin_name = "offset"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="Ridge height", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTextureOctaves(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOctaves"
    bl_label = "Octaves"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_OCTAVES
    octane_pin_name = "octaves"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=0, max=16, soft_min=0, soft_max=16, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTextureOmega(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureOmega"
    bl_label = "Omega"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_OMEGA
    octane_pin_name = "omega"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Difference per interval", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTextureLacunarity(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureLacunarity"
    bl_label = "Lacunarity"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_LACUNARITY
    octane_pin_name = "lacunarity"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Noise frequency scale factor per interval", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTextureTransform(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureTransform"
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


class OctaneRidgedFractalTextureProjection(OctaneBaseSocket):
    bl_idname = "OctaneRidgedFractalTextureProjection"
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
    octane_min_version = 1210000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneRidgedFractalTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRidgedFractalTexture"
    bl_label = "Ridged fractal texture"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneRidgedFractalTexturePower, OctaneRidgedFractalTextureOffset, OctaneRidgedFractalTextureOctaves, OctaneRidgedFractalTextureOmega, OctaneRidgedFractalTextureLacunarity, OctaneRidgedFractalTextureTransform, OctaneRidgedFractalTextureProjection, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_RGFRACTAL
    octane_socket_list = ["Power", "Ridge height", "Octaves", "Omega", "Lacunarity", "UVW transform", "Projection", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneRidgedFractalTexturePower", OctaneRidgedFractalTexturePower.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureOffset", OctaneRidgedFractalTextureOffset.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureOctaves", OctaneRidgedFractalTextureOctaves.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureOmega", OctaneRidgedFractalTextureOmega.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureLacunarity", OctaneRidgedFractalTextureLacunarity.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureTransform", OctaneRidgedFractalTextureTransform.bl_label).init()
        self.inputs.new("OctaneRidgedFractalTextureProjection", OctaneRidgedFractalTextureProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneRidgedFractalTexturePower,
    OctaneRidgedFractalTextureOffset,
    OctaneRidgedFractalTextureOctaves,
    OctaneRidgedFractalTextureOmega,
    OctaneRidgedFractalTextureLacunarity,
    OctaneRidgedFractalTextureTransform,
    OctaneRidgedFractalTextureProjection,
    OctaneRidgedFractalTexture,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
