##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRelativeDistanceDistanceMode(OctaneBaseSocket):
    bl_idname="OctaneRelativeDistanceDistanceMode"
    bl_label="Distance mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=646)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Distance", "Distance", "", 0),
        ("X-axis offset", "X-axis offset", "", 1),
        ("Y-axis offset", "Y-axis offset", "", 2),
        ("Z-axis offset", "Z-axis offset", "", 3),
    ]
    default_value: EnumProperty(default="Distance", update=None, description="Defines how the distance metric is computed", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRelativeDistanceTransform(OctaneBaseSocket):
    bl_idname="OctaneRelativeDistanceTransform"
    bl_label="Reference transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRelativeDistanceUseFullTransform(OctaneBaseSocket):
    bl_idname="OctaneRelativeDistanceUseFullTransform"
    bl_label="Use full transform"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=647)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If checked the distance metric is computed in the space of the reference transform, including rotation and scale.\nOtherwise only the position is taken into account")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRelativeDistanceNormalize(OctaneBaseSocket):
    bl_idname="OctaneRelativeDistanceNormalize"
    bl_label="Normalize result"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Whether the result should be remapped to the [0..1] range")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRelativeDistanceNormalizationRange(OctaneBaseSocket):
    bl_idname="OctaneRelativeDistanceNormalizationRange"
    bl_label="Normalization range"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=640)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000), update=None, description="Min and max values used for normalization", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRelativeDistance(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRelativeDistance"
    bl_label="Relative distance"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=329)
    octane_socket_list: StringProperty(name="Socket List", default="Distance mode;Reference transform;Use full transform;Normalize result;Normalization range;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneRelativeDistanceDistanceMode", OctaneRelativeDistanceDistanceMode.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceTransform", OctaneRelativeDistanceTransform.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceUseFullTransform", OctaneRelativeDistanceUseFullTransform.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceNormalize", OctaneRelativeDistanceNormalize.bl_label).init()
        self.inputs.new("OctaneRelativeDistanceNormalizationRange", OctaneRelativeDistanceNormalizationRange.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneRelativeDistanceDistanceMode,
    OctaneRelativeDistanceTransform,
    OctaneRelativeDistanceUseFullTransform,
    OctaneRelativeDistanceNormalize,
    OctaneRelativeDistanceNormalizationRange,
    OctaneRelativeDistance,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
