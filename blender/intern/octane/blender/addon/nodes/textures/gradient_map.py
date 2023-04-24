##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneGradientMapGradientInterpolationType(OctaneBaseSocket):
    bl_idname="OctaneGradientMapGradientInterpolationType"
    bl_label="Interpolation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=299)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="gradientInterpolationType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Cubic", "Cubic", "", 3),
    ]
    default_value: EnumProperty(default="Linear", update=OctaneBaseSocket.update_node_tree, description="Determines how colors are blended", items=items)
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientMapInput(OctaneBaseSocket):
    bl_idname="OctaneGradientMapInput"
    bl_label="Input texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="input")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientMapMin(OctaneBaseSocket):
    bl_idname="OctaneGradientMapMin"
    bl_label="Start value"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=113)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="min")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Output value at 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientMapMax(OctaneBaseSocket):
    bl_idname="OctaneGradientMapMax"
    bl_label="End value"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=33
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=106)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="max")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Output value at 1.0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientMapSmooth(OctaneBaseSocket):
    bl_idname="OctaneGradientMapSmooth"
    bl_label="Smoothing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="smooth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Make the gradient more smooth around the control points")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=3000005
    octane_deprecated=True

class OctaneGradientMap(bpy.types.Node, OctaneBaseRampNode):
    bl_idname="OctaneGradientMap"
    bl_label="Gradient map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=49)
    octane_socket_list: StringProperty(name="Socket List", default="Interpolation;Input texture;Start value;End value;Smoothing;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_num_controlpoints;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    a_num_controlpoints: IntProperty(name="Num controlpoints", default=0, update=OctaneBaseNode.update_node_tree, description="The number of control points between start and end")

    def init(self, context):
        self.inputs.new("OctaneGradientMapGradientInterpolationType", OctaneGradientMapGradientInterpolationType.bl_label).init()
        self.inputs.new("OctaneGradientMapInput", OctaneGradientMapInput.bl_label).init()
        self.inputs.new("OctaneGradientMapMin", OctaneGradientMapMin.bl_label).init()
        self.inputs.new("OctaneGradientMapMax", OctaneGradientMapMax.bl_label).init()
        self.inputs.new("OctaneGradientMapSmooth", OctaneGradientMapSmooth.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneGradientMapGradientInterpolationType,
    OctaneGradientMapInput,
    OctaneGradientMapMin,
    OctaneGradientMapMax,
    OctaneGradientMapSmooth,
    OctaneGradientMap,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneGradientMapGradientInterpolationType_Override(OctaneGradientMapGradientInterpolationType):
    items = [
        ("Constant", "Constant", "", 1),
        ("Linear", "Linear", "", 2),
        ("Cubic", "Cubic", "", 3),
    ]
    default_value: EnumProperty(default="Linear", update=lambda self, context: self.node.update_color_ramp_interpolation(context), description="Determines how colors are blended", items=items) 

class OctaneGradientMap_Override(OctaneGradientMap):
    bl_width_default = 300
    MAX_VALUE_SOCKET = 16

    def init(self, context):
        super().init(context)        
        self.init_octane_color_ramp()
        
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)

utility.override_class(_CLASSES, OctaneGradientMapGradientInterpolationType, OctaneGradientMapGradientInterpolationType_Override)
utility.override_class(_CLASSES, OctaneGradientMap, OctaneGradientMap_Override)