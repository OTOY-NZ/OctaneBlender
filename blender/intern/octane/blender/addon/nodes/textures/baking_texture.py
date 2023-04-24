##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneBakingTextureTexture(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureEnabled(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureEnabled"
    bl_label="Enable baking"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Enable texture baking. False means pausing texture baking")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureResolution(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureResolution"
    bl_label="Resolution"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(1024, 1024), update=None, description="Resolution of the baked texture", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureSamplingRate(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureSamplingRate"
    bl_label="Samples per pixel"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=206)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=32, update=None, description="Current samples/px used for the baked texture", min=1, max=10000, soft_min=1, soft_max=1000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureTonemapType(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureTonemapType"
    bl_label="Texture type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=356)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("LDR (sRGB)", "LDR (sRGB)", "", 0),
        ("HDR (linear sRGB)", "HDR (linear sRGB)", "", 2),
    ]
    default_value: EnumProperty(default="LDR (sRGB)", update=None, description="Current baked texture type", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureRgbBaking(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureRgbBaking"
    bl_label="RGB baking"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=355)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Baking the texture in RGB mode. False means baking in gray scale mode")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTexturePower(OctaneBaseSocket):
    bl_idname="OctaneBakingTexturePower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureGamma(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.200000, update=None, description="Gamma correction coefficient", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureInvert(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert image")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureLinearSpaceInvert(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureLinearSpaceInvert"
    bl_label="Linear space invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Invert image in the linear color space")
    octane_hide_value=False
    octane_min_version=4020000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneMeshUVProjection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureBorderMode(OctaneBaseSocket):
    bl_idname="OctaneBakingTextureBorderMode"
    bl_label="Border mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=15)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="Wrap around", update=None, description="Determines the texture lookup behavior when the texture-coords fall outside [0,1]", items=items)
    octane_hide_value=False
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBakingTextureGroupBakingProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneBakingTextureGroupBakingProperties"
    bl_label="[OctaneGroupTitle]Baking properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Texture;Enable baking;Resolution;Samples per pixel;Texture type;RGB baking;")

class OctaneBakingTextureGroupImageProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneBakingTextureGroupImageProperties"
    bl_label="[OctaneGroupTitle]Image properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Power;Gamma;Invert;Linear space invert;UV transform;Projection;Border mode;")

class OctaneBakingTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBakingTexture"
    bl_label="Baking texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=115)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Enable baking;Resolution;Samples per pixel;Texture type;RGB baking;Power;Gamma;Invert;Linear space invert;UV transform;Projection;Border mode;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_size;a_type;a_image_file_type;a_can_wrap_x;a_can_wrap_y;a_image_flip;a_source_info;a_image_layer_names;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="3;2;2;1;1;1;10;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=13)

    a_size: IntVectorProperty(name="Size", default=(0, 0), size=2, update=None, description="Size of the image in pixels or if the image is compressed the size of the image in blocks")
    a_type: IntProperty(name="Type", default=0, update=None, description="The image type, i.e. the data format used in A_BUFFER. Must be of type ImageType")
    a_image_file_type: IntProperty(name="Image file type", default=0, update=None, description="The original type of the image file, i.e. the data format stored in the image file")
    a_can_wrap_x: BoolProperty(name="Can wrap x", default=False, update=None, description="TRUE if the image can wrap around in the horizontal direction")
    a_can_wrap_y: BoolProperty(name="Can wrap y", default=False, update=None, description="TRUE if the image can wrap around in the vertical direction")
    a_image_flip: BoolProperty(name="Image flip", default=False, update=None, description="TRUE if the image needs to be flipped")
    a_source_info: StringProperty(name="Source info", default="", update=None, description="Information about the image source (file), which is used only in the UI")
    a_image_layer_names: StringProperty(name="Image layer names", default="", update=None, description="Will contain the layer names if the image was loaded from a file that contained layers. Will be empty otherwise")

    def init(self, context):
        self.inputs.new("OctaneBakingTextureGroupBakingProperties", OctaneBakingTextureGroupBakingProperties.bl_label).init()
        self.inputs.new("OctaneBakingTextureTexture", OctaneBakingTextureTexture.bl_label).init()
        self.inputs.new("OctaneBakingTextureEnabled", OctaneBakingTextureEnabled.bl_label).init()
        self.inputs.new("OctaneBakingTextureResolution", OctaneBakingTextureResolution.bl_label).init()
        self.inputs.new("OctaneBakingTextureSamplingRate", OctaneBakingTextureSamplingRate.bl_label).init()
        self.inputs.new("OctaneBakingTextureTonemapType", OctaneBakingTextureTonemapType.bl_label).init()
        self.inputs.new("OctaneBakingTextureRgbBaking", OctaneBakingTextureRgbBaking.bl_label).init()
        self.inputs.new("OctaneBakingTextureGroupImageProperties", OctaneBakingTextureGroupImageProperties.bl_label).init()
        self.inputs.new("OctaneBakingTexturePower", OctaneBakingTexturePower.bl_label).init()
        self.inputs.new("OctaneBakingTextureGamma", OctaneBakingTextureGamma.bl_label).init()
        self.inputs.new("OctaneBakingTextureInvert", OctaneBakingTextureInvert.bl_label).init()
        self.inputs.new("OctaneBakingTextureLinearSpaceInvert", OctaneBakingTextureLinearSpaceInvert.bl_label).init()
        self.inputs.new("OctaneBakingTextureTransform", OctaneBakingTextureTransform.bl_label).init()
        self.inputs.new("OctaneBakingTextureProjection", OctaneBakingTextureProjection.bl_label).init()
        self.inputs.new("OctaneBakingTextureBorderMode", OctaneBakingTextureBorderMode.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneBakingTextureTexture,
    OctaneBakingTextureEnabled,
    OctaneBakingTextureResolution,
    OctaneBakingTextureSamplingRate,
    OctaneBakingTextureTonemapType,
    OctaneBakingTextureRgbBaking,
    OctaneBakingTexturePower,
    OctaneBakingTextureGamma,
    OctaneBakingTextureInvert,
    OctaneBakingTextureLinearSpaceInvert,
    OctaneBakingTextureTransform,
    OctaneBakingTextureProjection,
    OctaneBakingTextureBorderMode,
    OctaneBakingTextureGroupBakingProperties,
    OctaneBakingTextureGroupImageProperties,
    OctaneBakingTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
