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


class OctaneVolumeSDFMaterial1(OctaneBaseSocket):
    bl_idname="OctaneVolumeSDFMaterial1"
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

class OctaneVolumeSDFObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneVolumeSDFObjectLayer"
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

class OctaneVolumeSDF(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumeSDF"
    bl_label="Volume SDF"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=134)
    octane_socket_list: StringProperty(name="Socket List", default="Material;Object layer;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_user_instance_id;a_geoimp_scale_unit;a_volume_isovalue;a_volume_absorption_id;a_volume_absorption_scale;a_volume_scatter_id;a_volume_scatter_scale;a_volume_emission_id;a_volume_emission_scale;a_volume_velocity_id;a_volume_velocity_id_x;a_volume_velocity_id_y;a_volume_velocity_id_z;a_volume_velocity_scale;a_volume_motion_blur_enabled;a_volume_leaves;a_volume_nodes;a_volume_absorption_offset;a_volume_absorption_max;a_volume_absorption_default;a_volume_scatter_offset;a_volume_scatter_max;a_volume_scatter_default;a_volume_emission_offset;a_volume_emission_max;a_volume_emission_default;a_volume_velocity_offset_x;a_volume_velocity_offset_y;a_volume_velocity_offset_z;a_volume_velocity_default;a_volume_regular_grid;a_volume_resolution;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;2;2;6;10;6;10;6;10;6;10;10;10;10;6;1;6;2;2;6;8;2;6;8;2;6;8;2;2;2;8;6;4;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=2)

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the name of the file from which to load the volume data from. Currently, only OpenVDB files are supported. To load a new file, just change this attribute and evaluate the node", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set to TRUE if the file needs a reload. After the node was evaluated, the attribute will be false again")
    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")
    a_geoimp_scale_unit: IntProperty(name="Geoimp scale unit", default=4, update=OctaneBaseNode.update_node_tree, description="Defines the length unit used to interpret the worldbounds of the volume. (see Octane::GeometryImportScale)")
    a_volume_isovalue: FloatProperty(name="Volume isovalue", default=0.040000, update=OctaneBaseNode.update_node_tree, description="Isovalue used for when rendering openvdb level sets")
    a_volume_absorption_id: StringProperty(name="Volume absorption id", default="density", update=OctaneBaseNode.update_node_tree, description="Name of the grid in a VDB to load for absorption. If an empty string is provided then no grid will be loaded. If the grid cannot be found in the VDB, then no grid will be loaded")
    a_volume_absorption_scale: FloatProperty(name="Volume absorption scale", default=1.000000, update=OctaneBaseNode.update_node_tree, description="This scalar value scales the grid value used for absorption")
    a_volume_scatter_id: StringProperty(name="Volume scatter id", default="density", update=OctaneBaseNode.update_node_tree, description="Name of the grid in a VDB to load for scattering. If an empty string is provided then no grid will be loaded. If the grid cannot be found in the VDB, then no grid will be loaded")
    a_volume_scatter_scale: FloatProperty(name="Volume scatter scale", default=1.000000, update=OctaneBaseNode.update_node_tree, description="This scalar value scales the grid value used for scattering")
    a_volume_emission_id: StringProperty(name="Volume emission id", default="temperature", update=OctaneBaseNode.update_node_tree, description="Name of the grid in a VDB to load for providing temperature information. If an empty string is provided then no grid will be loaded. If the grid cannot be found in the VDB, then no grid will be loaded")
    a_volume_emission_scale: FloatProperty(name="Volume emission scale", default=1.000000, update=OctaneBaseNode.update_node_tree, description="This scalar value scales the grid value used for temperature. Use this when temperature information in a grid is too low")
    a_volume_velocity_id: StringProperty(name="Volume velocity id", default="v", update=OctaneBaseNode.update_node_tree, description="Name of a vec3s type grid in the VDB to load for motion blur. If specified then this will take precedence over A_VOLUME_VELOCITY_ID_*. If specified when exporting from a regular grid to a VDB, then the exported VDB will contain a vec3s grid for velocities. If not, then the exporter will check whether the A_VOLUME_VELOCITY_ID_* attributes are set, and if so, it will export individual component grids")
    a_volume_velocity_id_x: StringProperty(name="Volume velocity id x", default="", update=OctaneBaseNode.update_node_tree, description="Name of a float grid in the VDB to use for the x-component of motion blur vectors. If A_VOLUME_VELOCITY_ID_* are all set to non-empty strings, when exporting from a regular grid, and A_VOLUME_VELOCITY_ID is set to an empty string, then the exporter will create independent velocity component grids in the VDB")
    a_volume_velocity_id_y: StringProperty(name="Volume velocity id y", default="", update=OctaneBaseNode.update_node_tree, description="Name of a float grid in the VDB to use for the y-component of motion blur vectors. If A_VOLUME_VELOCITY_ID_* are all set to non-empty strings, when exporting from a regular grid, and A_VOLUME_VELOCITY_ID is set to an empty string, then the exporter will create independent velocity component grids in the VDB")
    a_volume_velocity_id_z: StringProperty(name="Volume velocity id z", default="", update=OctaneBaseNode.update_node_tree, description="Name of a float grid in the VDB to use for the z-component of motion blur vectors. If A_VOLUME_VELOCITY_ID_* are all set to non-empty strings, when exporting from a regular grid, and A_VOLUME_VELOCITY_ID is set to an empty string, then the exporter will create independent velocity component grids in the VDB")
    a_volume_velocity_scale: FloatProperty(name="Volume velocity scale", default=1.000000, update=OctaneBaseNode.update_node_tree, description="This scalar value linearly scales velocity vectors in the velocity grid")
    a_volume_motion_blur_enabled: BoolProperty(name="Volume motion blur enabled", default=True, update=OctaneBaseNode.update_node_tree, description="If TRUE, then any motion blur grids will be ignored")
    a_volume_leaves: FloatProperty(name="Volume leaves", default=0.000000, update=OctaneBaseNode.update_node_tree, description="Hierarchical tree leaves for the volume")
    a_volume_nodes: IntProperty(name="Volume nodes", default=0, update=OctaneBaseNode.update_node_tree, description="Hierarchical tree nodes for the volume")
    a_volume_absorption_offset: IntProperty(name="Volume absorption offset", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies which float inside a voxel is applied to absorption. If negative, it will be assumed that the channel is disabled")
    a_volume_absorption_max: FloatProperty(name="Volume absorption max", default=0.000000, update=OctaneBaseNode.update_node_tree, description="The maximum float value in the absorption channel's grid. This value is calculated automatically")
    a_volume_absorption_default: FloatVectorProperty(name="Volume absorption default", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The default background absorption value of the volume. Usually 0")
    a_volume_scatter_offset: IntProperty(name="Volume scatter offset", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies which float inside a voxel is applied to  scattering. If negative, it will be assumed that the channel is disabled")
    a_volume_scatter_max: FloatProperty(name="Volume scatter max", default=0.000000, update=OctaneBaseNode.update_node_tree, description="The maximum float value in the scatter channel's grid. This value is calculated automatically")
    a_volume_scatter_default: FloatVectorProperty(name="Volume scatter default", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The default background absorption value of the volume. Usually 0")
    a_volume_emission_offset: IntProperty(name="Volume emission offset", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies which float inside a voxel is applied to emission. If negative, it will be assumed that the channel is disabled")
    a_volume_emission_max: FloatProperty(name="Volume emission max", default=0.000000, update=OctaneBaseNode.update_node_tree, description="The maximum float value in the emission channel's grid. This value is calculated automatically")
    a_volume_emission_default: FloatVectorProperty(name="Volume emission default", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The default background emission value for the volume. Usually 0")
    a_volume_velocity_offset_x: IntProperty(name="Volume velocity offset x", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies the channel index (offset inside a singlevoxel) to be used for the velocity vector x-component")
    a_volume_velocity_offset_y: IntProperty(name="Volume velocity offset y", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies the channel index (offset inside a singlevoxel) to be used for the velocity vector y-component")
    a_volume_velocity_offset_z: IntProperty(name="Volume velocity offset z", default=-1, update=OctaneBaseNode.update_node_tree, description="This zero-based offset specifies the channel index (offset inside a singlevoxel) to be used for the velocity vector z-component")
    a_volume_velocity_default: FloatVectorProperty(name="Volume velocity default", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The default background velocity value for this volume. Usually (0,0,0)")
    a_volume_regular_grid: FloatProperty(name="Volume regular grid", default=0.000000, update=OctaneBaseNode.update_node_tree, description="Voxels are stored in order of x-axis, followed by rows up the y-axis, then finally, it repeats for each z-slice. If you have more than one float per voxel, then store each voxel as a set of floats contiguously.  After that you set A_VOLUME_ABSORPTION_OFFSET, A_VOLUME_SCATTER_OFFSET, A_VOLUME_EMISSION_OFFSET to an integer index into your voxels. For example, if you have 2 floats in each voxel, and the second float is what you want for scatter, then you set A_VOLUME_SCATTER_OFFSET to 1. You must set at least one of these. Finally, set A_VOLUME_RESOLUTION to the number of voxels in each dimension. The volume at this point is set in space with each voxel measuring 1m x 1m x 1m. To change the scale, you should set A_TRANSFORM also")
    a_volume_resolution: IntVectorProperty(name="Volume resolution", default=(0, 0, 0), size=3, update=OctaneBaseNode.update_node_tree, description="Voxel resolution of the volume")

    def init(self, context):
        self.inputs.new("OctaneVolumeSDFMaterial1", OctaneVolumeSDFMaterial1.bl_label).init()
        self.inputs.new("OctaneVolumeSDFObjectLayer", OctaneVolumeSDFObjectLayer.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
    OctaneVolumeSDFMaterial1,
    OctaneVolumeSDFObjectLayer,
    OctaneVolumeSDF,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
