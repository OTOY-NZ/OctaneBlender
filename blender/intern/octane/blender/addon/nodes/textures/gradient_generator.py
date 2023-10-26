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


class OctaneGradientGeneratorGradientType(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorGradientType"
    bl_label="Gradient type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_GRADIENT_TYPE
    octane_pin_name="gradientType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Linear", "Linear", "", 0),
        ("Radial", "Radial", "", 1),
        ("Angular", "Angular", "", 2),
        ("Polygonal", "Polygonal", "", 3),
        ("Spiral", "Spiral", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="Type of gradient generated", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorRepetitions(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorRepetitions"
    bl_label="Repetitions"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_REPETITIONS
    octane_pin_name="repetitions"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Number of times the gradient is repeated", min=1.000000, max=20.000000, soft_min=1.000000, soft_max=20.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorPolygonSides(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorPolygonSides"
    bl_label="Polygon sides"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_POLYGON_SIDES
    octane_pin_name="polygonSides"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Number of sides to the polygon when using the polygonal gradient type", min=3, max=20, soft_min=3, soft_max=20, step=1, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorGamma(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAMMA
    octane_pin_name="gamma"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.200000, update=OctaneBaseSocket.update_node_tree, description="Gamma correction coefficient", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorInvert(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert the output color")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorTransform(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorProjection(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorBorderMode(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorBorderMode"
    bl_label="Repetition mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BORDER_MODE
    octane_pin_name="borderMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Clamp value", "Clamp value", "", 3),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
    ]
    default_value: EnumProperty(default="Wrap around", update=OctaneBaseSocket.update_node_tree, description="Determines the gradient behavior for repetitions", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGenerator(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGradientGenerator"
    bl_label="Gradient generator"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneGradientGeneratorGradientType,OctaneGradientGeneratorRepetitions,OctaneGradientGeneratorPolygonSides,OctaneGradientGeneratorGamma,OctaneGradientGeneratorInvert,OctaneGradientGeneratorTransform,OctaneGradientGeneratorProjection,OctaneGradientGeneratorBorderMode,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_GRADIENT_GENERATOR
    octane_socket_list=["Gradient type", "Repetitions", "Polygon sides", "Gamma", "Invert", "UVW transform", "Projection", "Repetition mode", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneGradientGeneratorGradientType", OctaneGradientGeneratorGradientType.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorRepetitions", OctaneGradientGeneratorRepetitions.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorPolygonSides", OctaneGradientGeneratorPolygonSides.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorGamma", OctaneGradientGeneratorGamma.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorInvert", OctaneGradientGeneratorInvert.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorTransform", OctaneGradientGeneratorTransform.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorProjection", OctaneGradientGeneratorProjection.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorBorderMode", OctaneGradientGeneratorBorderMode.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneGradientGeneratorGradientType,
    OctaneGradientGeneratorRepetitions,
    OctaneGradientGeneratorPolygonSides,
    OctaneGradientGeneratorGamma,
    OctaneGradientGeneratorInvert,
    OctaneGradientGeneratorTransform,
    OctaneGradientGeneratorProjection,
    OctaneGradientGeneratorBorderMode,
    OctaneGradientGenerator,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
