##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneBoxTransform(OctaneBaseSocket):
    bl_idname="OctaneBoxTransform"
    bl_label="Normal box transformation"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneBoxPositionType(OctaneBaseSocket):
    bl_idname="OctaneBoxPositionType"
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

class OctaneBox(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneBox"
    bl_label="Box Projection"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=79)
    octane_socket_list: StringProperty(name="Socket List", default="Normal box transformation;Coordinate space;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneBoxTransform", OctaneBoxTransform.bl_label).init()
        self.inputs.new("OctaneBoxPositionType", OctaneBoxPositionType.bl_label).init()
        self.outputs.new("OctaneProjectionOutSocket", "Projection out").init()


_CLASSES=[
    OctaneBoxTransform,
    OctaneBoxPositionType,
    OctaneBox,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
