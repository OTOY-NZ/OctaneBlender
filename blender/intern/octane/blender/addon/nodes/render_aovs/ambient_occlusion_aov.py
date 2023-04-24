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


class OctaneAmbientOcclusionAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneAmbientOcclusionAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAmbientOcclusionAOVAodist(OctaneBaseSocket):
    bl_idname="OctaneAmbientOcclusionAOVAodist"
    bl_label="AO distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum distance for which the occlusion should be tested", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAmbientOcclusionAOVAoAlphaShadows(OctaneBaseSocket):
    bl_idname="OctaneAmbientOcclusionAOVAoAlphaShadows"
    bl_label="AO alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=258)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take alpha maps into account when calculating ambient occlusion")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAmbientOcclusionAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAmbientOcclusionAOV"
    bl_label="Ambient occlusion AOV"
    bl_width_default=200
    octane_render_pass_id=1010
    octane_render_pass_name="Ambient occlusion"
    octane_render_pass_short_name="AO"
    octane_render_pass_description="Assigns a color to the camera ray's hit point proportional to the amount of occlusion by other geometry"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=183)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;AO distance;AO alpha shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneAmbientOcclusionAOVEnabled", OctaneAmbientOcclusionAOVEnabled.bl_label).init()
        self.inputs.new("OctaneAmbientOcclusionAOVAodist", OctaneAmbientOcclusionAOVAodist.bl_label).init()
        self.inputs.new("OctaneAmbientOcclusionAOVAoAlphaShadows", OctaneAmbientOcclusionAOVAoAlphaShadows.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneAmbientOcclusionAOVEnabled,
    OctaneAmbientOcclusionAOVAodist,
    OctaneAmbientOcclusionAOVAoAlphaShadows,
    OctaneAmbientOcclusionAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
