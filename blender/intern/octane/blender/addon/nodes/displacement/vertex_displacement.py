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


class OctaneVertexDisplacementTexture(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementTexture"
    bl_label = "Texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_TEXTURE
    octane_pin_name = "texture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementAmount(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementAmount"
    bl_label = "Height"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AMOUNT
    octane_pin_name = "amount"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The displacement height in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementBlackLevel(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementBlackLevel"
    bl_label = "Mid level"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_BLACK_LEVEL
    octane_pin_name = "black_level"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The value in the image which corresponds to zero displacement.The range is always normalized to [0, 1]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementDisplacementMapType(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementDisplacementMapType"
    bl_label = "Map type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_DISPLACEMENT_MAP_TYPE
    octane_pin_name = "displacementMapType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Vector", "Vector", "", 0),
        ("Height", "Height", "", 1),
    ]
    default_value: EnumProperty(default="Height", update=OctaneBaseSocket.update_node_tree, description="The displacement map input type. For height map we displace in object normal direction and for vector maps, please refer vector space and input axes pins", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementTextureSpace(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementTextureSpace"
    bl_label = "Vector space"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_TEXTURE_SPACE
    octane_pin_name = "textureSpace"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Object", "Object", "", 0),
        ("Tangent", "Tangent", "", 1),
    ]
    default_value: EnumProperty(default="Object", update=OctaneBaseSocket.update_node_tree, description="The vector displacement map space. Only valid if the displacement map type is a vector. For tangent space vector map. R is along the tangent, Y is along the normal and Z is along the BiTangent. For object space please refer input axes pin", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementInputAxes(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementInputAxes"
    bl_label = "Input axes"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_INPUT_AXES
    octane_pin_name = "inputAxes"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("+X,+Y,+Z", "+X,+Y,+Z", "", 0),
        ("+X,+Z,+Y", "+X,+Z,+Y", "", 1),
        ("+X,+Y,-Z", "+X,+Y,-Z", "", 2),
    ]
    default_value: EnumProperty(default="+X,+Y,+Z", update=OctaneBaseSocket.update_node_tree, description="This setting is valid only for object space vector maps. The input axes provide us information about how to interpret RGB data. The selected axes are then converted to Octane XYZ space during displacement", items=items)
    octane_hide_value = False
    octane_min_version = 11000500
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementBump(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementBump"
    bl_label = "Auto bump map"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_BUMP
    octane_pin_name = "bump"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to get fine details of the displacement map on a lower subdivision level")
    octane_hide_value = False
    octane_min_version = 5100002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacementSubdLevel(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementSubdLevel"
    bl_label = "Subdivision level"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_SUBD_LEVEL
    octane_pin_name = "subdLevel"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The subdivision level applied to polygons using this material. This overrides the subdivision level set in the geometry preferences. Other subdivision settings have to be set in the geometry preference dialog. If a level higher than 6 is needed, please enter it manually", min=0, max=10, soft_min=0, soft_max=6, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneVertexDisplacement(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVertexDisplacement"
    bl_label = "Vertex displacement"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneVertexDisplacementTexture, OctaneVertexDisplacementAmount, OctaneVertexDisplacementBlackLevel, OctaneVertexDisplacementDisplacementMapType, OctaneVertexDisplacementTextureSpace, OctaneVertexDisplacementInputAxes, OctaneVertexDisplacementBump, OctaneVertexDisplacementSubdLevel, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_VERTEX_DISPLACEMENT
    octane_socket_list = ["Texture", "Height", "Mid level", "Map type", "Vector space", "Input axes", "Auto bump map", "Subdivision level", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 8

    compatibility_mode_infos = [
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000005),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for worldspace projection affecting auto bump map texture.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000007, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneVertexDisplacementTexture", OctaneVertexDisplacementTexture.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementAmount", OctaneVertexDisplacementAmount.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementBlackLevel", OctaneVertexDisplacementBlackLevel.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementDisplacementMapType", OctaneVertexDisplacementDisplacementMapType.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementTextureSpace", OctaneVertexDisplacementTextureSpace.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementInputAxes", OctaneVertexDisplacementInputAxes.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementBump", OctaneVertexDisplacementBump.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementSubdLevel", OctaneVertexDisplacementSubdLevel.bl_label).init()
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneVertexDisplacementTexture,
    OctaneVertexDisplacementAmount,
    OctaneVertexDisplacementBlackLevel,
    OctaneVertexDisplacementDisplacementMapType,
    OctaneVertexDisplacementTextureSpace,
    OctaneVertexDisplacementInputAxes,
    OctaneVertexDisplacementBump,
    OctaneVertexDisplacementSubdLevel,
    OctaneVertexDisplacement,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
