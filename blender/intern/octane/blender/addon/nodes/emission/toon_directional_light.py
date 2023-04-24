##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneToonDirectionalLightEfficiencyOrTexture(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightEfficiencyOrTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=237)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="The emission texture (on the emitting surface)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightSundir(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightSundir"
    bl_label="Light direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneSunDirection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=231)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 0.800000, 0.000000), update=None, description="Vector which defines the direction from which the light is pointing to", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightPower(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Multiplier for light source's brightness", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.010000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightLightPassId(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightLightPassId"
    bl_label="Light pass ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=97)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="ID of the light pass that captures the contribution of this emitter", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3080005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightCastShadows(OctaneBaseSocket):
    bl_idname="OctaneToonDirectionalLightCastShadows"
    bl_label="Cast shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=361)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled (which is the default), direct light shadows are calculated for this light source")
    octane_hide_value=False
    octane_min_version=4000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneToonDirectionalLightGroupVisibility(OctaneGroupTitleSocket):
    bl_idname="OctaneToonDirectionalLightGroupVisibility"
    bl_label="[OctaneGroupTitle]Visibility"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Cast shadows;")

class OctaneToonDirectionalLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneToonDirectionalLight"
    bl_label="Toon directional light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=124)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Light direction;Power;Light pass ID;Cast shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneToonDirectionalLightEfficiencyOrTexture", OctaneToonDirectionalLightEfficiencyOrTexture.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightSundir", OctaneToonDirectionalLightSundir.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightPower", OctaneToonDirectionalLightPower.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightLightPassId", OctaneToonDirectionalLightLightPassId.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightGroupVisibility", OctaneToonDirectionalLightGroupVisibility.bl_label).init()
        self.inputs.new("OctaneToonDirectionalLightCastShadows", OctaneToonDirectionalLightCastShadows.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
    OctaneToonDirectionalLightEfficiencyOrTexture,
    OctaneToonDirectionalLightSundir,
    OctaneToonDirectionalLightPower,
    OctaneToonDirectionalLightLightPassId,
    OctaneToonDirectionalLightCastShadows,
    OctaneToonDirectionalLightGroupVisibility,
    OctaneToonDirectionalLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
