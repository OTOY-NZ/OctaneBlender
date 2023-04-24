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


class OctaneVolumeToTextureGeometry(OctaneBaseSocket):
    bl_idname="OctaneVolumeToTextureGeometry"
    bl_label="VDB"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="geometry")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeToTextureTransform(OctaneBaseSocket):
    bl_idname="OctaneVolumeToTextureTransform"
    bl_label="UVW transform"
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

class OctaneVolumeToTextureProjection(OctaneBaseSocket):
    bl_idname="OctaneVolumeToTextureProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=75
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="projection")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeToTextureGrid(OctaneBaseSocket):
    bl_idname="OctaneVolumeToTextureGrid"
    bl_label="Grid ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=705)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="grid")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Scatter", "Scatter", "", 1),
        ("Absorption", "Absorption", "", 2),
        ("Emission", "Emission", "", 3),
        ("Velocity X", "Velocity X", "", 4),
        ("Velocity Y", "Velocity Y", "", 5),
        ("Velocity Z", "Velocity Z", "", 6),
    ]
    default_value: EnumProperty(default="Scatter", update=OctaneBaseSocket.update_node_tree, description="Which grid to read from the VDB", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumeToTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumeToTexture"
    bl_label="Volume to texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=256)
    octane_socket_list: StringProperty(name="Socket List", default="VDB;UVW transform;Projection;Grid ID;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneVolumeToTextureGeometry", OctaneVolumeToTextureGeometry.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureTransform", OctaneVolumeToTextureTransform.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureProjection", OctaneVolumeToTextureProjection.bl_label).init()
        self.inputs.new("OctaneVolumeToTextureGrid", OctaneVolumeToTextureGrid.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneVolumeToTextureGeometry,
    OctaneVolumeToTextureTransform,
    OctaneVolumeToTextureProjection,
    OctaneVolumeToTextureGrid,
    OctaneVolumeToTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
