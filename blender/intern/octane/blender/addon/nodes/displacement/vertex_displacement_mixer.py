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


class OctaneVertexDisplacementMixer(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVertexDisplacementMixer"
    bl_label="Vertex displacement mixer"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_VERTEX_DISPLACEMENT_MIXER
    octane_socket_list=[]
    octane_attribute_list=["a_displacement_count", ]
    octane_attribute_config={"a_displacement_count": [consts.AttributeID.A_DISPLACEMENT_COUNT, "displacementCount", consts.AttributeType.AT_INT], }
    octane_static_pin_count=0

    a_displacement_count: IntProperty(name="Displacement count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of vertex displacements to mix")

    def init(self, context):
        self.outputs.new("OctaneDisplacementOutSocket", "Displacement out").init()


_CLASSES=[
    OctaneVertexDisplacementMixer,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

from octane.utils import utility
from octane.nodes.base_socket import OctanePatternInput


class OctaneVertexDisplacementMixerBlendWeightMovableInput(OctanePatternInput):
    bl_idname="OctaneVertexDisplacementMixerBlendWeightMovableInput"
    bl_label="Blend weight"
    octane_input_pattern=r"Blend weight \d+"
    octane_input_format_pattern="Blend weight {}"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False


class OctaneVertexDisplacementMixerDisplacementMovableInput(OctaneMovableInput):
    bl_idname="OctaneVertexDisplacementMixerDisplacementMovableInput"
    bl_label="Displacement"
    octane_movable_input_count_attribute_name="a_displacement_count"
    octane_input_pattern=r"Displacement \d+"
    octane_input_format_pattern="Displacement {}"
    octane_sub_movable_inputs=[OctaneVertexDisplacementMixerBlendWeightMovableInput, ]
    color=consts.OctanePinColor.Displacement
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneVertexDisplacementMixer_Override(OctaneVertexDisplacementMixer):
    MAX_DISPLACEMENT_COUNT = 16
    DEFAULT_DISPLACEMENT_COUNT = 2

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneVertexDisplacementMixerDisplacementMovableInput, self.DEFAULT_DISPLACEMENT_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneVertexDisplacementMixerDisplacementMovableInput, self.MAX_DISPLACEMENT_COUNT)


_ADDED_CLASSES = [OctaneVertexDisplacementMixerBlendWeightMovableInput, OctaneVertexDisplacementMixerDisplacementMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneVertexDisplacementMixer, OctaneVertexDisplacementMixer_Override)   