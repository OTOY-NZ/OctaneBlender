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


class OctaneBitValue(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBitValue"
    bl_label="Bit value"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=132)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_value;")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="value;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_value: IntProperty(name="Value", default=0, update=OctaneBaseNode.update_node_tree, description="The value of the bit mask node")

    def init(self, context):
        self.outputs.new("OctaneBitMaskOutSocket", "BitMask out").init()


_CLASSES=[
    OctaneBitValue,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneLightIDBitValue(OctaneBitValue):
    bl_idname="OctaneLightIDBitValue"
    bl_label="Light IDs"
    property_to_bits = ["sunlight", "environment", "light_pass_id_1", "light_pass_id_2", "light_pass_id_3", "light_pass_id_4", "light_pass_id_5", "light_pass_id_6", "light_pass_id_7", "light_pass_id_8"]

    def update_value(self, context):
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


_CLASSES=[
    OctaneLightIDBitValue,
]