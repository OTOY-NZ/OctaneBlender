##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCylindricalTransform(OctaneBaseSocket):
    bl_idname="OctaneCylindricalTransform"
    bl_label="Cylinder transformation"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCylindricalPositionType(OctaneBaseSocket):
    bl_idname="OctaneCylindricalPositionType"
    bl_label="Coordinate space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=135)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
        ("Normal space (IES Lights)", "Normal space (IES Lights)", "", 4),
    ]
    default_value: EnumProperty(default="Object space", update=None, description="Coordinate space used by the texture", items=items)
    octane_hide_value=False
    octane_min_version=1240000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCylindrical(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCylindrical"
    bl_label="Cylindrical Projection"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=74)
    octane_socket_list: StringProperty(name="Socket List", default="Cylinder transformation;Coordinate space;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneCylindricalTransform", OctaneCylindricalTransform.bl_label).init()
        self.inputs.new("OctaneCylindricalPositionType", OctaneCylindricalPositionType.bl_label).init()
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()


_classes=[
    OctaneCylindricalTransform,
    OctaneCylindricalPositionType,
    OctaneCylindrical,
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
