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


class OctaneSpotlightOrientation(OctaneBaseSocket):
    bl_idname="OctaneSpotlightOrientation"
    bl_label="Orientation"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=126)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="orientation")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Surface normal", "Surface normal", "", 1),
        ("Direction - world space", "Direction - world space", "", 2),
        ("Direction - object space", "Direction - object space", "", 3),
        ("Target point - world space", "Target point - world space", "", 4),
        ("Target point - object space", "Target point - object space", "", 5),
    ]
    default_value: EnumProperty(default="Direction - object space", update=OctaneBaseSocket.update_node_tree, description="Main axis for the emission cone", items=items)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpotlightTarget(OctaneBaseSocket):
    bl_idname="OctaneSpotlightTarget"
    bl_label="Direction or target"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="target")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, -1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Specify the direction or target point. Ignored if orientation is set to surface normal", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpotlightConeAngle(OctaneBaseSocket):
    bl_idname="OctaneSpotlightConeAngle"
    bl_label="Cone angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=562)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coneAngle")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=60.000000, update=OctaneBaseSocket.update_node_tree, description="Width of the cone angle in degrees", min=0.000000, max=180.000000, soft_min=0.000000, soft_max=180.000000, step=10, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpotlightHardness(OctaneBaseSocket):
    bl_idname="OctaneSpotlightHardness"
    bl_label="Hardness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=563)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="hardness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="Controls how abruptly the emission pattern falls of at the edge", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpotlightNormalize(OctaneBaseSocket):
    bl_idname="OctaneSpotlightNormalize"
    bl_label="Normalize power"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=118)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="normalize")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keep the emitted power constant if the angle changes")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSpotlight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSpotlight"
    bl_label="Spotlight"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=158)
    octane_socket_list: StringProperty(name="Socket List", default="Orientation;Direction or target;Cone angle;Hardness;Normalize power;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneSpotlightOrientation", OctaneSpotlightOrientation.bl_label).init()
        self.inputs.new("OctaneSpotlightTarget", OctaneSpotlightTarget.bl_label).init()
        self.inputs.new("OctaneSpotlightConeAngle", OctaneSpotlightConeAngle.bl_label).init()
        self.inputs.new("OctaneSpotlightHardness", OctaneSpotlightHardness.bl_label).init()
        self.inputs.new("OctaneSpotlightNormalize", OctaneSpotlightNormalize.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneSpotlightOrientation,
    OctaneSpotlightTarget,
    OctaneSpotlightConeAngle,
    OctaneSpotlightHardness,
    OctaneSpotlightNormalize,
    OctaneSpotlight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
