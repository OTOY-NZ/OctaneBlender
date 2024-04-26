##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneOutputAOVsApplyLUTEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyLUTEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyLUTStrength(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyLUTStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The extent to which the LUT should be applied. The output of this operation is linearly interpolated between the input and the LUT output based on this value", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyLUTInputColorSpace(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyLUTInputColorSpace"
    bl_label="Input color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INPUT_COLOR_SPACE
    octane_pin_name="inputColorSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("sRGB", "sRGB", "", 1),
        ("Linear sRGB", "Linear sRGB", "", 2),
    ]
    default_value: EnumProperty(default="sRGB", update=OctaneBaseSocket.update_node_tree, description="The color space that the LUT requires for input", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyLUTOutputColorSpace(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyLUTOutputColorSpace"
    bl_label="Output color space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OUTPUT_COLOR_SPACE
    octane_pin_name="outputColorSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("sRGB", "sRGB", "", 1),
        ("Linear sRGB", "Linear sRGB", "", 2),
    ]
    default_value: EnumProperty(default="sRGB", update=OctaneBaseSocket.update_node_tree, description="The color space that the LUT produces for output", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyLUT(bpy.types.Node, OctaneBaseLutNode):
    bl_idname="OctaneOutputAOVsApplyLUT"
    bl_label="Apply LUT"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsApplyLUTEnabled,OctaneOutputAOVsApplyLUTStrength,OctaneOutputAOVsApplyLUTInputColorSpace,OctaneOutputAOVsApplyLUTOutputColorSpace,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_APPLY_LUT
    octane_socket_list=["Enabled", "Strength", "Input color space", "Output color space", ]
    octane_attribute_list=["a_title", "a_domain_min_1d", "a_domain_max_1d", "a_values_1d", "a_domain_min_3d", "a_domain_max_3d", "a_values_3d", "a_filename", "a_reload", ]
    octane_attribute_config={"a_title": [consts.AttributeID.A_TITLE, "title", consts.AttributeType.AT_STRING], "a_domain_min_1d": [consts.AttributeID.A_DOMAIN_MIN_1D, "domainMin1D", consts.AttributeType.AT_FLOAT3], "a_domain_max_1d": [consts.AttributeID.A_DOMAIN_MAX_1D, "domainMax1D", consts.AttributeType.AT_FLOAT3], "a_values_1d": [consts.AttributeID.A_VALUES_1D, "values1d", consts.AttributeType.AT_FLOAT3], "a_domain_min_3d": [consts.AttributeID.A_DOMAIN_MIN_3D, "domainMin3D", consts.AttributeType.AT_FLOAT3], "a_domain_max_3d": [consts.AttributeID.A_DOMAIN_MAX_3D, "domainMax3D", consts.AttributeType.AT_FLOAT3], "a_values_3d": [consts.AttributeID.A_VALUES_3D, "values3d", consts.AttributeType.AT_FLOAT3], "a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], }
    octane_static_pin_count=4

    a_title: StringProperty(name="Title", default="", update=OctaneBaseNode.update_node_tree, description="The title stored in the LUT file")
    a_domain_min_1d: FloatVectorProperty(name="Domain min 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 1D look up table")
    a_domain_max_1d: FloatVectorProperty(name="Domain max 1d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 1D look up table")
    a_values_1d: FloatVectorProperty(name="Values 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The (XYZ or RGB) output values of the 1D look up table corresponding to input values that are equidistantly distributed between the A_DOMAIN_MIN_1D and A_DOMAIN_MAX_1D.\n\nNeeds to have a size >= 2")
    a_domain_min_3d: FloatVectorProperty(name="Domain min 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 3D look up table")
    a_domain_max_3d: FloatVectorProperty(name="Domain max 3d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 3D look up table")
    a_values_3d: FloatVectorProperty(name="Values 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Array storing the 3D LUT cube. Its size must be the cube of an integral number.\nThe order of the grid values is that the first dimension (X or red) changes fastest and the last dimension (Z or blue) changes slowest.\n\nNeeds to have a size >= 8")
    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the filename of the LUT", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set to true if the file needs a reload. After evaluation the attribute will be false again")

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsApplyLUTEnabled", OctaneOutputAOVsApplyLUTEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyLUTStrength", OctaneOutputAOVsApplyLUTStrength.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyLUTInputColorSpace", OctaneOutputAOVsApplyLUTInputColorSpace.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyLUTOutputColorSpace", OctaneOutputAOVsApplyLUTOutputColorSpace.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsApplyLUTEnabled,
    OctaneOutputAOVsApplyLUTStrength,
    OctaneOutputAOVsApplyLUTInputColorSpace,
    OctaneOutputAOVsApplyLUTOutputColorSpace,
    OctaneOutputAOVsApplyLUT,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneOutputAOVsApplyLUT.update_node_definition()