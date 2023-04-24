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


class OctaneChannelPickerTexture(OctaneBaseSocket):
    bl_idname="OctaneChannelPickerTexture"
    bl_label="Input"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelPickerColorChannel(OctaneBaseSocket):
    bl_idname="OctaneChannelPickerColorChannel"
    bl_label="Channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=618)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="colorChannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("R", "R", "", 0),
        ("G", "G", "", 1),
        ("B", "B", "", 2),
    ]
    default_value: EnumProperty(default="R", update=OctaneBaseSocket.update_node_tree, description="The color channel to pass through to the output texture", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneChannelPicker(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneChannelPicker"
    bl_label="Channel picker"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=171)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneChannelPickerTexture", OctaneChannelPickerTexture.bl_label).init()
        self.inputs.new("OctaneChannelPickerColorChannel", OctaneChannelPickerColorChannel.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneChannelPickerTexture,
    OctaneChannelPickerColorChannel,
    OctaneChannelPicker,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
