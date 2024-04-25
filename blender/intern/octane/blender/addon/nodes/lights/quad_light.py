# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneQuadLightSize(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightSize"
    bl_label = "Quad size"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SIZE
    octane_pin_name = "size"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Size of the quad. The quad light is always centered around the origin in the XY plane with the +Z axis as normal", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=2)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneQuadLightMaterial1(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightMaterial1"
    bl_label = "Material"
    color = consts.OctanePinColor.Material
    octane_default_node_type = consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name = "OctaneDiffuseMaterial"
    octane_pin_id = consts.PinID.P_MATERIAL1
    octane_pin_name = "material1"
    octane_pin_type = consts.PinType.PT_MATERIAL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneQuadLightObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightObjectLayer"
    bl_label = "Object layer"
    color = consts.OctanePinColor.ObjectLayer
    octane_default_node_type = consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name = "OctaneObjectLayer"
    octane_pin_id = consts.PinID.P_OBJECT_LAYER
    octane_pin_name = "objectLayer"
    octane_pin_type = consts.PinType.PT_OBJECTLAYER
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneQuadLightTransform(OctaneBaseSocket):
    bl_idname = "OctaneQuadLightTransform"
    bl_label = "Transformation"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 8000007
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneQuadLightGroupQuad(OctaneGroupTitleSocket):
    bl_idname = "OctaneQuadLightGroupQuad"
    bl_label = "[OctaneGroupTitle]Quad"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Quad size;")


class OctaneQuadLight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneQuadLight"
    bl_label = "Quad light"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneQuadLightGroupQuad, OctaneQuadLightSize, OctaneQuadLightMaterial1, OctaneQuadLightObjectLayer, OctaneQuadLightTransform, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_LIGHT_QUAD
    octane_socket_list = ["Quad size", "Material", "Object layer", "Transformation", ]
    octane_attribute_list = ["a_user_instance_id", ]
    octane_attribute_config = {"a_user_instance_id": [consts.AttributeID.A_USER_INSTANCE_ID, "userInstanceId", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 4

    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):  # noqa
        self.inputs.new("OctaneQuadLightGroupQuad", OctaneQuadLightGroupQuad.bl_label).init()
        self.inputs.new("OctaneQuadLightSize", OctaneQuadLightSize.bl_label).init()
        self.inputs.new("OctaneQuadLightMaterial1", OctaneQuadLightMaterial1.bl_label).init()
        self.inputs.new("OctaneQuadLightObjectLayer", OctaneQuadLightObjectLayer.bl_label).init()
        self.inputs.new("OctaneQuadLightTransform", OctaneQuadLightTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneQuadLightSize,
    OctaneQuadLightMaterial1,
    OctaneQuadLightObjectLayer,
    OctaneQuadLightTransform,
    OctaneQuadLightGroupQuad,
    OctaneQuadLight,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
