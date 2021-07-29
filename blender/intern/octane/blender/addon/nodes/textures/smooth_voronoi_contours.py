##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSmoothVoronoiContoursFrequency(OctaneBaseSocket):
    bl_idname = "OctaneSmoothVoronoiContoursFrequency"
    bl_label = "Frequency"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=710)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=12.000000, description="Frequency", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneSmoothVoronoiContoursTime(OctaneBaseSocket):
    bl_idname = "OctaneSmoothVoronoiContoursTime"
    bl_label = "Time"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Time", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneSmoothVoronoiContoursGlossy(OctaneBaseSocket):
    bl_idname = "OctaneSmoothVoronoiContoursGlossy"
    bl_label = "Glossy"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=711)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Glossy")

class OctaneSmoothVoronoiContoursTransform(OctaneBaseSocket):
    bl_idname = "OctaneSmoothVoronoiContoursTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSmoothVoronoiContoursProjection(OctaneBaseSocket):
    bl_idname = "OctaneSmoothVoronoiContoursProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneSmoothVoronoiContours(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSmoothVoronoiContours"
    bl_label = "Smooth Voronoi contours"
    octane_node_type: IntProperty(name="Octane Node Type", default=260)
    octane_socket_list: StringProperty(name="Socket List", default="Frequency;Time;Glossy;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSmoothVoronoiContoursFrequency", OctaneSmoothVoronoiContoursFrequency.bl_label)
        self.inputs.new("OctaneSmoothVoronoiContoursTime", OctaneSmoothVoronoiContoursTime.bl_label)
        self.inputs.new("OctaneSmoothVoronoiContoursGlossy", OctaneSmoothVoronoiContoursGlossy.bl_label)
        self.inputs.new("OctaneSmoothVoronoiContoursTransform", OctaneSmoothVoronoiContoursTransform.bl_label)
        self.inputs.new("OctaneSmoothVoronoiContoursProjection", OctaneSmoothVoronoiContoursProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneSmoothVoronoiContoursFrequency)
    register_class(OctaneSmoothVoronoiContoursTime)
    register_class(OctaneSmoothVoronoiContoursGlossy)
    register_class(OctaneSmoothVoronoiContoursTransform)
    register_class(OctaneSmoothVoronoiContoursProjection)
    register_class(OctaneSmoothVoronoiContours)

def unregister():
    unregister_class(OctaneSmoothVoronoiContours)
    unregister_class(OctaneSmoothVoronoiContoursProjection)
    unregister_class(OctaneSmoothVoronoiContoursTransform)
    unregister_class(OctaneSmoothVoronoiContoursGlossy)
    unregister_class(OctaneSmoothVoronoiContoursTime)
    unregister_class(OctaneSmoothVoronoiContoursFrequency)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
