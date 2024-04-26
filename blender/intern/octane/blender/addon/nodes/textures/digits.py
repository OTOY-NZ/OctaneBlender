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


class OctaneDigitsNumber(OctaneBaseSocket):
    bl_idname="OctaneDigitsNumber"
    bl_label="Number"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_NUMBER
    octane_pin_name="number"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=42.000000, update=OctaneBaseSocket.update_node_tree, description="The number to display", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsDigits(OctaneBaseSocket):
    bl_idname="OctaneDigitsDigits"
    bl_label="Digits"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_DIGITS
    octane_pin_name="digits"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="The minimum number of digits to display. Inserts leading zeroes if the number consists of fewer digits than requested", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsDecimals(OctaneBaseSocket):
    bl_idname="OctaneDigitsDecimals"
    bl_label="Decimals"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_DECIMALS
    octane_pin_name="decimals"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="The number of digits to display after the decimal point", min=0, max=7, soft_min=0, soft_max=7, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsTexture(OctaneBaseSocket):
    bl_idname="OctaneDigitsTexture"
    bl_label="Background"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_TEXTURE
    octane_pin_name="texture"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The background color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsEnabledColor(OctaneBaseSocket):
    bl_idname="OctaneDigitsEnabledColor"
    bl_label="On color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_ENABLED_COLOR
    octane_pin_name="enabledColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(1.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color for the enabled components of each digit", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsDisabledColor(OctaneBaseSocket):
    bl_idname="OctaneDigitsDisabledColor"
    bl_label="Off color"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_DISABLED_COLOR
    octane_pin_name="disabledColor"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.100000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color for the disabled components of each digit", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsShowDisabledComponents(OctaneBaseSocket):
    bl_idname="OctaneDigitsShowDisabledComponents"
    bl_label="Use off color"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SHOW_DISABLED_COMPONENTS
    octane_pin_name="showDisabledComponents"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Show the disabled components of the digits")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsTransform(OctaneBaseSocket):
    bl_idname="OctaneDigitsTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigitsProjection(OctaneBaseSocket):
    bl_idname="OctaneDigitsProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_UVW
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDigits(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDigits"
    bl_label="Digits"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDigitsNumber,OctaneDigitsDigits,OctaneDigitsDecimals,OctaneDigitsTexture,OctaneDigitsEnabledColor,OctaneDigitsDisabledColor,OctaneDigitsShowDisabledComponents,OctaneDigitsTransform,OctaneDigitsProjection,]
    octane_min_version=12000005
    octane_node_type=consts.NodeType.NT_TEX_DIGITS
    octane_socket_list=["Number", "Digits", "Decimals", "Background", "On color", "Off color", "Use off color", "UV transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneDigitsNumber", OctaneDigitsNumber.bl_label).init()
        self.inputs.new("OctaneDigitsDigits", OctaneDigitsDigits.bl_label).init()
        self.inputs.new("OctaneDigitsDecimals", OctaneDigitsDecimals.bl_label).init()
        self.inputs.new("OctaneDigitsTexture", OctaneDigitsTexture.bl_label).init()
        self.inputs.new("OctaneDigitsEnabledColor", OctaneDigitsEnabledColor.bl_label).init()
        self.inputs.new("OctaneDigitsDisabledColor", OctaneDigitsDisabledColor.bl_label).init()
        self.inputs.new("OctaneDigitsShowDisabledComponents", OctaneDigitsShowDisabledComponents.bl_label).init()
        self.inputs.new("OctaneDigitsTransform", OctaneDigitsTransform.bl_label).init()
        self.inputs.new("OctaneDigitsProjection", OctaneDigitsProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneDigitsNumber,
    OctaneDigitsDigits,
    OctaneDigitsDecimals,
    OctaneDigitsTexture,
    OctaneDigitsEnabledColor,
    OctaneDigitsDisabledColor,
    OctaneDigitsShowDisabledComponents,
    OctaneDigitsTransform,
    OctaneDigitsProjection,
    OctaneDigits,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
