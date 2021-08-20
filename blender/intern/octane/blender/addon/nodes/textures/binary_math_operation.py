##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneBinaryMathOperationTexture1(OctaneBaseSocket):
    bl_idname="OctaneBinaryMathOperationTexture1"
    bl_label="Argument A"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
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
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
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
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Add", "Add", "", 0),
        ("Arc tangent", "Arc tangent", "", 1),
        ("Cross product", "Cross product", "", 2),
        ("Divide", "Divide", "", 3),
        ("Dot product", "Dot product", "", 4),
        ("Exponential [a^b]", "Exponential [a^b]", "", 11),
        ("Logarithm [log_b(a)]", "Logarithm [log_b(a)]", "", 6),
        ("Maximum value", "Maximum value", "", 7),
        ("Minimum value", "Minimum value", "", 8),
        ("Multiply", "Multiply", "", 10),
        ("Remainder (always positive)", "Remainder (always positive)", "", 9),
        ("Remainder (keeps sign of a)", "Remainder (keeps sign of a)", "", 5),
        ("Subtract", "Subtract", "", 12),
    ]
    default_value: EnumProperty(default="Add", update=None, description="The operation to perform on the input", items=items)
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
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneBinaryMathOperationTexture1", OctaneBinaryMathOperationTexture1.bl_label).init()
        self.inputs.new("OctaneBinaryMathOperationTexture2", OctaneBinaryMathOperationTexture2.bl_label).init()
        self.inputs.new("OctaneBinaryMathOperationOperationType", OctaneBinaryMathOperationOperationType.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneBinaryMathOperationTexture1,
    OctaneBinaryMathOperationTexture2,
    OctaneBinaryMathOperationOperationType,
    OctaneBinaryMathOperation,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
