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


class OctaneNormalSmoothAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneNormalSmoothAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormalSmoothAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNormalSmoothAOV"
    bl_label="Normal (smooth) AOV"
    bl_width_default=200
    octane_render_pass_id=1008
    octane_render_pass_name="Normal (smooth)"
    octane_render_pass_short_name="SmN"
    octane_render_pass_description="Assigns a color for the smooth normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneNormalSmoothAOVEnabled,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_AOV_SMOOTH_NORMAL
    octane_socket_list=["Enabled", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=1

    def init(self, context):
        self.inputs.new("OctaneNormalSmoothAOVEnabled", OctaneNormalSmoothAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOV out").init()


_CLASSES=[
    OctaneNormalSmoothAOVEnabled,
    OctaneNormalSmoothAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneSmoothNormalAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneSmoothNormalAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothNormalAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSmoothNormalAOV"
    bl_label="Smooth normal AOV"
    bl_width_default=200
    octane_render_pass_id=1008
    octane_render_pass_name="Smooth normal"
    octane_render_pass_short_name="SmN"
    octane_render_pass_description="Assigns a color for the smooth normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=253)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctaneSmoothNormalAOVEnabled", OctaneSmoothNormalAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVOutSocket", "Render AOVs out").init()


_LEGACY_CLASSES=[
    OctaneSmoothNormalAOVEnabled,
    OctaneSmoothNormalAOV,
]

_CLASSES.extend(_LEGACY_CLASSES)