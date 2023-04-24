import bpy
import numpy as np
import xml.etree.ElementTree as ET
from collections import defaultdict
from array import array
from octane.utils import consts, utility
from octane.core.client import OctaneBlender
from octane.core.caches import OctaneNodeCache
from octane.core.octane_info import OctaneInfoManger
from octane.core.octane_node import OctaneNode, CArray


class ScatterData(object):
    def __init__(self, object_name):
        self.object_name = object_name        
        self.matrices = array("f", [])
        self.instance_ids = array("I", [])


class ObjectCache(OctaneNodeCache):
    TYPE_NAME = "OBJECT"

    MAX_OCTANE_COLOR_VERTEX_SETS = 2
    MAX_OCTANE_FLOAT_VERTEX_SETS = 4
    VOLUME_DENSITY_C_ARRAY_IDENTIFIER = "VOLUME_DENSITY"
    VOLUME_FLAME_C_ARRAY_IDENTIFIER = "VOLUME_FLAME"
    VOLUME_VELOCITY_C_ARRAY_IDENTIFIER = "VOLUME_VELOCITY"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Object
        self.type_collection_name = "objects"
        self.object_name_to_material_data_map = {}
        self.changed_particle_object_names = set()
        self.changed_material_slot_object_names = set()
        self.changed_mesh_names = set()
        self.object_instance_num = 0
        self.persistent_id_to_octane_scatter_id_map = defaultdict(dict)
        # Blender object name => Octane scatter node name
        self.synced_object_name_map = {}
        self.synced_mesh_names = set()
        # Motion blur
        self.motion_blur_node_names = {}

    @staticmethod
    def cast_light_mask(data):
        property_to_bits = ["light_id_sunlight", "light_id_env", "light_id_pass_1", "light_id_pass_2", "light_id_pass_3", "light_id_pass_4", "light_id_pass_5", "light_id_pass_6", "light_id_pass_7", "light_id_pass_8"]
        value = 0
        for idx, property_name in enumerate(property_to_bits):
            value += (int(getattr(data, property_name)) << idx)
        return value

    def resolve_octane_scatter_id(self, object_name, persistent_id):
        persistent_id_str_key = "_".join([str(pid) for pid in persistent_id])
        if not persistent_id_str_key in self.persistent_id_to_octane_scatter_id_map[object_name]:
            self.persistent_id_to_octane_scatter_id_map[object_name][persistent_id_str_key] = len(self.persistent_id_to_octane_scatter_id_map[object_name])
        return self.persistent_id_to_octane_scatter_id_map[object_name][persistent_id_str_key]

    def resolve_object_material_data_tag(self, _object):
        if _object.type != "EMPTY" and len(_object.material_slots) > 0:
            return ",".join([mat_slot.name for mat_slot in _object.material_slots])
        return ""

    def resolve_octane_id(self, name, node_type, prefix=""):
        return prefix + name + str(node_type)

    def has_octane_node(self, name, node_type, prefix=""):
        octane_node_id = self.resolve_octane_id(name, node_type, prefix)
        return self.has_data(octane_node_id)

    def get_octane_node(self, name, node_type, prefix=""):
        octane_node_id = self.resolve_octane_id(name, node_type, prefix)
        octane_node_name = prefix + name
        if self.has_data(octane_node_id):
            octane_node = self.get(octane_node_name, octane_node_id)
        else:
            octane_node = self.add(octane_node_name, node_type, octane_node_id)
        return octane_node

    def update_geometry_data(self, depsgraph, _object, object_eval, mesh, octane_node, motion_time_offset=0):
        mesh_data = _object.data
        octane_data = mesh_data.octane
        use_octane_coordinate = utility.use_octane_coordinate(_object)
        # Vertices
        vertices_num = len(mesh.vertices)
        vertices_addr = mesh.vertices[0].as_pointer() if vertices_num > 0 else 0
        if motion_time_offset == 0:
            # Normals
            normals_num = len(mesh.vertex_normals)
            normals_addr = mesh.vertex_normals[0].as_pointer() if normals_num > 0 else 0
            # Loop triangles
            loop_triangles_num = len(mesh.loop_triangles)
            loop_triangles_addr = mesh.loop_triangles[0].as_pointer() if loop_triangles_num > 0 else 0            
            # Loop
            loops_num = len(mesh.loops)
            loops_addr = mesh.loops[0].as_pointer() if loops_num > 0 else 0
            # Polygons
            polygons_num = len(mesh.polygons)
            polygons_addr = mesh.polygons[0].as_pointer() if polygons_num > 0 else 0
            winding_order = int(octane_data.winding_order)
            used_shaders_num = max(1, len(object_eval.data.materials))
            # UV Data
            uv_data = []
            active_uv_layer_index = -1
            if mesh.uv_layers:
                for idx, uv in enumerate(mesh.uv_layers):
                    uv_data.append(uv.data[0].as_pointer())
                    if uv.active_render:
                        active_uv_layer_index = idx
            octane_node.node.set_mesh_attribute(vertices_addr, vertices_num, 
                normals_addr, normals_num, 
                loop_triangles_addr, loop_triangles_num,
                loops_addr, loops_num,
                polygons_addr, polygons_num,
                use_octane_coordinate, False, False, winding_order, used_shaders_num, active_uv_layer_index, uv_data)
        else:
            octane_node.node.set_mesh_motion_attribute(vertices_addr, vertices_num, motion_time_offset, use_octane_coordinate)

    def update_hair_data(self, depsgraph, _object, object_eval, mesh, octane_node, motion_time_offset=0):
        # Hair Data
        has_hair_data = False
        is_viewport = depsgraph.mode == "VIEWPORT"
        inverted_matrix_world = object_eval.matrix_world.copy()
        inverted_matrix_world.invert_safe()
        hair_vertex_data = []
        hair_uv_data = []
        hair_vertex_per_strand = []
        hair_material_index_configs = []
        hair_min_curvature_configs = []
        hair_width_configs = []
        hair_w_configs = []        
        for psys in _object.particle_systems:
            settings = psys.settings
            if settings.type == "HAIR" and settings.render_type == "PATH":
                has_hair_data = True
                break
        if has_hair_data:
            # UV Data
            active_uv_index = -1
            if mesh.uv_layers:
                for idx, uv in enumerate(mesh.uv_layers):
                    if uv.active_render:
                        active_uv_index = idx
                        break
            for particle_system in object_eval.particle_systems:
                settings = particle_system.settings
                vertex_data = []
                if particle_system.particles and settings.type == "HAIR" and settings.render_type == "PATH":
                    shader_index = settings.material - 1
                    particle_num = len(particle_system.particles)
                    particle_child_num = len(particle_system.child_particles)
                    if is_viewport:
                        particle_child_num = int(particle_child_num * settings.display_percentage / 100.0)
                    strand_num = particle_child_num
                    if settings.child_type == "None" or particle_child_num == 0:
                        strand_num += particle_num
                    if strand_num == 0:
                        continue
                    step = settings.display_step if is_viewport else settings.render_step
                    vertex_per_strand = 2 ** step + 1                
                    if settings.kink == "SPIRAL":
                        vertex_per_strand += settings.kink_extra_steps
                    particle_start_index = 0
                    if settings.child_type != "None" and particle_child_num != 0:
                        particle_start_index = particle_num
                    co_hair = particle_system.co_hair
                    vertex_data = np.fromiter((elem 
                        for particle_index in range(particle_start_index, strand_num)
                        for step in range(vertex_per_strand)
                        for elem in co_hair(object=object_eval, particle_no=particle_index, step=step)),
                        dtype=np.float32, count=(strand_num - particle_start_index) * vertex_per_strand * 3)
                uv_data = []
                if len(vertex_data) > 0:
                    particle_system_mod = None
                    for mod in object_eval.modifiers:
                        if mod.type == "PARTICLE_SYSTEM" and mod.particle_system.name == particle_system.name:
                            particle_system_mod = mod
                            break            
                    if particle_system_mod is not None and active_uv_index != -1:
                        uv_on_emitter = particle_system.uv_on_emitter
                        try:
                            uv_data = np.fromiter((elem
                                for particle_index in range(particle_start_index, strand_num)
                                for elem in uv_on_emitter(particle_system_mod, particle=particle_system.particles[particle_index] if particle_child_num == 0 else particle_system.particles[0], particle_no=particle_index, uv_no=active_uv_index)),
                                dtype=np.float32, count=(strand_num - particle_start_index) * 2)
                        except:
                            pass
                if len(vertex_data) > 0:
                    hair_vertex_data.append(vertex_data)
                    hair_uv_data.append(uv_data)
                    hair_vertex_per_strand.append(vertex_per_strand)
                    hair_material_index_configs.append(shader_index)
                    hair_min_curvature_configs.append(settings.octane.min_curvature)
                    hair_width_configs.append([settings.octane.root_width, settings.octane.tip_width])
                    hair_w_configs.append([settings.octane.w_min, settings.octane.w_max])
        octane_node.node.set_hair_attribute(inverted_matrix_world, hair_vertex_data, hair_uv_data, hair_vertex_per_strand, hair_material_index_configs, hair_min_curvature_configs, hair_width_configs, hair_w_configs, motion_time_offset)

    def update_mesh_data(self, depsgraph, _object, octane_node, motion_time_offset=0):
        # Geometry Data
        object_eval = _object.evaluated_get(depsgraph)
        mesh = None
        need_subdivision = False
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
        if mesh is None:
            if object_eval:
                object_eval.to_mesh_clear()
            return
        # Geometry Data
        self.update_geometry_data(depsgraph, _object, object_eval, mesh, octane_node, motion_time_offset)
        # Hair Data
        self.update_hair_data(depsgraph, _object, object_eval, mesh, octane_node, motion_time_offset)
        # Clear Mesh
        if object_eval and mesh:
            object_eval.to_mesh_clear()

    def update_mesh(self, depsgraph, _object, octane_node, motion_time_offset=0):
        # Check mesh cache
        mesh_data = _object.data
        mesh_name = mesh_data.name
        # Do not process the unchanged mesh data repeatly
        if not utility.is_reshapable_proxy(_object) and mesh_name not in self.changed_mesh_names and mesh_name in self.synced_mesh_names:
            return
        # Modify cache tag data
        if mesh_name in self.changed_mesh_names:
            self.changed_mesh_names.remove(mesh_name)
        self.synced_mesh_names.add(mesh_name)
        # Materials
        material_names = [(material.name if material else "") for material in mesh_data.materials]
        octane_node.set_attribute_blender_name("SHADER_NAMES", consts.AttributeType.AT_STRING, ";".join(material_names))
        # Objects
        octane_node.set_attribute_blender_name("OBJECT_NAMES", consts.AttributeType.AT_STRING, "__" + octane_node.name)
        # Mesh Data
        self.update_mesh_data(depsgraph, _object, octane_node, motion_time_offset)

    def update_octane_orbx_proxy(self, name, filepath):
        from octane.core.octane_node import OctaneNode
        orbx_proxy_node = OctaneNode(name, consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE)
        orbx_proxy_node.node.set_orbx_proxy_attributes(filepath)
        orbx_proxy_node.update_to_engine(True)
        content = orbx_proxy_node.node.get_response()
        orbx_proxy_output_name = orbx_proxy_node.node.get_graph_linker_name(0, False)
        use_objectlayer = True
        if len(content):
            content_et = ET.fromstring(content)
            use_objectlayer = content_et.get("useObjectLayer") == "true" if content_et is not None else False
        return use_objectlayer

    def update_grid_data(self, grid_data, grid_data_identify, octane_node):
        c_array = octane_node.get_array_data(grid_data_identify)
        grid_data_num = len(grid_data)
        if grid_data_num > 0:
            if c_array is None or len(c_array) != grid_data_num:
                octane_node.delete_array_data(grid_data_identify)
            if octane_node.new_array_data(grid_data_identify, CArray.FLOAT, grid_data_num, 1):
                c_array = octane_node.get_array_data(grid_data_identify)
            if c_array is not None:
                grid_data.foreach_get(c_array)
        else:
            octane_node.delete_array_data(grid_data_identify)

    def update_volume(self, depsgraph, _object, octane_node):
        object_eval = _object.evaluated_get(depsgraph)
        material_name = ""
        if len(object_eval.data.materials) > 0:
            material_name = object_eval.data.materials[0].name
        octane_node.set_pin_id(consts.PinID.P_MEDIUM if octane_node.node_type == consts.NodeType.NT_GEO_VOLUME else consts.PinID.P_MATERIAL1, True, material_name, "")
        if _object.type == "MESH":
            domain_modifier = utility.find_smoke_domain_modifier(object_eval)
            if domain_modifier is not None:
                domain_settings = domain_modifier.domain_settings
                amplify = domain_settings.noise_scale if domain_settings.use_noise else 1
                resolution = [res * amplify for res in domain_settings.domain_resolution]
                width, height, depth = resolution[0], resolution[1], resolution[2]
                resolution_num = width * height * depth
                if resolution_num > 0:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_RESOLUTION, resolution)
                    self.update_grid_data(domain_settings.density_grid, self.VOLUME_DENSITY_C_ARRAY_IDENTIFIER, octane_node)
                    self.update_grid_data(domain_settings.flame_grid, self.VOLUME_FLAME_C_ARRAY_IDENTIFIER, octane_node)
                    self.update_grid_data(domain_settings.velocity_grid, self.VOLUME_VELOCITY_C_ARRAY_IDENTIFIER, octane_node)
                    bound_box = _object.bound_box
                    x_min = min([p[0] for p in bound_box])
                    y_min = min([p[1] for p in bound_box])
                    z_min = min([p[2] for p in bound_box])
                    x_max = max([p[0] for p in bound_box])
                    y_max = max([p[1] for p in bound_box])
                    z_max = max([p[2] for p in bound_box])
                    m = [[(x_max - x_min) / width, 0, 0, x_min], [0, (y_max - y_min) / height, 0, y_min], [0, 0, (z_max - z_min) / depth, z_min]]
                    octane_node.set_attribute_id(consts.AttributeID.A_TRANSFORM, m)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_MOTION_BLUR_ENABLED, True)
                    octane_node.need_update = True
        elif _object.type == "VOLUME":
            volume_data = _object.data
            octane_data = volume_data.octane
            # Update auto refresh attribute
            if volume_data.is_sequence:
                self.auto_refresh_data_names[_object.name] = consts.AutoRereshStrategy.FRAME_CHANGE
            else:
                if _object.name in self.auto_refresh_data_names:
                    self.auto_refresh_data_names.remove(_object.name)
            if not volume_data.grids.is_loaded:
                volume_data.grids.load()
            filepath = bpy.path.abspath(volume_data.grids.frame_filepath)
            active_grid_name = ""
            if volume_data.grids.is_loaded and len(volume_data.grids):
                volume_data.grids[volume_data.grids.active_index].name
            octane_node.set_attribute_id(consts.AttributeID.A_FILENAME, filepath)
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ISOVALUE, octane_data.vdb_iso)
            octane_node.set_attribute_id(consts.AttributeID.A_GEOIMP_SCALE_UNIT, utility.get_enum_int_value(octane_data, "vdb_import_scale", 4))
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_MOTION_BLUR_ENABLED, octane_data.vdb_motion_blur_enabled)
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_SCALE, octane_data.vdb_abs_scale)
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_SCALE, octane_data.vdb_emiss_scale)
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_SCALE, octane_data.vdb_scatter_scale)
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_SCALE, octane_data.vdb_vel_scale)
            if octane_data.vdb_velocity_grid_type == "Vector grid":
                if len(octane_data.vdb_vector_grid_id) > 0:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID, octane_data.vdb_vector_grid_id)
                else:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID, active_grid_name)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_X, "")
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Y, "")
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Z, "")
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_X, octane_data.vdb_x_components_grid_id)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Y, octane_data.vdb_y_components_grid_id)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Z, octane_data.vdb_z_components_grid_id)
            if len(octane_data.vdb_absorption_grid_id) > 0:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_ID, octane_data.vdb_absorption_grid_id)
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_ID, active_grid_name)
            if len(octane_data.vdb_scattering_grid_id) > 0:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_ID, octane_data.vdb_scattering_grid_id)
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_ID, active_grid_name)
            if len(octane_data.vdb_emission_grid_id) > 0:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_ID, octane_data.vdb_emission_grid_id)
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_ID, active_grid_name)
            if octane_node.need_update:
                octane_node.set_attribute_id(consts.AttributeID.A_RELOAD, True)

    def update_light(self, depsgraph, _object, light_node_name):
        light = _object.data
        linked_name = ""
        linked_light_name = ""
        if light.use_nodes:
            node_tree = light.node_tree
            owner_type = utility.get_node_tree_owner_type(light)
            active_output_node = utility.find_active_output_node(node_tree, owner_type)
            if active_output_node and len(active_output_node.inputs):                
                linked_light_name = utility.get_octane_name_for_root_node(active_output_node, "Surface", light)
                linked_name = linked_light_name
        if light.type == "AREA":
            need_init = not self.has_octane_node(light_node_name, consts.NodeType.NT_GEO_OBJECT)
            geo_object_node = self.get_octane_node(light_node_name, consts.NodeType.NT_GEO_OBJECT)
            if need_init:
                # Force Init
                geo_object_node.set_pin_id(consts.PinID.P_PRIMITIVE, False, "", 0)
                geo_object_node.update_to_engine(True)
            transform_node_name = light_node_name + "[Transform]"
            _3d_transform_node = self.get_octane_node(transform_node_name, consts.NodeType.NT_TRANSFORM_3D)
            linked_name = light_node_name
            primitive_type = 0
            rotation = [0, 0, 0]
            scale = [1, 1, 1]
            if light.shape == "DISK":
                primitive_type = 6 # ("Disc", "Disc", "", 6),
                rotation = [-90, 0, 0]
                scale = [light.size, 1, light.size]
            elif light.shape == "ELLIPSE":
                primitive_type = 6 # ("Disc", "Disc", "", 6),
                rotation = [-90, 0, 0]
                scale = [light.size, 1, light.size_y]
            elif light.shape == "RECTANGLE":
                primitive_type = 18 # ("Quad", "Quad", "", 18),
                rotation = [0, 180, 0]
                scale = [light.size, light.size_y, 1]
            elif light.shape == "SQUARE":
                primitive_type = 18 # ("Quad", "Quad", "", 18),
                rotation = [0, 180, 0]
                scale = [light.size, light.size, 1]
            geo_object_node.set_pin_id(consts.PinID.P_PRIMITIVE, False, "", primitive_type)
            geo_object_node.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, transform_node_name)
            geo_object_node.set_pin_id(consts.PinID.P_MATERIAL, True, linked_light_name, linked_light_name)
            _3d_transform_node.set_pin_id(consts.PinID.P_ROTATION, False, "", rotation)
            _3d_transform_node.set_pin_id(consts.PinID.P_SCALE, False, "", scale)
            if geo_object_node.need_update:
                geo_object_node.update_to_engine(True)
            if _3d_transform_node.need_update:
                _3d_transform_node.update_to_engine(True)
        return linked_name

    def update_object_layer(self, node, octane_data):
        node.set_pin_id(consts.PinID.P_LAYER_ID, False, "", octane_data.render_layer_id)
        node.set_pin_id(consts.PinID.P_GENERAL_VISIBILITY, False, "", octane_data.general_visibility)
        node.set_pin_id(consts.PinID.P_CAMERA_VISIBILITY, False, "", octane_data.camera_visibility)
        node.set_pin_id(consts.PinID.P_SHADOW_VISIBILITY, False, "", octane_data.shadow_visibility)
        node.set_pin_id(consts.PinID.P_DIRT_VISIBILITY, False, "", octane_data.dirt_visibility)
        node.set_pin_id(consts.PinID.P_CURVATURE_VISIBILITY, False, "", octane_data.curvature_visibility)
        node.set_pin_id(consts.PinID.P_RANDOM_SEED, False, "", octane_data.random_color_seed)
        node.set_pin_id(consts.PinID.P_OBJECT_COLOR, False, "", [int(c * 255.0) for c in octane_data.color])
        node.set_pin_id(consts.PinID.P_CUSTOM_AOV, False, "", utility.get_enum_int_value(octane_data, "custom_aov", 4096))
        node.set_pin_id(consts.PinID.P_CUSTOM_AOV_CHANNEL, False, "", utility.get_enum_int_value(octane_data, "custom_aov_channel", 0))
        node.set_pin_id(consts.PinID.P_BAKING_GROUP_ID, False, "", octane_data.baking_group_id)
        # Baking Transform
        transform_node_name = node.name + "[Transform]"
        _2d_transform_node = node.get_subnode(transform_node_name, consts.NodeType.NT_TRANSFORM_2D)
        _2d_transform_node.set_pin_id(consts.PinID.P_ROTATION, False, "", octane_data.baking_uv_transform_rz)
        _2d_transform_node.set_pin_id(consts.PinID.P_SCALE, False, "", (octane_data.baking_uv_transform_sx, octane_data.baking_uv_transform_sy))
        _2d_transform_node.set_pin_id(consts.PinID.P_TRANSLATION, False, "", (octane_data.baking_uv_transform_tx, octane_data.baking_uv_transform_ty))
        node.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, "")
        # Light ID Mask
        mask_value = 0
        for idx, property_name in enumerate(("light_id_sunlight", "light_id_env", "light_id_pass_1", "light_id_pass_2", "light_id_pass_3", "light_id_pass_4", "light_id_pass_5", "light_id_pass_6", "light_id_pass_7", "light_id_pass_8")):
            mask_value += (int(getattr(octane_data, property_name)) << idx)
        pin_info = OctaneInfoManger().get_pin_info_by_id(node.node_type, consts.PinID.P_LIGHT_PASS_MASK)
        node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name, consts.SocketType.ST_INT, pin_info.pin_type, pin_info.default_node_type, False, "", mask_value)

    def remove_object(self, removed_object_name):
        octane_scatter_name = self.synced_object_name_map[removed_object_name]
        del self.synced_object_name_map[removed_object_name]
        octane_scatter_node = self.get_octane_node(octane_scatter_name, consts.NodeType.NT_GEO_SCATTER)
        octane_scatter_node.set_pin_id(consts.PinID.P_GEOMETRY, True, "", "")
        octane_scatter_node.node.reset()
        octane_scatter_node.node.build()
        octane_scatter_node.update_to_engine(True)

    def update_object(self, scene, depsgraph, _object, octane_scatter_node):
        # General
        is_viewport = depsgraph.mode == "VIEWPORT"
        object_name = utility.resolve_octane_object_name(_object, scene, is_viewport)
        geometry_name = utility.resolve_octane_geometry_name(_object, scene, is_viewport)
        objectlayer_name = utility.resolve_octane_objectlayer_name(_object, scene, is_viewport)
        objectlayer_map_name = utility.resolve_octane_objectlayer_map_name(_object, scene, is_viewport)
        objectlayer_map_linked_mesh_name = geometry_name
        use_objectlayer = True
        octane_objectlayer_node = self.get_octane_node(objectlayer_name, consts.NodeType.NT_OBJECTLAYER)
        octane_objectlayer_map_node = self.get_octane_node(objectlayer_map_name, consts.NodeType.NT_OBJECTLAYER_MAP)
        use_multiple_objectlayers = False
        octane_mesh_node = None
        octane_property = getattr(_object.data, "octane", None)
        if _object.type == "MESH":
            # Mesh Data
            imported_orbx_file_path = getattr(octane_property, "imported_orbx_file_path", "")
            if len(imported_orbx_file_path):
                geometry_name = bpy.path.basename(imported_orbx_file_path)
                use_objectlayer = self.update_octane_orbx_proxy(geometry_name, imported_orbx_file_path)                
                objectlayer_map_linked_mesh_name = geometry_name
                use_multiple_objectlayers = True
            else:
                geometry_node_data = octane_property.octane_geo_node_collections
                if len(geometry_node_data.node_graph_tree) and len(geometry_node_data.osl_geo_node):
                    objectlayer_map_linked_mesh_name = geometry_node_data.node_graph_tree + "_" + geometry_node_data.osl_geo_node
                domain_modifier = utility.find_smoke_domain_modifier(_object)
                if domain_modifier is None or domain_modifier.domain_settings.use_mesh:
                    octane_mesh_node = self.get_octane_node(geometry_name, consts.NodeType.NT_GEO_MESH)
                    self.update_mesh(depsgraph, _object, octane_mesh_node)
                else:
                    octane_mesh_node = self.get_octane_node(geometry_name, consts.NodeType.NT_GEO_VOLUME)
                    self.update_volume(depsgraph, _object, octane_mesh_node)
                if octane_mesh_node.need_update:
                    octane_mesh_node.update_to_engine(True) 
        elif _object.type == "VOLUME":
            if _object.data.octane.vdb_sdf:
                octane_mesh_node = self.get_octane_node(geometry_name, consts.NodeType.NT_GEO_VOLUME_SDF)
            else:
                octane_mesh_node = self.get_octane_node(geometry_name, consts.NodeType.NT_GEO_VOLUME)
            self.update_volume(depsgraph, _object, octane_mesh_node)
            if octane_mesh_node.need_update:
                octane_mesh_node.update_to_engine(True)
        elif _object.type == "LIGHT":
            objectlayer_map_linked_mesh_name = self.update_light(depsgraph, _object, geometry_name)
        elif _object.type == "EMPTY":
            geometry_name = ""
            use_objectlayer = False
        # Set the Object Layers
        if use_objectlayer:
            octane_objectlayer_map_node.set_pin_id(consts.PinID.P_GEOMETRY, True, objectlayer_map_linked_mesh_name, "")
            # Update the nodes to the engine
            if octane_objectlayer_map_node.need_update:
                octane_objectlayer_map_node.update_to_engine(True)
            # Update the objectlayer at the last stage
            self.update_object_layer(octane_objectlayer_node, _object.octane)
            if octane_objectlayer_node.need_update:
                octane_objectlayer_node.update_to_engine(True)
            objectlayer_map_node_object_layer_num = 1
            if use_multiple_objectlayers:
                objectlayer_map_node_info = utility.fetch_node_info(objectlayer_map_name)
                if objectlayer_map_node_info is not None:
                    objectlayer_map_node_object_layer_num = objectlayer_map_node_info["dynPinCount"]
            for idx in range(objectlayer_map_node_object_layer_num):
                octane_objectlayer_node.link_to(objectlayer_map_name, idx + 1)
       # Set and build the Scatter node
        if use_objectlayer:            
            octane_scatter_node.set_pin_id(consts.PinID.P_GEOMETRY, True, objectlayer_map_name, "")
        else:
            octane_scatter_node.set_pin_id(consts.PinID.P_GEOMETRY, True, geometry_name, "")
        octane_scatter_node.node.build()
        if octane_scatter_node.need_update:
            octane_scatter_node.update_to_engine(True)        
        self.synced_object_name_map[_object.name] = octane_scatter_node.name

    def update_objects(self, scene, depsgraph): 
        is_viewport = depsgraph.mode == "VIEWPORT"
        # Find all changed meshes
        self.changed_mesh_names.clear()
        if depsgraph.id_type_updated("MESH") or depsgraph.id_type_updated("VOLUME"):
            for dg_update in depsgraph.updates:
                self.changed_mesh_names.add(dg_update.id.name)
        for object_name in self.changed_particle_object_names:
            self.changed_mesh_names.add(depsgraph.scene.objects[object_name].data.name)
        for object_name in self.changed_material_slot_object_names:
            self.changed_mesh_names.add(depsgraph.scene.objects[object_name].data.name)
        scatter_map = {}
        removed_object_names = set(self.synced_object_name_map.keys())
        updated_motion_blur_node_names = set()
        for instance_object in depsgraph.object_instances:
            _object = instance_object.object
            object_name = instance_object.object.name
            if object_name in removed_object_names:
                removed_object_names.remove(object_name)            
            scatter_name = utility.resolve_octane_scatter_name(instance_object, scene, is_viewport)
            octane_scatter_node = None
            if scatter_name not in scatter_map:
                scatter_map[scatter_name] = self.get_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER)
                scatter_map[scatter_name].node.reset()
            octane_scatter_node = scatter_map[scatter_name]
            octane_scatter_node.object_name = object_name
            octane_scatter_id = self.resolve_octane_scatter_id(object_name, instance_object.persistent_id)
            # we have to make a copy here, otherwise we get an identity matrix when passing to C++
            object_matrix = instance_object.matrix_world.copy()
            use_octane_coordinate = utility.use_octane_coordinate(_object)
            octane_scatter_node.node.set_instance(octane_scatter_id, octane_scatter_id, object_matrix, use_octane_coordinate)
            if self.session.need_motion_blur:
                if scatter_name not in updated_motion_blur_node_names:
                    motion_time_offsets = utility.object_motion_time_offsets(_object, self.session.motion_blur_start_frame_offset, self.session.motion_blur_end_frame_offset)
                    if instance_object.parent is not None:
                        parent_motion_time_offsets = utility.object_motion_time_offsets(instance_object.parent, self.session.motion_blur_start_frame_offset, self.session.motion_blur_end_frame_offset)
                        if parent_motion_time_offsets is not None:
                            if motion_time_offsets is None:
                                motion_time_offsets = parent_motion_time_offsets
                            else:
                                motion_time_offsets = motion_time_offsets.union(parent_motion_time_offsets)
                    if motion_time_offsets is not None:
                        octane_scatter_node.need_motion_blur = True
                        octane_scatter_node.motion_time_offsets = motion_time_offsets
                        for offset in motion_time_offsets:
                            self.session.motion_blur_time_offsets.add(offset)
                updated_motion_blur_node_names.add(scatter_name)
        for removed_object_name in removed_object_names:
            self.remove_object(removed_object_name)
        for scatter_name, octane_scatter_node in scatter_map.items():
            _object = bpy.data.objects[octane_scatter_node.object_name]
            self.update_object(scene, depsgraph, _object, octane_scatter_node)
        self.changed_data_names.clear()

    def update_motion_blur_sample(self, motion_time_offset, depsgraph, scene, view_layer, context=None):
        for instance_object in depsgraph.object_instances:
            _object = instance_object.object
            object_name = instance_object.object.name
            scatter_name = utility.resolve_octane_scatter_name(instance_object, scene, False)
            if not self.has_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER):
                continue
            octane_scatter_node = self.get_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER)
            if octane_scatter_node.motion_time_offsets and motion_time_offset in octane_scatter_node.motion_time_offsets:
                octane_scatter_id = self.resolve_octane_scatter_id(object_name, instance_object.persistent_id)
                object_matrix = instance_object.matrix_world.copy()
                use_octane_coordinate = utility.use_octane_coordinate(_object)
                octane_scatter_node.node.set_motion_sample(octane_scatter_id, motion_time_offset, object_matrix, use_octane_coordinate)
                self.motion_blur_node_names[scatter_name] = consts.NodeType.NT_GEO_SCATTER
                # Mesh Deformation
                if _object.octane.use_deform_motion:
                    if _object.type == "MESH":
                        # Mesh Data
                        domain_modifier = utility.find_smoke_domain_modifier(_object)
                        if domain_modifier is None or domain_modifier.domain_settings.use_mesh:                    
                            geometry_name = utility.resolve_octane_geometry_name(_object, scene, False)
                            octane_mesh_node = self.get_octane_node(geometry_name, consts.NodeType.NT_GEO_MESH)
                            if not hasattr(octane_mesh_node, "updated_motion_time_offsets"):
                                octane_mesh_node.updated_motion_time_offsets = {}
                            if not octane_mesh_node.updated_motion_time_offsets.get(motion_time_offset, False):
                                self.update_mesh_data(depsgraph, _object, octane_mesh_node, motion_time_offset)
                                octane_mesh_node.updated_motion_time_offsets[motion_time_offset] = True
                                self.motion_blur_node_names[geometry_name] = consts.NodeType.NT_GEO_MESH

    def update_motion_blur(self, depsgraph, scene, view_layer, context=None):
        for node_name, node_type in self.motion_blur_node_names.items():
            octane_node = self.get_octane_node(node_name, node_type)
            octane_node.node.build()
            if octane_node.need_update:
                octane_node.update_to_engine(True)

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        # Materials
        if depsgraph.id_type_updated("MATERIAL"):
            for _object in depsgraph.scene.objects:
                if _object.name in self.object_name_to_material_data_map:
                    material_tag = self.resolve_object_material_data_tag(_object)
                    if self.object_name_to_material_data_map[_object.name] != material_tag:
                        self.changed_material_slot_object_names.add(_object.name)
                        self.object_name_to_material_data_map[_object.name] = material_tag
                        self.need_update = True                        
        for dg_update in depsgraph.updates:
            if isinstance(dg_update.id, bpy.types.Object):
                material_tag = self.resolve_object_material_data_tag(dg_update.id)
                self.object_name_to_material_data_map[dg_update.id.name] = material_tag
        # Particles
        if depsgraph.id_type_updated("PARTICLE"):
            changed_particle_settings_names = set()
            for dg_update in depsgraph.updates:
                if isinstance(dg_update.id, bpy.types.ParticleSettings):
                    changed_particle_settings_names.add(dg_update.id.name)
            if len(changed_particle_settings_names) > 0:
                for _object in depsgraph.scene.objects:
                    for particle_system in _object.particle_systems:
                        if particle_system.settings.name in changed_particle_settings_names:
                            self.changed_particle_object_names.add(_object.name)
                            self.need_update = True
        if self.object_instance_num != len(depsgraph.object_instances):
            self.need_update = True
            self.object_instance_num = len(depsgraph.object_instances)

    def update(self, depsgraph, scene, view_layer, context=None):        
        self.update_objects(scene, depsgraph)
        self.need_update = False