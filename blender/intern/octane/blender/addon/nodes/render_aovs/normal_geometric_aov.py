##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneNormalGeometricAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneNormalGeometricAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormalGeometricAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNormalGeometricAOV"
    bl_label="Normal (geometric) AOV"
    bl_width_default=200
    octane_render_pass_id=1000
    octane_render_pass_name="Normal (geometric)"
    octane_render_pass_short_name="GN"
    octane_render_pass_description="Assigns a color for the geometry normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=198)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctaneNormalGeometricAOVEnabled", OctaneNormalGeometricAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneNormalGeometricAOVEnabled,
    OctaneNormalGeometricAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneGeometricNormalAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneGeometricNormalAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometricNormalAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGeometricNormalAOV"
    bl_label="Geometric normal AOV"
    bl_width_default=200
    octane_render_pass_id=1000
    octane_render_pass_name="Geometric normal"
    octane_render_pass_short_name="GN"
    octane_render_pass_description="Assigns a color for the geometry normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=198)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctaneGeometricNormalAOVEnabled", OctaneGeometricNormalAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()

_LEGACY_CLASSES=[
    OctaneGeometricNormalAOVEnabled,
    OctaneGeometricNormalAOV,
]

_CLASSES.extend(_LEGACY_CLASSES)
