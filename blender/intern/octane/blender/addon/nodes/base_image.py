# <pep8 compliant>

from xml.etree import ElementTree

import numpy as np
from bpy.props import IntProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty

import bpy
from bpy.utils import register_class, unregister_class
from octane.core.octane_node import CArray
from octane.nodes.base_node import OctaneBaseNode
from octane.utils import consts, logger, utility


class OCTANE_use_viewport_texture_paint(bpy.types.Operator):
    """Use this image for the viewport texture paint"""

    bl_idname = "octane.use_viewport_texture_paint"
    bl_label = "Used in the Viewport Texture Paint"
    bl_description = ("Use this image for the viewport texture paint - to fix the 'Missing Textures' warning in "
                      "Texture Paint mode")

    def execute(self, context):
        image_node = context.node
        if not image_node:
            return
        cycles_tex_image = image_node.get_octane_texture_paint_helper()
        cycles_tex_image.image = image_node.image
        return {"FINISHED"}


class OctaneBaseImageNode(OctaneBaseNode):
    AUTOMATIC_CHANNEL_FORMAT_VALUE = -1
    IMAGE_DATA_C_ARRAY_IDENTIFIER = "IMAGE_DATA"
    BLENDER_ATTRIBUTE_IMAGE_DATA_UPDATE = "IMAGE_DATA_UPDATE"
    OCTANE_IMAGE_HELPER = "OCTANE_TEXTURE_HELPER[ShaderNodeTexImage]"
    OCTANE_TEXTURE_PAINT_HELPER = "OCTANE_TEXTURE_PAINT_HELPER[ShaderNodeTexImage]"

    support_udim = False

    def update_image(self, context):
        self.get_octane_image_helper()
        last_image = bpy.data.images.get(self.last_image_name)
        if self.image != last_image:
            self.last_image_name = self.image.name if self.image else ""
            self.update_image_info()
        self.update_node_tree(context)

    frame_current: IntProperty(name="Current Frame", default=0, min=-1048574, max=1048574, update=update_image,
                               description="Current frame number in image sequence or movie")
    frame_duration: IntProperty(name="Frame Duration", default=0, min=0, max=1048574, update=update_image,
                                description="Number of images of a movie to use")
    frame_offset: IntProperty(name="Offset", default=0, min=-2147483647, max=2147483647, update=update_image,
                              description="Offset the number of the frame to use in the animation")
    frame_start: IntProperty(name="Start Frame", default=0, min=-1048574, max=1048574, update=update_image,
                             description="Global starting frame of the movie/sequence, assuming first picture has a #1")
    tile: IntProperty(name="Tile", default=0, min=0, max=2147483647, update=update_image,
                      description="Tile in tiled image")
    use_auto_refresh: BoolProperty(name="Auto Refresh", default=False, update=update_image,
                                   description="Always refresh image on frame changes")
    use_cyclic: BoolProperty(name="Cyclic", default=False, update=update_image,
                             description="Cycle the images in the movie")
    last_image_name: StringProperty()
    ies_items = [
        ("IES_MAX_1", "Normalize maximum value to 1.0", "", 1),
        ("IES_COMPENSATE_LUMINANCE", "Normalize using lamp luminance", "", 2),
        ("IES_CANDELA_ABSOLUTE", "Absolute photometric", "", 3),
    ]
    a_ies_photometry_mode: EnumProperty(name="IES scaling", default="IES_MAX_1", update=update_image,
                                        description="How to normalize data from IES files", items=ies_items)
    a_channel_format_enum_items_str: StringProperty()
    a_channel_format_enum_items_container = {}

    image: PointerProperty(type=bpy.types.Image, update=update_image)

    def get_a_channel_format_enum_items(self, _context):
        default_items = [
            ("Automatic", "Automatic", "", OctaneBaseImageNode.AUTOMATIC_CHANNEL_FORMAT_VALUE),
        ]
        if len(self.a_channel_format_enum_items_str) == 0:
            return default_items
        if self.a_channel_format_enum_items_container.get(self.a_channel_format_enum_items_str, None) is None:
            value_list = []
            label_list = []
            enum_items = []
            try:
                root_et = ElementTree.fromstring(self.a_channel_format_enum_items_str)
                items_et = root_et.find("items")
                for et in items_et.findall("value"):
                    value_list.append(int(et.text))
                for et in items_et.findall("label"):
                    label_list.append(et.text)
                for idx, label in enumerate(label_list):
                    enum_items.append((label, label, "", value_list[idx]))
            except Exception as e:
                logger.exception(e)
                return default_items
            self.a_channel_format_enum_items_container[self.a_channel_format_enum_items_str] = enum_items
        return self.a_channel_format_enum_items_container[self.a_channel_format_enum_items_str]

    a_channel_format: EnumProperty(name="Import format", update=update_image, description="",
                                   items=get_a_channel_format_enum_items)

    @classmethod
    def update_node_definition(cls):
        utility.remove_attribute_list(cls,
                                      ["a_channel_format", "a_filename", "a_grid_size", "a_type", "a_image_file_type",
                                       "a_can_wrap_x", "a_can_wrap_y", "a_image_flip", "a_source_info",
                                       "a_image_layer_names", "a_image_chosen_layer_name", "a_size", "a_reload"])
        utility.add_attribute_list(cls, ["a_ies_photometry_mode", "a_channel_format"])

    def init_image_attributes(self):
        self.a_ies_photometry_mode = "IES_MAX_1"
        self.a_channel_format = "Automatic"
        if "Legacy gamma" in self.inputs:
            output_node = utility.find_active_output_node(self.id_data, consts.OctaneNodeTreeIDName.MATERIAL)
            default_legacy_gamma = 2.2 if output_node is not None else 1.0
            self.inputs["Legacy gamma"].default_value = default_legacy_gamma

    def get_octane_texture_paint_helper(self):
        node_tree = self.id_data
        if self.OCTANE_TEXTURE_PAINT_HELPER not in node_tree.nodes:
            cycles_tex_image = node_tree.nodes.new("ShaderNodeTexImage")
            cycles_tex_image.name = self.OCTANE_TEXTURE_PAINT_HELPER
            # "Hide" this helper node
            cycles_tex_image.location = (-100000, 0)
        cycles_tex_image = node_tree.nodes[self.OCTANE_TEXTURE_PAINT_HELPER]
        return cycles_tex_image

    @staticmethod
    def get_octane_image_helper():
        node = utility.get_octane_helper_node(OctaneBaseImageNode.OCTANE_IMAGE_HELPER)
        if node is None:
            node = utility.create_octane_helper_node(OctaneBaseImageNode.OCTANE_IMAGE_HELPER, "ShaderNodeTexImage")
        return node

    def update_image_info(self):
        if self.image:
            filepath = self.image.filepath_from_user()
        else:
            filepath = ""
        if len(filepath):
            from octane.core.client import OctaneBlender
            response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_IMAGE_INFO, filepath)
            if len(response):
                self.a_channel_format_enum_items_str = ElementTree.fromstring(response).get("content")
        else:
            self.a_channel_format_enum_items_str = ""
        if self.a_channel_format == "":
            self.a_channel_format = "Automatic"

    def auto_refresh(self):
        if self.image and self.image.source in ("SEQUENCE", "MOVIE") and self.use_auto_refresh:
            return consts.AutoRefreshStrategy.FRAME_CHANGE
        else:
            return consts.AutoRefreshStrategy.DISABLE

    def is_octane_image_node(self):
        return True

    def refresh_image_data(self, frame_current):
        if self.auto_refresh() == consts.AutoRefreshStrategy.DISABLE:
            return
        if self.image.source == "MOVIE":
            self.image.gl_free()
            self.image.gl_touch(frame=frame_current)

    def get_frame(self, frame_current):
        if frame_current >= self.frame_start:
            frame = frame_current - self.frame_start + 1
        else:
            if self.use_cyclic:
                frame = frame_current + self.frame_start - 1
            else:
                frame = 0
        if frame > self.frame_duration:
            if self.use_cyclic:
                if self.frame_duration > 0:
                    frame %= self.frame_duration
                if frame == 0:
                    frame = self.frame_duration
            else:
                frame = self.frame_duration
        frame += self.frame_offset
        if frame == 0 and self.use_cyclic:
            frame = self.frame_duration
        return frame

    def calculate_image_md5(self):
        md5 = ""
        if self.image and self.image.pixels:
            size = len(self.image.pixels)
            if size != 0:
                np_array = np.empty(len(self.image.pixels), dtype=np.float32)
                self.image.pixels.foreach_get(np_array)
                md5 = utility.calculate_np_array_md5(np_array)
        return md5

    def release_image_c_array(self, octane_node):
        octane_node.delete_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)

    def _update_image_filepath(self, octane_node, scene_frame_current):
        filepath = ""
        if self.image and self.image.source in ("FILE", "SEQUENCE",):
            if self.image.source == "SEQUENCE" and self.use_auto_refresh:
                cycles_image_helper = self.get_octane_image_helper()
                cycles_image_helper.image_user.frame_current = self.get_frame(scene_frame_current)
                filepath = self.image.filepath_from_user(image_user=cycles_image_helper.image_user)
            else:
                filepath = self.image.filepath_from_user()
        result = octane_node.set_attribute_blender_name("a_filename", consts.AttributeType.AT_FILENAME, filepath)
        return result

    def _update_pixel_image(self, octane_node, scene_frame_current):
        result = False
        # Refresh the movie data
        if self.image and self.image.source == "MOVIE":
            self.refresh_image_data(self.get_frame(scene_frame_current))
        c_array = octane_node.get_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
        # The empty image cases
        if not self.image or len(self.image.pixels) == 0:
            octane_node.set_attribute_blender_name("a_size", consts.AttributeType.AT_INT2, [0, 0])
            return octane_node.delete_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
        # The non-empty image cases
        octane_node.set_attribute_blender_name("a_size", consts.AttributeType.AT_INT2, self.image.size)
        # md5_hash = self.calculate_image_md5()
        # current_colorspace_name = self.image.colorspace_settings.name
        #  self.image.colorspace_settings.is_data = True
        float_size = len(self.image.pixels)
        if c_array is None or len(c_array) != float_size:
            # Create or Re-create the CArray when size is changed
            octane_node.delete_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
            if octane_node.new_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT, float_size, 4):
                c_array = octane_node.get_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
                self.image.pixels.foreach_get(c_array)
                result = True
        else:
            self.image.pixels.foreach_get(c_array)
            result = True
        # self.image.colorspace_settings.name = current_colorspace_name
        return result

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        scene = depsgraph.scene_eval
        is_data_updated = False
        need_reload = getattr(self, "need_reload", False)
        if self.image:
            if need_reload:
                octane_node.need_update = True
                octane_node.set_attribute_blender_name("a_reload", consts.AttributeType.AT_BOOL, True)
                setattr(self, "need_reload", False)
            scene_frame_current = scene.frame_current if scene else 0
            if self.image.source in ("FILE", "SEQUENCE",) and self.image.packed_file is None:
                is_data_updated |= self._update_image_filepath(octane_node, scene_frame_current)
                octane_node.delete_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
            elif self.image.packed_file is not None or len(self.image.pixels) > 0:
                is_data_updated |= self._update_pixel_image(octane_node, scene_frame_current)
                is_data_updated |= octane_node.set_attribute_blender_name("a_filename",
                                                                          consts.AttributeType.AT_FILENAME, "")
        else:
            is_data_updated |= octane_node.set_attribute_blender_name("a_filename", consts.AttributeType.AT_FILENAME,
                                                                      "")
            c_array = octane_node.get_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
            if c_array is not None:
                octane_node.delete_array_data(self.IMAGE_DATA_C_ARRAY_IDENTIFIER)
                is_data_updated = True
        octane_node.set_attribute_blender_name(self.BLENDER_ATTRIBUTE_IMAGE_DATA_UPDATE, consts.AttributeType.AT_BOOL,
                                               is_data_updated)

    def copy_from_custom_node(self, other_node, copy_link=False):
        super().copy_from_custom_node(other_node, copy_link)
        self.a_channel_format = other_node.a_channel_format
        self.image = other_node.image
        self.frame_current = other_node.frame_current
        self.frame_duration = other_node.frame_duration
        self.frame_offset = other_node.frame_offset
        self.frame_start = other_node.frame_start
        self.use_auto_refresh = other_node.use_auto_refresh
        self.use_cyclic = other_node.use_cyclic
        self.a_ies_photometry_mode = other_node.a_ies_photometry_mode
        self.update_image_info()

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        super().load_custom_legacy_node(legacy_node, node_tree, context, report)
        self.image = legacy_node.image
        self.frame_current = legacy_node.image_user.frame_current
        self.frame_duration = legacy_node.image_user.frame_duration
        self.frame_offset = legacy_node.image_user.frame_offset
        self.frame_start = legacy_node.image_user.frame_start
        self.use_auto_refresh = legacy_node.image_user.use_auto_refresh
        self.use_cyclic = legacy_node.image_user.use_cyclic
        try:
            self.a_ies_photometry_mode = legacy_node.octane_ies_mode
        except TypeError:
            self.a_ies_photometry_mode = "IES_MAX_1"
        self.update_image_info()
        a_channel_format = "Automatic"
        if legacy_node.hdr_tex_bit_depth == "OCT_HDR_BIT_DEPTH_32":
            a_channel_format = "32-bit float"
        if legacy_node.hdr_tex_bit_depth == "OCT_HDR_BIT_DEPTH_16":
            a_channel_format = "16-bit float"
        if a_channel_format != "Automatic":
            if a_channel_format in [item[0] for item in
                                    self.a_channel_format_enum_items_container.get(self.a_channel_format_enum_items_str,
                                                                                   [])]:
                self.a_channel_format = a_channel_format
            else:
                report({"WARNING"},
                       "Channel format '%s' is not valid for Image Node: %s. 'Automatic' format is used as a fallback. "
                       % (a_channel_format, legacy_node.name))

    def load_custom_ocs_data(self, creator, ocs_element_tree):
        # image_name = ocs_element_tree.get("name", "OctaneDB Image")
        for attr_et in ocs_element_tree.findall("attr"):
            if attr_et.get("name", "") == "filename":
                try:
                    asset_filepath = creator.get_asset_filepath(attr_et.text) if attr_et.text is not None else ""
                    if len(asset_filepath):
                        self.image = bpy.data.images.load(asset_filepath)
                except Exception as e:
                    logger.exception(e)

    def get_attribute_value(self, attribute_name, attribute_type):
        if attribute_name == "a_channel_format":
            enum_items = OctaneBaseImageNode.a_channel_format_enum_items_container.get(
                self.a_channel_format_enum_items_str, None)
            return utility.cast_enum_value_to_int(enum_items, self.a_channel_format,
                                                  OctaneBaseImageNode.AUTOMATIC_CHANNEL_FORMAT_VALUE)
        return super().get_attribute_value(attribute_name, attribute_type)

    def draw_buttons(self, context, layout):
        layout.template_ID(self, "image", new="image.new", open="image.open")
        if self.image:
            if hasattr(self, "a_image_color_format_enum"):
                layout.row().prop(self, "a_image_color_format_enum")
            layout.row().prop(self, "a_ies_photometry_mode")
            layout.row().prop(self, "a_channel_format")
            layout.row().prop(self.image, "source")
        col = layout.column()
        if self.image:
            if self.support_udim:
                if self.image.source != "TILED":
                    col.label(text="The 'Image tiles' only supports UDIM type!", icon="ERROR")
                    return
            else:
                if self.image.source == "TILED":
                    col.label(text="Please use the 'Image tiles' node for UDIM!", icon="ERROR")
                    return
            if self.image.source in ("SEQUENCE", "MOVIE"):
                box = col.box()
                sub = box.column(align=True)
                sub.label(text="Frame: %d" % self.get_frame(context.scene.frame_current))
                sub.prop(self, "frame_duration")
                sub.prop(self, "frame_start")
                sub.prop(self, "frame_offset")
                sub.prop(self, "use_cyclic")
                sub.prop(self, "use_auto_refresh")
            elif self.image.source == "GENERATED":
                col.operator("octane.use_viewport_texture_paint", text="Used in the Viewport Paint",
                             icon="BRUSH_DATA")


_CLASSES = [
    OCTANE_use_viewport_texture_paint,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
