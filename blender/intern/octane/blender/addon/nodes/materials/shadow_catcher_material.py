##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneShadowCatcherMaterialEnabled(OctaneBaseSocket):
    bl_idname = "OctaneShadowCatcherMaterialEnabled"
    bl_label = "Enabled"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If true it will capture shadows")

class OctaneShadowCatcherMaterialOpacity(OctaneBaseSocket):
    bl_idname = "OctaneShadowCatcherMaterialOpacity"
    bl_label = "Opacity"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Opacity channel controlling the transparency of the shadow via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")

class OctaneShadowCatcherMaterialCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneShadowCatcherMaterialCustomAov"
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

class OctaneShadowCatcherMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneShadowCatcherMaterialCustomAovChannel"
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

class OctaneShadowCatcherMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneShadowCatcherMaterial"
    bl_label = "Shadow catcher material"
    octane_node_type: IntProperty(name="Octane Node Type", default=145)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Opacity;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneShadowCatcherMaterialEnabled", OctaneShadowCatcherMaterialEnabled.bl_label)
        self.inputs.new("OctaneShadowCatcherMaterialOpacity", OctaneShadowCatcherMaterialOpacity.bl_label)
        self.inputs.new("OctaneShadowCatcherMaterialCustomAov", OctaneShadowCatcherMaterialCustomAov.bl_label)
        self.inputs.new("OctaneShadowCatcherMaterialCustomAovChannel", OctaneShadowCatcherMaterialCustomAovChannel.bl_label)
        self.outputs.new("OctaneMaterialOutSocket", "Material out")


def register():
    register_class(OctaneShadowCatcherMaterialEnabled)
    register_class(OctaneShadowCatcherMaterialOpacity)
    register_class(OctaneShadowCatcherMaterialCustomAov)
    register_class(OctaneShadowCatcherMaterialCustomAovChannel)
    register_class(OctaneShadowCatcherMaterial)

def unregister():
    unregister_class(OctaneShadowCatcherMaterial)
    unregister_class(OctaneShadowCatcherMaterialCustomAovChannel)
    unregister_class(OctaneShadowCatcherMaterialCustomAov)
    unregister_class(OctaneShadowCatcherMaterialOpacity)
    unregister_class(OctaneShadowCatcherMaterialEnabled)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
