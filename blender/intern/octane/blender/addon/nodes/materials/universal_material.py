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


class OctaneUniversalMaterialTransmission(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TRANSMISSION
    octane_pin_name="transmission"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialTransmissionType(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialTransmissionType"
    bl_label="Transmission type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_TRANSMISSION_TYPE
    octane_pin_name="transmissionType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Specular", "Specular", "", 0),
        ("Diffuse", "Diffuse", "", 1),
        ("Thin wall", "Thin wall", "", 2),
        ("Thin wall (diffuse)", "Thin wall (diffuse)", "", 3),
    ]
    default_value: EnumProperty(default="Specular", update=OctaneBaseSocket.update_node_tree, description="- Specular: Behaves the same as transmission of the specular material, i.e. taking IOR and roughness into account.\n- Diffuse: Behaves the same as transmission of the diffuse material, i.e. not taking IOR into account and roughness has the same meaning as in the diffuse material. If additional layers are used, the layer ordering is dependent on the side the incident ray comes from.\n- Thin wall: Behaves the same as mode \"Specular\" but with no refraction and no roughness for transmission. Also the medium is not applied either.\n- Thin wall (diffuse): Behaves the same as mode \"Diffuse\" with the exception that the layer ordering is independent of which side the incident ray comes from. Can be used with a coating layer for foliages and leaves", items=items)
    octane_hide_value=False
    octane_min_version=6000006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialAlbedo(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialAlbedo"
    bl_label="Albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_ALBEDO
    octane_pin_name="albedo"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=OctaneBaseSocket.update_node_tree, description="The base color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDiffuseBrdf(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDiffuseBrdf"
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
    default_value: EnumProperty(default="Lambertian", update=OctaneBaseSocket.update_node_tree, description="Diffuse BRDF model", items=items)
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMetallic(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMetallic"
    bl_label="Metallic"
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
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialEdgeTint(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialEdgeTint"
    bl_label="Metallic edge tint"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_EDGE_TINT
    octane_pin_name="edgeTint"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the edge of the metal, only used in metallic layer with artistic and IOR + color mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=11000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SPECULAR
    octane_pin_name="specular"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specular reflection channel which determines the color of glossy reflection for dielectric material. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBrdf(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBrdf"
    bl_label="BSDF model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BRDF
    octane_pin_name="brdf"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("GGX (energy preserving)", "GGX (energy preserving)", "", 6),
        ("STD", "STD", "", 7),
    ]
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="BSDF model", items=items)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRoughness(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS
    octane_pin_name="roughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular reflection and transmission channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANISOTROPY
    octane_pin_name="anisotropy"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular and transmissive material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRotation(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRotation"
    bl_label="Rotation"
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
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSpread(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD
    octane_pin_name="spread"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the specular/metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex4(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex4"
    bl_label="Dielectric IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INDEX4
    octane_pin_name="index4"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection or transmission. By default, if 1/IOR map is empty, then the dielectric specular layer uses this IOR", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndexMap(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndexMap"
    bl_label="Dielectric 1/IOR map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INDEX_MAP
    octane_pin_name="indexMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMetallicMode(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMetallicMode"
    bl_label="Metallic reflection mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_METALLIC_MODE
    octane_pin_name="metallicMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", update=OctaneBaseSocket.update_node_tree, description="Change how the reflectivity is calculated for metallic material:\n - Artistic: use only the albedo color.\n - IOR + color: use the albedo color, and adjust the brightness using the IOR.\n - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore albedo color", items=items)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex"
    bl_label="Metallic IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INDEX
    octane_pin_name="index"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection for metallic material.\nFor RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex2(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex2"
    bl_label="Metallic IOR (green)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INDEX2
    octane_pin_name="index2"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex3(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex3"
    bl_label="Metallic IOR (blue)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INDEX3
    octane_pin_name="index3"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialHasCaustics(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialHasCaustics"
    bl_label="Allow caustics"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_HAS_CAUSTICS
    octane_pin_name="hasCaustics"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the photon tracing kernel will create caustics for light reflecting or transmitting through this object")
    octane_hide_value=False
    octane_min_version=12000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoating(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoating"
    bl_label="Coating"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_COATING
    octane_pin_name="coating"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingRoughness(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingRoughness"
    bl_label="Coating roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_COATING_ROUGHNESS
    octane_pin_name="coatingRoughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the coating layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingIndex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingIndex"
    bl_label="Coating IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_COATING_INDEX
    octane_pin_name="coatingIndex"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="IOR of the coating layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingBump"
    bl_label="Coating bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_COATING_BUMP
    octane_pin_name="coatingBump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingNormal"
    bl_label="Coating normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_COATING_NORMAL
    octane_pin_name="coatingNormal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFilmwidth"
    bl_label="Film width (um)"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_FILM_WIDTH
    octane_pin_name="filmwidth"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating in micrometers", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFilmindex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_FILM_INDEX
    octane_pin_name="filmindex"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheen(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheen"
    bl_label="Sheen"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SHEEN
    octane_pin_name="sheen"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenRoughness"
    bl_label="Sheen roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_SHEEN_ROUGHNESS
    octane_pin_name="sheenRoughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenBump"
    bl_label="Sheen bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_SHEEN_BUMP
    octane_pin_name="sheenBump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenNormal"
    bl_label="Sheen normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_SHEEN_NORMAL
    octane_pin_name="sheenNormal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDispersionCoefficientB"
    bl_label="Dispersion Coefficient"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISPERSION_COEFFICIENT_B
    octane_pin_name="dispersion_coefficient_B"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The dispersion coefficient, the meaning depends on the selected dispersion mode", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDispersionMode(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDispersionMode"
    bl_label="Dispersion mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_DISPERSION_MODE
    octane_pin_name="dispersionMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=31
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

class OctaneUniversalMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFakeShadows(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFakeShadows"
    bl_label="Fake shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_FAKE_SHADOWS
    octane_pin_name="fake_shadows"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRefractionAlpha"
    bl_label="Affect alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_REFRACTION_ALPHA
    octane_pin_name="refractionAlpha"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to have refractions affect the alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBumpHeight(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBumpHeight"
    bl_label="Bump height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BUMP_HEIGHT
    octane_pin_name="bumpHeight"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_DISPLACEMENT
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH
    octane_pin_name="smooth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH_SHADOW_TERMINATOR
    octane_pin_name="smoothShadowTerminator"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type=consts.NodeType.NT_ROUND_EDGES
    octane_default_node_name="OctaneRoundEdges"
    octane_pin_id=consts.PinID.P_ROUND_EDGES
    octane_pin_name="roundEdges"
    octane_pin_type=consts.PinType.PT_ROUND_EDGES
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_PRIORITY
    octane_pin_name="priority"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=10020900
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialEmission(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_EMISSION
    octane_pin_name="emission"
    octane_pin_type=consts.PinType.PT_EMISSION
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMatte(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMatte"
    bl_label="Shadow catcher"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_MATTE
    octane_pin_name="matte"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV
    octane_pin_name="customAov"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_ENUM
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
        ("Custom AOV 11", "Custom AOV 11", "", 10),
        ("Custom AOV 12", "Custom AOV 12", "", 11),
        ("Custom AOV 13", "Custom AOV 13", "", 12),
        ("Custom AOV 14", "Custom AOV 14", "", 13),
        ("Custom AOV 15", "Custom AOV 15", "", 14),
        ("Custom AOV 16", "Custom AOV 16", "", 15),
        ("Custom AOV 17", "Custom AOV 17", "", 16),
        ("Custom AOV 18", "Custom AOV 18", "", 17),
        ("Custom AOV 19", "Custom AOV 19", "", 18),
        ("Custom AOV 20", "Custom AOV 20", "", 19),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name="customAovChannel"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialLayer(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialLayer"
    bl_label="Material layer"
    color=consts.OctanePinColor.MaterialLayer
    octane_default_node_type=consts.NodeType.NT_MAT_LAYER_GROUP
    octane_default_node_name="OctaneMaterialLayerGroup"
    octane_pin_id=consts.PinID.P_LAYER
    octane_pin_name="layer"
    octane_pin_type=consts.PinType.PT_MATERIAL_LAYER
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBtdf(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBtdf"
    bl_label="[Deprecated]Transmission model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BTDF
    octane_pin_name="btdf"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=49
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Beckmann", "Beckmann", "", 1),
        ("GGX", "GGX", "", 2),
        ("Lambertian", "Lambertian", "", 5),
    ]
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="Transmission model", items=items)
    octane_hide_value=False
    octane_min_version=5100001
    octane_end_version=6000006
    octane_deprecated=True

class OctaneUniversalMaterialEdgesRounding(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialEdgesRounding"
    bl_label="[Deprecated]Rounded edges radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_EDGES_ROUNDING
    octane_pin_name="edgesRounding"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=50
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=5100001
    octane_deprecated=True

class OctaneUniversalMaterialThinWall(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialThinWall"
    bl_label="[Deprecated]Thin wall"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_THIN_WALL
    octane_pin_name="thinWall"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=51
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The geometry the material attached is a one sided planar, so the ray bounce exits the material immediately rather than entering the medium")
    octane_hide_value=False
    octane_min_version=6000002
    octane_end_version=6000006
    octane_deprecated=True

class OctaneUniversalMaterialGroupTransmissionLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupTransmissionLayer"
    bl_label="[OctaneGroupTitle]Transmission Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Transmission;Transmission type;Transmission model;")

class OctaneUniversalMaterialGroupBaseLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupBaseLayer"
    bl_label="[OctaneGroupTitle]Base Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Albedo;Diffuse BRDF model;Metallic;Metallic edge tint;")

class OctaneUniversalMaterialGroupSpecularLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupSpecularLayer"
    bl_label="[OctaneGroupTitle]Specular Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Specular;BSDF model;")

class OctaneUniversalMaterialGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Anisotropy;Rotation;Spread;")

class OctaneUniversalMaterialGroupIOR(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupIOR"
    bl_label="[OctaneGroupTitle]IOR"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dielectric IOR;Dielectric 1/IOR map;Metallic reflection mode;Metallic IOR;Metallic IOR (green);Metallic IOR (blue);Allow caustics;")

class OctaneUniversalMaterialGroupCoatingLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupCoatingLayer"
    bl_label="[OctaneGroupTitle]Coating Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Coating;Coating roughness;Coating IOR;Coating bump;Coating normal;")

class OctaneUniversalMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width (um);Film IOR;")

class OctaneUniversalMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupSheenLayer"
    bl_label="[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen;Sheen roughness;Sheen bump;Sheen normal;")

class OctaneUniversalMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dispersion Coefficient;Dispersion mode;Medium;Opacity;Fake shadows;Affect alpha;Thin wall;")

class OctaneUniversalMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneUniversalMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUniversalMaterial"
    bl_label="Universal material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneUniversalMaterialGroupTransmissionLayer,OctaneUniversalMaterialTransmission,OctaneUniversalMaterialTransmissionType,OctaneUniversalMaterialBtdf,OctaneUniversalMaterialGroupBaseLayer,OctaneUniversalMaterialAlbedo,OctaneUniversalMaterialDiffuseBrdf,OctaneUniversalMaterialMetallic,OctaneUniversalMaterialEdgeTint,OctaneUniversalMaterialGroupSpecularLayer,OctaneUniversalMaterialSpecular,OctaneUniversalMaterialBrdf,OctaneUniversalMaterialGroupRoughness,OctaneUniversalMaterialRoughness,OctaneUniversalMaterialAnisotropy,OctaneUniversalMaterialRotation,OctaneUniversalMaterialSpread,OctaneUniversalMaterialGroupIOR,OctaneUniversalMaterialIndex4,OctaneUniversalMaterialIndexMap,OctaneUniversalMaterialMetallicMode,OctaneUniversalMaterialIndex,OctaneUniversalMaterialIndex2,OctaneUniversalMaterialIndex3,OctaneUniversalMaterialHasCaustics,OctaneUniversalMaterialGroupCoatingLayer,OctaneUniversalMaterialCoating,OctaneUniversalMaterialCoatingRoughness,OctaneUniversalMaterialCoatingIndex,OctaneUniversalMaterialCoatingBump,OctaneUniversalMaterialCoatingNormal,OctaneUniversalMaterialGroupThinFilmLayer,OctaneUniversalMaterialFilmwidth,OctaneUniversalMaterialFilmindex,OctaneUniversalMaterialGroupSheenLayer,OctaneUniversalMaterialSheen,OctaneUniversalMaterialSheenRoughness,OctaneUniversalMaterialSheenBump,OctaneUniversalMaterialSheenNormal,OctaneUniversalMaterialGroupTransmissionProperties,OctaneUniversalMaterialDispersionCoefficientB,OctaneUniversalMaterialDispersionMode,OctaneUniversalMaterialMedium,OctaneUniversalMaterialOpacity,OctaneUniversalMaterialFakeShadows,OctaneUniversalMaterialRefractionAlpha,OctaneUniversalMaterialThinWall,OctaneUniversalMaterialGroupGeometryProperties,OctaneUniversalMaterialBump,OctaneUniversalMaterialBumpHeight,OctaneUniversalMaterialNormal,OctaneUniversalMaterialDisplacement,OctaneUniversalMaterialSmooth,OctaneUniversalMaterialSmoothShadowTerminator,OctaneUniversalMaterialRoundEdges,OctaneUniversalMaterialPriority,OctaneUniversalMaterialEmission,OctaneUniversalMaterialMatte,OctaneUniversalMaterialCustomAov,OctaneUniversalMaterialCustomAovChannel,OctaneUniversalMaterialLayer,OctaneUniversalMaterialEdgesRounding,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_UNIVERSAL
    octane_socket_list=["Transmission", "Transmission type", "Albedo", "Diffuse BRDF model", "Metallic", "Metallic edge tint", "Specular", "BSDF model", "Roughness", "Anisotropy", "Rotation", "Spread", "Dielectric IOR", "Dielectric 1/IOR map", "Metallic reflection mode", "Metallic IOR", "Metallic IOR (green)", "Metallic IOR (blue)", "Allow caustics", "Coating", "Coating roughness", "Coating IOR", "Coating bump", "Coating normal", "Film width (um)", "Film IOR", "Sheen", "Sheen roughness", "Sheen bump", "Sheen normal", "Dispersion Coefficient", "Dispersion mode", "Medium", "Opacity", "Fake shadows", "Affect alpha", "Bump", "Bump height", "Normal", "Displacement", "Smooth", "Smooth shadow terminator", "Round edges", "Priority", "Emission", "Shadow catcher", "Custom AOV", "Custom AOV channel", "Material layer", "[Deprecated]Transmission model", "[Deprecated]Rounded edges radius", "[Deprecated]Thin wall", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=49

    compatibility_mode_infos=[
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Legacy behaviour for bump map strength is active and bump map height is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000009, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneUniversalMaterialGroupTransmissionLayer", OctaneUniversalMaterialGroupTransmissionLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialTransmission", OctaneUniversalMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialTransmissionType", OctaneUniversalMaterialTransmissionType.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBtdf", OctaneUniversalMaterialBtdf.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupBaseLayer", OctaneUniversalMaterialGroupBaseLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialAlbedo", OctaneUniversalMaterialAlbedo.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialDiffuseBrdf", OctaneUniversalMaterialDiffuseBrdf.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialMetallic", OctaneUniversalMaterialMetallic.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialEdgeTint", OctaneUniversalMaterialEdgeTint.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupSpecularLayer", OctaneUniversalMaterialGroupSpecularLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSpecular", OctaneUniversalMaterialSpecular.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBrdf", OctaneUniversalMaterialBrdf.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupRoughness", OctaneUniversalMaterialGroupRoughness.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialRoughness", OctaneUniversalMaterialRoughness.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialAnisotropy", OctaneUniversalMaterialAnisotropy.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialRotation", OctaneUniversalMaterialRotation.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSpread", OctaneUniversalMaterialSpread.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupIOR", OctaneUniversalMaterialGroupIOR.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialIndex4", OctaneUniversalMaterialIndex4.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialIndexMap", OctaneUniversalMaterialIndexMap.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialMetallicMode", OctaneUniversalMaterialMetallicMode.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialIndex", OctaneUniversalMaterialIndex.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialIndex2", OctaneUniversalMaterialIndex2.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialIndex3", OctaneUniversalMaterialIndex3.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialHasCaustics", OctaneUniversalMaterialHasCaustics.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupCoatingLayer", OctaneUniversalMaterialGroupCoatingLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCoating", OctaneUniversalMaterialCoating.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCoatingRoughness", OctaneUniversalMaterialCoatingRoughness.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCoatingIndex", OctaneUniversalMaterialCoatingIndex.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCoatingBump", OctaneUniversalMaterialCoatingBump.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCoatingNormal", OctaneUniversalMaterialCoatingNormal.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupThinFilmLayer", OctaneUniversalMaterialGroupThinFilmLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialFilmwidth", OctaneUniversalMaterialFilmwidth.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialFilmindex", OctaneUniversalMaterialFilmindex.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupSheenLayer", OctaneUniversalMaterialGroupSheenLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSheen", OctaneUniversalMaterialSheen.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSheenRoughness", OctaneUniversalMaterialSheenRoughness.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSheenBump", OctaneUniversalMaterialSheenBump.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSheenNormal", OctaneUniversalMaterialSheenNormal.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupTransmissionProperties", OctaneUniversalMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialDispersionCoefficientB", OctaneUniversalMaterialDispersionCoefficientB.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialDispersionMode", OctaneUniversalMaterialDispersionMode.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialMedium", OctaneUniversalMaterialMedium.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialOpacity", OctaneUniversalMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialFakeShadows", OctaneUniversalMaterialFakeShadows.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialRefractionAlpha", OctaneUniversalMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialThinWall", OctaneUniversalMaterialThinWall.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupGeometryProperties", OctaneUniversalMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBump", OctaneUniversalMaterialBump.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBumpHeight", OctaneUniversalMaterialBumpHeight.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialNormal", OctaneUniversalMaterialNormal.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialDisplacement", OctaneUniversalMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSmooth", OctaneUniversalMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialSmoothShadowTerminator", OctaneUniversalMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialRoundEdges", OctaneUniversalMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialPriority", OctaneUniversalMaterialPriority.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialEmission", OctaneUniversalMaterialEmission.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialMatte", OctaneUniversalMaterialMatte.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCustomAov", OctaneUniversalMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialCustomAovChannel", OctaneUniversalMaterialCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialLayer", OctaneUniversalMaterialLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialEdgesRounding", OctaneUniversalMaterialEdgesRounding.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneUniversalMaterialTransmission,
    OctaneUniversalMaterialTransmissionType,
    OctaneUniversalMaterialAlbedo,
    OctaneUniversalMaterialDiffuseBrdf,
    OctaneUniversalMaterialMetallic,
    OctaneUniversalMaterialEdgeTint,
    OctaneUniversalMaterialSpecular,
    OctaneUniversalMaterialBrdf,
    OctaneUniversalMaterialRoughness,
    OctaneUniversalMaterialAnisotropy,
    OctaneUniversalMaterialRotation,
    OctaneUniversalMaterialSpread,
    OctaneUniversalMaterialIndex4,
    OctaneUniversalMaterialIndexMap,
    OctaneUniversalMaterialMetallicMode,
    OctaneUniversalMaterialIndex,
    OctaneUniversalMaterialIndex2,
    OctaneUniversalMaterialIndex3,
    OctaneUniversalMaterialHasCaustics,
    OctaneUniversalMaterialCoating,
    OctaneUniversalMaterialCoatingRoughness,
    OctaneUniversalMaterialCoatingIndex,
    OctaneUniversalMaterialCoatingBump,
    OctaneUniversalMaterialCoatingNormal,
    OctaneUniversalMaterialFilmwidth,
    OctaneUniversalMaterialFilmindex,
    OctaneUniversalMaterialSheen,
    OctaneUniversalMaterialSheenRoughness,
    OctaneUniversalMaterialSheenBump,
    OctaneUniversalMaterialSheenNormal,
    OctaneUniversalMaterialDispersionCoefficientB,
    OctaneUniversalMaterialDispersionMode,
    OctaneUniversalMaterialMedium,
    OctaneUniversalMaterialOpacity,
    OctaneUniversalMaterialFakeShadows,
    OctaneUniversalMaterialRefractionAlpha,
    OctaneUniversalMaterialBump,
    OctaneUniversalMaterialBumpHeight,
    OctaneUniversalMaterialNormal,
    OctaneUniversalMaterialDisplacement,
    OctaneUniversalMaterialSmooth,
    OctaneUniversalMaterialSmoothShadowTerminator,
    OctaneUniversalMaterialRoundEdges,
    OctaneUniversalMaterialPriority,
    OctaneUniversalMaterialEmission,
    OctaneUniversalMaterialMatte,
    OctaneUniversalMaterialCustomAov,
    OctaneUniversalMaterialCustomAovChannel,
    OctaneUniversalMaterialLayer,
    OctaneUniversalMaterialBtdf,
    OctaneUniversalMaterialEdgesRounding,
    OctaneUniversalMaterialThinWall,
    OctaneUniversalMaterialGroupTransmissionLayer,
    OctaneUniversalMaterialGroupBaseLayer,
    OctaneUniversalMaterialGroupSpecularLayer,
    OctaneUniversalMaterialGroupRoughness,
    OctaneUniversalMaterialGroupIOR,
    OctaneUniversalMaterialGroupCoatingLayer,
    OctaneUniversalMaterialGroupThinFilmLayer,
    OctaneUniversalMaterialGroupSheenLayer,
    OctaneUniversalMaterialGroupTransmissionProperties,
    OctaneUniversalMaterialGroupGeometryProperties,
    OctaneUniversalMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
