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


class OctaneDirectionalLightEmission(OctaneBaseSocket):
    bl_idname="OctaneDirectionalLightEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=consts.NodeType.NT_EMIS_TEXTURE
    octane_default_node_name="OctaneTextureEmission"
    octane_pin_id=consts.PinID.P_EMISSION
    octane_pin_name="emission"
    octane_pin_type=consts.PinType.PT_EMISSION
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectionalLightTransform(OctaneBaseSocket):
    bl_idname="OctaneDirectionalLightTransform"
    bl_label="Light transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectionalLightDirAnalyticLightAngle(OctaneBaseSocket):
    bl_idname="OctaneDirectionalLightDirAnalyticLightAngle"
    bl_label="Light sample spread angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DIR_ANALYTIC_LIGHT_ANGLE
    octane_pin_name="dirAnalyticLightAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Light's sampling spread angle [degrees]. The larger the value is, the bigger the light source is, hence producing softer shadows", min=0.000000, max=60.000000, soft_min=0.000000, soft_max=15.000000, step=10, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectionalLightUseInPostVolume(OctaneBaseSocket):
    bl_idname="OctaneDirectionalLightUseInPostVolume"
    bl_label="Use in post volume"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_USE_IN_POST_VOLUME
    octane_pin_name="useInPostVolume"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable or disable this directional light in post volume rendering")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectionalLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDirectionalLight"
    bl_label="Directional light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDirectionalLightEmission,OctaneDirectionalLightTransform,OctaneDirectionalLightDirAnalyticLightAngle,OctaneDirectionalLightUseInPostVolume,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_LIGHT_DIRECTIONAL
    octane_socket_list=["Emission", "Light transform", "Light sample spread angle", "Use in post volume", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=4

    def init(self, context):
        self.inputs.new("OctaneDirectionalLightEmission", OctaneDirectionalLightEmission.bl_label).init()
        self.inputs.new("OctaneDirectionalLightTransform", OctaneDirectionalLightTransform.bl_label).init()
        self.inputs.new("OctaneDirectionalLightDirAnalyticLightAngle", OctaneDirectionalLightDirAnalyticLightAngle.bl_label).init()
        self.inputs.new("OctaneDirectionalLightUseInPostVolume", OctaneDirectionalLightUseInPostVolume.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneDirectionalLightEmission,
    OctaneDirectionalLightTransform,
    OctaneDirectionalLightDirAnalyticLightAngle,
    OctaneDirectionalLightUseInPostVolume,
    OctaneDirectionalLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
