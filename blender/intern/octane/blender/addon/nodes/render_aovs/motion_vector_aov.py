##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneMotionVectorAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneMotionVectorAOVEnabled"
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

class OctaneMotionVectorAOVMaxSpeed(OctaneBaseSocket):
    bl_idname="OctaneMotionVectorAOVMaxSpeed"
    bl_label="Max speed"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=109)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Upper limit of the motion vector which will become 1, when the motion vector pass is imaged. The unit of the motion vector is pixels", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMotionVectorAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMotionVectorAOV"
    bl_label="Motion vector AOV"
    bl_width_default=200
    octane_render_pass_id=1011
    octane_render_pass_name="Motion vector"
    octane_render_pass_short_name="MV"
    octane_render_pass_description="Renders the motion vectors as 2D vectors in screen space.\nThe X coordinate (stored in the red channel) is the motion to the right in pixels.\nThe Y coordinate (stored in the green channel) is the motion up in pixels.\nWhen enabled, rendering of motion blur is disabled"
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=211)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Max speed;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    def init(self, context):
        self.inputs.new("OctaneMotionVectorAOVEnabled", OctaneMotionVectorAOVEnabled.bl_label).init()
        self.inputs.new("OctaneMotionVectorAOVMaxSpeed", OctaneMotionVectorAOVMaxSpeed.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneMotionVectorAOVEnabled,
    OctaneMotionVectorAOVMaxSpeed,
    OctaneMotionVectorAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
