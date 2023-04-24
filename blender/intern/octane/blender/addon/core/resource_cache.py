import bpy
from bpy.app.handlers import persistent
from collections import defaultdict
from octane.utils import consts, utility
from octane import core
from octane.core.client import OctaneBlender


@persistent
def reset_resource_cache(arg):
    from octane import engine
    from octane import operators
    if core.ENABLE_OCTANE_ADDON_CLIENT:
        if engine.IS_RENDERING:
            print("Cannot clear the resource cache during the Octane engine is rendering.")
        else:
            from octane.core.client import OctaneBlender
            from octane.core.resource_cache import ResourceCache
            scene = bpy.context.scene
            oct_scene = scene.octane
            OctaneBlender().update_server_settings(consts.ResourceCacheType.NONE)
            OctaneBlender().reset_render()
            ResourceCache().reset()
    else:
        import _octane
        if not engine.IS_RENDERING:
            print("Clear Octane Resource Cache System")
            _octane.command_to_octane(operators.COMMAND_TYPES['CLEAR_RESOURCE_CACHE_SYSTEM'])

@persistent
def update_dirty_mesh_names(scene, depsgraph):
    from octane import engine
    if engine.IS_RENDERING:
        return    
    for update in depsgraph.updates:
        if update.is_updated_geometry and isinstance(update.id, bpy.types.Mesh):
            ResourceCache().add_dirty_mesh_names(update.id.name)
    oct_scene = scene.octane
    if oct_scene.dirty_resource_detection_strategy_type == "Select":
        active_obj = bpy.context.active_object
        if active_obj.type == "MESH":
            ResourceCache().add_dirty_mesh_names(active_obj.data.name)


class ResourceCache(metaclass=utility.Singleton):

    def __init__(self):
        # resouce type => set(resouce names)
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

    def update_cached_node_resouce(self):
        node_resouce_dict = {}
        OctaneBlender().get_cached_node_resource(node_resouce_dict)
        self.cached_node_resource_names.clear()
        for name, _type in node_resouce_dict.items():
            self.cached_node_resource_names[_type].add(name)

    def add_dirty_mesh_names(self, mesh_name):
        self.dirty_mesh_names.add(mesh_name)