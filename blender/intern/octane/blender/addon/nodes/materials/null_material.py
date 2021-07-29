##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneNullMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneNullMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneNullMaterialRefractionAlpha(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialRefractionAlpha"
    bl_label = "Affect alpha"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=146)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable to have refractions affect the alpha channel")

class OctaneNullMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneNullMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneNullMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneNullMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneNullMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneNullMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneNullMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneNullMaterial"
    bl_label = "Null material"
    octane_node_type: IntProperty(name="Octane Node Type", default=159)
    octane_socket_list: StringProperty(name="Socket List", default="Medium;Opacity;Affect alpha;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneNullMaterialMedium", OctaneNullMaterialMedium.bl_label)
        self.inputs.new("OctaneNullMaterialOpacity", OctaneNullMaterialOpacity.bl_label)
        self.inputs.new("OctaneNullMaterialRefractionAlpha", OctaneNullMaterialRefractionAlpha.bl_label)
        self.inputs.new("OctaneNullMaterialDisplacement", OctaneNullMaterialDisplacement.bl_label)
        self.inputs.new("OctaneNullMaterialSmooth", OctaneNullMaterialSmooth.bl_label)
        self.inputs.new("OctaneNullMaterialSmoothShadowTerminator", OctaneNullMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneNullMaterialRoundEdges", OctaneNullMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneNullMaterialPriority", OctaneNullMaterialPriority.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneNullMaterialMedium)
    register_class(OctaneNullMaterialOpacity)
    register_class(OctaneNullMaterialRefractionAlpha)
    register_class(OctaneNullMaterialDisplacement)
    register_class(OctaneNullMaterialSmooth)
    register_class(OctaneNullMaterialSmoothShadowTerminator)
    register_class(OctaneNullMaterialRoundEdges)
    register_class(OctaneNullMaterialPriority)
    register_class(OctaneNullMaterial)

def unregister():
    unregister_class(OctaneNullMaterial)
    unregister_class(OctaneNullMaterialPriority)
    unregister_class(OctaneNullMaterialRoundEdges)
    unregister_class(OctaneNullMaterialSmoothShadowTerminator)
    unregister_class(OctaneNullMaterialSmooth)
    unregister_class(OctaneNullMaterialDisplacement)
    unregister_class(OctaneNullMaterialRefractionAlpha)
    unregister_class(OctaneNullMaterialOpacity)
    unregister_class(OctaneNullMaterialMedium)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
