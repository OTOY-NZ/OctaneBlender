##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneQuadLightSize(OctaneBaseSocket):
    bl_idname="OctaneQuadLightSize"
    bl_label="Quad size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=216)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT2)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=None, description="Size of the quad. The quad light is always centered around the origin in the XY plane with the +Z axis as normal", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneQuadLightMaterial1(OctaneBaseSocket):
    bl_idname="OctaneQuadLightMaterial1"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type="OctaneDiffuseMaterial"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=100)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneQuadLightObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneQuadLightObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type="OctaneObjectLayer"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneQuadLightTransform(OctaneBaseSocket):
    bl_idname="OctaneQuadLightTransform"
    bl_label="Transformation"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=8000007
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneQuadLightGroupQuad(OctaneGroupTitleSocket):
    bl_idname="OctaneQuadLightGroupQuad"
    bl_label="[OctaneGroupTitle]Quad"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Quad size;")

class OctaneQuadLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneQuadLight"
    bl_label="Quad light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=148)
    octane_socket_list: StringProperty(name="Socket List", default="Quad size;Material;Object layer;Transformation;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_user_instance_id;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=None, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):
        self.inputs.new("OctaneQuadLightGroupQuad", OctaneQuadLightGroupQuad.bl_label).init()
        self.inputs.new("OctaneQuadLightSize", OctaneQuadLightSize.bl_label).init()
        self.inputs.new("OctaneQuadLightMaterial1", OctaneQuadLightMaterial1.bl_label).init()
        self.inputs.new("OctaneQuadLightObjectLayer", OctaneQuadLightObjectLayer.bl_label).init()
        self.inputs.new("OctaneQuadLightTransform", OctaneQuadLightTransform.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
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
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
