##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneFalloffMapMode(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=324)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Normal vs. eye ray", "Normal vs. eye ray", "", 0),
        ("Normal vs. vector 90deg", "Normal vs. vector 90deg", "", 1),
        ("Normal vs. vector 180deg", "Normal vs. vector 180deg", "", 2),
    ]
    default_value: EnumProperty(default="Normal vs. eye ray", update=None, description="The falloff mode that should be used:\n\n'Normal vs. eye ray': The falloff is calculated from the angle between the surface normal and the eye ray.\n'Normal vs. vector 90deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 90 degrees.\n'Normal vs vector 180deg': The falloff is calculated from the angle between the surface normal and the specified direction vector maxing out at 180 degrees", items=items)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapNormal(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapNormal"
    bl_label="Minimum value"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Value if the angle between the two directions is 0", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapGrazing(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapGrazing"
    bl_label="Maximum value"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=68)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Value if the angle between the two directions is at the maximum", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapFalloffIndex(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapFalloffIndex"
    bl_label="Falloff skew factor"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=47)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=6.000000, update=None, description="Skew factor for the falloff curve", min=0.100000, max=15.000000, soft_min=0.100000, soft_max=15.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMapDirection(OctaneBaseSocket):
    bl_idname="OctaneFalloffMapDirection"
    bl_label="Falloff direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=327)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=None, description="The direction vector that is used by some of the falloff modes", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneFalloffMap(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneFalloffMap"
    bl_label="Falloff map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=50)
    octane_socket_list: StringProperty(name="Socket List", default="Mode;Minimum value;Maximum value;Falloff skew factor;Falloff direction;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneFalloffMapMode", OctaneFalloffMapMode.bl_label).init()
        self.inputs.new("OctaneFalloffMapNormal", OctaneFalloffMapNormal.bl_label).init()
        self.inputs.new("OctaneFalloffMapGrazing", OctaneFalloffMapGrazing.bl_label).init()
        self.inputs.new("OctaneFalloffMapFalloffIndex", OctaneFalloffMapFalloffIndex.bl_label).init()
        self.inputs.new("OctaneFalloffMapDirection", OctaneFalloffMapDirection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_classes=[
    OctaneFalloffMapMode,
    OctaneFalloffMapNormal,
    OctaneFalloffMapGrazing,
    OctaneFalloffMapFalloffIndex,
    OctaneFalloffMapDirection,
    OctaneFalloffMap,
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
