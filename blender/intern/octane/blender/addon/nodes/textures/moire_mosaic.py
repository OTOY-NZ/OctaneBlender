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


class OctaneMoireMosaicShape(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicShape"
    bl_label="Shape"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=608)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="shape")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Rectangle", "Rectangle", "", 0),
        ("Circle", "Circle", "", 1),
        ("Ring", "Ring", "", 2),
        ("Frame", "Frame", "", 3),
    ]
    default_value: EnumProperty(default="Ring", update=OctaneBaseSocket.update_node_tree, description="The type of the generated shapes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicSize(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicSize"
    bl_label="Size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="size")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="The width/height or radius of the generated shapes", min=0.000000, max=4.000000, soft_min=0.000000, soft_max=4.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicRadius(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicRadius"
    bl_label="Corner radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="radius")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="The corner radius (frame shape)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicBlur(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicBlur"
    bl_label="Blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=715)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="blur")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="The blurriness of the lines (circle and ring shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicShift(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicShift"
    bl_label="Shift"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=214)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="shift")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="A horizontal shift applied to alternating rows (rectangle and circle shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicSpacing(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicSpacing"
    bl_label="Ring spacing"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=717)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="spacing")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(4.000000, 4.000000), update=OctaneBaseSocket.update_node_tree, description="The horizontal and vertical spacing between rings (ring and frame shapes)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicIterationCount(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicIterationCount"
    bl_label="Iteration count"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=718)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="iterationCount")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="The number of iterations used by the shape generator (ring and frame shapes)", min=1, max=4, soft_min=1, soft_max=4, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicTime(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="time")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.250000, update=OctaneBaseSocket.update_node_tree, description="The time in the generation sequence (ring and frame shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicTransform(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=67
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transform")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaicProjection(OctaneBaseSocket):
    bl_idname="OctaneMoireMosaicProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=78
    octane_default_node_name="OctaneMeshUVProjection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="projection")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMoireMosaic(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMoireMosaic"
    bl_label="Moire mosaic"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=264)
    octane_socket_list: StringProperty(name="Socket List", default="Shape;Size;Corner radius;Blur;Shift;Ring spacing;Iteration count;Time;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=10)

    def init(self, context):
        self.inputs.new("OctaneMoireMosaicShape", OctaneMoireMosaicShape.bl_label).init()
        self.inputs.new("OctaneMoireMosaicSize", OctaneMoireMosaicSize.bl_label).init()
        self.inputs.new("OctaneMoireMosaicRadius", OctaneMoireMosaicRadius.bl_label).init()
        self.inputs.new("OctaneMoireMosaicBlur", OctaneMoireMosaicBlur.bl_label).init()
        self.inputs.new("OctaneMoireMosaicShift", OctaneMoireMosaicShift.bl_label).init()
        self.inputs.new("OctaneMoireMosaicSpacing", OctaneMoireMosaicSpacing.bl_label).init()
        self.inputs.new("OctaneMoireMosaicIterationCount", OctaneMoireMosaicIterationCount.bl_label).init()
        self.inputs.new("OctaneMoireMosaicTime", OctaneMoireMosaicTime.bl_label).init()
        self.inputs.new("OctaneMoireMosaicTransform", OctaneMoireMosaicTransform.bl_label).init()
        self.inputs.new("OctaneMoireMosaicProjection", OctaneMoireMosaicProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneMoireMosaicShape,
    OctaneMoireMosaicSize,
    OctaneMoireMosaicRadius,
    OctaneMoireMosaicBlur,
    OctaneMoireMosaicShift,
    OctaneMoireMosaicSpacing,
    OctaneMoireMosaicIterationCount,
    OctaneMoireMosaicTime,
    OctaneMoireMosaicTransform,
    OctaneMoireMosaicProjection,
    OctaneMoireMosaic,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
