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


class OctaneImageResolution(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneImageResolution"
    bl_label="Image resolution"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_IMAGE_RESOLUTION
    octane_socket_list=[]
    octane_attribute_list=["a_value", "a_preset", "a_aspect_ratio", ]
    octane_attribute_config={"a_value": [consts.AttributeID.A_VALUE, "value", consts.AttributeType.AT_INT3], "a_preset": [consts.AttributeID.A_PRESET, "preset", consts.AttributeType.AT_INT], "a_aspect_ratio": [consts.AttributeID.A_ASPECT_RATIO, "aspectRatio", consts.AttributeType.AT_FLOAT], }
    octane_static_pin_count=0

    a_value: IntVectorProperty(name="Value", default=(1024, 512, 0), size=3, update=OctaneBaseNode.update_node_tree, description="The resolution stored in the node. X and Y need to be > 0, Z is ignored")
    a_preset: IntProperty(name="Preset", default=403, update=OctaneBaseNode.update_node_tree, description="The preset chosen by the user - used only by the standalone UI, since many resolutions have multiple entries in the resolution menu")
    a_aspect_ratio: FloatProperty(name="Aspect ratio", default=0.000000, update=OctaneBaseNode.update_node_tree, description="The aspect ratio width/height or 0 if the aspect ratio is not locked. Needs to be >= 0")

    def init(self, context):
        self.outputs.new("OctaneIntOutSocket", "Int out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneImageResolution,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
