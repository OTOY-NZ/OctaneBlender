##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneDiffuseLayerEnabled(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLED
    octane_pin_name="enabled"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Whether this layer is applied or skipped")
    octane_hide_value=False
    octane_min_version=13000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerDiffuse(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerDiffuse"
    bl_label="Diffuse"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_RGB
    octane_default_node_name="OctaneRGBColor"
    octane_pin_id=consts.PinID.P_DIFFUSE
    octane_pin_name="diffuse"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.700000, 0.700000, 0.700000), update=OctaneBaseSocket.update_node_tree, description="The diffuse color of the material", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerTransmission(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerTransmission"
    bl_label="Transmission"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TRANSMISSION
    octane_pin_name="transmission"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerBrdf(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerBrdf"
    bl_label="BRDF model"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_BRDF
    octane_pin_name="brdf"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Octane", "Octane", "", 0),
        ("Lambertian", "Lambertian", "", 1),
        ("Oren-Nayar", "Oren-Nayar", "", 2),
    ]
    default_value: EnumProperty(default="Octane", update=OctaneBaseSocket.update_node_tree, description="BRDF model", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerRoughness(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_ROUGHNESS
    octane_pin_name="roughness"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the diffuse layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerBump(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_BUMP
    octane_pin_name="bump"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerBumpHeight(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerBumpHeight"
    bl_label="Bump height"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BUMP_HEIGHT
    octane_pin_name="bumpHeight"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The height represented by a normalized value of 1.0 in the bump texture. 0 disables bump mapping, negative values will invert the bump map", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=13000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerNormal(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_NORMAL
    octane_pin_name="normal"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneDiffuseLayerOpacity"
    bl_label="Layer opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_OPACITY
    octane_pin_name="opacity"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via grayscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype=consts.factor_property_subtype())
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDiffuseLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;")

class OctaneDiffuseLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Bump height;Normal;")

class OctaneDiffuseLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneDiffuseLayerGroupLayerProperties"
    bl_label="[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")

class OctaneDiffuseLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneDiffuseLayer"
    bl_label="Diffuse layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneDiffuseLayerEnabled,OctaneDiffuseLayerDiffuse,OctaneDiffuseLayerTransmission,OctaneDiffuseLayerBrdf,OctaneDiffuseLayerGroupRoughness,OctaneDiffuseLayerRoughness,OctaneDiffuseLayerGroupGeometryProperties,OctaneDiffuseLayerBump,OctaneDiffuseLayerBumpHeight,OctaneDiffuseLayerNormal,OctaneDiffuseLayerGroupLayerProperties,OctaneDiffuseLayerOpacity,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_DIFFUSE_LAYER
    octane_socket_list=["Enabled", "Diffuse", "Transmission", "BRDF model", "Roughness", "Bump", "Bump height", "Normal", "Layer opacity", ]
    octane_attribute_list=["a_compatibility_version", ]
    octane_attribute_config={"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count=9

    compatibility_mode_infos=[
        ("Latest (2023.1)", "Latest (2023.1)", """(null)""", 13000000),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """The "Octane" and "Lambertian" BRDF models are swapped. Legacy behaviour for bump map strength is active and bump map height is ignored.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000006, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):
        self.inputs.new("OctaneDiffuseLayerEnabled", OctaneDiffuseLayerEnabled.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerDiffuse", OctaneDiffuseLayerDiffuse.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerTransmission", OctaneDiffuseLayerTransmission.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerBrdf", OctaneDiffuseLayerBrdf.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupRoughness", OctaneDiffuseLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerRoughness", OctaneDiffuseLayerRoughness.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupGeometryProperties", OctaneDiffuseLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerBump", OctaneDiffuseLayerBump.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerBumpHeight", OctaneDiffuseLayerBumpHeight.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerNormal", OctaneDiffuseLayerNormal.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerGroupLayerProperties", OctaneDiffuseLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneDiffuseLayerOpacity", OctaneDiffuseLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES=[
    OctaneDiffuseLayerEnabled,
    OctaneDiffuseLayerDiffuse,
    OctaneDiffuseLayerTransmission,
    OctaneDiffuseLayerBrdf,
    OctaneDiffuseLayerRoughness,
    OctaneDiffuseLayerBump,
    OctaneDiffuseLayerBumpHeight,
    OctaneDiffuseLayerNormal,
    OctaneDiffuseLayerOpacity,
    OctaneDiffuseLayerGroupRoughness,
    OctaneDiffuseLayerGroupGeometryProperties,
    OctaneDiffuseLayerGroupLayerProperties,
    OctaneDiffuseLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
