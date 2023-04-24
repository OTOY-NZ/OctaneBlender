##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneNullMaterialMedium(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialMedium"
    bl_label="Medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialOpacity(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialOpacity"
    bl_label="Opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialRefractionAlpha"
    bl_label="Affect alpha"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=146)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Enable to have refractions affect the alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialSmooth(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialSmooth"
    bl_label="Smooth"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If disabled normal interpolation will be disabled and triangle meshes will appear \"facetted\"")
    octane_hide_value=False
    octane_min_version=10020200
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialSmoothShadowTerminator"
    bl_label="Smooth shadow terminator"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")
    octane_hide_value=False
    octane_min_version=11000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialRoundEdges(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialRoundEdges"
    bl_label="Round edges"
    color=consts.OctanePinColor.RoundEdges
    octane_default_node_type="OctaneRoundEdges"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneNullMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=10021300
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNullMaterialGroupTransmissionProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneNullMaterialGroupTransmissionProperties"
    bl_label="[OctaneGroupTitle]Transmission Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Medium;Opacity;Affect alpha;")

class OctaneNullMaterialGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneNullMaterialGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")

class OctaneNullMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNullMaterial"
    bl_label="Null material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=159)
    octane_socket_list: StringProperty(name="Socket List", default="Medium;Opacity;Affect alpha;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneNullMaterialGroupTransmissionProperties", OctaneNullMaterialGroupTransmissionProperties.bl_label).init()
        self.inputs.new("OctaneNullMaterialMedium", OctaneNullMaterialMedium.bl_label).init()
        self.inputs.new("OctaneNullMaterialOpacity", OctaneNullMaterialOpacity.bl_label).init()
        self.inputs.new("OctaneNullMaterialRefractionAlpha", OctaneNullMaterialRefractionAlpha.bl_label).init()
        self.inputs.new("OctaneNullMaterialGroupGeometryProperties", OctaneNullMaterialGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneNullMaterialDisplacement", OctaneNullMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneNullMaterialSmooth", OctaneNullMaterialSmooth.bl_label).init()
        self.inputs.new("OctaneNullMaterialSmoothShadowTerminator", OctaneNullMaterialSmoothShadowTerminator.bl_label).init()
        self.inputs.new("OctaneNullMaterialRoundEdges", OctaneNullMaterialRoundEdges.bl_label).init()
        self.inputs.new("OctaneNullMaterialPriority", OctaneNullMaterialPriority.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_CLASSES=[
    OctaneNullMaterialMedium,
    OctaneNullMaterialOpacity,
    OctaneNullMaterialRefractionAlpha,
    OctaneNullMaterialDisplacement,
    OctaneNullMaterialSmooth,
    OctaneNullMaterialSmoothShadowTerminator,
    OctaneNullMaterialRoundEdges,
    OctaneNullMaterialPriority,
    OctaneNullMaterialGroupTransmissionProperties,
    OctaneNullMaterialGroupGeometryProperties,
    OctaneNullMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
