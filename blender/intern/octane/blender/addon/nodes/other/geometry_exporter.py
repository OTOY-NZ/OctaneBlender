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


class OctaneGeometryExporterGeometry(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterGeometry"
    bl_label="Geometry"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterOutputFile(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterOutputFile"
    bl_label="Output file"
    color=consts.OctanePinColor.String
    octane_default_node_type="OctaneFileName"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=529)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_STRING)
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterExportMaterials(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterExportMaterials"
    bl_label="Export materials"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=530)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterTextureQuality(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterTextureQuality"
    bl_label="Texture quality"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneImageResolution"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=531)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT2)
    default_value: IntVectorProperty(default=(256, 256), update=OctaneBaseSocket.update_node_tree, description="When exporting materials this is the resolution. \n                                 Ignored, if export materials is disabled", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterPreserveOctaneData(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterPreserveOctaneData"
    bl_label="Preserve Octane material data"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=532)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Ignored, if export materials is disabled")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterGroupFBX(OctaneGroupTitleSocket):
    bl_idname="OctaneGeometryExporterGroupFBX"
    bl_label="[OctaneGroupTitle]FBX"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Export materials;Texture quality;Preserve Octane material data;")

class OctaneGeometryExporter(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneGeometryExporter"
    bl_label="Geometry exporter"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=156)
    octane_socket_list: StringProperty(name="Socket List", default="Geometry;Output file;Export materials;Texture quality;Preserve Octane material data;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneGeometryExporterGeometry", OctaneGeometryExporterGeometry.bl_label).init()
        self.inputs.new("OctaneGeometryExporterOutputFile", OctaneGeometryExporterOutputFile.bl_label).init()
        self.inputs.new("OctaneGeometryExporterGroupFBX", OctaneGeometryExporterGroupFBX.bl_label).init()
        self.inputs.new("OctaneGeometryExporterExportMaterials", OctaneGeometryExporterExportMaterials.bl_label).init()
        self.inputs.new("OctaneGeometryExporterTextureQuality", OctaneGeometryExporterTextureQuality.bl_label).init()
        self.inputs.new("OctaneGeometryExporterPreserveOctaneData", OctaneGeometryExporterPreserveOctaneData.bl_label).init()


_CLASSES=[
    OctaneGeometryExporterGeometry,
    OctaneGeometryExporterOutputFile,
    OctaneGeometryExporterExportMaterials,
    OctaneGeometryExporterTextureQuality,
    OctaneGeometryExporterPreserveOctaneData,
    OctaneGeometryExporterGroupFBX,
    OctaneGeometryExporter,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
