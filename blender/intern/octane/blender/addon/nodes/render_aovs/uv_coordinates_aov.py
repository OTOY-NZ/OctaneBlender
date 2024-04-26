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


class OctaneUVCoordinatesAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneUVCoordinatesAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUVCoordinatesAOVUVMax(OctaneBaseSocket):
    bl_idname="OctaneUVCoordinatesAOVUVMax"
    bl_label="UV max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_UV_MAX
    octane_pin_name="UV_max"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUVCoordinatesAOVUvSet(OctaneBaseSocket):
    bl_idname="OctaneUVCoordinatesAOVUvSet"
    bl_label="UV coordinate selection"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_UV_SET
    octane_pin_name="uvSet"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUVCoordinatesAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUVCoordinatesAOV"
    bl_label="UV coordinates AOV"
    bl_width_default=200
    octane_render_pass_id=1005
    octane_render_pass_name="UV coordinates"
    octane_render_pass_short_name="UV"
    octane_render_pass_description="Assigns RGB values according to the geometry's texture coordinates"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUVCoordinatesAOVEnabled,OctaneUVCoordinatesAOVUVMax,OctaneUVCoordinatesAOVUvSet,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_UV_COORD
    octane_socket_list=["Enabled", "UV max", "UV coordinate selection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneUVCoordinatesAOVEnabled", OctaneUVCoordinatesAOVEnabled.bl_label).init()
        self.inputs.new("OctaneUVCoordinatesAOVUVMax", OctaneUVCoordinatesAOVUVMax.bl_label).init()
        self.inputs.new("OctaneUVCoordinatesAOVUvSet", OctaneUVCoordinatesAOVUvSet.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneUVCoordinatesAOVEnabled,
    OctaneUVCoordinatesAOVUVMax,
    OctaneUVCoordinatesAOVUvSet,
    OctaneUVCoordinatesAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
