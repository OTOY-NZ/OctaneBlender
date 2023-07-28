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


class Octane2DTransformationRotation(OctaneBaseSocket):
    bl_idname="Octane2DTransformationRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROTATION
    octane_pin_name="rotation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-360.000000, soft_max=360.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class Octane2DTransformationScale(OctaneBaseSocket):
    bl_idname="Octane2DTransformationScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Scale", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", precision=3, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class Octane2DTransformationTranslation(OctaneBaseSocket):
    bl_idname="Octane2DTransformationTranslation"
    bl_label="Translation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TRANSLATION
    octane_pin_name="translation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class Octane2DTransformation(bpy.types.Node, OctaneBaseNode):
    bl_idname="Octane2DTransformation"
    bl_label="2D transformation"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[Octane2DTransformationRotation,Octane2DTransformationScale,Octane2DTransformationTranslation,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TRANSFORM_2D
    octane_socket_list=["Rotation", "Scale", "Translation", ]
    octane_attribute_list=[]
    octane_attribute_config={"a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("Octane2DTransformationRotation", Octane2DTransformationRotation.bl_label).init()
        self.inputs.new("Octane2DTransformationScale", Octane2DTransformationScale.bl_label).init()
        self.inputs.new("Octane2DTransformationTranslation", Octane2DTransformationTranslation.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()


_CLASSES=[
    Octane2DTransformationRotation,
    Octane2DTransformationScale,
    Octane2DTransformationTranslation,
    Octane2DTransformation,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
