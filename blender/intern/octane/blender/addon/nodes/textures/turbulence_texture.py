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


class OctaneTurbulenceTexturePower(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTexturePower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=138)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="power")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureOffset(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOffset"
    bl_label="Offset"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="offset")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Coordinate offset", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureOctaves(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=121)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="octaves")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureOmega(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureOmega"
    bl_label="Omega"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=123)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="omega")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Difference per octave interval", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=67
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="transform")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=75
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="projection")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureTurbulence(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureTurbulence"
    bl_label="Use turbulence"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=247)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="turbulence")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="On - turbulence. Off - regular noise")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureInvert(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="invert")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Invert output")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTextureGamma(OctaneBaseSocket):
    bl_idname="OctaneTurbulenceTextureGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=57)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="gamma")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2100003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTurbulenceTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTurbulenceTexture"
    bl_label="Turbulence texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=22)
    octane_socket_list: StringProperty(name="Socket List", default="Power;Offset;Octaves;Omega;UVW transform;Projection;Use turbulence;Invert;Gamma;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

    def init(self, context):
        self.inputs.new("OctaneTurbulenceTexturePower", OctaneTurbulenceTexturePower.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOffset", OctaneTurbulenceTextureOffset.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOctaves", OctaneTurbulenceTextureOctaves.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureOmega", OctaneTurbulenceTextureOmega.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureTransform", OctaneTurbulenceTextureTransform.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureProjection", OctaneTurbulenceTextureProjection.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureTurbulence", OctaneTurbulenceTextureTurbulence.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureInvert", OctaneTurbulenceTextureInvert.bl_label).init()
        self.inputs.new("OctaneTurbulenceTextureGamma", OctaneTurbulenceTextureGamma.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneTurbulenceTexturePower,
    OctaneTurbulenceTextureOffset,
    OctaneTurbulenceTextureOctaves,
    OctaneTurbulenceTextureOmega,
    OctaneTurbulenceTextureTransform,
    OctaneTurbulenceTextureProjection,
    OctaneTurbulenceTextureTurbulence,
    OctaneTurbulenceTextureInvert,
    OctaneTurbulenceTextureGamma,
    OctaneTurbulenceTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
