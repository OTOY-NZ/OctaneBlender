##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneWireframeAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneWireframeAOVBump(OctaneBaseSocket):
    bl_idname = "OctaneWireframeAOVBump"
    bl_label = "Bump and normal mapping"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Take bump and normal mapping into account for wireframe shading")

class OctaneWireframeAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneWireframeAOV"
    bl_label = "Wireframe AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=254)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Bump and normal mapping;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneWireframeAOVEnabled", OctaneWireframeAOVEnabled.bl_label)
        self.inputs.new("OctaneWireframeAOVBump", OctaneWireframeAOVBump.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneWireframeAOVEnabled)
    register_class(OctaneWireframeAOVBump)
    register_class(OctaneWireframeAOV)

def unregister():
    unregister_class(OctaneWireframeAOV)
    unregister_class(OctaneWireframeAOVBump)
    unregister_class(OctaneWireframeAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
