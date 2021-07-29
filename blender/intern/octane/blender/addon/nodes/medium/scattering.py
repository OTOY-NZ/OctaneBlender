##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneScatteringScale(OctaneBaseSocket):
    bl_idname = "OctaneScatteringScale"
    bl_label = "Density"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneScatteringRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneScatteringRayMarchStepLength"
    bl_label = "Volume step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneScatteringShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneScatteringShadowRayMarchStepLength"
    bl_label = "Vol. shadow ray step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneScatteringUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneScatteringUseRayStepLengthForShadowRays"
    bl_label = "Use Vol. step length for Vol. shadow ray step length"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Uses Volume step length as Volume shadow ray step length as well")

class OctaneScatteringDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneScatteringDisplacement"
    bl_label = "Sample position displacement"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatteringAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneScatteringAbsorption"
    bl_label = "Absorption"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=1)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="Absorption cross section. This channel defines how much light is absorbed over the color range. By enabling 'invert absorption' this channel behaves like transparency", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneScatteringInvertAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneScatteringInvertAbsorption"
    bl_label = "Invert absorption"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=302)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")

class OctaneScatteringScattering(OctaneBaseSocket):
    bl_idname = "OctaneScatteringScattering"
    bl_label = "Scattering"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=211)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Scattering cross section. This channel defines how much light is scattered over the color range", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneScatteringPhase(OctaneBaseSocket):
    bl_idname = "OctaneScatteringPhase"
    bl_label = "Phase"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=131)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=14)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatteringEmission(OctaneBaseSocket):
    bl_idname = "OctaneScatteringEmission"
    bl_label = "Emission"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=6)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScattering(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneScattering"
    bl_label = "Scattering"
    octane_node_type: IntProperty(name="Octane Node Type", default=59)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Absorption;Invert absorption;Scattering;Phase;Emission;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneScatteringScale", OctaneScatteringScale.bl_label)
        self.inputs.new("OctaneScatteringRayMarchStepLength", OctaneScatteringRayMarchStepLength.bl_label)
        self.inputs.new("OctaneScatteringShadowRayMarchStepLength", OctaneScatteringShadowRayMarchStepLength.bl_label)
        self.inputs.new("OctaneScatteringUseRayStepLengthForShadowRays", OctaneScatteringUseRayStepLengthForShadowRays.bl_label)
        self.inputs.new("OctaneScatteringDisplacement", OctaneScatteringDisplacement.bl_label)
        self.inputs.new("OctaneScatteringAbsorption", OctaneScatteringAbsorption.bl_label)
        self.inputs.new("OctaneScatteringInvertAbsorption", OctaneScatteringInvertAbsorption.bl_label)
        self.inputs.new("OctaneScatteringScattering", OctaneScatteringScattering.bl_label)
        self.inputs.new("OctaneScatteringPhase", OctaneScatteringPhase.bl_label)
        self.inputs.new("OctaneScatteringEmission", OctaneScatteringEmission.bl_label)
        self.outputs.new("OctaneMediumOutSocket", "Medium out")


def register():
    register_class(OctaneScatteringScale)
    register_class(OctaneScatteringRayMarchStepLength)
    register_class(OctaneScatteringShadowRayMarchStepLength)
    register_class(OctaneScatteringUseRayStepLengthForShadowRays)
    register_class(OctaneScatteringDisplacement)
    register_class(OctaneScatteringAbsorption)
    register_class(OctaneScatteringInvertAbsorption)
    register_class(OctaneScatteringScattering)
    register_class(OctaneScatteringPhase)
    register_class(OctaneScatteringEmission)
    register_class(OctaneScattering)

def unregister():
    unregister_class(OctaneScattering)
    unregister_class(OctaneScatteringEmission)
    unregister_class(OctaneScatteringPhase)
    unregister_class(OctaneScatteringScattering)
    unregister_class(OctaneScatteringInvertAbsorption)
    unregister_class(OctaneScatteringAbsorption)
    unregister_class(OctaneScatteringDisplacement)
    unregister_class(OctaneScatteringUseRayStepLengthForShadowRays)
    unregister_class(OctaneScatteringShadowRayMarchStepLength)
    unregister_class(OctaneScatteringRayMarchStepLength)
    unregister_class(OctaneScatteringScale)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
