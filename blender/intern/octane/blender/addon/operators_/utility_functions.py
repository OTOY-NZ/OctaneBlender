# <pep8 compliant>

import bpy
from bpy.types import Operator

from octane.utils import consts, logger


def set_mesh_resource_cache_tag(obj, is_dirty):
    if obj and obj.type in ('MESH',):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            if hasattr(cur_octane_mesh_data, 'resource_dirty_tag'):
                cur_octane_mesh_data.resource_dirty_tag = is_dirty


def generate_resource_data_hash_tag(obj):
    resource_data_hash_tag = ''
    if obj and obj.type in ('MESH',):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            material_resource_hash_tag = ''
            for mat in obj.material_slots:
                material_resource_hash_tag += (mat.name + ",")
            sphere_primitive_hash_tag_1 = "[%d-%d-%f]" % (
                obj.data.octane_enable_sphere_attribute, obj.data.octane_hide_original_mesh,
                obj.data.octane_sphere_radius)
            sphere_primitive_hash_tag_2 = "[%d-%d-%f-%f]" % (
                obj.data.octane_use_randomized_radius, obj.data.octane_sphere_randomized_radius_seed,
                obj.data.octane_sphere_randomized_radius_min, obj.data.octane_sphere_randomized_radius_max)
            sphere_primitive_hash_tag = sphere_primitive_hash_tag_1 + sphere_primitive_hash_tag_2
            resource_data_hash_tag = material_resource_hash_tag + sphere_primitive_hash_tag
    return resource_data_hash_tag


def is_resource_data_hash_tag_updated(obj, cur_resource_data_hash_tag):
    if obj and obj.type in ('MESH',):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            return cur_resource_data_hash_tag != cur_octane_mesh_data.resource_data_hash_tag
    return True


def update_resource_data_hash_tag_updated(obj, cur_resource_data_hash_tag):
    if obj and obj.type in ('MESH',):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            cur_octane_mesh_data.resource_data_hash_tag = cur_resource_data_hash_tag


def get_dirty_resources():
    resources = []
    for obj in bpy.data.objects:
        if obj and obj.type in ('MESH',):
            resource_data_hash_tag = generate_resource_data_hash_tag(obj)
            is_dirty = is_resource_data_hash_tag_updated(obj, resource_data_hash_tag)
            update_resource_data_hash_tag_updated(obj, resource_data_hash_tag)
            if is_dirty:
                resources.append(obj.data.name)
            else:
                if len(obj.particle_systems):
                    resources.append(obj.data.name)
                else:
                    cur_octane_mesh_data = getattr(obj.data, 'octane', None)
                    if cur_octane_mesh_data:
                        if getattr(cur_octane_mesh_data, 'resource_dirty_tag', False):
                            resources.append(obj.data.name)
    return resources


def set_all_mesh_resource_cache_tags(is_dirty):
    for obj in bpy.data.objects:
        if obj.mode == "OBJECT":
            set_mesh_resource_cache_tag(obj, is_dirty)
        else:
            set_mesh_resource_cache_tag(obj, True)


class OCTANE_OT_base_command(Operator):
    command_type = 0
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane import core
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.client import OctaneBlender
            OctaneBlender().utils_function(self.command_type, "")
            return {'FINISHED'}
        else:
            import _octane
            _octane.command_to_octane(self.command_type)
            return {'FINISHED'}


class OCTANE_OT_show_octane_node_graph(OCTANE_OT_base_command):
    """Show Octane NodeGraph(VIEW Mode Only. Please DO NOT ADD or DELETE nodes.)"""
    bl_idname = "octane.show_octane_node_graph"
    bl_label = "Show Octane Node Graph"
    command_type = consts.UtilsFunctionType.SHOW_NODEGRAPH


class OCTANE_OT_show_octane_viewport(OCTANE_OT_base_command):
    """Show Octane Viewport (Suggest VIEW Mode Only. Camera navigation in the viewport would not synchronize to
    Blender viewport.)"""
    bl_idname = "octane.show_octane_viewport"
    bl_label = "Show Octane Viewport"
    command_type = consts.UtilsFunctionType.SHOW_VIEWPORT


class OCTANE_OT_show_octane_network_preference(OCTANE_OT_base_command):
    """Show Octane Network Preference (For the Studio+ License Only)"""
    bl_idname = "octane.show_octane_network_preference"
    bl_label = "Show Octane Network Preference"
    command_type = consts.UtilsFunctionType.SHOW_NETWORK_PREFERENCE


class OCTANE_OT_stop_render(OCTANE_OT_base_command):
    """Force to stop rendering and empty GPUs"""
    bl_idname = "octane.stop_render"
    bl_label = "Stop Render and Empty GPUs"
    command_type = consts.UtilsFunctionType.STOP_RENDERING


class OCTANE_OT_show_octane_log(OCTANE_OT_base_command):
    """Show Octane Log"""
    bl_idname = "octane.show_octane_log"
    bl_label = "Show Octane Log"
    command_type = consts.UtilsFunctionType.SHOW_LOG


class OCTANE_OT_show_octane_device_setting(OCTANE_OT_base_command):
    """Show Octane Device Setting"""
    bl_idname = "octane.show_octane_device_setting"
    bl_label = "Show Octane Device Setting"
    command_type = consts.UtilsFunctionType.SHOW_DEVICE_SETTINGS


class OCTANE_OT_activate(OCTANE_OT_base_command):
    """Activate the Octane license"""
    bl_idname = "octane.activate"
    bl_label = "Open activation state dialog on OctaneServer"
    command_type = consts.UtilsFunctionType.SHOW_ACTIVATION


class OCTANE_OT_toggle_record(OCTANE_OT_base_command):
    """DEBUG: Toggle Record"""
    bl_idname = "octane.toggle_record"
    bl_label = "Toggle Record"
    command_type = consts.UtilsFunctionType.TOGGLE_RECORD


class OCTANE_OT_play_record(OCTANE_OT_base_command):
    """DEBUG: Play Record"""
    bl_idname = "octane.play_record"
    bl_label = "Play Record"
    command_type = consts.UtilsFunctionType.PLAY_RECORD


class OCTANE_OT_clear_resource_cache(Operator):
    """Clear the Resource Cache"""
    bl_idname = "octane.clear_resource_cache"
    bl_label = "Clear"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, _context):
        from octane.core import resource_cache
        resource_cache.reset_resource_cache(None)
        return {'FINISHED'}


class OCTANE_OT_open_octanedb(OCTANE_OT_base_command):
    """Show the Octane DB"""
    bl_idname = "octane.open_octanedb"
    bl_label = "Open Octane DB(LiveDB and LocalDB)"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane.core.octanedb import OctaneDBManager
        OctaneDBManager().open_octanedb()
        return {'FINISHED'}


class OCTANE_OT_save_as_octanedb(bpy.types.Operator):
    """Save current material as OctaneDB"""
    bl_idname = "octane.save_as_octanedb"
    bl_label = "Save as OctaneDB"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, context):
        import _octane
        scene = context.scene
        cur_obj = bpy.context.object
        if cur_obj and len(cur_obj.material_slots):
            cur_material = cur_obj.material_slots[cur_obj.active_material_index].material
            data = context.blend_data.as_pointer()
            prefs = bpy.context.preferences.as_pointer()
            _ret = _octane.export_localdb(scene.as_pointer(), context.as_pointer(), prefs, data,
                                          cur_material.as_pointer())
        return {'FINISHED'}


def sync_octane_aov_output_number(_scene):
    try:
        view_layer = bpy.context.view_layer
        octane_view_layer = view_layer.octane
        composite_node_tree_name = octane_view_layer.aov_output_group_collection.composite_node_tree
        aov_output_group_name = octane_view_layer.aov_output_group_collection.aov_output_group_node
        if composite_node_tree_name in bpy.data.node_groups:
            if aov_output_group_name in bpy.data.node_groups[composite_node_tree_name].nodes:
                bpy.data.node_groups[composite_node_tree_name].check_validity()
                node = bpy.data.node_groups[composite_node_tree_name].nodes[aov_output_group_name]
                octane_view_layer.aov_out_number = int(node.group_number)
    except Exception as e:
        logger.exception(e)


def update_resource_cache_tag(_scene):
    obj = None
    try:
        obj = bpy.context.view_layer.objects.active
    except Exception as e:
        logger.exception(e)
    from octane import is_render_engine_active
    if obj and not is_render_engine_active():
        scene = bpy.context.scene
        oct_scene = scene.octane
        if oct_scene.dirty_resource_detection_strategy_type == 'Edit Mode':
            if obj.mode == 'EDIT':
                set_mesh_resource_cache_tag(obj, True)
        else:
            set_mesh_resource_cache_tag(obj, True)


def octane_db_menu_func(self, _context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.separator()
    self.layout.operator(OCTANE_OT_open_octanedb.bl_idname, text="Open Octane DB")


_CLASSES = [
    OCTANE_OT_show_octane_node_graph,
    OCTANE_OT_show_octane_viewport,
    OCTANE_OT_show_octane_network_preference,
    OCTANE_OT_stop_render,
    OCTANE_OT_show_octane_log,
    OCTANE_OT_show_octane_device_setting,
    OCTANE_OT_activate,
    OCTANE_OT_open_octanedb,
    OCTANE_OT_save_as_octanedb,
    OCTANE_OT_clear_resource_cache,
    OCTANE_OT_toggle_record,
    OCTANE_OT_play_record,
]


def register():
    from bpy.utils import register_class
    for cls in _CLASSES:
        register_class(cls)
    bpy.types.TOPBAR_MT_window.append(octane_db_menu_func)


def unregister():
    from bpy.utils import unregister_class
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.TOPBAR_MT_window.remove(octane_db_menu_func)
