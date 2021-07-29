##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGlobalTextureAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneGlobalTextureAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneGlobalTextureAOVSubType(OctaneBaseSocket):
    bl_idname = "OctaneGlobalTextureAOVSubType"
    bl_label = "ID"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Global texture 1", "Global texture 1", "", 0),
        ("Global texture 2", "Global texture 2", "", 1),
        ("Global texture 3", "Global texture 3", "", 2),
        ("Global texture 4", "Global texture 4", "", 3),
        ("Global texture 5", "Global texture 5", "", 4),
        ("Global texture 6", "Global texture 6", "", 5),
        ("Global texture 7", "Global texture 7", "", 6),
        ("Global texture 8", "Global texture 8", "", 7),
        ("Global texture 9", "Global texture 9", "", 8),
        ("Global texture 10", "Global texture 10", "", 9),
    ]
    default_value: EnumProperty(default="Global texture 1", description="The ID or index of the global texture AOV", items=items)

class OctaneGlobalTextureAOVTexture(OctaneBaseSocket):
    bl_idname = "OctaneGlobalTextureAOVTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneGlobalTextureAOVAlphachannel(OctaneBaseSocket):
    bl_idname = "OctaneGlobalTextureAOVAlphachannel"
    bl_label = "Alpha channel"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneGlobalTextureAOVIncludeEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneGlobalTextureAOVIncludeEnvironment"
    bl_label = "Include environment"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=634)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the texture will also be evaluated for camera rays that leave the scene. This can be useful for textures that need to be evaluated over the whole screen")

class OctaneGlobalTextureAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGlobalTextureAOV"
    bl_label = "Global texture AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=199)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;Texture;Alpha channel;Include environment;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGlobalTextureAOVEnabled", OctaneGlobalTextureAOVEnabled.bl_label)
        self.inputs.new("OctaneGlobalTextureAOVSubType", OctaneGlobalTextureAOVSubType.bl_label)
        self.inputs.new("OctaneGlobalTextureAOVTexture", OctaneGlobalTextureAOVTexture.bl_label)
        self.inputs.new("OctaneGlobalTextureAOVAlphachannel", OctaneGlobalTextureAOVAlphachannel.bl_label)
        self.inputs.new("OctaneGlobalTextureAOVIncludeEnvironment", OctaneGlobalTextureAOVIncludeEnvironment.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneGlobalTextureAOVEnabled)
    register_class(OctaneGlobalTextureAOVSubType)
    register_class(OctaneGlobalTextureAOVTexture)
    register_class(OctaneGlobalTextureAOVAlphachannel)
    register_class(OctaneGlobalTextureAOVIncludeEnvironment)
    register_class(OctaneGlobalTextureAOV)

def unregister():
    unregister_class(OctaneGlobalTextureAOV)
    unregister_class(OctaneGlobalTextureAOVIncludeEnvironment)
    unregister_class(OctaneGlobalTextureAOVAlphachannel)
    unregister_class(OctaneGlobalTextureAOVTexture)
    unregister_class(OctaneGlobalTextureAOVSubType)
    unregister_class(OctaneGlobalTextureAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
