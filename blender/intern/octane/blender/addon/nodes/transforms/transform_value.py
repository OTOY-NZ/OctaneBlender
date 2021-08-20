##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTransformValue(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTransformValue"
    bl_label="Transform value"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=67)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_rotation_order;a_rotation;a_scale;a_translation;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;8;8;8;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    a_rotation_order: IntProperty(name="Rotation order", default=2, update=None, description="The axis order in which the rotation will be executed. Must be of type Matrix::RotationOrder. Changing this attribute will re-calculate A_ROTATION from A_TRANSFORM using the new rotation order")
    a_rotation: FloatVectorProperty(name="Rotation", default=(0.000000, 0.000000, 0.000000), size=3, update=None, description="Rotation. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")
    a_scale: FloatVectorProperty(name="Scale", default=(1.000000, 1.000000, 1.000000), size=3, update=None, description="Scale. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")
    a_translation: FloatVectorProperty(name="Translation", default=(0.000000, 0.000000, 0.000000), size=3, update=None, description="Translation. Either calculated from A_TRANSFORM or used to calculate A_TRANSFORM")

    def init(self, context):
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()


_classes=[
    OctaneTransformValue,
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

from ...utils import utility
from . import _3d_transformation

class OctaneTransformValue_Override(OctaneTransformValue):
    rotation_order_items=_3d_transformation.Octane3DTransformationRotationOrder.items
    a_rotation_order: EnumProperty(name="Rotation Order", default="YXZ", update=None, description="Provides the rotation order that is used when the transformation matrix calculated", items=rotation_order_items)

    def draw_buttons(self, context, layout):        
        layout.row().prop(self, "a_rotation_order")
        # layout in column to enable multiple selections for vector properties
        layout.row().column().prop(self, "a_rotation")
        layout.row().column().prop(self, "a_scale")
        layout.row().column().prop(self, "a_translation")

utility.override_class(_classes, OctaneTransformValue, OctaneTransformValue_Override)          