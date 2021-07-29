##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneAmbientOcclusionAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneAmbientOcclusionAOVAodist(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVAodist"
    bl_label = "AO distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=3.000000, description="The maximum distance for which the occlusion should be tested", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1, subtype="FACTOR")

class OctaneAmbientOcclusionAOVAoAlphaShadows(OctaneBaseSocket):
    bl_idname = "OctaneAmbientOcclusionAOVAoAlphaShadows"
    bl_label = "AO alpha shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=258)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Take alpha maps into account when calculating ambient occlusion")

class OctaneAmbientOcclusionAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAmbientOcclusionAOV"
    bl_label = "Ambient occlusion AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=183)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;AO distance;AO alpha shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneAmbientOcclusionAOVEnabled", OctaneAmbientOcclusionAOVEnabled.bl_label)
        self.inputs.new("OctaneAmbientOcclusionAOVAodist", OctaneAmbientOcclusionAOVAodist.bl_label)
        self.inputs.new("OctaneAmbientOcclusionAOVAoAlphaShadows", OctaneAmbientOcclusionAOVAoAlphaShadows.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneAmbientOcclusionAOVEnabled)
    register_class(OctaneAmbientOcclusionAOVAodist)
    register_class(OctaneAmbientOcclusionAOVAoAlphaShadows)
    register_class(OctaneAmbientOcclusionAOV)

def unregister():
    unregister_class(OctaneAmbientOcclusionAOV)
    unregister_class(OctaneAmbientOcclusionAOVAoAlphaShadows)
    unregister_class(OctaneAmbientOcclusionAOVAodist)
    unregister_class(OctaneAmbientOcclusionAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
