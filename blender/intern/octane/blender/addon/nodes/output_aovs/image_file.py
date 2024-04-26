##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsImageFileEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsImageFileEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsImageFileColorSpace(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsImageFileColorSpace"
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
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsImageFilePremultipliedAlpha(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsImageFilePremultipliedAlpha"
    bl_label="Premultiplied alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_PREMULTIPLIED_ALPHA
    octane_pin_name="premultiplied_alpha"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether the RGB channels in the image have been premultiplied by the alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsImageFileBlendingSettings(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsImageFileBlendingSettings"
    bl_label="Blending settings"
    color=consts.OctanePinColor.BlendingSettings
    octane_default_node_type=consts.NodeType.NT_BLENDING_SETTINGS
    octane_default_node_name="OctaneBlendingSettings"
    octane_pin_id=consts.PinID.P_BLENDING_SETTINGS
    octane_pin_name="blendingSettings"
    octane_pin_type=consts.PinType.PT_BLENDING_SETTINGS
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsImageFile(bpy.types.Node, OctaneBaseImageNode):
    bl_idname="OctaneOutputAOVsImageFile"
    bl_label="Image file"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsImageFileEnabled,OctaneOutputAOVsImageFileColorSpace,OctaneOutputAOVsImageFilePremultipliedAlpha,OctaneOutputAOVsImageFileBlendingSettings,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_BLEND_IMAGE
    octane_socket_list=["Enabled", "Color space", "Premultiplied alpha", "Blending settings", ]
    octane_attribute_list=["a_filename", "a_reload", "a_initial_color_space_selected", "a_size", "a_type", "a_image_file_type", "a_can_wrap_x", "a_can_wrap_y", "a_image_flip", "a_source_info", "a_image_layer_names", "a_image_chosen_layer_name", "a_legacy_png_gamma", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_initial_color_space_selected": [consts.AttributeID.A_INITIAL_COLOR_SPACE_SELECTED, "initialColorSpaceSelected", consts.AttributeType.AT_BOOL], "a_buffer": [consts.AttributeID.A_BUFFER, "buffer", consts.AttributeType.AT_BYTE], "a_size": [consts.AttributeID.A_SIZE, "size", consts.AttributeType.AT_INT2], "a_type": [consts.AttributeID.A_TYPE, "type", consts.AttributeType.AT_INT], "a_image_file_type": [consts.AttributeID.A_IMAGE_FILE_TYPE, "imageFileType", consts.AttributeType.AT_INT], "a_can_wrap_x": [consts.AttributeID.A_CAN_WRAP_X, "canWrapX", consts.AttributeType.AT_BOOL], "a_can_wrap_y": [consts.AttributeID.A_CAN_WRAP_Y, "canWrapY", consts.AttributeType.AT_BOOL], "a_image_flip": [consts.AttributeID.A_IMAGE_FLIP, "imageFlip", consts.AttributeType.AT_BOOL], "a_source_info": [consts.AttributeID.A_SOURCE_INFO, "sourceInfo", consts.AttributeType.AT_STRING], "a_image_layer_names": [consts.AttributeID.A_IMAGE_LAYER_NAMES, "imageLayerNames", consts.AttributeType.AT_STRING], "a_channel_format": [consts.AttributeID.A_CHANNEL_FORMAT, "channelFormat", consts.AttributeType.AT_INT], "a_image_chosen_layer_name": [consts.AttributeID.A_IMAGE_CHOSEN_LAYER_NAME, "imageChosenLayerName", consts.AttributeType.AT_STRING], "a_ies_photometry_mode": [consts.AttributeID.A_IES_PHOTOMETRY_MODE, "iesPhotometryMode", consts.AttributeType.AT_INT], "a_legacy_png_gamma": [consts.AttributeID.A_LEGACY_PNG_GAMMA, "legacyPngGamma", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=4

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the filename of the texture image", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="TRUE if the file needs a reload or the preference of the image file has been changed.After evaluation the attribute will be false again")
    a_initial_color_space_selected: BoolProperty(name="Initial color space selected", default=False, update=OctaneBaseNode.update_node_tree, description="If true, an initial color space has previously been automatically selected, and so one will not be selected again. If false, the color space will be set the next time an image is loaded. This also applies to the premultiplied alpha pin if there is one")
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
        self.inputs.new("OctaneOutputAOVsImageFileEnabled", OctaneOutputAOVsImageFileEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsImageFileColorSpace", OctaneOutputAOVsImageFileColorSpace.bl_label).init()
        self.inputs.new("OctaneOutputAOVsImageFilePremultipliedAlpha", OctaneOutputAOVsImageFilePremultipliedAlpha.bl_label).init()
        self.inputs.new("OctaneOutputAOVsImageFileBlendingSettings", OctaneOutputAOVsImageFileBlendingSettings.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsImageFileEnabled,
    OctaneOutputAOVsImageFileColorSpace,
    OctaneOutputAOVsImageFilePremultipliedAlpha,
    OctaneOutputAOVsImageFileBlendingSettings,
    OctaneOutputAOVsImageFile,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneOutputAOVsImageFile_Override(OctaneOutputAOVsImageFile):

    def init(self, context):
        super().init(context)
        self.init_image_attributes()

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

OctaneOutputAOVsImageFile_Override.update_node_definition()
utility.override_class(_CLASSES, OctaneOutputAOVsImageFile, OctaneOutputAOVsImageFile_Override)