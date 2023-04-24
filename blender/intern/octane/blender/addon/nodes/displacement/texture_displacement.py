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


class OctaneTextureDisplacementTexture(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementTexture"
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

class OctaneTextureDisplacementBlackLevel(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementBlackLevel"
    bl_label="Mid level"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=13)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="black_level")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The value in the image which corresponds to zero displacement. The range is always normalized to [0, 1]", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementLevelOfDetail(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementLevelOfDetail"
    bl_label="Level of detail"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=96)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="levelOfDetail")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("256x256", "256x256", "", 8),
        ("512x512", "512x512", "", 9),
        ("1024x1024", "1024x1024", "", 10),
        ("2048x2048", "2048x2048", "", 11),
        ("4096x4096", "4096x4096", "", 12),
        ("8192x8192", "8192x8192", "", 13),
    ]
    default_value: EnumProperty(default="1024x1024", update=OctaneBaseSocket.update_node_tree, description="Level of detail, i.e. the resolution of the internal displacement map", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementAmount(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementAmount"
    bl_label="Height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="amount")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The displacement height in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementDisplacementDirection(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementDisplacementDirection"
    bl_label="Displacement direction"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=371)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="displacementDirection")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Follow geometric normal", "Follow geometric normal", "", 2),
        ("Follow vertex normal", "Follow vertex normal", "", 1),
        ("Follow smoothed normal", "Follow smoothed normal", "", 3),
    ]
    default_value: EnumProperty(default="Follow vertex normal", update=OctaneBaseSocket.update_node_tree, description="The surface will be displaced along the given direction", items=items)
    octane_hide_value=False
    octane_min_version=3080008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementFilterType(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementFilterType"
    bl_label="Filter type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=336)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filterType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 0),
        ("Box", "Box", "", 1),
        ("Gaussian", "Gaussian", "", 2),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="Specifies which filter type to use on the displacement map texture", items=items)
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementFiltersize(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementFiltersize"
    bl_label="Filter radius"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filtersize")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=2, update=OctaneBaseSocket.update_node_tree, description="Number of nearest pixels to use for filtering. The higher the value the smoother the displacement map. Only valid if a filter is enabled", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureDisplacementShift(OctaneBaseSocket):
    bl_idname="OctaneTextureDisplacementShift"
    bl_label="Offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=214)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="shift")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Additional offset applied to allow moving the displaced surface", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=3000000
    octane_deprecated=True

class OctaneTextureDisplacement(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTextureDisplacement"
    bl_label="Texture displacement"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=80)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Mid level;Level of detail;Height;Displacement direction;Filter type;Filter radius;Offset;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneTextureDisplacementTexture", OctaneTextureDisplacementTexture.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementBlackLevel", OctaneTextureDisplacementBlackLevel.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementLevelOfDetail", OctaneTextureDisplacementLevelOfDetail.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementAmount", OctaneTextureDisplacementAmount.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementDisplacementDirection", OctaneTextureDisplacementDisplacementDirection.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementFilterType", OctaneTextureDisplacementFilterType.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementFiltersize", OctaneTextureDisplacementFiltersize.bl_label).init()
        self.inputs.new("OctaneTextureDisplacementShift", OctaneTextureDisplacementShift.bl_label).init()
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out").init()


_CLASSES=[
    OctaneTextureDisplacementTexture,
    OctaneTextureDisplacementBlackLevel,
    OctaneTextureDisplacementLevelOfDetail,
    OctaneTextureDisplacementAmount,
    OctaneTextureDisplacementDisplacementDirection,
    OctaneTextureDisplacementFilterType,
    OctaneTextureDisplacementFiltersize,
    OctaneTextureDisplacementShift,
    OctaneTextureDisplacement,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
