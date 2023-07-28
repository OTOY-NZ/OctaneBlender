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


class OctaneNoiseTexturePower(OctaneBaseSocket):
    bl_idname="OctaneNoiseTexturePower"
    bl_label="Power"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_POWER
    octane_pin_name="power"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Power/brightness", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000014
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureNoiseType(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureNoiseType"
    bl_label="Noise type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_NOISE_TYPE
    octane_pin_name="noiseType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Perlin", "Perlin", "", 0),
        ("Turbulence", "Turbulence", "", 1),
        ("Circular", "Circular", "", 2),
        ("Chips", "Chips", "", 3),
        ("Voronoi", "Voronoi", "", 4),
    ]
    default_value: EnumProperty(default="Perlin", update=OctaneBaseSocket.update_node_tree, description="Noise type", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureOctaves(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureOctaves"
    bl_label="Octaves"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_OCTAVES
    octane_pin_name="octaves"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="Number of octaves", min=1, max=16, soft_min=1, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureOmega(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureOmega"
    bl_label="Omega"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_OMEGA
    octane_pin_name="omega"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Difference per octave interval", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureInvert(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_INVERT
    octane_pin_name="invert"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Inert output")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureGamma(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureGamma"
    bl_label="Gamma"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_GAMMA
    octane_pin_name="gamma"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Output gamma", min=0.010000, max=100.000000, soft_min=0.010000, soft_max=100.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTextureContrast(OctaneBaseSocket):
    bl_idname="OctaneNoiseTextureContrast"
    bl_label="Contrast"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CONTRAST
    octane_pin_name="contrast"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Output contrast", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneNoiseTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneNoiseTexture"
    bl_label="Noise texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneNoiseTexturePower,OctaneNoiseTextureNoiseType,OctaneNoiseTextureOctaves,OctaneNoiseTextureOmega,OctaneNoiseTextureTransform,OctaneNoiseTextureProjection,OctaneNoiseTextureInvert,OctaneNoiseTextureGamma,OctaneNoiseTextureContrast,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_NOISE
    octane_socket_list=["Power", "Noise type", "Octaves", "Omega", "UVW transform", "Projection", "Invert", "Gamma", "Contrast", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneNoiseTexturePower", OctaneNoiseTexturePower.bl_label).init()
        self.inputs.new("OctaneNoiseTextureNoiseType", OctaneNoiseTextureNoiseType.bl_label).init()
        self.inputs.new("OctaneNoiseTextureOctaves", OctaneNoiseTextureOctaves.bl_label).init()
        self.inputs.new("OctaneNoiseTextureOmega", OctaneNoiseTextureOmega.bl_label).init()
        self.inputs.new("OctaneNoiseTextureTransform", OctaneNoiseTextureTransform.bl_label).init()
        self.inputs.new("OctaneNoiseTextureProjection", OctaneNoiseTextureProjection.bl_label).init()
        self.inputs.new("OctaneNoiseTextureInvert", OctaneNoiseTextureInvert.bl_label).init()
        self.inputs.new("OctaneNoiseTextureGamma", OctaneNoiseTextureGamma.bl_label).init()
        self.inputs.new("OctaneNoiseTextureContrast", OctaneNoiseTextureContrast.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneNoiseTexturePower,
    OctaneNoiseTextureNoiseType,
    OctaneNoiseTextureOctaves,
    OctaneNoiseTextureOmega,
    OctaneNoiseTextureTransform,
    OctaneNoiseTextureProjection,
    OctaneNoiseTextureInvert,
    OctaneNoiseTextureGamma,
    OctaneNoiseTextureContrast,
    OctaneNoiseTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
