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


class OctaneRenderLayerEnabled(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerEnabled"
    bl_label="Enable"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="enabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Tick to enable render layers")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderLayerLayerId(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerLayerId"
    bl_label="Active layer ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=92)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="layerId")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the active render layer", min=1, max=255, soft_min=1, soft_max=255, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderLayerInvert(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="invert")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="All the non-active render layers become the active render layer and the active render layer becomes inactive")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderLayerMode(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=324)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="mode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Normal", "Normal", "", 0),
        ("Hide inactive layers", "Hide inactive layers", "", 1),
        ("Hide from camera", "Hide from camera", "", 3),
        ("Only side effects", "Only side effects", "", 2),
    ]
    default_value: EnumProperty(default="Normal", update=OctaneBaseSocket.update_node_tree, description="The render mode that should be used to render layers:\n\n'Normal': The beauty passes contain the active layer only and the render layer passes (shadows, reflections...) record the side-effects of the active render layer for those samples/pixels that are not obstructed by the active render layer.\nBeauty passes will be transparent for those pixels which are covered by objects on the inactive layers, even if there is an object on the active layer behind the foreground object.\n\n'Hide inactive layers': All geometry that is not on an active layer will be made invisible. No side effects will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n\n'Only side effects': Similar to 'normal', with the exception that the active layer will be made invisible to the camera, i.e. the beauty passes will be empty. The render layer passes (shadows, reflections...) still record the side-effects of the active render layer.\nThis is useful to capture all side-effects without having the active layer obstructing those.\n'Hide from camera': Similar to RENDER_LAYER_MODE_HIDE_INACTIVE_LAYERs All geometry that is not on an active layer will be made invisible. But side effects(shadows, reflections...)will be recorded in the render layer passes", items=items)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderLayerVisibilityOnly(OctaneBaseSocket):
    bl_idname="OctaneRenderLayerVisibilityOnly"
    bl_label="Visibility only"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=253)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="visibilityOnly")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="The layers only affect visibility i.e. objects on the non-active layer are treated as if they are not in the scene at all. Render layer passes don't work if this option is enabled")
    octane_hide_value=False
    octane_min_version=2210000
    octane_end_version=3030005
    octane_deprecated=True

class OctaneRenderLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderLayer"
    bl_label="Render layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=90)
    octane_socket_list: StringProperty(name="Socket List", default="Enable;Active layer ID;Invert;Mode;Visibility only;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneRenderLayerEnabled", OctaneRenderLayerEnabled.bl_label).init()
        self.inputs.new("OctaneRenderLayerLayerId", OctaneRenderLayerLayerId.bl_label).init()
        self.inputs.new("OctaneRenderLayerInvert", OctaneRenderLayerInvert.bl_label).init()
        self.inputs.new("OctaneRenderLayerMode", OctaneRenderLayerMode.bl_label).init()
        self.inputs.new("OctaneRenderLayerVisibilityOnly", OctaneRenderLayerVisibilityOnly.bl_label).init()
        self.outputs.new("OctaneRenderLayerOutSocket", "Render layer out").init()


_CLASSES=[
    OctaneRenderLayerEnabled,
    OctaneRenderLayerLayerId,
    OctaneRenderLayerInvert,
    OctaneRenderLayerMode,
    OctaneRenderLayerVisibilityOnly,
    OctaneRenderLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
