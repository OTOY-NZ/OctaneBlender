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


class OctaneSmoothVoronoiContoursFrequency(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursFrequency"
    bl_label="Frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FREQUENCY
    octane_pin_name="frequency"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=12.000000, update=OctaneBaseSocket.update_node_tree, description="Frequency", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursTime(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TIME
    octane_pin_name="time"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Time", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursGlossy(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursGlossy"
    bl_label="Glossy"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_GLOSSY
    octane_pin_name="glossy"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Glossy")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursTransform(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursTransform"
    bl_label="UV transform"
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

class OctaneSmoothVoronoiContoursProjection(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContours(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSmoothVoronoiContours"
    bl_label="Smooth Voronoi contours"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSmoothVoronoiContoursFrequency,OctaneSmoothVoronoiContoursTime,OctaneSmoothVoronoiContoursGlossy,OctaneSmoothVoronoiContoursTransform,OctaneSmoothVoronoiContoursProjection,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_VORONOI_SMOOTH_CONTOURS
    octane_socket_list=["Frequency", "Time", "Glossy", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneSmoothVoronoiContoursFrequency", OctaneSmoothVoronoiContoursFrequency.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursTime", OctaneSmoothVoronoiContoursTime.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursGlossy", OctaneSmoothVoronoiContoursGlossy.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursTransform", OctaneSmoothVoronoiContoursTransform.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursProjection", OctaneSmoothVoronoiContoursProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSmoothVoronoiContoursFrequency,
    OctaneSmoothVoronoiContoursTime,
    OctaneSmoothVoronoiContoursGlossy,
    OctaneSmoothVoronoiContoursTransform,
    OctaneSmoothVoronoiContoursProjection,
    OctaneSmoothVoronoiContours,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
