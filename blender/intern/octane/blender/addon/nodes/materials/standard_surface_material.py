##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneStandardSurfaceMaterialBase(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialBase"
    bl_label="Base weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_BASE
    octane_pin_name="base"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="Contribution of the base layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialBaseColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialBaseColor"
    bl_label="Base color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_BASE_COLOR
    octane_pin_name="baseColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Color of the base layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialDiffuseRoughness(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialDiffuseRoughness"
    bl_label="Diffuse roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_DIFFUSE_ROUGHNESS
    octane_pin_name="diffuseRoughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Diffuse roughness to allow simulation of very rough surfaces like sand or clay", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialDiffuseBrdf(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialDiffuseBrdf"
    bl_label="Diffuse BRDF model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_DIFFUSE_BRDF
    octane_pin_name="diffuseBrdf"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Lambertian", "Lambertian", "", 1),
        ("Oren-Nayar", "Oren-Nayar", "", 2),
    ]
    default_value: EnumProperty(default="Oren-Nayar", update=OctaneBaseSocket.update_node_tree, description="Diffuse BRDF model", items=items)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialMetallic(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialMetallic"
    bl_label="Metalness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_METALLIC
    octane_pin_name="metallic"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The metallic-ness of the material, blends between dielectric and metallic material", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSpecular"
    bl_label="Specular weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SPECULAR
    octane_pin_name="specular"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Contribution of the specular layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSpecularColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSpecularColor"
    bl_label="Specular color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SPECULAR_COLOR
    octane_pin_name="specularColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Specular reflection channel which determines the color of glossy reflection for dielectric material. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRoughness"
    bl_label="Specular roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS
    octane_pin_name="roughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular reflection and transmission channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialIor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialIor"
    bl_label="Specular IOR"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_IOR
    octane_pin_name="ior"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection or transmission", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialAnisotropyTexture(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialAnisotropyTexture"
    bl_label="Specular anisotropy"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ANISOTROPY_TEXTURE
    octane_pin_name="anisotropyTexture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular and transmissive material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRotation(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRotation"
    bl_label="Specular rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROTATION
    octane_pin_name="rotation"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection and transmission channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialTransmission(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialTransmission"
    bl_label="Transmission weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TRANSMISSION
    octane_pin_name="transmission"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Transmission weight controlling the contribution of light passing the surface of the material (via refraction)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialTransmissionColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialTransmissionColor"
    bl_label="Transmission color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TRANSMISSION_COLOR
    octane_pin_name="transmissionColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Transmission color tint for refraction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialTransmissionDepth(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialTransmissionDepth"
    bl_label="Transmission depth"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_TRANSMISSION_DEPTH
    octane_pin_name="transmissionDepth"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The distance travelled inside the material by white light before its color become transmission color by beer's law, if it is zero then transmission color is applied constantly as it crosses boundary", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialScattering(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialScattering"
    bl_label="Scatter"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SCATTERING
    octane_pin_name="scattering"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Scattering coefficient of the interior medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialScatteringAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialScatteringAnisotropy"
    bl_label="Scatter anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCATTERING_ANISOTROPY
    octane_pin_name="scatteringAnisotropy"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the Henyey-Greenstein phase function of the interior medium ranging between -1 and 1", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialDispersionCoefficientB"
    bl_label="Dispersion Coefficient"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISPERSION_COEFFICIENT_B
    octane_pin_name="dispersion_coefficient_B"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The dispersion coefficient, the meaning depends on the selected dispersion mode", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialDispersionMode(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialDispersionMode"
    bl_label="Dispersion mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_DISPERSION_MODE
    octane_pin_name="dispersionMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Abbe number", "Abbe number", "", 1),
        ("Cauchy formula", "Cauchy formula", "", 2),
    ]
    default_value: EnumProperty(default="Abbe number", update=OctaneBaseSocket.update_node_tree, description="Select how the IOR and dispersion coefficient inputs are interpreted", items=items)
    octane_hide_value=False
    octane_min_version=13000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRoughnessExtra(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRoughnessExtra"
    bl_label="Extra roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS_EXTRA
    octane_pin_name="roughnessExtra"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Additional (positive or negative) roughness on top of specular layer roughness", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialPriority"
    bl_label="Dielectric priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_PRIORITY
    octane_pin_name="priority"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialFakeShadows(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialFakeShadows"
    bl_label="Fake shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_FAKE_SHADOWS
    octane_pin_name="fake_shadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")
    octane_hide_value=False
    octane_min_version=12000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRefractionAlpha"
    bl_label="Affect alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_REFRACTION_ALPHA
    octane_pin_name="refractionAlpha"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to have refractions affect the alpha channel")
    octane_hide_value=False
    octane_min_version=12000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialHasCaustics(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialHasCaustics"
    bl_label="Allow caustics"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_HAS_CAUSTICS
    octane_pin_name="hasCaustics"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSubsurface(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSubsurface"
    bl_label="Subsurface weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SUBSURFACE
    octane_pin_name="subsurface"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Contribution of diffuse transmission", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSubsurfaceColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSubsurfaceColor"
    bl_label="Subsurface color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SUBSURFACE_COLOR
    octane_pin_name="subsurfaceColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Color used for subsurface scattering", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRadius(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRadius"
    bl_label="Subsurface radius"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Subsurface radii (i.e. mean free paths) of the red, green, and blue channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialScale(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialScale"
    bl_label="Subsurface scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SCALE
    octane_pin_name="scale"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scalar scale for subsurface radius", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSubsurfaceAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSubsurfaceAnisotropy"
    bl_label="Subsurface anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUBSURFACE_ANISOTROPY
    octane_pin_name="subsurfaceAnisotropy"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Anisotropy of the subsurface medium phase function, ranging between -1 and 1", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialMedium"
    bl_label="Override medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=13000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoating(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoating"
    bl_label="Coating weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING
    octane_pin_name="coating"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Reflection weight of the coating layer (reflection color is fixed to white)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingColor"
    bl_label="Coating color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_COATING_COLOR
    octane_pin_name="coatingColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Tint color for the light coming from all layers below", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingRoughness(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingRoughness"
    bl_label="Coating roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_ROUGHNESS
    octane_pin_name="coatingRoughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=31
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the coating layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingIor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingIor"
    bl_label="Coating IOR"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_IOR
    octane_pin_name="coatingIor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="IOR of the coating layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingAnisotropy"
    bl_label="Coating anisotropy"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_ANISOTROPY
    octane_pin_name="coatingAnisotropy"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the coating layer, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingRotation(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingRotation"
    bl_label="Coating rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_ROTATION
    octane_pin_name="coatingRotation"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic coating reflection", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingBump(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingBump"
    bl_label="Coating bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_COATING_BUMP
    octane_pin_name="coatingBump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialCoatingNormal(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingNormal"
    bl_label="Coating normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_COATING_NORMAL
    octane_pin_name="coatingNormal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSheen(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSheen"
    bl_label="Sheen weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SHEEN
    octane_pin_name="sheen"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The contribution of sheen layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSheenColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSheenColor"
    bl_label="Sheen color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SHEEN_COLOR
    octane_pin_name="sheenColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSheenRoughness"
    bl_label="Sheen roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SHEEN_ROUGHNESS
    octane_pin_name="sheenRoughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialEmissionWeight(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialEmissionWeight"
    bl_label="Emission weight"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_EMISSION_WEIGHT
    octane_pin_name="emissionWeight"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The scale multiplier for emission", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialEmissionColor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialEmissionColor"
    bl_label="Emission color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_EMISSION_COLOR
    octane_pin_name="emissionColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The emission color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialEmission(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_EMISSION
    octane_pin_name="emission"
    octane_pin_type=consts.PinType.PT_EMISSION
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialFilmwidth"
    bl_label="Film thickness (nm)"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_FILM_WIDTH
    octane_pin_name="filmwidth"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in nanometers", min=0.000000, max=2000.000000, soft_min=0.000000, soft_max=2000.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialFilmIor(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialFilmIor"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_FILM_IOR
    octane_pin_name="filmIor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000010
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialThinWall(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialThinWall"
    bl_label="Thin wall"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_THIN_WALL
    octane_pin_name="thinWall"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The geometry the material attached is a one sided planar, so the ray bounce exits the material immediately rather than entering the medium")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialBumpHeight(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialBumpHeight"
    bl_label="Bump height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BUMP_HEIGHT
    octane_pin_name="bumpHeight"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_DISPLACEMENT
    octane_pin_index=49
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH
    octane_pin_name="smooth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=50
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name="smoothShadowTerminator"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=51
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type=consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name="OctaneRoundEdges"
    octane_pin_id=consts.PinID.P_ROUND_EDGES
    octane_pin_name="roundEdges"
    octane_pin_type=consts.PinType.PT_ROUND_EDGES
    octane_pin_index=52
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=53
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialLayer(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialLayer"
    bl_label="Material layer"
    color=consts.OctanePinColor.MaterialLayer
    octane_default_node_type=consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name="OctaneMaterialLayerGroup"
    octane_pin_id=consts.PinID.P_LAYER
    octane_pin_name="layer"
    octane_pin_type=consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index=54
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStandardSurfaceMaterialIndexMap(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialIndexMap"
    bl_label="[Deprecated]Specular IOR"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_INDEX_MAP
    octane_pin_name="indexMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=55
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection or transmission", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000000
    octane_end_version=12000010
    octane_deprecated=True

class OctaneStandardSurfaceMaterialCoatingIndex(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialCoatingIndex"
    bl_label="[Deprecated]Coating IOR"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_INDEX
    octane_pin_name="coatingIndex"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=56
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="IOR of the coating layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=12000000
    octane_end_version=12000010
    octane_deprecated=True

class OctaneStandardSurfaceMaterialFilmindex(OctaneBaseSocket):
    bl_idname="OctaneStandardSurfaceMaterialFilmindex"
    bl_label="[Deprecated]Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FILM_INDEX
    octane_pin_name="filmindex"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=57
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000000
    octane_end_version=12000010
    octane_deprecated=True

class OctaneStandardSurfaceMaterialGroupBaseLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupBaseLayer"
    bl_label="[OctaneGroupTitle]Base Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Base weight;Base color;Diffuse roughness;Diffuse BRDF model;Metalness;")

class OctaneStandardSurfaceMaterialGroupSpecularLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupSpecularLayer"
    bl_label="[OctaneGroupTitle]Specular Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Specular weight;Specular color;Specular roughness;Specular IOR;Specular anisotropy;Specular rotation;Specular IOR;")

class OctaneStandardSurfaceMaterialGroupTransmissionLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupTransmissionLayer"
    bl_label="[OctaneGroupTitle]Transmission Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Transmission weight;Transmission color;Transmission depth;Scatter;Scatter anisotropy;Dispersion Coefficient;Dispersion mode;Extra roughness;Dielectric priority;Fake shadows;Affect alpha;Allow caustics;")

class OctaneStandardSurfaceMaterialGroupSubsurface(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupSubsurface"
    bl_label="[OctaneGroupTitle]Subsurface"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Subsurface weight;Subsurface color;Subsurface radius;Subsurface scale;Subsurface anisotropy;")

class OctaneStandardSurfaceMaterialGroupMedium(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupMedium"
    bl_label="[OctaneGroupTitle]Medium"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Override medium;")

class OctaneStandardSurfaceMaterialGroupCoatingLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupCoatingLayer"
    bl_label="[OctaneGroupTitle]Coating Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Coating weight;Coating color;Coating roughness;Coating IOR;Coating anisotropy;Coating rotation;Coating bump;Coating normal;Coating IOR;")

class OctaneStandardSurfaceMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupSheenLayer"
    bl_label="[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen weight;Sheen color;Sheen roughness;")

class OctaneStandardSurfaceMaterialGroupEmissionLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupEmissionLayer"
    bl_label="[OctaneGroupTitle]Emission Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emission weight;Emission color;Emission;")

class OctaneStandardSurfaceMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film thickness (nm);Film IOR;Film IOR;")

class OctaneStandardSurfaceMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneStandardSurfaceMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Thin wall;Bump;Bump height;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Opacity;")

class OctaneStandardSurfaceMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneStandardSurfaceMaterial"
    bl_label="Standard surface material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneStandardSurfaceMaterialGroupBaseLayer,OctaneStandardSurfaceMaterialBase,OctaneStandardSurfaceMaterialBaseColor,OctaneStandardSurfaceMaterialDiffuseRoughness,OctaneStandardSurfaceMaterialDiffuseBrdf,OctaneStandardSurfaceMaterialMetallic,OctaneStandardSurfaceMaterialGroupSpecularLayer,OctaneStandardSurfaceMaterialSpecular,OctaneStandardSurfaceMaterialSpecularColor,OctaneStandardSurfaceMaterialRoughness,OctaneStandardSurfaceMaterialIor,OctaneStandardSurfaceMaterialAnisotropyTexture,OctaneStandardSurfaceMaterialRotation,OctaneStandardSurfaceMaterialIndexMap,OctaneStandardSurfaceMaterialGroupTransmissionLayer,OctaneStandardSurfaceMaterialTransmission,OctaneStandardSurfaceMaterialTransmissionColor,OctaneStandardSurfaceMaterialTransmissionDepth,OctaneStandardSurfaceMaterialScattering,OctaneStandardSurfaceMaterialScatteringAnisotropy,OctaneStandardSurfaceMaterialDispersionCoefficientB,OctaneStandardSurfaceMaterialDispersionMode,OctaneStandardSurfaceMaterialRoughnessExtra,OctaneStandardSurfaceMaterialPriority,OctaneStandardSurfaceMaterialFakeShadows,OctaneStandardSurfaceMaterialRefractionAlpha,OctaneStandardSurfaceMaterialHasCaustics,OctaneStandardSurfaceMaterialGroupSubsurface,OctaneStandardSurfaceMaterialSubsurface,OctaneStandardSurfaceMaterialSubsurfaceColor,OctaneStandardSurfaceMaterialRadius,OctaneStandardSurfaceMaterialScale,OctaneStandardSurfaceMaterialSubsurfaceAnisotropy,OctaneStandardSurfaceMaterialGroupMedium,OctaneStandardSurfaceMaterialMedium,OctaneStandardSurfaceMaterialGroupCoatingLayer,OctaneStandardSurfaceMaterialCoating,OctaneStandardSurfaceMaterialCoatingColor,OctaneStandardSurfaceMaterialCoatingRoughness,OctaneStandardSurfaceMaterialCoatingIor,OctaneStandardSurfaceMaterialCoatingAnisotropy,OctaneStandardSurfaceMaterialCoatingRotation,OctaneStandardSurfaceMaterialCoatingBump,OctaneStandardSurfaceMaterialCoatingNormal,OctaneStandardSurfaceMaterialCoatingIndex,OctaneStandardSurfaceMaterialGroupSheenLayer,OctaneStandardSurfaceMaterialSheen,OctaneStandardSurfaceMaterialSheenColor,OctaneStandardSurfaceMaterialSheenRoughness,OctaneStandardSurfaceMaterialGroupEmissionLayer,OctaneStandardSurfaceMaterialEmissionWeight,OctaneStandardSurfaceMaterialEmissionColor,OctaneStandardSurfaceMaterialEmission,OctaneStandardSurfaceMaterialGroupThinFilmLayer,OctaneStandardSurfaceMaterialFilmwidth,OctaneStandardSurfaceMaterialFilmIor,OctaneStandardSurfaceMaterialFilmindex,OctaneStandardSurfaceMaterialGroupGeometryProperties,OctaneStandardSurfaceMaterialThinWall,OctaneStandardSurfaceMaterialBump,OctaneStandardSurfaceMaterialBumpHeight,OctaneStandardSurfaceMaterialNormal,OctaneStandardSurfaceMaterialDisplacement,OctaneStandardSurfaceMaterialSmooth,OctaneStandardSurfaceMaterialSmoothShadowTerminator,OctaneStandardSurfaceMaterialRoundEdges,OctaneStandardSurfaceMaterialOpacity,OctaneStandardSurfaceMaterialLayer,]
    octane_min_version=12000000
    octane_node_type=consts.NodeType.NT_MAT_STANDARD_SURFACE
    octane_socket_list=["Base weight", "Base color", "Diffuse roughness", "Diffuse BRDF model", "Metalness", "Specular weight", "Specular color", "Specular roughness", "Specular IOR", "Specular anisotropy", "Specular rotation", "Transmission weight", "Transmission color", "Transmission depth", "Scatter", "Scatter anisotropy", "Dispersion Coefficient", "Dispersion mode", "Extra roughness", "Dielectric priority", "Fake shadows", "Affect alpha", "Allow caustics", "Subsurface weight", "Subsurface color", "Subsurface radius", "Subsurface scale", "Subsurface anisotropy", "Override medium", "Coating weight", "Coating color", "Coating roughness", "Coating IOR", "Coating anisotropy", "Coating rotation", "Coating bump", "Coating normal", "Sheen weight", "Sheen color", "Sheen roughness", "Emission weight", "Emission color", "Emission", "Film thickness (nm)", "Film IOR", "Thin wall", "Bump", "Bump height", "Normal", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Opacity", "Material layer", "[Deprecated]Specular IOR", "[Deprecated]Coating IOR", "[Deprecated]Film IOR", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=55

    compatibility_mode_infos=[
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000006, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneStandardSurfaceMaterialGroupBaseLayer", OctaneStandardSurfaceMaterialGroupBaseLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialBase", OctaneStandardSurfaceMaterialBase.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialBaseColor", OctaneStandardSurfaceMaterialBaseColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialDiffuseRoughness", OctaneStandardSurfaceMaterialDiffuseRoughness.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialDiffuseBrdf", OctaneStandardSurfaceMaterialDiffuseBrdf.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialMetallic", OctaneStandardSurfaceMaterialMetallic.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupSpecularLayer", OctaneStandardSurfaceMaterialGroupSpecularLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSpecular", OctaneStandardSurfaceMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSpecularColor", OctaneStandardSurfaceMaterialSpecularColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRoughness", OctaneStandardSurfaceMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialIor", OctaneStandardSurfaceMaterialIor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialAnisotropyTexture", OctaneStandardSurfaceMaterialAnisotropyTexture.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRotation", OctaneStandardSurfaceMaterialRotation.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialIndexMap", OctaneStandardSurfaceMaterialIndexMap.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupTransmissionLayer", OctaneStandardSurfaceMaterialGroupTransmissionLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialTransmission", OctaneStandardSurfaceMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialTransmissionColor", OctaneStandardSurfaceMaterialTransmissionColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialTransmissionDepth", OctaneStandardSurfaceMaterialTransmissionDepth.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialScattering", OctaneStandardSurfaceMaterialScattering.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialScatteringAnisotropy", OctaneStandardSurfaceMaterialScatteringAnisotropy.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialDispersionCoefficientB", OctaneStandardSurfaceMaterialDispersionCoefficientB.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialDispersionMode", OctaneStandardSurfaceMaterialDispersionMode.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRoughnessExtra", OctaneStandardSurfaceMaterialRoughnessExtra.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialPriority", OctaneStandardSurfaceMaterialPriority.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialFakeShadows", OctaneStandardSurfaceMaterialFakeShadows.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRefractionAlpha", OctaneStandardSurfaceMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialHasCaustics", OctaneStandardSurfaceMaterialHasCaustics.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupSubsurface", OctaneStandardSurfaceMaterialGroupSubsurface.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSubsurface", OctaneStandardSurfaceMaterialSubsurface.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSubsurfaceColor", OctaneStandardSurfaceMaterialSubsurfaceColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRadius", OctaneStandardSurfaceMaterialRadius.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialScale", OctaneStandardSurfaceMaterialScale.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSubsurfaceAnisotropy", OctaneStandardSurfaceMaterialSubsurfaceAnisotropy.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupMedium", OctaneStandardSurfaceMaterialGroupMedium.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialMedium", OctaneStandardSurfaceMaterialMedium.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupCoatingLayer", OctaneStandardSurfaceMaterialGroupCoatingLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoating", OctaneStandardSurfaceMaterialCoating.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingColor", OctaneStandardSurfaceMaterialCoatingColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingRoughness", OctaneStandardSurfaceMaterialCoatingRoughness.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingIor", OctaneStandardSurfaceMaterialCoatingIor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingAnisotropy", OctaneStandardSurfaceMaterialCoatingAnisotropy.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingRotation", OctaneStandardSurfaceMaterialCoatingRotation.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingBump", OctaneStandardSurfaceMaterialCoatingBump.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingNormal", OctaneStandardSurfaceMaterialCoatingNormal.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialCoatingIndex", OctaneStandardSurfaceMaterialCoatingIndex.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupSheenLayer", OctaneStandardSurfaceMaterialGroupSheenLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSheen", OctaneStandardSurfaceMaterialSheen.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSheenColor", OctaneStandardSurfaceMaterialSheenColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSheenRoughness", OctaneStandardSurfaceMaterialSheenRoughness.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupEmissionLayer", OctaneStandardSurfaceMaterialGroupEmissionLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialEmissionWeight", OctaneStandardSurfaceMaterialEmissionWeight.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialEmissionColor", OctaneStandardSurfaceMaterialEmissionColor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialEmission", OctaneStandardSurfaceMaterialEmission.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupThinFilmLayer", OctaneStandardSurfaceMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialFilmwidth", OctaneStandardSurfaceMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialFilmIor", OctaneStandardSurfaceMaterialFilmIor.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialFilmindex", OctaneStandardSurfaceMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialGroupGeometryProperties", OctaneStandardSurfaceMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialThinWall", OctaneStandardSurfaceMaterialThinWall.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialBump", OctaneStandardSurfaceMaterialBump.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialBumpHeight", OctaneStandardSurfaceMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialNormal", OctaneStandardSurfaceMaterialNormal.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialDisplacement", OctaneStandardSurfaceMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSmooth", OctaneStandardSurfaceMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialSmoothShadowTerminator", OctaneStandardSurfaceMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialRoundEdges", OctaneStandardSurfaceMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialOpacity", OctaneStandardSurfaceMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneStandardSurfaceMaterialLayer", OctaneStandardSurfaceMaterialLayer.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneStandardSurfaceMaterialBase,
    OctaneStandardSurfaceMaterialBaseColor,
    OctaneStandardSurfaceMaterialDiffuseRoughness,
    OctaneStandardSurfaceMaterialDiffuseBrdf,
    OctaneStandardSurfaceMaterialMetallic,
    OctaneStandardSurfaceMaterialSpecular,
    OctaneStandardSurfaceMaterialSpecularColor,
    OctaneStandardSurfaceMaterialRoughness,
    OctaneStandardSurfaceMaterialIor,
    OctaneStandardSurfaceMaterialAnisotropyTexture,
    OctaneStandardSurfaceMaterialRotation,
    OctaneStandardSurfaceMaterialTransmission,
    OctaneStandardSurfaceMaterialTransmissionColor,
    OctaneStandardSurfaceMaterialTransmissionDepth,
    OctaneStandardSurfaceMaterialScattering,
    OctaneStandardSurfaceMaterialScatteringAnisotropy,
    OctaneStandardSurfaceMaterialDispersionCoefficientB,
    OctaneStandardSurfaceMaterialDispersionMode,
    OctaneStandardSurfaceMaterialRoughnessExtra,
    OctaneStandardSurfaceMaterialPriority,
    OctaneStandardSurfaceMaterialFakeShadows,
    OctaneStandardSurfaceMaterialRefractionAlpha,
    OctaneStandardSurfaceMaterialHasCaustics,
    OctaneStandardSurfaceMaterialSubsurface,
    OctaneStandardSurfaceMaterialSubsurfaceColor,
    OctaneStandardSurfaceMaterialRadius,
    OctaneStandardSurfaceMaterialScale,
    OctaneStandardSurfaceMaterialSubsurfaceAnisotropy,
    OctaneStandardSurfaceMaterialMedium,
    OctaneStandardSurfaceMaterialCoating,
    OctaneStandardSurfaceMaterialCoatingColor,
    OctaneStandardSurfaceMaterialCoatingRoughness,
    OctaneStandardSurfaceMaterialCoatingIor,
    OctaneStandardSurfaceMaterialCoatingAnisotropy,
    OctaneStandardSurfaceMaterialCoatingRotation,
    OctaneStandardSurfaceMaterialCoatingBump,
    OctaneStandardSurfaceMaterialCoatingNormal,
    OctaneStandardSurfaceMaterialSheen,
    OctaneStandardSurfaceMaterialSheenColor,
    OctaneStandardSurfaceMaterialSheenRoughness,
    OctaneStandardSurfaceMaterialEmissionWeight,
    OctaneStandardSurfaceMaterialEmissionColor,
    OctaneStandardSurfaceMaterialEmission,
    OctaneStandardSurfaceMaterialFilmwidth,
    OctaneStandardSurfaceMaterialFilmIor,
    OctaneStandardSurfaceMaterialThinWall,
    OctaneStandardSurfaceMaterialBump,
    OctaneStandardSurfaceMaterialBumpHeight,
    OctaneStandardSurfaceMaterialNormal,
    OctaneStandardSurfaceMaterialDisplacement,
    OctaneStandardSurfaceMaterialSmooth,
    OctaneStandardSurfaceMaterialSmoothShadowTerminator,
    OctaneStandardSurfaceMaterialRoundEdges,
    OctaneStandardSurfaceMaterialOpacity,
    OctaneStandardSurfaceMaterialLayer,
    OctaneStandardSurfaceMaterialIndexMap,
    OctaneStandardSurfaceMaterialCoatingIndex,
    OctaneStandardSurfaceMaterialFilmindex,
    OctaneStandardSurfaceMaterialGroupBaseLayer,
    OctaneStandardSurfaceMaterialGroupSpecularLayer,
    OctaneStandardSurfaceMaterialGroupTransmissionLayer,
    OctaneStandardSurfaceMaterialGroupSubsurface,
    OctaneStandardSurfaceMaterialGroupMedium,
    OctaneStandardSurfaceMaterialGroupCoatingLayer,
    OctaneStandardSurfaceMaterialGroupSheenLayer,
    OctaneStandardSurfaceMaterialGroupEmissionLayer,
    OctaneStandardSurfaceMaterialGroupThinFilmLayer,
    OctaneStandardSurfaceMaterialGroupGeometryProperties,
    OctaneStandardSurfaceMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
