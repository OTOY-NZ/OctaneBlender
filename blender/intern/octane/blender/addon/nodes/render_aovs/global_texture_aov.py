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


class OctaneGlobalTextureAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneGlobalTextureAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlobalTextureAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneGlobalTextureAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Global texture 1", "Global texture 1", "", 0),
        ("Global texture 2", "Global texture 2", "", 1),
        ("Global texture 3", "Global texture 3", "", 2),
        ("Global texture 4", "Global texture 4", "", 3),
        ("Global texture 5", "Global texture 5", "", 4),
        ("Global texture 6", "Global texture 6", "", 5),
        ("Global texture 7", "Global texture 7", "", 6),
        ("Global texture 8", "Global texture 8", "", 7),
        ("Global texture 9", "Global texture 9", "", 8),
        ("Global texture 10", "Global texture 10", "", 9),
        ("Global texture 11", "Global texture 11", "", 10),
        ("Global texture 12", "Global texture 12", "", 11),
        ("Global texture 13", "Global texture 13", "", 12),
        ("Global texture 14", "Global texture 14", "", 13),
        ("Global texture 15", "Global texture 15", "", 14),
        ("Global texture 16", "Global texture 16", "", 15),
        ("Global texture 17", "Global texture 17", "", 16),
        ("Global texture 18", "Global texture 18", "", 17),
        ("Global texture 19", "Global texture 19", "", 18),
        ("Global texture 20", "Global texture 20", "", 19),
    ]
    default_value: EnumProperty(default="Global texture 1", update=OctaneBaseSocket.update_node_tree, description="The ID or index of the global texture AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlobalTextureAOVTexture(OctaneBaseSocket):
    bl_idname="OctaneGlobalTextureAOVTexture"
    bl_label="Texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlobalTextureAOVAlphachannel(OctaneBaseSocket):
    bl_idname="OctaneGlobalTextureAOVAlphachannel"
    bl_label="Alpha channel"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlobalTextureAOVIncludeEnvironment(OctaneBaseSocket):
    bl_idname="OctaneGlobalTextureAOVIncludeEnvironment"
    bl_label="Include environment"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=634)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the texture will also be evaluated for camera rays that leave the scene. This can be useful for textures that need to be evaluated over the whole screen")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGlobalTextureAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGlobalTextureAOV"
    bl_label="Global texture AOV"
    bl_width_default=200
    octane_render_pass_id={0: 1101, 1: 1102, 2: 1103, 3: 1104, 4: 1105, 5: 1106, 6: 1107, 7: 1108, 8: 1109, 9: 1110, 10: 1111, 11: 1112, 12: 1113, 13: 1114, 14: 1115, 15: 1116, 16: 1117, 17: 1118, 18: 1119, 19: 1120, }
    octane_render_pass_name={0: "Global texture AOV 1", 1: "Global texture AOV 2", 2: "Global texture AOV 3", 3: "Global texture AOV 4", 4: "Global texture AOV 5", 5: "Global texture AOV 6", 6: "Global texture AOV 7", 7: "Global texture AOV 8", 8: "Global texture AOV 9", 9: "Global texture AOV 10", 10: "Global texture AOV 11", 11: "Global texture AOV 12", 12: "Global texture AOV 13", 13: "Global texture AOV 14", 14: "Global texture AOV 15", 15: "Global texture AOV 16", 16: "Global texture AOV 17", 17: "Global texture AOV 18", 18: "Global texture AOV 19", 19: "Global texture AOV 20", }
    octane_render_pass_short_name={0: "Glob1", 1: "Glob2", 2: "Glob3", 3: "Glob4", 4: "Glob5", 5: "Glob6", 6: "Glob7", 7: "Glob8", 8: "Glob9", 9: "Glob10", 10: "Glob11", 11: "Glob12", 12: "Glob13", 13: "Glob14", 14: "Glob15", 15: "Glob16", 16: "Glob17", 17: "Glob18", 18: "Glob19", 19: "Glob20", }
    octane_render_pass_description={0: "Global texture AOV 1", 1: "Global texture AOV 2", 2: "Global texture AOV 3", 3: "Global texture AOV 4", 4: "Global texture AOV 5", 5: "Global texture AOV 6", 6: "Global texture AOV 7", 7: "Global texture AOV 8", 8: "Global texture AOV 9", 9: "Global texture AOV 10", 10: "Global texture AOV 11", 11: "Global texture AOV 12", 12: "Global texture AOV 13", 13: "Global texture AOV 14", 14: "Global texture AOV 15", 15: "Global texture AOV 16", 16: "Global texture AOV 17", 17: "Global texture AOV 18", 18: "Global texture AOV 19", 19: "Global texture AOV 20", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=199)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;Texture;Alpha channel;Include environment;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneGlobalTextureAOVEnabled", OctaneGlobalTextureAOVEnabled.bl_label).init()
        self.inputs.new("OctaneGlobalTextureAOVSubType", OctaneGlobalTextureAOVSubType.bl_label).init()
        self.inputs.new("OctaneGlobalTextureAOVTexture", OctaneGlobalTextureAOVTexture.bl_label).init()
        self.inputs.new("OctaneGlobalTextureAOVAlphachannel", OctaneGlobalTextureAOVAlphachannel.bl_label).init()
        self.inputs.new("OctaneGlobalTextureAOVIncludeEnvironment", OctaneGlobalTextureAOVIncludeEnvironment.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_CLASSES=[
    OctaneGlobalTextureAOVEnabled,
    OctaneGlobalTextureAOVSubType,
    OctaneGlobalTextureAOVTexture,
    OctaneGlobalTextureAOVAlphachannel,
    OctaneGlobalTextureAOVIncludeEnvironment,
    OctaneGlobalTextureAOV,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
