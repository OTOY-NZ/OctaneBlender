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
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_GEOMETRY
    octane_pin_name="geometry"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterOutputFile(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterOutputFile"
    bl_label="Output file"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_FILE
    octane_default_node_name="OctaneFileName"
    octane_pin_id=consts.PinID.P_OUTPUT_FILE
    octane_pin_name="outputFile"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterExportMaterials(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterExportMaterials"
    bl_label="Export materials"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_EXPORT_MATERIALS
    octane_pin_name="exportMaterials"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterTextureQuality(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterTextureQuality"
    bl_label="Texture quality"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_IMAGE_RESOLUTION
    octane_default_node_name="OctaneImageResolution"
    octane_pin_id=consts.PinID.P_TEXTURE_QUALITY
    octane_pin_name="textureQuality"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_INT2
    default_value: IntVectorProperty(default=(256, 256), update=OctaneBaseSocket.update_node_tree, description="When exporting materials this is the resolution. \n                                 Ignored, if export materials is disabled", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneGeometryExporterPreserveOctaneData(OctaneBaseSocket):
    bl_idname="OctaneGeometryExporterPreserveOctaneData"
    bl_label="Preserve Octane material data"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_PRESERVE_OCTANE_DATA
    octane_pin_name="preserveOctaneData"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_BOOL
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
    octane_socket_class_list=[OctaneGeometryExporterGeometry,OctaneGeometryExporterOutputFile,OctaneGeometryExporterGroupFBX,OctaneGeometryExporterExportMaterials,OctaneGeometryExporterTextureQuality,OctaneGeometryExporterPreserveOctaneData,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_GEO_EXPORTER
    octane_socket_list=["Geometry", "Output file", "Export materials", "Texture quality", "Preserve Octane material data", ]
    octane_attribute_list=[]
    octane_attribute_config={"a_execute": [consts.AttributeID.A_EXECUTE, "execute", consts.AttributeType.AT_INT], }
    octane_static_pin_count=5

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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
