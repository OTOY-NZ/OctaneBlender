##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneLayeredMaterialMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneLayeredMaterialMaterial1"
    bl_label = "Base Material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneLayeredMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneLayeredMaterialCustomAov"
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

class OctaneLayeredMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneLayeredMaterialCustomAovChannel"
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

class OctaneLayeredMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneLayeredMaterial"
    bl_label = "Layered material"
    octane_node_type: IntProperty(name="Octane Node Type", default=143)
    octane_socket_list: StringProperty(name="Socket List", default="Base Material;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneLayeredMaterialMaterial1", OctaneLayeredMaterialMaterial1.bl_label)
        self.inputs.new("OctaneLayeredMaterialCustomAov", OctaneLayeredMaterialCustomAov.bl_label)
        self.inputs.new("OctaneLayeredMaterialCustomAovChannel", OctaneLayeredMaterialCustomAovChannel.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneLayeredMaterialMaterial1)
    register_class(OctaneLayeredMaterialCustomAov)
    register_class(OctaneLayeredMaterialCustomAovChannel)
    register_class(OctaneLayeredMaterial)

def unregister():
    unregister_class(OctaneLayeredMaterial)
    unregister_class(OctaneLayeredMaterialCustomAovChannel)
    unregister_class(OctaneLayeredMaterialCustomAov)
    unregister_class(OctaneLayeredMaterialMaterial1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
