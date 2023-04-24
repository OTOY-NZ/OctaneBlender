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


class OctaneGradientGeneratorGradientType(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorGradientType"
    bl_label="Gradient type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=667)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Linear", "Linear", "", 0),
        ("Radial", "Radial", "", 1),
        ("Angular", "Angular", "", 2),
        ("Polygonal", "Polygonal", "", 3),
        ("Spiral", "Spiral", "", 4),
    ]
    default_value: EnumProperty(default="Linear", update=None, description="Type of gradient generated", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorRepetitions(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorRepetitions"
    bl_label="Repetitions"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=659)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Number of times the gradient is repeated", min=1.000000, max=20.000000, soft_min=1.000000, soft_max=20.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorPolygonSides(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorPolygonSides"
    bl_label="Polygon sides"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=660)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=None, description="Number of sides to the polygon when using the polygonal gradient type", min=3, max=20, soft_min=3, soft_max=20, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorGamma(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=2.200000, update=None, description="Gamma correction coefficient", min=0.100000, max=8.000000, soft_min=0.100000, soft_max=8.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorInvert(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert the output color")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorTransform(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorProjection(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGeneratorBorderMode(OctaneBaseSocket):
    bl_idname="OctaneGradientGeneratorBorderMode"
    bl_label="Repetition mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=15)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Wrap around", "Wrap around", "", 0),
        ("Mirror", "Mirror", "", 4),
        ("Black color", "Black color", "", 1),
        ("White color", "White color", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="Wrap around", update=None, description="Determines the gradient behavior for repetitions", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGradientGenerator(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGradientGenerator"
    bl_label="Gradient generator"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=332)
    octane_socket_list: StringProperty(name="Socket List", default="Gradient type;Repetitions;Polygon sides;Gamma;Invert;UVW transform;Projection;Repetition mode;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneGradientGeneratorGradientType", OctaneGradientGeneratorGradientType.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorRepetitions", OctaneGradientGeneratorRepetitions.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorPolygonSides", OctaneGradientGeneratorPolygonSides.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorGamma", OctaneGradientGeneratorGamma.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorInvert", OctaneGradientGeneratorInvert.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorTransform", OctaneGradientGeneratorTransform.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorProjection", OctaneGradientGeneratorProjection.bl_label).init()
        self.inputs.new("OctaneGradientGeneratorBorderMode", OctaneGradientGeneratorBorderMode.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneGradientGeneratorGradientType,
    OctaneGradientGeneratorRepetitions,
    OctaneGradientGeneratorPolygonSides,
    OctaneGradientGeneratorGamma,
    OctaneGradientGeneratorInvert,
    OctaneGradientGeneratorTransform,
    OctaneGradientGeneratorProjection,
    OctaneGradientGeneratorBorderMode,
    OctaneGradientGenerator,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
