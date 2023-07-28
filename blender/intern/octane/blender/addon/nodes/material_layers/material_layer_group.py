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


class OctaneMaterialLayerGroup(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMaterialLayerGroup"
    bl_label="Material layer group"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_LAYER_GROUP
    octane_socket_list=[]
    octane_attribute_list=["a_pin_count", ]
    octane_attribute_config={"a_pin_count": [consts.AttributeID.A_PIN_COUNT, "pin_count", consts.AttributeType.AT_INT], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count=0

    a_pin_count: IntProperty(name="Pin count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of layers to group. Any new layers will be added to the end of the pin list")

    def init(self, context):
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMaterialLayerGroup,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneMaterialLayerGroupLayerMovableInput(OctaneMovableInput):
    bl_idname="OctaneMaterialLayerGroupLayerMovableInput"
    bl_label="Layer"
    octane_movable_input_count_attribute_name="a_pin_count"
    octane_input_pattern=r"Layer (\d+)"
    octane_input_format_pattern="Layer {}"
    color=consts.OctanePinColor.MaterialLayer
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneMaterialLayerGroup_Override(OctaneMaterialLayerGroup):
    MAX_AOV_OUTPUT_COUNT = 8
    DEFAULT_AOV_OUTPUT_COUNT = 2

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneMaterialLayerGroupLayerMovableInput, self.DEFAULT_AOV_OUTPUT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneMaterialLayerGroupLayerMovableInput, self.MAX_AOV_OUTPUT_COUNT)


_ADDED_CLASSES = [OctaneMaterialLayerGroupLayerMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneMaterialLayerGroup, OctaneMaterialLayerGroup_Override)    