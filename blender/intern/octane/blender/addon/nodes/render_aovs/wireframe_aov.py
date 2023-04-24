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


class OctaneWireframeAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneWireframeAOVEnabled"
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

class OctaneWireframeAOVShadingEnabled(OctaneBaseSocket):
    bl_idname="OctaneWireframeAOVShadingEnabled"
    bl_label="Enable shading"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=736)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, the wireframe will be rendered on slightly shaded objects")
    octane_hide_value=False
    octane_min_version=11000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWireframeAOVBump(OctaneBaseSocket):
    bl_idname="OctaneWireframeAOVBump"
    bl_label="Bump and normal mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Take bump and normal mapping into account for wireframe shading (if shading is enabled)")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWireframeAOVHighlightBackfaces(OctaneBaseSocket):
    bl_idname="OctaneWireframeAOVHighlightBackfaces"
    bl_label="Highlight backfaces"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=72)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled, the backfaces will be tinted red")
    octane_hide_value=False
    octane_min_version=11000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWireframeAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneWireframeAOV"
    bl_label="Wireframe AOV"
    bl_width_default=200
    octane_render_pass_id=1007
    octane_render_pass_name="Wireframe"
    octane_render_pass_short_name="Wire"
    octane_render_pass_description="Wireframe display of the geometry"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=254)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Enable shading;Bump and normal mapping;Highlight backfaces;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneWireframeAOVEnabled", OctaneWireframeAOVEnabled.bl_label).init()
        self.inputs.new("OctaneWireframeAOVShadingEnabled", OctaneWireframeAOVShadingEnabled.bl_label).init()
        self.inputs.new("OctaneWireframeAOVBump", OctaneWireframeAOVBump.bl_label).init()
        self.inputs.new("OctaneWireframeAOVHighlightBackfaces", OctaneWireframeAOVHighlightBackfaces.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneWireframeAOVEnabled,
    OctaneWireframeAOVShadingEnabled,
    OctaneWireframeAOVBump,
    OctaneWireframeAOVHighlightBackfaces,
    OctaneWireframeAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
