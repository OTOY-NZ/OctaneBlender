##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneObjectLayerLayerId(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerLayerId"
    bl_label = "Render layer ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=92)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="ID of the render layer the object belongs to", min=1, max=255, soft_min=1, soft_max=255, step=1, subtype="FACTOR")

class OctaneObjectLayerGeneralVisibility(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerGeneralVisibility"
    bl_label = "General visibility"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=58)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="General visibility", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneObjectLayerCameraVisibility(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerCameraVisibility"
    bl_label = "Camera visibility"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=21)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Camera visibility")

class OctaneObjectLayerShadowVisibility(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerShadowVisibility"
    bl_label = "Shadow visibility"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=213)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Shadow visibility")

class OctaneObjectLayerDirtVisibility(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerDirtVisibility"
    bl_label = "Dirt visibility"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=513)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Dirt visibility")

class OctaneObjectLayerLightPassMask(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerLightPassMask"
    bl_label = "Light pass mask"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneObjectLayerRandomSeed(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerRandomSeed"
    bl_label = "Random color seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Random color seed", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="FACTOR")

class OctaneObjectLayerObjectColor(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerObjectColor"
    bl_label = "Color"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=297)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="The color that is rendered in the object layer render pass", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="NONE", size=3)

class OctaneObjectLayerCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerCustomAov"
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
    default_value: EnumProperty(default="None", description="If a custom AOV is selected, it will write a mask to it where it is visible", items=items)

class OctaneObjectLayerCustomAovChannel(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerCustomAovChannel"
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

class OctaneObjectLayerBakingGroupId(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerBakingGroupId"
    bl_label = "Baking group ID"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=262)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="ID of the baking group the object belongs to", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")

class OctaneObjectLayerTransform(OctaneBaseSocket):
    bl_idname = "OctaneObjectLayerTransform"
    bl_label = "Baking UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneObjectLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneObjectLayer"
    bl_label = "Object layer"
    octane_node_type: IntProperty(name="Octane Node Type", default=65)
    octane_socket_list: StringProperty(name="Socket List", default="Render layer ID;General visibility;Camera visibility;Shadow visibility;Dirt visibility;Light pass mask;Random color seed;Color;Custom AOV;Custom AOV channel;Baking group ID;Baking UV transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneObjectLayerLayerId", OctaneObjectLayerLayerId.bl_label)
        self.inputs.new("OctaneObjectLayerGeneralVisibility", OctaneObjectLayerGeneralVisibility.bl_label)
        self.inputs.new("OctaneObjectLayerCameraVisibility", OctaneObjectLayerCameraVisibility.bl_label)
        self.inputs.new("OctaneObjectLayerShadowVisibility", OctaneObjectLayerShadowVisibility.bl_label)
        self.inputs.new("OctaneObjectLayerDirtVisibility", OctaneObjectLayerDirtVisibility.bl_label)
        self.inputs.new("OctaneObjectLayerLightPassMask", OctaneObjectLayerLightPassMask.bl_label)
        self.inputs.new("OctaneObjectLayerRandomSeed", OctaneObjectLayerRandomSeed.bl_label)
        self.inputs.new("OctaneObjectLayerObjectColor", OctaneObjectLayerObjectColor.bl_label)
        self.inputs.new("OctaneObjectLayerCustomAov", OctaneObjectLayerCustomAov.bl_label)
        self.inputs.new("OctaneObjectLayerCustomAovChannel", OctaneObjectLayerCustomAovChannel.bl_label)
        self.inputs.new("OctaneObjectLayerBakingGroupId", OctaneObjectLayerBakingGroupId.bl_label)
        self.inputs.new("OctaneObjectLayerTransform", OctaneObjectLayerTransform.bl_label)
        self.outputs.new("OctaneObjectLayerOutSocket", "Object layer out")


def register():
    register_class(OctaneObjectLayerLayerId)
    register_class(OctaneObjectLayerGeneralVisibility)
    register_class(OctaneObjectLayerCameraVisibility)
    register_class(OctaneObjectLayerShadowVisibility)
    register_class(OctaneObjectLayerDirtVisibility)
    register_class(OctaneObjectLayerLightPassMask)
    register_class(OctaneObjectLayerRandomSeed)
    register_class(OctaneObjectLayerObjectColor)
    register_class(OctaneObjectLayerCustomAov)
    register_class(OctaneObjectLayerCustomAovChannel)
    register_class(OctaneObjectLayerBakingGroupId)
    register_class(OctaneObjectLayerTransform)
    register_class(OctaneObjectLayer)

def unregister():
    unregister_class(OctaneObjectLayer)
    unregister_class(OctaneObjectLayerTransform)
    unregister_class(OctaneObjectLayerBakingGroupId)
    unregister_class(OctaneObjectLayerCustomAovChannel)
    unregister_class(OctaneObjectLayerCustomAov)
    unregister_class(OctaneObjectLayerObjectColor)
    unregister_class(OctaneObjectLayerRandomSeed)
    unregister_class(OctaneObjectLayerLightPassMask)
    unregister_class(OctaneObjectLayerDirtVisibility)
    unregister_class(OctaneObjectLayerShadowVisibility)
    unregister_class(OctaneObjectLayerCameraVisibility)
    unregister_class(OctaneObjectLayerGeneralVisibility)
    unregister_class(OctaneObjectLayerLayerId)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
