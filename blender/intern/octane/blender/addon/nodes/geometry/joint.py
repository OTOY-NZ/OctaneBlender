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


class OctaneJointTransform(OctaneBaseSocket):
    bl_idname="OctaneJointTransform"
    bl_label="Joint transform"
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

class OctaneJoint(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneJoint"
    bl_label="Joint"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=102)
    octane_socket_list: StringProperty(name="Socket List", default="Joint transform;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_pin_count;a_index;")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="pin_count;index;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;14;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    a_pin_count: IntProperty(name="Pin count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of child geometry pins. Ideally for connecting child joints, but you can connect other geometry nodes as well to a hierarchy, But only the joint nodes in the hierarchy will be used in deformation calculation. Joint nodes will work as placement node for other geometries connected to the joint hierarchy.\n\n Restrictions:\n     - A joint node should have only one joint parent(destination). Except a root joint node")
    a_index: IntProperty(name="Index", default=0, update=OctaneBaseNode.update_node_tree, description="Index/ID of this joint. Index value must be unique to a joint hierarchy. If more than one joint hierarchies have same index then the closest hierarchy(compared between closest common parent depths) to the mesh node is selected for deformation")

    def init(self, context):
        self.inputs.new("OctaneJointTransform", OctaneJointTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
    OctaneJointTransform,
    OctaneJoint,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
