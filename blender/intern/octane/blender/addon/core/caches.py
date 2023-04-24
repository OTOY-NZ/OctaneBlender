import bpy
from collections import defaultdict
from octane.utils import consts, utility
from octane.core.client import OctaneClient
from octane.core.octane_node import OctaneNode, OctaneNodeType, CArray


class NodeTreeAttributes(object):
    def __init__(self):
        self.auto_refresh = False
        self.image_names = []
        self.object_names = []


class BaseDataCache(object):
    def __init__(self, session):
        self.session = session        
        self.type_name = ""
        self.type_class = None
        self.type_collection_name = ""
        self.last_update_frame = 0
        self.cached_data = {}
        self.changed_data_names = set()
        # {type_name => {data => a set of dependent names}}
        self.data_to_dependent = defaultdict(lambda: defaultdict(set))
        # {type_name => {dependent => a set of data names}
        self.dependent_to_data = defaultdict(lambda: defaultdict(set))
        self.auto_refresh_data_names = set()
        self.need_update_all = True
        self.need_update = False

    def reset(self, session):
        self.session = session
        self.last_update_frame = 0
        self.cached_data.clear()
        self.changed_data_names.clear()
        self.data_to_dependent.clear()
        self.dependent_to_data.clear()
        self.need_update_all = True
        self.need_update = False

    def need_update(self):
        return self.need_update

    def has_data(self, name):
        return name in self.cached_data

    def get(self, name):
        if name in self.cached_data:
            return self.cached_data[name]
        return None

    def add(self, name):
        self.cached_data[name] = name

    def remove(self, name):
        if name in self.cached_data:
            del self.cached_data[name]
        if name in self.auto_refresh_data_names:
            self.auto_refresh_data_names.remove(name)

    def add_all(self, context, depsgraph):
        for _id in getattr(bpy.data, self.type_collection_name):
            self.changed_data_names.add(_id.name)
            self.need_update = True
        self.need_update_all = False

    def dependency_diff(self, context, depsgraph):
        pass

    def custom_diff(self, context, depsgraph):
        pass

    def diff(self, engine, context, depsgraph):
        self.changed_data_names.clear()
        if self.need_update_all:
            self.add_all(context, depsgraph)
        else:
            if depsgraph.id_type_updated(self.type_name):
                for dg_update in depsgraph.updates:
                    if isinstance(dg_update.id, self.type_class):
                        self.changed_data_names.add(dg_update.id.name)
                        self.need_update = True          
            # Process auto refresh
            if self.last_update_frame != context.scene.frame_current:
                if len(self.auto_refresh_data_names):
                    self.changed_data_names.update(self.auto_refresh_data_names)
                    self.need_update = True
            # Process dependency
            self.dependency_diff(context, depsgraph)
            self.custom_diff(context, depsgraph)
        self.last_update_frame = context.scene.frame_current
        return self.need_update

    def update(self, engine, context, depsgraph):
        pass


class OctaneNodeCache(BaseDataCache):

    @staticmethod
    def generate_octane_node_id(node_name, node_id):
        return "%s[%s]" % (node_name, node_id)

    def add(self, node_name, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_name, node_id)
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        self.cached_data[_id] = octane_node
        return octane_node

    def get(self, node_name, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_name, node_id)
        if _id in self.cached_data:
            return self.cached_data[_id]
        return None


class OctaneRenderTargetCache(BaseDataCache):
    DEFAULT_RENDERTARGET_NAME = "RenderTarget"
    P_CAMERA_NAME = "camera"
    P_IMAGER_NAME = "imager"
    P_KERNEL_NAME = "kernel"
    P_ENVIRONMENT_NAME = "environment"
    P_VISIBLE_ENVIRONMENT_NAME = "cameraEnvironment"
    P_RENDER_PASSES_NAME = "renderPasses"
    P_OUTPUT_AOVS_NAME = "compositeAovs"
    P_POST_PROCESSING_NAME = "postproc"

    def __init__(self, session):
        super().__init__(session)
        self.rendertarget_node = self.add(self.DEFAULT_RENDERTARGET_NAME)
        self.links = {}

    def get_rendertarget_node(self):
        return self.rendertarget_node

    def add(self, name):
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        octane_node.set_name(name)
        octane_node.set_node_type(consts.NodeType.NT_RENDERTARGET)
        self.cached_data[name] = octane_node
        return octane_node

    def diff(self, engine, context, depsgraph):
        return self.rendertarget_node.need_update

    def update(self, engine, context, depsgraph):        
        if self.rendertarget_node.need_update:
            self.session.add_to_update_node_queue(self.rendertarget_node)

    def update_link(self, pin_name, node_name, link_name):
        self.rendertarget_node.set_blender_attribute(pin_name, consts.AttributeType.AT_STRING, link_name)
        # If the linked blender node is changed, force to update it
        if self.links.get(pin_name, None) != node_name:
            self.links[pin_name] = node_name
            self.rendertarget_node.need_update = True

    def update_links(self, owner_type, input_socket_name, root_node, root_name):
        node_name = root_node.name if root_node else ""
        link_name = root_name if root_node else ""
        if owner_type == consts.OctaneNodeTreeIDName.MATERIAL:
            pass
        elif owner_type == consts.OctaneNodeTreeIDName.WORLD:
            if input_socket_name in (consts.OctaneOutputNodeSocketNames.ENVIRONMENT, consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT):                
                self.update_link(self.P_ENVIRONMENT_NAME, node_name, link_name)
            elif input_socket_name in (consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT, consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT):                
                self.update_link(self.P_VISIBLE_ENVIRONMENT_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.COMPOSITE:
            self.update_link(self.P_OUTPUT_AOVS_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.RENDER_AOV:
            self.update_link(self.P_RENDER_PASSES_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.KERNEL:
            self.update_link(self.P_KERNEL_NAME, node_name, link_name)


class ObjectCache(BaseDataCache):
    TYPE_NAME = "OBJECT"
    # Object attributes
    BLENDER_ATTRIBUTE_OBJECT_COUNT = "OBJECT_COUNT"
    BLENDER_ATTRIBUTE_OBJECT_NAME = "OBJECT_NAME"
    BLENDER_ATTRIBUTE_MESH_NAME = "MESH_NAME"
    BLENDER_ATTRIBUTE_INSTANCE_SIZE = "INSTANCE_SIZE"
    BLENDER_ATTRIBUTE_INSTANCE_ID = "INSTANCE_ID"
    BLENDER_ATTRIBUTE_SAMPLE_NUM = "SAMPLE_NUM"
    BLENDER_ATTRIBUTE_USE_OBJECTLAYER_MODE = "USE_OBJECTLAYER_MODE"
    # Mesh attributes
    BLENDER_ATTRIBUTE_MESH_COUNT = "MESH_COUNT"
    BLENDER_ATTRIBUTE_OSL_GEO_NAME = "OSL_GEO_NAME"
    BLENDER_ATTRIBUTE_ORBX_PATH = "ORBX_PATH"
    BLENDER_ATTRIBUTE_SHADER_NAMES = "SHADER_NAMES"
    BLENDER_ATTRIBUTE_OBJECTS_NAMES = "OBJECTS_NAMES"
    BLENDER_ATTRIBUTE_ACTIVE_UV_INDEX = "ACTIVE_UV_INDEX"
    BLENDER_ATTRIBUTE_HAIR_W_SIZE = "HAIR_W_SIZE"
    BLENDER_ATTRIBUTE_HAIR_INTERPOLATIONS = "HAIR_INTERPOLATIONS"
    BLENDER_ATTRIBUTE_INFINITE_PLANE = "INFINITE_PLANE"
    BLENDER_ATTRIBUTE_RESHAPEABLE = "RESHAPEABLE"
    BLENDER_ATTRIBUTE_MAX_SMOOTH_ANGLE = "MAX_SMOOTH_ANGLE"
    BLENDER_ATTRIBUTE_MESH_DATA_UPDATE = "MESH_DATA_UPDATE"
    BLENDER_ATTRIBUTE_SHOW_VERTEX_DATA = "SHOW_VERTEX_DATA"
    BLENDER_ATTRIBUTE_VERTEX_COLOR_NAMES = "VERTEX_COLOR_NAMES"
    BLENDER_ATTRIBUTE_VERTEX_FLOAT_NAMES = "VERTEX_FLOAT_NAMES"
    # Mesh Subdivision attributes
    BLENDER_ATTRIBUTE_SUBDIVISION = "SUBDIVISION"
    BLENDER_ATTRIBUTE_SUBDIVISION_SCHEME = "SUBDIVISION_SCHEME"
    BLENDER_ATTRIBUTE_SUBDIVISION_LEVEL = "SUBDIVISION_LEVEL"
    BLENDER_ATTRIBUTE_SUBDIVISION_SHARPNESS = "SUBDIVISION_SHARPNESS"
    BLENDER_ATTRIBUTE_SUBDIVISION_BOUND_INTERPOLATION = "SUBDIVISION_BOUND_INTERPOLATION"
    BLENDER_ATTRIBUTE_SUBDIVISION_DATA_NEED_UPDATE = "SUBDIVISION_DATA_NEED_UPDATE"
    # Sphere attributes
    BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_ENABLE = "SPHERE_ATTRIBUTE_ENABLE"
    BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_RADIUS = "SPHERE_ATTRIBUTE_RADIUS"
    BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_RANDOM_SEED = "SPHERE_ATTRIBUTE_RANDOM_SEED"
    BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_MIN_RANDOM_RADIUS = "SPHERE_ATTRIBUTE_MIN_RANDOM_RADIUS"
    BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_MAX_RANDOM_RADIUS = "SPHERE_ATTRIBUTE_MAX_RANDOM_RADIUS"
    # Object layer attributes
    BLENDER_ATTRIBUTE_RENDER_LAYER_ID = "RENDER_LAYER_ID"
    BLENDER_ATTRIBUTE_GENERAL_VISIBILITY = "GENERAL_VISIBILITY"
    BLENDER_ATTRIBUTE_CAMERA_VISIBILITY = "CAMERA_VISIBILITY"
    BLENDER_ATTRIBUTE_SHADOW_VISIBILITY = "SHADOW_VISIBILITY"
    BLENDER_ATTRIBUTE_DIRT_VISIBILITY = "DIRT_VISIBILITY"
    BLENDER_ATTRIBUTE_RANDOM_COLOR_SEED = "RANDOM_COLOR_SEED"
    BLENDER_ATTRIBUTE_COLOR = "COLOR"
    BLENDER_ATTRIBUTE_BAKING_GROUP_ID = "BAKING_GROUP_ID"
    BLENDER_ATTRIBUTE_BAKING_TRANSFORM_ROTATION_Z = "BAKING_TRANSFORM_ROTATION_Z"
    BLENDER_ATTRIBUTE_BAKING_TRANSFORM_SCALE = "BAKING_TRANSFORM_SCALE"
    BLENDER_ATTRIBUTE_BAKING_TRANSFORM_TRANSLATION = "BAKING_TRANSFORM_TRANSLATION"
    BLENDER_ATTRIBUTE_LIGHT_PASS_MASK = "LIGHT_PASS_MASK"
    BLENDER_ATTRIBUTE_CUSTOM_AOV = "CUSTOM_AOV"
    BLENDER_ATTRIBUTE_CUSTOM_AOV_CHANNEL = "CUSTOM_AOV_CHANNEL"

    MAX_OCTANE_COLOR_VERTEX_SETS = 2
    MAX_OCTANE_FLOAT_VERTEX_SETS = 4

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Object
        self.type_collection_name = "objects"
        self.changed_mesh_names = set()
        self.synced_mesh_names = set()
       
    def update_start(self):
        self.object_index = 0
        self.mesh_index = 0
        self.object_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        self.object_node.set_name("LOAD_OBJECTS")
        self.object_node.set_node_type(consts.NodeType.NT_BLENDER_NODE_SCATTER)
        self.mesh_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        self.mesh_node.set_name("LOAD_MESHES")
        self.mesh_node.set_node_type(consts.NodeType.NT_BLENDER_NODE_MESH)
        self.mesh_node.create_scene_data("LOAD_MESHES")

    def update_end(self):
        self.object_index = 0
        self.mesh_index = 0
        self.object_node = None
        self.mesh_node.release_scene_data("LOAD_MESHES")
        self.mesh_node = None

    @staticmethod
    def resolve_identifier_with_index(identifier, index):
        return identifier + consts.OBJECT_INDEX_SEPARATOR + str(index)

    def set_object_attribute(self, attribute_name, attribute_type, value):
        return self.object_node.set_blender_attribute(ObjectCache.resolve_identifier_with_index(attribute_name, self.object_index), attribute_type, value)    

    def set_mesh_attribute(self, attribute_name, attribute_type, value):
        return self.mesh_node.set_blender_attribute(ObjectCache.resolve_identifier_with_index(attribute_name, self.mesh_index), attribute_type, value)    

    def set_object_layer_attribute(self, node, attribute_name, index, attribute_type, value):
        return node.set_blender_attribute(ObjectCache.resolve_identifier_with_index(attribute_name, index), attribute_type, value)

    def create_object_array(self, identifier, size, _type, dimension=1):
        array_identifier = ObjectCache.resolve_identifier_with_index(identifier, self.object_index)            
        self.object_node.create_c_array(size, array_identifier, _type, dimension)
        c_array = self.object_node.get_c_array(array_identifier, _type)
        c_array.need_update = True
        return c_array.array

    def create_mesh_array(self, identifier, size, _type, dimension=1):
        array_identifier = ObjectCache.resolve_identifier_with_index(identifier, self.mesh_index)            
        self.mesh_node.create_c_array(size, array_identifier, _type, dimension)
        c_array = self.mesh_node.get_c_array(array_identifier, _type)
        c_array.need_update = True
        return c_array.array

    @staticmethod
    def cast_light_mask(data):
        property_to_bits = ["light_id_sunlight", "light_id_env", "light_id_pass_1", "light_id_pass_2", "light_id_pass_3", "light_id_pass_4", "light_id_pass_5", "light_id_pass_6", "light_id_pass_7", "light_id_pass_8"]
        value = 0
        for idx, property_name in enumerate(property_to_bits):
            value += (int(getattr(data, property_name)) << idx)
        return value

    def update_changed_mesh_names(self, depsgraph):
        self.changed_mesh_names.clear()
        if depsgraph.id_type_updated("MESH"):
            for dg_update in depsgraph.updates:
                self.changed_mesh_names.add(dg_update.id.name)

    def update_object_layer(self, node, index, octane_data):
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_RENDER_LAYER_ID, index, consts.AttributeType.AT_INT, octane_data.render_layer_id)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_GENERAL_VISIBILITY, index, consts.AttributeType.AT_FLOAT, octane_data.general_visibility)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_CAMERA_VISIBILITY, index, consts.AttributeType.AT_BOOL, octane_data.camera_visibility)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_SHADOW_VISIBILITY, index, consts.AttributeType.AT_BOOL, octane_data.shadow_visibility)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_DIRT_VISIBILITY, index, consts.AttributeType.AT_BOOL, octane_data.dirt_visibility)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_RANDOM_COLOR_SEED, index, consts.AttributeType.AT_INT, octane_data.random_color_seed)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_COLOR, index, consts.AttributeType.AT_INT3, [int(c * 255.0) for c in octane_data.color])
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_BAKING_GROUP_ID, index, consts.AttributeType.AT_INT, octane_data.baking_group_id)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_BAKING_TRANSFORM_ROTATION_Z, index, consts.AttributeType.AT_FLOAT, octane_data.baking_uv_transform_rz)
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_BAKING_TRANSFORM_SCALE, index, consts.AttributeType.AT_FLOAT2, (octane_data.baking_uv_transform_sx, octane_data.baking_uv_transform_sy))
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_BAKING_TRANSFORM_TRANSLATION, index, consts.AttributeType.AT_FLOAT2, (octane_data.baking_uv_transform_tx, octane_data.baking_uv_transform_ty))
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_CUSTOM_AOV, index, consts.AttributeType.AT_INT, utility.get_enum_value(octane_data, "custom_aov", 4096))
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_CUSTOM_AOV_CHANNEL, index, consts.AttributeType.AT_INT, utility.get_enum_value(octane_data, "custom_aov_channel", 0))
        self.set_object_layer_attribute(node, self.BLENDER_ATTRIBUTE_LIGHT_PASS_MASK, index, consts.AttributeType.AT_INT, ObjectCache.cast_light_mask(octane_data))

    def update_mesh_array_data(self, engine, context, depsgraph, _object, mesh_name, need_subdivision=False, winding_order=0):
        self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_MESH_DATA_UPDATE, consts.AttributeType.AT_BOOL, True)
        # Create Mesh
        mesh = None
        object_eval = _object.evaluated_get(depsgraph)
        if object_eval:
            mesh = object_eval.to_mesh()
            if mesh and not need_subdivision:
                if mesh.use_auto_smooth:
                    if not mesh.has_custom_normals:
                        mesh.calc_normals()
                    mesh.split_faces()
                mesh.calc_loop_triangles()
                if mesh.has_custom_normals:
                    mesh.calc_normals_split()
        vertices_num = len(mesh.vertices)
        vertices_addr = mesh.vertices[0].as_pointer() if vertices_num > 0 else 0
        loop_triangles_num = len(mesh.loop_triangles)
        loop_triangles_addr = mesh.loop_triangles[0].as_pointer() if loop_triangles_num > 0 else 0
        loops_num = len(mesh.loops)
        loops_addr = mesh.loops[0].as_pointer() if loops_num > 0 else 0
        polygons_num = len(mesh.polygons)
        polygons_addr = mesh.polygons[0].as_pointer() if polygons_num > 0 else 0
        materials_num = max(1, len(object_eval.data.materials))
        # UV Data
        uv_addrs = []
        active_uv_set_index = 0
        if mesh.uv_layers:
            for idx, uv in enumerate(mesh.uv_layers):
                uv_addrs.append(uv.data[0].as_pointer())
                if uv.active_render:
                    active_uv_set_index = idx
        self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_ACTIVE_UV_INDEX, consts.AttributeType.AT_INT, active_uv_set_index)
        # Vertex Float Data
        blender_vertex_float_num = len(object_eval.vertex_groups)
        vertex_float_num = min(self.MAX_OCTANE_FLOAT_VERTEX_SETS, blender_vertex_float_num)
        vertex_float_names = []
        vertex_float_arrays = []
        vertex_group_index_map = {}
        if vertex_float_num > 0:
            self.create_mesh_array(consts.ArrayIdentifier.ARRAY_INFO_VERTEX_FLOAT_DATA, vertex_float_num, CArray.INT, 1)
        for idx, vertex_group in enumerate(object_eval.vertex_groups):
            vertex_float_names.append(vertex_group.name)
            vertex_float_arrays.append(self.create_mesh_array(consts.ArrayIdentifier.ARRAY_INFO_VERTEX_FLOAT_DATA + str(idx), vertices_num, CArray.FLOAT, 1))
            vertex_float_arrays[-1].fill(0)
            vertex_group_index_map[vertex_group.index] = idx
        for v_idx, vertex in enumerate(mesh.vertices):
            for group in vertex.groups:
                group_id = group.group
                if group_id in vertex_group_index_map:
                    vertex_float_arrays[vertex_group_index_map[group_id]][v_idx] = group.weight
        self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_VERTEX_FLOAT_NAMES, consts.AttributeType.AT_STRING, ";".join(vertex_float_names))
        # Vertex Color Data
        blender_vertex_colors_num = len(mesh.vertex_colors)
        vertex_colors_num = min(self.MAX_OCTANE_COLOR_VERTEX_SETS, blender_vertex_colors_num)
        inactive_vertex_colors_num = self.MAX_OCTANE_COLOR_VERTEX_SETS - 1
        vertex_color_addrs = []
        vertex_color_names = []
        if mesh.vertex_colors:
            for idx, col in enumerate(mesh.vertex_colors):
                if inactive_vertex_colors_num == 0 and not col.active_render:
                    continue
                if not col.active_render:
                    inactive_vertex_colors_num -= 1
                vertex_color_names.append(col.name)
                vertex_color_addrs.append(col.data[0].as_pointer())
                if len(vertex_color_names) >= self.MAX_OCTANE_COLOR_VERTEX_SETS:
                    break
        self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_VERTEX_COLOR_NAMES, consts.AttributeType.AT_STRING, ";".join(vertex_color_names))
        # Build Mesh Data via C API
        dict_args = {
            "INDEX": self.mesh_index, 
            "VERTICES_NUM": vertices_num, 
            "VERTICES_ADDR": vertices_addr, 
            "LOOP_TRIANGLES_NUM": loop_triangles_num, 
            "LOOP_TRIANGLES_ADDR": loop_triangles_addr, 
            "LOOPS_NUM": loops_num, 
            "LOOPS_ADDR": loops_addr, 
            "POLYGONS_NUM": polygons_num, 
            "POLYGONS_ADDR": polygons_addr,
            "UVS_ADDR": uv_addrs,
            "VERTEX_COLORS_ADDR": vertex_color_addrs,
            "NEED_SUBDIVISION": need_subdivision,
            "WINDING_ORDER": winding_order,
            "USED_SHADER_NUM": materials_num,
            "ACTIVE_UV_LAYER_INDEX": active_uv_set_index,
        }
        self.mesh_node.build_scene_data(consts.SceneDataType.MESH, dict_args)
        # Build Mesh Subdivision Data via C API
        if need_subdivision:
            edges_num = len(mesh.edges)
            edges_addr = mesh.edges[0].as_pointer() if edges_num > 0 else 0            
            subd_dict_args = {
                "INDEX": self.mesh_index, 
                "EDGES_NUM": edges_num, 
                "EDGES_ADDR": edges_addr,
            }
            self.mesh_node.build_scene_data(consts.SceneDataType.SUBDIVISION_MESH, subd_dict_args)
        # Clear Mesh
        if object_eval and mesh:
            object_eval.to_mesh_clear()

    def update_mesh(self, engine, context, depsgraph, _object):
        mesh_data = _object.data
        mesh_name = mesh_data.name
        if mesh_name in self.changed_data_names or mesh_name not in self.synced_mesh_names:
            show_vertex_data = True
            octane_mesh_name = utility.resolve_mesh_octane_name(_object, context.scene, True)
            octane_data = mesh_data.octane
            # General
            osl_geo_name = utility.resolve_octane_vectron_name(_object)
            orbx_proxy_path = bpy.path.abspath(octane_data.imported_orbx_file_path)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_MESH_NAME, consts.AttributeType.AT_STRING, octane_mesh_name)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_OSL_GEO_NAME, consts.AttributeType.AT_STRING, osl_geo_name)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_ORBX_PATH, consts.AttributeType.AT_STRING, orbx_proxy_path)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_INFINITE_PLANE, consts.AttributeType.AT_BOOL, octane_data.infinite_plane)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_RESHAPEABLE, consts.AttributeType.AT_BOOL, False)
            # Materials
            material_names = [material.name for material in mesh_data.materials]            
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SHADER_NAMES, consts.AttributeType.AT_STRING, ";".join(material_names))
            # Objects
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_OBJECTS_NAMES, consts.AttributeType.AT_STRING, "__" + octane_mesh_name)
            # Subdivision
            open_subd_enable = octane_data.open_subd_enable
            open_subd_level = octane_data.open_subd_level
            need_subdivision = open_subd_enable and open_subd_level > 0
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION, consts.AttributeType.AT_BOOL, open_subd_enable)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION_SCHEME, consts.AttributeType.AT_INT, int(octane_data.open_subd_scheme))
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION_LEVEL, consts.AttributeType.AT_INT, octane_data.open_subd_level)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION_SHARPNESS, consts.AttributeType.AT_FLOAT, octane_data.open_subd_sharpness)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION_BOUND_INTERPOLATION, consts.AttributeType.AT_INT, int(octane_data.open_subd_bound_interp))
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SUBDIVISION_DATA_NEED_UPDATE, consts.AttributeType.AT_BOOL, True)
            # Sphere Attributes
            if octane_data.octane_hide_original_mesh:
                show_vertex_data = False
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_ENABLE, consts.AttributeType.AT_BOOL, octane_data.octane_enable_sphere_attribute)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_RADIUS, consts.AttributeType.AT_FLOAT, octane_data.octane_sphere_radius)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_RANDOM_SEED, consts.AttributeType.AT_INT, octane_data.octane_sphere_randomized_radius_seed if octane_data.octane_use_randomized_radius else -1)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_MIN_RANDOM_RADIUS, consts.AttributeType.AT_FLOAT, octane_data.octane_sphere_randomized_radius_min)
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SPHERE_ATTRIBUTE_MAX_RANDOM_RADIUS, consts.AttributeType.AT_FLOAT, octane_data.octane_sphere_randomized_radius_max)
            # Mesh Data
            self.update_mesh_array_data(engine, context, depsgraph, _object, mesh_name, need_subdivision, int(octane_data.winding_order))
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_HAIR_INTERPOLATIONS, consts.AttributeType.AT_INT, int(octane_data.hair_interpolation))
            hair_w_size = 0
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_HAIR_W_SIZE, consts.AttributeType.AT_INT, hair_w_size)            
            self.set_mesh_attribute(self.BLENDER_ATTRIBUTE_SHOW_VERTEX_DATA, consts.AttributeType.AT_BOOL, show_vertex_data)
            self.mesh_index += 1
            self.synced_mesh_names.add(mesh_name)

    def update_object(self, engine, context, depsgraph, _object):
        # General
        object_name = utility.resolve_object_octane_name(_object, context.scene, True)
        mesh_name = utility.resolve_mesh_octane_name(_object, context.scene, True)
        self.set_object_attribute(self.BLENDER_ATTRIBUTE_OBJECT_NAME, consts.AttributeType.AT_STRING, object_name)            
        if _object.type == "MESH":
            osl_geo_name = utility.resolve_octane_vectron_name(_object)
            if len(osl_geo_name):
                mesh_name = osl_geo_name
            orbx_proxy_path = bpy.path.abspath(_object.data.octane.imported_orbx_file_path)
            self.set_object_attribute(self.BLENDER_ATTRIBUTE_MESH_NAME, consts.AttributeType.AT_STRING, mesh_name)       
            self.set_object_attribute(self.BLENDER_ATTRIBUTE_INSTANCE_SIZE, consts.AttributeType.AT_INT, 1)
            self.set_object_attribute(self.BLENDER_ATTRIBUTE_INSTANCE_ID, consts.AttributeType.AT_INT, 0)
            self.set_object_attribute(self.BLENDER_ATTRIBUTE_SAMPLE_NUM, consts.AttributeType.AT_INT, 1)
            self.set_object_attribute(self.BLENDER_ATTRIBUTE_USE_OBJECTLAYER_MODE, consts.AttributeType.AT_INT, 2 if len(orbx_proxy_path) else 1)
            # Transforms
            matrix = utility.OctaneMatrixConvertor.get_octane_matrix(_object.matrix_world)
            array = self.create_object_array(consts.ArrayIdentifier.ARRAY_INFO_MATRIX_DATA, 12, CArray.FLOAT)            
            array_index = 0
            for i in range(3):
                for j in range(4):
                    array[array_index] = matrix[i][j]
                    array_index += 1
            # Instance ID
            array = self.create_object_array(consts.ArrayIdentifier.ARRAY_INFO_INSTANCE_ID_DATA, 1, CArray.INT)
            array[0] = -1
            # Mesh Data
            self.update_mesh(engine, context, depsgraph, _object)
            # Object Layer
            self.update_object_layer(self.object_node, self.object_index, _object.octane)
            # Object Index
            self.object_index += 1            


    def update_objects(self, engine, context, depsgraph):
        for name in self.changed_data_names:
            _object = getattr(bpy.data, self.type_collection_name).get(name, None)
            self.update_object(engine, context, depsgraph, _object)            
        self.object_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_OBJECT_COUNT, consts.AttributeType.AT_INT, self.object_index)
        self.mesh_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_MESH_COUNT, consts.AttributeType.AT_INT, self.mesh_index)

    def update(self, engine, context, depsgraph):
        self.update_start()
        self.update_changed_mesh_names(depsgraph)
        self.update_objects(engine, context, depsgraph)
        if self.mesh_node and self.mesh_node.need_update:
            OctaneClient().process_octane_node(self.mesh_node)
        if self.object_node and self.object_node.need_update:
            OctaneClient().process_octane_node(self.object_node)
        self.need_update = False
        self.update_end()

class ImageCache(BaseDataCache):
    TYPE_NAME = "IMAGE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Image
        self.type_collection_name = "images"


class NodeTreeCache(BaseDataCache):

    def _dependency_diff(self, context, depsgraph, cache_depend_on):
        if cache_depend_on and len(cache_depend_on.changed_data_names):
            for dependent_name in cache_depend_on.changed_data_names:
                for data_name in self.dependent_to_data[cache_depend_on.type_name][dependent_name]:
                    self.changed_data_names.add(data_name)
                    self.need_update = True

    def dependency_diff(self, context, depsgraph):
        # Process image
        self._dependency_diff(context, depsgraph, self.session.image_cache)
        # Process object
        self._dependency_diff(context, depsgraph, self.session.object_cache)

    def use_node_tree(self, context, _id):
        return _id is not None and _id.use_nodes

    def get_node_tree(self, _id):
        return _id.node_tree

    def update(self, engine, context, depsgraph):
        self.custom_update(context, depsgraph)
        for name in self.changed_data_names:            
            _id = getattr(bpy.data, self.type_collection_name).get(name, None)
            if self.use_node_tree(context, _id):
                data_name = _id.name
                node_tree_attributes = NodeTreeAttributes()
                self.session.update_node_tree(context, self.get_node_tree(_id), _id, node_tree_attributes)
                self.add(data_name)
                # Update auto refresh attribute
                if node_tree_attributes.auto_refresh:
                    self.auto_refresh_data_names.add(data_name)
                else:
                    if data_name in self.auto_refresh_data_names:
                        self.auto_refresh_data_names.remove(data_name)
                # Update image attribute
                self.data_to_dependent[ImageCache.TYPE_NAME][data_name] = set(node_tree_attributes.image_names)
                # Update object attribute
                self.data_to_dependent[ObjectCache.TYPE_NAME][data_name] = set(node_tree_attributes.object_names)
        # Update image attribute
        self.dependent_to_data[ImageCache.TYPE_NAME].clear()
        for data_name, dependent_set in self.data_to_dependent[ImageCache.TYPE_NAME].items():
            for dependent_name in dependent_set:
                self.dependent_to_data[ImageCache.TYPE_NAME][dependent_name].add(data_name)
        # Update object attribute
        self.dependent_to_data[ObjectCache.TYPE_NAME].clear()
        for data_name, dependent_set in self.data_to_dependent[ObjectCache.TYPE_NAME].items():
            for dependent_name in dependent_set:
                self.dependent_to_data[ObjectCache.TYPE_NAME][dependent_name].add(data_name)
        self.changed_data_names.clear()
        self.need_update = False

    def custom_update(self, context, depsgraph):
        pass


class MaterialCache(NodeTreeCache):
    TYPE_NAME = "MATERIAL"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Material
        self.type_collection_name = "materials"


class WorldCache(NodeTreeCache):
    TYPE_NAME = "WORLD"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.World
        self.type_collection_name = "worlds"
        self.last_name = ""

    def use_node_tree(self, context, _id):
        return super().use_node_tree(context, _id) and context.scene.world is _id

    def custom_diff(self, context, depsgraph):
        current_name = getattr(context.scene.world, "name", "")
        if current_name != self.last_name:
            self.last_name = current_name
            self.need_update = True

    def custom_update(self, context, depsgraph):        
        if context.scene.world is None:            
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.ENVIRONMENT, None, "")
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT, None, "")


class CompositeCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_composite_node_tree(context) is _id

    def find_active_composite_node_tree(self, context):
        node_tree = utility.find_active_composite_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_composite_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_composite_node_tree(context) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneOutputNodeSocketNames.COMPOSITE, None, "")


class RenderAOVCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_render_aov_node_tree(context) is _id

    def find_active_render_aov_node_tree(self, context):
        node_tree = utility.find_active_render_aov_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_render_aov_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_render_aov_node_tree(context) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.RENDER_AOV, consts.OctaneOutputNodeSocketNames.RENDER_AOV, None, "")            


class KernelCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_kernel_node_tree(context) is _id

    def find_active_kernel_node_tree(self, context):
        node_tree = utility.find_active_kernel_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_kernel_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_kernel_node_tree(context) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.KERNEL, consts.OctaneOutputNodeSocketNames.KERNEL, None, "")


class SceneCache(BaseDataCache):
    def __init__(self, session):
        super().__init__(session)
        self.camera_node = self.create_octane_node(consts.OctanePresetNodeTreeNames.CAMERA)
        self.imager_node = self.create_octane_node(consts.OctanePresetNodeTreeNames.IMAGER, consts.NodeType.NT_IMAGER_CAMERA)
        self.post_processing_node = self.create_octane_node(consts.OctanePresetNodeTreeNames.POST_PROCESSING, consts.NodeType.NT_POSTPROCESSING)
        self.last_camera_name = ""
        self.last_imager_name = ""
        self.last_post_processing_name = ""

    def create_octane_node(self, name, node_type=None):
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        octane_node.set_name(name)
        if node_type is not None:
            octane_node.set_node_type(node_type)
        return octane_node

    def diff(self, engine, context, depsgraph):
        if self.need_update_all or depsgraph.id_type_updated("SCENE") or depsgraph.id_type_updated("CAMERA"):
            self.need_update_all = False
            self.need_update = True
        else:
            _, post_processing_name = utility.find_active_post_process_data(context)            
            if post_processing_name != self.last_post_processing_name:
                self.last_post_processing_name = post_processing_name
                self.need_update = True
            _, imager_name = utility.find_active_imager_data(context)
            if imager_name != self.last_imager_name:
                self.last_imager_name = imager_name
                self.need_update = True            
        return self.need_update

    def update(self, engine, context, depsgraph):
        if self.need_update:
            self.update_post_processing(context, depsgraph)
            self.update_imager(context, depsgraph)
        self.need_update = False

    def update_camera(self, engine, context, depsgraph):        
        camera_data, camera_name = utility.find_active_camera_data(context)
        is_viewport = self.session.is_viewport()
        if is_viewport:
            camera_data.sync_data(self.camera_node, engine=engine, scene=context.scene, region=context.region, v3d=context.space_data, rv3d=context.region_data, is_viewport=True)
        else:
            camera_data.sync_data(self.camera_node, engine=engine, scene=context.scene, is_viewport=False)
        if self.camera_node.need_update:
            self.session.add_to_update_node_queue(self.camera_node)
        self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_CAMERA_NAME, self.camera_node.name, self.camera_node.name)            

    def update_post_processing(self, context, depsgraph):
        camera_data, camera_name = utility.find_active_post_process_data(context)
        if camera_data is None:
            self.post_processing_node.set_pin("on_off", "postprocess", consts.SocketType.ST_BOOL, False, False, "")
        else:
            self.post_processing_node.set_pin("on_off", "postprocess", consts.SocketType.ST_BOOL, getattr(camera_data, "postprocess", False), False, "")            
            camera_data.post_processing.sync_data(self.post_processing_node, scene=context.scene, is_viewport=self.session.is_viewport())
        if self.post_processing_node.need_update:
            self.session.add_to_update_node_queue(self.post_processing_node)
        self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_POST_PROCESSING_NAME, self.post_processing_node.name, self.post_processing_node.name)

    def update_imager(self, context, depsgraph):
        camera_data, camera_name = utility.find_active_imager_data(context)
        enable_imager = utility.is_active_imager_enabled(context)
        if not enable_imager or camera_data is None:
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_IMAGER_NAME, "", "")
        else:
            camera_data.imager.sync_data(self.imager_node, scene=context.scene, is_viewport=self.session.is_viewport())
            if self.imager_node.need_update:
                self.session.add_to_update_node_queue(self.imager_node)
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_IMAGER_NAME, self.imager_node.name, self.imager_node.name)