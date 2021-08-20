##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneChannelMapperTexture(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperTexture"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex"
    bl_label="Red channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="The input channel index to map to the red output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex2(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex2"
    bl_label="Green channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="The input channel index to map to the green output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapperIndex3(OctaneBaseSocket):
    bl_idname="OctaneChannelMapperIndex3"
    bl_label="Blue channel index"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=2, update=None, description="The input channel index to map to the blue output channel", min=0, max=2, soft_min=0, soft_max=2, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelMapper(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneChannelMapper"
    bl_label="Channel mapper"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=175)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Red channel index;Green channel index;Blue channel index;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneChannelMapperTexture", OctaneChannelMapperTexture.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex", OctaneChannelMapperIndex.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex2", OctaneChannelMapperIndex2.bl_label).init()
        self.inputs.new("OctaneChannelMapperIndex3", OctaneChannelMapperIndex3.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneChannelMapperTexture,
    OctaneChannelMapperIndex,
    OctaneChannelMapperIndex2,
    OctaneChannelMapperIndex3,
    OctaneChannelMapper,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
