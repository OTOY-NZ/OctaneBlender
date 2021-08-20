##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneTriplanarMapBlendAngle(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapBlendAngle"
    bl_label="Blend angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=345)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=5.000000, update=None, description="The angle on an edge to linearly blend two adjacent textures", min=0.000000, max=90.000000, soft_min=0.000000, soft_max=90.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapPositionType(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapPositionType"
    bl_label="Coordinate space"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=135)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("World space", "World space", "", 1),
        ("Object space", "Object space", "", 3),
    ]
    default_value: EnumProperty(default="Object space", update=None, description="Coordinate space used when blending. ", items=items)
    octane_hide_value=False
    octane_min_version=3060001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTransform(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTransform"
    bl_label="Blend cube transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type="OctaneTransformValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3060002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosX(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosX"
    bl_label="Positive X axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=339)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegX(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegX"
    bl_label="Negative X axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=342)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosY(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosY"
    bl_label="Positive Y axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=340)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegY(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegY"
    bl_label="Negative Y axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=343)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTexturePosZ(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTexturePosZ"
    bl_label="Positive Z axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=341)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3050400
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneTriplanarMapTextureNegZ(OctaneBaseSocket):
    bl_idname="OctaneTriplanarMapTextureNegZ"
    bl_label="Negative Z axis texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=344)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
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
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=109)
    octane_socket_list: StringProperty(name="Socket List", default="Blend angle;Coordinate space;Blend cube transform;Positive X axis texture;Negative X axis texture;Positive Y axis texture;Negative Y axis texture;Positive Z axis texture;Negative Z axis texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=9)

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


_classes=[
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

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####
