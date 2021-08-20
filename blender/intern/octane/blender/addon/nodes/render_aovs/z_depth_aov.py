##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneZDepthAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneZDepthAOVEnabled"
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

class OctaneZDepthAOVZDepthMax(OctaneBaseSocket):
    bl_idname="OctaneZDepthAOVZDepthMax"
    bl_label="Maximum Z-depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=257)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=5.000000, update=None, description="The maximum Z-depth value. Background pixels will get this value and and any foreground depths will be clamped at this value. This applies with or without tone mapping, but tone mapping will map the maximum Z-depth to white (0 is mapped to black)", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneZDepthAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneZDepthAOV"
    bl_label="Z-depth AOV"
    bl_width_default=200
    octane_render_pass_id=1003
    octane_render_pass_name="Z-depth"
    octane_render_pass_short_name="Z"
    octane_render_pass_description="Assigns a gray value proportional to the camera ray hit distance"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=255)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Maximum Z-depth;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneZDepthAOVEnabled", OctaneZDepthAOVEnabled.bl_label).init()
        self.inputs.new("OctaneZDepthAOVZDepthMax", OctaneZDepthAOVZDepthMax.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneZDepthAOVEnabled,
    OctaneZDepthAOVZDepthMax,
    OctaneZDepthAOV,
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
