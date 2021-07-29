##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneMixMaterialAmount(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialAmount"
    bl_label = "Amount"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="Mix amount", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneMixMaterialMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialMaterial1"
    bl_label = "First material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMixMaterialMaterial2(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialMaterial2"
    bl_label = "Second material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=101)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMixMaterialDisplacement(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialDisplacement"
    bl_label = "Displacement"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=22)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneMixMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialCustomAov"
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

class OctaneMixMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneMixMaterialCustomAovChannel"
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

class OctaneMixMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneMixMaterial"
    bl_label = "Mix material"
    octane_node_type: IntProperty(name="Octane Node Type", default=19)
    octane_socket_list: StringProperty(name="Socket List", default="Amount;First material;Second material;Displacement;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneMixMaterialAmount", OctaneMixMaterialAmount.bl_label)
        self.inputs.new("OctaneMixMaterialMaterial1", OctaneMixMaterialMaterial1.bl_label)
        self.inputs.new("OctaneMixMaterialMaterial2", OctaneMixMaterialMaterial2.bl_label)
        self.inputs.new("OctaneMixMaterialDisplacement", OctaneMixMaterialDisplacement.bl_label)
        self.inputs.new("OctaneMixMaterialCustomAov", OctaneMixMaterialCustomAov.bl_label)
        self.inputs.new("OctaneMixMaterialCustomAovChannel", OctaneMixMaterialCustomAovChannel.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneMixMaterialAmount)
    register_class(OctaneMixMaterialMaterial1)
    register_class(OctaneMixMaterialMaterial2)
    register_class(OctaneMixMaterialDisplacement)
    register_class(OctaneMixMaterialCustomAov)
    register_class(OctaneMixMaterialCustomAovChannel)
    register_class(OctaneMixMaterial)

def unregister():
    unregister_class(OctaneMixMaterial)
    unregister_class(OctaneMixMaterialCustomAovChannel)
    unregister_class(OctaneMixMaterialCustomAov)
    unregister_class(OctaneMixMaterialDisplacement)
    unregister_class(OctaneMixMaterialMaterial2)
    unregister_class(OctaneMixMaterialMaterial1)
    unregister_class(OctaneMixMaterialAmount)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
