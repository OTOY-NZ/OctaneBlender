# <pep8 compliant>

import os

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

from octane.utils import logger, utility


class OCTANE_OT_update_osl_camera_nodes(Operator):
    bl_idname = 'octane.update_osl_camera_nodes'
    bl_label = ''

    def invoke(self, context, _event):
        cam = context.camera
        oct_cam = cam.octane
        oct_cam.osl_camera_node_collections.update_nodes(context)
        return {'FINISHED'}


class OCTANE_OT_update_aov_output_group_nodes(Operator):
    bl_idname = 'octane.update_aov_output_group_nodes'
    bl_label = ''

    def invoke(self, context, _event):
        view_layer = context.view_layer
        oct_view_layer = view_layer.octane
        oct_view_layer.aov_output_group_collection.update_nodes(context)
        return {'FINISHED'}


class OCTANE_OT_update_octane_geo_nodes(Operator):
    bl_idname = 'octane.update_octane_geo_nodes'
    bl_label = ''

    def invoke(self, context, _event):
        current_object = context.active_object
        if current_object and current_object.data and getattr(current_object.data, 'octane', None):
            current_object.data.octane.octane_geo_node_collections.update_nodes(context)
        return {'FINISHED'}


class OCTANE_OT_generate_orbx_preview(Operator):
    """Generate Orbx Preview Mesh (The current mesh data will be replaced with the preview data. The current object's
    delta matrix may be updated according to the orbx settings.)"""
    bl_idname = "octane.generate_orbx_preview"
    bl_label = "Generate Orbx Preview"
    bl_register = True
    bl_undo = True

    def clear_abc(self, imported_abc):
        pending_nodes = []
        resource_names = []
        pending_nodes.append(imported_abc)
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            resource_names.append(cur_node.name)
            for sub_node in cur_node.children:
                pending_nodes.append(sub_node)
        for name in resource_names:
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)

    def find_mesh_data(self, imported_abc):
        pending_nodes = []
        pending_nodes_matrix = []
        mesh_and_matrix_data = []
        pending_nodes.append(imported_abc)
        pending_nodes_matrix.append(imported_abc.matrix_world)
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            if cur_node.type == "MESH":
                mesh_and_matrix_data.append((cur_node.data, cur_node.matrix_world.inverted()))
            for sub_node in cur_node.children:
                pending_nodes.append(sub_node)
        return mesh_and_matrix_data

    def reorganize_alembic_mesh_data(self, current_obj, imported_abc):
        default_matrix = mathutils.Matrix()
        empty_mesh_data = current_obj.data.copy()
        empty_mesh_data.clear_geometry()
        empty_mesh_data.name = "[OrbxPreview]%s" % current_obj.name
        children_names = []
        for child in current_obj.children:
            children_names.append(child.name)
        for name in children_names:
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)
        current_obj.data = empty_mesh_data
        pending_nodes = [imported_abc]
        empty_resources = []
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            if cur_node.type == "EMPTY":
                if cur_node.matrix_world == default_matrix:
                    for sub_node in cur_node.children:
                        pending_nodes.append(sub_node)
                    empty_resources.append(cur_node.name)
                else:
                    cur_node.parent = current_obj
            if cur_node.type == "MESH":
                cur_node.parent = current_obj
                cur_node.data.octane.external_alembic_mesh_tag = True
                if len(cur_node.constraints) == 0:
                    constraint = cur_node.constraints.new("TRANSFORM")
                    constraint.target = current_obj
                    constraint.to_min_x = constraint.to_max_x = cur_node.location.x
                    constraint.to_min_y = constraint.to_max_y = cur_node.location.y
                    constraint.to_min_z = constraint.to_max_z = cur_node.location.z
                    constraint.to_min_x_rot = constraint.to_max_x_rot = cur_node.rotation_euler.x
                    constraint.to_min_y_rot = constraint.to_max_y_rot = cur_node.rotation_euler.y
                    constraint.to_min_z_rot = constraint.to_max_z_rot = cur_node.rotation_euler.z
                    constraint.to_min_x_scale = constraint.to_max_x_scale = cur_node.scale.x
                    constraint.to_min_y_scale = constraint.to_min_y_scale = cur_node.scale.y
                    constraint.to_min_z_scale = constraint.to_min_z_scale = cur_node.scale.z
                    constraint.mix_mode = 'REPLACE'
                    constraint.target_space = 'LOCAL'
                    constraint.owner_space = 'LOCAL'
                cur_node.data.update_tag()
        return empty_resources

    def copy_mesh_data_from_abc(self, current_obj, imported_abc):
        import mathutils
        imported_abc.matrix_world = mathutils.Matrix()
        mesh_data_list = self.find_mesh_data(imported_abc)
        if len(mesh_data_list):
            current_obj.data = mesh_data_list[0][0]
            current_obj.data.octane.enable_octane_offset_transform = True
            offset_matrix = mesh_data_list[0][1]
            current_obj.data.octane.octane_offset_translation = offset_matrix.to_translation()
            current_obj.data.octane.octane_offset_rotation = offset_matrix.to_euler('YXZ')
            current_obj.data.octane.octane_offset_scale = offset_matrix.to_scale()
            current_obj.data.octane.octane_offset_rotation_order = '2'

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, context):
        import _octane
        import os
        import time
        current_obj = context.active_object
        current_obj_name = current_obj.name
        if current_obj.data and len(current_obj.data.octane.imported_orbx_file_path):
            orbx_path = current_obj.data.octane.imported_orbx_file_path
            orbx_path = bpy.path.abspath(orbx_path)
            if os.path.exists(orbx_path):
                abc_filename = 'ORBX_PREVIEW_%s_%d.abc' % (current_obj_name, int(time.time()) % 10000)
                if current_obj.data.octane.orbx_preview_type == "External Alembic":
                    if len(current_obj.data.octane.converted_alembic_asset_path) == 0:
                        base_dir = bpy.path.abspath("//")
                        if base_dir == '':
                            abc_dir = bpy.context.preferences.filepaths.temporary_directory
                        else:
                            abc_dir = base_dir
                    else:
                        abc_dir = bpy.path.abspath(current_obj.data.octane.converted_alembic_asset_path)
                else:
                    abc_dir = bpy.app.tempdir
                abc_path = os.path.join(abc_dir, abc_filename)
                try:
                    if os.path.exists(abc_path):
                        os.remove(abc_path)
                except Exception as e:
                    logger.exception(e)
                abc_path = bpy.path.abspath(abc_path)
                _octane.orbx_preview(orbx_path, abc_path, bpy.context.scene.render.fps)
                if os.path.exists(abc_path):
                    bpy.ops.wm.alembic_import(filepath=abc_path, validate_meshes=True, as_background_job=False,
                                              set_frame_range=False)
                    imported_abc = context.active_object
                    imported_abc_name = imported_abc.name
                    current_obj = bpy.data.objects[current_obj_name]
                    imported_abc = bpy.data.objects[imported_abc_name]
                    if current_obj.data.octane.orbx_preview_type == "External Alembic":
                        empty_resources = self.reorganize_alembic_mesh_data(current_obj, imported_abc)
                        for resource_name in empty_resources:
                            bpy.data.objects.remove(bpy.data.objects[resource_name], do_unlink=True)
                    else:
                        self.copy_mesh_data_from_abc(current_obj, imported_abc)
                        self.clear_abc(imported_abc)
                    current_obj.data.octane.imported_orbx_file_path = orbx_path
                    current_obj.select_set(True)
                    # os.remove(abc_path)
        return {'FINISHED'}


class OCTANE_OT_load_octane_startup(Operator):
    """Load the Octane Startup blend file"""
    bl_idname = "octane.load_octane_startup"
    bl_label = "Load Octane Startup"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, _context):
        addon_folder = utility.get_addon_folder()
        path = os.path.join(addon_folder, r"assets/startup.blend")
        path = bpy.path.abspath(path)
        bpy.ops.wm.read_homefile(filepath=path)
        return {"FINISHED"}


def new_menu_func(self, _context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(OCTANE_OT_load_octane_startup.bl_idname, text="Octane Default Startup")


_CLASSES = [
    OCTANE_OT_update_octane_geo_nodes,
    OCTANE_OT_update_osl_camera_nodes,
    OCTANE_OT_update_aov_output_group_nodes,
    OCTANE_OT_generate_orbx_preview,
    OCTANE_OT_load_octane_startup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)
    bpy.types.TOPBAR_MT_file_new.append(new_menu_func)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.TOPBAR_MT_file_new.remove(new_menu_func)
