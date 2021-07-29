##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSunDirectionLatitude(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionLatitude"
    bl_label = "Latitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=91)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=-37.043659, description="Latitude of the location", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, subtype="FACTOR")

class OctaneSunDirectionLongitude(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionLongitude"
    bl_label = "Longitude"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=99)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=174.509171, description="Longitude of the location", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, subtype="FACTOR")

class OctaneSunDirectionMonth(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionMonth"
    bl_label = "Month"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=115)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=3, description="Month of the time the sun direction should be calculated for", min=1, max=12, soft_min=1, soft_max=12, step=1, subtype="FACTOR")

class OctaneSunDirectionDay(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionDay"
    bl_label = "Day"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=27)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Day of the month of the time the sun direction should be calculated for", min=1, max=31, soft_min=1, soft_max=31, step=1, subtype="FACTOR")

class OctaneSunDirectionHour(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionHour"
    bl_label = "Local time"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=75)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=10.000000, description="The local time as hours since 0:00", min=0.000000, max=24.000000, soft_min=0.000000, soft_max=24.000000, step=1, subtype="FACTOR")

class OctaneSunDirectionGmtoffset(OctaneBaseSocket):
    bl_idname = "OctaneSunDirectionGmtoffset"
    bl_label = "GMT offset"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=67)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=12, description="The time zone as offset to GMT", min=-12, max=12, soft_min=-12, soft_max=12, step=1, subtype="FACTOR")

class OctaneSunDirection(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSunDirection"
    bl_label = "Sun direction"
    octane_node_type: IntProperty(name="Octane Node Type", default=30)
    octane_socket_list: StringProperty(name="Socket List", default="Latitude;Longitude;Month;Day;Local time;GMT offset;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSunDirectionLatitude", OctaneSunDirectionLatitude.bl_label)
        self.inputs.new("OctaneSunDirectionLongitude", OctaneSunDirectionLongitude.bl_label)
        self.inputs.new("OctaneSunDirectionMonth", OctaneSunDirectionMonth.bl_label)
        self.inputs.new("OctaneSunDirectionDay", OctaneSunDirectionDay.bl_label)
        self.inputs.new("OctaneSunDirectionHour", OctaneSunDirectionHour.bl_label)
        self.inputs.new("OctaneSunDirectionGmtoffset", OctaneSunDirectionGmtoffset.bl_label)
        self.outputs.new("OctaneFloatOutSocket", "Float out")


def register():
    register_class(OctaneSunDirectionLatitude)
    register_class(OctaneSunDirectionLongitude)
    register_class(OctaneSunDirectionMonth)
    register_class(OctaneSunDirectionDay)
    register_class(OctaneSunDirectionHour)
    register_class(OctaneSunDirectionGmtoffset)
    register_class(OctaneSunDirection)

def unregister():
    unregister_class(OctaneSunDirection)
    unregister_class(OctaneSunDirectionGmtoffset)
    unregister_class(OctaneSunDirectionHour)
    unregister_class(OctaneSunDirectionDay)
    unregister_class(OctaneSunDirectionMonth)
    unregister_class(OctaneSunDirectionLongitude)
    unregister_class(OctaneSunDirectionLatitude)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
