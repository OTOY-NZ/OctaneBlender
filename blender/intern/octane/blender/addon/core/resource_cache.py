# <pep8 compliant>

import bpy
from collections import defaultdict
from octane.utils import consts, utility
from octane import core
from octane.core.client import OctaneBlender
from octane.operators_ import utility_functions


class ResourceCache(metaclass=utility.Singleton):

    def __init__(self):
        # resource type => set(resource names)
        self.cached_node_resource_names = defaultdict(set)
        # updated mesh_names
        self.dirty_mesh_names = set()

    def reset(self):
        self.cached_node_resource_names.clear()
        self.dirty_mesh_names.clear()

    def is_mesh_node_cached(self, mesh_name, mesh_node_name):
        if mesh_name in self.dirty_mesh_names:
            return False
        if mesh_node_name not in self.cached_node_resource_names[consts.NodeResourceType.GEOMETRY]:
            return False
        return True

    def update_cached_node_resource(self):
        node_resource_dict = {}
        OctaneBlender().get_cached_node_resource(node_resource_dict)
        self.cached_node_resource_names.clear()
        for name, _type in node_resource_dict.items():
            self.cached_node_resource_names[_type].add(name)

    def add_dirty_mesh_names(self, mesh_name):
        self.dirty_mesh_names.add(mesh_name)


def reset_resource_cache(_scene):
    from octane import is_render_engine_active
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        if is_render_engine_active():
            print("Cannot clear the resource cache during the Octane engine is rendering.")
        else:
            from octane.core.client import OctaneBlender
            OctaneBlender().update_server_settings(consts.ResourceCacheType.NONE)
            OctaneBlender().reset_render()
            ResourceCache().reset()
    else:
        import _octane
        if not is_render_engine_active():
            print("Clear Octane Resource Cache System")
            _octane.command_to_octane(utility_functions.COMMAND_TYPES['CLEAR_RESOURCE_CACHE_SYSTEM'])


def update_dirty_mesh_names(scene, depsgraph):
    from octane import is_render_engine_active
    if is_render_engine_active():
        return
    for update in depsgraph.updates:
        if update.is_updated_geometry and isinstance(update.id, bpy.types.Mesh):
            ResourceCache().add_dirty_mesh_names(update.id.name)
    oct_scene = scene.octane
    active_obj = getattr(bpy.context, "active_object", None)
    if not active_obj:
        active_obj = bpy.context.view_layer.objects.active
    if not active_obj or not active_obj.data:
        return
    eval_obj = active_obj.evaluated_get(depsgraph)
    is_editmode = getattr(eval_obj.data, "is_editmode", False)
    strategy_type = oct_scene.dirty_resource_detection_strategy_type
    if strategy_type == "Select" or (strategy_type == "Edit Mode" and is_editmode):
        if eval_obj.type == "MESH":
            ResourceCache().add_dirty_mesh_names(eval_obj.data.name)
