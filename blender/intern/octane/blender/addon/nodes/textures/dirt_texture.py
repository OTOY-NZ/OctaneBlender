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


class OctaneDirtTextureStrength(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_STRENGTH
    octane_pin_name="strength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Strength", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDetails(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDetails"
    bl_label="Details"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DETAILS
    octane_pin_name="details"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Details", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureRadius(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specifies the maximum area affected by the dirt effect", min=0.000010, max=100000.000000, soft_min=0.000010, soft_max=100000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtMap(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtMap"
    bl_label="Radius map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_DIRT_MAP
    octane_pin_name="dirtMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Determines the proportion of the maximum area affected by the dirt effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureTolerance(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureTolerance"
    bl_label="Tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TOLERANCE
    octane_pin_name="tolerance"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Tolerance for small curvature and small angles between polygons", min=0.000000, max=0.300000, soft_min=0.000000, soft_max=0.300000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureSpread(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD
    octane_pin_name="spread"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Spread controls the ray direction with respect to the normal of the surface. 0 means the dirt direction is shot straight in the direction of the surface normal, and 1 means the dirt rays are shot in all directions in the upper hemisphere in a cosine lobe", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDistribution(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDistribution"
    bl_label="Distribution"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISTRIBUTION
    octane_pin_name="distribution"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Distribution controls how evenly rays are shot within the sampling cone. When the value is 100, rays gather closer to the lateral surface. If the value is 1 rays are evenly distributed", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureOffset"
    bl_label="Bias"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OFFSET
    octane_pin_name="offset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The shading normal vector in shading space that we sample with as a custom direction. By default the direction is (0, 0, 1), which is the shading normal in shading coordinates. If any non-zero bias is set, then this bias vector is used as shading normal to sample dirt rays", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtOffsetSpace(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtOffsetSpace"
    bl_label="Bias coordinate space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_DIRT_OFFSET_SPACE
    octane_pin_name="dirtOffsetSpace"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
        ("Normal space", "Normal space", "", 4),
    ]
    default_value: EnumProperty(default="Normal space", update=OctaneBaseSocket.update_node_tree, description="The coordinate space the bias vector is in", items=items)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureObjectIncludeMode(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureObjectIncludeMode"
    bl_label="Include object mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OBJECT_INCLUDE_MODE
    octane_pin_name="objectIncludeMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="Includes objects when calculating dirt value: By default the selected mode is All, which includes all object intersections into calculating dirt. If Self is selected, then only self-intersection is taken into account for dirt. If Others is selected, then only ray-intersection with other objects is used for dirt", items=items)
    octane_hide_value=False
    octane_min_version=11000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureInvertNormal(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureInvertNormal"
    bl_label="Invert normal"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT_NORMAL
    octane_pin_name="invert_normal"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirtTextureDirtGlobal(OctaneBaseSocket):
    bl_idname="OctaneDirtTextureDirtGlobal"
    bl_label="[Deprecated]Dirt global"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_DIRT_GLOBAL
    octane_pin_name="dirtGlobal"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="(deprecated)", items=items)
    octane_hide_value=False
    octane_min_version=8000000
    octane_end_version=11000010
    octane_deprecated=True

class OctaneDirtTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDirtTexture"
    bl_label="Dirt texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDirtTextureStrength,OctaneDirtTextureDetails,OctaneDirtTextureRadius,OctaneDirtTextureDirtMap,OctaneDirtTextureTolerance,OctaneDirtTextureSpread,OctaneDirtTextureDistribution,OctaneDirtTextureOffset,OctaneDirtTextureDirtOffsetSpace,OctaneDirtTextureObjectIncludeMode,OctaneDirtTextureInvertNormal,OctaneDirtTextureDirtGlobal,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_DIRT
    octane_socket_list=["Strength", "Details", "Radius", "Radius map", "Tolerance", "Spread", "Distribution", "Bias", "Bias coordinate space", "Include object mode", "Invert normal", "[Deprecated]Dirt global", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=11

    def init(self, context):
        self.inputs.new("OctaneDirtTextureStrength", OctaneDirtTextureStrength.bl_label).init()
        self.inputs.new("OctaneDirtTextureDetails", OctaneDirtTextureDetails.bl_label).init()
        self.inputs.new("OctaneDirtTextureRadius", OctaneDirtTextureRadius.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtMap", OctaneDirtTextureDirtMap.bl_label).init()
        self.inputs.new("OctaneDirtTextureTolerance", OctaneDirtTextureTolerance.bl_label).init()
        self.inputs.new("OctaneDirtTextureSpread", OctaneDirtTextureSpread.bl_label).init()
        self.inputs.new("OctaneDirtTextureDistribution", OctaneDirtTextureDistribution.bl_label).init()
        self.inputs.new("OctaneDirtTextureOffset", OctaneDirtTextureOffset.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtOffsetSpace", OctaneDirtTextureDirtOffsetSpace.bl_label).init()
        self.inputs.new("OctaneDirtTextureObjectIncludeMode", OctaneDirtTextureObjectIncludeMode.bl_label).init()
        self.inputs.new("OctaneDirtTextureInvertNormal", OctaneDirtTextureInvertNormal.bl_label).init()
        self.inputs.new("OctaneDirtTextureDirtGlobal", OctaneDirtTextureDirtGlobal.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneDirtTextureStrength,
    OctaneDirtTextureDetails,
    OctaneDirtTextureRadius,
    OctaneDirtTextureDirtMap,
    OctaneDirtTextureTolerance,
    OctaneDirtTextureSpread,
    OctaneDirtTextureDistribution,
    OctaneDirtTextureOffset,
    OctaneDirtTextureDirtOffsetSpace,
    OctaneDirtTextureObjectIncludeMode,
    OctaneDirtTextureInvertNormal,
    OctaneDirtTextureDirtGlobal,
    OctaneDirtTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
