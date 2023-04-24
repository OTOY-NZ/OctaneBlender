##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneImageTilesPower(OctaneBaseSocket):
    bl_idname="OctaneImageTilesPower"
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

class OctaneImageTilesColorSpace(OctaneBaseSocket):
    bl_idname="OctaneImageTilesColorSpace"
    bl_label="Color space"
    color=consts.OctanePinColor.OCIOColorSpace
    octane_default_node_type="OctaneOCIOColorSpace"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=616)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=11000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageTilesGamma(OctaneBaseSocket):
    bl_idname="OctaneImageTilesGamma"
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

class OctaneImageTilesInvert(OctaneBaseSocket):
    bl_idname="OctaneImageTilesInvert"
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

class OctaneImageTilesLinearSpaceInvert(OctaneBaseSocket):
    bl_idname="OctaneImageTilesLinearSpaceInvert"
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

class OctaneImageTilesTransform(OctaneBaseSocket):
    bl_idname="OctaneImageTilesTransform"
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

class OctaneImageTilesProjection(OctaneBaseSocket):
    bl_idname="OctaneImageTilesProjection"
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

class OctaneImageTilesEmptyTileColor(OctaneBaseSocket):
    bl_idname="OctaneImageTilesEmptyTileColor"
    bl_label="Empty tile color"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=441)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Color to use if no image is loaded for a tile", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=4000011
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageTiles(bpy.types.Node, OctaneBaseImageNode):
    bl_idname="OctaneImageTiles"
    bl_label="Image tiles"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=131)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Color space;Legacy gamma;Invert;Linear sRGB invert;UV transform;Projection;Empty tile color;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_image_color_format;a_grid_size;a_reload;a_image_chosen_layer_name;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;2;3;1;10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    a_filename: StringProperty(name="Filename", default="", update=None, description="Stores the filenames of the texture image tiles. Entries may be left empty if no image is available for a particular tile. If the length doesn't cover the entire grid then the remaining entries are assumed to be empty", subtype="FILE_PATH")
    a_image_color_format: IntProperty(name="Image color format", default=0, update=None, description="Control in which color format the textures are loaded, see Octane::ImageColorType. If set to IMAGE_COLOR_KEEP_SOURCE images are loaded either as RGB color or greyscale, depending on the format used to save the image file")
    a_grid_size: IntVectorProperty(name="Grid size", default=(1, 1), size=2, update=None, description="The size of the image tile grid")
    a_reload: BoolProperty(name="Reload", default=False, update=None, description="TRUE if the files needs a reload. After evaluation the attribute will be false again")
    a_image_chosen_layer_name: StringProperty(name="Image chosen layer name", default="", update=None, description="Indicate the chosen layer name, if the current image has multiple layers")

    def init(self, context):
        self.inputs.new("OctaneImageTilesPower", OctaneImageTilesPower.bl_label).init()
        self.inputs.new("OctaneImageTilesColorSpace", OctaneImageTilesColorSpace.bl_label).init()
        self.inputs.new("OctaneImageTilesGamma", OctaneImageTilesGamma.bl_label).init()
        self.inputs.new("OctaneImageTilesInvert", OctaneImageTilesInvert.bl_label).init()
        self.inputs.new("OctaneImageTilesLinearSpaceInvert", OctaneImageTilesLinearSpaceInvert.bl_label).init()
        self.inputs.new("OctaneImageTilesTransform", OctaneImageTilesTransform.bl_label).init()
        self.inputs.new("OctaneImageTilesProjection", OctaneImageTilesProjection.bl_label).init()
        self.inputs.new("OctaneImageTilesEmptyTileColor", OctaneImageTilesEmptyTileColor.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneImageTilesPower,
    OctaneImageTilesColorSpace,
    OctaneImageTilesGamma,
    OctaneImageTilesInvert,
    OctaneImageTilesLinearSpaceInvert,
    OctaneImageTilesTransform,
    OctaneImageTilesProjection,
    OctaneImageTilesEmptyTileColor,
    OctaneImageTiles,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
