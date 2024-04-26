##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneSphereLightRadius(OctaneBaseSocket):
    bl_idname="OctaneSphereLightRadius"
    bl_label="Sphere radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_RADIUS
    octane_pin_name="radius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Radius of the sphere. The Sphere light is always centered around the origin. If set to 0 this will be a point light", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSphereLightMaterial1(OctaneBaseSocket):
    bl_idname="OctaneSphereLightMaterial1"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL1
    octane_pin_name="material1"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSphereLightObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneSphereLightObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id=consts.PinID.P_OBJECT_LAYER
    octane_pin_name="objectLayer"
    octane_pin_type=consts.PinType.PT_OBJECTLAYER
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSphereLightTransform(OctaneBaseSocket):
    bl_idname="OctaneSphereLightTransform"
    bl_label="Transformation"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=8000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneSphereLightGroupSphere(OctaneGroupTitleSocket):
    bl_idname="OctaneSphereLightGroupSphere"
    bl_label="[OctaneGroupTitle]Sphere"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sphere radius;")

class OctaneSphereLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneSphereLight"
    bl_label="Sphere light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneSphereLightGroupSphere,OctaneSphereLightRadius,OctaneSphereLightMaterial1,OctaneSphereLightObjectLayer,OctaneSphereLightTransform,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_LIGHT_SPHERE
    octane_socket_list=["Sphere radius", "Material", "Object layer", "Transformation", ]
    octane_attribute_list=["a_user_instance_id", ]
    octane_attribute_config={"a_user_instance_id": [consts.AttributeID.A_USER_INSTANCE_ID, "userInstanceId", consts.AttributeType.AT_INT], }
    octane_static_pin_count=4

    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):
        self.inputs.new("OctaneSphereLightGroupSphere", OctaneSphereLightGroupSphere.bl_label).init()
        self.inputs.new("OctaneSphereLightRadius", OctaneSphereLightRadius.bl_label).init()
        self.inputs.new("OctaneSphereLightMaterial1", OctaneSphereLightMaterial1.bl_label).init()
        self.inputs.new("OctaneSphereLightObjectLayer", OctaneSphereLightObjectLayer.bl_label).init()
        self.inputs.new("OctaneSphereLightTransform", OctaneSphereLightTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneSphereLightRadius,
    OctaneSphereLightMaterial1,
    OctaneSphereLightObjectLayer,
    OctaneSphereLightTransform,
    OctaneSphereLightGroupSphere,
    OctaneSphereLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
