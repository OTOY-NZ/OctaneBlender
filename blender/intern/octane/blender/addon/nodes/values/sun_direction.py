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


class OctaneSunDirectionLatitude(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionLatitude"
    bl_label="Latitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=91)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="latitude")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=-37.043659, update=OctaneBaseSocket.update_node_tree, description="Latitude of the location", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=4, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionLongitude(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionLongitude"
    bl_label="Longitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=99)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="longitude")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=174.509171, update=OctaneBaseSocket.update_node_tree, description="Longitude of the location", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, precision=4, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionMonth(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionMonth"
    bl_label="Month"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=115)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="month")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=3, update=OctaneBaseSocket.update_node_tree, description="Month of the time the sun direction should be calculated for", min=1, max=12, soft_min=1, soft_max=12, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionDay(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionDay"
    bl_label="Day"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=27)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="day")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Day of the month of the time the sun direction should be calculated for", min=1, max=31, soft_min=1, soft_max=31, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionHour(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionHour"
    bl_label="Local time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=75)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="hour")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The local time as hours since 0:00", min=0.000000, max=24.000000, soft_min=0.000000, soft_max=24.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirectionGmtoffset(OctaneBaseSocket):
    bl_idname="OctaneSunDirectionGmtoffset"
    bl_label="GMT offset"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=67)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="gmtoffset")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=12, update=OctaneBaseSocket.update_node_tree, description="The time zone as offset to GMT", min=-12, max=12, soft_min=-12, soft_max=12, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSunDirection(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSunDirection"
    bl_label="Sun direction"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=30)
    octane_socket_list: StringProperty(name="Socket List", default="Latitude;Longitude;Month;Day;Local time;GMT offset;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="8;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=6)

    a_value: FloatVectorProperty(name="Value", default=(0.617750, 0.703410, -0.351568), size=3, update=OctaneBaseNode.update_node_tree, description="The direction calculated from the input pins of the node (normalized)")

    def init(self, context):
        self.inputs.new("OctaneSunDirectionLatitude", OctaneSunDirectionLatitude.bl_label).init()
        self.inputs.new("OctaneSunDirectionLongitude", OctaneSunDirectionLongitude.bl_label).init()
        self.inputs.new("OctaneSunDirectionMonth", OctaneSunDirectionMonth.bl_label).init()
        self.inputs.new("OctaneSunDirectionDay", OctaneSunDirectionDay.bl_label).init()
        self.inputs.new("OctaneSunDirectionHour", OctaneSunDirectionHour.bl_label).init()
        self.inputs.new("OctaneSunDirectionGmtoffset", OctaneSunDirectionGmtoffset.bl_label).init()
        self.outputs.new("OctaneFloatOutSocket", "Float out").init()


_CLASSES=[
    OctaneSunDirectionLatitude,
    OctaneSunDirectionLongitude,
    OctaneSunDirectionMonth,
    OctaneSunDirectionDay,
    OctaneSunDirectionHour,
    OctaneSunDirectionGmtoffset,
    OctaneSunDirection,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

from ...utils import utility

class OctaneSunDirection_Override(OctaneSunDirection):
    octane_attribute_list: StringProperty(name="Attribute List", default="")

utility.override_class(_CLASSES, OctaneSunDirection, OctaneSunDirection_Override)  