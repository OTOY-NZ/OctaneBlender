##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneGeometryExporterGeometry(OctaneBaseSocket):
    bl_idname = "OctaneGeometryExporterGeometry"
    bl_label = "Geometry"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneGeometryExporterOutputFile(OctaneBaseSocket):
    bl_idname = "OctaneGeometryExporterOutputFile"
    bl_label = "Output file"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=529)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=23)
    octane_socket_type: IntProperty(name="Socket Type", default=10)
    default_value: StringProperty(default="", description="")

class OctaneGeometryExporterExportMaterials(OctaneBaseSocket):
    bl_idname = "OctaneGeometryExporterExportMaterials"
    bl_label = "Export materials"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=530)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="")

class OctaneGeometryExporterTextureQuality(OctaneBaseSocket):
    bl_idname = "OctaneGeometryExporterTextureQuality"
    bl_label = "Texture quality"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=531)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=4)
    default_value: IntVectorProperty(default=(256, 256), description="When exporting materials this is the resolution.                                   Ignored, if export materials is disabled", min=-2147483648, max=2147483647, soft_min=-2147483648, soft_max=2147483647, step=1, subtype="NONE", size=2)

class OctaneGeometryExporterPreserveOctaneData(OctaneBaseSocket):
    bl_idname = "OctaneGeometryExporterPreserveOctaneData"
    bl_label = "Preserve Octane material data"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=532)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Ignored, if export materials is disabled")

class OctaneGeometryExporter(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneGeometryExporter"
    bl_label = "Geometry exporter"
    octane_node_type: IntProperty(name="Octane Node Type", default=156)
    octane_socket_list: StringProperty(name="Socket List", default="Geometry;Output file;Export materials;Texture quality;Preserve Octane material data;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneGeometryExporterGeometry", OctaneGeometryExporterGeometry.bl_label)
        self.inputs.new("OctaneGeometryExporterOutputFile", OctaneGeometryExporterOutputFile.bl_label)
        self.inputs.new("OctaneGeometryExporterExportMaterials", OctaneGeometryExporterExportMaterials.bl_label)
        self.inputs.new("OctaneGeometryExporterTextureQuality", OctaneGeometryExporterTextureQuality.bl_label)
        self.inputs.new("OctaneGeometryExporterPreserveOctaneData", OctaneGeometryExporterPreserveOctaneData.bl_label)


def register():
    register_class(OctaneGeometryExporterGeometry)
    register_class(OctaneGeometryExporterOutputFile)
    register_class(OctaneGeometryExporterExportMaterials)
    register_class(OctaneGeometryExporterTextureQuality)
    register_class(OctaneGeometryExporterPreserveOctaneData)
    register_class(OctaneGeometryExporter)

def unregister():
    unregister_class(OctaneGeometryExporter)
    unregister_class(OctaneGeometryExporterPreserveOctaneData)
    unregister_class(OctaneGeometryExporterTextureQuality)
    unregister_class(OctaneGeometryExporterExportMaterials)
    unregister_class(OctaneGeometryExporterOutputFile)
    unregister_class(OctaneGeometryExporterGeometry)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
