##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTextureEnvironmentTexture(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Environment texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentPower(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentPower"
    bl_label="Power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentImportanceSampling(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentImportanceSampling"
    bl_label="Importance sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMPORTANCE_SAMPLING
    octane_pin_name="importance_sampling"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Use importance sampling for image textures")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentCastPhotons(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentCastPhotons"
    bl_label="Cast photons"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_CAST_PHOTONS
    octane_pin_name="castPhotons"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If photon mapping is used, cast photons from bright sources in the environment map")
    octane_hide_value=False
    octane_min_version=12000200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentMedium(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentMediumRadius(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentMediumRadius"
    bl_label="Medium radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_MEDIUM_RADIUS
    octane_pin_name="mediumRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius", min=0.000100, max=10000000000.000000, soft_min=0.000100, soft_max=10000000000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentLightPassMask(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentLightPassMask"
    bl_label="Medium light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type=consts.NodeType.NT_BIT_MASK
    octane_default_node_name="OctaneBitValue"
    octane_pin_id=consts.PinID.P_LIGHT_PASS_MASK
    octane_pin_name="lightPassMask"
    octane_pin_type=consts.PinType.PT_BIT_MASK
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentVisibleEnvironmentBackplate(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentVisibleEnvironmentBackplate"
    bl_label="Backplate"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_BACKPLATE
    octane_pin_name="visibleEnvironmentBackplate"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will behave as a backplate image")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentVisibleEnvironmentReflections(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentVisibleEnvironmentReflections"
    bl_label="Reflections"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFLECTIONS
    octane_pin_name="visibleEnvironmentReflections"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentVisibleEnvironmentRefractions(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentVisibleEnvironmentRefractions"
    bl_label="Refractions"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_VISIBLE_ENVIRONMENT_REFRACTIONS
    octane_pin_name="visibleEnvironmentRefractions"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When used as a visible environment, this environment will be visible in refractions")
    octane_hide_value=False
    octane_min_version=3030003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTextureEnvironmentRotation(OctaneBaseSocket):
    bl_idname="OctaneTextureEnvironmentRotation"
    bl_label="[Deprecated]Rotation"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ROTATION
    octane_pin_name="rotation"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="(deprecated) Rotation", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=1210000
    octane_deprecated=True

class OctaneTextureEnvironmentGroupVisibleEnvironment(OctaneGroupTitleSocket):
    bl_idname="OctaneTextureEnvironmentGroupVisibleEnvironment"
    bl_label="[OctaneGroupTitle]Visible environment"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Backplate;Reflections;Refractions;")

class OctaneTextureEnvironment(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTextureEnvironment"
    bl_label="Texture environment"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTextureEnvironmentTexture,OctaneTextureEnvironmentPower,OctaneTextureEnvironmentImportanceSampling,OctaneTextureEnvironmentCastPhotons,OctaneTextureEnvironmentMedium,OctaneTextureEnvironmentMediumRadius,OctaneTextureEnvironmentLightPassMask,OctaneTextureEnvironmentGroupVisibleEnvironment,OctaneTextureEnvironmentVisibleEnvironmentBackplate,OctaneTextureEnvironmentVisibleEnvironmentReflections,OctaneTextureEnvironmentVisibleEnvironmentRefractions,OctaneTextureEnvironmentRotation,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_ENV_TEXTURE
    octane_socket_list=["Texture", "Power", "Importance sampling", "Cast photons", "Medium", "Medium radius", "Medium light pass mask", "Backplate", "Reflections", "Refractions", "[Deprecated]Rotation", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=10

    def init(self, context):
        self.inputs.new("OctaneTextureEnvironmentTexture", OctaneTextureEnvironmentTexture.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentPower", OctaneTextureEnvironmentPower.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentImportanceSampling", OctaneTextureEnvironmentImportanceSampling.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentCastPhotons", OctaneTextureEnvironmentCastPhotons.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentMedium", OctaneTextureEnvironmentMedium.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentMediumRadius", OctaneTextureEnvironmentMediumRadius.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentLightPassMask", OctaneTextureEnvironmentLightPassMask.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentGroupVisibleEnvironment", OctaneTextureEnvironmentGroupVisibleEnvironment.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentBackplate", OctaneTextureEnvironmentVisibleEnvironmentBackplate.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentReflections", OctaneTextureEnvironmentVisibleEnvironmentReflections.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentVisibleEnvironmentRefractions", OctaneTextureEnvironmentVisibleEnvironmentRefractions.bl_label).init()
        self.inputs.new("OctaneTextureEnvironmentRotation", OctaneTextureEnvironmentRotation.bl_label).init()
        self.outputs.new("OctaneEnvironmentOutSocket", "Environment out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneTextureEnvironmentTexture,
    OctaneTextureEnvironmentPower,
    OctaneTextureEnvironmentImportanceSampling,
    OctaneTextureEnvironmentCastPhotons,
    OctaneTextureEnvironmentMedium,
    OctaneTextureEnvironmentMediumRadius,
    OctaneTextureEnvironmentLightPassMask,
    OctaneTextureEnvironmentVisibleEnvironmentBackplate,
    OctaneTextureEnvironmentVisibleEnvironmentReflections,
    OctaneTextureEnvironmentVisibleEnvironmentRefractions,
    OctaneTextureEnvironmentRotation,
    OctaneTextureEnvironmentGroupVisibleEnvironment,
    OctaneTextureEnvironment,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneTextureEnvironmentLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"