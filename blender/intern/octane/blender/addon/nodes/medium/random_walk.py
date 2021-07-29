##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneRandomWalkScale(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkScale"
    bl_label = "Density"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneRandomWalkRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkRayMarchStepLength"
    bl_label = "Volume step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneRandomWalkShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkShadowRayMarchStepLength"
    bl_label = "Vol. shadow ray step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneRandomWalkUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkUseRayStepLengthForShadowRays"
    bl_label = "Use Vol. step length for Vol. shadow ray step length"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Uses Volume step length as Volume shadow ray step length as well")

class OctaneRandomWalkDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkDisplacement"
    bl_label = "Sample position displacement"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneRandomWalkAlbedo(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkAlbedo"
    bl_label = "Albedo"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=409)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="Scattering albedo. The coefficients are determined from this using the mean free  path", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneRandomWalkRadius(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkRadius"
    bl_label = "Radius"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Determines the depth that the light scatters in the medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneRandomWalkBias(OctaneBaseSocket):
    bl_idname = "OctaneRandomWalkBias"
    bl_label = "Bias"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=489)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Bias of the subsurface scattering. Higher values use biased sampling, which usually gives better results for lower depth settings, and more speed for objects with low curvature", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneRandomWalk(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRandomWalk"
    bl_label = "Random walk"
    octane_node_type: IntProperty(name="Octane Node Type", default=146)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Albedo;Radius;Bias;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneRandomWalkScale", OctaneRandomWalkScale.bl_label)
        self.inputs.new("OctaneRandomWalkRayMarchStepLength", OctaneRandomWalkRayMarchStepLength.bl_label)
        self.inputs.new("OctaneRandomWalkShadowRayMarchStepLength", OctaneRandomWalkShadowRayMarchStepLength.bl_label)
        self.inputs.new("OctaneRandomWalkUseRayStepLengthForShadowRays", OctaneRandomWalkUseRayStepLengthForShadowRays.bl_label)
        self.inputs.new("OctaneRandomWalkDisplacement", OctaneRandomWalkDisplacement.bl_label)
        self.inputs.new("OctaneRandomWalkAlbedo", OctaneRandomWalkAlbedo.bl_label)
        self.inputs.new("OctaneRandomWalkRadius", OctaneRandomWalkRadius.bl_label)
        self.inputs.new("OctaneRandomWalkBias", OctaneRandomWalkBias.bl_label)
        self.outputs.new("OctaneMediumOutSocket", "Medium out")


def register():
    register_class(OctaneRandomWalkScale)
    register_class(OctaneRandomWalkRayMarchStepLength)
    register_class(OctaneRandomWalkShadowRayMarchStepLength)
    register_class(OctaneRandomWalkUseRayStepLengthForShadowRays)
    register_class(OctaneRandomWalkDisplacement)
    register_class(OctaneRandomWalkAlbedo)
    register_class(OctaneRandomWalkRadius)
    register_class(OctaneRandomWalkBias)
    register_class(OctaneRandomWalk)

def unregister():
    unregister_class(OctaneRandomWalk)
    unregister_class(OctaneRandomWalkBias)
    unregister_class(OctaneRandomWalkRadius)
    unregister_class(OctaneRandomWalkAlbedo)
    unregister_class(OctaneRandomWalkDisplacement)
    unregister_class(OctaneRandomWalkUseRayStepLengthForShadowRays)
    unregister_class(OctaneRandomWalkShadowRayMarchStepLength)
    unregister_class(OctaneRandomWalkRayMarchStepLength)
    unregister_class(OctaneRandomWalkScale)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
