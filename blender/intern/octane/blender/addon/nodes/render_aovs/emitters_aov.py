##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneEmittersAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneEmittersAOVEnabled"
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

class OctaneEmittersAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneEmittersAOV"
    bl_label="Emitters AOV"
    bl_width_default=200
    octane_render_pass_id=1
    octane_render_pass_name="Emitters"
    octane_render_pass_short_name="Emit"
    octane_render_pass_description="Contains all samples where the camera ray hits an emitter"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=196)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctaneEmittersAOVEnabled", OctaneEmittersAOVEnabled.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneEmittersAOVEnabled,
    OctaneEmittersAOV,
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