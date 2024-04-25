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


class OctaneTransformValue(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTransformValue"
    bl_label = "Transform value"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = []
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TRANSFORM_VALUE
    octane_socket_list = []
    octane_attribute_list = ["a_rotation_order", "a_rotation", "a_scale", "a_translation", ]
    octane_attribute_config = {"a_rotation_order": [consts.AttributeID.A_ROTATION_ORDER, "rotationOrder", consts.AttributeType.AT_INT], "a_rotation": [consts.AttributeID.A_ROTATION, "rotation", consts.AttributeType.AT_FLOAT3], "a_scale": [consts.AttributeID.A_SCALE, "scale", consts.AttributeType.AT_FLOAT3], "a_translation": [consts.AttributeID.A_TRANSLATION, "translation", consts.AttributeType.AT_FLOAT3], "a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count = 0

    a_rotation_order: IntProperty(name="Rotation order", default=2, update=OctaneBaseNode.update_node_tree, description="The axis order in which the rotation will be executed. Must be of type Matrix::RotationOrder. Changing this attribute will re-calculate A_ROTATION from A_TRANSFORM using the new rotation order")
    a_rotation: FloatVectorProperty(name="Rotation", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Rotation. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")
    a_scale: FloatVectorProperty(name="Scale", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Scale. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")
    a_translation: FloatVectorProperty(name="Translation", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Translation. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")

    def init(self, context):  # noqa
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneTransformValue,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


from octane.utils import utility
from octane.nodes.transforms import _3d_transformation


class OctaneTransformValue_Override(OctaneTransformValue):
    octane_attribute_list = ["a_rotation_order", "a_rotation", "a_scale", "a_translation", "a_transform"]
    rotation_order_items = _3d_transformation.Octane3DTransformationRotationOrder.items
    a_rotation_order: EnumProperty(name="Rotation Order", default="YXZ", update=OctaneBaseNode.update_node_tree, description="Provides the rotation order that is used when the transformation matrix calculated", items=rotation_order_items)

    def draw_buttons(self, context, layout):        
        layout.row().prop(self, "a_rotation_order")
        # layout in column to enable multiple selections for vector properties
        layout.row().column().prop(self, "a_rotation")
        layout.row().column().prop(self, "a_scale")
        layout.row().column().prop(self, "a_translation")


utility.override_class(_CLASSES, OctaneTransformValue, OctaneTransformValue_Override)
