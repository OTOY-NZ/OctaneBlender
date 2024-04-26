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


class OctaneCustomLUTStrength(OctaneBaseSocket):
    bl_idname="OctaneCustomLUTStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The amount how much the LUT should be applied", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomLUT(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCustomLUT"
    bl_label="Custom LUT"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCustomLUTStrength,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_LUT_CUSTOM
    octane_socket_list=["Strength", ]
    octane_attribute_list=["a_filename", "a_reload", "a_title", "a_domain_min_1d", "a_domain_max_1d", "a_values_1d", "a_domain_min_3d", "a_domain_max_3d", "a_values_3d", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_title": [consts.AttributeID.A_TITLE, "title", consts.AttributeType.AT_STRING], "a_domain_min_1d": [consts.AttributeID.A_DOMAIN_MIN_1D, "domainMin1D", consts.AttributeType.AT_FLOAT3], "a_domain_max_1d": [consts.AttributeID.A_DOMAIN_MAX_1D, "domainMax1D", consts.AttributeType.AT_FLOAT3], "a_values_1d": [consts.AttributeID.A_VALUES_1D, "values1d", consts.AttributeType.AT_FLOAT3], "a_domain_min_3d": [consts.AttributeID.A_DOMAIN_MIN_3D, "domainMin3D", consts.AttributeType.AT_FLOAT3], "a_domain_max_3d": [consts.AttributeID.A_DOMAIN_MAX_3D, "domainMax3D", consts.AttributeType.AT_FLOAT3], "a_values_3d": [consts.AttributeID.A_VALUES_3D, "values3d", consts.AttributeType.AT_FLOAT3], }
    octane_static_pin_count=1

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the filename of the LUT", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_title: StringProperty(name="Title", default="", update=OctaneBaseNode.update_node_tree, description="The title stored in the LUT file")
    a_domain_min_1d: FloatVectorProperty(name="Domain min 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 1D look up table")
    a_domain_max_1d: FloatVectorProperty(name="Domain max 1d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 1D look up table")
    a_values_1d: FloatVectorProperty(name="Values 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The (XYZ or RGB) output values of the 1D look up table corresponding to input values that are equidistantly distributed between the A_DOMAIN_MIN_1D and A_DOMAIN_MAX_1D.\n\nNeeds to have a size >= 2")
    a_domain_min_3d: FloatVectorProperty(name="Domain min 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 3D look up table")
    a_domain_max_3d: FloatVectorProperty(name="Domain max 3d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 3D look up table")
    a_values_3d: FloatVectorProperty(name="Values 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Array storing the 3D LUT cube. Its size must be the cube of an integral number.\nThe order of the grid values is that the first dimension (X or red) changes fastest and the last dimension (Z or blue) changes slowest.\n\nNeeds to have a size >= 8")

    def init(self, context):
        self.inputs.new("OctaneCustomLUTStrength", OctaneCustomLUTStrength.bl_label).init()
        self.outputs.new("OctaneLUTOutSocket", "LUT out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCustomLUTStrength,
    OctaneCustomLUT,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
