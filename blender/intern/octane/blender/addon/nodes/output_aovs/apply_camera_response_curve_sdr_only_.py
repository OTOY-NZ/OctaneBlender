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


class OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse"
    bl_label="Curve"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_RESPONSE
    octane_pin_name="response"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("None", "None", "", 401),
        ("Agfa|Agfacolor Futura 100CD", "Agfa|Agfacolor Futura 100CD", "", 99),
        ("Agfa|Agfacolor Futura 200CD", "Agfa|Agfacolor Futura 200CD", "", 100),
        ("Agfa|Agfacolor Futura 400CD", "Agfa|Agfacolor Futura 400CD", "", 101),
        ("Agfa|Agfacolor Futura II 100CD", "Agfa|Agfacolor Futura II 100CD", "", 102),
        ("Agfa|Agfacolor Futura II 200CD", "Agfa|Agfacolor Futura II 200CD", "", 103),
        ("Agfa|Agfacolor Futura II 400CD", "Agfa|Agfacolor Futura II 400CD", "", 104),
        ("Agfa|Agfacolor HDC 100 plusCD", "Agfa|Agfacolor HDC 100 plusCD", "", 105),
        ("Agfa|Agfacolor HDC 200 plusCD", "Agfa|Agfacolor HDC 200 plusCD", "", 106),
        ("Agfa|Agfacolor HDC 400 plusCD", "Agfa|Agfacolor HDC 400 plusCD", "", 107),
        ("Agfa|Agfacolor Optima II 100CD", "Agfa|Agfacolor Optima II 100CD", "", 108),
        ("Agfa|Agfacolor Optima II 200CD", "Agfa|Agfacolor Optima II 200CD", "", 109),
        ("Agfa|Agfacolor ultra 050 CD", "Agfa|Agfacolor ultra 050 CD", "", 110),
        ("Agfa|Agfacolor Vista 100CD", "Agfa|Agfacolor Vista 100CD", "", 111),
        ("Agfa|Agfacolor Vista 200CD", "Agfa|Agfacolor Vista 200CD", "", 112),
        ("Agfa|Agfacolor Vista 400CD", "Agfa|Agfacolor Vista 400CD", "", 113),
        ("Agfa|Agfacolor Vista 800CD", "Agfa|Agfacolor Vista 800CD", "", 114),
        ("Agfa|Agfachrome CT precisa 100CD", "Agfa|Agfachrome CT precisa 100CD", "", 115),
        ("Agfa|Agfachrome CT precisa 200CD", "Agfa|Agfachrome CT precisa 200CD", "", 116),
        ("Agfa|Agfachrome RSX2 050CD", "Agfa|Agfachrome RSX2 050CD", "", 117),
        ("Agfa|Agfachrome RSX2 100CD", "Agfa|Agfachrome RSX2 100CD", "", 118),
        ("Agfa|Agfachrome RSX2 200CD", "Agfa|Agfachrome RSX2 200CD", "", 119),
        ("Kodak|Advantix 100CD", "Kodak|Advantix 100CD", "", 201),
        ("Kodak|Advantix 200CD", "Kodak|Advantix 200CD", "", 202),
        ("Kodak|Advantix 400CD", "Kodak|Advantix 400CD", "", 203),
        ("Kodak|Gold 100CD", "Kodak|Gold 100CD", "", 204),
        ("Kodak|Gold 200CD", "Kodak|Gold 200CD", "", 205),
        ("Kodak|Max Zoom 800CD", "Kodak|Max Zoom 800CD", "", 206),
        ("Kodak|Portra 100TCD", "Kodak|Portra 100TCD", "", 207),
        ("Kodak|Portra 160NCCD", "Kodak|Portra 160NCCD", "", 208),
        ("Kodak|Portra 160VCCD", "Kodak|Portra 160VCCD", "", 209),
        ("Kodak|Portra 800CD", "Kodak|Portra 800CD", "", 210),
        ("Kodak|Portra 400VCCD", "Kodak|Portra 400VCCD", "", 211),
        ("Kodak|Portra 400NCCD", "Kodak|Portra 400NCCD", "", 212),
        ("Kodak|Ektachrome 100 plusCD", "Kodak|Ektachrome 100 plusCD", "", 213),
        ("Kodak|Ektachrome 320TCD", "Kodak|Ektachrome 320TCD", "", 214),
        ("Kodak|Ektachrome 400XCD", "Kodak|Ektachrome 400XCD", "", 215),
        ("Kodak|Ektachrome 64CD", "Kodak|Ektachrome 64CD", "", 216),
        ("Kodak|Ektachrome 64TCD", "Kodak|Ektachrome 64TCD", "", 217),
        ("Kodak|Ektachrome E100SCD", "Kodak|Ektachrome E100SCD", "", 218),
        ("Kodak|Ektachrome 100CD", "Kodak|Ektachrome 100CD", "", 219),
        ("Kodak|Kodachrome 200CD", "Kodak|Kodachrome 200CD", "", 220),
        ("Kodak|Kodachrome 25", "Kodak|Kodachrome 25", "", 221),
        ("Kodak|Kodachrome 64CD", "Kodak|Kodachrome 64CD", "", 222),
        ("Misc.|F125CD", "Misc.|F125CD", "", 301),
        ("Misc.|F250CD", "Misc.|F250CD", "", 302),
        ("Misc.|F400CD", "Misc.|F400CD", "", 303),
        ("Misc.|FCICD", "Misc.|FCICD", "", 304),
        ("Misc.|dscs315_1", "Misc.|dscs315_1", "", 305),
        ("Misc.|dscs315_2", "Misc.|dscs315_2", "", 306),
        ("Misc.|dscs315_3", "Misc.|dscs315_3", "", 307),
        ("Misc.|dscs315_4", "Misc.|dscs315_4", "", 308),
        ("Misc.|dscs315_5", "Misc.|dscs315_5", "", 309),
        ("Misc.|dscs315_6", "Misc.|dscs315_6", "", 310),
        ("Misc.|FP2900Z", "Misc.|FP2900Z", "", 311),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="Camera response curve provided by Octane", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse(OctaneBaseSocket):
    bl_idname="OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse"
    bl_label="Neutral"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_NEUTRAL_RESPONSE
    octane_pin_name="neutralResponse"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the selected response curve will not affect the hue or saturation. The green component of the curve will be used for the red and blue channels")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneOutputAOVsApplyCameraResponseCurveSDROnly(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneOutputAOVsApplyCameraResponseCurveSDROnly"
    bl_label="Apply camera response curve (SDR only)"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled,OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse,OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_LAYER_APPLY_CAMERA_RESPONSE_CURVE
    octane_socket_list=["Enabled", "Curve", "Neutral", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled", OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse", OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse.bl_label).init()
        self.inputs.new("OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse", OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneOutputAOVsApplyCameraResponseCurveSDROnlyEnabled,
    OctaneOutputAOVsApplyCameraResponseCurveSDROnlyResponse,
    OctaneOutputAOVsApplyCameraResponseCurveSDROnlyNeutralResponse,
    OctaneOutputAOVsApplyCameraResponseCurveSDROnly,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
