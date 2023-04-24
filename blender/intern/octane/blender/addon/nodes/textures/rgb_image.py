##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRGBImagePower(OctaneBaseSocket):
    bl_idname="OctaneRGBImagePower"
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

class OctaneRGBImageColorSpace(OctaneBaseSocket):
    bl_idname="OctaneRGBImageColorSpace"
    bl_label="Color space"
    color=consts.OctanePinColor.OCIOColorSpace
    octane_default_node_type="OctaneOCIOColorSpace"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRGBImageGamma(OctaneBaseSocket):
    bl_idname="OctaneRGBImageGamma"
    bl_label="Legacy gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Gamma value. Only used when the color space is set to \"Linear sRGB + legacy gamma\"", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRGBImageInvert(OctaneBaseSocket):
    bl_idname="OctaneRGBImageInvert"
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

class OctaneRGBImageLinearSpaceInvert(OctaneBaseSocket):
    bl_idname="OctaneRGBImageLinearSpaceInvert"
    bl_label="Linear sRGB invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=466)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Invert image after conversion to the linear sRGB color space, not before")
    octane_hide_value=False
    octane_min_version=4020000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRGBImageTransform(OctaneBaseSocket):
    bl_idname="OctaneRGBImageTransform"
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

class OctaneRGBImageProjection(OctaneBaseSocket):
    bl_idname="OctaneRGBImageProjection"
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

class OctaneRGBImageBorderMode(OctaneBaseSocket):
    bl_idname="OctaneRGBImageBorderMode"
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

class OctaneRGBImageScale(OctaneBaseSocket):
    bl_idname="OctaneRGBImageScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(1.000000, 0.000000), update=None, description="(deprecated) Scale", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", precision=3, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=1210000
    octane_deprecated=True

class OctaneRGBImage(bpy.types.Node, OctaneBaseImageNode):
    bl_idname="OctaneRGBImage"
    bl_label="RGB image"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=34)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Color space;Legacy gamma;Invert;Linear sRGB invert;UV transform;Projection;Border mode;Scale;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_size;a_type;a_image_file_type;a_can_wrap_x;a_can_wrap_y;a_image_flip;a_source_info;a_image_layer_names;a_image_chosen_layer_name;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;3;2;2;1;1;1;10;10;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    a_filename: StringProperty(name="Filename", default="", update=None, description="Stores the filename of the texture image", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=None, description="TRUE if the file needs a reload or the preference of the image file has been changed.After evaluation the attribute will be false again")
    a_size: IntVectorProperty(name="Size", default=(0, 0), size=2, update=None, description="Size of the image in pixels or if the image is compressed the size of the image in blocks")
    a_type: IntProperty(name="Type", default=0, update=None, description="The image type, i.e. the data format used in A_BUFFER. Must be of type ImageType")
    a_image_file_type: IntProperty(name="Image file type", default=0, update=None, description="The original type of the image file, i.e. the data format stored in the image file")
    a_can_wrap_x: BoolProperty(name="Can wrap x", default=False, update=None, description="TRUE if the image can wrap around in the horizontal direction")
    a_can_wrap_y: BoolProperty(name="Can wrap y", default=False, update=None, description="TRUE if the image can wrap around in the vertical direction")
    a_image_flip: BoolProperty(name="Image flip", default=False, update=None, description="TRUE if the image needs to be flipped")
    a_source_info: StringProperty(name="Source info", default="", update=None, description="Information about the image source (file), which is used only in the UI")
    a_image_layer_names: StringProperty(name="Image layer names", default="", update=None, description="Will contain the layer names if the image was loaded from a file that contained layers. Will be empty otherwise")
    a_image_chosen_layer_name: StringProperty(name="Image chosen layer name", default="", update=None, description="Indicate the chosen layer name, if the current image has multiple layers")

    def init(self, context):
        self.inputs.new("OctaneRGBImagePower", OctaneRGBImagePower.bl_label).init()
        self.inputs.new("OctaneRGBImageColorSpace", OctaneRGBImageColorSpace.bl_label).init()
        self.inputs.new("OctaneRGBImageGamma", OctaneRGBImageGamma.bl_label).init()
        self.inputs.new("OctaneRGBImageInvert", OctaneRGBImageInvert.bl_label).init()
        self.inputs.new("OctaneRGBImageLinearSpaceInvert", OctaneRGBImageLinearSpaceInvert.bl_label).init()
        self.inputs.new("OctaneRGBImageTransform", OctaneRGBImageTransform.bl_label).init()
        self.inputs.new("OctaneRGBImageProjection", OctaneRGBImageProjection.bl_label).init()
        self.inputs.new("OctaneRGBImageBorderMode", OctaneRGBImageBorderMode.bl_label).init()
        self.inputs.new("OctaneRGBImageScale", OctaneRGBImageScale.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneRGBImagePower,
    OctaneRGBImageColorSpace,
    OctaneRGBImageGamma,
    OctaneRGBImageInvert,
    OctaneRGBImageLinearSpaceInvert,
    OctaneRGBImageTransform,
    OctaneRGBImageProjection,
    OctaneRGBImageBorderMode,
    OctaneRGBImageScale,
    OctaneRGBImage,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
