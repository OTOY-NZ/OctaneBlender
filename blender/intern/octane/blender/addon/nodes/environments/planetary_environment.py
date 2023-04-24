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


class OctanePlanetaryEnvironmentSundir(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSundir"
    bl_label="Sun direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_SUN_DIRECTION
    octane_default_node_name="OctaneSunDirection"
    octane_pin_id=consts.PinID.P_SUN_DIR
    octane_pin_name="sundir"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Vector which defines the direction from which the sun is shining", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentTurbidity"
    bl_label="Sky turbidity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TURBIDITY
    octane_pin_name="turbidity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.400000, update=OctaneBaseSocket.update_node_tree, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPower(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scale factor that is applied to the sun and sky", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSunIntensity"
    bl_label="Sun intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUN_INTENSITY
    octane_pin_name="sunIntensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Scale factor that is applied to the sun only. Use this to adjust the relative power of the sun compared to the sky.\n\nNote: values other than 1.0 can produce unrealistic results because in the real world the sky is lit by the sun. Adjusting the balance between the yellowish sun and the bluish sky can also produce a hue shift in the scene", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=8000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentNorthoffset"
    bl_label="North offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NORTHOFFSET
    octane_pin_name="northoffset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentSunSize(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentSunSize"
    bl_label="Sun size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUN_SIZE
    octane_pin_name="sun_size"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degrees)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryAltitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAltitude"
    bl_label="Altitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_PLANETARY_ALTITUDE
    octane_pin_name="planetaryAltitude"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The camera altitude", min=0.100000, max=340282346638528859811704183484516925440.000000, soft_min=0.100000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryStarField(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryStarField"
    bl_label="Star field"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_PLANETARY_STAR_FIELD
    octane_pin_name="planetaryStarField"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentImportanceSampling"
    bl_label="Importance sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMPORTANCE_SAMPLING
    octane_pin_name="importance_sampling"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Use importance sampling for image textures")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentMedium(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MEDIUM_RADIUS
    octane_pin_name="mediumRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLightPassMask"
    bl_label="Medium light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type=consts.NodeType.NT_BIT_MASK
    octane_default_node_name="OctaneBitValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_MASK
    octane_pin_name="lightPassMask"
    octane_pin_type=consts.PinType.PT_BIT_MASK
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLatitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLatitude"
    bl_label="Latitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LATITUDE
    octane_pin_name="latitude"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Latitude coordinate where we are currently positioned", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4010000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentLongitude(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentLongitude"
    bl_label="Longitude"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LONGITUDE
    octane_pin_name="longitude"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Longitude coordinate where we are currently positioned", min=-180.000000, max=180.000000, soft_min=-180.000000, soft_max=180.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4010000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryDiffuse(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryDiffuse"
    bl_label="Ground albedo"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_PLANETARY_DIFFUSE_MAP
    octane_pin_name="planetaryDiffuse"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.031928, 0.130434, 0.557292), update=OctaneBaseSocket.update_node_tree, description="Surface texture map on the planet", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetarySpecular(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetarySpecular"
    bl_label="Ground reflection"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_PLANETARY_SPECULAR_MAP
    octane_pin_name="planetarySpecular"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryGlossiness(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryGlossiness"
    bl_label="Ground glossiness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_PLANETARY_GLOSSINESS
    octane_pin_name="planetaryGlossiness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryEmission(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryEmission"
    bl_label="Ground emission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_PLANETARY_EMISSION_MAP
    octane_pin_name="planetaryEmission"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Surface texture map on the planet at night time", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=4000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryNormal(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryNormal"
    bl_label="Ground normal map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_PLANETARY_NORMAL_MAP
    octane_pin_name="planetaryNormal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryElevation(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryElevation"
    bl_label="Ground elevation"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_PLANETARY_ELEVATION_MAP
    octane_pin_name="planetaryElevation"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentBackplate"
    bl_label="Backplate"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_BACKPLATE
    octane_pin_name="visibleEnvironmentBackplate"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will behave as a backplate image")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentReflections"
    bl_label="Reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFLECTIONS
    octane_pin_name="visibleEnvironmentReflections"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentVisibleEnvironmentRefractions"
    bl_label="Refractions"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFRACTIONS
    octane_pin_name="visibleEnvironmentRefractions"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in refractions")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlanetaryEnvironmentPlanetaryAxis(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAxis"
    bl_label="Planetary axis"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_PLANETARY_AXIS
    octane_pin_name="planetaryAxis"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="(deprecated) The rotational axis of the planet running through the north and south poles", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4010000
    octane_deprecated=True

class OctanePlanetaryEnvironmentPlanetaryAngle(OctaneBaseSocket):
    bl_idname="OctanePlanetaryEnvironmentPlanetaryAngle"
    bl_label="Planetary angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_PLANETARY_ANGLE
    octane_pin_name="planetaryAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) The rotation around the planetary axis", min=-3.141593, max=3.141593, soft_min=-3.141593, soft_max=3.141593, step=1, precision=4, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4010000
    octane_deprecated=True

class OctanePlanetaryEnvironmentGroupPlanetarySurface(OctaneGroupTitleSocket):
    bl_idname="OctanePlanetaryEnvironmentGroupPlanetarySurface"
    bl_label="[OctaneGroupTitle]Planetary surface"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Ground albedo;Ground reflection;Ground glossiness;Ground emission;Ground normal map;Ground elevation;")

class OctanePlanetaryEnvironmentGroupVisibleEnvironment(OctaneGroupTitleSocket):
    bl_idname="OctanePlanetaryEnvironmentGroupVisibleEnvironment"
    bl_label="[OctaneGroupTitle]Visible environment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Backplate;Reflections;Refractions;")

class OctanePlanetaryEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePlanetaryEnvironment"
    bl_label="Planetary environment"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctanePlanetaryEnvironmentSundir,OctanePlanetaryEnvironmentTurbidity,OctanePlanetaryEnvironmentPower,OctanePlanetaryEnvironmentSunIntensity,OctanePlanetaryEnvironmentNorthoffset,OctanePlanetaryEnvironmentSunSize,OctanePlanetaryEnvironmentPlanetaryAltitude,OctanePlanetaryEnvironmentPlanetaryStarField,OctanePlanetaryEnvironmentImportanceSampling,OctanePlanetaryEnvironmentMedium,OctanePlanetaryEnvironmentMediumRadius,OctanePlanetaryEnvironmentLightPassMask,OctanePlanetaryEnvironmentLatitude,OctanePlanetaryEnvironmentLongitude,OctanePlanetaryEnvironmentGroupPlanetarySurface,OctanePlanetaryEnvironmentPlanetaryDiffuse,OctanePlanetaryEnvironmentPlanetarySpecular,OctanePlanetaryEnvironmentPlanetaryGlossiness,OctanePlanetaryEnvironmentPlanetaryEmission,OctanePlanetaryEnvironmentPlanetaryNormal,OctanePlanetaryEnvironmentPlanetaryElevation,OctanePlanetaryEnvironmentGroupVisibleEnvironment,OctanePlanetaryEnvironmentVisibleEnvironmentBackplate,OctanePlanetaryEnvironmentVisibleEnvironmentReflections,OctanePlanetaryEnvironmentVisibleEnvironmentRefractions,OctanePlanetaryEnvironmentPlanetaryAxis,OctanePlanetaryEnvironmentPlanetaryAngle,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_ENV_PLANETARY
    octane_socket_list=["Sun direction", "Sky turbidity", "Power", "Sun intensity", "North offset", "Sun size", "Altitude", "Star field", "Importance sampling", "Medium", "Medium radius", "Medium light pass mask", "Latitude", "Longitude", "Ground albedo", "Ground reflection", "Ground glossiness", "Ground emission", "Ground normal map", "Ground elevation", "Backplate", "Reflections", "Refractions", "Planetary axis", "Planetary angle", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=23

    def init(self, context):
        self.inputs.new("OctanePlanetaryEnvironmentSundir", OctanePlanetaryEnvironmentSundir.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentTurbidity", OctanePlanetaryEnvironmentTurbidity.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPower", OctanePlanetaryEnvironmentPower.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentSunIntensity", OctanePlanetaryEnvironmentSunIntensity.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentNorthoffset", OctanePlanetaryEnvironmentNorthoffset.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentSunSize", OctanePlanetaryEnvironmentSunSize.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAltitude", OctanePlanetaryEnvironmentPlanetaryAltitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryStarField", OctanePlanetaryEnvironmentPlanetaryStarField.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentImportanceSampling", OctanePlanetaryEnvironmentImportanceSampling.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentMedium", OctanePlanetaryEnvironmentMedium.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentMediumRadius", OctanePlanetaryEnvironmentMediumRadius.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLightPassMask", OctanePlanetaryEnvironmentLightPassMask.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLatitude", OctanePlanetaryEnvironmentLatitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentLongitude", OctanePlanetaryEnvironmentLongitude.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentGroupPlanetarySurface", OctanePlanetaryEnvironmentGroupPlanetarySurface.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryDiffuse", OctanePlanetaryEnvironmentPlanetaryDiffuse.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetarySpecular", OctanePlanetaryEnvironmentPlanetarySpecular.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryGlossiness", OctanePlanetaryEnvironmentPlanetaryGlossiness.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryEmission", OctanePlanetaryEnvironmentPlanetaryEmission.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryNormal", OctanePlanetaryEnvironmentPlanetaryNormal.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryElevation", OctanePlanetaryEnvironmentPlanetaryElevation.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentGroupVisibleEnvironment", OctanePlanetaryEnvironmentGroupVisibleEnvironment.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentBackplate", OctanePlanetaryEnvironmentVisibleEnvironmentBackplate.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentReflections", OctanePlanetaryEnvironmentVisibleEnvironmentReflections.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentVisibleEnvironmentRefractions", OctanePlanetaryEnvironmentVisibleEnvironmentRefractions.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAxis", OctanePlanetaryEnvironmentPlanetaryAxis.bl_label).init()
        self.inputs.new("OctanePlanetaryEnvironmentPlanetaryAngle", OctanePlanetaryEnvironmentPlanetaryAngle.bl_label).init()
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out").init()


_CLASSES=[
    OctanePlanetaryEnvironmentSundir,
    OctanePlanetaryEnvironmentTurbidity,
    OctanePlanetaryEnvironmentPower,
    OctanePlanetaryEnvironmentSunIntensity,
    OctanePlanetaryEnvironmentNorthoffset,
    OctanePlanetaryEnvironmentSunSize,
    OctanePlanetaryEnvironmentPlanetaryAltitude,
    OctanePlanetaryEnvironmentPlanetaryStarField,
    OctanePlanetaryEnvironmentImportanceSampling,
    OctanePlanetaryEnvironmentMedium,
    OctanePlanetaryEnvironmentMediumRadius,
    OctanePlanetaryEnvironmentLightPassMask,
    OctanePlanetaryEnvironmentLatitude,
    OctanePlanetaryEnvironmentLongitude,
    OctanePlanetaryEnvironmentPlanetaryDiffuse,
    OctanePlanetaryEnvironmentPlanetarySpecular,
    OctanePlanetaryEnvironmentPlanetaryGlossiness,
    OctanePlanetaryEnvironmentPlanetaryEmission,
    OctanePlanetaryEnvironmentPlanetaryNormal,
    OctanePlanetaryEnvironmentPlanetaryElevation,
    OctanePlanetaryEnvironmentVisibleEnvironmentBackplate,
    OctanePlanetaryEnvironmentVisibleEnvironmentReflections,
    OctanePlanetaryEnvironmentVisibleEnvironmentRefractions,
    OctanePlanetaryEnvironmentPlanetaryAxis,
    OctanePlanetaryEnvironmentPlanetaryAngle,
    OctanePlanetaryEnvironmentGroupPlanetarySurface,
    OctanePlanetaryEnvironmentGroupVisibleEnvironment,
    OctanePlanetaryEnvironment,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
