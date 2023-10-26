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

class OctaneFilmSettingsRegionOffsetRelative(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionOffsetRelative"
    bl_label="Region start"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_REGION_OFFSET_RELATIVE
    octane_pin_name="regionOffsetRelative"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The relative start coordinate where the render region starts in percent. This input exists only to control the absolute region start in pixels, but is not used directly in the render settings.\n\nThe calculated absolute start position in pixels will be rounded down", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=13000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionSizeRelative(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionSizeRelative"
    bl_label="Region size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_REGION_SIZE_RELATIVE
    octane_pin_name="regionSizeRelative"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The relative size of the render region in percent. This input exists only to control the absolute region size in pixels, but is not used directly in the render settings.\n\nThe absolute size in pixels will be rounded up", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=13000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionOffset(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionOffset"
    bl_label="Region start (pixel)"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_REGION_OFFSET
    octane_pin_name="regionOffset"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(0, 0), update=OctaneBaseSocket.update_node_tree, description="The absolute start coordinate where the render region starts in pixels", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFilmSettingsRegionSize(OctaneBaseSocket):
    bl_idname="OctaneFilmSettingsRegionSize"
    bl_label="Region size (pixel)"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_REGION_SIZE
    octane_pin_name="regionSize"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(65536, 65536), update=OctaneBaseSocket.update_node_tree, description="The absolute size of the render region in pixels", min=1, max=65536, soft_min=1, soft_max=65536, step=1, subtype="NONE", size=2)
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
    octane_socket_class_list=[OctaneFilmSettingsResolution,OctaneFilmSettingsRegionOffsetRelative,OctaneFilmSettingsRegionSizeRelative,OctaneFilmSettingsRegionOffset,OctaneFilmSettingsRegionSize,]
    octane_min_version=3000013
    octane_node_type=consts.NodeType.NT_FILM_SETTINGS
    octane_socket_list=["Resolution", "Region start", "Region size", "Region start (pixel)", "Region size (pixel)", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneFilmSettingsResolution", OctaneFilmSettingsResolution.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionOffsetRelative", OctaneFilmSettingsRegionOffsetRelative.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionSizeRelative", OctaneFilmSettingsRegionSizeRelative.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionOffset", OctaneFilmSettingsRegionOffset.bl_label).init()
        self.inputs.new("OctaneFilmSettingsRegionSize", OctaneFilmSettingsRegionSize.bl_label).init()
        self.outputs.new("OctaneFilmSettingsOutSocket", "Film settings out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneFilmSettingsResolution,
    OctaneFilmSettingsRegionOffsetRelative,
    OctaneFilmSettingsRegionSizeRelative,
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
