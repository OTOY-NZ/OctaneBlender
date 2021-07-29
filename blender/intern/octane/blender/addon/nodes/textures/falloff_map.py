##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneFalloffMapMode(OctaneBaseSocket):
    bl_idname = "OctaneFalloffMapMode"
    bl_label = "Mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=324)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Normal vs. eye ray", "Normal vs. eye ray", "", 0),
        ("Normal vs. vector 90deg", "Normal vs. vector 90deg", "", 1),
        ("Normal vs. vector 180deg", "Normal vs. vector 180deg", "", 2),
    ]
    default_value: EnumProperty(default="Normal vs. eye ray", description="The falloff mode that should be used:  'Normal vs. eye ray': The falloff is calculated from the angle between the surface normal and the eye ray. 'Normal vs. vector 90deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 90 degrees. 'Normal vs vector 180deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 180 degrees", items=items)

class OctaneFalloffMapNormal(OctaneBaseSocket):
    bl_idname = "OctaneFalloffMapNormal"
    bl_label = "Minimum value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Value if the angle between the two directions is 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneFalloffMapGrazing(OctaneBaseSocket):
    bl_idname = "OctaneFalloffMapGrazing"
    bl_label = "Maximum value"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=68)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Value if the angle between the two directions is at the maximum", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneFalloffMapFalloffIndex(OctaneBaseSocket):
    bl_idname = "OctaneFalloffMapFalloffIndex"
    bl_label = "Falloff skew factor"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=47)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=6.000000, description="Skew factor for the falloff curve", min=0.100000, max=15.000000, soft_min=0.100000, soft_max=15.000000, step=1, subtype="FACTOR")

class OctaneFalloffMapDirection(OctaneBaseSocket):
    bl_idname = "OctaneFalloffMapDirection"
    bl_label = "Falloff direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=327)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="The direction vector that is used by some of the falloff modes", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneFalloffMap(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneFalloffMap"
    bl_label = "Falloff map"
    octane_node_type: IntProperty(name="Octane Node Type", default=50)
    octane_socket_list: StringProperty(name="Socket List", default="Mode;Minimum value;Maximum value;Falloff skew factor;Falloff direction;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneFalloffMapMode", OctaneFalloffMapMode.bl_label)
        self.inputs.new("OctaneFalloffMapNormal", OctaneFalloffMapNormal.bl_label)
        self.inputs.new("OctaneFalloffMapGrazing", OctaneFalloffMapGrazing.bl_label)
        self.inputs.new("OctaneFalloffMapFalloffIndex", OctaneFalloffMapFalloffIndex.bl_label)
        self.inputs.new("OctaneFalloffMapDirection", OctaneFalloffMapDirection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneFalloffMapMode)
    register_class(OctaneFalloffMapNormal)
    register_class(OctaneFalloffMapGrazing)
    register_class(OctaneFalloffMapFalloffIndex)
    register_class(OctaneFalloffMapDirection)
    register_class(OctaneFalloffMap)

def unregister():
    unregister_class(OctaneFalloffMap)
    unregister_class(OctaneFalloffMapDirection)
    unregister_class(OctaneFalloffMapFalloffIndex)
    unregister_class(OctaneFalloffMapGrazing)
    unregister_class(OctaneFalloffMapNormal)
    unregister_class(OctaneFalloffMapMode)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
