import bpy
import re
import math
import numpy as np
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.core.octane_node import OctaneNode, CArray, OctaneNodeType
from octane.core.client import OctaneClient
from octane.utils import utility, consts
from octane.nodes import base_node, base_socket
from octane.nodes.base_node import OctaneBaseNode


class OCTANE_use_viewport_texture_paint(bpy.types.Operator):
    """Use this image for the viewport texture paint"""
    
    bl_idname = "octane.use_viewport_texture_paint"
    bl_label = "Used in the Viewport Texture Paint"
    bl_description = "Use this image for the viewport texture paint - to fix the 'Missing Textures' warning in Texture Paint mode"

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
    OCTANE_IMAGE_HELPER = "OCTANE_TEXTURE_PAINT_HELPER[ShaderNodeTexImage]"
    OCTANE_TEXTURE_PAINT_HELPER = "OCTANE_TEXTURE_PAINT_HELPER[ShaderNodeTexImage]"

    support_udim=False

    frame_current: IntProperty(name="Current Frame", default=0, min=-1048574, max=1048574, description="Current frame number in image sequence or movie")
    frame_duration: IntProperty(name="Frame Duration", default=0, min=0, max=1048574, description="Number of images of a movie to use")
    frame_offset: IntProperty(name="Offset", default=0, min=-2147483647, max=2147483647, description="Offset the number of the frame to use in the animation")
    frame_start: IntProperty(name="Start Frame", default=0, min=-1048574, max=1048574, description="Global starting frame of the movie/sequence, assuming first picture has a #1")
    tile: IntProperty(name="Tile", default=0, min=0, max=2147483647, description="Tile in tiled image")
    use_auto_refresh: BoolProperty(name="Auto Refresh", default=False, description="Always refresh image on frame changes")
    use_cyclic: BoolProperty(name="Cyclic", default=False, description="Cycle the images in the movie")
    last_image_name: StringProperty()
    ies_items = [
        ("IES_MAX_1", "Normalize maximum value to 1.0", "", 1),
        ("IES_COMPENSATE_LUMINANCE", "Normalize using lamp luminance", "", 2),
        ("IES_CANDELA_ABSOLUTE", "Absolute photometric", "", 3),
    ]
    a_ies_photometry_mode: EnumProperty(name="IES scaling", default="IES_MAX_1", description="How to normalize data from IES files", items=ies_items)
    a_channel_format_enum_items_str: StringProperty()
    a_channel_format_enum_items_container = {}

    def update_image(self, context):
        last_image = bpy.data.images.get(self.last_image_name)
        if self.image != last_image:
            self.last_image_name = self.image.name if self.image else ""
            self.update_image_info()
    
    image: PointerProperty(type=bpy.types.Image, update=update_image)

    def get_a_channel_format_enum_items(self, context):
        DEFAULT_ITEMS = [
            ("Automatic", "Automatic", "", OctaneBaseImageNode.AUTOMATIC_CHANNEL_FORMAT_VALUE),
        ]
        if len(self.a_channel_format_enum_items_str) == 0:
            return DEFAULT_ITEMS
        if OctaneBaseImageNode.a_channel_format_enum_items_container.get(self.a_channel_format_enum_items_str, None) is None:
            value_list = []
            label_list = []
            enum_items = []
            try:
                root_et = ET.fromstring(self.a_channel_format_enum_items_str)
                items_et = root_et.find("items")
                for et in items_et.findall("value"):
                    value_list.append(int(et.text))
                for et in items_et.findall("label"):
                    label_list.append(et.text)
                for idx, label in enumerate(label_list):
                    enum_items.append((label, label, "", value_list[idx]))
            except:
                return DEFAULT_ITEMS
            OctaneBaseImageNode.a_channel_format_enum_items_container[self.a_channel_format_enum_items_str] = enum_items            
        return OctaneBaseImageNode.a_channel_format_enum_items_container[self.a_channel_format_enum_items_str]

    a_channel_format: EnumProperty(name="Import format", update=update_image, description="", items=get_a_channel_format_enum_items)
    
    def init_image_attributes(self):
        utility.remove_attribute_list(self, "a_filename;a_grid_size;a_type;a_image_file_type;a_can_wrap_x;a_can_wrap_y;a_image_flip;a_source_info;a_image_layer_names;a_image_chosen_layer_name;")        
        utility.add_attribute_list(self, "a_ies_photometry_mode;a_channel_format", "iesPhotometryMode;channelFormat", "2;2;")
        self.a_ies_photometry_mode = "IES_MAX_1"
        self.a_channel_format = "Automatic"

    def get_octane_texture_paint_helper(self):        
        node_tree = self.id_data
        if self.OCTANE_TEXTURE_PAINT_HELPER not in node_tree.nodes:
            cycles_tex_image = node_tree.nodes.new("ShaderNodeTexImage")
            cycles_tex_image.name = self.OCTANE_TEXTURE_PAINT_HELPER
            # "Hide" this helper node
            cycles_tex_image.location = (-100000, 0)             
        cycles_tex_image = node_tree.nodes[self.OCTANE_TEXTURE_PAINT_HELPER]
        return cycles_tex_image

    def get_octane_image_helper(self):
        node = utility.get_octane_helper_node(self.OCTANE_IMAGE_HELPER)
        if node is None:
            node = utility.create_octane_helper_node(self.OCTANE_IMAGE_HELPER, "ShaderNodeTexImage")
        return node

    def update_image_info(self):
        if self.image:
            filepath = self.image.filepath_from_user()
        else:
            filepath = ""
        if len(filepath):
            octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
            octane_node.set_name("QueryImageInfo")
            octane_node.set_node_type(consts.NodeType.NT_BLENDER_NODE_IMAGE_INFO)
            octane_node.set_attribute("a_filename", consts.AttributeType.AT_FILENAME, filepath)
            self.a_channel_format_enum_items_str = OctaneClient().process_octane_node(octane_node)
        else:
            self.a_channel_format_enum_items_str = ""
        if self.a_channel_format == "":
            self.a_channel_format = "Automatic"

    def auto_refresh(self):
        return self.image and self.image.source in ("SEQUENCE", "MOVIE") and self.use_auto_refresh
    
    def is_octane_image_node(self):
        return True    

    def refresh_image_data(self, frame_current):
        if not self.auto_refresh():
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
        c_array = octane_node.get_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
        if c_array is not None:
            octane_node.release_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
            return True
        return False

    def _update_image_filepath(self, octane_node, scene_frame_current):
        filepath = ""
        if self.image and self.image.source in ("FILE", "SEQUENCE", ):            
            if self.image.source == "SEQUENCE" and self.use_auto_refresh:
                cycles_image_helper = self.get_octane_image_helper()
                cycles_image_helper.image_user.frame_current = self.get_frame(scene_frame_current)
                filepath = self.image.filepath_from_user(image_user=cycles_image_helper.image_user)
            else:
                filepath = self.image.filepath_from_user()        
        result = octane_node.set_attribute("a_filename", consts.AttributeType.AT_FILENAME, filepath)
        return result
    
    def _update_pixel_image(self, octane_node, scene_frame_current):
        # Refresh the movie data
        if self.image and self.image.source == "MOVIE":
            self.refresh_image_data(self.get_frame(scene_frame_current))
        c_array = octane_node.get_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
        # The empty image cases
        if not self.image or self.image.source not in ("MOVIE", "GENERATED", ) or len(self.image.pixels) == 0:
            octane_node.set_attribute("a_size", consts.AttributeType.AT_INT2, [0, 0])
            return self.release_image_c_array(octane_node)            
        # The non-empty image cases
        octane_node.set_attribute("a_size", consts.AttributeType.AT_INT2, self.image.size)
        md5_hash = self.calculate_image_md5()
        if c_array is None or c_array.size != len(self.image.pixels):
            # Create or Re-create the CArray when size is changed
            self.release_image_c_array(octane_node)
            if octane_node.create_c_array(len(self.image.pixels), self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT):
                c_array = octane_node.get_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
                c_array.hash_id = md5_hash
                self.image.pixels.foreach_get(c_array.array)
                return True
            return False
        else:
            # Compare the hash id
            if c_array.hash_id == md5_hash:
                return False
            else:
                c_array.hash_id = md5_hash
                self.image.pixels.foreach_get(c_array.array)
                return True
    
    def sync_custom_data(self, octane_node, octane_graph_node_data, owner_type, scene, is_viewport):
        super().sync_custom_data(octane_node, octane_graph_node_data, owner_type, scene, is_viewport)
        is_data_updated = False
        if self.image:
            scene_frame_current = scene.frame_current if scene else 0
            if self.image.source in ("FILE", "SEQUENCE", ):
                is_data_updated |= self._update_image_filepath(octane_node, scene_frame_current)
                self.release_image_c_array(octane_node)
            elif self.image.source in ("MOVIE", "GENERATED"):
                is_data_updated |= self._update_pixel_image(octane_node, scene_frame_current)
                is_data_updated |= octane_node.set_attribute("a_filename", consts.AttributeType.AT_FILENAME, "")
                c_array = octane_node.get_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
                if c_array is not None:
                    c_array.need_update = is_data_updated
        else:
            is_data_updated |= octane_node.set_attribute("a_filename", consts.AttributeType.AT_FILENAME, "")
            c_array = octane_node.get_c_array(self.IMAGE_DATA_C_ARRAY_IDENTIFIER, CArray.FLOAT)
            if c_array is not None:
                self.release_image_c_array(octane_node)
                is_data_updated = True
        octane_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_IMAGE_DATA_UPDATE, consts.AttributeType.AT_BOOL, is_data_updated)

    def get_attribute_value(self, attribute_name, attribute_type):
        if attribute_name == "a_channel_format":
            enum_items = OctaneBaseImageNode.a_channel_format_enum_items_container.get(self.a_channel_format_enum_items_str, None)
            return utility.cast_enum_value_to_int(enum_items, self.a_channel_format, OctaneBaseImageNode.AUTOMATIC_CHANNEL_FORMAT_VALUE)       
        return super().get_attribute_value(attribute_name, attribute_type)

    def draw_buttons(self, context, layout):
        layout.template_ID(self, "image", new="image.new", open="image.open")
        if self.image:
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
                op = col.operator("octane.use_viewport_texture_paint", text="Used in the Viewport Paint", icon="BRUSH_DATA")


_CLASSES = [
    OCTANE_use_viewport_texture_paint,
]

def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)