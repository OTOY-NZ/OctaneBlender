##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRenderAOVGroupEnabled(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables/disables all AOVs of this group")

class OctaneRenderAOVGroupRenderPassesRaw(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupRenderPassesRaw"
    bl_label = "Raw"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=277)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray")

class OctaneRenderAOVGroupRenderPassCryptomatteCount(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupRenderPassCryptomatteCount"
    bl_label = "Cryptomatte bins"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=456)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=6, description="Amount of cryptomatte bins to render", min=2, max=10, soft_min=2, soft_max=10, step=2, subtype="FACTOR")

class OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor"
    bl_label = "Cryptomatte seed factor"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=472)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=10, description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. Low values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs", min=4, max=25, soft_min=4, soft_max=25, step=1, subtype="FACTOR")

class OctaneRenderAOVGroupRenderPassInfoMaxSamples(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupRenderPassInfoMaxSamples"
    bl_label = "Max info samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=161)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=128, description="The maximum number of samples for the info passes", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")

class OctaneRenderAOVGroupSamplingMode(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupSamplingMode"
    bl_label = "Info sampling mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=329)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", description="Enables motion blur and depth of field, and sets pixel filtering modes.  'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering. 'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled. 'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render passes except for render layer mask and ambient occlusion", items=items)

class OctaneRenderAOVGroupOpacityThreshold(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVGroupOpacityThreshold"
    bl_label = "Info opacity threshold"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=630)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Geometry with an opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneRenderAOVGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRenderAOVGroup"
    bl_label = "Render AOV group"
    octane_node_type: IntProperty(name="Octane Node Type", default=179)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Raw;Cryptomatte bins;Cryptomatte seed factor;Max info samples;Info sampling mode;Info opacity threshold;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRenderAOVGroupEnabled", OctaneRenderAOVGroupEnabled.bl_label)
        self.inputs.new("OctaneRenderAOVGroupRenderPassesRaw", OctaneRenderAOVGroupRenderPassesRaw.bl_label)
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteCount", OctaneRenderAOVGroupRenderPassCryptomatteCount.bl_label)
        self.inputs.new("OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor", OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor.bl_label)
        self.inputs.new("OctaneRenderAOVGroupRenderPassInfoMaxSamples", OctaneRenderAOVGroupRenderPassInfoMaxSamples.bl_label)
        self.inputs.new("OctaneRenderAOVGroupSamplingMode", OctaneRenderAOVGroupSamplingMode.bl_label)
        self.inputs.new("OctaneRenderAOVGroupOpacityThreshold", OctaneRenderAOVGroupOpacityThreshold.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneRenderAOVGroupEnabled)
    register_class(OctaneRenderAOVGroupRenderPassesRaw)
    register_class(OctaneRenderAOVGroupRenderPassCryptomatteCount)
    register_class(OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor)
    register_class(OctaneRenderAOVGroupRenderPassInfoMaxSamples)
    register_class(OctaneRenderAOVGroupSamplingMode)
    register_class(OctaneRenderAOVGroupOpacityThreshold)
    register_class(OctaneRenderAOVGroup)

def unregister():
    unregister_class(OctaneRenderAOVGroup)
    unregister_class(OctaneRenderAOVGroupOpacityThreshold)
    unregister_class(OctaneRenderAOVGroupSamplingMode)
    unregister_class(OctaneRenderAOVGroupRenderPassInfoMaxSamples)
    unregister_class(OctaneRenderAOVGroupRenderPassCryptomatteSeedFactor)
    unregister_class(OctaneRenderAOVGroupRenderPassCryptomatteCount)
    unregister_class(OctaneRenderAOVGroupRenderPassesRaw)
    unregister_class(OctaneRenderAOVGroupEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
