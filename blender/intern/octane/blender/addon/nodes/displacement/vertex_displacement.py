##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVertexDisplacementTexture(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneVertexDisplacementAmount(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementAmount"
    bl_label = "Height"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="The displacement height in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneVertexDisplacementBlackLevel(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementBlackLevel"
    bl_label = "Mid level"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=13)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The value in the image which corresponds to zero displacement. The range is always normalized to [0, 1]", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneVertexDisplacementDisplacementMapType(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementDisplacementMapType"
    bl_label = "Map type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=468)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Vector", "Vector", "", 0),
        ("Height", "Height", "", 1),
    ]
    default_value: EnumProperty(default="Height", description="The displacement map input type", items=items)

class OctaneVertexDisplacementTextureSpace(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementTextureSpace"
    bl_label = "Vector space"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=469)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Object", "Object", "", 0),
        ("Tangent", "Tangent", "", 1),
    ]
    default_value: EnumProperty(default="Object", description="The vector displacement map space. Only valid if the displacement map type is vector", items=items)

class OctaneVertexDisplacementBump(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementBump"
    bl_label = "Auto bump map"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enable to get fine details of the displacement map on a lower subdivision level")

class OctaneVertexDisplacementSubdLevel(OctaneBaseSocket):
    bl_idname = "OctaneVertexDisplacementSubdLevel"
    bl_label = "Subdivision level"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=479)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="The subdivision level applied to polygons using this material. This overrides the subdivision level set in the geometry preferences. Other subdivision settings have to be set in the geometry preference dialog. If a level higher than 6 is needed, please enter it manually", min=0, max=6, soft_min=0, soft_max=10, step=1, subtype="FACTOR")

class OctaneVertexDisplacement(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVertexDisplacement"
    bl_label = "Vertex displacement"
    octane_node_type: IntProperty(name="Octane Node Type", default=97)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Height;Mid level;Map type;Vector space;Auto bump map;Subdivision level;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVertexDisplacementTexture", OctaneVertexDisplacementTexture.bl_label)
        self.inputs.new("OctaneVertexDisplacementAmount", OctaneVertexDisplacementAmount.bl_label)
        self.inputs.new("OctaneVertexDisplacementBlackLevel", OctaneVertexDisplacementBlackLevel.bl_label)
        self.inputs.new("OctaneVertexDisplacementDisplacementMapType", OctaneVertexDisplacementDisplacementMapType.bl_label)
        self.inputs.new("OctaneVertexDisplacementTextureSpace", OctaneVertexDisplacementTextureSpace.bl_label)
        self.inputs.new("OctaneVertexDisplacementBump", OctaneVertexDisplacementBump.bl_label)
        self.inputs.new("OctaneVertexDisplacementSubdLevel", OctaneVertexDisplacementSubdLevel.bl_label)
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out")


def register():
    register_class(OctaneVertexDisplacementTexture)
    register_class(OctaneVertexDisplacementAmount)
    register_class(OctaneVertexDisplacementBlackLevel)
    register_class(OctaneVertexDisplacementDisplacementMapType)
    register_class(OctaneVertexDisplacementTextureSpace)
    register_class(OctaneVertexDisplacementBump)
    register_class(OctaneVertexDisplacementSubdLevel)
    register_class(OctaneVertexDisplacement)

def unregister():
    unregister_class(OctaneVertexDisplacement)
    unregister_class(OctaneVertexDisplacementSubdLevel)
    unregister_class(OctaneVertexDisplacementBump)
    unregister_class(OctaneVertexDisplacementTextureSpace)
    unregister_class(OctaneVertexDisplacementDisplacementMapType)
    unregister_class(OctaneVertexDisplacementBlackLevel)
    unregister_class(OctaneVertexDisplacementAmount)
    unregister_class(OctaneVertexDisplacementTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
