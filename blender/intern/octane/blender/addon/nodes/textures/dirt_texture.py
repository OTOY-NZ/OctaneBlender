##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDirtTextureStrength(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureStrength"
    bl_label = "Strength"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=230)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Strength", min=0.100000, max=10.000000, soft_min=0.100000, soft_max=10.000000, step=1, subtype="FACTOR")

class OctaneDirtTextureDetails(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureDetails"
    bl_label = "Details"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=28)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Details", min=0.000000, max=100.000000, soft_min=0.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneDirtTextureRadius(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureRadius"
    bl_label = "Radius"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=142)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Specifies the maximum area affected by the dirt effect", min=0.000010, max=100000.000000, soft_min=0.000010, soft_max=100000.000000, step=1, subtype="FACTOR")

class OctaneDirtTextureDirtMap(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureDirtMap"
    bl_label = "Radius map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=502)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Determines the proportion of the maximum area affected by the dirt effect", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneDirtTextureTolerance(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureTolerance"
    bl_label = "Tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=242)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Tolerance for small curvature and small angles between polygons", min=0.000000, max=0.300000, soft_min=0.000000, soft_max=0.300000, step=1, subtype="FACTOR")

class OctaneDirtTextureSpread(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureSpread"
    bl_label = "Spread"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=501)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Spread controls the ray direction with respect to the normal of the surface. 0 means the dirt direction is shot straight in the direction of the surface normal, and 1 means the dirt rays are shot in all directions in the upper hemisphere in a cosine lobe", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDirtTextureDistribution(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureDistribution"
    bl_label = "Distribution"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=37)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Distribution controls how evenly rays are shot within the sampling cone. When the value is 100, rays gather closer to the lateral surface. If the value is 1 rays are evenly distributed", min=1.000000, max=100.000000, soft_min=1.000000, soft_max=100.000000, step=1, subtype="FACTOR")

class OctaneDirtTextureOffset(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureOffset"
    bl_label = "Bias"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), description="The shading normal vector in shading space that we sample with as a custom direction. By default the direction is (0, 0, 1), which is the shading normal in shading coordinates. If any non-zero bias is set, then this bias vector is used as shading normal to sample dirt rays", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneDirtTextureDirtOffsetSpace(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureDirtOffsetSpace"
    bl_label = "Bias coordinate space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=505)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
        ("Normal space", "Normal space", "", 4),
    ]
    default_value: EnumProperty(default="Normal space", description="The coordinate space the bias vector is in", items=items)

class OctaneDirtTextureDirtGlobal(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureDirtGlobal"
    bl_label = "Include object mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=503)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("All", "All", "", 0),
        ("Self", "Self", "", 1),
        ("Others", "Others", "", 2),
    ]
    default_value: EnumProperty(default="All", description="Includes objects when calculating dirt value:  By default the selected mode is All, which includes all object intersections into calculating dirt. If Self is selected, then only self-intersection is taken into account for dirt. If Others is selected, then only ray-intersection with other objects is used for dirt", items=items)

class OctaneDirtTextureInvertNormal(OctaneBaseSocket):
    bl_idname = "OctaneDirtTextureInvertNormal"
    bl_label = "Invert normal"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=84)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Invert normal")

class OctaneDirtTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDirtTexture"
    bl_label = "Dirt texture"
    octane_node_type: IntProperty(name="Octane Node Type", default=63)
    octane_socket_list: StringProperty(name="Socket List", default="Strength;Details;Radius;Radius map;Tolerance;Spread;Distribution;Bias;Bias coordinate space;Include object mode;Invert normal;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDirtTextureStrength", OctaneDirtTextureStrength.bl_label)
        self.inputs.new("OctaneDirtTextureDetails", OctaneDirtTextureDetails.bl_label)
        self.inputs.new("OctaneDirtTextureRadius", OctaneDirtTextureRadius.bl_label)
        self.inputs.new("OctaneDirtTextureDirtMap", OctaneDirtTextureDirtMap.bl_label)
        self.inputs.new("OctaneDirtTextureTolerance", OctaneDirtTextureTolerance.bl_label)
        self.inputs.new("OctaneDirtTextureSpread", OctaneDirtTextureSpread.bl_label)
        self.inputs.new("OctaneDirtTextureDistribution", OctaneDirtTextureDistribution.bl_label)
        self.inputs.new("OctaneDirtTextureOffset", OctaneDirtTextureOffset.bl_label)
        self.inputs.new("OctaneDirtTextureDirtOffsetSpace", OctaneDirtTextureDirtOffsetSpace.bl_label)
        self.inputs.new("OctaneDirtTextureDirtGlobal", OctaneDirtTextureDirtGlobal.bl_label)
        self.inputs.new("OctaneDirtTextureInvertNormal", OctaneDirtTextureInvertNormal.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneDirtTextureStrength)
    register_class(OctaneDirtTextureDetails)
    register_class(OctaneDirtTextureRadius)
    register_class(OctaneDirtTextureDirtMap)
    register_class(OctaneDirtTextureTolerance)
    register_class(OctaneDirtTextureSpread)
    register_class(OctaneDirtTextureDistribution)
    register_class(OctaneDirtTextureOffset)
    register_class(OctaneDirtTextureDirtOffsetSpace)
    register_class(OctaneDirtTextureDirtGlobal)
    register_class(OctaneDirtTextureInvertNormal)
    register_class(OctaneDirtTexture)

def unregister():
    unregister_class(OctaneDirtTexture)
    unregister_class(OctaneDirtTextureInvertNormal)
    unregister_class(OctaneDirtTextureDirtGlobal)
    unregister_class(OctaneDirtTextureDirtOffsetSpace)
    unregister_class(OctaneDirtTextureOffset)
    unregister_class(OctaneDirtTextureDistribution)
    unregister_class(OctaneDirtTextureSpread)
    unregister_class(OctaneDirtTextureTolerance)
    unregister_class(OctaneDirtTextureDirtMap)
    unregister_class(OctaneDirtTextureRadius)
    unregister_class(OctaneDirtTextureDetails)
    unregister_class(OctaneDirtTextureStrength)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
