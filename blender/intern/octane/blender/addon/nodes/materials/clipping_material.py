##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneClippingMaterialEnabled(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If true, geometries located inside the clipping material will be clipped away")

class OctaneClippingMaterialIntersectionMaterial(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialIntersectionMaterial"
    bl_label = "Intersection"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=658)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneClippingMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialPriority"
    bl_label = "Priority"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=100, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")

class OctaneClippingMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneClippingMaterial"
    bl_label = "Clipping material"
    octane_node_type: IntProperty(name="Octane Node Type", default=178)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Intersection;Priority;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneClippingMaterialEnabled", OctaneClippingMaterialEnabled.bl_label)
        self.inputs.new("OctaneClippingMaterialIntersectionMaterial", OctaneClippingMaterialIntersectionMaterial.bl_label)
        self.inputs.new("OctaneClippingMaterialPriority", OctaneClippingMaterialPriority.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneClippingMaterialEnabled)
    register_class(OctaneClippingMaterialIntersectionMaterial)
    register_class(OctaneClippingMaterialPriority)
    register_class(OctaneClippingMaterial)

def unregister():
    unregister_class(OctaneClippingMaterial)
    unregister_class(OctaneClippingMaterialPriority)
    unregister_class(OctaneClippingMaterialIntersectionMaterial)
    unregister_class(OctaneClippingMaterialEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
