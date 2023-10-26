##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneImageTilesPower(OctaneBaseSocket):
    bl_idname="OctaneImageTilesPower"
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

class OctaneImageTilesColorSpace(OctaneBaseSocket):
    bl_idname="OctaneImageTilesColorSpace"
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

class OctaneImageTilesGamma(OctaneBaseSocket):
    bl_idname="OctaneImageTilesGamma"
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

class OctaneImageTilesInvert(OctaneBaseSocket):
    bl_idname="OctaneImageTilesInvert"
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

class OctaneImageTilesLinearSpaceInvert(OctaneBaseSocket):
    bl_idname="OctaneImageTilesLinearSpaceInvert"
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

class OctaneImageTilesTransform(OctaneBaseSocket):
    bl_idname="OctaneImageTilesTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageTilesProjection(OctaneBaseSocket):
    bl_idname="OctaneImageTilesProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneImageTilesEmptyTileColor(OctaneBaseSocket):
    bl_idname="OctaneImageTilesEmptyTileColor"
    bl_label="Empty tile color"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_EMPTY_TILE_COLOR
    octane_pin_name="emptyTileColor"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Color to use if no image is loaded for a tile", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
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
    octane_socket_class_list=[OctaneImageTilesPower,OctaneImageTilesColorSpace,OctaneImageTilesGamma,OctaneImageTilesInvert,OctaneImageTilesLinearSpaceInvert,OctaneImageTilesTransform,OctaneImageTilesProjection,OctaneImageTilesEmptyTileColor,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_IMAGE_TILES
    octane_socket_list=["Power", "Color space", "Legacy gamma", "Invert", "Linear sRGB invert", "UV transform", "Projection", "Empty tile color", ]
    octane_attribute_list=["a_filename", "a_image_color_format", "a_grid_size", "a_reload", "a_image_chosen_layer_name", "a_legacy_png_gamma", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_image_color_format": [consts.AttributeID.A_IMAGE_COLOR_FORMAT, "imageColorFormat", consts.AttributeType.AT_INT], "a_grid_size": [consts.AttributeID.A_GRID_SIZE, "gridSize", consts.AttributeType.AT_INT2], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_channel_format": [consts.AttributeID.A_CHANNEL_FORMAT, "channelFormat", consts.AttributeType.AT_INT], "a_image_chosen_layer_name": [consts.AttributeID.A_IMAGE_CHOSEN_LAYER_NAME, "imageChosenLayerName", consts.AttributeType.AT_STRING], "a_ies_photometry_mode": [consts.AttributeID.A_IES_PHOTOMETRY_MODE, "iesPhotometryMode", consts.AttributeType.AT_INT], "a_legacy_png_gamma": [consts.AttributeID.A_LEGACY_PNG_GAMMA, "legacyPngGamma", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=8

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the filenames of the texture image tiles. Entries may be left empty if no image is available for a particular tile. If the length doesn't cover the entire grid then the remaining entries are assumed to be empty", subtype="FILE_PATH")
    a_image_color_format: IntProperty(name="Image color format", default=0, update=OctaneBaseNode.update_node_tree, description="The color format in which the textures are loaded, see Octane::ImageColorType. If set to IMAGE_COLOR_KEEP_SOURCE images are loaded either as RGB color or grayscale, depending on the format used to save the image file")
    a_grid_size: IntVectorProperty(name="Grid size", default=(1, 1), size=2, update=OctaneBaseNode.update_node_tree, description="The size of the image tile grid")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="TRUE if the files needs a reload. After evaluation the attribute will be false again")
    a_image_chosen_layer_name: StringProperty(name="Image chosen layer name", default="", update=OctaneBaseNode.update_node_tree, description="Indicate the chosen layer name, if the current image has multiple layers")
    a_legacy_png_gamma: BoolProperty(name="Legacy png gamma", default=False, update=OctaneBaseNode.update_node_tree, description="If true, PNG files with a gAMA chunk will be converted to display gamma 2.2 while loading")

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

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneImageTiles_Override(OctaneImageTiles):

    support_udim=True

    def init(self, context):
        super().init(context)
        self.init_image_attributes()

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        filepath = "" 
        is_data_updated = False
        grid_size = [0, 0]
        if self.image and self.image.source == "TILED" and len(self.image.tiles):
            filepaths = []
            # Resolve grid size
            for tile in self.image.tiles:
                n = tile.number - 1000
                grid_size[0] = max(grid_size[0], n % 10)
                grid_size[1] = max(1, max(grid_size[1], int(n / 10) + 1))
                cycles_image_helper = self.get_octane_image_helper()
                cycles_image_helper.image_user.tile = tile.number
                tile_filepath = self.image.filepath_from_user(image_user=cycles_image_helper.image_user)
                filepaths.append(tile_filepath)
            filepath = ";".join(filepaths)
        is_data_updated |= octane_node.set_attribute_blender_name("a_filename", consts.AttributeType.AT_FILENAME, filepath)
        is_data_updated |= octane_node.set_attribute_blender_name("a_grid_size", consts.AttributeType.AT_INT2, grid_size)
        octane_node.set_attribute_blender_name(self.BLENDER_ATTRIBUTE_IMAGE_DATA_UPDATE, consts.AttributeType.AT_BOOL, is_data_updated)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

OctaneImageTiles_Override.update_node_definition()
utility.override_class(_CLASSES, OctaneImageTiles, OctaneImageTiles_Override)