##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneToonMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialDiffuse"
    bl_label = "Diffuse"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneToonMaterialSpecular(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialSpecular"
    bl_label = "Specular"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=222)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specular reflection channel which behaves like a coating on top of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneToonMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.063200, description="Roughness of the specular reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneToonMaterialToonLightMode(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialToonLightMode"
    bl_label = "Toon lighting mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=367)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Toon lights", "Toon lights", "", 0),
        ("Camera light", "Camera light", "", 1),
    ]
    default_value: EnumProperty(default="Toon lights", description="The assumed source of light for this toon material", items=items)

class OctaneToonMaterialToonDiffuseRamp(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialToonDiffuseRamp"
    bl_label = "Toon Diffuse Ramp"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=364)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=30)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneToonMaterialToonSpecularRamp(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialToonSpecularRamp"
    bl_label = "Toon Specular Ramp"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=366)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=30)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneToonMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneToonMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneToonMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneToonMaterialOutlineColor(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialOutlineColor"
    bl_label = "Outline Color"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=365)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Outline Color", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneToonMaterialWidth(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialWidth"
    bl_label = "Outline Thickness"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=256)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.300000, description="Outline Thickness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneToonMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneToonMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneToonMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneToonMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneToonMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialCustomAov"
    bl_label = "Custom AOV"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)

class OctaneToonMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneToonMaterialCustomAovChannel"
    bl_label = "Custom AOV channel"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)

class OctaneToonMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneToonMaterial"
    bl_label = "Toon material"
    octane_node_type: IntProperty(name="Octane Node Type", default=121)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Specular;Roughness;Toon lighting mode;Toon Diffuse Ramp;Toon Specular Ramp;Bump;Normal;Displacement;Outline Color;Outline Thickness;Opacity;Smooth;Smooth shadow terminator;Round edges;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneToonMaterialDiffuse", OctaneToonMaterialDiffuse.bl_label)
        self.inputs.new("OctaneToonMaterialSpecular", OctaneToonMaterialSpecular.bl_label)
        self.inputs.new("OctaneToonMaterialRoughness", OctaneToonMaterialRoughness.bl_label)
        self.inputs.new("OctaneToonMaterialToonLightMode", OctaneToonMaterialToonLightMode.bl_label)
        self.inputs.new("OctaneToonMaterialToonDiffuseRamp", OctaneToonMaterialToonDiffuseRamp.bl_label)
        self.inputs.new("OctaneToonMaterialToonSpecularRamp", OctaneToonMaterialToonSpecularRamp.bl_label)
        self.inputs.new("OctaneToonMaterialBump", OctaneToonMaterialBump.bl_label)
        self.inputs.new("OctaneToonMaterialNormal", OctaneToonMaterialNormal.bl_label)
        self.inputs.new("OctaneToonMaterialDisplacement", OctaneToonMaterialDisplacement.bl_label)
        self.inputs.new("OctaneToonMaterialOutlineColor", OctaneToonMaterialOutlineColor.bl_label)
        self.inputs.new("OctaneToonMaterialWidth", OctaneToonMaterialWidth.bl_label)
        self.inputs.new("OctaneToonMaterialOpacity", OctaneToonMaterialOpacity.bl_label)
        self.inputs.new("OctaneToonMaterialSmooth", OctaneToonMaterialSmooth.bl_label)
        self.inputs.new("OctaneToonMaterialSmoothShadowTerminator", OctaneToonMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneToonMaterialRoundEdges", OctaneToonMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneToonMaterialCustomAov", OctaneToonMaterialCustomAov.bl_label)
        self.inputs.new("OctaneToonMaterialCustomAovChannel", OctaneToonMaterialCustomAovChannel.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneToonMaterialDiffuse)
    register_class(OctaneToonMaterialSpecular)
    register_class(OctaneToonMaterialRoughness)
    register_class(OctaneToonMaterialToonLightMode)
    register_class(OctaneToonMaterialToonDiffuseRamp)
    register_class(OctaneToonMaterialToonSpecularRamp)
    register_class(OctaneToonMaterialBump)
    register_class(OctaneToonMaterialNormal)
    register_class(OctaneToonMaterialDisplacement)
    register_class(OctaneToonMaterialOutlineColor)
    register_class(OctaneToonMaterialWidth)
    register_class(OctaneToonMaterialOpacity)
    register_class(OctaneToonMaterialSmooth)
    register_class(OctaneToonMaterialSmoothShadowTerminator)
    register_class(OctaneToonMaterialRoundEdges)
    register_class(OctaneToonMaterialCustomAov)
    register_class(OctaneToonMaterialCustomAovChannel)
    register_class(OctaneToonMaterial)

def unregister():
    unregister_class(OctaneToonMaterial)
    unregister_class(OctaneToonMaterialCustomAovChannel)
    unregister_class(OctaneToonMaterialCustomAov)
    unregister_class(OctaneToonMaterialRoundEdges)
    unregister_class(OctaneToonMaterialSmoothShadowTerminator)
    unregister_class(OctaneToonMaterialSmooth)
    unregister_class(OctaneToonMaterialOpacity)
    unregister_class(OctaneToonMaterialWidth)
    unregister_class(OctaneToonMaterialOutlineColor)
    unregister_class(OctaneToonMaterialDisplacement)
    unregister_class(OctaneToonMaterialNormal)
    unregister_class(OctaneToonMaterialBump)
    unregister_class(OctaneToonMaterialToonSpecularRamp)
    unregister_class(OctaneToonMaterialToonDiffuseRamp)
    unregister_class(OctaneToonMaterialToonLightMode)
    unregister_class(OctaneToonMaterialRoughness)
    unregister_class(OctaneToonMaterialSpecular)
    unregister_class(OctaneToonMaterialDiffuse)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
