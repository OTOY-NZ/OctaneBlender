##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMoireMosaicShape(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicShape"
    bl_label = "Shape"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=608)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Rectangle", "Rectangle", "", 0),
        ("Circle", "Circle", "", 1),
        ("Ring", "Ring", "", 2),
        ("Frame", "Frame", "", 3),
    ]
    default_value: EnumProperty(default="Ring", description="The type of the generated shapes", items=items)

class OctaneMoireMosaicSize(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicSize"
    bl_label = "Size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="The width/height or radius of the generated shapes", min=0.000000, max=4.000000, soft_min=0.000000, soft_max=4.000000, step=1, subtype="FACTOR")

class OctaneMoireMosaicRadius(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicRadius"
    bl_label = "Corner radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.100000, description="The corner radius (frame shape)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMoireMosaicBlur(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicBlur"
    bl_label = "Blur"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=715)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.100000, description="The blurriness of the lines (circle and ring shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMoireMosaicShift(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicShift"
    bl_label = "Shift"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=214)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="A horizontal shift applied to alternating rows (rectangle and circle shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMoireMosaicSpacing(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicSpacing"
    bl_label = "Ring spacing"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=717)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=7)
    default_value: FloatVectorProperty(default=(4.000000, 4.000000), description="The horizontal and vertical spacing between rings (ring and frame shapes)", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=2)

class OctaneMoireMosaicIterationCount(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicIterationCount"
    bl_label = "Iteration count"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=718)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="The number of iterations used by the shape generator (ring and frame shapes)", min=1, max=4, soft_min=1, soft_max=4, step=1, subtype="FACTOR")

class OctaneMoireMosaicTime(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicTime"
    bl_label = "Time"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.250000, description="The time in the generation sequence (ring and frame shapes)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneMoireMosaicTransform(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMoireMosaicProjection(OctaneBaseSocket):
    bl_idname = "OctaneMoireMosaicProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMoireMosaic(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMoireMosaic"
    bl_label = "Moire mosaic"
    octane_node_type: IntProperty(name="Octane Node Type", default=264)
    octane_socket_list: StringProperty(name="Socket List", default="Shape;Size;Corner radius;Blur;Shift;Ring spacing;Iteration count;Time;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMoireMosaicShape", OctaneMoireMosaicShape.bl_label)
        self.inputs.new("OctaneMoireMosaicSize", OctaneMoireMosaicSize.bl_label)
        self.inputs.new("OctaneMoireMosaicRadius", OctaneMoireMosaicRadius.bl_label)
        self.inputs.new("OctaneMoireMosaicBlur", OctaneMoireMosaicBlur.bl_label)
        self.inputs.new("OctaneMoireMosaicShift", OctaneMoireMosaicShift.bl_label)
        self.inputs.new("OctaneMoireMosaicSpacing", OctaneMoireMosaicSpacing.bl_label)
        self.inputs.new("OctaneMoireMosaicIterationCount", OctaneMoireMosaicIterationCount.bl_label)
        self.inputs.new("OctaneMoireMosaicTime", OctaneMoireMosaicTime.bl_label)
        self.inputs.new("OctaneMoireMosaicTransform", OctaneMoireMosaicTransform.bl_label)
        self.inputs.new("OctaneMoireMosaicProjection", OctaneMoireMosaicProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneMoireMosaicShape)
    register_class(OctaneMoireMosaicSize)
    register_class(OctaneMoireMosaicRadius)
    register_class(OctaneMoireMosaicBlur)
    register_class(OctaneMoireMosaicShift)
    register_class(OctaneMoireMosaicSpacing)
    register_class(OctaneMoireMosaicIterationCount)
    register_class(OctaneMoireMosaicTime)
    register_class(OctaneMoireMosaicTransform)
    register_class(OctaneMoireMosaicProjection)
    register_class(OctaneMoireMosaic)

def unregister():
    unregister_class(OctaneMoireMosaic)
    unregister_class(OctaneMoireMosaicProjection)
    unregister_class(OctaneMoireMosaicTransform)
    unregister_class(OctaneMoireMosaicTime)
    unregister_class(OctaneMoireMosaicIterationCount)
    unregister_class(OctaneMoireMosaicSpacing)
    unregister_class(OctaneMoireMosaicShift)
    unregister_class(OctaneMoireMosaicBlur)
    unregister_class(OctaneMoireMosaicRadius)
    unregister_class(OctaneMoireMosaicSize)
    unregister_class(OctaneMoireMosaicShape)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
