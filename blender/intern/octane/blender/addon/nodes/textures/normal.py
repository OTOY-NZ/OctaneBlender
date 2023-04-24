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


class OctaneNormalNormalType(OctaneBaseSocket):
    bl_idname="OctaneNormalNormalType"
    bl_label="Normal type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=649)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Geometric", "Geometric", "", 0),
        ("Smooth", "Smooth", "", 1),
        ("Shading", "Shading", "", 2),
    ]
    default_value: EnumProperty(default="Geometric", update=OctaneBaseSocket.update_node_tree, description="Type of normal computed", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormalCoordinateSystem(OctaneBaseSocket):
    bl_idname="OctaneNormalCoordinateSystem"
    bl_label="Coordinate system"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=645)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("World", "World", "", 0),
        ("Camera", "Camera", "", 1),
        ("Object", "Object", "", 2),
        ("Tangent", "Tangent", "", 3),
    ]
    default_value: EnumProperty(default="World", update=OctaneBaseSocket.update_node_tree, description="Coordinate space used to compute the normal", items=items)
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormalNormalize(OctaneBaseSocket):
    bl_idname="OctaneNormalNormalize"
    bl_label="Normalize result"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Whether to remap the result to the [0..1] range or leave it in the [-1..+1] range")
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormal(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNormal"
    bl_label="Normal"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=327)
    octane_socket_list: StringProperty(name="Socket List", default="Normal type;Coordinate system;Normalize result;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneNormalNormalType", OctaneNormalNormalType.bl_label).init()
        self.inputs.new("OctaneNormalCoordinateSystem", OctaneNormalCoordinateSystem.bl_label).init()
        self.inputs.new("OctaneNormalNormalize", OctaneNormalNormalize.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneNormalNormalType,
    OctaneNormalCoordinateSystem,
    OctaneNormalNormalize,
    OctaneNormal,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
