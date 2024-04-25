# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneAbsorptionScale(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionScale"
    bl_label = "Density"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SCALE
    octane_pin_name = "scale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Absorption scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1.000000, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionRayMarchStepLength"
    bl_label = "Volume step length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RAYMARCH_STEP_LENGTH
    octane_pin_name = "rayMarchStepLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3030001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionShadowRayMarchStepLength"
    bl_label = "Vol. shadow ray step length"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SHADOW_RAY_MARCH_STEP_LENGTH
    octane_pin_name = "shadowRayMarchStepLength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 7000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionUseRayStepLengthForShadowRays"
    bl_label = "Use Vol. step length for Vol. shadow ray step length"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_RAY_STEP_LENGTH_FOR_SHADOW_RAYS
    octane_pin_name = "useRayStepLengthForShadowRays"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value = False
    octane_min_version = 8000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionDisplacement"
    bl_label = "Sample position displacement"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_DISPLACEMENT
    octane_pin_name = "displacement"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 7000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionAbsorption"
    bl_label = "Absorption"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_ABSORPTION
    octane_pin_name = "absorption"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Absorption cross section. Determines how quickly light is absorbed while traveling through this medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionInvertAbsorption(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionInvertAbsorption"
    bl_label = "Invert absorption"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_INVERT_ABSORPTION
    octane_pin_name = "invertAbsorption"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")
    octane_hide_value = False
    octane_min_version = 3000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneAbsorptionLockStepLength(OctaneBaseSocket):
    bl_idname = "OctaneAbsorptionLockStepLength"
    bl_label = "[Deprecated]Lock step length pins"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_LOCK_STEP_LENGTH
    octane_pin_name = "lockStepLength"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value = False
    octane_min_version = 7000000
    octane_end_version = 8000005
    octane_deprecated = True


class OctaneAbsorptionGroupAbsorption(OctaneGroupTitleSocket):
    bl_idname = "OctaneAbsorptionGroupAbsorption"
    bl_label = "[OctaneGroupTitle]Absorption"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Absorption;Invert absorption;")


class OctaneAbsorption(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneAbsorption"
    bl_label = "Absorption"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneAbsorptionScale, OctaneAbsorptionRayMarchStepLength, OctaneAbsorptionShadowRayMarchStepLength, OctaneAbsorptionUseRayStepLengthForShadowRays, OctaneAbsorptionDisplacement, OctaneAbsorptionGroupAbsorption, OctaneAbsorptionAbsorption, OctaneAbsorptionInvertAbsorption, OctaneAbsorptionLockStepLength, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MED_ABSORPTION
    octane_socket_list = ["Density", "Volume step length", "Vol. shadow ray step length", "Use Vol. step length for Vol. shadow ray step length", "Sample position displacement", "Absorption", "Invert absorption", "[Deprecated]Lock step length pins", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 7

    def init(self, context):  # noqa
        self.inputs.new("OctaneAbsorptionScale", OctaneAbsorptionScale.bl_label).init()
        self.inputs.new("OctaneAbsorptionRayMarchStepLength", OctaneAbsorptionRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneAbsorptionShadowRayMarchStepLength", OctaneAbsorptionShadowRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneAbsorptionUseRayStepLengthForShadowRays", OctaneAbsorptionUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneAbsorptionDisplacement", OctaneAbsorptionDisplacement.bl_label).init()
        self.inputs.new("OctaneAbsorptionGroupAbsorption", OctaneAbsorptionGroupAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionAbsorption", OctaneAbsorptionAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionInvertAbsorption", OctaneAbsorptionInvertAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionLockStepLength", OctaneAbsorptionLockStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneAbsorptionScale,
    OctaneAbsorptionRayMarchStepLength,
    OctaneAbsorptionShadowRayMarchStepLength,
    OctaneAbsorptionUseRayStepLengthForShadowRays,
    OctaneAbsorptionDisplacement,
    OctaneAbsorptionAbsorption,
    OctaneAbsorptionInvertAbsorption,
    OctaneAbsorptionLockStepLength,
    OctaneAbsorptionGroupAbsorption,
    OctaneAbsorption,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
