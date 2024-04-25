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


class OctaneBitValue(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneBitValue"
    bl_label = "Bit value"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_BIT_MASK
    octane_socket_list = []
    octane_attribute_list = ["a_value", ]
    octane_attribute_config = {"a_value": [consts.AttributeID.A_VALUE, "value", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 0

    a_value: IntProperty(name="Value", default=0, update=OctaneBaseNode.update_node_tree, description="The value of the bit mask node")

    def init(self, context):  # noqa
        self.outputs.new("OctaneBitMaskOutSocket", "BitMask out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneBitValue,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


class OctaneLightIDBitValue(OctaneBitValue):
    bl_idname = "OctaneLightIDBitValue"
    bl_label = "Light IDs"
    property_to_bits = ["sunlight", "environment",
                        "light_pass_id_1", "light_pass_id_2", "light_pass_id_3", "light_pass_id_4", "light_pass_id_5",
                        "light_pass_id_6", "light_pass_id_7", "light_pass_id_8", "light_pass_id_9", "light_pass_id_10",
                        "light_pass_id_11", "light_pass_id_12", "light_pass_id_13", "light_pass_id_14", "light_pass_id_15",
                        "light_pass_id_16", "light_pass_id_17", "light_pass_id_18", "light_pass_id_19", "light_pass_id_20",]

    def update_value(self, _context):
        value = 0
        for idx, property_name in enumerate(self.property_to_bits):
            value += (int(getattr(self, property_name)) << idx)
        self.a_value = value

    sunlight: BoolProperty(name="s", default=False, description="Sunlight", update=update_value)
    environment: BoolProperty(name="e", default=False, description="Environment", update=update_value)
    light_pass_id_1: BoolProperty(name="1", default=False, description="Light pass ID 1", update=update_value)
    light_pass_id_2: BoolProperty(name="2", default=False, description="Light pass ID 2", update=update_value)
    light_pass_id_3: BoolProperty(name="3", default=False, description="Light pass ID 3", update=update_value)
    light_pass_id_4: BoolProperty(name="4", default=False, description="Light pass ID 4", update=update_value)
    light_pass_id_5: BoolProperty(name="5", default=False, description="Light pass ID 5", update=update_value)
    light_pass_id_6: BoolProperty(name="6", default=False, description="Light pass ID 6", update=update_value)
    light_pass_id_7: BoolProperty(name="7", default=False, description="Light pass ID 7", update=update_value)
    light_pass_id_8: BoolProperty(name="8", default=False, description="Light pass ID 8", update=update_value)
    light_pass_id_9: BoolProperty(name="9", default=False, description="Light pass ID 9", update=update_value)
    light_pass_id_10: BoolProperty(name="10", default=False, description="Light pass ID 10", update=update_value)
    light_pass_id_11: BoolProperty(name="11", default=False, description="Light pass ID 11", update=update_value)
    light_pass_id_12: BoolProperty(name="12", default=False, description="Light pass ID 12", update=update_value)
    light_pass_id_13: BoolProperty(name="13", default=False, description="Light pass ID 13", update=update_value)
    light_pass_id_14: BoolProperty(name="14", default=False, description="Light pass ID 14", update=update_value)
    light_pass_id_15: BoolProperty(name="15", default=False, description="Light pass ID 15", update=update_value)
    light_pass_id_16: BoolProperty(name="16", default=False, description="Light pass ID 16", update=update_value)
    light_pass_id_17: BoolProperty(name="17", default=False, description="Light pass ID 17", update=update_value)
    light_pass_id_18: BoolProperty(name="18", default=False, description="Light pass ID 18", update=update_value)
    light_pass_id_19: BoolProperty(name="19", default=False, description="Light pass ID 19", update=update_value)
    light_pass_id_20: BoolProperty(name="20", default=False, description="Light pass ID 20", update=update_value)

    def draw_buttons(self, context, layout):
        layout.label(text="Light IDs:")
        row = layout.row(align=True)
        row.prop(self, "sunlight", toggle=True)
        row.prop(self, "environment", toggle=True)
        row.prop(self, "light_pass_id_1", toggle=True)
        row.prop(self, "light_pass_id_2", toggle=True)
        row.prop(self, "light_pass_id_3", toggle=True)
        row.prop(self, "light_pass_id_4", toggle=True)
        row.prop(self, "light_pass_id_5", toggle=True)
        row.prop(self, "light_pass_id_6", toggle=True)
        row.prop(self, "light_pass_id_7", toggle=True)
        row.prop(self, "light_pass_id_8", toggle=True)
        row = layout.row(align=True)  
        row.prop(self, "light_pass_id_9", toggle=True)
        row.prop(self, "light_pass_id_10", toggle=True)
        row.prop(self, "light_pass_id_11", toggle=True)
        row.prop(self, "light_pass_id_12", toggle=True)
        row.prop(self, "light_pass_id_13", toggle=True)
        row.prop(self, "light_pass_id_14", toggle=True)
        row = layout.row(align=True)
        row.prop(self, "light_pass_id_15", toggle=True)
        row.prop(self, "light_pass_id_16", toggle=True)
        row.prop(self, "light_pass_id_17", toggle=True)
        row.prop(self, "light_pass_id_18", toggle=True)  
        row.prop(self, "light_pass_id_19", toggle=True)
        row.prop(self, "light_pass_id_20", toggle=True)

    def dump_json_custom_node(self, node_dict):
        attributes_dict = node_dict["attributes"]
        for attribute_name in self.property_to_bits:
            if hasattr(self, attribute_name):
                self.dump_json_attribute(attribute_name, consts.AttributeType.AT_BOOL, attributes_dict)

    def load_json_custom_node(self, node_dict, links_list):
        attributes_dict = node_dict["attributes"]
        for attribute_name in self.property_to_bits:
            if hasattr(self, attribute_name) and attribute_name in attributes_dict:
                self.load_json_attribute(attribute_name, consts.AttributeType.AT_BOOL, attributes_dict)


utility.override_class(_CLASSES, OctaneBitValue, OctaneLightIDBitValue)
