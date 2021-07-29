##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGaussianSpectrumWavelength(OctaneBaseSocket):
    bl_idname = "OctaneGaussianSpectrumWavelength"
    bl_label = "Wavelength"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=254)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Mean wavelength (380nm-720nm)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGaussianSpectrumWidth(OctaneBaseSocket):
    bl_idname = "OctaneGaussianSpectrumWidth"
    bl_label = "Width"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=256)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.100000, description="Standard deviation (0-800nm)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGaussianSpectrumPower(OctaneBaseSocket):
    bl_idname = "OctaneGaussianSpectrumPower"
    bl_label = "Power/brightness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Power/brightness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneGaussianSpectrum(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGaussianSpectrum"
    bl_label = "Gaussian spectrum"
    octane_node_type: IntProperty(name="Octane Node Type", default=32)
    octane_socket_list: StringProperty(name="Socket List", default="Wavelength;Width;Power/brightness;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGaussianSpectrumWavelength", OctaneGaussianSpectrumWavelength.bl_label)
        self.inputs.new("OctaneGaussianSpectrumWidth", OctaneGaussianSpectrumWidth.bl_label)
        self.inputs.new("OctaneGaussianSpectrumPower", OctaneGaussianSpectrumPower.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneGaussianSpectrumWavelength)
    register_class(OctaneGaussianSpectrumWidth)
    register_class(OctaneGaussianSpectrumPower)
    register_class(OctaneGaussianSpectrum)

def unregister():
    unregister_class(OctaneGaussianSpectrum)
    unregister_class(OctaneGaussianSpectrumPower)
    unregister_class(OctaneGaussianSpectrumWidth)
    unregister_class(OctaneGaussianSpectrumWavelength)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
