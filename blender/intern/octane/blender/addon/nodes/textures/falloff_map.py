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


class OctaneFalloffMapMode(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_MODE
    octane_pin_name="mode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Normal vs. eye ray", "Normal vs. eye ray", "", 0),
        ("Normal vs. vector 90deg", "Normal vs. vector 90deg", "", 1),
        ("Normal vs. vector 180deg", "Normal vs. vector 180deg", "", 2),
    ]
    default_value: EnumProperty(default="Normal vs. eye ray", update=OctaneBaseSocket.update_node_tree, description="The falloff mode that should be used:\n\n'Normal vs. eye ray': The falloff is calculated from the angle between the surface normal and the eye ray.\n'Normal vs. vector 90deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 90 degrees.\n'Normal vs vector 180deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 180 degrees", items=items)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapNormal(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapNormal"
    bl_label="Minimum value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Value if the angle between the two directions is 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapGrazing(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapGrazing"
    bl_label="Maximum value"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GRAZING
    octane_pin_name="grazing"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Value if the angle between the two directions is at the maximum", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapFalloffIndex(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapFalloffIndex"
    bl_label="Falloff skew factor"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FALLOFF
    octane_pin_name="falloff index"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=6.000000, update=OctaneBaseSocket.update_node_tree, description="Skew factor for the falloff curve", min=0.100000, max=15.000000, soft_min=0.100000, soft_max=15.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapDirection(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapDirection"
    bl_label="Falloff direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DIRECTION
    octane_pin_name="direction"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The direction vector that is used by some of the falloff modes", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMap(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFalloffMap"
    bl_label="Falloff map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneFalloffMapMode,OctaneFalloffMapNormal,OctaneFalloffMapGrazing,OctaneFalloffMapFalloffIndex,OctaneFalloffMapDirection,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_FALLOFF
    octane_socket_list=["Mode", "Minimum value", "Maximum value", "Falloff skew factor", "Falloff direction", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=5

    def init(self, context):
        self.inputs.new("OctaneFalloffMapMode", OctaneFalloffMapMode.bl_label).init()
        self.inputs.new("OctaneFalloffMapNormal", OctaneFalloffMapNormal.bl_label).init()
        self.inputs.new("OctaneFalloffMapGrazing", OctaneFalloffMapGrazing.bl_label).init()
        self.inputs.new("OctaneFalloffMapFalloffIndex", OctaneFalloffMapFalloffIndex.bl_label).init()
        self.inputs.new("OctaneFalloffMapDirection", OctaneFalloffMapDirection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneFalloffMapMode,
    OctaneFalloffMapNormal,
    OctaneFalloffMapGrazing,
    OctaneFalloffMapFalloffIndex,
    OctaneFalloffMapDirection,
    OctaneFalloffMap,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
