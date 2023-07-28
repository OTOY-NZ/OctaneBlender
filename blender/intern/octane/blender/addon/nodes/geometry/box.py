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


class OctaneSDFBoxMaterial(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxMaterial"
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

class OctaneSDFBoxObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxObjectLayer"
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

class OctaneSDFBoxTransform(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxTransform"
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

class OctaneSDFBoxWidth(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxWidth"
    bl_label="Width"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_WIDTH
    octane_pin_name="width"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFBoxHeight(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxHeight"
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

class OctaneSDFBoxDepth(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxDepth"
    bl_label="Depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DEPTH
    octane_pin_name="depth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=10000.000000, soft_min=0.000000, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFBoxRoundBaseRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxRoundBaseRadius"
    bl_label="Round base"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROUND_BASE_RADIUS
    octane_pin_name="roundBaseRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rounds the base rectangle. Rounds vertical edges without rounding the horizontal edges", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFBoxRoundEdgesRadius(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxRoundEdgesRadius"
    bl_label="Round"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROUND_EDGES_RADIUS
    octane_pin_name="roundEdgesRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFBoxThickness(OctaneBaseSocket):
    bl_idname="OctaneSDFBoxThickness"
    bl_label="Fill"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THICKNESS
    octane_pin_name="thickness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSDFBoxGroupParameters(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFBoxGroupParameters"
    bl_label="[OctaneGroupTitle]Parameters"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Width;Height;Depth;")

class OctaneSDFBoxGroupModifiers(OctaneGroupTitleSocket):
    bl_idname="OctaneSDFBoxGroupModifiers"
    bl_label="[OctaneGroupTitle]Modifiers"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Round base;Round;Fill;")

class OctaneSDFBox(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSDFBox"
    bl_label="Box"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSDFBoxMaterial,OctaneSDFBoxObjectLayer,OctaneSDFBoxTransform,OctaneSDFBoxGroupParameters,OctaneSDFBoxWidth,OctaneSDFBoxHeight,OctaneSDFBoxDepth,OctaneSDFBoxGroupModifiers,OctaneSDFBoxRoundBaseRadius,OctaneSDFBoxRoundEdgesRadius,OctaneSDFBoxThickness,]
    octane_min_version=12000001
    octane_node_type=consts.NodeType.NT_GEO_SDF_BOX
    octane_socket_list=["Material", "Object layer", "Transform", "Width", "Height", "Depth", "Round base", "Round", "Fill", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneSDFBoxMaterial", OctaneSDFBoxMaterial.bl_label).init()
        self.inputs.new("OctaneSDFBoxObjectLayer", OctaneSDFBoxObjectLayer.bl_label).init()
        self.inputs.new("OctaneSDFBoxTransform", OctaneSDFBoxTransform.bl_label).init()
        self.inputs.new("OctaneSDFBoxGroupParameters", OctaneSDFBoxGroupParameters.bl_label).init()
        self.inputs.new("OctaneSDFBoxWidth", OctaneSDFBoxWidth.bl_label).init()
        self.inputs.new("OctaneSDFBoxHeight", OctaneSDFBoxHeight.bl_label).init()
        self.inputs.new("OctaneSDFBoxDepth", OctaneSDFBoxDepth.bl_label).init()
        self.inputs.new("OctaneSDFBoxGroupModifiers", OctaneSDFBoxGroupModifiers.bl_label).init()
        self.inputs.new("OctaneSDFBoxRoundBaseRadius", OctaneSDFBoxRoundBaseRadius.bl_label).init()
        self.inputs.new("OctaneSDFBoxRoundEdgesRadius", OctaneSDFBoxRoundEdgesRadius.bl_label).init()
        self.inputs.new("OctaneSDFBoxThickness", OctaneSDFBoxThickness.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSDFBoxMaterial,
    OctaneSDFBoxObjectLayer,
    OctaneSDFBoxTransform,
    OctaneSDFBoxWidth,
    OctaneSDFBoxHeight,
    OctaneSDFBoxDepth,
    OctaneSDFBoxRoundBaseRadius,
    OctaneSDFBoxRoundEdgesRadius,
    OctaneSDFBoxThickness,
    OctaneSDFBoxGroupParameters,
    OctaneSDFBoxGroupModifiers,
    OctaneSDFBox,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
