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


class OctaneConverterLookatToTransformPos(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookatToTransformPos"
    bl_label = "Position"
    color = consts.OctanePinColor.Float
    octane_default_node_type = 6
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=133)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="pos")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.500000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="The position of the camera", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneConverterLookatToTransformTarget(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookatToTransformTarget"
    bl_label = "Target"
    color = consts.OctanePinColor.Float
    octane_default_node_type = 6
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=235)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="target")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The target position, i.e. the point the camera looks at", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneConverterLookatToTransformUp(OctaneBaseSocket):
    bl_idname = "OctaneConverterLookatToTransformUp"
    bl_label = "Up-vector"
    color = consts.OctanePinColor.Float
    octane_default_node_type = 6
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=248)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="up")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="The up-vector, i.e. the vector that defines where is up", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False

class OctaneConverterLookatToTransform(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneConverterLookatToTransform"
    bl_label = "Lookat to transform"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list=[OctaneConverterLookatToTransformPos,OctaneConverterLookatToTransformTarget,OctaneConverterLookatToTransformUp,]
    octane_min_version = 12000001
    octane_node_type=283
    octane_socket_list: StringProperty(name="Socket List", default="Position;Target;Up-vector;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneConverterLookatToTransformPos", OctaneConverterLookatToTransformPos.bl_label).init()
        self.inputs.new("OctaneConverterLookatToTransformTarget", OctaneConverterLookatToTransformTarget.bl_label).init()
        self.inputs.new("OctaneConverterLookatToTransformUp", OctaneConverterLookatToTransformUp.bl_label).init()
        self.outputs.new("OctaneTransformOutSocket", "Transform out").init()


_CLASSES=[
    OctaneConverterLookatToTransformPos,
    OctaneConverterLookatToTransformTarget,
    OctaneConverterLookatToTransformUp,
    OctaneConverterLookatToTransform,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
