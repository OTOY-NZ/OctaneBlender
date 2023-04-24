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


class OctaneSheenLayerSheen(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerSheen"
    bl_label="Sheen"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=377)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The color of the sheen layer", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerSheenRoughness(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerSheenRoughness"
    bl_label="Roughness"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=387)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.200000, update=OctaneBaseSocket.update_node_tree, description="Roughness of the sheen layer", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerAffectRoughness(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerAffectRoughness"
    bl_label="Affect roughness"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=487)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness. Note that the affect roughness takes the maximum affect roughness  along the stack", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000006
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerBump(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerBump"
    bl_label="Bump"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerNormal(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerNormal"
    bl_label="Normal"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=119)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerOpacity(OctaneBaseSocket):
    bl_idname="OctaneSheenLayerOpacity"
    bl_label="Layer opacity"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Opacity channel controlling the transparency of the layer via greyscale texture", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSheenLayerGroupRoughness(OctaneGroupTitleSocket):
    bl_idname="OctaneSheenLayerGroupRoughness"
    bl_label="[OctaneGroupTitle]Roughness"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Roughness;Affect roughness;")

class OctaneSheenLayerGroupGeometryProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneSheenLayerGroupGeometryProperties"
    bl_label="[OctaneGroupTitle]Geometry Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Bump;Normal;")

class OctaneSheenLayerGroupLayerProperties(OctaneGroupTitleSocket):
    bl_idname="OctaneSheenLayerGroupLayerProperties"
    bl_label="[OctaneGroupTitle]Layer Properties"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Layer opacity;")

class OctaneSheenLayer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSheenLayer"
    bl_label="Sheen layer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=142)
    octane_socket_list: StringProperty(name="Socket List", default="Sheen;Roughness;Affect roughness;Bump;Normal;Layer opacity;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=6)

    def init(self, context):
        self.inputs.new("OctaneSheenLayerSheen", OctaneSheenLayerSheen.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupRoughness", OctaneSheenLayerGroupRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerSheenRoughness", OctaneSheenLayerSheenRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerAffectRoughness", OctaneSheenLayerAffectRoughness.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupGeometryProperties", OctaneSheenLayerGroupGeometryProperties.bl_label).init()
        self.inputs.new("OctaneSheenLayerBump", OctaneSheenLayerBump.bl_label).init()
        self.inputs.new("OctaneSheenLayerNormal", OctaneSheenLayerNormal.bl_label).init()
        self.inputs.new("OctaneSheenLayerGroupLayerProperties", OctaneSheenLayerGroupLayerProperties.bl_label).init()
        self.inputs.new("OctaneSheenLayerOpacity", OctaneSheenLayerOpacity.bl_label).init()
        self.outputs.new("OctaneMaterialLayerOutSocket", "Material layer out").init()


_CLASSES=[
    OctaneSheenLayerSheen,
    OctaneSheenLayerSheenRoughness,
    OctaneSheenLayerAffectRoughness,
    OctaneSheenLayerBump,
    OctaneSheenLayerNormal,
    OctaneSheenLayerOpacity,
    OctaneSheenLayerGroupRoughness,
    OctaneSheenLayerGroupGeometryProperties,
    OctaneSheenLayerGroupLayerProperties,
    OctaneSheenLayer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
