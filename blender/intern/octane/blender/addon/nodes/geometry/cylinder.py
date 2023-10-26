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


class OctaneSDFCylinderMaterial(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderMaterial"
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

class OctaneSDFCylinderObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderObjectLayer"
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

class OctaneSDFCylinderTransform(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderTransform"
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

class OctaneSDFCylinderRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFCylinderHeight(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderHeight"
    bl_label="Height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_HEIGHT
    octane_pin_name="height"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFCylinderRoundEdgesRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderRoundEdgesRadius"
    bl_label="Round"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROUND_EDGES_RADIUS
    octane_pin_name="roundEdgesRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFCylinderThickness(OctaneBaseSocket):
    bl_idname="OctaneSDFCylinderThickness"
    bl_label="Fill"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THICKNESS
    octane_pin_name="thickness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFCylinderGroupParameters(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFCylinderGroupParameters"
    bl_label="[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Radius;Height;")

class OctaneSDFCylinderGroupModifiers(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFCylinderGroupModifiers"
    bl_label="[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Round;Fill;")

class OctaneSDFCylinder(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSDFCylinder"
    bl_label="Cylinder"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSDFCylinderMaterial,OctaneSDFCylinderObjectLayer,OctaneSDFCylinderTransform,OctaneSDFCylinderGroupParameters,OctaneSDFCylinderRadius,OctaneSDFCylinderHeight,OctaneSDFCylinderGroupModifiers,OctaneSDFCylinderRoundEdgesRadius,OctaneSDFCylinderThickness,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_GEO_SDF_CYLINDER
    octane_socket_list=["Material", "Object layer", "Transform", "Radius", "Height", "Round", "Fill", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=7

    def init(self, context):
        self.inputs.new("OctaneSDFCylinderMaterial", OctaneSDFCylinderMaterial.bl_label).init()
        self.inputs.new("OctaneSDFCylinderObjectLayer", OctaneSDFCylinderObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFCylinderTransform", OctaneSDFCylinderTransform.bl_label).init()
        self.inputs.new("OctaneSDFCylinderGroupParameters", OctaneSDFCylinderGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFCylinderRadius", OctaneSDFCylinderRadius.bl_label).init()
        self.inputs.new("OctaneSDFCylinderHeight", OctaneSDFCylinderHeight.bl_label).init()
        self.inputs.new("OctaneSDFCylinderGroupModifiers", OctaneSDFCylinderGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFCylinderRoundEdgesRadius", OctaneSDFCylinderRoundEdgesRadius.bl_label).init()
        self.inputs.new("OctaneSDFCylinderThickness", OctaneSDFCylinderThickness.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSDFCylinderMaterial,
    OctaneSDFCylinderObjectLayer,
    OctaneSDFCylinderTransform,
    OctaneSDFCylinderRadius,
    OctaneSDFCylinderHeight,
    OctaneSDFCylinderRoundEdgesRadius,
    OctaneSDFCylinderThickness,
    OctaneSDFCylinderGroupParameters,
    OctaneSDFCylinderGroupModifiers,
    OctaneSDFCylinder,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
