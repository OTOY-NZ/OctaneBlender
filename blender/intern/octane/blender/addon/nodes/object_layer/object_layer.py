##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneObjectLayerLayerId(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerLayerId"
    bl_label="Render layer ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=92)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the render layer the object belongs to", min=1, max=255, soft_min=1, soft_max=255, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerGeneralVisibility(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerGeneralVisibility"
    bl_label="General visibility"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=58)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="General visibility", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerCameraVisibility(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerCameraVisibility"
    bl_label="Camera visibility"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=21)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Camera visibility")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerShadowVisibility(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerShadowVisibility"
    bl_label="Shadow visibility"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=213)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Shadow visibility")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerDirtVisibility(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerDirtVisibility"
    bl_label="Dirt visibility"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=513)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Dirt visibility")
    octane_hide_value=False
    octane_min_version=6000600
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerLightPassMask(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerLightPassMask"
    bl_label="Light pass mask"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerRandomSeed(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerRandomSeed"
    bl_label="Random color seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=143)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Random color seed", min=0, max=65535, soft_min=0, soft_max=65535, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerObjectColor(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerObjectColor"
    bl_label="Color"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=297)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The color that is rendered in the object layer render pass", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerCustomAov(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
        ("Custom AOV 11", "Custom AOV 11", "", 10),
        ("Custom AOV 12", "Custom AOV 12", "", 11),
        ("Custom AOV 13", "Custom AOV 13", "", 12),
        ("Custom AOV 14", "Custom AOV 14", "", 13),
        ("Custom AOV 15", "Custom AOV 15", "", 14),
        ("Custom AOV 16", "Custom AOV 16", "", 15),
        ("Custom AOV 17", "Custom AOV 17", "", 16),
        ("Custom AOV 18", "Custom AOV 18", "", 17),
        ("Custom AOV 19", "Custom AOV 19", "", 18),
        ("Custom AOV 20", "Custom AOV 20", "", 19),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, it will write a mask to it where it is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerBakingGroupId(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerBakingGroupId"
    bl_label="Baking group ID"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=262)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="ID of the baking group the object belongs to", min=1, max=65535, soft_min=1, soft_max=65535, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerTransform(OctaneBaseSocket):
    bl_idname="OctaneObjectLayerTransform"
    bl_label="Baking UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3070000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneObjectLayerGroupBakingSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneObjectLayerGroupBakingSettings"
    bl_label="[OctaneGroupTitle]Baking settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Baking group ID;Baking UV transform;")

class OctaneObjectLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneObjectLayer"
    bl_label="Object layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=65)
    octane_socket_list: StringProperty(name="Socket List", default="Render layer ID;General visibility;Camera visibility;Shadow visibility;Dirt visibility;Light pass mask;Random color seed;Color;Custom AOV;Custom AOV channel;Baking group ID;Baking UV transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=12)

    def init(self, context):
        self.inputs.new("OctaneObjectLayerLayerId", OctaneObjectLayerLayerId.bl_label).init()
        self.inputs.new("OctaneObjectLayerGeneralVisibility", OctaneObjectLayerGeneralVisibility.bl_label).init()
        self.inputs.new("OctaneObjectLayerCameraVisibility", OctaneObjectLayerCameraVisibility.bl_label).init()
        self.inputs.new("OctaneObjectLayerShadowVisibility", OctaneObjectLayerShadowVisibility.bl_label).init()
        self.inputs.new("OctaneObjectLayerDirtVisibility", OctaneObjectLayerDirtVisibility.bl_label).init()
        self.inputs.new("OctaneObjectLayerLightPassMask", OctaneObjectLayerLightPassMask.bl_label).init()
        self.inputs.new("OctaneObjectLayerRandomSeed", OctaneObjectLayerRandomSeed.bl_label).init()
        self.inputs.new("OctaneObjectLayerObjectColor", OctaneObjectLayerObjectColor.bl_label).init()
        self.inputs.new("OctaneObjectLayerCustomAov", OctaneObjectLayerCustomAov.bl_label).init()
        self.inputs.new("OctaneObjectLayerCustomAovChannel", OctaneObjectLayerCustomAovChannel.bl_label).init()
        self.inputs.new("OctaneObjectLayerGroupBakingSettings", OctaneObjectLayerGroupBakingSettings.bl_label).init()
        self.inputs.new("OctaneObjectLayerBakingGroupId", OctaneObjectLayerBakingGroupId.bl_label).init()
        self.inputs.new("OctaneObjectLayerTransform", OctaneObjectLayerTransform.bl_label).init()
        self.outputs.new("OctaneObjectLayerOutSocket", "Object layer out").init()


_CLASSES=[
    OctaneObjectLayerLayerId,
    OctaneObjectLayerGeneralVisibility,
    OctaneObjectLayerCameraVisibility,
    OctaneObjectLayerShadowVisibility,
    OctaneObjectLayerDirtVisibility,
    OctaneObjectLayerLightPassMask,
    OctaneObjectLayerRandomSeed,
    OctaneObjectLayerObjectColor,
    OctaneObjectLayerCustomAov,
    OctaneObjectLayerCustomAovChannel,
    OctaneObjectLayerBakingGroupId,
    OctaneObjectLayerTransform,
    OctaneObjectLayerGroupBakingSettings,
    OctaneObjectLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
