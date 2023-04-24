##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneImageAOVOutputColorSpace(OctaneBaseSocket):
    bl_idname="OctaneImageAOVOutputColorSpace"
    bl_label="Color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("sRGB", "sRGB", "", 1),
        ("Linear sRGB", "Linear sRGB", "", 2),
    ]
    default_value: EnumProperty(default="sRGB", update=None, description="Select the color space of the input image. Octane compositing happens in the Linear sRGB space. All sRGB images are converted to linear sRGB during compositing. Currently NAMED_COLOR_SPACE_SRGB and NAMED_COLOR_SPACE_LINEAR_SRGB from NamedColorSpace enum are the only two allowed as the inputs in this pin", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageAOVOutputOutputChannels(OctaneBaseSocket):
    bl_idname="OctaneImageAOVOutputOutputChannels"
    bl_label="Output channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=615)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGBA", update=None, description="Select output channels type of this node. Can be set to one of enum ChannelGroups", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageAOVOutputImager(OctaneBaseSocket):
    bl_idname="OctaneImageAOVOutputImager"
    bl_label="Enable imager"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, The imager settings is applied on the final AOV output. Otherwise ignored  Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageAOVOutputPostproc(OctaneBaseSocket):
    bl_idname="OctaneImageAOVOutputPostproc"
    bl_label="Enable post processing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, The post processing settings is applied on the final AOV output. Otherwise ignored Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageAOVOutputPremultipliedAlpha(OctaneBaseSocket):
    bl_idname="OctaneImageAOVOutputPremultipliedAlpha"
    bl_label="Pre multiply alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=139)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled the input RGB values will be multiplied with alpha")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=10021500
    octane_deprecated=True

class OctaneImageAOVOutputGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneImageAOVOutputGroupOutputSettings"
    bl_label="[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post processing;")

class OctaneImageAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneImageAOVOutput"
    bl_label="Image AOV output"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=168)
    octane_socket_list: StringProperty(name="Socket List", default="Color space;Output channels;Enable imager;Enable post processing;Pre multiply alpha;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_size;a_type;a_image_file_type;a_can_wrap_x;a_can_wrap_y;a_image_flip;a_source_info;a_image_layer_names;a_channel_format;a_image_chosen_layer_name;a_ies_photometry_mode;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;3;2;2;1;1;1;10;10;2;10;2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

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
    a_channel_format: IntProperty(name="Channel format", default=2, update=None, description="Indicate the preferred channel format for loading this image. This is ignored for 8-bit images. For other images, use IMAGE_CHANNEL_HALF and IMAGE_CHANNEL_FLOAT to always load images in that format, use IMAGE_CHANNEL_AUTO to infer the format from the source data")
    a_image_chosen_layer_name: StringProperty(name="Image chosen layer name", default="", update=None, description="Indicate the chosen layer name, if the current image has multiple layers")
    a_ies_photometry_mode: IntProperty(name="Ies photometry mode", default=1, update=None, description="How to normalize data from IES files. (see Octane::IesPhotometryMode)")

    def init(self, context):
        self.inputs.new("OctaneImageAOVOutputColorSpace", OctaneImageAOVOutputColorSpace.bl_label).init()
        self.inputs.new("OctaneImageAOVOutputOutputChannels", OctaneImageAOVOutputOutputChannels.bl_label).init()
        self.inputs.new("OctaneImageAOVOutputGroupOutputSettings", OctaneImageAOVOutputGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneImageAOVOutputImager", OctaneImageAOVOutputImager.bl_label).init()
        self.inputs.new("OctaneImageAOVOutputPostproc", OctaneImageAOVOutputPostproc.bl_label).init()
        self.inputs.new("OctaneImageAOVOutputPremultipliedAlpha", OctaneImageAOVOutputPremultipliedAlpha.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out").init()


_CLASSES=[
    OctaneImageAOVOutputColorSpace,
    OctaneImageAOVOutputOutputChannels,
    OctaneImageAOVOutputImager,
    OctaneImageAOVOutputPostproc,
    OctaneImageAOVOutputPremultipliedAlpha,
    OctaneImageAOVOutputGroupOutputSettings,
    OctaneImageAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
