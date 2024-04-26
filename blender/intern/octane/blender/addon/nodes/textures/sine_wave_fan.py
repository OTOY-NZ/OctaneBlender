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


class OctaneSineWaveFanIntensity(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanIntensity"
    bl_label = "Intensity"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_INTENSITY
    octane_pin_name = "intensity"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The intensity of the effect", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanAmplitude(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanAmplitude"
    bl_label = "Rayon"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AMPLITUDE
    octane_pin_name = "amplitude"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The amplitude of the sine waves", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanFrequency(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanFrequency"
    bl_label = "Rotation"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FREQUENCY
    octane_pin_name = "frequency"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The frequency of the sine waves", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanTime(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanTime"
    bl_label = "Movement"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TIME
    octane_pin_name = "time"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Adjust to animate the effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanStripeCount(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanStripeCount"
    bl_label = "Stripes"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_STRIPE_COUNT
    octane_pin_name = "stripeCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=35, update=OctaneBaseSocket.update_node_tree, description="The number of stripes", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanTexture(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanTexture"
    bl_label = "Color"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_TEX_RGB
    octane_default_node_name = "OctaneRGBColor"
    octane_pin_id = consts.PinID.P_TEXTURE
    octane_pin_name = "texture"
    octane_pin_type = consts.PinType.PT_TEXTURE
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the stripes", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanTransform(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanTransform"
    bl_label = "UV transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFanProjection(OctaneBaseSocket):
    bl_idname = "OctaneSineWaveFanProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_UVW
    octane_default_node_name = "OctaneMeshUVProjection"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSineWaveFan(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSineWaveFan"
    bl_label = "Sine wave fan"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSineWaveFanIntensity, OctaneSineWaveFanAmplitude, OctaneSineWaveFanFrequency, OctaneSineWaveFanTime, OctaneSineWaveFanStripeCount, OctaneSineWaveFanTexture, OctaneSineWaveFanTransform, OctaneSineWaveFanProjection, ]
    octane_min_version = 12000003
    octane_node_type = consts.NodeType.NT_TEX_SINE_WAVE_FAN
    octane_socket_list = ["Intensity", "Rayon", "Rotation", "Movement", "Stripes", "Color", "UV transform", "Projection", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 8

    def init(self, context):  # noqa
        self.inputs.new("OctaneSineWaveFanIntensity", OctaneSineWaveFanIntensity.bl_label).init()
        self.inputs.new("OctaneSineWaveFanAmplitude", OctaneSineWaveFanAmplitude.bl_label).init()
        self.inputs.new("OctaneSineWaveFanFrequency", OctaneSineWaveFanFrequency.bl_label).init()
        self.inputs.new("OctaneSineWaveFanTime", OctaneSineWaveFanTime.bl_label).init()
        self.inputs.new("OctaneSineWaveFanStripeCount", OctaneSineWaveFanStripeCount.bl_label).init()
        self.inputs.new("OctaneSineWaveFanTexture", OctaneSineWaveFanTexture.bl_label).init()
        self.inputs.new("OctaneSineWaveFanTransform", OctaneSineWaveFanTransform.bl_label).init()
        self.inputs.new("OctaneSineWaveFanProjection", OctaneSineWaveFanProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSineWaveFanIntensity,
    OctaneSineWaveFanAmplitude,
    OctaneSineWaveFanFrequency,
    OctaneSineWaveFanTime,
    OctaneSineWaveFanStripeCount,
    OctaneSineWaveFanTexture,
    OctaneSineWaveFanTransform,
    OctaneSineWaveFanProjection,
    OctaneSineWaveFan,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
