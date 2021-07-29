##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumeMediumScale(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumScale"
    bl_label = "Density"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="Absorption and scattering scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneVolumeMediumRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumRayMarchStepLength"
    bl_label = "Volume step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneVolumeMediumShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumShadowRayMarchStepLength"
    bl_label = "Vol. shadow ray step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneVolumeMediumUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumUseRayStepLengthForShadowRays"
    bl_label = "Use Vol. step length for Vol. shadow ray step length"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Uses Volume step length as Volume shadow ray step length as well")

class OctaneVolumeMediumDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumDisplacement"
    bl_label = "Sample position displacement"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneVolumeMediumAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumAbsorption"
    bl_label = "Absorption"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=1)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="Absorption cross section. This channel defines how much light is absorbed over the color range. By enabling 'invert absorption' this channel behaves like transparency", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneVolumeMediumAbsorptionRamp(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumAbsorptionRamp"
    bl_label = "Absorption ramp"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=291)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=26)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeMediumInvertAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumInvertAbsorption"
    bl_label = "Invert absorption"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=302)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")

class OctaneVolumeMediumScattering(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumScattering"
    bl_label = "Scattering"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=211)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Scattering cross section", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneVolumeMediumScatteringRamp(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumScatteringRamp"
    bl_label = "Scattering ramp"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=292)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=26)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeMediumPhase(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumPhase"
    bl_label = "Phase"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=131)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=14)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeMediumEmission(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumEmission"
    bl_label = "Emission"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=6)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeMediumEmissionRamp(OctaneBaseSocket):
    bl_idname = "OctaneVolumeMediumEmissionRamp"
    bl_label = "Emission ramp"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=293)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=26)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumeMedium(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumeMedium"
    bl_label = "Volume medium"
    octane_node_type: IntProperty(name="Octane Node Type", default=98)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Absorption;Absorption ramp;Invert absorption;Scattering;Scattering ramp;Phase;Emission;Emission ramp;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumeMediumScale", OctaneVolumeMediumScale.bl_label)
        self.inputs.new("OctaneVolumeMediumRayMarchStepLength", OctaneVolumeMediumRayMarchStepLength.bl_label)
        self.inputs.new("OctaneVolumeMediumShadowRayMarchStepLength", OctaneVolumeMediumShadowRayMarchStepLength.bl_label)
        self.inputs.new("OctaneVolumeMediumUseRayStepLengthForShadowRays", OctaneVolumeMediumUseRayStepLengthForShadowRays.bl_label)
        self.inputs.new("OctaneVolumeMediumDisplacement", OctaneVolumeMediumDisplacement.bl_label)
        self.inputs.new("OctaneVolumeMediumAbsorption", OctaneVolumeMediumAbsorption.bl_label)
        self.inputs.new("OctaneVolumeMediumAbsorptionRamp", OctaneVolumeMediumAbsorptionRamp.bl_label)
        self.inputs.new("OctaneVolumeMediumInvertAbsorption", OctaneVolumeMediumInvertAbsorption.bl_label)
        self.inputs.new("OctaneVolumeMediumScattering", OctaneVolumeMediumScattering.bl_label)
        self.inputs.new("OctaneVolumeMediumScatteringRamp", OctaneVolumeMediumScatteringRamp.bl_label)
        self.inputs.new("OctaneVolumeMediumPhase", OctaneVolumeMediumPhase.bl_label)
        self.inputs.new("OctaneVolumeMediumEmission", OctaneVolumeMediumEmission.bl_label)
        self.inputs.new("OctaneVolumeMediumEmissionRamp", OctaneVolumeMediumEmissionRamp.bl_label)
        self.outputs.new("OctaneMediumOutSocket", "Medium out")


def register():
    register_class(OctaneVolumeMediumScale)
    register_class(OctaneVolumeMediumRayMarchStepLength)
    register_class(OctaneVolumeMediumShadowRayMarchStepLength)
    register_class(OctaneVolumeMediumUseRayStepLengthForShadowRays)
    register_class(OctaneVolumeMediumDisplacement)
    register_class(OctaneVolumeMediumAbsorption)
    register_class(OctaneVolumeMediumAbsorptionRamp)
    register_class(OctaneVolumeMediumInvertAbsorption)
    register_class(OctaneVolumeMediumScattering)
    register_class(OctaneVolumeMediumScatteringRamp)
    register_class(OctaneVolumeMediumPhase)
    register_class(OctaneVolumeMediumEmission)
    register_class(OctaneVolumeMediumEmissionRamp)
    register_class(OctaneVolumeMedium)

def unregister():
    unregister_class(OctaneVolumeMedium)
    unregister_class(OctaneVolumeMediumEmissionRamp)
    unregister_class(OctaneVolumeMediumEmission)
    unregister_class(OctaneVolumeMediumPhase)
    unregister_class(OctaneVolumeMediumScatteringRamp)
    unregister_class(OctaneVolumeMediumScattering)
    unregister_class(OctaneVolumeMediumInvertAbsorption)
    unregister_class(OctaneVolumeMediumAbsorptionRamp)
    unregister_class(OctaneVolumeMediumAbsorption)
    unregister_class(OctaneVolumeMediumDisplacement)
    unregister_class(OctaneVolumeMediumUseRayStepLengthForShadowRays)
    unregister_class(OctaneVolumeMediumShadowRayMarchStepLength)
    unregister_class(OctaneVolumeMediumRayMarchStepLength)
    unregister_class(OctaneVolumeMediumScale)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
