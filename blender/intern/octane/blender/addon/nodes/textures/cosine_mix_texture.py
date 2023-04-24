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


class OctaneCosineMixTextureAmount(OctaneBaseSocket):
    bl_idname="OctaneCosineMixTextureAmount"
    bl_label="Mix amount"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=31
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=6)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="amount")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Mix amount between the first and second texture", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCosineMixTextureTexture1(OctaneBaseSocket):
    bl_idname="OctaneCosineMixTextureTexture1"
    bl_label="First texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=238)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture1")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCosineMixTextureTexture2(OctaneBaseSocket):
    bl_idname="OctaneCosineMixTextureTexture2"
    bl_label="Second texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=239)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="texture2")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCosineMixTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCosineMixTexture"
    bl_label="Cosine mix texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=40)
    octane_socket_list: StringProperty(name="Socket List", default="Mix amount;First texture;Second texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneCosineMixTextureAmount", OctaneCosineMixTextureAmount.bl_label).init()
        self.inputs.new("OctaneCosineMixTextureTexture1", OctaneCosineMixTextureTexture1.bl_label).init()
        self.inputs.new("OctaneCosineMixTextureTexture2", OctaneCosineMixTextureTexture2.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneCosineMixTextureAmount,
    OctaneCosineMixTextureTexture1,
    OctaneCosineMixTextureTexture2,
    OctaneCosineMixTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
