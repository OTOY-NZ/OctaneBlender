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


class OctaneColorVertexAttributeName(OctaneBaseSocket):
    bl_idname="OctaneColorVertexAttributeName"
    bl_label="Name"
    color=consts.OctanePinColor.String
    octane_default_node_type="OctaneStringValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=465)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_STRING)
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="Name of the vertex attribute")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneColorVertexAttribute(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneColorVertexAttribute"
    bl_label="Color vertex attribute"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=135)
    octane_socket_list: StringProperty(name="Socket List", default="Name;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    def init(self, context):
        self.inputs.new("OctaneColorVertexAttributeName", OctaneColorVertexAttributeName.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneColorVertexAttributeName,
    OctaneColorVertexAttribute,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
