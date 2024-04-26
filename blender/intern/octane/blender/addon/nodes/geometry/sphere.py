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


class OctaneSDFSphereMaterial(OctaneBaseSocket):
    bl_idname="OctaneSDFSphereMaterial"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL
    octane_pin_name="material"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFSphereObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneSDFSphereObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id=consts.PinID.P_OBJECT_LAYER
    octane_pin_name="objectLayer"
    octane_pin_type=consts.PinType.PT_OBJECTLAYER
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFSphereTransform(OctaneBaseSocket):
    bl_idname="OctaneSDFSphereTransform"
    bl_label="Transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFSphereRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFSphereRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFSphereThickness(OctaneBaseSocket):
    bl_idname="OctaneSDFSphereThickness"
    bl_label="Fill"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THICKNESS
    octane_pin_name="thickness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFSphereGroupParameters(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFSphereGroupParameters"
    bl_label="[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Radius;")

class OctaneSDFSphereGroupModifiers(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFSphereGroupModifiers"
    bl_label="[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Fill;")

class OctaneSDFSphere(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSDFSphere"
    bl_label="Sphere"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSDFSphereMaterial,OctaneSDFSphereObjectLayer,OctaneSDFSphereTransform,OctaneSDFSphereGroupParameters,OctaneSDFSphereRadius,OctaneSDFSphereGroupModifiers,OctaneSDFSphereThickness,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_GEO_SDF_SPHERE
    octane_socket_list=["Material", "Object layer", "Transform", "Radius", "Fill", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneSDFSphereMaterial", OctaneSDFSphereMaterial.bl_label).init()
        self.inputs.new("OctaneSDFSphereObjectLayer", OctaneSDFSphereObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFSphereTransform", OctaneSDFSphereTransform.bl_label).init()
        self.inputs.new("OctaneSDFSphereGroupParameters", OctaneSDFSphereGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFSphereRadius", OctaneSDFSphereRadius.bl_label).init()
        self.inputs.new("OctaneSDFSphereGroupModifiers", OctaneSDFSphereGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFSphereThickness", OctaneSDFSphereThickness.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSDFSphereMaterial,
    OctaneSDFSphereObjectLayer,
    OctaneSDFSphereTransform,
    OctaneSDFSphereRadius,
    OctaneSDFSphereThickness,
    OctaneSDFSphereGroupParameters,
    OctaneSDFSphereGroupModifiers,
    OctaneSDFSphere,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
