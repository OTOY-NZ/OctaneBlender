##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCurvatureTextureCurvatureMode(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureCurvatureMode"
    bl_label="Mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=733)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 3),
        ("Concavity", "Concavity", "", 1),
        ("Convexity", "Convexity", "", 2),
    ]
    default_value: EnumProperty(default="Convexity", update=None, description="The type of curvature to sample", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureStrength(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=230)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Strength", min=0.100000, max=5.000000, soft_min=0.100000, soft_max=5.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureRadius(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureRadius"
    bl_label="Radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Specifies the maximum area affected by the curvature effect", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureDirtMap(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureDirtMap"
    bl_label="Radius map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=502)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Determines the proportion of the maximum area affected by the curvature effect", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.005000, update=None, description="Specifies the offset from the surface used to sample the neighbouring geometry", min=0.001000, max=0.100000, soft_min=0.001000, soft_max=0.100000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureTolerance(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureTolerance"
    bl_label="Tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="Tolerance for small curvature and small angles between polygons", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureSpread(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureSpread"
    bl_label="Spread"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Spread controls the ray direction with respect to the normal of the surface. 0 means curvature  is sampled straight in the direction of the surface normal, and 1 means the sampling rays  are shot perpendicular to the surface normal", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureObjectIncludeMode(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureObjectIncludeMode"
    bl_label="Include object mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=734)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", update=None, description="Includes objects when calculating the curvature value:  By default the selected mode is All, which includes all object intersections into calculating curvature. If Self is selected, then only self-intersection is taken into account for curvature. If Others is selected, then only ray-intersection with other objects is used for curvature", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTextureInvertNormal(OctaneBaseSocket):
    bl_idname="OctaneCurvatureTextureInvertNormal"
    bl_label="Invert normal"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=84)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert normal")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCurvatureTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCurvatureTexture"
    bl_label="Curvature texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=11000010
    octane_node_type: IntProperty(name="Octane Node Type", default=271)
    octane_socket_list: StringProperty(name="Socket List", default="Mode;Strength;Radius;Radius map;Offset;Tolerance;Spread;Include object mode;Invert normal;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    def init(self, context):
        self.inputs.new("OctaneCurvatureTextureCurvatureMode", OctaneCurvatureTextureCurvatureMode.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureStrength", OctaneCurvatureTextureStrength.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureRadius", OctaneCurvatureTextureRadius.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureDirtMap", OctaneCurvatureTextureDirtMap.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureOffset", OctaneCurvatureTextureOffset.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureTolerance", OctaneCurvatureTextureTolerance.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureSpread", OctaneCurvatureTextureSpread.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureObjectIncludeMode", OctaneCurvatureTextureObjectIncludeMode.bl_label).init()
        self.inputs.new("OctaneCurvatureTextureInvertNormal", OctaneCurvatureTextureInvertNormal.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneCurvatureTextureCurvatureMode,
    OctaneCurvatureTextureStrength,
    OctaneCurvatureTextureRadius,
    OctaneCurvatureTextureDirtMap,
    OctaneCurvatureTextureOffset,
    OctaneCurvatureTextureTolerance,
    OctaneCurvatureTextureSpread,
    OctaneCurvatureTextureObjectIncludeMode,
    OctaneCurvatureTextureInvertNormal,
    OctaneCurvatureTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
