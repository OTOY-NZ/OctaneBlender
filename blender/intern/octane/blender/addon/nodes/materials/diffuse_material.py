##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDiffuseMaterialDiffuse(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialDiffuse"
    bl_label = "Diffuse"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=30)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), description="Diffuse reflection channel", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)

class OctaneDiffuseMaterialTransmission(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialTransmission"
    bl_label = "Transmission"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=245)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseMaterialRoughness(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialRoughness"
    bl_label = "Roughness"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=204)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Diffuse roughness to allow simulation of very rough surfaces like sand or clay", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDiffuseMaterialMedium(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialMedium"
    bl_label = "Medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDiffuseMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the material via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDiffuseMaterialBump(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialBump"
    bl_label = "Bump"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseMaterialNormal(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialNormal"
    bl_label = "Normal"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDiffuseMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDiffuseMaterialSmooth(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialSmooth"
    bl_label = "Smooth"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If disabled normal interpolation will be disabled and triangle meshes will appear 'facetted'")

class OctaneDiffuseMaterialSmoothShadowTerminator(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialSmoothShadowTerminator"
    bl_label = "Smooth shadow terminator"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=731)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled self-intersecting shadow terminator for low polygon is smoothed according to the polygon's curvature")

class OctaneDiffuseMaterialRoundEdges(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialRoundEdges"
    bl_label = "Round edges"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=467)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=32)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDiffuseMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneDiffuseMaterialEmission(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialEmission"
    bl_label = "Emission"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=41)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=6)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDiffuseMaterialMatte(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialMatte"
    bl_label = "Shadow catcher"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=102)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Switches the material to a shadow catcher, i.e. it will be transparent unless there is some (direct) shadow cast onto the material, which will make it less transparent depending on the shadow strength")

class OctaneDiffuseMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialCustomAov"
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

class OctaneDiffuseMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialCustomAovChannel"
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

class OctaneDiffuseMaterialLayer(OctaneBaseSocket):
    bl_idname = "OctaneDiffuseMaterialLayer"
    bl_label = "Material layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=474)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=33)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDiffuseMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDiffuseMaterial"
    bl_label = "Diffuse material"
    octane_node_type: IntProperty(name="Octane Node Type", default=17)
    octane_socket_list: StringProperty(name="Socket List", default="Diffuse;Transmission;Roughness;Medium;Opacity;Bump;Normal;Displacement;Smooth;Smooth shadow terminator;Round edges;Priority;Emission;Shadow catcher;Custom AOV;Custom AOV channel;Material layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDiffuseMaterialDiffuse", OctaneDiffuseMaterialDiffuse.bl_label)
        self.inputs.new("OctaneDiffuseMaterialTransmission", OctaneDiffuseMaterialTransmission.bl_label)
        self.inputs.new("OctaneDiffuseMaterialRoughness", OctaneDiffuseMaterialRoughness.bl_label)
        self.inputs.new("OctaneDiffuseMaterialMedium", OctaneDiffuseMaterialMedium.bl_label)
        self.inputs.new("OctaneDiffuseMaterialOpacity", OctaneDiffuseMaterialOpacity.bl_label)
        self.inputs.new("OctaneDiffuseMaterialBump", OctaneDiffuseMaterialBump.bl_label)
        self.inputs.new("OctaneDiffuseMaterialNormal", OctaneDiffuseMaterialNormal.bl_label)
        self.inputs.new("OctaneDiffuseMaterialDisplacement", OctaneDiffuseMaterialDisplacement.bl_label)
        self.inputs.new("OctaneDiffuseMaterialSmooth", OctaneDiffuseMaterialSmooth.bl_label)
        self.inputs.new("OctaneDiffuseMaterialSmoothShadowTerminator", OctaneDiffuseMaterialSmoothShadowTerminator.bl_label)
        self.inputs.new("OctaneDiffuseMaterialRoundEdges", OctaneDiffuseMaterialRoundEdges.bl_label)
        self.inputs.new("OctaneDiffuseMaterialPriority", OctaneDiffuseMaterialPriority.bl_label)
        self.inputs.new("OctaneDiffuseMaterialEmission", OctaneDiffuseMaterialEmission.bl_label)
        self.inputs.new("OctaneDiffuseMaterialMatte", OctaneDiffuseMaterialMatte.bl_label)
        self.inputs.new("OctaneDiffuseMaterialCustomAov", OctaneDiffuseMaterialCustomAov.bl_label)
        self.inputs.new("OctaneDiffuseMaterialCustomAovChannel", OctaneDiffuseMaterialCustomAovChannel.bl_label)
        self.inputs.new("OctaneDiffuseMaterialLayer", OctaneDiffuseMaterialLayer.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneDiffuseMaterialDiffuse)
    register_class(OctaneDiffuseMaterialTransmission)
    register_class(OctaneDiffuseMaterialRoughness)
    register_class(OctaneDiffuseMaterialMedium)
    register_class(OctaneDiffuseMaterialOpacity)
    register_class(OctaneDiffuseMaterialBump)
    register_class(OctaneDiffuseMaterialNormal)
    register_class(OctaneDiffuseMaterialDisplacement)
    register_class(OctaneDiffuseMaterialSmooth)
    register_class(OctaneDiffuseMaterialSmoothShadowTerminator)
    register_class(OctaneDiffuseMaterialRoundEdges)
    register_class(OctaneDiffuseMaterialPriority)
    register_class(OctaneDiffuseMaterialEmission)
    register_class(OctaneDiffuseMaterialMatte)
    register_class(OctaneDiffuseMaterialCustomAov)
    register_class(OctaneDiffuseMaterialCustomAovChannel)
    register_class(OctaneDiffuseMaterialLayer)
    register_class(OctaneDiffuseMaterial)

def unregister():
    unregister_class(OctaneDiffuseMaterial)
    unregister_class(OctaneDiffuseMaterialLayer)
    unregister_class(OctaneDiffuseMaterialCustomAovChannel)
    unregister_class(OctaneDiffuseMaterialCustomAov)
    unregister_class(OctaneDiffuseMaterialMatte)
    unregister_class(OctaneDiffuseMaterialEmission)
    unregister_class(OctaneDiffuseMaterialPriority)
    unregister_class(OctaneDiffuseMaterialRoundEdges)
    unregister_class(OctaneDiffuseMaterialSmoothShadowTerminator)
    unregister_class(OctaneDiffuseMaterialSmooth)
    unregister_class(OctaneDiffuseMaterialDisplacement)
    unregister_class(OctaneDiffuseMaterialNormal)
    unregister_class(OctaneDiffuseMaterialBump)
    unregister_class(OctaneDiffuseMaterialOpacity)
    unregister_class(OctaneDiffuseMaterialMedium)
    unregister_class(OctaneDiffuseMaterialRoughness)
    unregister_class(OctaneDiffuseMaterialTransmission)
    unregister_class(OctaneDiffuseMaterialDiffuse)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
