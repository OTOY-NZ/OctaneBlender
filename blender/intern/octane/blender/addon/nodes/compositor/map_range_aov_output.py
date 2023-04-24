##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneMapRangeAOVOutputInput(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputInput"
    bl_label="Input"
    color=consts.OctanePinColor.AOVOutput
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputInputMin(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputInputMin"
    bl_label="Input minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=662)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The start value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputInputMax(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputInputMax"
    bl_label="Input maximum"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=663)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The end value of the input range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputOutputMin(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputOutputMin"
    bl_label="Output minimum"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=664)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="The start value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputOutputMax(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputOutputMax"
    bl_label="Output maximum"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=665)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The end value of the output range", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputClamp(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=628)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled,  the values are clamped to the minimum and maximum range. Otherwise values which are outside the range will be untouched")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutputColorChannelGroup(OctaneBaseSocket):
    bl_idname="OctaneMapRangeAOVOutputColorChannelGroup"
    bl_label="Channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=668)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGB", update=None, description="Select channels on which the map range operation should be performed", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMapRangeAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMapRangeAOVOutput"
    bl_label="Map range AOV output"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=375)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Input minimum;Input maximum;Output minimum;Output maximum;Clamp;Channels;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=7)

    def init(self, context):
        self.inputs.new("OctaneMapRangeAOVOutputInput", OctaneMapRangeAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputInputMin", OctaneMapRangeAOVOutputInputMin.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputInputMax", OctaneMapRangeAOVOutputInputMax.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputOutputMin", OctaneMapRangeAOVOutputOutputMin.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputOutputMax", OctaneMapRangeAOVOutputOutputMax.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputClamp", OctaneMapRangeAOVOutputClamp.bl_label).init()
        self.inputs.new("OctaneMapRangeAOVOutputColorChannelGroup", OctaneMapRangeAOVOutputColorChannelGroup.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out").init()


_CLASSES=[
    OctaneMapRangeAOVOutputInput,
    OctaneMapRangeAOVOutputInputMin,
    OctaneMapRangeAOVOutputInputMax,
    OctaneMapRangeAOVOutputOutputMin,
    OctaneMapRangeAOVOutputOutputMax,
    OctaneMapRangeAOVOutputClamp,
    OctaneMapRangeAOVOutputColorChannelGroup,
    OctaneMapRangeAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
