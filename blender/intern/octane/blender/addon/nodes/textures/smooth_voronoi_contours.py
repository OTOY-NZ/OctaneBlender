##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneSmoothVoronoiContoursFrequency(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursFrequency"
    bl_label="Frequency"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=710)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=12.000000, update=None, description="Frequency", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursTime(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursTime"
    bl_label="Time"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Time", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursGlossy(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursGlossy"
    bl_label="Glossy"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=711)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Glossy")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursTransform(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContoursProjection(OctaneBaseSocket):
    bl_idname="OctaneSmoothVoronoiContoursProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type="OctaneMeshUVProjection"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSmoothVoronoiContours(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSmoothVoronoiContours"
    bl_label="Smooth Voronoi contours"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=260)
    octane_socket_list: StringProperty(name="Socket List", default="Frequency;Time;Glossy;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneSmoothVoronoiContoursFrequency", OctaneSmoothVoronoiContoursFrequency.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursTime", OctaneSmoothVoronoiContoursTime.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursGlossy", OctaneSmoothVoronoiContoursGlossy.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursTransform", OctaneSmoothVoronoiContoursTransform.bl_label).init()
        self.inputs.new("OctaneSmoothVoronoiContoursProjection", OctaneSmoothVoronoiContoursProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneSmoothVoronoiContoursFrequency,
    OctaneSmoothVoronoiContoursTime,
    OctaneSmoothVoronoiContoursGlossy,
    OctaneSmoothVoronoiContoursTransform,
    OctaneSmoothVoronoiContoursProjection,
    OctaneSmoothVoronoiContours,
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
