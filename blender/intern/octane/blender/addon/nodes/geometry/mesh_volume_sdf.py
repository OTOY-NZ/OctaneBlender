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


class OctaneMeshVolumeSDFMaterial1(OctaneBaseSocket):
    bl_idname="OctaneMeshVolumeSDFMaterial1"
    bl_label="Material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL1
    octane_pin_name="material1"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMeshVolumeSDFObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneMeshVolumeSDFObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id=consts.PinID.P_OBJECT_LAYER
    octane_pin_name="objectLayer"
    octane_pin_type=consts.PinType.PT_OBJECTLAYER
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMeshVolumeSDF(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMeshVolumeSDF"
    bl_label="Mesh volume SDF"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneMeshVolumeSDFMaterial1,OctaneMeshVolumeSDFObjectLayer,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_GEO_MESH_VOLUME_SDF
    octane_socket_list=["Material", "Object layer", ]
    octane_attribute_list=["a_filename", "a_reload", "a_user_instance_id", "a_volume_channel_config", "a_geoimp_scale_unit", "a_volume_isovalue", "a_volume_absorption_id", "a_volume_absorption_scale", "a_volume_scatter_id", "a_volume_scatter_scale", "a_volume_emission_id", "a_volume_emission_scale", "a_volume_velocity_id", "a_volume_velocity_id_x", "a_volume_velocity_id_y", "a_volume_velocity_id_z", "a_volume_velocity_scale", "a_volume_channel_ids", "a_volume_motion_blur_enabled", "a_voxel_size", "a_border_width", "a_winding_order", "a_constant_topology", "a_vertices_per_poly", "a_vertices", "a_poly_vertex_indices", "a_volume_leaves", "a_volume_nodes", "a_volume_absorption_offset", "a_volume_absorption_max", "a_volume_absorption_default", "a_volume_scatter_offset", "a_volume_scatter_max", "a_volume_scatter_default", "a_volume_emission_offset", "a_volume_emission_max", "a_volume_emission_default", "a_volume_velocity_offset_x", "a_volume_velocity_offset_y", "a_volume_velocity_offset_z", "a_volume_velocity_default", "a_volume_channel_offsets", "a_volume_channel_max_values", "a_volume_channel_defaults", "a_volume_channel_is_float3", "a_volume_regular_grid", "a_volume_resolution", "a_volume_voxel_float_size", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_user_instance_id": [consts.AttributeID.A_USER_INSTANCE_ID, "userInstanceId", consts.AttributeType.AT_INT], "a_volume_channel_config": [consts.AttributeID.A_VOLUME_CHANNEL_CONFIG, "volumeChannelConfig", consts.AttributeType.AT_LONG], "a_geoimp_scale_unit": [consts.AttributeID.A_GEOIMP_SCALE_UNIT, "scaleUnitType", consts.AttributeType.AT_INT], "a_volume_isovalue": [consts.AttributeID.A_VOLUME_ISOVALUE, "volumeIsoValue", consts.AttributeType.AT_FLOAT], "a_volume_absorption_id": [consts.AttributeID.A_VOLUME_ABSORPTION_ID, "volumeAbsorptionId", consts.AttributeType.AT_STRING], "a_volume_absorption_scale": [consts.AttributeID.A_VOLUME_ABSORPTION_SCALE, "volumeAbsorptionScale", consts.AttributeType.AT_FLOAT], "a_volume_scatter_id": [consts.AttributeID.A_VOLUME_SCATTER_ID, "volumeScatterId", consts.AttributeType.AT_STRING], "a_volume_scatter_scale": [consts.AttributeID.A_VOLUME_SCATTER_SCALE, "volumeScatteringScale", consts.AttributeType.AT_FLOAT], "a_volume_emission_id": [consts.AttributeID.A_VOLUME_EMISSION_ID, "volumeEmissionId", consts.AttributeType.AT_STRING], "a_volume_emission_scale": [consts.AttributeID.A_VOLUME_EMISSION_SCALE, "volumeEmissionScale", consts.AttributeType.AT_FLOAT], "a_volume_velocity_id": [consts.AttributeID.A_VOLUME_VELOCITY_ID, "volumeVelocityId", consts.AttributeType.AT_STRING], "a_volume_velocity_id_x": [consts.AttributeID.A_VOLUME_VELOCITY_ID_X, "volumeVelocityIdX", consts.AttributeType.AT_STRING], "a_volume_velocity_id_y": [consts.AttributeID.A_VOLUME_VELOCITY_ID_Y, "volumeVelocityIdY", consts.AttributeType.AT_STRING], "a_volume_velocity_id_z": [consts.AttributeID.A_VOLUME_VELOCITY_ID_Z, "volumeVelocityIdZ", consts.AttributeType.AT_STRING], "a_volume_velocity_scale": [consts.AttributeID.A_VOLUME_VELOCITY_SCALE, "volumeVelocityScale", consts.AttributeType.AT_FLOAT], "a_volume_channel_ids": [consts.AttributeID.A_VOLUME_CHANNEL_IDS, "volumeChannelIds", consts.AttributeType.AT_STRING], "a_volume_motion_blur_enabled": [consts.AttributeID.A_VOLUME_MOTION_BLUR_ENABLED, "volumeMotionBlurEnabled", consts.AttributeType.AT_BOOL], "a_voxel_size": [consts.AttributeID.A_VOXEL_SIZE, "voxelSize", consts.AttributeType.AT_FLOAT], "a_border_width": [consts.AttributeID.A_BORDER_WIDTH, "borderWidth", consts.AttributeType.AT_FLOAT2], "a_winding_order": [consts.AttributeID.A_WINDING_ORDER, "windingOrder", consts.AttributeType.AT_INT], "a_constant_topology": [consts.AttributeID.A_CONSTANT_TOPOLOGY, "constantTopology", consts.AttributeType.AT_BOOL], "a_vertices_per_poly": [consts.AttributeID.A_VERTICES_PER_POLY, "verticesPerPoly", consts.AttributeType.AT_INT], "a_vertices": [consts.AttributeID.A_VERTICES, "vertices", consts.AttributeType.AT_FLOAT3], "a_poly_vertex_indices": [consts.AttributeID.A_POLY_VERTEX_INDICES, "polyVertexIndices", consts.AttributeType.AT_INT], "a_volume_leaves": [consts.AttributeID.A_VOLUME_LEAVES, "volumeLeaves", consts.AttributeType.AT_FLOAT], "a_volume_nodes": [consts.AttributeID.A_VOLUME_NODES, "volumeNodes", consts.AttributeType.AT_INT], "a_volume_absorption_offset": [consts.AttributeID.A_VOLUME_ABSORPTION_OFFSET, "volumeAbsorptionOffset", consts.AttributeType.AT_INT], "a_volume_absorption_max": [consts.AttributeID.A_VOLUME_ABSORPTION_MAX, "volumeAbsorptionMax", consts.AttributeType.AT_FLOAT], "a_volume_absorption_default": [consts.AttributeID.A_VOLUME_ABSORPTION_DEFAULT, "volumeAbsorptionDefault", consts.AttributeType.AT_FLOAT3], "a_volume_scatter_offset": [consts.AttributeID.A_VOLUME_SCATTER_OFFSET, "volumeScatterOffset", consts.AttributeType.AT_INT], "a_volume_scatter_max": [consts.AttributeID.A_VOLUME_SCATTER_MAX, "volumeScatterMax", consts.AttributeType.AT_FLOAT], "a_volume_scatter_default": [consts.AttributeID.A_VOLUME_SCATTER_DEFAULT, "volumeScatterDefault", consts.AttributeType.AT_FLOAT3], "a_volume_emission_offset": [consts.AttributeID.A_VOLUME_EMISSION_OFFSET, "volumeEmissionOffset", consts.AttributeType.AT_INT], "a_volume_emission_max": [consts.AttributeID.A_VOLUME_EMISSION_MAX, "volumeEmissionMax", consts.AttributeType.AT_FLOAT], "a_volume_emission_default": [consts.AttributeID.A_VOLUME_EMISSION_DEFAULT, "volumeEmissionDefault", consts.AttributeType.AT_FLOAT3], "a_volume_velocity_offset_x": [consts.AttributeID.A_VOLUME_VELOCITY_OFFSET_X, "volumeVelocityOffsetX", consts.AttributeType.AT_INT], "a_volume_velocity_offset_y": [consts.AttributeID.A_VOLUME_VELOCITY_OFFSET_Y, "volumeVelocityOffsetY", consts.AttributeType.AT_INT], "a_volume_velocity_offset_z": [consts.AttributeID.A_VOLUME_VELOCITY_OFFSET_Z, "volumeVelocityOffsetZ", consts.AttributeType.AT_INT], "a_volume_velocity_default": [consts.AttributeID.A_VOLUME_VELOCITY_DEFAULT, "volumeVelocityDefault", consts.AttributeType.AT_FLOAT3], "a_volume_channel_offsets": [consts.AttributeID.A_VOLUME_CHANNEL_OFFSETS, "volumeChannelOffsets", consts.AttributeType.AT_INT], "a_volume_channel_max_values": [consts.AttributeID.A_VOLUME_CHANNEL_MAX_VALUES, "volumeChannelMaxValues", consts.AttributeType.AT_FLOAT3], "a_volume_channel_defaults": [consts.AttributeID.A_VOLUME_CHANNEL_DEFAULTS, "volumeChannelDefaults", consts.AttributeType.AT_FLOAT3], "a_volume_channel_is_float3": [consts.AttributeID.A_VOLUME_CHANNEL_IS_FLOAT3, "volumeChannelIsFloat3", consts.AttributeType.AT_BOOL], "a_volume_regular_grid": [consts.AttributeID.A_VOLUME_REGULAR_GRID, "volumeRegularGrid", consts.AttributeType.AT_FLOAT], "a_volume_resolution": [consts.AttributeID.A_VOLUME_RESOLUTION, "volumeResolution", consts.AttributeType.AT_INT3], "a_volume_voxel_float_size": [consts.AttributeID.A_VOLUME_VOXEL_FLOAT_SIZE, "volumeVoxelFloatSize", consts.AttributeType.AT_INT], "a_transform": [consts.AttributeID.A_TRANSFORM, "transform", consts.AttributeType.AT_MATRIX], }
    octane_static_pin_count=2

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="File name, if any, of the file containing the mesh data", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set to TRUE if the file needs a reload. After the node was evaluated, the attribute will be false again")
    a_user_instance_id: IntProperty(name="User instance id", default=-1, update=OctaneBaseNode.update_node_tree, description="The user ID of this geometry node. A valid ID should be a non-negative number. It's a non-unique ID attribute, multiple geometry nodes can have same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")
    a_volume_channel_config: IntProperty(name="Volume channel config", default=0, update=OctaneBaseNode.update_node_tree, description="The instance channel config for this node. This is set automatically")
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
    a_volume_channel_ids: StringProperty(name="Volume channel ids", default="", update=OctaneBaseNode.update_node_tree, description="The names of the grids to load. The grid names specified via usage specific attributes like A_VOLUME_SCATTER_ID will be added automatically if necessary. Standard Volume mediums support per-instance channel assignments and can select any of the grids loaded for the volume")
    a_volume_motion_blur_enabled: BoolProperty(name="Volume motion blur enabled", default=True, update=OctaneBaseNode.update_node_tree, description="If TRUE, then any motion blur grids will be ignored")
    a_voxel_size: FloatProperty(name="Voxel size", default=0.100000, update=OctaneBaseNode.update_node_tree, description="Size of one voxel")
    a_border_width: FloatVectorProperty(name="Border width", default=(3.000000, 3.000000), size=2, update=OctaneBaseNode.update_node_tree, description="Amount of voxels that will be generated on either side of the surface (outside, inside)")
    a_winding_order: IntProperty(name="Winding order", default=1, update=OctaneBaseNode.update_node_tree, description="The order of the vertices in polygons, as seen from the side where the normal is pointing")
    a_constant_topology: BoolProperty(name="Constant topology", default=False, update=OctaneBaseNode.update_node_tree, description="Can be set to TRUE if the geometry has a constant topology. This means the connectivity between faces, edges and vertices stays the same during the animation of this geometry. If TRUE Octane may try to calculate motion blur from the motion of vertices between frames. This applies to polygons, hair and sphere primitives")
    a_vertices_per_poly: IntProperty(name="Vertices per poly", default=0, update=OctaneBaseNode.update_node_tree, description="An array of the number of vertices for each polygon in the polygon sequence. Can only be left empty if the mesh node doesn't contain any polygons")
    a_vertices: FloatVectorProperty(name="Vertices", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="An array of polygon vertex positions. Can only be left empty if the mesh node doesn't contain any polygons. Animated vertices are only taken into account for motion blur if A_CONSTANT_TOPOLOGY is set to TRUE and A_POLY_VERTEX_SPEED is empty")
    a_poly_vertex_indices: IntProperty(name="Poly vertex indices", default=0, update=OctaneBaseNode.update_node_tree, description="An array that stores the indices into A_VERTICES and A_POLY_VERTEX_SPEED for each vertex of each polygon. Its size must be equal to the sum of all vertex counts in A_VERTICES_PER_POLY")
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
    a_volume_channel_offsets: IntProperty(name="Volume channel offsets", default=0, update=OctaneBaseNode.update_node_tree, description="These zero-based offsets specify the first float in a voxel referenced by the channel at the corresponding index in A_VOLUME_CHANNEL_IDS. If negative, it will be assumed that the respective channel is disabled. When importing a VDB, this array will be populated automatically, but when loading a grid via A_VOLUME_REGULAR_GRID, then the size of this array must match the size of A_VOLUME_CHANNEL_IDS")
    a_volume_channel_max_values: FloatVectorProperty(name="Volume channel max values", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum float values in the channels corresponding to A_VOLUME_CHANNEL_IDS. These will be determined automatically")
    a_volume_channel_defaults: FloatVectorProperty(name="Volume channel defaults", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The default background values for the channels corresponding to A_VOLUME_CHANNEL_IDS. Usually (0, 0, 0). When importing a VDB, this array will be populated automatically, but when loading a grid via A_VOLUME_REGULAR_GRID, then the size of this array must match the size of A_VOLUME_CHANNEL_IDS")
    a_volume_channel_is_float3: BoolProperty(name="Volume channel is float3", default=False, update=OctaneBaseNode.update_node_tree, description="A bool array to indicate if the channels corresponding to A_VOLUME_CHANNEL_IDS provide a single float (false) or a float3 (true) per voxel. When importing a VDB, this array will be populated automatically, but when loading a grid via A_VOLUME_REGULAR_GRID, then the size of this array must match the size of A_VOLUME_CHANNEL_IDS")
    a_volume_regular_grid: FloatProperty(name="Volume regular grid", default=0.000000, update=OctaneBaseNode.update_node_tree, description="Voxels are stored in order of x-axis, followed by rows up the y-axis, then finally, it repeats for each z-slice. If you have more than one float per voxel, then store each voxel as a set of floats contiguously. After that you set A_VOLUME_ABSORPTION_OFFSET, A_VOLUME_SCATTER_OFFSET, A_VOLUME_EMISSION_OFFSET and A_VOLUME_VELOCITY_OFFSET_{XYZ} to an integer index into your voxels. For example, if you have 2 floats in each voxel, and the second float is what you want for scatter, then you set A_VOLUME_SCATTER_OFFSET to 1.\n\n Optionally, you can also provide the A_VOLUME_CHANNEL_{IDS, OFFSETS, DEFAULTS, IS_FLOAT3} array attributes to load additional named channels for use with standard volume mediums. The floats of any float3 channel must be stored in consecutive indices of the voxel.\n\n You must provide at least one valid offset. Finally, set A_VOLUME_RESOLUTION to the number of voxels in each dimension. The volume at this point is set in space with each voxel measuring 1m x 1m x 1m. To change the scale, you can set A_TRANSFORM")
    a_volume_resolution: IntVectorProperty(name="Volume resolution", default=(0, 0, 0), size=3, update=OctaneBaseNode.update_node_tree, description="Voxel resolution of the volume")
    a_volume_voxel_float_size: IntProperty(name="Volume voxel float size", default=0, update=OctaneBaseNode.update_node_tree, description="The voxel size in floats for the volume channel data stored in each voxel. This will be set automatically")

    def init(self, context):
        self.inputs.new("OctaneMeshVolumeSDFMaterial1", OctaneMeshVolumeSDFMaterial1.bl_label).init()
        self.inputs.new("OctaneMeshVolumeSDFObjectLayer", OctaneMeshVolumeSDFObjectLayer.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMeshVolumeSDFMaterial1,
    OctaneMeshVolumeSDFObjectLayer,
    OctaneMeshVolumeSDF,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
