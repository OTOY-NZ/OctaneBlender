# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneOutputAOVsRenderAOVEnabled(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsRenderAOVEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsRenderAOVInput(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsRenderAOVInput"
    bl_label = "Render AOV"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_INPUT
    octane_pin_name = "input"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Beauty", "Beauty", "", 0),
        ("Denoised beauty", "Denoised beauty", "", 43),
        ("Auxiliary|Irradiance", "Auxiliary|Irradiance", "", 33),
        ("Auxiliary|Light direction", "Auxiliary|Light direction", "", 34),
        ("Auxiliary|Noise", "Auxiliary|Noise", "", 31),
        ("Auxiliary|Postfx media", "Auxiliary|Postfx media", "", 84),
        ("Auxiliary|Post processing", "Auxiliary|Post processing", "", 16),
        ("Auxiliary|Shadow", "Auxiliary|Shadow", "", 32),
        ("Beauty - surfaces|Denoise albedo", "Beauty - surfaces|Denoise albedo", "", 123),
        ("Beauty - surfaces|Denoise normal", "Beauty - surfaces|Denoise normal", "", 40),
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
        ("Light|Light ID 9", "Light|Light ID 9", "", 85),
        ("Light|Light ID 9 direct", "Light|Light ID 9 direct", "", 97),
        ("Light|Light ID 9 indirect", "Light|Light ID 9 indirect", "", 109),
        ("Light|Light ID 10", "Light|Light ID 10", "", 86),
        ("Light|Light ID 10 direct", "Light|Light ID 10 direct", "", 98),
        ("Light|Light ID 10 indirect", "Light|Light ID 10 indirect", "", 110),
        ("Light|Light ID 11", "Light|Light ID 11", "", 87),
        ("Light|Light ID 11 direct", "Light|Light ID 11 direct", "", 99),
        ("Light|Light ID 11 indirect", "Light|Light ID 11 indirect", "", 111),
        ("Light|Light ID 12", "Light|Light ID 12", "", 88),
        ("Light|Light ID 12 direct", "Light|Light ID 12 direct", "", 100),
        ("Light|Light ID 12 indirect", "Light|Light ID 12 indirect", "", 112),
        ("Light|Light ID 13", "Light|Light ID 13", "", 89),
        ("Light|Light ID 13 direct", "Light|Light ID 13 direct", "", 101),
        ("Light|Light ID 13 indirect", "Light|Light ID 13 indirect", "", 113),
        ("Light|Light ID 14", "Light|Light ID 14", "", 90),
        ("Light|Light ID 14 direct", "Light|Light ID 14 direct", "", 102),
        ("Light|Light ID 14 indirect", "Light|Light ID 14 indirect", "", 114),
        ("Light|Light ID 15", "Light|Light ID 15", "", 91),
        ("Light|Light ID 15 direct", "Light|Light ID 15 direct", "", 103),
        ("Light|Light ID 15 indirect", "Light|Light ID 15 indirect", "", 115),
        ("Light|Light ID 16", "Light|Light ID 16", "", 92),
        ("Light|Light ID 16 direct", "Light|Light ID 16 direct", "", 104),
        ("Light|Light ID 16 indirect", "Light|Light ID 16 indirect", "", 116),
        ("Light|Light ID 17", "Light|Light ID 17", "", 93),
        ("Light|Light ID 17 direct", "Light|Light ID 17 direct", "", 105),
        ("Light|Light ID 17 indirect", "Light|Light ID 17 indirect", "", 117),
        ("Light|Light ID 18", "Light|Light ID 18", "", 94),
        ("Light|Light ID 18 direct", "Light|Light ID 18 direct", "", 106),
        ("Light|Light ID 18 indirect", "Light|Light ID 18 indirect", "", 118),
        ("Light|Light ID 19", "Light|Light ID 19", "", 95),
        ("Light|Light ID 19 direct", "Light|Light ID 19 direct", "", 107),
        ("Light|Light ID 19 indirect", "Light|Light ID 19 indirect", "", 119),
        ("Light|Light ID 20", "Light|Light ID 20", "", 96),
        ("Light|Light ID 20 direct", "Light|Light ID 20 direct", "", 108),
        ("Light|Light ID 20 indirect", "Light|Light ID 20 indirect", "", 120),
        ("Light|Sunlight", "Light|Sunlight", "", 22),
        ("Light|Sunlight direct", "Light|Sunlight direct", "", 56),
        ("Light|Sunlight indirect", "Light|Sunlight indirect", "", 57),
        ("Render layer|Black layer shadows", "Render layer|Black layer shadows", "", 18),
        ("Render layer|Layer reflections", "Render layer|Layer reflections", "", 20),
        ("Render layer|Layer shadows", "Render layer|Layer shadows", "", 17),
    ]
    default_value: EnumProperty(default="Beauty", update=OctaneBaseSocket.update_node_tree, description="The render AOV to blend. This must be enabled as a render AOV", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsRenderAOVBlendingSettings(OctaneBaseSocket):
    bl_idname = "OctaneOutputAOVsRenderAOVBlendingSettings"
    bl_label = "Blending settings"
    color = consts.OctanePinColor.BlendingSettings
    octane_default_node_type = consts.NodeType.NT_BLENDING_SETTINGS
    octane_default_node_name = "OctaneBlendingSettings"
    octane_pin_id = consts.PinID.P_BLENDING_SETTINGS
    octane_pin_name = "blendingSettings"
    octane_pin_type = consts.PinType.PT_BLENDING_SETTINGS
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneOutputAOVsRenderAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneOutputAOVsRenderAOV"
    bl_label = "Render AOV"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneOutputAOVsRenderAOVEnabled, OctaneOutputAOVsRenderAOVInput, OctaneOutputAOVsRenderAOVBlendingSettings, ]
    octane_min_version = 13000000
    octane_node_type = consts.NodeType.NT_OUTPUT_AOV_LAYER_BLEND_RENDER_AOV
    octane_socket_list = ["Enabled", "Render AOV", "Blending settings", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 3

    def init(self, context):  # noqa
        self.inputs.new("OctaneOutputAOVsRenderAOVEnabled", OctaneOutputAOVsRenderAOVEnabled.bl_label).init()
        self.inputs.new("OctaneOutputAOVsRenderAOVInput", OctaneOutputAOVsRenderAOVInput.bl_label).init()
        self.inputs.new("OctaneOutputAOVsRenderAOVBlendingSettings", OctaneOutputAOVsRenderAOVBlendingSettings.bl_label).init()
        self.outputs.new("OctaneOutputAOVLayerOutSocket", "Output AOV layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneOutputAOVsRenderAOVEnabled,
    OctaneOutputAOVsRenderAOVInput,
    OctaneOutputAOVsRenderAOVBlendingSettings,
    OctaneOutputAOVsRenderAOV,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


# OctaneOutputAOVsRenderAOVInput_simplified_items = utility.make_blender_style_enum_items(
#     OctaneOutputAOVsRenderAOVInput.items, True, True,
#     [
#         {"Beauty, Denoised": ["", "Beauty - surfaces", "Beauty - volumes", "Denoised"]},
#         {"Auxiliary, Render layer": ["Auxiliary", "Render layer", ]},
#         {"Info": ["Info", ]},
#         {"Light": ["Light", ]},
#         {"Custom": ["Custom", ]},
#     ])
OctaneOutputAOVsRenderAOVInput_no_heading_simplified_items = utility.make_blender_style_enum_items(OctaneOutputAOVsRenderAOVInput.items, False, False)
OctaneOutputAOVsRenderAOVInput_simplified_items = [
    ('', 'Beauty, Denoised', ''),
    ('Beauty', 'Beauty', '', 0),
    ('Denoised beauty', 'Denoised beauty', '', 43),
    None,
    ('Denoise albedo', 'Denoise albedo', '', 123),
    ('Denoise normal', 'Denoise normal', '', 40),
    ('Diffuse', 'Diffuse', '', 3),
    ('Diffuse direct', 'Diffuse direct', '', 4),
    ('Diffuse filter (beauty)', 'Diffuse filter (beauty)', '', 6),
    ('Diffuse indirect', 'Diffuse indirect', '', 5),
    ('Emitters', 'Emitters', '', 1),
    ('Environment', 'Environment', '', 2),
    ('Reflection', 'Reflection', '', 7),
    ('Reflection direct', 'Reflection direct', '', 8),
    ('Reflection filter (beauty)', 'Reflection filter (beauty)', '', 10),
    ('Reflection indirect', 'Reflection indirect', '', 9),
    ('Refraction', 'Refraction', '', 11),
    ('Refraction filter (beauty)', 'Refraction filter (beauty)', '', 12),
    ('Subsurface scattering', 'Subsurface scattering', '', 15),
    ('Transmission', 'Transmission', '', 13),
    ('Transmission filter (beauty)', 'Transmission filter (beauty)', '', 14),
    None,
    ('Volume', 'Volume', '', 35),
    ('Volume emission', 'Volume emission', '', 37),
    ('Volume mask', 'Volume mask', '', 36),
    ('Volume Z-depth back', 'Volume Z-depth back', '', 39),
    ('Volume Z-depth front', 'Volume Z-depth front', '', 38),
    None,
    ('Denoised diffuse direct', 'Denoised diffuse direct', '', 44),
    ('Denoised diffuse indirect', 'Denoised diffuse indirect', '', 45),
    ('Denoised emission', 'Denoised emission', '', 76),
    ('Denoised reflection direct', 'Denoised reflection direct', '', 46),
    ('Denoised reflection indirect', 'Denoised reflection indirect', '', 47),
    ('Denoised remainder', 'Denoised remainder', '', 49),
    ('Denoised volume', 'Denoised volume', '', 74),
    ('Denoised volume emission', 'Denoised volume emission', '', 75),
    ('', 'Auxiliary, Render layer', ''),
    ('Irradiance', 'Irradiance', '', 33),
    ('Light direction', 'Light direction', '', 34),
    ('Noise', 'Noise', '', 31),
    ('Postfx media', 'Postfx media', '', 84),
    ('Post processing', 'Post processing', '', 16),
    ('Shadow', 'Shadow', '', 32),
    None,
    ('Black layer shadows', 'Black layer shadows', '', 18),
    ('Layer reflections', 'Layer reflections', '', 20),
    ('Layer shadows', 'Layer shadows', '', 17),
    ('', 'Info', ''),
    ('Ambient occlusion', 'Ambient occlusion', '', 1010),
    ('Baking group ID', 'Baking group ID', '', 1017),
    ('Diffuse filter (info)', 'Diffuse filter (info)', '', 1020),
    ('Index of refraction', 'Index of refraction', '', 1019),
    ('Light pass ID', 'Light pass ID', '', 1014),
    ('Material ID', 'Material ID', '', 1004),
    ('Motion vector', 'Motion vector', '', 1011),
    ('Normal (geometric)', 'Normal (geometric)', '', 1000),
    ('Normal (shading)', 'Normal (shading)', '', 1001),
    ('Normal (smooth)', 'Normal (smooth)', '', 1008),
    ('Normal (tangent)', 'Normal (tangent)', '', 1015),
    ('Object ID', 'Object ID', '', 1009),
    ('Object layer color', 'Object layer color', '', 1024),
    ('Opacity', 'Opacity', '', 1016),
    ('Position', 'Position', '', 1002),
    ('Reflection filter (info)', 'Reflection filter (info)', '', 1021),
    ('Refraction filter (info)', 'Refraction filter (info)', '', 1022),
    ('Render layer ID', 'Render layer ID', '', 1012),
    ('Render layer mask', 'Render layer mask', '', 1013),
    ('Roughness', 'Roughness', '', 1018),
    ('Texture tangent', 'Texture tangent', '', 1006),
    ('Transmission filter (info)', 'Transmission filter (info)', '', 1023),
    ('UV coordinates', 'UV coordinates', '', 1005),
    ('Wireframe', 'Wireframe', '', 1007),
    ('Z-depth', 'Z-depth', '', 1003),
    ('', 'Light', ''),
    ('Ambient light', 'Ambient light', '', 21),
    ('Sunlight', 'Sunlight', '', 22),
    ('Light ID 1', 'Light ID 1', '', 23),
    ('Light ID 2', 'Light ID 2', '', 24),
    ('Light ID 3', 'Light ID 3', '', 25),
    ('Light ID 4', 'Light ID 4', '', 26),
    ('Light ID 5', 'Light ID 5', '', 27),
    ('Light ID 6', 'Light ID 6', '', 28),
    ('Light ID 7', 'Light ID 7', '', 29),
    ('Light ID 8', 'Light ID 8', '', 30),
    ('Light ID 9', 'Light ID 9', '', 85),
    ('Light ID 10', 'Light ID 10', '', 86),
    ('Light ID 11', 'Light ID 11', '', 87),
    ('Light ID 12', 'Light ID 12', '', 88),
    ('Light ID 13', 'Light ID 13', '', 89),
    ('Light ID 14', 'Light ID 14', '', 90),
    ('Light ID 15', 'Light ID 15', '', 91),
    ('Light ID 16', 'Light ID 16', '', 92),
    ('Light ID 17', 'Light ID 17', '', 93),
    ('Light ID 18', 'Light ID 18', '', 94),
    ('Light ID 19', 'Light ID 19', '', 95),
    ('Light ID 20', 'Light ID 20', '', 96),
    ('', 'Light direct', ''),
    ('Ambient light direct', 'Ambient light direct', '', 54),
    ('Sunlight direct', 'Sunlight direct', '', 56),
    ('Light ID 1 direct', 'Light ID 1 direct', '', 58),
    ('Light ID 2 direct', 'Light ID 2 direct', '', 59),
    ('Light ID 3 direct', 'Light ID 3 direct', '', 60),
    ('Light ID 4 direct', 'Light ID 4 direct', '', 61),
    ('Light ID 5 direct', 'Light ID 5 direct', '', 62),
    ('Light ID 6 direct', 'Light ID 6 direct', '', 63),
    ('Light ID 7 direct', 'Light ID 7 direct', '', 64),
    ('Light ID 8 direct', 'Light ID 8 direct', '', 65),
    ('Light ID 9 direct', 'Light ID 9 direct', '', 97),
    ('Light ID 10 direct', 'Light ID 10 direct', '', 98),
    ('Light ID 11 direct', 'Light ID 11 direct', '', 99),
    ('Light ID 12 direct', 'Light ID 12 direct', '', 100),
    ('Light ID 13 direct', 'Light ID 13 direct', '', 101),
    ('Light ID 14 direct', 'Light ID 14 direct', '', 102),
    ('Light ID 15 direct', 'Light ID 15 direct', '', 103),
    ('Light ID 16 direct', 'Light ID 16 direct', '', 104),
    ('Light ID 17 direct', 'Light ID 17 direct', '', 105),
    ('Light ID 18 direct', 'Light ID 18 direct', '', 106),
    ('Light ID 19 direct', 'Light ID 19 direct', '', 107),
    ('Light ID 20 direct', 'Light ID 20 direct', '', 108),
    ('', 'Light indirect', ''),
    ('Ambient light indirect', 'Ambient light indirect', '', 55),
    ('Sunlight indirect', 'Sunlight indirect', '', 57),
    ('Light ID 1 indirect', 'Light ID 1 indirect', '', 66),
    ('Light ID 2 indirect', 'Light ID 2 indirect', '', 67),
    ('Light ID 3 indirect', 'Light ID 3 indirect', '', 68),
    ('Light ID 4 indirect', 'Light ID 4 indirect', '', 69),
    ('Light ID 5 indirect', 'Light ID 5 indirect', '', 70),
    ('Light ID 6 indirect', 'Light ID 6 indirect', '', 71),
    ('Light ID 7 indirect', 'Light ID 7 indirect', '', 72),
    ('Light ID 8 indirect', 'Light ID 8 indirect', '', 73),
    ('Light ID 9 indirect', 'Light ID 9 indirect', '', 109),
    ('Light ID 10 indirect', 'Light ID 10 indirect', '', 110),
    ('Light ID 11 indirect', 'Light ID 11 indirect', '', 111),
    ('Light ID 12 indirect', 'Light ID 12 indirect', '', 112),
    ('Light ID 13 indirect', 'Light ID 13 indirect', '', 113),
    ('Light ID 14 indirect', 'Light ID 14 indirect', '', 114),
    ('Light ID 15 indirect', 'Light ID 15 indirect', '', 115),
    ('Light ID 16 indirect', 'Light ID 16 indirect', '', 116),
    ('Light ID 17 indirect', 'Light ID 17 indirect', '', 117),
    ('Light ID 18 indirect', 'Light ID 18 indirect', '', 118),
    ('Light ID 19 indirect', 'Light ID 19 indirect', '', 119),
    ('Light ID 20 indirect', 'Light ID 20 indirect', '', 120),
    ('', 'Custom AOV', ''),
    ('Custom AOV 1', 'Custom AOV 1', '', 501),
    ('Custom AOV 2', 'Custom AOV 2', '', 502),
    ('Custom AOV 3', 'Custom AOV 3', '', 503),
    ('Custom AOV 4', 'Custom AOV 4', '', 504),
    ('Custom AOV 5', 'Custom AOV 5', '', 505),
    ('Custom AOV 6', 'Custom AOV 6', '', 506),
    ('Custom AOV 7', 'Custom AOV 7', '', 507),
    ('Custom AOV 8', 'Custom AOV 8', '', 508),
    ('Custom AOV 9', 'Custom AOV 9', '', 509),
    ('Custom AOV 10', 'Custom AOV 10', '', 510),
    ('Custom AOV 11', 'Custom AOV 11', '', 511),
    ('Custom AOV 12', 'Custom AOV 12', '', 512),
    ('Custom AOV 13', 'Custom AOV 13', '', 513),
    ('Custom AOV 14', 'Custom AOV 14', '', 514),
    ('Custom AOV 15', 'Custom AOV 15', '', 515),
    ('Custom AOV 16', 'Custom AOV 16', '', 516),
    ('Custom AOV 17', 'Custom AOV 17', '', 517),
    ('Custom AOV 18', 'Custom AOV 18', '', 518),
    ('Custom AOV 19', 'Custom AOV 19', '', 519),
    ('Custom AOV 20', 'Custom AOV 20', '', 520),
    ('', 'Global texture AOV', ''),
    ('Global texture AOV 1', 'Global texture AOV 1', '', 1101),
    ('Global texture AOV 2', 'Global texture AOV 2', '', 1102),
    ('Global texture AOV 3', 'Global texture AOV 3', '', 1103),
    ('Global texture AOV 4', 'Global texture AOV 4', '', 1104),
    ('Global texture AOV 5', 'Global texture AOV 5', '', 1105),
    ('Global texture AOV 6', 'Global texture AOV 6', '', 1106),
    ('Global texture AOV 7', 'Global texture AOV 7', '', 1107),
    ('Global texture AOV 8', 'Global texture AOV 8', '', 1108),
    ('Global texture AOV 9', 'Global texture AOV 9', '', 1109),
    ('Global texture AOV 10', 'Global texture AOV 10', '', 1110),
    ('Global texture AOV 11', 'Global texture AOV 11', '', 1111),
    ('Global texture AOV 12', 'Global texture AOV 12', '', 1112),
    ('Global texture AOV 13', 'Global texture AOV 13', '', 1113),
    ('Global texture AOV 14', 'Global texture AOV 14', '', 1114),
    ('Global texture AOV 15', 'Global texture AOV 15', '', 1115),
    ('Global texture AOV 16', 'Global texture AOV 16', '', 1116),
    ('Global texture AOV 17', 'Global texture AOV 17', '', 1117),
    ('Global texture AOV 18', 'Global texture AOV 18', '', 1118),
    ('Global texture AOV 19', 'Global texture AOV 19', '', 1119),
    ('Global texture AOV 20', 'Global texture AOV 20', '', 1120),
]


class OctaneOutputAOVsRenderAOVInput_OT_search_popup(bpy.types.Operator):
    bl_idname = "octane_render_aov.search_popup"
    bl_label = "Render AOV Input"
    bl_property = "default_value"

    default_value: EnumProperty(default="Beauty", update=None, description="The render AOV to blend. This must be enabled as a render AOV", items=OctaneOutputAOVsRenderAOVInput_no_heading_simplified_items)    

    def execute(self, context):
        context.active_node.inputs[OctaneOutputAOVsRenderAOVInput.bl_label].default_value = self.default_value
        return {"FINISHED"}

    def invoke(self, context, _event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {"FINISHED"}


class OctaneOutputAOVsRenderAOVInput_Override(OctaneOutputAOVsRenderAOVInput):
    default_value: EnumProperty(default="Beauty", update=OctaneBaseSocket.update_node_tree, description="The render AOV to blend. This must be enabled as a render AOV", items=OctaneOutputAOVsRenderAOVInput_simplified_items)

    def draw_prop(self, context, layout, text):
        c = layout.column()
        row = c.row()
        split = row.split(factor=0.4)
        c = split.column()
        c.label(text=text)
        split = split.split(factor=0.85)
        c = split.column()
        c.alignment = "LEFT"
        c.prop(self, "default_value", text="")
        split = split.split()
        c = split.column()
        c.operator("octane_render_aov.search_popup", icon="VIEWZOOM", text="")


_CLASSES.append(OctaneOutputAOVsRenderAOVInput_OT_search_popup)
utility.override_class(_CLASSES, OctaneOutputAOVsRenderAOVInput, OctaneOutputAOVsRenderAOVInput_Override)
