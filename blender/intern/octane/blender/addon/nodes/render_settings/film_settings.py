##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneFilmSettingsResolution(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsResolution"
    bl_label="Resolution"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneImageResolution"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=198)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(1024, 512), update=None, description="Resolution of the render result", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionOffset(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionOffset"
    bl_label="Region start"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=312)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(0, 0), update=None, description="The start coordinate where the render region starts", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionSize(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionSize"
    bl_label="Region size"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=313)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(65536, 65536), update=None, description="The size of the render region", min=1, max=65536, soft_min=1, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettings(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFilmSettings"
    bl_label="Film settings"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=100)
    octane_socket_list: StringProperty(name="Socket List", default="Resolution;Region start;Region size;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneFilmSettingsResolution", OctaneFilmSettingsResolution.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionOffset", OctaneFilmSettingsRegionOffset.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionSize", OctaneFilmSettingsRegionSize.bl_label).init()
        self.outputs.new("OctaneFilmSettingsOutSocket", "Film settings out").init()


_CLASSES=[
    OctaneFilmSettingsResolution,
    OctaneFilmSettingsRegionOffset,
    OctaneFilmSettingsRegionSize,
    OctaneFilmSettings,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
