##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneNormalShadingAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneNormalShadingAOVEnabled"
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

class OctaneNormalShadingAOVBump(OctaneBaseSocket):
    bl_idname="OctaneNormalShadingAOVBump"
    bl_label="Bump and normal mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Take bump and normal mapping into account for shading normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNormalShadingAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNormalShadingAOV"
    bl_label="Normal (shading) AOV"
    bl_width_default=200
    octane_render_pass_id=1001
    octane_render_pass_name="Normal (shading)"
    octane_render_pass_short_name="ShN"
    octane_render_pass_description="Assigns a color for the shading normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=236)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Bump and normal mapping;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneNormalShadingAOVEnabled", OctaneNormalShadingAOVEnabled.bl_label).init()
        self.inputs.new("OctaneNormalShadingAOVBump", OctaneNormalShadingAOVBump.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneNormalShadingAOVEnabled,
    OctaneNormalShadingAOVBump,
    OctaneNormalShadingAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

class OctaneShadingNormalAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneShadingNormalAOVEnabled"
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

class OctaneShadingNormalAOVBump(OctaneBaseSocket):
    bl_idname="OctaneShadingNormalAOVBump"
    bl_label="Bump and normal mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Take bump and normal mapping into account for shading normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneShadingNormalAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneShadingNormalAOV"
    bl_label="Shading normal AOV"
    bl_width_default=200
    octane_render_pass_id=1001
    octane_render_pass_name="Shading normal"
    octane_render_pass_short_name="ShN"
    octane_render_pass_description="Assigns a color for the shading normal at the position hit by the camera ray"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=236)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Bump and normal mapping;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneShadingNormalAOVEnabled", OctaneShadingNormalAOVEnabled.bl_label).init()
        self.inputs.new("OctaneShadingNormalAOVBump", OctaneShadingNormalAOVBump.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_LEGACY_CLASSES=[
    OctaneShadingNormalAOVEnabled,
    OctaneShadingNormalAOVBump,
    OctaneShadingNormalAOV,
]

_CLASSES.extend(_LEGACY_CLASSES)