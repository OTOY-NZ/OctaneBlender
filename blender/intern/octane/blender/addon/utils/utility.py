import bpy


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def set_collection(collection, items, set_func):
    for i in range(0, len(collection)):
        collection.remove(0)
    for item in items:
        collection.add()
        set_func(collection[-1], item)


def traverse_all_node_trees_in_collection(collection):
    for item in collection.values():
        if getattr(item, "node_tree", None) is not None:
            yield item.node_tree

def traverse_all_node_trees():
    if getattr(bpy.data, "worlds", None):
        for world_node_tree in traverse_all_node_trees_in_collection(bpy.data.worlds):
            yield world_node_tree
    if getattr(bpy.data, "materials", None):
        for material_node_tree in traverse_all_node_trees_in_collection(bpy.data.materials):
            yield material_node_tree
    if getattr(bpy.data, "textures", None):
        for texture_node_tree in traverse_all_node_trees_in_collection(bpy.data.textures):
            yield texture_node_tree
    if getattr(bpy.data, "node_groups", None):
        for node_group_tree in bpy.data.node_groups:
            yield node_group_tree