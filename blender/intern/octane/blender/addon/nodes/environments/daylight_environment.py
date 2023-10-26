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


class OctaneDaylightEnvironmentSundir(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSundir"
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
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentTurbidity"
    bl_label="Sky turbidity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TURBIDITY
    octane_pin_name="turbidity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.400000, update=OctaneBaseSocket.update_node_tree, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentPower(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentPower"
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
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunIntensity"
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

class OctaneDaylightEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentNorthoffset"
    bl_label="North offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NORTHOFFSET
    octane_pin_name="northoffset"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentModel(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentModel"
    bl_label="Daylight model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_MODEL
    octane_pin_name="model"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Preetham Daylight Model", "Preetham Daylight Model", "", 0),
        ("Octane Daylight Model", "Octane Daylight Model", "", 1),
        ("Nishita Daylight Model", "Nishita Daylight Model", "", 2),
        ("Hosek-Wilkie Daylight Model", "Hosek-Wilkie Daylight Model", "", 3),
    ]
    default_value: EnumProperty(default="Octane Daylight Model", update=OctaneBaseSocket.update_node_tree, description="The daylight model to use", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSkyColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSkyColor"
    bl_label="Sky color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SKY_COLOR
    octane_pin_name="sky_color"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.050000, 0.300000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Base color of the sky, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunsetColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunsetColor"
    bl_label="Sunset color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_SUNSET_COLOR
    octane_pin_name="sunset_color"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.600000, 0.120000, 0.020000), update=OctaneBaseSocket.update_node_tree, description="Color of the sky and sun at sunset, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunSize(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunSize"
    bl_label="Sun size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SUN_SIZE
    octane_pin_name="sun_size"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degrees)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundColor"
    bl_label="Ground color"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GROUND_COLOR
    octane_pin_name="groundColor"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Base color of the ground, which applies only to the Octane, Nishita and Hosek-Wilkie daylight models", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundStartAngle(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundStartAngle"
    bl_label="Ground start angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GROUND_START_ANGLE
    octane_pin_name="groundStartAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=90.000000, update=OctaneBaseSocket.update_node_tree, description="The angle (in degrees) below the horizon where the transition to the ground color starts. This applies only to the Octane daylight model", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundBlendAngle(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundBlendAngle"
    bl_label="Ground blend angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GROUND_BLEND_ANGLE
    octane_pin_name="groundBlendAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The angle (in degrees) over which the sky color transitions to the ground color. This applies only to the Octane daylight model", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1, precision=2, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentTexture(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentTexture"
    bl_label="Sky texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentImportanceSampling"
    bl_label="Importance sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMPORTANCE_SAMPLING
    octane_pin_name="importance_sampling"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Use importance sampling for image textures")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentCastPhotons(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentCastPhotons"
    bl_label="Cast photons"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CAST_PHOTONS
    octane_pin_name="castPhotons"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If photon mapping is used, cast photons from bright sources in the environment map")
    octane_hide_value=False
    octane_min_version=12000200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentMedium(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MEDIUM_RADIUS
    octane_pin_name="mediumRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentLightPassMask"
    bl_label="Medium light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type=consts.NodeType.NT_BIT_MASK
    octane_default_node_name="OctaneBitValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_MASK
    octane_pin_name="lightPassMask"
    octane_pin_type=consts.PinType.PT_BIT_MASK
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentUseInPostVolume(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentUseInPostVolume"
    bl_label="Use in post volume"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_USE_IN_POST_VOLUME
    octane_pin_name="useInPostVolume"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable or disable this daylight environment in post volume rendering")
    octane_hide_value=False
    octane_min_version=13000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentBackplate"
    bl_label="Backplate"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_BACKPLATE
    octane_pin_name="visibleEnvironmentBackplate"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will behave as a backplate image")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentReflections"
    bl_label="Reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFLECTIONS
    octane_pin_name="visibleEnvironmentReflections"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentRefractions"
    bl_label="Refractions"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFRACTIONS
    octane_pin_name="visibleEnvironmentRefractions"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in refractions")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroupVisibleEnvironment(OctaneGroupTitleSocket):
    bl_idname="OctaneDaylightEnvironmentGroupVisibleEnvironment"
    bl_label="[OctaneGroupTitle]Visible environment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Backplate;Reflections;Refractions;")

class OctaneDaylightEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDaylightEnvironment"
    bl_label="Daylight environment"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDaylightEnvironmentSundir,OctaneDaylightEnvironmentTurbidity,OctaneDaylightEnvironmentPower,OctaneDaylightEnvironmentSunIntensity,OctaneDaylightEnvironmentNorthoffset,OctaneDaylightEnvironmentModel,OctaneDaylightEnvironmentSkyColor,OctaneDaylightEnvironmentSunsetColor,OctaneDaylightEnvironmentSunSize,OctaneDaylightEnvironmentGroundColor,OctaneDaylightEnvironmentGroundStartAngle,OctaneDaylightEnvironmentGroundBlendAngle,OctaneDaylightEnvironmentTexture,OctaneDaylightEnvironmentImportanceSampling,OctaneDaylightEnvironmentCastPhotons,OctaneDaylightEnvironmentMedium,OctaneDaylightEnvironmentMediumRadius,OctaneDaylightEnvironmentLightPassMask,OctaneDaylightEnvironmentUseInPostVolume,OctaneDaylightEnvironmentGroupVisibleEnvironment,OctaneDaylightEnvironmentVisibleEnvironmentBackplate,OctaneDaylightEnvironmentVisibleEnvironmentReflections,OctaneDaylightEnvironmentVisibleEnvironmentRefractions,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_ENV_DAYLIGHT
    octane_socket_list=["Sun direction", "Sky turbidity", "Power", "Sun intensity", "North offset", "Daylight model", "Sky color", "Sunset color", "Sun size", "Ground color", "Ground start angle", "Ground blend angle", "Sky texture", "Importance sampling", "Cast photons", "Medium", "Medium radius", "Medium light pass mask", "Use in post volume", "Backplate", "Reflections", "Refractions", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=22

    compatibility_mode_infos=[
        ("Latest (2022.1)", "Latest (2022.1)", """(null)""", 12000005),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """The Octane daylight model produces absolute spectral colors, not relative to the white light spectrum set in the kernel.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2022.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000009, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneDaylightEnvironmentSundir", OctaneDaylightEnvironmentSundir.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentTurbidity", OctaneDaylightEnvironmentTurbidity.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentPower", OctaneDaylightEnvironmentPower.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentSunIntensity", OctaneDaylightEnvironmentSunIntensity.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentNorthoffset", OctaneDaylightEnvironmentNorthoffset.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentModel", OctaneDaylightEnvironmentModel.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentSkyColor", OctaneDaylightEnvironmentSkyColor.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentSunsetColor", OctaneDaylightEnvironmentSunsetColor.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentSunSize", OctaneDaylightEnvironmentSunSize.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentGroundColor", OctaneDaylightEnvironmentGroundColor.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentGroundStartAngle", OctaneDaylightEnvironmentGroundStartAngle.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentGroundBlendAngle", OctaneDaylightEnvironmentGroundBlendAngle.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentTexture", OctaneDaylightEnvironmentTexture.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentImportanceSampling", OctaneDaylightEnvironmentImportanceSampling.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentCastPhotons", OctaneDaylightEnvironmentCastPhotons.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentMedium", OctaneDaylightEnvironmentMedium.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentMediumRadius", OctaneDaylightEnvironmentMediumRadius.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentLightPassMask", OctaneDaylightEnvironmentLightPassMask.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentUseInPostVolume", OctaneDaylightEnvironmentUseInPostVolume.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentGroupVisibleEnvironment", OctaneDaylightEnvironmentGroupVisibleEnvironment.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentBackplate", OctaneDaylightEnvironmentVisibleEnvironmentBackplate.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentReflections", OctaneDaylightEnvironmentVisibleEnvironmentReflections.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentRefractions", OctaneDaylightEnvironmentVisibleEnvironmentRefractions.bl_label).init()
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneDaylightEnvironmentSundir,
    OctaneDaylightEnvironmentTurbidity,
    OctaneDaylightEnvironmentPower,
    OctaneDaylightEnvironmentSunIntensity,
    OctaneDaylightEnvironmentNorthoffset,
    OctaneDaylightEnvironmentModel,
    OctaneDaylightEnvironmentSkyColor,
    OctaneDaylightEnvironmentSunsetColor,
    OctaneDaylightEnvironmentSunSize,
    OctaneDaylightEnvironmentGroundColor,
    OctaneDaylightEnvironmentGroundStartAngle,
    OctaneDaylightEnvironmentGroundBlendAngle,
    OctaneDaylightEnvironmentTexture,
    OctaneDaylightEnvironmentImportanceSampling,
    OctaneDaylightEnvironmentCastPhotons,
    OctaneDaylightEnvironmentMedium,
    OctaneDaylightEnvironmentMediumRadius,
    OctaneDaylightEnvironmentLightPassMask,
    OctaneDaylightEnvironmentUseInPostVolume,
    OctaneDaylightEnvironmentVisibleEnvironmentBackplate,
    OctaneDaylightEnvironmentVisibleEnvironmentReflections,
    OctaneDaylightEnvironmentVisibleEnvironmentRefractions,
    OctaneDaylightEnvironmentGroupVisibleEnvironment,
    OctaneDaylightEnvironment,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneDaylightEnvironmentLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"