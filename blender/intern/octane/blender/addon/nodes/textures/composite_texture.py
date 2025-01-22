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


class OctaneCompositeTextureClamp(OctaneBaseSocket):
    bl_idname = "OctaneCompositeTextureClamp"
    bl_label = "Clamp"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_CLAMP
    octane_pin_name = "clamp"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Clamp the result of blending each layer to [0,1] (ignored when used as a normal map)")
    octane_hide_value = False
    octane_min_version = 10020600
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneCompositeTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCompositeTexture"
    bl_label = "Composite texture"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneCompositeTextureClamp, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_COMPOSITE
    octane_socket_list = ["Clamp", ]
    octane_attribute_list = ["a_layer_count", "a_compatibility_version", ]
    octane_attribute_config = {"a_layer_count": [consts.AttributeID.A_LAYER_COUNT, "layerCount", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], "a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 1

    compatibility_mode_infos = [
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000001),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """The background color is gray (0.7) instead of black if the bottom layer is disconnected. The "Texture" layer inputs are clamped in addition to the blend results if "Clamp" is enabled.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_layer_count: IntProperty(name="Layer count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layer pins. Changing this value and evaluating the node will update the number of layer pins. New pins will be added to the front of the dynamic pin list")
    a_compatibility_version: IntProperty(name="Compatibility version", default=14000007, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctaneCompositeTextureClamp", OctaneCompositeTextureClamp.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctaneCompositeTextureClamp,
    OctaneCompositeTexture,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneCompositeTextureMovableTextureLayerInput(OctaneMovableInput):
    bl_idname = "OctaneCompositeTextureMovableTextureLayerInput"
    bl_label = "Layer"
    octane_movable_input_count_attribute_name = "a_layer_count"
    octane_input_pattern = r"Layer (\d+)"
    octane_input_format_pattern = "Layer {}"
    octane_reversed_input_sockets = True
    color = consts.OctanePinColor.CompositeTextureLayer
    octane_default_node_type = consts.NodeType.NT_TEX_COMPOSITE_LAYER
    octane_default_node_name = "OctaneTexLayerTexture"
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneCompositeTextureGroupTextureLayers(OctaneGroupTitleMovableInputs):
    bl_idname = "OctaneCompositeTextureGroupTextureLayers"
    bl_label = "[OctaneGroupTitle]Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="")


class OctaneCompositeTexture_Override(OctaneCompositeTexture):
    MAX_LAYER_COUNT = 16
    DEFAULT_LAYER_COUNT = 2   

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeTextureGroupTextureLayers", OctaneCompositeTextureGroupTextureLayers.bl_label).init(cls=OctaneCompositeTextureMovableTextureLayerInput, max_num=self.MAX_LAYER_COUNT)        
        self.init_movable_inputs(context, OctaneCompositeTextureMovableTextureLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        self.draw_movable_inputs(context, layout, OctaneCompositeTextureMovableTextureLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneCompositeTextureMovableTextureLayerInput, OctaneCompositeTextureGroupTextureLayers]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneCompositeTexture, OctaneCompositeTexture_Override)
