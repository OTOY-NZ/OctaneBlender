##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneUVCoordinatesAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneUVCoordinatesAOVEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables the render AOV")

class OctaneUVCoordinatesAOVUVMax(OctaneBaseSocket):
    bl_idname = "OctaneUVCoordinatesAOVUVMax"
    bl_label = "UV max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=250)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneUVCoordinatesAOVUvSet(OctaneBaseSocket):
    bl_idname = "OctaneUVCoordinatesAOVUvSet"
    bl_label = "UV coordinate selection"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")

class OctaneUVCoordinatesAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneUVCoordinatesAOV"
    bl_label = "UV coordinates AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=245)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;UV max;UV coordinate selection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneUVCoordinatesAOVEnabled", OctaneUVCoordinatesAOVEnabled.bl_label)
        self.inputs.new("OctaneUVCoordinatesAOVUVMax", OctaneUVCoordinatesAOVUVMax.bl_label)
        self.inputs.new("OctaneUVCoordinatesAOVUvSet", OctaneUVCoordinatesAOVUvSet.bl_label)
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out")


def register():
    register_class(OctaneUVCoordinatesAOVEnabled)
    register_class(OctaneUVCoordinatesAOVUVMax)
    register_class(OctaneUVCoordinatesAOVUvSet)
    register_class(OctaneUVCoordinatesAOV)

def unregister():
    unregister_class(OctaneUVCoordinatesAOV)
    unregister_class(OctaneUVCoordinatesAOVUvSet)
    unregister_class(OctaneUVCoordinatesAOVUVMax)
    unregister_class(OctaneUVCoordinatesAOVEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
