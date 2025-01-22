# <pep8 compliant>

import bpy
from octane.utils import consts

def init():
    print("OctaneBlender Engine Init")
    import os.path

    path = os.path.dirname(__file__)
    user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', path='')))

    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        _octane.init(path, user_path)


def exit():
    print("OctaneBlender Engine Exit")
    from octane import core
    from octane.core import resource_cache
    resource_cache.reset_resource_cache(None)
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        import _octane
        _octane.exit()


def create(engine, data, region=None, v3d=None, rv3d=None):
    print("OctaneBlender Engine Create")

    from octane import core
    from octane.utils import ocio
    ocio.update_ocio_info()
    # Init node helper
    from octane.nodes.base_node_tree import NodeTreeHandler
    NodeTreeHandler.init_node_helper()

    import bpy
    data = data.as_pointer()
    prefs = bpy.context.preferences.as_pointer()
    screen = 0

    from octane.operators_ import utility_functions
    dirty_resources = utility_functions.get_dirty_resources()

    if region:
        screen = region.id_data.as_pointer()
        region = region.as_pointer()
    if v3d:
        screen = screen or v3d.id_data.as_pointer()
        v3d = v3d.as_pointer()
    if rv3d:
        screen = screen or rv3d.id_data.as_pointer()
        rv3d = rv3d.as_pointer()

    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        engine.session = _octane.create(
            engine.as_pointer(), prefs, data, screen, region, v3d, rv3d,
            consts.ExportSceneMode.NONE, "", dirty_resources)


def free(engine):
    print("OctaneBlender Engine Free")
    if hasattr(engine, "session"):
        if engine.session:
            from octane import core
            if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
                import _octane
                _octane.free(engine.session)
        del engine.session

    from octane.operators_ import utility_functions
    utility_functions.set_all_mesh_resource_cache_tags(False)


def render(engine, depsgraph):
    from octane import utility
    # print("OctaneBlender Engine Render")
    if engine.is_preview:
        return
    scene = depsgraph.scene_eval
    utility.add_render_passes(engine, scene)
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        import _octane
        if hasattr(engine, "session"):
            _octane.render(engine.session, depsgraph.as_pointer())


def bake(engine, depsgraph, obj, pass_type, pass_filter, object_id, pixel_array, num_pixels, depth, result):
    # print("OctaneBlender Engine Bake")
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        session = getattr(engine, "session", None)
        import _octane
        if session is not None:
            _octane.bake(engine.session, depsgraph.as_pointer(), obj.as_pointer(), pass_type, pass_filter,
                         object_id, pixel_array.as_pointer(), num_pixels, depth, result.as_pointer())


def reset(engine, data, depsgraph):
    # print("OctaneBlender Engine Reset")
    if engine.is_preview:
        return
    data = data.as_pointer()
    depsgraph = depsgraph.as_pointer()
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        if getattr(engine, "session", None):
            import _octane
            _octane.reset(engine.session, data, depsgraph)


def sync(engine, depsgraph, _data):
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        if getattr(engine, "session", None):
            import _octane
            _octane.sync(engine.session, depsgraph.as_pointer())


def draw(engine, depsgraph, _region, v3d, rv3d):
    # print("OctaneBlender Engine Draw")
    depsgraph = depsgraph.as_pointer()
    v3d = v3d.as_pointer()
    rv3d = rv3d.as_pointer()
    from octane import core
    if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        if getattr(engine, "session", None):
            import _octane
            # draw render image
            _octane.draw(engine.session, depsgraph, v3d, rv3d)
