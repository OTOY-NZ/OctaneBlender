##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePostProcessingAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctanePostProcessingAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctanePostProcessingAOVPostProcEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePostProcessingAOVPostProcEnvironment"
    bl_label = "Include environment"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=137)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled")

class OctanePostProcessingAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePostProcessingAOV"
    bl_label = "Post processing AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=221)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Include environment;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePostProcessingAOVEnabled", OctanePostProcessingAOVEnabled.bl_label)
        self.inputs.new("OctanePostProcessingAOVPostProcEnvironment", OctanePostProcessingAOVPostProcEnvironment.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctanePostProcessingAOVEnabled)
    register_class(OctanePostProcessingAOVPostProcEnvironment)
    register_class(OctanePostProcessingAOV)

def unregister():
    unregister_class(OctanePostProcessingAOV)
    unregister_class(OctanePostProcessingAOVPostProcEnvironment)
    unregister_class(OctanePostProcessingAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
