##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneRenderAOVOutputInput(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVOutputInput"
    bl_label="Input"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=82)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Main", "Main", "", 0),
        ("Beauty AOVs|Emitters", "Beauty AOVs|Emitters", "", 1),
        ("Beauty AOVs|Environment", "Beauty AOVs|Environment", "", 2),
        ("Beauty AOVs|Diffuse", "Beauty AOVs|Diffuse", "", 3),
        ("Beauty AOVs|Diffuse direct", "Beauty AOVs|Diffuse direct", "", 4),
        ("Beauty AOVs|Diffuse indirect", "Beauty AOVs|Diffuse indirect", "", 5),
        ("Beauty AOVs|Diffuse filter (beauty)", "Beauty AOVs|Diffuse filter (beauty)", "", 6),
        ("Beauty AOVs|Reflection", "Beauty AOVs|Reflection", "", 7),
        ("Beauty AOVs|Reflection direct", "Beauty AOVs|Reflection direct", "", 8),
        ("Beauty AOVs|Reflection indirect", "Beauty AOVs|Reflection indirect", "", 9),
        ("Beauty AOVs|Reflection filter (beauty)", "Beauty AOVs|Reflection filter (beauty)", "", 10),
        ("Beauty AOVs|Refraction", "Beauty AOVs|Refraction", "", 11),
        ("Beauty AOVs|Refraction filter (beauty)", "Beauty AOVs|Refraction filter (beauty)", "", 12),
        ("Beauty AOVs|Transmission", "Beauty AOVs|Transmission", "", 13),
        ("Beauty AOVs|Transmission filter (beauty)", "Beauty AOVs|Transmission filter (beauty)", "", 14),
        ("Beauty AOVs|Subsurface scattering", "Beauty AOVs|Subsurface scattering", "", 15),
        ("Beauty AOVs|Volume", "Beauty AOVs|Volume", "", 35),
        ("Beauty AOVs|Volume mask", "Beauty AOVs|Volume mask", "", 36),
        ("Beauty AOVs|Volume emission", "Beauty AOVs|Volume emission", "", 37),
        ("Beauty AOVs|Volume Z-depth front", "Beauty AOVs|Volume Z-depth front", "", 38),
        ("Beauty AOVs|Volume Z-depth back", "Beauty AOVs|Volume Z-depth back", "", 39),
        ("Beauty AOVs|Shadow", "Beauty AOVs|Shadow", "", 32),
        ("Beauty AOVs|Irradiance", "Beauty AOVs|Irradiance", "", 33),
        ("Beauty AOVs|Light direction", "Beauty AOVs|Light direction", "", 34),
        ("Post processing AOVs|Post processing", "Post processing AOVs|Post processing", "", 16),
        ("Beauty AOVs|Noise", "Beauty AOVs|Noise", "", 31),
        ("Render layer AOVs|Layer shadows", "Render layer AOVs|Layer shadows", "", 17),
        ("Render layer AOVs|Black layer shadows", "Render layer AOVs|Black layer shadows", "", 18),
        ("Render layer AOVs|Layer reflections", "Render layer AOVs|Layer reflections", "", 20),
        ("Lighting AOVs|Ambient light", "Lighting AOVs|Ambient light", "", 21),
        ("Lighting AOVs|Ambient light direct", "Lighting AOVs|Ambient light direct", "", 54),
        ("Lighting AOVs|Ambient light indirect", "Lighting AOVs|Ambient light indirect", "", 55),
        ("Lighting AOVs|Sunlight", "Lighting AOVs|Sunlight", "", 22),
        ("Lighting AOVs|Sunlight direct", "Lighting AOVs|Sunlight direct", "", 56),
        ("Lighting AOVs|Sunlight indirect", "Lighting AOVs|Sunlight indirect", "", 57),
        ("Lighting AOVs|Light ID 1", "Lighting AOVs|Light ID 1", "", 23),
        ("Lighting AOVs|Light ID 1 direct", "Lighting AOVs|Light ID 1 direct", "", 58),
        ("Lighting AOVs|Light ID 1 indirect", "Lighting AOVs|Light ID 1 indirect", "", 66),
        ("Lighting AOVs|Light ID 2", "Lighting AOVs|Light ID 2", "", 24),
        ("Lighting AOVs|Light ID 2 direct", "Lighting AOVs|Light ID 2 direct", "", 59),
        ("Lighting AOVs|Light ID 2 indirect", "Lighting AOVs|Light ID 2 indirect", "", 67),
        ("Lighting AOVs|Light ID 3", "Lighting AOVs|Light ID 3", "", 25),
        ("Lighting AOVs|Light ID 3 direct", "Lighting AOVs|Light ID 3 direct", "", 60),
        ("Lighting AOVs|Light ID 3 indirect", "Lighting AOVs|Light ID 3 indirect", "", 68),
        ("Lighting AOVs|Light ID 4", "Lighting AOVs|Light ID 4", "", 26),
        ("Lighting AOVs|Light ID 4 direct", "Lighting AOVs|Light ID 4 direct", "", 61),
        ("Lighting AOVs|Light ID 4 indirect", "Lighting AOVs|Light ID 4 indirect", "", 69),
        ("Lighting AOVs|Light ID 5", "Lighting AOVs|Light ID 5", "", 27),
        ("Lighting AOVs|Light ID 5 direct", "Lighting AOVs|Light ID 5 direct", "", 62),
        ("Lighting AOVs|Light ID 5 indirect", "Lighting AOVs|Light ID 5 indirect", "", 70),
        ("Lighting AOVs|Light ID 6", "Lighting AOVs|Light ID 6", "", 28),
        ("Lighting AOVs|Light ID 6 direct", "Lighting AOVs|Light ID 6 direct", "", 63),
        ("Lighting AOVs|Light ID 6 indirect", "Lighting AOVs|Light ID 6 indirect", "", 71),
        ("Lighting AOVs|Light ID 7", "Lighting AOVs|Light ID 7", "", 29),
        ("Lighting AOVs|Light ID 7 direct", "Lighting AOVs|Light ID 7 direct", "", 64),
        ("Lighting AOVs|Light ID 7 indirect", "Lighting AOVs|Light ID 7 indirect", "", 72),
        ("Lighting AOVs|Light ID 8", "Lighting AOVs|Light ID 8", "", 30),
        ("Lighting AOVs|Light ID 8 direct", "Lighting AOVs|Light ID 8 direct", "", 65),
        ("Lighting AOVs|Light ID 8 indirect", "Lighting AOVs|Light ID 8 indirect", "", 73),
        ("Denoiser AOVs|Denoised beauty", "Denoiser AOVs|Denoised beauty", "", 43),
        ("Denoiser AOVs|Denoised diffuse direct", "Denoiser AOVs|Denoised diffuse direct", "", 44),
        ("Denoiser AOVs|Denoised diffuse indirect", "Denoiser AOVs|Denoised diffuse indirect", "", 45),
        ("Denoiser AOVs|Denoised reflection direct", "Denoiser AOVs|Denoised reflection direct", "", 46),
        ("Denoiser AOVs|Denoised reflection indirect", "Denoiser AOVs|Denoised reflection indirect", "", 47),
        ("Denoiser AOVs|Denoised emission", "Denoiser AOVs|Denoised emission", "", 76),
        ("Denoiser AOVs|Denoised remainder", "Denoiser AOVs|Denoised remainder", "", 49),
        ("Denoiser AOVs|Denoised volume", "Denoiser AOVs|Denoised volume", "", 74),
        ("Denoiser AOVs|Denoised volume emission", "Denoiser AOVs|Denoised volume emission", "", 75),
        ("Custom AOVs|Custom AOV 1", "Custom AOVs|Custom AOV 1", "", 501),
        ("Custom AOVs|Custom AOV 2", "Custom AOVs|Custom AOV 2", "", 502),
        ("Custom AOVs|Custom AOV 3", "Custom AOVs|Custom AOV 3", "", 503),
        ("Custom AOVs|Custom AOV 4", "Custom AOVs|Custom AOV 4", "", 504),
        ("Custom AOVs|Custom AOV 5", "Custom AOVs|Custom AOV 5", "", 505),
        ("Custom AOVs|Custom AOV 6", "Custom AOVs|Custom AOV 6", "", 506),
        ("Custom AOVs|Custom AOV 7", "Custom AOVs|Custom AOV 7", "", 507),
        ("Custom AOVs|Custom AOV 8", "Custom AOVs|Custom AOV 8", "", 508),
        ("Custom AOVs|Custom AOV 9", "Custom AOVs|Custom AOV 9", "", 509),
        ("Custom AOVs|Custom AOV 10", "Custom AOVs|Custom AOV 10", "", 510),
        ("Material AOVs|Opacity", "Material AOVs|Opacity", "", 1016),
        ("Material AOVs|Roughness", "Material AOVs|Roughness", "", 1018),
        ("Material AOVs|Index of refraction", "Material AOVs|Index of refraction", "", 1019),
        ("Material AOVs|Diffuse filter (info)", "Material AOVs|Diffuse filter (info)", "", 1020),
        ("Material AOVs|Reflection filter (info)", "Material AOVs|Reflection filter (info)", "", 1021),
        ("Material AOVs|Refraction filter (info)", "Material AOVs|Refraction filter (info)", "", 1022),
        ("Material AOVs|Transmission filter (info)", "Material AOVs|Transmission filter (info)", "", 1023),
        ("Global texture AOVs|Global texture AOV 1", "Global texture AOVs|Global texture AOV 1", "", 1101),
        ("Global texture AOVs|Global texture AOV 2", "Global texture AOVs|Global texture AOV 2", "", 1102),
        ("Global texture AOVs|Global texture AOV 3", "Global texture AOVs|Global texture AOV 3", "", 1103),
        ("Global texture AOVs|Global texture AOV 4", "Global texture AOVs|Global texture AOV 4", "", 1104),
        ("Global texture AOVs|Global texture AOV 5", "Global texture AOVs|Global texture AOV 5", "", 1105),
        ("Global texture AOVs|Global texture AOV 6", "Global texture AOVs|Global texture AOV 6", "", 1106),
        ("Global texture AOVs|Global texture AOV 7", "Global texture AOVs|Global texture AOV 7", "", 1107),
        ("Global texture AOVs|Global texture AOV 8", "Global texture AOVs|Global texture AOV 8", "", 1108),
        ("Global texture AOVs|Global texture AOV 9", "Global texture AOVs|Global texture AOV 9", "", 1109),
        ("Global texture AOVs|Global texture AOV 10", "Global texture AOVs|Global texture AOV 10", "", 1110),
        ("Info AOVs|Geometric normal", "Info AOVs|Geometric normal", "", 1000),
        ("Info AOVs|Smooth normal", "Info AOVs|Smooth normal", "", 1008),
        ("Info AOVs|Shading normal", "Info AOVs|Shading normal", "", 1001),
        ("Info AOVs|Tangent normal", "Info AOVs|Tangent normal", "", 1015),
        ("Info AOVs|Z-depth", "Info AOVs|Z-depth", "", 1003),
        ("Info AOVs|Position", "Info AOVs|Position", "", 1002),
        ("Info AOVs|UV coordinates", "Info AOVs|UV coordinates", "", 1005),
        ("Info AOVs|Texture tangent", "Info AOVs|Texture tangent", "", 1006),
        ("Info AOVs|Motion vector", "Info AOVs|Motion vector", "", 1011),
        ("Info AOVs|Material ID", "Info AOVs|Material ID", "", 1004),
        ("Info AOVs|Object ID", "Info AOVs|Object ID", "", 1009),
        ("Info AOVs|Baking group ID", "Info AOVs|Baking group ID", "", 1017),
        ("Info AOVs|Light pass ID", "Info AOVs|Light pass ID", "", 1014),
        ("Info AOVs|Render layer ID", "Info AOVs|Render layer ID", "", 1012),
        ("Info AOVs|Render layer mask", "Info AOVs|Render layer mask", "", 1013),
        ("Info AOVs|Wireframe", "Info AOVs|Wireframe", "", 1007),
        ("Info AOVs|Ambient occlusion", "Info AOVs|Ambient occlusion", "", 1010),
        ("Info AOVs|Object layer color", "Info AOVs|Object layer color", "", 1024),
        ("Info AOVs normalized|Geometric normal normalized", "Info AOVs normalized|Geometric normal normalized", "", 11002),
        ("Info AOVs normalized|Smooth normal normalized", "Info AOVs normalized|Smooth normal normalized", "", 11000),
        ("Info AOVs normalized|Shading normal normalized", "Info AOVs normalized|Shading normal normalized", "", 11003),
        ("Info AOVs normalized|Tangent normal normalized", "Info AOVs normalized|Tangent normal normalized", "", 11001),
        ("Info AOVs normalized|Z-depth normalized", "Info AOVs normalized|Z-depth normalized", "", 11005),
        ("Info AOVs normalized|Position normalized", "Info AOVs normalized|Position normalized", "", 11004),
        ("Info AOVs normalized|UV coordinates normalized", "Info AOVs normalized|UV coordinates normalized", "", 11006),
        ("Info AOVs normalized|Texture tangent normalized", "Info AOVs normalized|Texture tangent normalized", "", 11008),
        ("Info AOVs normalized|Motion vector normalized", "Info AOVs normalized|Motion vector normalized", "", 11007),
    ]
    default_value: EnumProperty(default="Main", update=None, description="Select a render pass from the list of all available render passes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVOutputOutputChannels(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVOutputOutputChannels"
    bl_label="Output channels"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=615)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("RGBA", "RGBA", "", 0),
        ("RGB", "RGB", "", 1),
        ("ALPHA", "ALPHA", "", 2),
    ]
    default_value: EnumProperty(default="RGBA", update=None, description="Select output channels type of this node. Can be set to one of enum ChannelGroups", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVOutputImager(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVOutputImager"
    bl_label="Enable imager"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=78)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, The imager settings is applied on the final AOV output. Otherwise ignored  Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVOutputPostproc(OctaneBaseSocket):
    bl_idname="OctaneRenderAOVOutputPostproc"
    bl_label="Enable post processing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=136)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If enabled, The post processing settings is applied on the final AOV output. Otherwise ignored Only used/vaild if this node is the root output AOV node (I.e. directly connected to the AOV output group node)")
    octane_hide_value=False
    octane_min_version=10021000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRenderAOVOutputGroupOutputSettings(OctaneGroupTitleSocket):
    bl_idname="OctaneRenderAOVOutputGroupOutputSettings"
    bl_label="[OctaneGroupTitle]Output settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable imager;Enable post processing;")

class OctaneRenderAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRenderAOVOutput"
    bl_label="Render AOV output"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=169)
    octane_socket_list: StringProperty(name="Socket List", default="Input;Output channels;Enable imager;Enable post processing;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneRenderAOVOutputInput", OctaneRenderAOVOutputInput.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputOutputChannels", OctaneRenderAOVOutputOutputChannels.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputGroupOutputSettings", OctaneRenderAOVOutputGroupOutputSettings.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputImager", OctaneRenderAOVOutputImager.bl_label).init()
        self.inputs.new("OctaneRenderAOVOutputPostproc", OctaneRenderAOVOutputPostproc.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "AOV output out").init()


_classes=[
    OctaneRenderAOVOutputInput,
    OctaneRenderAOVOutputOutputChannels,
    OctaneRenderAOVOutputImager,
    OctaneRenderAOVOutputPostproc,
    OctaneRenderAOVOutputGroupOutputSettings,
    OctaneRenderAOVOutput,
]

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####

from ...utils import utility

OctaneRenderAOVOutputInput_simplified_items = utility.make_blender_style_enum_items(OctaneRenderAOVOutputInput.items)

class OctaneRenderAOVOutputInput_Override(OctaneRenderAOVOutputInput):
    default_value: EnumProperty(default="Main", update=None, description="Select a render pass from the list of all available render passes", items=OctaneRenderAOVOutputInput_simplified_items)

utility.override_class(_classes, OctaneRenderAOVOutputInput, OctaneRenderAOVOutputInput_Override)  