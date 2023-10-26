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


class OctaneCurvatureTextureCurvatureMode(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureCurvatureMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CURVATURE_MODE
    octane_pin_name="curvatureMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 3),
        ("Concavity", "Concavity", "", 1),
        ("Convexity", "Convexity", "", 2),
    ]
    default_value: EnumProperty(default="Convexity", update=OctaneBaseSocket.update_node_tree, description="The type of curvature to sample", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureStrength(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Strength", min=0.100000, max=5.000000, soft_min=0.100000, soft_max=5.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureRadius(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specifies the maximum area affected by the curvature effect", min=0.000100, max=100000.000000, soft_min=0.000100, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureDirtMap(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureDirtMap"
    bl_label="Radius map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_DIRT_MAP
    octane_pin_name="dirtMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Determines the proportion of the maximum area affected by the curvature effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OFFSET
    octane_pin_name="offset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.005000, update=OctaneBaseSocket.update_node_tree, description="Specifies the offset from the surface used to sample the neighbouring geometry", min=0.000010, max=1.000000, soft_min=0.000010, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureTolerance(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureTolerance"
    bl_label="Tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TOLERANCE
    octane_pin_name="tolerance"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Tolerance for small curvature and small angles between polygons", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureSpread(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD
    octane_pin_name="spread"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Spread controls the ray direction with respect to the normal of the surface. 0 means curvature is sampled straight in the direction of the surface normal, and 1 means the sampling rays are shot perpendicular to the surface normal", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureObjectIncludeMode(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureObjectIncludeMode"
    bl_label="Include object mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OBJECT_INCLUDE_MODE
    octane_pin_name="objectIncludeMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="Includes objects when calculating the curvature value: By default the selected mode is All, which includes all object intersections into calculating curvature. If Self is selected, then only self-intersection is taken into account for curvature. If Others is selected, then only ray-intersection with other objects is used for curvature", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureInvertNormal(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureInvertNormal"
    bl_label="Invert normal"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT_NORMAL
    octane_pin_name="invert_normal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCurvatureTexture"
    bl_label="Curvature texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCurvatureTextureCurvatureMode,OctaneCurvatureTextureStrength,OctaneCurvatureTextureRadius,OctaneCurvatureTextureDirtMap,OctaneCurvatureTextureOffset,OctaneCurvatureTextureTolerance,OctaneCurvatureTextureSpread,OctaneCurvatureTextureObjectIncludeMode,OctaneCurvatureTextureInvertNormal,]
    octane_min_version=11000010
    octane_node_type=consts.NodeType.NT_TEX_CURVATURE
    octane_socket_list=["Mode", "Strength", "Radius", "Radius map", "Offset", "Tolerance", "Spread", "Include object mode", "Invert normal", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneCurvatureTextureCurvatureMode", OctaneCurvatureTextureCurvatureMode.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureStrength", OctaneCurvatureTextureStrength.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureRadius", OctaneCurvatureTextureRadius.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureDirtMap", OctaneCurvatureTextureDirtMap.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureOffset", OctaneCurvatureTextureOffset.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureTolerance", OctaneCurvatureTextureTolerance.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureSpread", OctaneCurvatureTextureSpread.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureObjectIncludeMode", OctaneCurvatureTextureObjectIncludeMode.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureInvertNormal", OctaneCurvatureTextureInvertNormal.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCurvatureTextureCurvatureMode,
    OctaneCurvatureTextureStrength,
    OctaneCurvatureTextureRadius,
    OctaneCurvatureTextureDirtMap,
    OctaneCurvatureTextureOffset,
    OctaneCurvatureTextureTolerance,
    OctaneCurvatureTextureSpread,
    OctaneCurvatureTextureObjectIncludeMode,
    OctaneCurvatureTextureInvertNormal,
    OctaneCurvatureTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
