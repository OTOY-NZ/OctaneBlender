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


class OctaneRotationRotationOrder(OctaneBaseSocket):
    bl_idname="OctaneRotationRotationOrder"
    bl_label="Order"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_ROTATION_ORDER
    octane_pin_name="rotationOrder"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("XYZ", "XYZ", "", 0),
        ("XZY", "XZY", "", 1),
        ("YXZ", "YXZ", "", 2),
        ("YZX", "YZX", "", 3),
        ("ZXY", "ZXY", "", 4),
        ("ZYX", "ZYX", "", 5),
    ]
    default_value: EnumProperty(default="YXZ", update=OctaneBaseSocket.update_node_tree, description="Provides the rotation order that is used when the transformation matrix calculated", items=items)
    octane_hide_value=False
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRotationRotation(OctaneBaseSocket):
    bl_idname="OctaneRotationRotation"
    bl_label="Angles"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROTATION
    octane_pin_name="rotation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Provides the X/Y/Z rotation angles", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRotation(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRotation"
    bl_label="Rotation Transform"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRotationRotationOrder,OctaneRotationRotation,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TRANSFORM_ROTATION
    octane_socket_list=["Order", "Angles", ]
    octane_attribute_list=[]
    octane_attribute_config={"a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneRotationRotationOrder", OctaneRotationRotationOrder.bl_label).init()
        self.inputs.new("OctaneRotationRotation", OctaneRotationRotation.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRotationRotationOrder,
    OctaneRotationRotation,
    OctaneRotation,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
