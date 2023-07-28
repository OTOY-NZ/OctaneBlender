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


class OctaneFilmSettingsResolution(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsResolution"
    bl_label="Resolution"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_IMAGE_RESOLUTION
    octane_default_node_name="OctaneImageResolution"
    octane_pin_id=consts.PinID.P_RESOLUTION
    octane_pin_name="resolution"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(1024, 512), update=OctaneBaseSocket.update_node_tree, description="Resolution of the render result", min=4, max=65536, soft_min=4, soft_max=65536, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionOffset(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionOffset"
    bl_label="Region start"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_REGION_OFFSET
    octane_pin_name="regionOffset"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(0, 0), update=OctaneBaseSocket.update_node_tree, description="The start coordinate where the render region starts", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionSize(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionSize"
    bl_label="Region size"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_REGION_SIZE
    octane_pin_name="regionSize"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(65536, 65536), update=OctaneBaseSocket.update_node_tree, description="The size of the render region", min=1, max=65536, soft_min=1, soft_max=65536, step=1, subtype="NONE", size=2)
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
    octane_socket_class_list=[OctaneFilmSettingsResolution,OctaneFilmSettingsRegionOffset,OctaneFilmSettingsRegionSize,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_FILM_SETTINGS
    octane_socket_list=["Resolution", "Region start", "Region size", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneFilmSettingsResolution", OctaneFilmSettingsResolution.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionOffset", OctaneFilmSettingsRegionOffset.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionSize", OctaneFilmSettingsRegionSize.bl_label).init()
        self.outputs.new("OctaneFilmSettingsOutSocket", "Film settings out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
