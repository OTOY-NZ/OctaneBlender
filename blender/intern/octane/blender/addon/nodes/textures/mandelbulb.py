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


class OctaneMandelbulbIterationCount(OctaneBaseSocket):
    bl_idname="OctaneMandelbulbIterationCount"
    bl_label="Iterations"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_ITERATION_COUNT
    octane_pin_name="iterationCount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The number of fractal iterations", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMandelbulbPower(OctaneBaseSocket):
    bl_idname="OctaneMandelbulbPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="", min=-100.000000, max=100.000000, soft_min=-100.000000, soft_max=100.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMandelbulbThreshold(OctaneBaseSocket):
    bl_idname="OctaneMandelbulbThreshold"
    bl_label="Bailout"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THRESHOLD
    octane_pin_name="threshold"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=20.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMandelbulbTransform(OctaneBaseSocket):
    bl_idname="OctaneMandelbulbTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMandelbulbProjection(OctaneBaseSocket):
    bl_idname="OctaneMandelbulbProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMandelbulb(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMandelbulb"
    bl_label="Mandelbulb"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneMandelbulbIterationCount,OctaneMandelbulbPower,OctaneMandelbulbThreshold,OctaneMandelbulbTransform,OctaneMandelbulbProjection,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_TEX_MANDELBULB
    octane_socket_list=["Iterations", "Power", "Bailout", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneMandelbulbIterationCount", OctaneMandelbulbIterationCount.bl_label).init()
        self.inputs.new("OctaneMandelbulbPower", OctaneMandelbulbPower.bl_label).init()
        self.inputs.new("OctaneMandelbulbThreshold", OctaneMandelbulbThreshold.bl_label).init()
        self.inputs.new("OctaneMandelbulbTransform", OctaneMandelbulbTransform.bl_label).init()
        self.inputs.new("OctaneMandelbulbProjection", OctaneMandelbulbProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMandelbulbIterationCount,
    OctaneMandelbulbPower,
    OctaneMandelbulbThreshold,
    OctaneMandelbulbTransform,
    OctaneMandelbulbProjection,
    OctaneMandelbulb,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
