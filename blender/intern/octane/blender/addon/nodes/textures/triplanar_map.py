##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTriplanarMapBlendAngle(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapBlendAngle"
    bl_label="Blend angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BLEND_ANGLE
    octane_pin_name="blendAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The angle on an edge to linearly blend two adjacent textures", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapPositionType(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapPositionType"
    bl_label="Coordinate space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_POSITION_TYPE
    octane_pin_name="positionType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
    ]
    default_value: EnumProperty(default="Object space", update=OctaneBaseSocket.update_node_tree, description="Coordinate space used when blending", items=items)
    octane_hide_value=False
    octane_min_version=3060001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTransform(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTransform"
    bl_label="Blend cube transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3060002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosX(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosX"
    bl_label="Positive X axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_POS_X_AXIS
    octane_pin_name="texturePosX"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegX(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegX"
    bl_label="Negative X axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_NEG_X_AXIS
    octane_pin_name="textureNegX"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosY(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosY"
    bl_label="Positive Y axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_POS_Y_AXIS
    octane_pin_name="texturePosY"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegY(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegY"
    bl_label="Negative Y axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_NEG_Y_AXIS
    octane_pin_name="textureNegY"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosZ(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosZ"
    bl_label="Positive Z axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_POS_Z_AXIS
    octane_pin_name="texturePosZ"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegZ(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegZ"
    bl_label="Negative Z axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_TEXTURE_NEG_Z_AXIS
    octane_pin_name="textureNegZ"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapGroupAxisTextures(OctaneGroupTitleSocket):
    bl_idname="OctaneTriplanarMapGroupAxisTextures"
    bl_label="[OctaneGroupTitle]Axis textures"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Positive X axis texture;Negative X axis texture;Positive Y axis texture;Negative Y axis texture;Positive Z axis texture;Negative Z axis texture;")

class OctaneTriplanarMap(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneTriplanarMap"
    bl_label="Triplanar map"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneTriplanarMapBlendAngle,OctaneTriplanarMapPositionType,OctaneTriplanarMapTransform,OctaneTriplanarMapGroupAxisTextures,OctaneTriplanarMapTexturePosX,OctaneTriplanarMapTextureNegX,OctaneTriplanarMapTexturePosY,OctaneTriplanarMapTextureNegY,OctaneTriplanarMapTexturePosZ,OctaneTriplanarMapTextureNegZ,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_TEX_TRIPLANAR
    octane_socket_list=["Blend angle", "Coordinate space", "Blend cube transform", "Positive X axis texture", "Negative X axis texture", "Positive Y axis texture", "Negative Y axis texture", "Positive Z axis texture", "Negative Z axis texture", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=9

    def init(self, context):
        self.inputs.new("OctaneTriplanarMapBlendAngle", OctaneTriplanarMapBlendAngle.bl_label).init()
        self.inputs.new("OctaneTriplanarMapPositionType", OctaneTriplanarMapPositionType.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTransform", OctaneTriplanarMapTransform.bl_label).init()
        self.inputs.new("OctaneTriplanarMapGroupAxisTextures", OctaneTriplanarMapGroupAxisTextures.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTexturePosX", OctaneTriplanarMapTexturePosX.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTextureNegX", OctaneTriplanarMapTextureNegX.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTexturePosY", OctaneTriplanarMapTexturePosY.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTextureNegY", OctaneTriplanarMapTextureNegY.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTexturePosZ", OctaneTriplanarMapTexturePosZ.bl_label).init()
        self.inputs.new("OctaneTriplanarMapTextureNegZ", OctaneTriplanarMapTextureNegZ.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneTriplanarMapBlendAngle,
    OctaneTriplanarMapPositionType,
    OctaneTriplanarMapTransform,
    OctaneTriplanarMapTexturePosX,
    OctaneTriplanarMapTextureNegX,
    OctaneTriplanarMapTexturePosY,
    OctaneTriplanarMapTextureNegY,
    OctaneTriplanarMapTexturePosZ,
    OctaneTriplanarMapTextureNegZ,
    OctaneTriplanarMapGroupAxisTextures,
    OctaneTriplanarMap,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
