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


class OctanePlaneUvTransform(OctaneBaseSocket):
    bl_idname="OctanePlaneUvTransform"
    bl_label="UV transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=67
    octane_default_node_name="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=362)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="uvTransform")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3070002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlaneGroundColor(OctaneBaseSocket):
    bl_idname="OctanePlaneGroundColor"
    bl_label="Plane material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=17
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=331)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="groundColor")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlaneObjectLayer(OctaneBaseSocket):
    bl_idname="OctanePlaneObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=65
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="objectLayer")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePlane(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctanePlane"
    bl_label="Plane"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=110)
    octane_socket_list: StringProperty(name="Socket List", default="UV transform;Plane material;Object layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_user_instance_id;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):
        self.inputs.new("OctanePlaneUvTransform", OctanePlaneUvTransform.bl_label).init()
        self.inputs.new("OctanePlaneGroundColor", OctanePlaneGroundColor.bl_label).init()
        self.inputs.new("OctanePlaneObjectLayer", OctanePlaneObjectLayer.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
    OctanePlaneUvTransform,
    OctanePlaneGroundColor,
    OctanePlaneObjectLayer,
    OctanePlane,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
