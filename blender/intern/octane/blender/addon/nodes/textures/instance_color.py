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


class OctaneInstanceColorPower(OctaneBaseSocket):
    bl_idname="OctaneInstanceColorPower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceColorColorSpace(OctaneBaseSocket):
    bl_idname="OctaneInstanceColorColorSpace"
    bl_label="Color space"
    color=consts.OctanePinColor.OCIOColorSpace
    octane_default_node_type=consts.NodeType.NT_OCIO_COLOR_SPACE
    octane_default_node_name="OctaneOCIOColorSpace"
    octane_pin_id=consts.PinID.P_COLOR_SPACE
    octane_pin_name="colorSpace"
    octane_pin_type=consts.PinType.PT_OCIO_COLOR_SPACE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=11000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceColorGamma(OctaneBaseSocket):
    bl_idname="OctaneInstanceColorGamma"
    bl_label="Legacy gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAMMA
    octane_pin_name="gamma"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Gamma value. Only used when the color space is set to \"Linear sRGB + legacy gamma\"", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceColorInvert(OctaneBaseSocket):
    bl_idname="OctaneInstanceColorInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert image")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceColorLinearSpaceInvert(OctaneBaseSocket):
    bl_idname="OctaneInstanceColorLinearSpaceInvert"
    bl_label="Linear sRGB invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_LINEAR_SPACE_INVERT
    octane_pin_name="linearSpaceInvert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Invert image after conversion to the linear sRGB color space, not before")
    octane_hide_value=False
    octane_min_version=4020000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInstanceColor(bpy.types.Node, OctaneBaseImageNode):
    bl_idname="OctaneInstanceColor"
    bl_label="Instance color"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneInstanceColorPower,OctaneInstanceColorColorSpace,OctaneInstanceColorGamma,OctaneInstanceColorInvert,OctaneInstanceColorLinearSpaceInvert,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_INSTANCE_COLOR
    octane_socket_list=["Power", "Color space", "Legacy gamma", "Invert", "Linear sRGB invert", ]
    octane_attribute_list=["a_filename", "a_reload", "a_initial_color_space_selected", "a_size", "a_type", "a_image_file_type", "a_can_wrap_x", "a_can_wrap_y", "a_image_flip", "a_source_info", "a_image_layer_names", "a_image_chosen_layer_name", "a_legacy_png_gamma", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_initial_color_space_selected": [consts.AttributeID.A_INITIAL_COLOR_SPACE_SELECTED, "initialColorSpaceSelected", consts.AttributeType.AT_BOOL], "a_buffer": [consts.AttributeID.A_BUFFER, "buffer", consts.AttributeType.AT_BYTE], "a_size": [consts.AttributeID.A_SIZE, "size", consts.AttributeType.AT_INT2], "a_type": [consts.AttributeID.A_TYPE, "type", consts.AttributeType.AT_INT], "a_image_file_type": [consts.AttributeID.A_IMAGE_FILE_TYPE, "imageFileType", consts.AttributeType.AT_INT], "a_can_wrap_x": [consts.AttributeID.A_CAN_WRAP_X, "canWrapX", consts.AttributeType.AT_BOOL], "a_can_wrap_y": [consts.AttributeID.A_CAN_WRAP_Y, "canWrapY", consts.AttributeType.AT_BOOL], "a_image_flip": [consts.AttributeID.A_IMAGE_FLIP, "imageFlip", consts.AttributeType.AT_BOOL], "a_source_info": [consts.AttributeID.A_SOURCE_INFO, "sourceInfo", consts.AttributeType.AT_STRING], "a_image_layer_names": [consts.AttributeID.A_IMAGE_LAYER_NAMES, "imageLayerNames", consts.AttributeType.AT_STRING], "a_channel_format": [consts.AttributeID.A_CHANNEL_FORMAT, "channelFormat", consts.AttributeType.AT_INT], "a_image_chosen_layer_name": [consts.AttributeID.A_IMAGE_CHOSEN_LAYER_NAME, "imageChosenLayerName", consts.AttributeType.AT_STRING], "a_ies_photometry_mode": [consts.AttributeID.A_IES_PHOTOMETRY_MODE, "iesPhotometryMode", consts.AttributeType.AT_INT], "a_legacy_png_gamma": [consts.AttributeID.A_LEGACY_PNG_GAMMA, "legacyPngGamma", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=5

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the filename of the texture image", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="TRUE if the file needs a reload or the preference of the image file has been changed.After evaluation the attribute will be false again")
    a_initial_color_space_selected: BoolProperty(name="Initial color space selected", default=False, update=OctaneBaseNode.update_node_tree, description="If true, an initial color space has previously been automatically selected, and so one will not be selected again. If false, the color space will be set the next time an image is loaded")
    a_size: IntVectorProperty(name="Size", default=(0, 0), size=2, update=OctaneBaseNode.update_node_tree, description="Size of the image in pixels or if the image is compressed the size of the image in blocks")
    a_type: IntProperty(name="Type", default=0, update=OctaneBaseNode.update_node_tree, description="The image type, i.e. the data format used in A_BUFFER. Must be of type ImageType")
    a_image_file_type: IntProperty(name="Image file type", default=0, update=OctaneBaseNode.update_node_tree, description="The original type of the image file, i.e. the data format stored in the image file")
    a_can_wrap_x: BoolProperty(name="Can wrap x", default=False, update=OctaneBaseNode.update_node_tree, description="True if the image can wrap around in the horizontal direction, false otherwise")
    a_can_wrap_y: BoolProperty(name="Can wrap y", default=False, update=OctaneBaseNode.update_node_tree, description="True if the image can wrap around in the vertical direction, false otherwise")
    a_image_flip: BoolProperty(name="Image flip", default=False, update=OctaneBaseNode.update_node_tree, description="True if the rows of pixels are stored in the buffer starting with the top row of the image and going down, false if they are stored starting with the bottom row of the image and going up. If A_TYPE is a compressed type, this must be true")
    a_source_info: StringProperty(name="Source info", default="", update=OctaneBaseNode.update_node_tree, description="Information about the image source (file), which is used only in the UI")
    a_image_layer_names: StringProperty(name="Image layer names", default="", update=OctaneBaseNode.update_node_tree, description="Will contain the layer names if the image was loaded from a file that contained layers. Will be empty otherwise")
    a_image_chosen_layer_name: StringProperty(name="Image chosen layer name", default="", update=OctaneBaseNode.update_node_tree, description="Indicate the chosen layer name, if the current image has multiple layers")
    a_legacy_png_gamma: BoolProperty(name="Legacy png gamma", default=False, update=OctaneBaseNode.update_node_tree, description="If true, PNG files with a gAMA chunk will be converted to display gamma 2.2 while loading")

    def init(self, context):
        self.inputs.new("OctaneInstanceColorPower", OctaneInstanceColorPower.bl_label).init()
        self.inputs.new("OctaneInstanceColorColorSpace", OctaneInstanceColorColorSpace.bl_label).init()
        self.inputs.new("OctaneInstanceColorGamma", OctaneInstanceColorGamma.bl_label).init()
        self.inputs.new("OctaneInstanceColorInvert", OctaneInstanceColorInvert.bl_label).init()
        self.inputs.new("OctaneInstanceColorLinearSpaceInvert", OctaneInstanceColorLinearSpaceInvert.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneInstanceColorPower,
    OctaneInstanceColorColorSpace,
    OctaneInstanceColorGamma,
    OctaneInstanceColorInvert,
    OctaneInstanceColorLinearSpaceInvert,
    OctaneInstanceColor,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneInstanceColor_Override(OctaneInstanceColor):

    def init(self, context):
        super().init(context)
        self.init_image_attributes()

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

OctaneInstanceColor_Override.update_node_definition()
utility.override_class(_CLASSES, OctaneInstanceColor, OctaneInstanceColor_Override)