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


class OctaneBinaryMathOperationTexture1(OctaneBaseSocket):
    bl_idname="OctaneBinaryMathOperationTexture1"
    bl_label="Argument A"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture1")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBinaryMathOperationTexture2(OctaneBaseSocket):
    bl_idname="OctaneBinaryMathOperationTexture2"
    bl_label="Argument B"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture2")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBinaryMathOperationOperationType(OctaneBaseSocket):
    bl_idname="OctaneBinaryMathOperationOperationType"
    bl_label="Operation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="operationType")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Functions|Add", "Functions|Add", "", 0),
        ("Functions|Cross product", "Functions|Cross product", "", 2),
        ("Functions|Divide", "Functions|Divide", "", 3),
        ("Functions|Dot product", "Functions|Dot product", "", 4),
        ("Functions|Exponential [a^b]", "Functions|Exponential [a^b]", "", 11),
        ("Functions|Logarithm [log_b(a)]", "Functions|Logarithm [log_b(a)]", "", 6),
        ("Functions|Multiply", "Functions|Multiply", "", 10),
        ("Functions|Remainder (always positive)", "Functions|Remainder (always positive)", "", 9),
        ("Functions|Remainder (keeps sign of a)", "Functions|Remainder (keeps sign of a)", "", 5),
        ("Functions|Subtract", "Functions|Subtract", "", 12),
        ("Comparison|Maximum value", "Comparison|Maximum value", "", 7),
        ("Comparison|Minimum value", "Comparison|Minimum value", "", 8),
        ("Trigonometric|Arc tangent", "Trigonometric|Arc tangent", "", 1),
    ]
    default_value: EnumProperty(default="Functions|Add", update=OctaneBaseSocket.update_node_tree, description="The operation to perform on the input", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBinaryMathOperation(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBinaryMathOperation"
    bl_label="Binary math operation"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=339)
    octane_socket_list: StringProperty(name="Socket List", default="Argument A;Argument B;Operation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneBinaryMathOperationTexture1", OctaneBinaryMathOperationTexture1.bl_label).init()
        self.inputs.new("OctaneBinaryMathOperationTexture2", OctaneBinaryMathOperationTexture2.bl_label).init()
        self.inputs.new("OctaneBinaryMathOperationOperationType", OctaneBinaryMathOperationOperationType.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneBinaryMathOperationTexture1,
    OctaneBinaryMathOperationTexture2,
    OctaneBinaryMathOperationOperationType,
    OctaneBinaryMathOperation,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneBinaryMathOperationOperationType_simplified_items = utility.make_blender_style_enum_items(OctaneBinaryMathOperationOperationType.items)

class OctaneBinaryMathOperationOperationType_Override(OctaneBinaryMathOperationOperationType):
    default_value: EnumProperty(default="Add", update=OctaneBaseSocket.update_node_tree, description="The operation to perform on the input", items=OctaneBinaryMathOperationOperationType_simplified_items)

utility.override_class(_CLASSES, OctaneBinaryMathOperationOperationType, OctaneBinaryMathOperationOperationType_Override)  