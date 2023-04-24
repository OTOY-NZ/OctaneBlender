import bpy
import re
import math
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty
from bpy.utils import register_class, unregister_class
from octane.bin import octane_blender_client
from octane.octane_server import RpcProtocolType, RpcProtocol, OctaneServer
from octane.utils import utility, consts
from octane.nodes import base_node, base_socket
from octane.nodes.base_node import OctaneBaseNode


class OctaneBaseImageNode(OctaneBaseNode):
    AUTOMATIC_CHANNEL_FORMAT_VALUE = -1

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
    is_image_data_updated: BoolProperty(default=False)
    a_channel_format_enum_items_container = {}

    def init_image_attributes(self):
        utility.remove_attribute(self, "a_type;a_image_file_type;a_can_wrap_x;a_can_wrap_y;a_image_flip;a_source_info;a_image_layer_names;a_image_chosen_layer_name;")
        self.a_ies_photometry_mode = "IES_MAX_1"
        self.a_channel_format = "Automatic"

    def update_image(self, context):
        last_image = bpy.data.images.get(self.last_image_name)
        if self.image != last_image:
            self.is_image_data_updated = True
            self.last_image_name = self.image.name if self.image else ""
            self.update_image_info()
    
    def update_image_info(self):
        if self.image:
            filepath = self.image.filepath_from_user()
        else:
            filepath = ""
        if len(filepath):
            rpc_protocol = RpcProtocol(RpcProtocolType.GET_IMAGE_INFO)
            rpc_protocol.set_attribute("filename", consts.AttributeType.AT_FILENAME, filepath)
            self.a_channel_format_enum_items_str = OctaneServer().handle_rpc(rpc_protocol)
        else:
            self.a_channel_format_enum_items_str = ""
        if self.a_channel_format == "":
            self.a_channel_format = "Automatic"
    
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
    
    image: PointerProperty(type=bpy.types.Image, update=update_image)
    a_channel_format: EnumProperty(name="Import format", update=update_image, description="", items=get_a_channel_format_enum_items)
    
    def auto_refresh(self):
        return self.image and self.image.source in ("SEQUENCE", "MOVIE") and self.use_auto_refresh
    
    def refresh_image_data(self, frame_current):
        if not self.auto_refresh():
            return
        self.is_image_data_updated = True
        if self.image.source == "MOVIE":
            self.image.gl_free()
            self.image.gl_touch(frame=frame_current)
        self.update()

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
                frame %= self.frame_duration
                if frame == 0: 
                    frame = self.frame_duration
            else:
                frame = self.frame_duration
        frame += self.frame_offset
        if frame == 0 and self.use_cyclic:
            frame = self.frame_duration
        return frame

    def _update_image_filepath(self, rpc_protocol, frame_current):
        if not self.image:
            return
        if self.image.source not in ("FILE", "SEQUENCE", ):
            return
        if self.image.source == "SEQUENCE" and self.use_auto_refresh:
            temp_image_texture_name = "[OctaneTempImageTexture]" + self.image.name
            temp_image_texture = bpy.data.textures.new(temp_image_texture_name, "IMAGE")            
            temp_image_texture.image_user.frame_current = self.get_frame(frame_current)
            filepath = self.image.filepath_from_user(image_user=temp_image_texture.image_user)
            bpy.data.textures.remove(temp_image_texture)
        else:
            filepath = self.image.filepath_from_user()
        rpc_protocol.set_attribute("a_filename", consts.AttributeType.AT_FILENAME, filepath)
    
    def _update_pixel_image(self, rpc_protocol, frame_current):      
        if not self.image:
            return
        if self.image.source not in ("MOVIE", "GENERATED", ):
            return
        if self.image.source == "MOVIE":
            self.refresh_image_data(self.get_frame(frame_current))
        if len(self.image.pixels):
            rpc_protocol.require_float_c_array(len(self.image.pixels))
            self.image.pixels.foreach_get(rpc_protocol.c_array)
        rpc_protocol.set_attribute("a_size", consts.AttributeType.AT_INT2, self.image.size)
    
    def sync_custom_data(self, rpc_protocol, scene):
        if not self.is_image_data_updated:
            return        
        frame_current = 0
        if scene:
            frame_current = scene.frame_current
        if self.image.source in ("FILE", "SEQUENCE", ):
            self._update_image_filepath(rpc_protocol, frame_current)
        elif self.image.source in ("MOVIE", "GENERATED") and len(self.image.pixels):
            self._update_pixel_image(rpc_protocol, frame_current)
        self.is_image_data_updated = False

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
        if self.image and self.image.source in ("SEQUENCE", "MOVIE"):
            box = col.box()
            sub = box.column(align=True)
            sub.label(text="Frame: %d" % self.get_frame(context.scene.frame_current))
            sub.prop(self, "frame_duration")
            sub.prop(self, "frame_start")
            sub.prop(self, "frame_offset")
            sub.prop(self, "use_cyclic")
            sub.prop(self, "use_auto_refresh")


_CLASSES = [
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))