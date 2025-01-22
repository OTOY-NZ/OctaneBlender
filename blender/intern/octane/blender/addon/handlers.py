# <pep8 compliant>
import bpy
from bpy.app.handlers import persistent
from octane.core import resource_cache
from octane.operators_ import utility_functions
from octane.properties_ import geometry
from octane.nodes import base_node_tree
from octane.nodes.base_node_tree import NodeTreeHandler
from octane.utils import ocio, utility


@persistent
def octane_load_post_handler(arg):
    if arg is None or type(arg) is str:
        # Blender version >= 3.6
        scene = bpy.context.scene
    else:
        # Blender version <= 3.5
        scene = arg
    ocio.update_ocio_info()
    resource_cache.reset_resource_cache(scene)
    NodeTreeHandler.on_file_load(scene)
    utility.set_all_viewport_shading_type("SOLID")


@persistent
def octane_depsgraph_update_post_handler(scene, depsgraph):
    base_node_tree.node_tree_update_handler(scene)
    utility_functions.sync_octane_aov_output_number(scene)
    utility_functions.update_resource_cache_tag(scene)
    geometry.update_blender_volume_grid_info(scene)
    resource_cache.update_dirty_mesh_names(scene, depsgraph)
