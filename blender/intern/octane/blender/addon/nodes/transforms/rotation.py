##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRotationRotationOrder(OctaneBaseSocket):
    bl_idname="OctaneRotationRotationOrder"
    bl_label="Order"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=202)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("XYZ", "XYZ", "", 0),
        ("XZY", "XZY", "", 1),
        ("YXZ", "YXZ", "", 2),
        ("YZX", "YZX", "", 3),
        ("ZXY", "ZXY", "", 4),
        ("ZYX", "ZYX", "", 5),
    ]
    default_value: EnumProperty(default="YXZ", update=None, description="Provides the rotation order that is used when the transformation matrix calculated", items=items)
    octane_hide_value=False
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRotationRotation(OctaneBaseSocket):
    bl_idname="OctaneRotationRotation"
    bl_label="Angles"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=203)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Provides the X/Y/Z rotation angles", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=10, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRotation(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRotation"
    bl_label="Rotation Transform"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=29)
    octane_socket_list: StringProperty(name="Socket List", default="Order;Angles;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneRotationRotationOrder", OctaneRotationRotationOrder.bl_label).init()
        self.inputs.new("OctaneRotationRotation", OctaneRotationRotation.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()


_classes=[
    OctaneRotationRotationOrder,
    OctaneRotationRotation,
    OctaneRotation,
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
