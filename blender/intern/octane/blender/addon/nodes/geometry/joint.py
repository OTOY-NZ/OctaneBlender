# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneJointTransform(OctaneBaseSocket):
    bl_idname = "OctaneJointTransform"
    bl_label = "Joint transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneJoint(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneJoint"
    bl_label = "Joint"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneJointTransform, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_GEO_JOINT
    octane_socket_list = ["Joint transform", ]
    octane_attribute_list = ["a_pin_count", "a_index", ]
    octane_attribute_config = {"a_pin_count": [consts.AttributeID.A_PIN_COUNT, "pin_count", consts.AttributeType.AT_INT], "a_index": [consts.AttributeID.A_INDEX, "index", consts.AttributeType.AT_LONG], "a_input_action": [consts.AttributeID.A_INPUT_ACTION, "inputAction", consts.AttributeType.AT_INT2], }
    octane_static_pin_count = 1

    a_pin_count: IntProperty(name="Pin count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of child geometry pins. Ideally for connecting child joints, but you can connect other geometry nodes as well to a hierarchy, But only the joint nodes in the hierarchy will be used in deformation calculation. Joint nodes will work as placement node for other geometries connected to the joint hierarchy.\n\n Restrictions:\n     - A joint node should have only one joint parent (destination). Except a root joint node")
    a_index: IntProperty(name="Index", default=0, update=OctaneBaseNode.update_node_tree, description="Index/ID of this joint. Index value must be unique to a joint hierarchy. If more than one joint hierarchies have same index then the closest hierarchy (compared between closest common parent depths) to the mesh node is selected for deformation")

    def init(self, context):  # noqa
        self.inputs.new("OctaneJointTransform", OctaneJointTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneJointTransform,
    OctaneJoint,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
