# <pep8 compliant>

import array
import copy
import math
import os
from xml.etree import ElementTree
from collections import defaultdict

import bpy
import mathutils
import numpy as np
from octane.core.caches import OctaneNodeCache
from octane.core.octane_info import OctaneInfoManger
from octane.core.resource_cache import ResourceCache
from octane.utils import consts, utility, octane_name
from octane.utils import curve as curve_utils
from octane.utils.utility import BlenderID


class ObjectMaterialTagManager(object):
    def __init__(self):
        # Material tags for objects
        self.object_to_material_tag_map = {}

    @staticmethod
    def resolve_tag(material_cache, _object):
        if _object is not None:
            # ensure it's an original object
            origin_object = _object.original
            if origin_object.material_slots is not None and len(origin_object.material_slots) > 0:
                material_names = []
                for mat_slot in origin_object.material_slots:
                    mat = mat_slot.material
                    octane_mat_name = material_cache.get_octane_node_tree_name(mat)
                    material_names.append(octane_mat_name)
                return ";".join(material_names)
        return ""

    @staticmethod
    def resolve_first_material_octane_name(tag):
        return tag.split(";")[0]

    def update_tag(self, material_cache, _object):
        new_tag = self.resolve_tag(material_cache, _object)
        obj_blender_id = BlenderID(_object)
        if self.object_to_material_tag_map.get(obj_blender_id, None) != new_tag:
            self.object_to_material_tag_map[obj_blender_id] = new_tag
            return True, new_tag
        return False, new_tag

    def update_object_material_tags(self, material_cache, depsgraph, updated_object_names):
        for _object in depsgraph.scene.objects:
            obj_blender_id = BlenderID(_object)
            if obj_blender_id in self.object_to_material_tag_map:
                is_updated, new_tag = self.update_tag(material_cache, _object)
                if is_updated:
                    updated_object_names.add(_object.name)


class ObjectCache(OctaneNodeCache):
    TYPE_NAME = "OBJECT"

    MAX_OCTANE_COLOR_VERTEX_SETS = 2
    MAX_OCTANE_FLOAT_VERTEX_SETS = 4
    BLENDER_ATTRIBUTE_MESH_DATA_UPDATE = "MESH_DATA_UPDATE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Object
        self.type_collection_name = "objects"
        self.geometry_group_node = self.add_node(consts.OctanePresetNodeNames.GEOMETRY_GROUP,
                                                 consts.NodeType.NT_GEO_GROUP)
        # Material tags for objects, used for detecting the cases of material changes (add, remove, rename)
        self.object_material_tag_manager = ObjectMaterialTagManager()
        # Depsgraph updated evaluated object data names. Reset every view_update.
        # Used for detecting whether an object's data is updated in Blender's depsgraph in this view_update.
        # In this way, we can optimize the performance by filtering the unchanged object data.
        self.dg_updated_object_data_names = set()
        # A set of octane names of the object data which are updated to the octane. Reset every view_update. Used for
        # detecting whether an object's data is synced to Octane engine in this view_update. After processing the
        # data, we can add the octane name to the set to mark it as processed, preventing duplicates from being
        # processed again.
        self.oct_synced_object_data_octane_names = set()
        # Data for the depsgraph object instances, used for detecting the cases of object deletion
        self.depsgraph_object_instances_num_changed = False
        self.depsgraph_object_instances_num = 0
        self.depsgraph_object_instance_names = set()
        # Blender object instances' persistent ids => Octane scatter ids
        self.persistent_id_to_octane_scatter_id_map = defaultdict(dict)
        # Octane scatter node names
        self.synced_octane_scatter_node_names = set()
        # Motion blur
        self.motion_blur_node_names = {}

    def custom_add_all(self, depsgraph):
        for _id in [item for item in depsgraph.ids if (isinstance(item, bpy.types.Mesh)
                                                       or isinstance(item, bpy.types.Volume)
                                                       or isinstance(item, bpy.types.Light)
                                                       or isinstance(item, bpy.types.Curve)
                                                       or isinstance(item, bpy.types.Curves))]:
            self.dg_updated_object_data_names.add(_id.name)
            self.need_update = True

    def depsgraph_update_diff(self, depsgraph, scene, view_layer, context=None):
        # Sometimes Blender's id_type_updated cannot return the correct result even if the corresponding data block
        # is changed(e.g. OBJECT) So we need to a force check here
        for dg_update in depsgraph.updates:
            if isinstance(dg_update.id, self.type_class):
                self.changed_data_ids.add(BlenderID(dg_update.id))
                self.need_update = True
            if dg_update.is_updated_geometry:
                object_data_name = getattr(getattr(dg_update.id, "data", None), "name", "")
                if len(object_data_name):
                    self.dg_updated_object_data_names.add(object_data_name)

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        # Look for changes of particle systems
        if depsgraph.id_type_updated("PARTICLE"):
            updated_particle_settings_names = set()
            for dg_update in depsgraph.updates:
                if isinstance(dg_update.id, bpy.types.ParticleSettings):
                    updated_particle_settings_names.add(dg_update.id.name)
            if len(updated_particle_settings_names) > 0:
                updated_particle_object_names = set()
                for eval_object in depsgraph.objects:
                    for particle_system in eval_object.particle_systems:
                        if particle_system.settings.name in updated_particle_settings_names:
                            updated_particle_object_names.add(eval_object.name)
                for object_name in updated_particle_object_names:
                    if object_name in depsgraph.objects:
                        self.dg_updated_object_data_names.add(depsgraph.objects[object_name].data.name)
        # Detection for changes of numbers of instances
        depsgraph_object_instances_num = 0
        for instance_object in depsgraph.object_instances:
            eval_object = instance_object.object
            if context and context.space_data:
                show_in_viewport = eval_object.visible_in_viewport_get(context.space_data)
            else:
                show_in_viewport = True
            if show_in_viewport:
                depsgraph_object_instances_num += 1
        if self.depsgraph_object_instances_num != depsgraph_object_instances_num:
            self.depsgraph_object_instances_num = depsgraph_object_instances_num
            self.need_update = True
            self.depsgraph_object_instances_num_changed = True
        self.need_update |= (len(self.dg_updated_object_data_names) > 0 or len(self.changed_data_ids) > 0)

    def is_object_data_updated_in_depgraph(self, eval_object):
        eval_object_data = eval_object.data
        if eval_object_data is None:
            return False
        is_editmode = getattr(eval_object_data, "is_editmode", False)
        if is_editmode:
            return True
        if utility.is_reshapable_proxy(eval_object):
            return True
        if utility.is_reshapable_modifiers_applied(eval_object.original):
            return True
        return eval_object_data.name in self.dg_updated_object_data_names or \
            eval_object.original.data.name in self.dg_updated_object_data_names

    @staticmethod
    def cast_light_mask(data):
        property_to_bits = ["light_id_sunlight", "light_id_env", "light_id_pass_1", "light_id_pass_2",
                            "light_id_pass_3", "light_id_pass_4", "light_id_pass_5", "light_id_pass_6",
                            "light_id_pass_7", "light_id_pass_8"]
        value = 0
        for idx, property_name in enumerate(property_to_bits):
            value += (int(getattr(data, property_name)) << idx)
        return value

    def resolve_octane_scatter_id(self, object_name, persistent_id):
        persistent_id_str_key = "_".join([str(pid) for pid in persistent_id])
        if persistent_id_str_key not in self.persistent_id_to_octane_scatter_id_map[object_name]:
            self.persistent_id_to_octane_scatter_id_map[object_name][persistent_id_str_key] = len(
                self.persistent_id_to_octane_scatter_id_map[object_name])
        return self.persistent_id_to_octane_scatter_id_map[object_name][persistent_id_str_key]

    def resolve_octane_id(self, name, node_type, prefix=""):
        return prefix + name + str(node_type)

    def has_octane_node(self, name, node_type, prefix=""):
        octane_node_id = self.resolve_octane_id(name, node_type, prefix)
        return self.has_data(octane_node_id)

    def get_octane_node(self, name, node_type, prefix=""):
        octane_node_id = self.resolve_octane_id(name, node_type, prefix)
        octane_node_name = prefix + name
        if self.has_data(octane_node_id):
            octane_node = self.get_node(octane_node_id)
            octane_node.is_newly_created = False
        else:
            octane_node = self.add_node(octane_node_name, node_type, octane_node_id)
            octane_node.is_newly_created = True
        return octane_node

    def remove_octane_node(self, name, node_type, prefix=""):
        octane_node_id = self.resolve_octane_id(name, node_type, prefix)
        self.remove(octane_node_id)

    def update_mesh_data(self, _depsgraph, origin_object, eval_object, mesh, octane_node, octane_property,
                         need_subdivision=False, motion_time_offset=0):
        use_octane_coordinate = utility.use_octane_coordinate(eval_object)
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
            # Loop triangle polygons
            if hasattr(mesh, "loop_triangle_polygons"):
                loop_triangle_polygons_num = len(mesh.loop_triangle_polygons)
                loop_triangle_polygons_addr = mesh.loop_triangle_polygons[
                    0].as_pointer() if loop_triangle_polygons_num > 0 else 0
            else:
                loop_triangle_polygons_num = 0
                loop_triangle_polygons_addr = 0
            # Loop
            loops_num = len(mesh.loops)
            loops_addr = mesh.loops[0].as_pointer() if loops_num > 0 else 0
            if ".corner_vert" in mesh.attributes:
                corner_verts = list([i.value for i in mesh.attributes[".corner_vert"].data])
            else:
                corner_verts = []
            # Custom normals
            custom_normals = []
            if not need_subdivision and mesh.has_custom_normals:
                custom_normals = [0] * (len(mesh.loops) * 3)
                for loop_tri in mesh.loop_triangles:
                    loops = loop_tri.loops
                    split_normals = loop_tri.split_normals
                    start0 = loops[0] * 3
                    start1 = loops[1] * 3
                    start2 = loops[2] * 3
                    custom_normals[start0:start0 + 3] = split_normals[0][:]
                    custom_normals[start1:start1 + 3] = split_normals[1][:]
                    custom_normals[start2:start2 + 3] = split_normals[2][:]
            # Sharp faces
            sharp_faces_addr = 0
            if "sharp_face" in mesh.attributes:
                sharp_faces_addr = mesh.attributes["sharp_face"].data[0].as_pointer()
            # Polygons
            polygons_num = len(mesh.polygons)
            polygons_addr = mesh.polygons[0].as_pointer() if polygons_num > 0 else 0
            winding_order = int(octane_property.winding_order)
            used_shaders_num = max(1, len(origin_object.data.materials))
            if "material_index" in mesh.attributes:
                material_indices = list([i.value for i in mesh.attributes["material_index"].data])
            else:
                material_indices = [0] * polygons_num
            # UV Data
            uv_data = []
            active_uv_layer_index = -1
            if mesh.uv_layers:
                for idx, uv in enumerate(mesh.uv_layers):
                    if uv.name in mesh.attributes:
                        uv_attr_data = mesh.attributes[uv.name].data
                        uv_data.append(uv_attr_data[0].as_pointer() if len(uv_attr_data) > 0 else 0)
                    else:
                        uv_data.append(uv.data[0].as_pointer() if len(uv.data) > 0 else 0)
                    if uv.active_render:
                        active_uv_layer_index = idx
            # Float attributes
            float_attribute_data_list = []
            float_attribute_weight_list = []
            available_float_vertex_sets_num = self.MAX_OCTANE_FLOAT_VERTEX_SETS
            group_index_to_float_vertex_index = {}
            for idx, vertex_group in enumerate(eval_object.vertex_groups):
                if available_float_vertex_sets_num == 1:
                    if eval_object.vertex_groups.active_index != idx:
                        continue
                elif available_float_vertex_sets_num == 0:
                    continue
                float_attribute_name = vertex_group.name
                float_array = array.array("f", [0] * vertices_num)
                float_attribute_weight_list.append(float_array)
                float_attribute_data_list.append([float_attribute_name, float_array])
                group_index_to_float_vertex_index[idx] = len(float_attribute_data_list) - 1
                available_float_vertex_sets_num -= 1
            for vertex_idx, v in enumerate(mesh.vertices):
                if len(v.groups) == 0:
                    continue
                else:
                    for g in v.groups:
                        idx = group_index_to_float_vertex_index.get(g.group, None)
                        if idx is not None:
                            float_attribute_weight_list[idx][vertex_idx] = g.weight
            # Color attributes
            color_attribute_data_list = []
            available_color_vertex_sets_num = self.MAX_OCTANE_COLOR_VERTEX_SETS
            # Always sync the active color attribute if there is one
            if mesh.color_attributes.active_color_index != -1:
                available_color_vertex_sets_num -= 1
            for idx, color_attribute in enumerate(mesh.color_attributes):
                if mesh.color_attributes.active_color_index == idx or available_color_vertex_sets_num > 0:
                    color_attribute_data_list.append(
                        [color_attribute.data[0].as_pointer(), color_attribute.name, color_attribute.data_type])
                    available_color_vertex_sets_num -= 1
            # Sphere attributes
            sphere_attribute_data = [
                octane_property.octane_enable_sphere_attribute,
                max(0.00001, octane_property.octane_sphere_radius),
                octane_property.octane_use_randomized_radius,
                octane_property.octane_sphere_randomized_radius_seed,
                max(0.00001, octane_property.octane_sphere_randomized_radius_min),
                octane_property.octane_sphere_randomized_radius_max
            ]
            show_mesh_data = (
                    not octane_property.octane_enable_sphere_attribute or not octane_property.octane_hide_original_mesh)
            octane_node.node.set_mesh_attribute(vertices_addr, vertices_num,
                                                normals_addr, normals_num,
                                                loop_triangles_addr, loop_triangles_num,
                                                loop_triangle_polygons_addr, loop_triangle_polygons_num,
                                                loops_addr, loops_num, sharp_faces_addr, corner_verts, custom_normals,
                                                polygons_addr, polygons_num,
                                                used_shaders_num, material_indices,
                                                sphere_attribute_data,
                                                float_attribute_data_list,
                                                color_attribute_data_list,
                                                active_uv_layer_index, uv_data,
                                                mesh.auto_smooth_angle / math.pi * 180.0,
                                                use_octane_coordinate, show_mesh_data, need_subdivision, winding_order)
            # Octane Subdivision
            if octane_property.open_subd_enable:
                octane_node.set_attribute_id(consts.AttributeID.A_SUBD_LEVEL, octane_property.open_subd_level)
                octane_node.set_attribute_id(consts.AttributeID.A_SUBD_SHARPNESS, octane_property.open_subd_sharpness)
                octane_node.set_attribute_id(consts.AttributeID.A_SUBD_BOUND_INTERP,
                                             utility.get_enum_int_value(octane_property,
                                                                        "octane.open_subd_bound_interp", 0))
                octane_node.set_attribute_id(consts.AttributeID.A_SUBD_SCHEME,
                                             utility.get_enum_int_value(octane_property,
                                                                        "octane.octane.open_subd_scheme", 0))
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_SUBD_LEVEL, 0)
        else:
            octane_node.node.set_mesh_motion_attribute(vertices_addr, vertices_num, motion_time_offset,
                                                       use_octane_coordinate)

    def update_hair_data(self, depsgraph, origin_object, eval_object, mesh, octane_node, _octane_property,
                         motion_time_offset=0):
        # Hair Data
        has_hair_data = False
        is_viewport = depsgraph.mode == "VIEWPORT"
        inverted_matrix_world = eval_object.matrix_world.copy()
        inverted_matrix_world.invert_safe()
        if is_viewport:
            show_mesh_data = origin_object.show_instancer_for_viewport
        else:
            show_mesh_data = origin_object.show_instancer_for_render
        hair_vertex_data = []
        hair_uv_data = []
        hair_vertex_per_strand = []
        hair_material_index_configs = []
        hair_min_curvature_configs = []
        hair_width_configs = []
        hair_w_configs = []
        for psys in eval_object.particle_systems:
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
            for particle_system in eval_object.particle_systems:
                settings = particle_system.settings
                vertex_data = []
                particle_start_index = 0
                strand_num = 0
                particle_child_num = 0
                vertex_per_strand = 0
                shader_index = 0
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
                    if settings.child_type != "None" and particle_child_num != 0:
                        particle_start_index = particle_num
                    co_hair = particle_system.co_hair
                    vertex_data = np.fromiter((elem
                                               for particle_index in range(particle_start_index, strand_num)
                                               for step in range(vertex_per_strand)
                                               for elem in
                                               co_hair(object=eval_object, particle_no=particle_index, step=step)),
                                              dtype=np.float32,
                                              count=(strand_num - particle_start_index) * vertex_per_strand * 3)
                uv_data = []
                if len(vertex_data) > 0:
                    particle_system_mod = None
                    for mod in eval_object.modifiers:
                        if mod.type == "PARTICLE_SYSTEM" and mod.particle_system.name == particle_system.name:
                            particle_system_mod = mod
                            break
                    if particle_system_mod is not None and active_uv_index != -1:
                        uv_on_emitter = particle_system.uv_on_emitter
                        uv_data = np.fromiter((elem for particle_index in range(particle_start_index, strand_num)
                                               for elem in uv_on_emitter(particle_system_mod,
                                                                         particle=particle_system.particles[
                                                                             particle_index]
                                                                         if particle_child_num == 0 else
                                                                         particle_system.particles[0],
                                                                         particle_no=particle_index,
                                                                         uv_no=active_uv_index)),
                                              dtype=np.float32, count=(strand_num - particle_start_index) * 2)
                if len(vertex_data) > 0:
                    hair_vertex_data.append(vertex_data)
                    hair_uv_data.append(uv_data)
                    hair_vertex_per_strand.append(vertex_per_strand)
                    hair_material_index_configs.append(shader_index)
                    hair_min_curvature_configs.append(settings.octane.min_curvature)
                    hair_width_configs.append([settings.octane.root_width, settings.octane.tip_width])
                    hair_w_configs.append([settings.octane.w_min, settings.octane.w_max])
        octane_node.node.set_hair_attribute(inverted_matrix_world, hair_vertex_data, hair_uv_data,
                                            hair_vertex_per_strand, hair_material_index_configs,
                                            hair_min_curvature_configs, hair_width_configs, hair_w_configs,
                                            show_mesh_data, motion_time_offset)

    def update_curve_data(self, depsgraph, _eval_object, curve, octane_node, octane_property, motion_time_offset=0):
        if len(curve.splines):
            root_thickness = octane_property.hair_root_width
            tip_thickness = octane_property.hair_tip_width
            points_data = curve_utils.calculate_points_on_curve(curve, depsgraph.mode == "VIEWPORT")
            thickness_data = []
            vertex_num_per_hair_data = []
            material_index_data = []
            for idx, spline_points_data in enumerate(points_data):
                cur_spline = curve.splines[idx]
                thickness_data.append([root_thickness, tip_thickness])
                vertex_num_per_hair_data.append(int(len(spline_points_data) / 3))
                material_index_data.append(cur_spline.material_index)
            octane_node.node.set_curve_attribute(points_data, vertex_num_per_hair_data, material_index_data,
                                                 thickness_data, motion_time_offset)

    def update_curves_data(self, _depsgraph, eval_object, octane_node, octane_property, motion_time_offset=0):
        curve_data = eval_object.data
        keys_num = len(curve_data.points)
        curves_num = len(curve_data.curves)
        use_octane_radius_setting = octane_property.use_octane_radius_setting
        octane_root_radius = octane_property.hair_root_width
        octane_tip_radius = octane_property.hair_tip_width
        width_configs = [use_octane_radius_setting, octane_root_radius, octane_tip_radius]
        position_addr = 0
        radius_addr = 0
        uv_addr = 0
        curve_offset_data_addr = 0
        position_num = 0
        radius_num = 0
        uv_num = 0
        curve_offset_data_num = 0
        if "position" in curve_data.attributes and len(curve_data.attributes["position"].data):
            position_addr = curve_data.attributes["position"].data[0].as_pointer()
            position_num = len(curve_data.attributes["position"].data)
        if "radius" in curve_data.attributes and len(curve_data.attributes["radius"].data):
            radius_addr = curve_data.attributes["radius"].data[0].as_pointer()
            radius_num = len(curve_data.attributes["radius"].data)
        if "surface_uv_coordinate" in curve_data.attributes and len(
                curve_data.attributes["surface_uv_coordinate"].data):
            uv_addr = curve_data.attributes["surface_uv_coordinate"].data[0].as_pointer()
            uv_num = len(curve_data.attributes["surface_uv_coordinate"].data)
        if len(curve_data.curve_offset_data):
            curve_offset_data_addr = curve_data.curve_offset_data[0].as_pointer()
            curve_offset_data_num = len(curve_data.curve_offset_data)
        octane_node.node.set_curves_attribute(keys_num, curves_num, position_addr, position_num, radius_addr,
                                              radius_num, uv_addr, uv_num, curve_offset_data_addr,
                                              curve_offset_data_num, width_configs, motion_time_offset)

    def need_subdivision(self, _object, octane_property):
        origin_object = _object.original
        need_subdivision = octane_property.open_subd_enable
        # Check the vertex displacement setting
        if not need_subdivision:
            for mat_slot in origin_object.material_slots:
                mat = mat_slot.material
                if mat is not None and mat.use_nodes:
                    if self.session.material_cache.need_subdivision(mat):
                        need_subdivision = True
                        break
        return need_subdivision

    def update_geometry_data(self, depsgraph, eval_object, octane_node, octane_property, motion_time_offset=0):
        # Is resource cached? If so, do not generate the mesh data.
        is_mesh_data_updated = True
        if not utility.is_reshapable_proxy(eval_object):
            is_newly_created = getattr(octane_node, "is_newly_created", False)
            if is_newly_created:
                is_mesh_data_updated = not ResourceCache().is_mesh_node_cached(getattr(eval_object.data, "name", ""),
                                                                               octane_node.name)
        octane_node.set_attribute_blender_name(self.BLENDER_ATTRIBUTE_MESH_DATA_UPDATE, consts.AttributeType.AT_BOOL,
                                               is_mesh_data_updated)
        if not is_mesh_data_updated:
            return
        origin_object = eval_object.original
        if eval_object.type == "CURVE":
            curve_data = eval_object.data
            octane_data = curve_data.octane
            if octane_data.render_curve_as_octane_hair:
                curve = None
                if eval_object:
                    curve = eval_object.to_curve(depsgraph, apply_modifiers=True)
                if curve is None:
                    if eval_object:
                        eval_object.to_curve_clear()
                # Curve Data
                self.update_curve_data(depsgraph, eval_object, curve, octane_node, octane_property, motion_time_offset)
                # Clear Mesh
                if eval_object and curve:
                    eval_object.to_curve_clear()
        elif eval_object.type == "CURVES":
            # Curves Data
            self.update_curves_data(depsgraph, eval_object, octane_node, octane_property, motion_time_offset)
        elif eval_object.type in ("MESH", "META"):
            mesh = None
            need_subdivision = self.need_subdivision(origin_object, octane_property)
            if eval_object:
                mesh = eval_object.to_mesh()
                if mesh and not need_subdivision:
                    if mesh.use_auto_smooth:
                        # if not mesh.has_custom_normals:
                        #     mesh.calc_normals()
                        mesh.split_faces()
                    mesh.calc_loop_triangles()
                    if mesh.has_custom_normals:
                        mesh.calc_normals_split()
            if mesh is None:
                if eval_object:
                    eval_object.to_mesh_clear()
                return
            # Mesh Data
            self.update_mesh_data(depsgraph, origin_object, eval_object, mesh, octane_node, octane_property,
                                  need_subdivision, motion_time_offset)
            # Hair Data
            self.update_hair_data(depsgraph, origin_object, eval_object, mesh, octane_node, octane_property,
                                  motion_time_offset)
            # Clear Mesh
            if eval_object and mesh:
                eval_object.to_mesh_clear()

    def update_mesh(self, object_data_name, depsgraph, eval_object, octane_property, octane_material_tag,
                    need_full_update, motion_time_offset=0, update_now=True):
        if not need_full_update:
            return
        octane_node = self.get_octane_node(object_data_name, consts.NodeType.NT_GEO_MESH)
        # Materials
        octane_node.set_attribute_blender_name("SHADER_NAMES", consts.AttributeType.AT_STRING, octane_material_tag)
        # Objects
        octane_node.set_attribute_blender_name("OBJECT_NAMES", consts.AttributeType.AT_STRING, "__" + octane_node.name)
        # Geometry Data
        self.update_geometry_data(depsgraph, eval_object, octane_node, octane_property, motion_time_offset)
        if octane_node.need_update:
            octane_node.update_to_engine(update_now)

    def update_infinite_plane(self, _depsgraph, name, octane_material_tag, need_full_update, update_now):
        if not need_full_update:
            return
        node = self.get_octane_node(name, consts.NodeType.NT_GEO_PLANE)
        material_name = ObjectMaterialTagManager.resolve_first_material_octane_name(octane_material_tag)
        node.set_pin_id(consts.PinID.P_GROUND_COLOR, True, material_name, "")
        node.update_to_engine(update_now)

    def update_octane_orbx_proxy(self, name, filepath, enable_time_transform, time_transform_delay,
                                 time_transform_scale, need_full_update):
        from octane.core.octane_node import OctaneNode
        orbx_proxy_node = OctaneNode(name, consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE)
        if need_full_update:
            orbx_proxy_node.node.set_orbx_proxy_attributes(filepath, False, enable_time_transform, time_transform_delay,
                                                           time_transform_scale)
            orbx_proxy_node.update_to_engine(True)
            content = orbx_proxy_node.node.get_response()
            use_objectlayer = True
            if len(content):
                content_et = ElementTree.fromstring(content)
                use_objectlayer = content_et.get("useObjectLayer") == "true" if content_et is not None else False
            orbx_proxy_node.use_objectlayer = use_objectlayer
            return use_objectlayer
        else:
            return getattr(orbx_proxy_node, "use_objectlayer", False)

    def update_volume(self, object_data_name, _depsgraph, eval_object, octane_property, octane_material_tag,
                      need_full_update, update_now):
        if not need_full_update:
            return
        if octane_property.vdb_sdf:
            octane_node = self.get_octane_node(object_data_name, consts.NodeType.NT_GEO_VOLUME_SDF)
        else:
            octane_node = self.get_octane_node(object_data_name, consts.NodeType.NT_GEO_VOLUME)
        # Material
        material_name = ObjectMaterialTagManager.resolve_first_material_octane_name(octane_material_tag)
        if octane_node.node_type == consts.NodeType.NT_GEO_VOLUME:
            material_pin_id = consts.PinID.P_MEDIUM
        else:
            material_pin_id = consts.PinID.P_MATERIAL1
        octane_node.set_pin_id(material_pin_id, True, material_name, "")
        eval_object_blender_id = BlenderID(eval_object)
        if eval_object.type == "MESH":
            domain_modifier = utility.find_smoke_domain_modifier(eval_object)
            if domain_modifier is not None:
                domain_settings = domain_modifier.domain_settings
                amplify = domain_settings.noise_scale if domain_settings.use_noise else 1
                resolution = [res * amplify for res in domain_settings.domain_resolution]
                width, height, depth = resolution[0], resolution[1], resolution[2]
                resolution_num = width * height * depth
                if resolution_num > 0:
                    density_grid = array.array("f", domain_settings.density_grid)
                    flame_grid = array.array("f", domain_settings.flame_grid)
                    velocity_grid = array.array("f", domain_settings.velocity_grid)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_RESOLUTION, resolution)
                    bound_box = eval_object.bound_box
                    x_min = min([p[0] for p in bound_box])
                    y_min = min([p[1] for p in bound_box])
                    z_min = min([p[2] for p in bound_box])
                    x_max = max([p[0] for p in bound_box])
                    y_max = max([p[1] for p in bound_box])
                    z_max = max([p[2] for p in bound_box])
                    matrix = mathutils.Matrix(
                        [[(x_max - x_min) / width, 0, 0, x_min], [0, (y_max - y_min) / height, 0, y_min],
                         [0, 0, (z_max - z_min) / depth, z_min], [0, 0, 0, 1]])
                    # It's weird, but I cannot find the A_TRANSFORM in the NT_GEO_VOLUME
                    # octane_node.set_attribute_id(consts.AttributeID.A_TRANSFORM, matrix)
                    octane_node.node.set_attribute(consts.OctaneDataBlockSymbolType.ATTRIBUTE_NAME,
                                                   consts.AttributeID.A_TRANSFORM, "transform",
                                                   consts.AttributeType.AT_MATRIX, matrix, 1)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_MOTION_BLUR_ENABLED, True)
                    octane_node.node.set_volume_grid_attribute(resolution, density_grid, flame_grid, velocity_grid)
        elif eval_object.type == "VOLUME":
            volume_data = eval_object.data
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ISOVALUE, octane_property.vdb_iso)
            octane_node.set_attribute_id(consts.AttributeID.A_GEOIMP_SCALE_UNIT,
                                         utility.get_enum_int_value(octane_property, "vdb_import_scale", 4))
            octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_MOTION_BLUR_ENABLED,
                                         octane_property.vdb_motion_blur_enabled)
            # Update auto refresh attribute
            if volume_data.is_sequence:
                self.auto_refresh_data_ids[eval_object_blender_id] = consts.AutoRefreshStrategy.FRAME_CHANGE
            else:
                if eval_object_blender_id in self.auto_refresh_data_ids:
                    self.auto_refresh_data_ids.remove(eval_object_blender_id)
            if not volume_data.grids.is_loaded:
                volume_data.grids.load()
            filepath = bpy.path.abspath(volume_data.grids.frame_filepath)
            active_grid_name = ""
            if volume_data.grids.is_loaded and len(volume_data.grids):
                active_grid_name = volume_data.grids[volume_data.grids.active_index].name
            if len(filepath) == 0:
                tempdir = bpy.app.tempdir
                filepath = os.path.join(tempdir, eval_object.name + ".vdb")
                volume_data.grids.save(filepath)
                octane_node.node.set_volume_file_attribute(filepath, True, active_grid_name)
            else:
                octane_node.set_attribute_id(consts.AttributeID.A_FILENAME, filepath)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_SCALE,
                                             octane_property.vdb_abs_scale)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_SCALE,
                                             octane_property.vdb_emiss_scale)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_SCALE,
                                             octane_property.vdb_scatter_scale)
                octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_SCALE, octane_property.vdb_vel_scale)
                if octane_property.vdb_velocity_grid_type == "Vector grid":
                    if len(octane_property.vdb_vector_grid_id) > 0:
                        octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID,
                                                     octane_property.vdb_vector_grid_id)
                    else:
                        octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID, active_grid_name)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_X, "")
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Y, "")
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Z, "")
                else:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_X,
                                                 octane_property.vdb_x_components_grid_id)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Y,
                                                 octane_property.vdb_y_components_grid_id)
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_VELOCITY_ID_Z,
                                                 octane_property.vdb_z_components_grid_id)
                if len(octane_property.vdb_absorption_grid_id) > 0:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_ID,
                                                 octane_property.vdb_absorption_grid_id)
                else:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_ABSORPTION_ID, active_grid_name)
                if len(octane_property.vdb_scattering_grid_id) > 0:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_ID,
                                                 octane_property.vdb_scattering_grid_id)
                else:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_SCATTER_ID, active_grid_name)
                if len(octane_property.vdb_emission_grid_id) > 0:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_ID,
                                                 octane_property.vdb_emission_grid_id)
                else:
                    octane_node.set_attribute_id(consts.AttributeID.A_VOLUME_EMISSION_ID, active_grid_name)
            if octane_node.need_update:
                octane_node.set_attribute_id(consts.AttributeID.A_RELOAD, True)
        if octane_node and octane_node.need_update:
            octane_node.update_to_engine(update_now)

    def update_light(self, object_data_name, scatter_node_name, depsgraph, eval_object, octane_property,
                     need_full_update, update_now):
        scene = depsgraph.scene
        is_viewport = depsgraph.mode == "VIEWPORT"
        light = eval_object.data
        linked_name = ""
        linked_light_name = ""
        # Quick update about the linked geometry
        if light.use_nodes:
            node_tree = light.node_tree
            owner_type = utility.get_node_tree_owner_type(light)
            active_output_node = utility.find_active_output_node(node_tree, owner_type)
            if active_output_node and len(active_output_node.inputs):
                linked_light_name = utility.get_octane_name_for_root_node(active_output_node, "Surface", light)
                linked_name = linked_light_name
        if light.type == "POINT" and octane_property.octane_point_light_type == "Sphere":
            sphere_light_name = object_data_name + "[SphereLight]"
            linked_name = sphere_light_name
        elif light.type == "AREA":
            if octane_property.used_as_octane_mesh_light:
                material_map_name = octane_name.resolve_material_map_octane_name(scatter_node_name)
                linked_name = material_map_name
            else:
                area_light_geo_name = object_data_name + "[AreaLightGeo]"
                linked_name = area_light_geo_name
        if not need_full_update:
            return linked_name
        # Full update
        if light.type == "POINT" and octane_property.octane_point_light_type == "Sphere":
            sphere_light_name = linked_name
            sphere_light_node = self.get_octane_node(sphere_light_name, consts.NodeType.NT_LIGHT_SPHERE)
            sphere_light_node.set_pin_id(consts.PinID.P_RADIUS, False, "", light.shadow_soft_size)
            sphere_light_node.set_pin_id(consts.PinID.P_MATERIAL1, True, linked_light_name, "")
            sphere_light_node.update_to_engine(update_now)
        elif light.type == "AREA":
            if octane_property.used_as_octane_mesh_light:
                material_map_name = linked_name
                material_map_node = self.get_octane_node(material_map_name, consts.NodeType.NT_MAT_MAP)
                material_map_node_material_pin_num = 1
                if octane_property.use_external_mesh:
                    external_mesh_file = octane_property.external_mesh_file
                    external_mesh_file = bpy.path.abspath(external_mesh_file)
                    mesh_light_name = ""
                    if len(external_mesh_file) > 0:
                        mesh_light_name = object_data_name + "[MeshLight]"
                        mesh_light_node = self.get_octane_node(mesh_light_name, consts.NodeType.NT_GEO_MESH)
                        mesh_light_node.set_attribute_id(consts.AttributeID.A_FILENAME, external_mesh_file)
                        mesh_light_node.update_to_engine(update_now)
                    material_map_node.set_pin_id(consts.PinID.P_GEOMETRY, len(mesh_light_name) > 0, mesh_light_name, "")
                    material_map_node.update_to_engine(update_now)
                    material_map_node_info = utility.fetch_node_info(material_map_name)
                    if material_map_node_info is not None:
                        material_map_node_material_pin_num = material_map_node_info["dynPinCount"]
                else:
                    light_mesh_name = ""
                    light_mesh_object = octane_property.light_mesh_object
                    if light_mesh_object is not None and light_mesh_object.type == "MESH":
                        light_mesh_name = octane_name.resolve_object_data_octane_name(light_mesh_object, scene,
                                                                                      is_viewport)
                        material_map_node_material_pin_num = max(material_map_node_material_pin_num,
                                                                 len(light_mesh_object.material_slots))
                    material_map_node.set_pin_id(consts.PinID.P_GEOMETRY, len(light_mesh_name) > 0, light_mesh_name, "")
                for idx in range(material_map_node_material_pin_num):
                    material_map_node.set_pin_index(idx + 1, "Material" + str(idx), consts.SocketType.ST_LINK,
                                                    consts.PinType.PT_MATERIAL, 0, True, linked_light_name, "")
                material_map_node.update_to_engine(update_now)
            else:
                area_light_geo_name = linked_name
                need_init = not self.has_octane_node(area_light_geo_name, consts.NodeType.NT_GEO_OBJECT)
                geo_object_node = self.get_octane_node(area_light_geo_name, consts.NodeType.NT_GEO_OBJECT)
                if need_init:
                    # Force Init
                    geo_object_node.set_pin_id(consts.PinID.P_PRIMITIVE, False, "", 0)
                    geo_object_node.update_to_engine(True)
                transform_node_name = area_light_geo_name + "[Transform]"
                _3d_transform_node = self.get_octane_node(transform_node_name, consts.NodeType.NT_TRANSFORM_3D)
                primitive_type = 0
                rotation = [0, 0, 0]
                scale = [1, 1, 1]
                if light.shape == "DISK":
                    primitive_type = 6  # ("Disc", "Disc", "", 6),
                    rotation = [-90, 0, 0]
                    scale = [light.size, 1, light.size]
                elif light.shape == "ELLIPSE":
                    primitive_type = 6  # ("Disc", "Disc", "", 6),
                    rotation = [-90, 0, 0]
                    scale = [light.size, 1, light.size_y]
                elif light.shape == "RECTANGLE":
                    primitive_type = 18  # ("Quad", "Quad", "", 18),
                    rotation = [0, 180, 0]
                    scale = [light.size, light.size_y, 1]
                elif light.shape == "SQUARE":
                    primitive_type = 18  # ("Quad", "Quad", "", 18),
                    rotation = [0, 180, 0]
                    scale = [light.size, light.size, 1]
                geo_object_node.set_pin_id(consts.PinID.P_PRIMITIVE, False, "", primitive_type)
                geo_object_node.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, transform_node_name)
                geo_object_node.set_pin_id(consts.PinID.P_MATERIAL, True, linked_light_name, linked_light_name)
                _3d_transform_node.set_pin_id(consts.PinID.P_ROTATION, False, "", rotation)
                _3d_transform_node.set_pin_id(consts.PinID.P_SCALE, False, "", scale)
                if geo_object_node.need_update:
                    geo_object_node.update_to_engine(update_now)
                if _3d_transform_node.need_update:
                    _3d_transform_node.update_to_engine(update_now)
        return linked_name

    def update_object_layer(self, node, octane_data):
        if octane_data.__class__.__name__ != "OctaneObjectSettings":
            return
        node.set_pin_id(consts.PinID.P_LAYER_ID, False, "", octane_data.render_layer_id)
        node.set_pin_id(consts.PinID.P_GENERAL_VISIBILITY, False, "", octane_data.general_visibility)
        node.set_pin_id(consts.PinID.P_CAMERA_VISIBILITY, False, "", octane_data.camera_visibility)
        node.set_pin_id(consts.PinID.P_SHADOW_VISIBILITY, False, "", octane_data.shadow_visibility)
        node.set_pin_id(consts.PinID.P_DIRT_VISIBILITY, False, "", octane_data.dirt_visibility)
        node.set_pin_id(consts.PinID.P_CURVATURE_VISIBILITY, False, "", octane_data.curvature_visibility)
        node.set_pin_id(consts.PinID.P_RANDOM_SEED, False, "", octane_data.random_color_seed)
        node.set_pin_id(consts.PinID.P_OBJECT_COLOR, False, "", [int(c * 255.0) for c in octane_data.color])
        node.set_pin_id(consts.PinID.P_CUSTOM_AOV, False, "",
                        utility.get_enum_int_value(octane_data, "custom_aov", 4096))
        node.set_pin_id(consts.PinID.P_CUSTOM_AOV_CHANNEL, False, "",
                        utility.get_enum_int_value(octane_data, "custom_aov_channel", 0))
        node.set_pin_id(consts.PinID.P_BAKING_GROUP_ID, False, "", octane_data.baking_group_id)
        # Baking Transform
        transform_node_name = node.name + "[Transform]"
        _2d_transform_node = node.get_subnode(transform_node_name, consts.NodeType.NT_TRANSFORM_2D)
        _2d_transform_node.set_pin_id(consts.PinID.P_ROTATION, False, "", octane_data.baking_uv_transform_rz)
        _2d_transform_node.set_pin_id(consts.PinID.P_SCALE, False, "",
                                      (octane_data.baking_uv_transform_sx, octane_data.baking_uv_transform_sy))
        _2d_transform_node.set_pin_id(consts.PinID.P_TRANSLATION, False, "",
                                      (octane_data.baking_uv_transform_tx, octane_data.baking_uv_transform_ty))
        node.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, "")
        # Light ID Mask
        mask_value = 0
        for idx, property_name in enumerate(("light_id_sunlight", "light_id_env", "light_id_pass_1", "light_id_pass_2",
                                             "light_id_pass_3", "light_id_pass_4", "light_id_pass_5", "light_id_pass_6",
                                             "light_id_pass_7", "light_id_pass_8")):
            mask_value += (int(getattr(octane_data, property_name)) << idx)
        pin_info = OctaneInfoManger().get_pin_info_by_id(node.node_type, consts.PinID.P_LIGHT_PASS_MASK)
        node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, pin_info.index, pin_info.name,
                          consts.SocketType.ST_INT, pin_info.pin_type, pin_info.default_node_type, False, "",
                          mask_value)

    def update_object(self, scene, depsgraph, eval_object, octane_scatter_node, update_now):
        # General
        is_viewport = depsgraph.mode == "VIEWPORT"
        object_name = octane_name.resolve_object_octane_name(eval_object, scene, is_viewport)
        object_data_name = octane_name.resolve_object_data_octane_name(eval_object, scene, is_viewport)
        objectlayer_name = octane_name.resolve_objectlayer_octane_name(octane_scatter_node.name)
        objectlayer_map_name = octane_name.resolve_objectlayer_map_octane_name(octane_scatter_node.name)
        objectlayer_map_linked_mesh_name = object_data_name
        use_objectlayer = True
        octane_objectlayer_node = self.get_octane_node(objectlayer_name, consts.NodeType.NT_OBJECTLAYER)
        octane_objectlayer_map_node = self.get_octane_node(objectlayer_map_name, consts.NodeType.NT_OBJECTLAYER_MAP)
        use_multiple_objectlayers = False
        origin_object = eval_object.original
        object_octane_property = getattr(origin_object, "octane", None)
        object_data_octane_property = getattr(origin_object.data, "octane", None)
        self.update_object_layer(octane_objectlayer_node, object_octane_property)
        if octane_objectlayer_node.need_update:
            octane_objectlayer_node.update_to_engine(update_now)
        # Is the object data updated in the depgraph?
        # If so, make a full update of the object data
        need_update_object_data = need_full_update_object_data = self.is_object_data_updated_in_depgraph(eval_object)
        # Is the object data synced in this view_update?
        # If so, we don't need a full update this time
        if object_data_name in self.oct_synced_object_data_octane_names:
            need_full_update_object_data = False
            # If the scatter node is newly-created, make a "partial" update of the object data by force (to ensure the
            # linked_geometry_name is valid)
        need_update_object_data |= getattr(octane_scatter_node, "is_newly_created", False)
        if not need_update_object_data:
            return None
        # Update Object Data
        # Material tags
        _, octane_material_tag = self.object_material_tag_manager.update_tag(self.session.material_cache, origin_object)
        self.session.set_status_msg(
            "Uploading and evaluating object[%s] and data[%s] in Octane..." % (object_name, object_data_name),
            update_now)
        if eval_object.type == "MESH":
            # Mesh Data
            is_infinite_plane = getattr(object_data_octane_property, "infinite_plane", "")
            imported_orbx_file_path = getattr(object_data_octane_property, "imported_orbx_file_path", "")
            geometry_node_data = object_data_octane_property.octane_geo_node_collections
            domain_modifier = utility.find_smoke_domain_modifier(eval_object)
            if is_infinite_plane:
                # Infinite plane
                self.update_infinite_plane(depsgraph, object_data_name, octane_material_tag,
                                           need_full_update_object_data, update_now)
            elif len(imported_orbx_file_path):
                # Orbx graph
                object_data_name = bpy.path.basename(imported_orbx_file_path)
                enable_time_transform = getattr(object_data_octane_property, "enable_animation_time_transformation",
                                                False)
                time_transform_delay = getattr(object_data_octane_property, "animation_time_transformation_delay", 0.0)
                time_transform_scale = getattr(object_data_octane_property, "animation_time_transformation_scale", 0.0)
                use_objectlayer = self.update_octane_orbx_proxy(object_data_name, imported_orbx_file_path,
                                                                enable_time_transform, time_transform_delay,
                                                                time_transform_scale, need_full_update_object_data)
                objectlayer_map_linked_mesh_name = object_data_name
                use_multiple_objectlayers = True
            elif geometry_node_data.is_octane_geo_used():
                # OSL Geometry or Surface/Volume Scatter
                objectlayer_map_linked_mesh_name = object_data_name
            elif domain_modifier is not None and not domain_modifier.domain_settings.use_mesh:
                # Octane Volume
                self.update_volume(object_data_name, depsgraph, eval_object, object_data_octane_property,
                                   octane_material_tag, need_full_update_object_data, update_now)
            else:
                # Octane Mesh
                self.update_mesh(object_data_name, depsgraph, eval_object, object_data_octane_property,
                                 octane_material_tag, need_full_update_object_data, 0, update_now)
        elif eval_object.type == "META":
            self.update_mesh(object_data_name, depsgraph, eval_object, object_data_octane_property, octane_material_tag,
                             need_full_update_object_data, 0, update_now)
        elif eval_object.type == "CURVE":
            self.update_mesh(object_data_name, depsgraph, eval_object, object_data_octane_property, octane_material_tag,
                             need_full_update_object_data, 0, update_now)
        elif eval_object.type == "CURVES":
            self.update_mesh(object_data_name, depsgraph, eval_object, object_data_octane_property, octane_material_tag,
                             need_full_update_object_data, 0, update_now)
        elif eval_object.type == "VOLUME":
            self.update_volume(object_data_name, depsgraph, eval_object, object_data_octane_property,
                               octane_material_tag, need_full_update_object_data, update_now)
        elif eval_object.type == "LIGHT":
            objectlayer_map_linked_mesh_name = self.update_light(object_data_name, octane_scatter_node.name, depsgraph,
                                                                 eval_object, object_data_octane_property,
                                                                 need_full_update_object_data, update_now)
        elif eval_object.type == "EMPTY":
            object_data_name = ""
            use_objectlayer = False
        # Update Object Layers
        if use_objectlayer:
            octane_objectlayer_map_node.set_pin_id(consts.PinID.P_GEOMETRY, True, objectlayer_map_linked_mesh_name, "")
            # Update the nodes to the engine
            if octane_objectlayer_map_node.need_update:
                octane_objectlayer_map_node.update_to_engine(update_now)
            if octane_objectlayer_node.need_update:
                octane_objectlayer_node.update_to_engine(update_now)
            objectlayer_map_node_object_layer_num = 1
            if use_multiple_objectlayers:
                objectlayer_map_node_info = utility.fetch_node_info(objectlayer_map_name)
                if objectlayer_map_node_info is not None:
                    objectlayer_map_node_object_layer_num = objectlayer_map_node_info["dynPinCount"]
            for idx in range(objectlayer_map_node_object_layer_num):
                octane_objectlayer_node.link_to(objectlayer_map_name, idx + 1, update_now)
        linked_geometry_name = objectlayer_map_name if use_objectlayer else object_data_name
        octane_scatter_node.linked_geometry_name = linked_geometry_name
        self.oct_synced_object_data_octane_names.add(object_data_name)
        return linked_geometry_name

    def custom_update(self, depsgraph, scene, view_layer, context=None, update_now=True):
        is_viewport = depsgraph.mode == "VIEWPORT"
        current_object_instance_names = set()
        scatter_map = {}
        updated_object_data_map = set()
        to_remove_octane_scatter_node_names = copy.deepcopy(self.synced_octane_scatter_node_names)
        updated_motion_blur_node_names = set()
        for instance_object in depsgraph.object_instances:
            eval_object = instance_object.object
            if context and context.space_data:
                show_in_viewport = eval_object.visible_in_viewport_get(context.space_data)
            else:
                show_in_viewport = True
            if not show_in_viewport:
                continue
            is_instance = instance_object.is_instance
            eval_object_name = eval_object.name
            eval_object_blender_id = BlenderID(eval_object) if not is_instance else BlenderID(
                instance_object.parent.evaluated_get(depsgraph))
            eval_object_data_name = getattr(eval_object.data, "name", "")
            current_object_instance_names.add(eval_object_name)
            scatter_name = octane_name.resolve_scatter_octane_name(instance_object, scene, is_viewport)
            if scatter_name in to_remove_octane_scatter_node_names:
                to_remove_octane_scatter_node_names.remove(scatter_name)
            need_sync = False
            # Optimizations for viewport rendering
            # For viewport rendering, we do some pre-checks to get better performance
            if is_viewport:
                # Is this object a depgraph update?
                need_sync |= eval_object_blender_id in self.changed_data_ids
                # Is this object's data a depgraph update?
                need_sync |= eval_object_data_name in self.dg_updated_object_data_names
                # Is this object newly-created? 
                need_sync |= eval_object_name not in self.depsgraph_object_instance_names
                if not need_sync:
                    continue
            if scatter_name not in scatter_map:
                scatter_map[scatter_name] = self.get_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER)
                scatter_map[scatter_name].node.reset()
            octane_scatter_node = scatter_map[scatter_name]
            # Update object data
            if scatter_name not in updated_object_data_map:
                updated_object_data_map.add(scatter_name)
                self.update_object(scene, depsgraph, eval_object, octane_scatter_node, update_now)
            octane_scatter_node.object_name = eval_object_name
            octane_scatter_id = self.resolve_octane_scatter_id(eval_object_name, instance_object.persistent_id)
            # we have to make a copy here, otherwise we get an identity matrix when passing to C++
            object_matrix = instance_object.matrix_world.copy()
            use_octane_coordinate = utility.use_octane_coordinate(eval_object)
            octane_scatter_node.node.set_instance(octane_scatter_id, octane_scatter_id, object_matrix,
                                                  use_octane_coordinate)
            if self.session.need_motion_blur:
                if scatter_name not in updated_motion_blur_node_names:
                    motion_time_offsets = utility.object_motion_time_offsets(
                        eval_object,
                        self.session.motion_blur_start_frame_offset,
                        self.session.motion_blur_end_frame_offset)
                    if instance_object.parent is not None:
                        parent_motion_time_offsets = utility.object_motion_time_offsets(
                            instance_object.parent,
                            self.session.motion_blur_start_frame_offset,
                            self.session.motion_blur_end_frame_offset)
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
        # Update scatters
        # Remove objects
        for octane_scatter_name in to_remove_octane_scatter_node_names:
            octane_scatter_node = self.get_octane_node(octane_scatter_name, consts.NodeType.NT_GEO_SCATTER)
            octane_scatter_node.linked_geometry_name = ""
            self.update_scatter_node(depsgraph, octane_scatter_node, True)
            if octane_scatter_name in self.synced_octane_scatter_node_names:
                self.synced_octane_scatter_node_names.remove(octane_scatter_name)
            self.remove_octane_node(octane_scatter_name, consts.NodeType.NT_GEO_SCATTER)
        # Update transforms
        for scatter_name, octane_scatter_node in scatter_map.items():
            self.update_scatter_node(depsgraph, octane_scatter_node, update_now)
            self.synced_octane_scatter_node_names.add(octane_scatter_node.name)
        self.changed_data_ids.clear()
        self.oct_synced_object_data_octane_names.clear()
        self.depsgraph_object_instance_names = current_object_instance_names
        self.depsgraph_object_instances_num_changed = False
        # Always trigger an update here; we will check whether this update is necessary in C++ code
        self.geometry_group_node.need_update = True
        self.geometry_group_node.update_to_engine(update_now)

    def update_scatter_node(self, _depsgraph, octane_scatter_node, update_now):
        linked_geometry_name = getattr(octane_scatter_node, "linked_geometry_name", "")
        octane_scatter_node.set_pin_id(consts.PinID.P_GEOMETRY, True, linked_geometry_name, "")
        octane_scatter_node.node.build()
        if octane_scatter_node.need_update:
            self.session.set_status_msg(
                "Uploading and evaluating scatter node[%s] in Octane..." % octane_scatter_node.name, update_now)
            octane_scatter_node.update_to_engine(update_now)

    def update_motion_blur_sample(self, motion_time_offset, depsgraph, scene, _view_layer, _context=None,
                                  _update_now=True):
        for instance_object in depsgraph.object_instances:
            eval_object = instance_object.object
            origin_object = eval_object.original
            octane_property = getattr(origin_object.data, "octane", None)
            object_name = instance_object.object.name
            scatter_name = octane_name.resolve_scatter_octane_name(instance_object, scene, False)
            if not self.has_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER):
                continue
            octane_scatter_node = self.get_octane_node(scatter_name, consts.NodeType.NT_GEO_SCATTER)
            if (octane_scatter_node.motion_time_offsets
                    and motion_time_offset in octane_scatter_node.motion_time_offsets):
                octane_scatter_id = self.resolve_octane_scatter_id(object_name, instance_object.persistent_id)
                object_matrix = instance_object.matrix_world.copy()
                use_octane_coordinate = utility.use_octane_coordinate(eval_object)
                octane_scatter_node.node.set_motion_sample(octane_scatter_id, motion_time_offset, object_matrix,
                                                           use_octane_coordinate)
                self.motion_blur_node_names[scatter_name] = consts.NodeType.NT_GEO_SCATTER
                # Mesh Deformation
                if origin_object.octane.use_deform_motion:
                    if eval_object.type in ("MESH", "CURVE"):
                        # Mesh Data
                        domain_modifier = utility.find_smoke_domain_modifier(eval_object)
                        if domain_modifier is None or domain_modifier.domain_settings.use_mesh:
                            object_data_name = octane_name.resolve_object_data_octane_name(eval_object, scene, False)
                            octane_node = self.get_octane_node(object_data_name, consts.NodeType.NT_GEO_MESH)
                            if not hasattr(octane_node, "updated_motion_time_offsets"):
                                octane_node.updated_motion_time_offsets = {}
                            if not octane_node.updated_motion_time_offsets.get(motion_time_offset, False):
                                self.update_geometry_data(depsgraph, eval_object, octane_node, octane_property,
                                                          motion_time_offset)
                                octane_node.updated_motion_time_offsets[motion_time_offset] = True
                                self.motion_blur_node_names[object_data_name] = consts.NodeType.NT_GEO_MESH

    def update_motion_blur(self, _depsgraph, _scene, _view_layer, _context=None, update_now=True):
        for node_name, node_type in self.motion_blur_node_names.items():
            octane_node = self.get_octane_node(node_name, node_type)
            octane_node.node.build()
            if octane_node.need_update:
                octane_node.update_to_engine(update_now)

    def update_object_material_tags(self, depsgraph):
        changed_material_slot_object_names = set()
        self.object_material_tag_manager.update_object_material_tags(self.session.material_cache, depsgraph,
                                                                     changed_material_slot_object_names)
        for object_name in changed_material_slot_object_names:
            _object = depsgraph.scene.objects[object_name]
            _object.update_tag()
            _object.data.update_tag()

    def post_update(self):
        super().post_update()
        self.dg_updated_object_data_names.clear()
