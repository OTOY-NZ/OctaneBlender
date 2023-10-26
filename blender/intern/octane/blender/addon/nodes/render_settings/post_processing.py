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


class OctanePostProcessingOnOff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingOnOff"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ON_OFF
    octane_pin_name="on_off"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables post processing")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingCutoff(OctaneBaseSocket):
    bl_idname="OctanePostProcessingCutoff"
    bl_label="Cutoff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CUTOFF
    octane_pin_name="cutoff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The minimum brightness of a pixel to have bloom and glare applied. The brightness is measured after the application of the exposure.\n\nIncreasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5100001
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingBloomPower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingBloomPower"
    bl_label="Bloom power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BLOOM_POWER
    octane_pin_name="bloom_power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Bloom power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlarePower(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlarePower"
    bl_label="Glare power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_POWER
    octane_pin_name="glare_power"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Glare power", min=0.000000, max=100000.000000, soft_min=0.000000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareRayAmount(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareRayAmount"
    bl_label="Glare ray count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_GLARE_RAY_AMOUNT
    octane_pin_name="glare_ray_amount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=3, update=OctaneBaseSocket.update_node_tree, description="Glare ray count", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareAngle(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareAngle"
    bl_label="Glare rotation angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_ANGLE
    octane_pin_name="glare_angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=15.000000, update=OctaneBaseSocket.update_node_tree, description="Glare rotation angle", min=-90.000000, max=90.000000, soft_min=-90.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGlareBlur(OctaneBaseSocket):
    bl_idname="OctanePostProcessingGlareBlur"
    bl_label="Glare blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GLARE_BLUR
    octane_pin_name="glare_blur"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="Glare blur", min=0.001000, max=0.200000, soft_min=0.001000, soft_max=0.200000, step=1, precision=3, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpreadStart(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpreadStart"
    bl_label="Spread start"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD_START
    octane_pin_name="spreadStart"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The minimum blur radius for bloom/glare, as a proportion of image width or height (whichever is larger).\n\nIdeally this should be set to correspond to about half a pixel (i.e. 0.5 / max(width, height) * 100%) at the maximum resolution you will be using. Too large a value will produce an overly blurry result without fine details. Too small a value will reduce the maximum possible strength of the bloom/glare", min=0.000500, max=1.000000, soft_min=0.005000, soft_max=0.100000, step=1, precision=3, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpreadEnd(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpreadEnd"
    bl_label="Spread end"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPREAD_END
    octane_pin_name="spreadEnd"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum blur radius for bloom/glare, as a proportion of image width or height (whichever is larger)", min=0.100000, max=200.000000, soft_min=0.100000, soft_max=100.000000, step=1, precision=3, subtype="PERCENTAGE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralIntensity(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralIntensity"
    bl_label="Spectral intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPECTRAL_INTENSITY
    octane_pin_name="spectral_intensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Spectral intensity", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingSpectralShift(OctaneBaseSocket):
    bl_idname="OctanePostProcessingSpectralShift"
    bl_label="Spectral shift"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPECTRAL_SHIFT
    octane_pin_name="spectral_shift"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.000000, update=OctaneBaseSocket.update_node_tree, description="Spectral shift", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=6.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingChromaticAbrIntensity(OctaneBaseSocket):
    bl_idname="OctanePostProcessingChromaticAbrIntensity"
    bl_label="Chromatic aberration intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CHROMATIC_ABERRATION_INTENSITY
    octane_pin_name="chromaticAberrationIntensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Chromatic aberration intensity", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingLensFlare(OctaneBaseSocket):
    bl_idname="OctanePostProcessingLensFlare"
    bl_label="Lens flare intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LENS_FLARE
    octane_pin_name="lensFlare"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Lens flare intensity", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingLensFlareExtent(OctaneBaseSocket):
    bl_idname="OctanePostProcessingLensFlareExtent"
    bl_label="Lens flare extent"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_LENS_FLARE_EXTENT
    octane_pin_name="lensFlareExtent"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2.000000, update=OctaneBaseSocket.update_node_tree, description="Lens flare extent. This controls the overall length and distances between lens flare highlights", min=0.000000, max=10.000000, soft_min=0.000000, soft_max=10.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingPostVolume(OctaneBaseSocket):
    bl_idname="OctanePostProcessingPostVolume"
    bl_label="Post volume"
    color=consts.OctanePinColor.PostVolume
    octane_default_node_type=consts.NodeType.NT_POST_VOLUME
    octane_default_node_name="OctanePostVolumeEffects"
    octane_pin_id=consts.PinID.P_POST_VOLUME
    octane_pin_name="postVolume"
    octane_pin_type=consts.PinType.PT_POST_VOLUME
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePostProcessingGroupPostImageProcessing(OctaneGroupTitleSocket):
    bl_idname="OctanePostProcessingGroupPostImageProcessing"
    bl_label="[OctaneGroupTitle]Post image processing"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enabled;Cutoff;Bloom power;Glare power;Glare ray count;Glare rotation angle;Glare blur;Spread start;Spread end;Spectral intensity;Spectral shift;")

class OctanePostProcessingGroupPostProcessingLensEffects(OctaneGroupTitleSocket):
    bl_idname="OctanePostProcessingGroupPostProcessingLensEffects"
    bl_label="[OctaneGroupTitle]Post processing lens effects"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Chromatic aberration intensity;Lens flare intensity;Lens flare extent;")

class OctanePostProcessingGroupPostProcessingVolumeEffects(OctaneGroupTitleSocket):
    bl_idname="OctanePostProcessingGroupPostProcessingVolumeEffects"
    bl_label="[OctaneGroupTitle]Post processing volume effects"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Post volume;")

class OctanePostProcessing(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePostProcessing"
    bl_label="Post processing"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctanePostProcessingGroupPostImageProcessing,OctanePostProcessingOnOff,OctanePostProcessingCutoff,OctanePostProcessingBloomPower,OctanePostProcessingGlarePower,OctanePostProcessingGlareRayAmount,OctanePostProcessingGlareAngle,OctanePostProcessingGlareBlur,OctanePostProcessingSpreadStart,OctanePostProcessingSpreadEnd,OctanePostProcessingSpectralIntensity,OctanePostProcessingSpectralShift,OctanePostProcessingGroupPostProcessingLensEffects,OctanePostProcessingChromaticAbrIntensity,OctanePostProcessingLensFlare,OctanePostProcessingLensFlareExtent,OctanePostProcessingGroupPostProcessingVolumeEffects,OctanePostProcessingPostVolume,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_POSTPROCESSING
    octane_socket_list=["Enabled", "Cutoff", "Bloom power", "Glare power", "Glare ray count", "Glare rotation angle", "Glare blur", "Spread start", "Spread end", "Spectral intensity", "Spectral shift", "Chromatic aberration intensity", "Lens flare intensity", "Lens flare extent", "Post volume", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=15

    def init(self, context):
        self.inputs.new("OctanePostProcessingGroupPostImageProcessing", OctanePostProcessingGroupPostImageProcessing.bl_label).init()
        self.inputs.new("OctanePostProcessingOnOff", OctanePostProcessingOnOff.bl_label).init()
        self.inputs.new("OctanePostProcessingCutoff", OctanePostProcessingCutoff.bl_label).init()
        self.inputs.new("OctanePostProcessingBloomPower", OctanePostProcessingBloomPower.bl_label).init()
        self.inputs.new("OctanePostProcessingGlarePower", OctanePostProcessingGlarePower.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareRayAmount", OctanePostProcessingGlareRayAmount.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareAngle", OctanePostProcessingGlareAngle.bl_label).init()
        self.inputs.new("OctanePostProcessingGlareBlur", OctanePostProcessingGlareBlur.bl_label).init()
        self.inputs.new("OctanePostProcessingSpreadStart", OctanePostProcessingSpreadStart.bl_label).init()
        self.inputs.new("OctanePostProcessingSpreadEnd", OctanePostProcessingSpreadEnd.bl_label).init()
        self.inputs.new("OctanePostProcessingSpectralIntensity", OctanePostProcessingSpectralIntensity.bl_label).init()
        self.inputs.new("OctanePostProcessingSpectralShift", OctanePostProcessingSpectralShift.bl_label).init()
        self.inputs.new("OctanePostProcessingGroupPostProcessingLensEffects", OctanePostProcessingGroupPostProcessingLensEffects.bl_label).init()
        self.inputs.new("OctanePostProcessingChromaticAbrIntensity", OctanePostProcessingChromaticAbrIntensity.bl_label).init()
        self.inputs.new("OctanePostProcessingLensFlare", OctanePostProcessingLensFlare.bl_label).init()
        self.inputs.new("OctanePostProcessingLensFlareExtent", OctanePostProcessingLensFlareExtent.bl_label).init()
        self.inputs.new("OctanePostProcessingGroupPostProcessingVolumeEffects", OctanePostProcessingGroupPostProcessingVolumeEffects.bl_label).init()
        self.inputs.new("OctanePostProcessingPostVolume", OctanePostProcessingPostVolume.bl_label).init()
        self.outputs.new("OctanePostProcessingOutSocket", "Post processing out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctanePostProcessingOnOff,
    OctanePostProcessingCutoff,
    OctanePostProcessingBloomPower,
    OctanePostProcessingGlarePower,
    OctanePostProcessingGlareRayAmount,
    OctanePostProcessingGlareAngle,
    OctanePostProcessingGlareBlur,
    OctanePostProcessingSpreadStart,
    OctanePostProcessingSpreadEnd,
    OctanePostProcessingSpectralIntensity,
    OctanePostProcessingSpectralShift,
    OctanePostProcessingChromaticAbrIntensity,
    OctanePostProcessingLensFlare,
    OctanePostProcessingLensFlareExtent,
    OctanePostProcessingPostVolume,
    OctanePostProcessingGroupPostImageProcessing,
    OctanePostProcessingGroupPostProcessingLensEffects,
    OctanePostProcessingGroupPostProcessingVolumeEffects,
    OctanePostProcessing,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
