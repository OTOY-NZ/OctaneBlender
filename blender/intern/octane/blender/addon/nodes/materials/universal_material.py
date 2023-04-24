##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneUniversalMaterialTransmission(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transmission")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialTransmissionType(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialTransmissionType"
    bl_label="Transmission type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=506)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transmissionType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Specular", "Specular", "", 0),
        ("Diffuse", "Diffuse", "", 1),
        ("Thin wall", "Thin wall", "", 2),
        ("Thin wall (diffuse)", "Thin wall (diffuse)", "", 3),
    ]
    default_value: EnumProperty(default="Specular", update=OctaneBaseSocket.update_node_tree, description="- Specular: Behaves the same as transmission of the specular material, i.e. taking IOR and roughness into account.\n- Diffuse: Behaves the same as transmission of the diffuse material, i.e. not taking IOR into account and roughness has the same meaning as in the diffuse material. If additional layers are used, the layer ordering is dependent on the side the incident ray comes from.\n- Thin wall: Behaves the same as mode \"Specular\" but with no refraction and no roughness for transmission. Also the medium is not applied either.\n- Thin wall (diffuse): Behaves the same as mode \"Diffuse\" with the exception that the layer ordering is independent of which side the incident ray comes from. Can be used with a coating layer for foliages and leaves.\n", items=items)
    octane_hide_value=False
    octane_min_version=6000006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialAlbedo(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialAlbedo"
    bl_label="Albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=409)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="albedo")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=OctaneBaseSocket.update_node_tree, description="The base color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMetallic(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMetallic"
    bl_label="Metallic"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=410)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="metallic")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The metallic-ness of the material, blends between dielectric and metallic material", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialEdgeTint(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialEdgeTint"
    bl_label="Metallic edge tint"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=732)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="edgeTint")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the edge of the metal, only used in metallic layer with artistic and IOR + color mode", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=11000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSpecular(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSpecular"
    bl_label="Specular"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="specular")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Specular reflection channel which determines the color of glossy reflection for dielectric material. If the index of reflection is set to a value > 0, then the brightness of this color is adjusted so it matches the Fresnel equations", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBrdf(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBrdf"
    bl_label="BSDF model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=357)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="brdf")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="roughness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the specular reflection and transmission channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialAnisotropy(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialAnisotropy"
    bl_label="Anisotropy"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=358)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="anisotropy")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The anisotropy of the specular and transmissive material, -1 is horizontal and 1 is vertical, 0 is isotropy", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRotation(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRotation"
    bl_label="Rotation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rotation")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Rotation of the anisotropic specular reflection and transmission channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSpread(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="spread")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="The spread of the tail of the specular BSDF model (STD only) of the specular/metallic layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex4(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex4"
    bl_label="Dielectric IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=411)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index4")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction controlling the Fresnel effect of the specular reflection or transmission. By default, if 1/IOR map is empty, then the dielectric specular layer uses this IOR", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndexMap(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndexMap"
    bl_label="Dielectric 1/IOR map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=440)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="indexMap")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMetallicMode(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMetallicMode"
    bl_label="Metallic reflection mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=376)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="metallicMode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Artistic", "Artistic", "", 0),
        ("IOR + color", "IOR + color", "", 1),
        ("RGB IOR", "RGB IOR", "", 2),
    ]
    default_value: EnumProperty(default="Artistic", update=OctaneBaseSocket.update_node_tree, description="Change how the reflectivity is calculated for metallic material:\n - Artistic: use only the albedo color.\n - IOR + color: use the albedo color, and adjust the brightness using the IOR.\n - RGB IOR: use only the 3 IOR values (for 650, 550 and 450 nm) and ignore albedo color.\n", items=items)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex"
    bl_label="Metallic IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=80)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Complex-valued index of refraction (n - k*i) controlling the Fresnel effect of the specular reflection for metallic material.\nFor RGB mode, the IOR for red light (650 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex2(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex2"
    bl_label="Metallic IOR (green)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=374)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index2")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for green light (550 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialIndex3(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialIndex3"
    bl_label="Metallic IOR (blue)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=375)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="index3")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="For RGB mode, the IOR for blue light (450 nm)", min=0.000000, max=8.000000, soft_min=0.000000, soft_max=8.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoating(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoating"
    bl_label="Coating"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=437)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coating")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The coating color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingRoughness(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingRoughness"
    bl_label="Coating roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=438)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coatingRoughness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.063200, update=OctaneBaseSocket.update_node_tree, description="Roughness of the coating layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingIndex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingIndex"
    bl_label="Coating IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=439)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coatingIndex")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.500000, update=OctaneBaseSocket.update_node_tree, description="IOR of the coating layer", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingBump"
    bl_label="Coating bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=477)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coatingBump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCoatingNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCoatingNormal"
    bl_label="Coating normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=478)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coatingNormal")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFilmwidth(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFilmwidth"
    bl_label="Film width"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=49)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filmwidth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Thickness of the film coating", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFilmindex(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFilmindex"
    bl_label="Film IOR"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=48)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filmindex")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.450000, update=OctaneBaseSocket.update_node_tree, description="Index of refraction of the film coating", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheen(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheen"
    bl_label="Sheen"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sheen")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The sheen color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenRoughness"
    bl_label="Sheen roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sheenRoughness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen channel", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenBump"
    bl_label="Sheen bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=483)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sheenBump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSheenNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSheenNormal"
    bl_label="Sheen normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=484)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="sheenNormal")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4030000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDispersionCoefficientB(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDispersionCoefficientB"
    bl_label="Dispersion coefficient"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=33)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="dispersion_coefficient_B")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="B parameter of the Cauchy dispersion model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="medium")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="opacity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialFakeShadows(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialFakeShadows"
    bl_label="Fake shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=46)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="fake_shadows")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, light will be traced directly through the material during the shadow calculation, ignoring refraction")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRefractionAlpha"
    bl_label="Affect alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=146)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="refractionAlpha")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable to have refractions affect the alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBump(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialNormal(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="normal")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="displacement")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="smooth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="smoothShadowTerminator")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type=137
    octane_default_node_name="OctaneRoundEdges"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="roundEdges")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="priority")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10020900
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialEmission(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="emission")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialMatte(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialMatte"
    bl_label="Shadow catcher"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=102)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="matte")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="customAov")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="customAovChannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    octane_default_node_type=144
    octane_default_node_name="OctaneMaterialLayerGroup"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="layer")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=5100002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneUniversalMaterialBtdf(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialBtdf"
    bl_label="Transmission model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=481)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="btdf")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    bl_label="Rounded edges radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=39)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="edgesRounding")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Radius of rounded edges that are rendered as shading effect", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=5100001
    octane_deprecated=True

class OctaneUniversalMaterialThinWall(OctaneBaseSocket):
    bl_idname="OctaneUniversalMaterialThinWall"
    bl_label="Thin wall"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=482)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="thinWall")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
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
    octane_group_sockets: StringProperty(name="Group Sockets", default="Albedo;Metallic;Metallic edge tint;")

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
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dielectric IOR;Dielectric 1/IOR map;Metallic reflection mode;Metallic IOR;Metallic IOR (green);Metallic IOR (blue);")

class OctaneUniversalMaterialGroupCoatingLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupCoatingLayer"
    bl_label="[OctaneGroupTitle]Coating Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Coating;Coating roughness;Coating IOR;Coating bump;Coating normal;")

class OctaneUniversalMaterialGroupThinFilmLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupThinFilmLayer"
    bl_label="[OctaneGroupTitle]Thin Film Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Film width;Film IOR;")

class OctaneUniversalMaterialGroupSheenLayer(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupSheenLayer"
    bl_label="[OctaneGroupTitle]Sheen Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sheen;Sheen roughness;Sheen bump;Sheen normal;")

class OctaneUniversalMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Dispersion coefficient;Medium;Opacity;Fake shadows;Affect alpha;Thin wall;")

class OctaneUniversalMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneUniversalMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneUniversalMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneUniversalMaterial"
    bl_label="Universal material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=130)
    octane_socket_list: StringProperty(name="Socket List", default="Transmission;Transmission type;Albedo;Metallic;Metallic edge tint;Specular;BSDF model;Roughness;Anisotropy;Rotation;Spread;Dielectric IOR;Dielectric 1/IOR map;Metallic reflection mode;Metallic IOR;Metallic IOR (green);Metallic IOR (blue);Coating;Coating roughness;Coating IOR;Coating bump;Coating normal;Film width;Film IOR;Sheen;Sheen roughness;Sheen bump;Sheen normal;Dispersion coefficient;Medium;Opacity;Fake shadows;Affect alpha;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Emission;Shadow catcher;Custom AOV;Custom AOV channel;Material layer;Transmission model;Rounded edges radius;Thin wall;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=48)

    def init(self, context):
        self.inputs.new("OctaneUniversalMaterialGroupTransmissionLayer", OctaneUniversalMaterialGroupTransmissionLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialTransmission", OctaneUniversalMaterialTransmission.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialTransmissionType", OctaneUniversalMaterialTransmissionType.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBtdf", OctaneUniversalMaterialBtdf.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupBaseLayer", OctaneUniversalMaterialGroupBaseLayer.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialAlbedo", OctaneUniversalMaterialAlbedo.bl_label).init()
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
        self.inputs.new("OctaneUniversalMaterialMedium", OctaneUniversalMaterialMedium.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialOpacity", OctaneUniversalMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialFakeShadows", OctaneUniversalMaterialFakeShadows.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialRefractionAlpha", OctaneUniversalMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialThinWall", OctaneUniversalMaterialThinWall.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialGroupGeometryProperties", OctaneUniversalMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneUniversalMaterialBump", OctaneUniversalMaterialBump.bl_label).init()
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


_CLASSES=[
    OctaneUniversalMaterialTransmission,
    OctaneUniversalMaterialTransmissionType,
    OctaneUniversalMaterialAlbedo,
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
    OctaneUniversalMaterialMedium,
    OctaneUniversalMaterialOpacity,
    OctaneUniversalMaterialFakeShadows,
    OctaneUniversalMaterialRefractionAlpha,
    OctaneUniversalMaterialBump,
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
