##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRoundEdgesRoundEdgesMode(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesMode"
    bl_label = "Mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=485)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Off", "Off", "", 0),
        ("Fast", "Fast", "", 1),
        ("Accurate", "Accurate", "", 2),
        ("Accurate convex only", "Accurate convex only", "", 3),
        ("Accurate concave only", "Accurate concave only", "", 4),
    ]
    default_value: EnumProperty(default="Fast", description="Whether rounding is applied to convex and/or concave edges", items=items)

class OctaneRoundEdgesRoundEdgesRadius(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesRadius"
    bl_label = "Radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=473)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Edge rounding radius", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneRoundEdgesRoundEdgesCurvatureRoundness(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesCurvatureRoundness"
    bl_label = "Roundness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=475)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specifies the roundness of the edge being 1 completely round and 0 a chamfer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneRoundEdgesRoundEdgesSampleCount(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesSampleCount"
    bl_label = "Samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=508)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The number of rays to use when sampling the neighboring geometry", min=4, max=16, soft_min=4, soft_max=16, step=2, subtype="FACTOR")

class OctaneRoundEdgesRoundEdgesConsiderOtherObjects(OctaneBaseSocket):
    bl_idname = "OctaneRoundEdgesRoundEdgesConsiderOtherObjects"
    bl_label = "Consider other objects"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=476)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Whether to consider other objects in the scene or just the current object")

class OctaneRoundEdges(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRoundEdges"
    bl_label = "Round edges"
    octane_node_type: IntProperty(name="Octane Node Type", default=137)
    octane_socket_list: StringProperty(name="Socket List", default="Mode;Radius;Roundness;Samples;Consider other objects;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRoundEdgesRoundEdgesMode", OctaneRoundEdgesRoundEdgesMode.bl_label)
        self.inputs.new("OctaneRoundEdgesRoundEdgesRadius", OctaneRoundEdgesRoundEdgesRadius.bl_label)
        self.inputs.new("OctaneRoundEdgesRoundEdgesCurvatureRoundness", OctaneRoundEdgesRoundEdgesCurvatureRoundness.bl_label)
        self.inputs.new("OctaneRoundEdgesRoundEdgesSampleCount", OctaneRoundEdgesRoundEdgesSampleCount.bl_label)
        self.inputs.new("OctaneRoundEdgesRoundEdgesConsiderOtherObjects", OctaneRoundEdgesRoundEdgesConsiderOtherObjects.bl_label)
        self.outputs.new("OctaneRoundEdgesOutSocket", "Round edges out")


def register():
    register_class(OctaneRoundEdgesRoundEdgesMode)
    register_class(OctaneRoundEdgesRoundEdgesRadius)
    register_class(OctaneRoundEdgesRoundEdgesCurvatureRoundness)
    register_class(OctaneRoundEdgesRoundEdgesSampleCount)
    register_class(OctaneRoundEdgesRoundEdgesConsiderOtherObjects)
    register_class(OctaneRoundEdges)

def unregister():
    unregister_class(OctaneRoundEdges)
    unregister_class(OctaneRoundEdgesRoundEdgesConsiderOtherObjects)
    unregister_class(OctaneRoundEdgesRoundEdgesSampleCount)
    unregister_class(OctaneRoundEdgesRoundEdgesCurvatureRoundness)
    unregister_class(OctaneRoundEdgesRoundEdgesRadius)
    unregister_class(OctaneRoundEdgesRoundEdgesMode)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
