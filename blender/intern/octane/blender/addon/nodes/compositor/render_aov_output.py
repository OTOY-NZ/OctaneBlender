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


class OctaneRenderAOVOutputInput(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVOutputInput"
    bl_label = "Input"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Beauty", "Beauty", "", 0),
        ("Denoised beauty", "Denoised beauty", "", 43),
        ("Auxiliary|Irradiance", "Auxiliary|Irradiance", "", 33),
        ("Auxiliary|Light direction", "Auxiliary|Light direction", "", 34),
        ("Auxiliary|Noise", "Auxiliary|Noise", "", 31),
        ("Auxiliary|Post processing", "Auxiliary|Post processing", "", 16),
        ("Auxiliary|Shadow", "Auxiliary|Shadow", "", 32),
        ("Beauty - surfaces|Diffuse", "Beauty - surfaces|Diffuse", "", 3),
        ("Beauty - surfaces|Diffuse direct", "Beauty - surfaces|Diffuse direct", "", 4),
        ("Beauty - surfaces|Diffuse filter (beauty)", "Beauty - surfaces|Diffuse filter (beauty)", "", 6),
        ("Beauty - surfaces|Diffuse indirect", "Beauty - surfaces|Diffuse indirect", "", 5),
        ("Beauty - surfaces|Emitters", "Beauty - surfaces|Emitters", "", 1),
        ("Beauty - surfaces|Environment", "Beauty - surfaces|Environment", "", 2),
        ("Beauty - surfaces|Reflection", "Beauty - surfaces|Reflection", "", 7),
        ("Beauty - surfaces|Reflection direct", "Beauty - surfaces|Reflection direct", "", 8),
        ("Beauty - surfaces|Reflection filter (beauty)", "Beauty - surfaces|Reflection filter (beauty)", "", 10),
        ("Beauty - surfaces|Reflection indirect", "Beauty - surfaces|Reflection indirect", "", 9),
        ("Beauty - surfaces|Refraction", "Beauty - surfaces|Refraction", "", 11),
        ("Beauty - surfaces|Refraction filter (beauty)", "Beauty - surfaces|Refraction filter (beauty)", "", 12),
        ("Beauty - surfaces|Subsurface scattering", "Beauty - surfaces|Subsurface scattering", "", 15),
        ("Beauty - surfaces|Transmission", "Beauty - surfaces|Transmission", "", 13),
        ("Beauty - surfaces|Transmission filter (beauty)", "Beauty - surfaces|Transmission filter (beauty)", "", 14),
        ("Beauty - volumes|Volume", "Beauty - volumes|Volume", "", 35),
        ("Beauty - volumes|Volume emission", "Beauty - volumes|Volume emission", "", 37),
        ("Beauty - volumes|Volume mask", "Beauty - volumes|Volume mask", "", 36),
        ("Beauty - volumes|Volume Z-depth back", "Beauty - volumes|Volume Z-depth back", "", 39),
        ("Beauty - volumes|Volume Z-depth front", "Beauty - volumes|Volume Z-depth front", "", 38),
        ("Custom|Custom AOV 1", "Custom|Custom AOV 1", "", 501),
        ("Custom|Custom AOV 2", "Custom|Custom AOV 2", "", 502),
        ("Custom|Custom AOV 3", "Custom|Custom AOV 3", "", 503),
        ("Custom|Custom AOV 4", "Custom|Custom AOV 4", "", 504),
        ("Custom|Custom AOV 5", "Custom|Custom AOV 5", "", 505),
        ("Custom|Custom AOV 6", "Custom|Custom AOV 6", "", 506),
        ("Custom|Custom AOV 7", "Custom|Custom AOV 7", "", 507),
        ("Custom|Custom AOV 8", "Custom|Custom AOV 8", "", 508),
        ("Custom|Custom AOV 9", "Custom|Custom AOV 9", "", 509),
        ("Custom|Custom AOV 10", "Custom|Custom AOV 10", "", 510),
        ("Custom|Custom AOV 11", "Custom|Custom AOV 11", "", 511),
        ("Custom|Custom AOV 12", "Custom|Custom AOV 12", "", 512),
        ("Custom|Custom AOV 13", "Custom|Custom AOV 13", "", 513),
        ("Custom|Custom AOV 14", "Custom|Custom AOV 14", "", 514),
        ("Custom|Custom AOV 15", "Custom|Custom AOV 15", "", 515),
        ("Custom|Custom AOV 16", "Custom|Custom AOV 16", "", 516),
        ("Custom|Custom AOV 17", "Custom|Custom AOV 17", "", 517),
        ("Custom|Custom AOV 18", "Custom|Custom AOV 18", "", 518),
        ("Custom|Custom AOV 19", "Custom|Custom AOV 19", "", 519),
        ("Custom|Custom AOV 20", "Custom|Custom AOV 20", "", 520),
        ("Custom|Global texture AOV 1", "Custom|Global texture AOV 1", "", 1101),
        ("Custom|Global texture AOV 2", "Custom|Global texture AOV 2", "", 1102),
        ("Custom|Global texture AOV 3", "Custom|Global texture AOV 3", "", 1103),
        ("Custom|Global texture AOV 4", "Custom|Global texture AOV 4", "", 1104),
        ("Custom|Global texture AOV 5", "Custom|Global texture AOV 5", "", 1105),
        ("Custom|Global texture AOV 6", "Custom|Global texture AOV 6", "", 1106),
        ("Custom|Global texture AOV 7", "Custom|Global texture AOV 7", "", 1107),
        ("Custom|Global texture AOV 8", "Custom|Global texture AOV 8", "", 1108),
        ("Custom|Global texture AOV 9", "Custom|Global texture AOV 9", "", 1109),
        ("Custom|Global texture AOV 10", "Custom|Global texture AOV 10", "", 1110),
        ("Custom|Global texture AOV 11", "Custom|Global texture AOV 11", "", 1111),
        ("Custom|Global texture AOV 12", "Custom|Global texture AOV 12", "", 1112),
        ("Custom|Global texture AOV 13", "Custom|Global texture AOV 13", "", 1113),
        ("Custom|Global texture AOV 14", "Custom|Global texture AOV 14", "", 1114),
        ("Custom|Global texture AOV 15", "Custom|Global texture AOV 15", "", 1115),
        ("Custom|Global texture AOV 16", "Custom|Global texture AOV 16", "", 1116),
        ("Custom|Global texture AOV 17", "Custom|Global texture AOV 17", "", 1117),
        ("Custom|Global texture AOV 18", "Custom|Global texture AOV 18", "", 1118),
        ("Custom|Global texture AOV 19", "Custom|Global texture AOV 19", "", 1119),
        ("Custom|Global texture AOV 20", "Custom|Global texture AOV 20", "", 1120),
        ("Denoised|Denoised diffuse direct", "Denoised|Denoised diffuse direct", "", 44),
        ("Denoised|Denoised diffuse indirect", "Denoised|Denoised diffuse indirect", "", 45),
        ("Denoised|Denoised emission", "Denoised|Denoised emission", "", 76),
        ("Denoised|Denoised reflection direct", "Denoised|Denoised reflection direct", "", 46),
        ("Denoised|Denoised reflection indirect", "Denoised|Denoised reflection indirect", "", 47),
        ("Denoised|Denoised remainder", "Denoised|Denoised remainder", "", 49),
        ("Denoised|Denoised volume", "Denoised|Denoised volume", "", 74),
        ("Denoised|Denoised volume emission", "Denoised|Denoised volume emission", "", 75),
        ("Info|Ambient occlusion", "Info|Ambient occlusion", "", 1010),
        ("Info|Baking group ID", "Info|Baking group ID", "", 1017),
        ("Info|Diffuse filter (info)", "Info|Diffuse filter (info)", "", 1020),
        ("Info|Index of refraction", "Info|Index of refraction", "", 1019),
        ("Info|Light pass ID", "Info|Light pass ID", "", 1014),
        ("Info|Material ID", "Info|Material ID", "", 1004),
        ("Info|Motion vector", "Info|Motion vector", "", 1011),
        ("Info|Normal (geometric)", "Info|Normal (geometric)", "", 1000),
        ("Info|Normal (shading)", "Info|Normal (shading)", "", 1001),
        ("Info|Normal (smooth)", "Info|Normal (smooth)", "", 1008),
        ("Info|Normal (tangent)", "Info|Normal (tangent)", "", 1015),
        ("Info|Object ID", "Info|Object ID", "", 1009),
        ("Info|Object layer color", "Info|Object layer color", "", 1024),
        ("Info|Opacity", "Info|Opacity", "", 1016),
        ("Info|Position", "Info|Position", "", 1002),
        ("Info|Reflection filter (info)", "Info|Reflection filter (info)", "", 1021),
        ("Info|Refraction filter (info)", "Info|Refraction filter (info)", "", 1022),
        ("Info|Render layer ID", "Info|Render layer ID", "", 1012),
        ("Info|Render layer mask", "Info|Render layer mask", "", 1013),
        ("Info|Roughness", "Info|Roughness", "", 1018),
        ("Info|Texture tangent", "Info|Texture tangent", "", 1006),
        ("Info|Transmission filter (info)", "Info|Transmission filter (info)", "", 1023),
        ("Info|UV coordinates", "Info|UV coordinates", "", 1005),
        ("Info|Wireframe", "Info|Wireframe", "", 1007),
        ("Info|Z-depth", "Info|Z-depth", "", 1003),
        ("Light|Ambient light", "Light|Ambient light", "", 21),
        ("Light|Ambient light direct", "Light|Ambient light direct", "", 54),
        ("Light|Ambient light indirect", "Light|Ambient light indirect", "", 55),
        ("Light|Light ID 1", "Light|Light ID 1", "", 23),
        ("Light|Light ID 1 direct", "Light|Light ID 1 direct", "", 58),
        ("Light|Light ID 1 indirect", "Light|Light ID 1 indirect", "", 66),
        ("Light|Light ID 2", "Light|Light ID 2", "", 24),
        ("Light|Light ID 2 direct", "Light|Light ID 2 direct", "", 59),
        ("Light|Light ID 2 indirect", "Light|Light ID 2 indirect", "", 67),
        ("Light|Light ID 3", "Light|Light ID 3", "", 25),
        ("Light|Light ID 3 direct", "Light|Light ID 3 direct", "", 60),
        ("Light|Light ID 3 indirect", "Light|Light ID 3 indirect", "", 68),
        ("Light|Light ID 4", "Light|Light ID 4", "", 26),
        ("Light|Light ID 4 direct", "Light|Light ID 4 direct", "", 61),
        ("Light|Light ID 4 indirect", "Light|Light ID 4 indirect", "", 69),
        ("Light|Light ID 5", "Light|Light ID 5", "", 27),
        ("Light|Light ID 5 direct", "Light|Light ID 5 direct", "", 62),
        ("Light|Light ID 5 indirect", "Light|Light ID 5 indirect", "", 70),
        ("Light|Light ID 6", "Light|Light ID 6", "", 28),
        ("Light|Light ID 6 direct", "Light|Light ID 6 direct", "", 63),
        ("Light|Light ID 6 indirect", "Light|Light ID 6 indirect", "", 71),
        ("Light|Light ID 7", "Light|Light ID 7", "", 29),
        ("Light|Light ID 7 direct", "Light|Light ID 7 direct", "", 64),
        ("Light|Light ID 7 indirect", "Light|Light ID 7 indirect", "", 72),
        ("Light|Light ID 8", "Light|Light ID 8", "", 30),
        ("Light|Light ID 8 direct", "Light|Light ID 8 direct", "", 65),
        ("Light|Light ID 8 indirect", "Light|Light ID 8 indirect", "", 73),
        ("Light|Sunlight", "Light|Sunlight", "", 22),
        ("Light|Sunlight direct", "Light|Sunlight direct", "", 56),
        ("Light|Sunlight indirect", "Light|Sunlight indirect", "", 57),
        ("Render layer|Black layer shadows", "Render layer|Black layer shadows", "", 18),
        ("Render layer|Layer reflections", "Render layer|Layer reflections", "", 20),
        ("Render layer|Layer shadows", "Render layer|Layer shadows", "", 17),
    ]
    default_value: EnumProperty(default="Beauty", update=OctaneBaseSocket.update_node_tree, description="Select a render AOV from the list of all available render AOVs", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneRenderAOVOutputOutputChannels(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVOutputOutputChannels"
    bl_label = "Output channels"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id=consts.PinID.P_OUTPUT_CHANNELS
    octane_pin_name="outputChannels"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("Alpha", "Alpha", "", 2),
    ]
    default_value: EnumProperty(default="RGBA", update=OctaneBaseSocket.update_node_tree, description="Select output channels type of this node. Can be set to one of enum ChannelGroups", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneRenderAOVOutputImager(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVOutputImager"
    bl_label = "Enable imager"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id=consts.PinID.P_IMAGER
    octane_pin_name="imager"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether to apply the imager settings on the final AOV output. Only used if this node is the root output AOV node (i.e. directly connected to the output AOV group node)")
    octane_hide_value = False
    octane_min_version = 10021000
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneRenderAOVOutputPostproc(OctaneBaseSocket):
    bl_idname = "OctaneRenderAOVOutputPostproc"
    bl_label = "Enable post processing"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POST_PROCESSING
    octane_pin_name="postproc"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether to apply the post processing settings on the final AOV output. Only used if this node is the root output AOV node (i.e. directly connected to the output AOV group node)")
    octane_hide_value = False
    octane_min_version = 10021000
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneRenderAOVOutputGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname = "OctaneRenderAOVOutputGroupOutputSettings"
    bl_label = "[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post processing;")

class OctaneRenderAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneRenderAOVOutput"
    bl_label = "Render output AOV"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list=[OctaneRenderAOVOutputInput,OctaneRenderAOVOutputOutputChannels,OctaneRenderAOVOutputGroupOutputSettings,OctaneRenderAOVOutputImager,OctaneRenderAOVOutputPostproc,]
    octane_min_version = 0
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_RENDER
    octane_socket_list=["Input", "Output channels", "Enable imager", "Enable post processing", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=4

    compatibility_mode_infos=[
        ("Latest (2022.1)", "Latest (2022.1)", """(null)""", 12000008),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """When "Enable imager" is disabled, some aspects of the imager are not bypassed, and linear sRGB data is output as sRGB.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2022.1)", update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=12000102, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneRenderAOVOutputInput", OctaneRenderAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputOutputChannels", OctaneRenderAOVOutputOutputChannels.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputGroupOutputSettings", OctaneRenderAOVOutputGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputImager", OctaneRenderAOVOutputImager.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputPostproc", OctaneRenderAOVOutputPostproc.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRenderAOVOutputInput,
    OctaneRenderAOVOutputOutputChannels,
    OctaneRenderAOVOutputImager,
    OctaneRenderAOVOutputPostproc,
    OctaneRenderAOVOutputGroupOutputSettings,
    OctaneRenderAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #

from ...utils import utility

OctaneRenderAOVOutputInput_simplified_items = utility.make_blender_style_enum_items(OctaneRenderAOVOutputInput.items)

class OctaneRenderAOVOutputInput_Override(OctaneRenderAOVOutputInput):
    default_value: EnumProperty(default="Beauty", update=OctaneBaseSocket.update_node_tree, description="Select a render AOV from the list of all available render AOVs", items=OctaneRenderAOVOutputInput_simplified_items)

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")

utility.override_class(_CLASSES, OctaneRenderAOVOutputInput, OctaneRenderAOVOutputInput_Override)
