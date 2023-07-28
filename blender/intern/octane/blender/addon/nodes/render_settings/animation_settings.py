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


class OctaneAnimationSettingsShutterAlignment(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsShutterAlignment"
    bl_label="Shutter alignment"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_SHUTTER_ALIGNMENT
    octane_pin_name="shutterAlignment"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Before", "Before", "", 1),
        ("Symmetric", "Symmetric", "", 2),
        ("After", "After", "", 3),
    ]
    default_value: EnumProperty(default="After", update=OctaneBaseSocket.update_node_tree, description="Specifies how the shutter interval is aligned to the current time", items=items)
    octane_hide_value=False
    octane_min_version=3000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsShutterTime(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsShutterTime"
    bl_label="Shutter time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SHUTTER_TIME
    octane_pin_name="shutterTime"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="The shutter time percentage relative to the duration of a single frame", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsSubFrameStart(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsSubFrameStart"
    bl_label="Subframe start"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUBFRAME_START
    octane_pin_name="subFrameStart"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Minimum sub-frame % time to sample", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsSubFrameEnd(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsSubFrameEnd"
    bl_label="Subframe end"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUBFRAME_END
    octane_pin_name="subFrameEnd"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Maximum sub-frame % time to sample", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettings(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAnimationSettings"
    bl_label="Animation settings"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneAnimationSettingsShutterAlignment,OctaneAnimationSettingsShutterTime,OctaneAnimationSettingsSubFrameStart,OctaneAnimationSettingsSubFrameEnd,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_ANIMATION_SETTINGS
    octane_socket_list=["Shutter alignment", "Shutter time", "Subframe start", "Subframe end", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneAnimationSettingsShutterAlignment", OctaneAnimationSettingsShutterAlignment.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsShutterTime", OctaneAnimationSettingsShutterTime.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsSubFrameStart", OctaneAnimationSettingsSubFrameStart.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsSubFrameEnd", OctaneAnimationSettingsSubFrameEnd.bl_label).init()
        self.outputs.new("OctaneAnimationSettingsOutSocket", "Animation settings out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneAnimationSettingsShutterAlignment,
    OctaneAnimationSettingsShutterTime,
    OctaneAnimationSettingsSubFrameStart,
    OctaneAnimationSettingsSubFrameEnd,
    OctaneAnimationSettings,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
