##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDaylightEnvironmentSundir(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSundir"
    bl_label="Sun direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneSunDirection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), update=None, description="Vector which defines the direction from which the sun is shining", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentTurbidity(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentTurbidity"
    bl_label="Sky turbidity"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=246)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.400000, update=None, description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light", min=2.000000, max=15.000000, soft_min=2.000000, soft_max=15.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentPower(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Scale factor that is applied to the sun and sky", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunIntensity(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunIntensity"
    bl_label="Sun intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=514)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Scale factor that is applied to the sun only. Use this to adjust the relative power of the sun compared to the sky.\n\nNote: values other than 1.0 can produce unrealistic results because in the real world the sky is lit by the sun. Adjusting the balance between the yellowish sun and the bluish sky can also produce a hue shift in the scene", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=8000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentNorthoffset(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentNorthoffset"
    bl_label="North offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=120)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Additional rotation offset on longitude", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentModel(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentModel"
    bl_label="Daylight model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=114)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Preetham Daylight Model", "Preetham Daylight Model", "", 0),
        ("Octane Daylight Model", "Octane Daylight Model", "", 1),
        ("Nishita Daylight Model", "Nishita Daylight Model", "", 2),
        ("Hosek-Wilkie Daylight Model", "Hosek-Wilkie Daylight Model", "", 3),
    ]
    default_value: EnumProperty(default="Octane Daylight Model", update=None, description="The daylight model to use", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSkyColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSkyColor"
    bl_label="Sky color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=217)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.050000, 0.300000, 1.000000), update=None, description="Base color of the sky, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunsetColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunsetColor"
    bl_label="Sunset color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=232)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.600000, 0.120000, 0.020000), update=None, description="Color of the sky and sun at sunset, which applies only to the Octane daylight model", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentSunSize(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentSunSize"
    bl_label="Sun size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=233)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Size of the sun given as a factor of the actual sun diameter (which is ~0.5 degrees)", min=0.100000, max=30.000000, soft_min=0.100000, soft_max=30.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundColor(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundColor"
    bl_label="Ground color"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=331)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.031928, 0.130434, 0.557292), update=None, description="Base color of the ground, which applies only to the Octane, Nishita and Hosek-Wilkie daylight models", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=3, size=3)
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundStartAngle(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundStartAngle"
    bl_label="Ground start angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=332)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=90.000000, update=None, description="The angle (in degrees) below the horizon where the transition to the ground color starts. This applies only to the Octane daylight model", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentGroundBlendAngle(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentGroundBlendAngle"
    bl_label="Ground blend angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=330)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=5.000000, update=None, description="The angle (in degrees) over which the sky color transitions to the ground color. This applies only to the Octane daylight model", min=1.000000, max=90.000000, soft_min=1.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentTexture(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentTexture"
    bl_label="Sky texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentImportanceSampling"
    bl_label="Importance sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=79)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Use importance sampling for image textures")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentMedium(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=269)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentLightPassMask"
    bl_label="Medium light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentBackplate"
    bl_label="Backplate"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=317)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will behave as a backplate image")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentReflections"
    bl_label="Reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=318)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDaylightEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname="OctaneDaylightEnvironmentVisibleEnvironmentRefractions"
    bl_label="Refractions"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=319)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When used as a visible environment, this environment will be visible in refractions")
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
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=14)
    octane_socket_list: StringProperty(name="Socket List", default="Sun direction;Sky turbidity;Power;Sun intensity;North offset;Daylight model;Sky color;Sunset color;Sun size;Ground color;Ground start angle;Ground blend angle;Sky texture;Importance sampling;Medium;Medium radius;Medium light pass mask;Backplate;Reflections;Refractions;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=20)

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
        self.inputs.new("OctaneDaylightEnvironmentMedium", OctaneDaylightEnvironmentMedium.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentMediumRadius", OctaneDaylightEnvironmentMediumRadius.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentLightPassMask", OctaneDaylightEnvironmentLightPassMask.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentGroupVisibleEnvironment", OctaneDaylightEnvironmentGroupVisibleEnvironment.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentBackplate", OctaneDaylightEnvironmentVisibleEnvironmentBackplate.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentReflections", OctaneDaylightEnvironmentVisibleEnvironmentReflections.bl_label).init()
        self.inputs.new("OctaneDaylightEnvironmentVisibleEnvironmentRefractions", OctaneDaylightEnvironmentVisibleEnvironmentRefractions.bl_label).init()
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out").init()


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
    OctaneDaylightEnvironmentMedium,
    OctaneDaylightEnvironmentMediumRadius,
    OctaneDaylightEnvironmentLightPassMask,
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
