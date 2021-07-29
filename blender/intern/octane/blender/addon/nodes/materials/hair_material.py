##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneHairMaterialDiffuseAmount(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialDiffuseAmount"
    bl_label = "Diffuse"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=706)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneHairMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialDiffuse"
    bl_label = "Diffuse color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneHairMaterialAlbedo(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialAlbedo"
    bl_label = "Albedo"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=409)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.100000, 0.100000, 0.100000), description="Hair base color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneHairMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialSpecular"
    bl_label = "Specular"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Hair specular color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneHairMaterialHairMelanin(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairMelanin"
    bl_label = "Melanin"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=490)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The absolute quantity of pigment that gives the hair base color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialHairPheomelanin(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairPheomelanin"
    bl_label = "Pheomelanin"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=491)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The extent of redness of a hair strand", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialHairMode(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairMode"
    bl_label = "Mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=492)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Albedo", "Albedo", "", 0),
        ("Melanin + Pheomelanin", "Melanin + Pheomelanin", "", 1),
    ]
    default_value: EnumProperty(default="Albedo", description="Hair base color", items=items)

class OctaneHairMaterialIndex(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialIndex"
    bl_label = "Index of refraction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.550000, description="Index of refraction controlling the Fresnel effect of the specular reflection", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneHairMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialRoughness"
    bl_label = "Longitudinal roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Longitudinal roughness, roughness along a hair strand for longitudinal scattering", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialRoughnessV(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialRoughnessV"
    bl_label = "Azimuthal roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=493)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.200000, description="Azimuthal roughness, roughness used for cross section of a hair strand for azimuth scattering", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialOffset(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialOffset"
    bl_label = "Offset"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Scale offset on the surface of the hair. 0 denotes perfectly smooth cylindrical hair, increasing the value shifts the specular highlight away from perfectly reflective direction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialHairRandomFrequency(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomFrequency"
    bl_label = "Randomness frequency"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=512)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Controls the frequency of randomness on hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneHairMaterialHairRandomOffset(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomOffset"
    bl_label = "Randomness offset"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=511)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), description="Controls the offset of randomness on hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="NONE", size=2)

class OctaneHairMaterialHairRandomnessIntensity(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomnessIntensity"
    bl_label = "Randomness intensity"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=510)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Controls the intensity of randomness on each hair strand", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneHairMaterialHairAlbedoRandomnColor(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairAlbedoRandomnColor"
    bl_label = "Random albedo"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=509)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Controls the target random albedo on the hair, this only works with albedo mode enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneHairMaterialHairRandomRoughness(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialHairRandomRoughness"
    bl_label = "Random roughness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=704)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Adds random roughness on top of the base roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneHairMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneHairMaterialEmission(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialEmission"
    bl_label = "Emission"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=6)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneHairMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialCustomAov"
    bl_label = "Custom AOV"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)

class OctaneHairMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)

class OctaneHairMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneHairMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneHairMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneHairMaterial"
    bl_label = "Hair material"
    octane_node_type: IntProperty(name="Octane Node Type", default=147)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Diffuse color;Albedo;Specular;Melanin;Pheomelanin;Mode;Index of refraction;Longitudinal roughness;Azimuthal roughness;Offset;Randomness frequency;Randomness offset;Randomness intensity;Random albedo;Random roughness;Opacity;Emission;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneHairMaterialDiffuseAmount", OctaneHairMaterialDiffuseAmount.bl_label)
        self.inputs.new("OctaneHairMaterialDiffuse", OctaneHairMaterialDiffuse.bl_label)
        self.inputs.new("OctaneHairMaterialAlbedo", OctaneHairMaterialAlbedo.bl_label)
        self.inputs.new("OctaneHairMaterialSpecular", OctaneHairMaterialSpecular.bl_label)
        self.inputs.new("OctaneHairMaterialHairMelanin", OctaneHairMaterialHairMelanin.bl_label)
        self.inputs.new("OctaneHairMaterialHairPheomelanin", OctaneHairMaterialHairPheomelanin.bl_label)
        self.inputs.new("OctaneHairMaterialHairMode", OctaneHairMaterialHairMode.bl_label)
        self.inputs.new("OctaneHairMaterialIndex", OctaneHairMaterialIndex.bl_label)
        self.inputs.new("OctaneHairMaterialRoughness", OctaneHairMaterialRoughness.bl_label)
        self.inputs.new("OctaneHairMaterialRoughnessV", OctaneHairMaterialRoughnessV.bl_label)
        self.inputs.new("OctaneHairMaterialOffset", OctaneHairMaterialOffset.bl_label)
        self.inputs.new("OctaneHairMaterialHairRandomFrequency", OctaneHairMaterialHairRandomFrequency.bl_label)
        self.inputs.new("OctaneHairMaterialHairRandomOffset", OctaneHairMaterialHairRandomOffset.bl_label)
        self.inputs.new("OctaneHairMaterialHairRandomnessIntensity", OctaneHairMaterialHairRandomnessIntensity.bl_label)
        self.inputs.new("OctaneHairMaterialHairAlbedoRandomnColor", OctaneHairMaterialHairAlbedoRandomnColor.bl_label)
        self.inputs.new("OctaneHairMaterialHairRandomRoughness", OctaneHairMaterialHairRandomRoughness.bl_label)
        self.inputs.new("OctaneHairMaterialOpacity", OctaneHairMaterialOpacity.bl_label)
        self.inputs.new("OctaneHairMaterialEmission", OctaneHairMaterialEmission.bl_label)
        self.inputs.new("OctaneHairMaterialCustomAov", OctaneHairMaterialCustomAov.bl_label)
        self.inputs.new("OctaneHairMaterialCustomAovChannel", OctaneHairMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneHairMaterialLayer", OctaneHairMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneHairMaterialDiffuseAmount)
    register_class(OctaneHairMaterialDiffuse)
    register_class(OctaneHairMaterialAlbedo)
    register_class(OctaneHairMaterialSpecular)
    register_class(OctaneHairMaterialHairMelanin)
    register_class(OctaneHairMaterialHairPheomelanin)
    register_class(OctaneHairMaterialHairMode)
    register_class(OctaneHairMaterialIndex)
    register_class(OctaneHairMaterialRoughness)
    register_class(OctaneHairMaterialRoughnessV)
    register_class(OctaneHairMaterialOffset)
    register_class(OctaneHairMaterialHairRandomFrequency)
    register_class(OctaneHairMaterialHairRandomOffset)
    register_class(OctaneHairMaterialHairRandomnessIntensity)
    register_class(OctaneHairMaterialHairAlbedoRandomnColor)
    register_class(OctaneHairMaterialHairRandomRoughness)
    register_class(OctaneHairMaterialOpacity)
    register_class(OctaneHairMaterialEmission)
    register_class(OctaneHairMaterialCustomAov)
    register_class(OctaneHairMaterialCustomAovChannel)
    register_class(OctaneHairMaterialLayer)
    register_class(OctaneHairMaterial)

def unregister():
    unregister_class(OctaneHairMaterial)
    unregister_class(OctaneHairMaterialLayer)
    unregister_class(OctaneHairMaterialCustomAovChannel)
    unregister_class(OctaneHairMaterialCustomAov)
    unregister_class(OctaneHairMaterialEmission)
    unregister_class(OctaneHairMaterialOpacity)
    unregister_class(OctaneHairMaterialHairRandomRoughness)
    unregister_class(OctaneHairMaterialHairAlbedoRandomnColor)
    unregister_class(OctaneHairMaterialHairRandomnessIntensity)
    unregister_class(OctaneHairMaterialHairRandomOffset)
    unregister_class(OctaneHairMaterialHairRandomFrequency)
    unregister_class(OctaneHairMaterialOffset)
    unregister_class(OctaneHairMaterialRoughnessV)
    unregister_class(OctaneHairMaterialRoughness)
    unregister_class(OctaneHairMaterialIndex)
    unregister_class(OctaneHairMaterialHairMode)
    unregister_class(OctaneHairMaterialHairPheomelanin)
    unregister_class(OctaneHairMaterialHairMelanin)
    unregister_class(OctaneHairMaterialSpecular)
    unregister_class(OctaneHairMaterialAlbedo)
    unregister_class(OctaneHairMaterialDiffuse)
    unregister_class(OctaneHairMaterialDiffuseAmount)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
