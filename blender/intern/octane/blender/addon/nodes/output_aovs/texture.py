# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneOutputAOVsTextureEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureRgbTexture(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureRgbTexture"
    bl_label = "RGB texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_RGB_TEXTURE
    octane_pin_name = "rgbTexture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureRgbSampleCount(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureRgbSampleCount"
    bl_label = "RGB sample count"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_RGB_SAMPLE_COUNT
    octane_pin_name = "rgbSampleCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="The number of times to sample the RGB texture for each pixel", min=1, max=10000, soft_min=1, soft_max=100, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureAlphaTexture(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureAlphaTexture"
    bl_label = "Alpha texture"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name = "OctaneGreyscaleColor"
    octane_pin_id = consts.PinID.P_ALPHA_TEXTURE
    octane_pin_name = "alphaTexture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The opacity channel to use in conjunction with the texture to blend", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureAlphaSampleCount(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureAlphaSampleCount"
    bl_label = "Alpha sample count"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_ALPHA_SAMPLE_COUNT
    octane_pin_name = "alphaSampleCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="The number of times to sample the alpha texture for each pixel", min=1, max=10000, soft_min=1, soft_max=100, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureUvTransform(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureUvTransform"
    bl_label = "UV transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_UV_TRANSFORM
    octane_pin_name = "uvTransform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTextureBlendingSettings(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsTextureBlendingSettings"
    bl_label = "Blending settings"
    color = consts.OctanePinColor.BlendingSettings
    octane_default_node_type = consts.NodeType.NT_BLENDING_SETTINGS
    octane_default_node_name = "OctaneBlendingSettings"
    octane_pin_id = consts.PinID.P_BLENDING_SETTINGS
    octane_pin_name = "blendingSettings"
    octane_pin_type = consts.PinType.PT_BLENDING_SETTINGS
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsTexture"
    bl_label = "Texture"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsTextureEnabled, OctaneOutputAOVsTextureRgbTexture, OctaneOutputAOVsTextureRgbSampleCount, OctaneOutputAOVsTextureAlphaTexture, OctaneOutputAOVsTextureAlphaSampleCount, OctaneOutputAOVsTextureUvTransform, OctaneOutputAOVsTextureBlendingSettings, ]
    octane_min_version = 14000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_BLEND_TEXTURE
    octane_socket_list = ["Enabled", "RGB texture", "RGB sample count", "Alpha texture", "Alpha sample count", "UV transform", "Blending settings", ]
    octane_attribute_list = ["a_parameter_count", ]
    octane_attribute_config = {"a_parameter_count": [consts.AttributeID.A_PARAMETER_COUNT, "parameterCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 7

    a_parameter_count: IntProperty(name="Parameter count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of parameters. Changing this value and evaluating the node will update the number of parameter pins. New pins will be added to the end of the dynamic pin list")

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsTextureEnabled", OctaneOutputAOVsTextureEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureRgbTexture", OctaneOutputAOVsTextureRgbTexture.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureRgbSampleCount", OctaneOutputAOVsTextureRgbSampleCount.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureAlphaTexture", OctaneOutputAOVsTextureAlphaTexture.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureAlphaSampleCount", OctaneOutputAOVsTextureAlphaSampleCount.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureUvTransform", OctaneOutputAOVsTextureUvTransform.bl_label).init()
        self.inputs.new("OctaneOutputAOVsTextureBlendingSettings", OctaneOutputAOVsTextureBlendingSettings.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsTextureEnabled,
    OctaneOutputAOVsTextureRgbTexture,
    OctaneOutputAOVsTextureRgbSampleCount,
    OctaneOutputAOVsTextureAlphaTexture,
    OctaneOutputAOVsTextureAlphaSampleCount,
    OctaneOutputAOVsTextureUvTransform,
    OctaneOutputAOVsTextureBlendingSettings,
    OctaneOutputAOVsTexture,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
