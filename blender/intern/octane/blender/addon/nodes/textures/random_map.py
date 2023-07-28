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


class OctaneRandomMapInput(OctaneBaseSocket):
    bl_idname="OctaneRandomMapInput"
    bl_label="Input texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT
    octane_pin_name="input"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomMapInputScale(OctaneBaseSocket):
    bl_idname="OctaneRandomMapInputScale"
    bl_label="Input scale"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT_SCALE
    octane_pin_name="inputScale"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Scale factor for the input texture values", min=1, max=65536, soft_min=1, soft_max=65536, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomMapNoiseType(OctaneBaseSocket):
    bl_idname="OctaneRandomMapNoiseType"
    bl_label="Noise function"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_NOISE_TYPE
    octane_pin_name="noiseType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Perlin", "Perlin", "", 0),
        ("Unsigned perlin", "Unsigned perlin", "", 1),
        ("Cell", "Cell", "", 2),
        ("Hash", "Hash", "", 3),
    ]
    default_value: EnumProperty(default="Perlin", update=OctaneBaseSocket.update_node_tree, description="Noise function", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneRandomMap(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneRandomMap"
    bl_label="Random map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneRandomMapInput,OctaneRandomMapInputScale,OctaneRandomMapNoiseType,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_RANDOM_MAP
    octane_socket_list=["Input texture", "Input scale", "Noise function", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=3

    def init(self, context):
        self.inputs.new("OctaneRandomMapInput", OctaneRandomMapInput.bl_label).init()
        self.inputs.new("OctaneRandomMapInputScale", OctaneRandomMapInputScale.bl_label).init()
        self.inputs.new("OctaneRandomMapNoiseType", OctaneRandomMapNoiseType.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneRandomMapInput,
    OctaneRandomMapInputScale,
    OctaneRandomMapNoiseType,
    OctaneRandomMap,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
