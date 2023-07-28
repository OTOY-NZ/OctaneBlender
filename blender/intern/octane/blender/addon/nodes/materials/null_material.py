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


class OctaneNullMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialRefractionAlpha"
    bl_label="Affect alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_REFRACTION_ALPHA
    octane_pin_name="refractionAlpha"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to have refractions affect the alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_DISPLACEMENT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH
    octane_pin_name="smooth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=10020200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name="smoothShadowTerminator"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type=consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name="OctaneRoundEdges"
    octane_pin_id=consts.PinID.P_ROUND_EDGES
    octane_pin_name="roundEdges"
    octane_pin_type=consts.PinType.PT_ROUND_EDGES
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_PRIORITY
    octane_pin_name="priority"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10021300
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneNullMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Medium;Opacity;Affect alpha;")

class OctaneNullMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneNullMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneNullMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNullMaterial"
    bl_label="Null material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneNullMaterialGroupTransmissionProperties,OctaneNullMaterialMedium,OctaneNullMaterialOpacity,OctaneNullMaterialRefractionAlpha,OctaneNullMaterialGroupGeometryProperties,OctaneNullMaterialDisplacement,OctaneNullMaterialSmooth,OctaneNullMaterialSmoothShadowTerminator,OctaneNullMaterialRoundEdges,OctaneNullMaterialPriority,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_NULL
    octane_socket_list=["Medium", "Opacity", "Affect alpha", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Priority", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneNullMaterialGroupTransmissionProperties", OctaneNullMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneNullMaterialMedium", OctaneNullMaterialMedium.bl_label).init()
        self.inputs.new("OctaneNullMaterialOpacity", OctaneNullMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneNullMaterialRefractionAlpha", OctaneNullMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneNullMaterialGroupGeometryProperties", OctaneNullMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneNullMaterialDisplacement", OctaneNullMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneNullMaterialSmooth", OctaneNullMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneNullMaterialSmoothShadowTerminator", OctaneNullMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneNullMaterialRoundEdges", OctaneNullMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneNullMaterialPriority", OctaneNullMaterialPriority.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneNullMaterialMedium,
    OctaneNullMaterialOpacity,
    OctaneNullMaterialRefractionAlpha,
    OctaneNullMaterialDisplacement,
    OctaneNullMaterialSmooth,
    OctaneNullMaterialSmoothShadowTerminator,
    OctaneNullMaterialRoundEdges,
    OctaneNullMaterialPriority,
    OctaneNullMaterialGroupTransmissionProperties,
    OctaneNullMaterialGroupGeometryProperties,
    OctaneNullMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
