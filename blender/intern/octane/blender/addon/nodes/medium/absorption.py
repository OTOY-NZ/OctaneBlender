##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneAbsorptionScale(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionScale"
    bl_label = "Density"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=100.000000, description="Absorption scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneAbsorptionRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionRayMarchStepLength"
    bl_label = "Volume step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneAbsorptionShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionShadowRayMarchStepLength"
    bl_label = "Vol. shadow ray step length"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=4.000000, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctaneAbsorptionUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionUseRayStepLengthForShadowRays"
    bl_label = "Use Vol. step length for Vol. shadow ray step length"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Uses Volume step length as Volume shadow ray step length as well")

class OctaneAbsorptionDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionDisplacement"
    bl_label = "Sample position displacement"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneAbsorptionAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionAbsorption"
    bl_label = "Absorption"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=1)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="Absorption cross section. This channel defines how much light is absorbed over the color range. By enabling 'invert absorption' this channel behaves like transparency", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneAbsorptionInvertAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionInvertAbsorption"
    bl_label = "Invert absorption"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=302)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")

class OctaneAbsorption(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAbsorption"
    bl_label = "Absorption"
    octane_node_type: IntProperty(name="Octane Node Type", default=58)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Absorption;Invert absorption;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneAbsorptionScale", OctaneAbsorptionScale.bl_label)
        self.inputs.new("OctaneAbsorptionRayMarchStepLength", OctaneAbsorptionRayMarchStepLength.bl_label)
        self.inputs.new("OctaneAbsorptionShadowRayMarchStepLength", OctaneAbsorptionShadowRayMarchStepLength.bl_label)
        self.inputs.new("OctaneAbsorptionUseRayStepLengthForShadowRays", OctaneAbsorptionUseRayStepLengthForShadowRays.bl_label)
        self.inputs.new("OctaneAbsorptionDisplacement", OctaneAbsorptionDisplacement.bl_label)
        self.inputs.new("OctaneAbsorptionAbsorption", OctaneAbsorptionAbsorption.bl_label)
        self.inputs.new("OctaneAbsorptionInvertAbsorption", OctaneAbsorptionInvertAbsorption.bl_label)
        self.outputs.new("OctaneMediumOutSocket", "Medium out")


def register():
    register_class(OctaneAbsorptionScale)
    register_class(OctaneAbsorptionRayMarchStepLength)
    register_class(OctaneAbsorptionShadowRayMarchStepLength)
    register_class(OctaneAbsorptionUseRayStepLengthForShadowRays)
    register_class(OctaneAbsorptionDisplacement)
    register_class(OctaneAbsorptionAbsorption)
    register_class(OctaneAbsorptionInvertAbsorption)
    register_class(OctaneAbsorption)

def unregister():
    unregister_class(OctaneAbsorption)
    unregister_class(OctaneAbsorptionInvertAbsorption)
    unregister_class(OctaneAbsorptionAbsorption)
    unregister_class(OctaneAbsorptionDisplacement)
    unregister_class(OctaneAbsorptionUseRayStepLengthForShadowRays)
    unregister_class(OctaneAbsorptionShadowRayMarchStepLength)
    unregister_class(OctaneAbsorptionRayMarchStepLength)
    unregister_class(OctaneAbsorptionScale)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
