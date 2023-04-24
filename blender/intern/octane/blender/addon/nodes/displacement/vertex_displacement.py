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


class OctaneVertexDisplacementTexture(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementAmount(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementAmount"
    bl_label="Height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="amount")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The displacement height in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementBlackLevel(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementBlackLevel"
    bl_label="Mid level"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=13)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="black_level")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The value in the image which corresponds to zero displacement.The range is always normalized to [0, 1]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementDisplacementMapType(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementDisplacementMapType"
    bl_label="Map type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=468)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="displacementMapType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Vector", "Vector", "", 0),
        ("Height", "Height", "", 1),
    ]
    default_value: EnumProperty(default="Height", update=OctaneBaseSocket.update_node_tree, description="The displacement map input type. For height map we displace in object normal direction and for vector maps, please refer vector space and input axes pins", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementTextureSpace(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementTextureSpace"
    bl_label="Vector space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=469)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="textureSpace")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Object", "Object", "", 0),
        ("Tangent", "Tangent", "", 1),
    ]
    default_value: EnumProperty(default="Object", update=OctaneBaseSocket.update_node_tree, description="The vector displacement map space. Only valid if the displacement map type is a vector. For tangent space vector map. R is along the tangent, Y is along the normal and Z is along the BiTangent. For object space please refer input axes pin", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementInputAxes(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementInputAxes"
    bl_label="Input axes"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=831)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="inputAxes")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("+X,+Y,+Z", "+X,+Y,+Z", "", 0),
        ("+X,+Z,+Y", "+X,+Z,+Y", "", 1),
        ("+X,+Y,-Z", "+X,+Y,-Z", "", 2),
    ]
    default_value: EnumProperty(default="+X,+Y,+Z", update=OctaneBaseSocket.update_node_tree, description="This setting is valid only for object space vector maps. The input axes provide us information about how to interpret RGB data. The selected axes are then converted to Octane XYZ space during displacement", items=items)
    octane_hide_value=False
    octane_min_version=11000500
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementBump(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementBump"
    bl_label="Auto bump map"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to get fine details of the displacement map on a lower subdivision level")
    octane_hide_value=False
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacementSubdLevel(OctaneBaseSocket):
    bl_idname="OctaneVertexDisplacementSubdLevel"
    bl_label="Subdivision level"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=479)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="subdLevel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The subdivision level applied to polygons using this material. This overrides the subdivision level set in the geometry preferences. Other subdivision settings have to be set in the geometry preference dialog. If a level higher than 6 is needed, please enter it manually", min=0, max=10, soft_min=0, soft_max=6, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVertexDisplacement(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVertexDisplacement"
    bl_label="Vertex displacement"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=97)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Height;Mid level;Map type;Vector space;Input axes;Auto bump map;Subdivision level;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneVertexDisplacementTexture", OctaneVertexDisplacementTexture.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementAmount", OctaneVertexDisplacementAmount.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementBlackLevel", OctaneVertexDisplacementBlackLevel.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementDisplacementMapType", OctaneVertexDisplacementDisplacementMapType.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementTextureSpace", OctaneVertexDisplacementTextureSpace.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementInputAxes", OctaneVertexDisplacementInputAxes.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementBump", OctaneVertexDisplacementBump.bl_label).init()
        self.inputs.new("OctaneVertexDisplacementSubdLevel", OctaneVertexDisplacementSubdLevel.bl_label).init()
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out").init()


_CLASSES=[
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

##### END OCTANE GENERATED CODE BLOCK #####
