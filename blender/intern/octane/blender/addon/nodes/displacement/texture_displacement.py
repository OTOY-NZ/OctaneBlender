##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneTextureDisplacementTexture(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementTexture"
    bl_label = "Texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneTextureDisplacementBlackLevel(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementBlackLevel"
    bl_label = "Mid level"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=13)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The value in the image which corresponds to zero displacement. The range is always normalized to [0, 1]", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneTextureDisplacementLevelOfDetail(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementLevelOfDetail"
    bl_label = "Level of detail"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=96)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("256x256", "256x256", "", 8),
        ("512x512", "512x512", "", 9),
        ("1024x1024", "1024x1024", "", 10),
        ("2048x2048", "2048x2048", "", 11),
        ("4096x4096", "4096x4096", "", 12),
        ("8192x8192", "8192x8192", "", 13),
    ]
    default_value: EnumProperty(default="1024x1024", description="Level of detail, i.e. the resolution of the internal displacement map", items=items)

class OctaneTextureDisplacementAmount(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementAmount"
    bl_label = "Height"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.001000, description="The displacement height in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneTextureDisplacementDisplacementDirection(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementDisplacementDirection"
    bl_label = "Displacement direction"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=371)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Follow geometric normal", "Follow geometric normal", "", 2),
        ("Follow vertex normal", "Follow vertex normal", "", 1),
        ("Follow smoothed normal", "Follow smoothed normal", "", 3),
    ]
    default_value: EnumProperty(default="Follow vertex normal", description="The surface will be displaced along the given direction", items=items)

class OctaneTextureDisplacementFilterType(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementFilterType"
    bl_label = "Filter type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=336)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 0),
        ("Box", "Box", "", 1),
        ("Gaussian", "Gaussian", "", 2),
    ]
    default_value: EnumProperty(default="None", description="Specifies which filter type to use on the displacement map texture", items=items)

class OctaneTextureDisplacementFiltersize(OctaneBaseSocket):
    bl_idname = "OctaneTextureDisplacementFiltersize"
    bl_label = "Filter radius"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=2, description="Number of nearest pixels to use for filtering. The higher the value the smoother the displacement map. Only valid if a filter is enabled", min=1, max=20, soft_min=1, soft_max=20, step=1, subtype="FACTOR")

class OctaneTextureDisplacement(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneTextureDisplacement"
    bl_label = "Texture displacement"
    octane_node_type: IntProperty(name="Octane Node Type", default=80)
    octane_socket_list: StringProperty(name="Socket List", default="Texture;Mid level;Level of detail;Height;Displacement direction;Filter type;Filter radius;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneTextureDisplacementTexture", OctaneTextureDisplacementTexture.bl_label)
        self.inputs.new("OctaneTextureDisplacementBlackLevel", OctaneTextureDisplacementBlackLevel.bl_label)
        self.inputs.new("OctaneTextureDisplacementLevelOfDetail", OctaneTextureDisplacementLevelOfDetail.bl_label)
        self.inputs.new("OctaneTextureDisplacementAmount", OctaneTextureDisplacementAmount.bl_label)
        self.inputs.new("OctaneTextureDisplacementDisplacementDirection", OctaneTextureDisplacementDisplacementDirection.bl_label)
        self.inputs.new("OctaneTextureDisplacementFilterType", OctaneTextureDisplacementFilterType.bl_label)
        self.inputs.new("OctaneTextureDisplacementFiltersize", OctaneTextureDisplacementFiltersize.bl_label)
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out")


def register():
    register_class(OctaneTextureDisplacementTexture)
    register_class(OctaneTextureDisplacementBlackLevel)
    register_class(OctaneTextureDisplacementLevelOfDetail)
    register_class(OctaneTextureDisplacementAmount)
    register_class(OctaneTextureDisplacementDisplacementDirection)
    register_class(OctaneTextureDisplacementFilterType)
    register_class(OctaneTextureDisplacementFiltersize)
    register_class(OctaneTextureDisplacement)

def unregister():
    unregister_class(OctaneTextureDisplacement)
    unregister_class(OctaneTextureDisplacementFiltersize)
    unregister_class(OctaneTextureDisplacementFilterType)
    unregister_class(OctaneTextureDisplacementDisplacementDirection)
    unregister_class(OctaneTextureDisplacementAmount)
    unregister_class(OctaneTextureDisplacementLevelOfDetail)
    unregister_class(OctaneTextureDisplacementBlackLevel)
    unregister_class(OctaneTextureDisplacementTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
