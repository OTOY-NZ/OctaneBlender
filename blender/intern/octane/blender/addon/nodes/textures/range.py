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


class OctaneRangeInput(OctaneBaseSocket):
    bl_idname="OctaneRangeInput"
    bl_label="Value"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneRangeInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_TYPE
    octane_pin_name="interpolationType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear", "Linear", "", 0),
        ("Smoothstep", "Smoothstep", "", 2),
        ("Smootherstep", "Smootherstep", "", 3),
        ("Steps", "Steps", "", 1),
        ("Posterize", "Posterize", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="The type of interpolation to perform", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInputMin(OctaneBaseSocket):
    bl_idname="OctaneRangeInputMin"
    bl_label="Input min"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_INPUT_MIN
    octane_pin_name="inputMin"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Input min", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInputMax(OctaneBaseSocket):
    bl_idname="OctaneRangeInputMax"
    bl_label="Input max"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_INPUT_MAX
    octane_pin_name="inputMax"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Input max", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeOutputMin(OctaneBaseSocket):
    bl_idname="OctaneRangeOutputMin"
    bl_label="Output min"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OUTPUT_MIN
    octane_pin_name="outputMin"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Output min", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeOutputMax(OctaneBaseSocket):
    bl_idname="OctaneRangeOutputMax"
    bl_label="Output max"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OUTPUT_MAX
    octane_pin_name="outputMax"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Output max", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeInterpolationSteps(OctaneBaseSocket):
    bl_idname="OctaneRangeInterpolationSteps"
    bl_label="Levels"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INTERPOLATION_STEPS
    octane_pin_name="interpolationSteps"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Number of distinct output levels per channel. Only active when using the Steps or Posterize interpolation methods", min=1, max=2147483647, soft_min=2, soft_max=256, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRangeClamp(OctaneBaseSocket):
    bl_idname="OctaneRangeClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CLAMP
    octane_pin_name="clamp"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Clamp the input to the input range. Interpolation modes other than Linear are always clamped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRange(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRange"
    bl_label="Range"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRangeInput,OctaneRangeInterpolationType,OctaneRangeInputMin,OctaneRangeInputMax,OctaneRangeOutputMin,OctaneRangeOutputMax,OctaneRangeInterpolationSteps,OctaneRangeClamp,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_RANGE
    octane_socket_list=["Value", "Interpolation", "Input min", "Input max", "Output min", "Output max", "Levels", "Clamp", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=8

    compatibility_mode_infos=[
        ("Latest (2022.1)", "Latest (2022.1)", """(null)""", 12000005),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """The Steps interpolation type produces more distinct output values than requested by Levels if the input values are inclusive of "Input max", or if Clamp is disabled and the input contains values outside of the specified input range.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2022.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=12000200, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneRangeInput", OctaneRangeInput.bl_label).init()
        self.inputs.new("OctaneRangeInterpolationType", OctaneRangeInterpolationType.bl_label).init()
        self.inputs.new("OctaneRangeInputMin", OctaneRangeInputMin.bl_label).init()
        self.inputs.new("OctaneRangeInputMax", OctaneRangeInputMax.bl_label).init()
        self.inputs.new("OctaneRangeOutputMin", OctaneRangeOutputMin.bl_label).init()
        self.inputs.new("OctaneRangeOutputMax", OctaneRangeOutputMax.bl_label).init()
        self.inputs.new("OctaneRangeInterpolationSteps", OctaneRangeInterpolationSteps.bl_label).init()
        self.inputs.new("OctaneRangeClamp", OctaneRangeClamp.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRangeInput,
    OctaneRangeInterpolationType,
    OctaneRangeInputMin,
    OctaneRangeInputMax,
    OctaneRangeOutputMin,
    OctaneRangeOutputMax,
    OctaneRangeInterpolationSteps,
    OctaneRangeClamp,
    OctaneRange,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneRange_Override(OctaneRange):

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")

utility.override_class(_CLASSES, OctaneRange, OctaneRange_Override) 