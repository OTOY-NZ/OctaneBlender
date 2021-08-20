##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneAnimationSettingsShutterAlignment(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsShutterAlignment"
    bl_label="Shutter alignment"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=304)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Before", "Before", "", 1),
        ("Symmetric", "Symmetric", "", 2),
        ("After", "After", "", 3),
    ]
    default_value: EnumProperty(default="After", update=None, description="Specifies how the shutter interval is aligned to the current time", items=items)
    octane_hide_value=False
    octane_min_version=3000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsShutterTime(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsShutterTime"
    bl_label="Shutter time"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=305)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.200000, update=None, description="The shutter time percentage relative to the duration of a single frame", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsSubFrameStart(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsSubFrameStart"
    bl_label="Subframe start"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=308)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Minimum sub-frame % time to sample", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnimationSettingsSubFrameEnd(OctaneBaseSocket):
    bl_idname="OctaneAnimationSettingsSubFrameEnd"
    bl_label="Subframe end"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=309)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Maximum sub-frame % time to sample", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="PERCENTAGE")
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
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=99)
    octane_socket_list: StringProperty(name="Socket List", default="Shutter alignment;Shutter time;Subframe start;Subframe end;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneAnimationSettingsShutterAlignment", OctaneAnimationSettingsShutterAlignment.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsShutterTime", OctaneAnimationSettingsShutterTime.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsSubFrameStart", OctaneAnimationSettingsSubFrameStart.bl_label).init()
        self.inputs.new("OctaneAnimationSettingsSubFrameEnd", OctaneAnimationSettingsSubFrameEnd.bl_label).init()
        self.outputs.new("OctaneAnimationSettingsOutSocket", "Animation settings out").init()


_classes=[
    OctaneAnimationSettingsShutterAlignment,
    OctaneAnimationSettingsShutterTime,
    OctaneAnimationSettingsSubFrameStart,
    OctaneAnimationSettingsSubFrameEnd,
    OctaneAnimationSettings,
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
