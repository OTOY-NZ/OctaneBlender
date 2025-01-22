# <pep8 compliant>


bl_info = {
    "name": "OctaneBlender (v. 29.12)",
    "author": "OTOY Inc.",
    "version": (29, 11, 0),
    "blender": (4, 2, 0),
    "location": "Info header, render engine menu",
    "description": "OctaneBlender",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#60Octane%20for%20Blender",
    "tracker_url": "https://render.otoy.com/forum/viewforum.php?f=114",
    "support": 'OFFICIAL',
    "category": "Render"
}

import os
import time
import weakref
import numpy as np
import bpy
from octane import engine
from octane import core
from octane.core.client import OctaneBlender
from octane.core.frame_buffer import ViewportDrawData, RenderDrawData
from octane.utils import consts, logger, runtime_globals, utility

# Activate the OctaneRender engine
ACTIVE_RENDER_ENGINE = None


def set_active_render_engine(active_engine):
    global ACTIVE_RENDER_ENGINE
    ACTIVE_RENDER_ENGINE = weakref.ref(active_engine) if active_engine is not None else None


def get_active_render_engine():
    # noinspection PyCallingNonCallable
    return ACTIVE_RENDER_ENGINE() if ACTIVE_RENDER_ENGINE is not None else None


def is_render_engine_active():
    return get_active_render_engine() is not None


class OctaneRender(bpy.types.RenderEngine):
    bl_idname = 'octane'
    bl_label = "Octane"
    bl_use_shading_nodes = True
    bl_use_shading_nodes_custom = False
    bl_use_eevee_viewport = True
    bl_use_preview = False
    bl_use_exclude_layers = True
    bl_use_save_buffers = True
    bl_use_spherical_stereo = True

    def __init__(self):
        self.session = None
        self.draw_data = None
        self.is_active = True
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.create_session()

    def __del__(self):
        try:
            self.is_active = False
            self.free_session()
        except ReferenceError:
            pass

    def create_session(self):
        from octane.core.session import RenderSession
        self.session = RenderSession(self)

    def free_session(self):
        try:
            if core.ENABLE_OCTANE_ADDON_CLIENT:
                self.free_draw_data()
                if self.session.is_render_started:
                    if self.session.session_type == consts.SessionType.VIEWPORT:
                        self.session.stop_render()
                if self.session is not None:
                    self.session.clear()
            else:
                engine.free(self)
        except AttributeError:
            pass
        except ReferenceError:
            pass

    # final render
    def update(self, data, depsgraph):
        active_engine = get_active_render_engine()
        if active_engine is not None:
            active_engine.free_session()
            active_engine.is_active = False
            active_engine.tag_update()
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            return
        if getattr(self, "session", None) is None:
            engine.create(self, data)
        engine.reset(self, data, depsgraph)

    def render(self, depsgraph):
        set_active_render_engine(self)
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.final_render(depsgraph)
        else:
            engine.render(self, depsgraph)

    def final_render(self, depsgraph):
        if not OctaneBlender().init_server():
            self.update_stats("Error", "OctaneServer is not connected or activated")
            self.report({"ERROR"}, "OctaneServer is not connected or activated")
            return
        scene = depsgraph.scene_eval
        width = utility.render_resolution_x(scene)
        height = utility.render_resolution_y(scene)
        for layer_index, layer in enumerate(scene.view_layers):
            if not layer.use:
                continue
            self.create_session()
            self.session.session_type = consts.SessionType.FINAL_RENDER
            utility.add_render_passes(self, scene, layer)
            self.render_layer(depsgraph, scene, layer, width, height)
            if self.test_break():
                break
            # Blender 4.2 Update: only process the first view layer as Blender calls render() for each view layer
            break

    def render_layer(self, depsgraph, scene, layer, width, height):
        start_time = time.time()
        # self.session.reset_render()
        # Init Scene
        self.session.start_render(scene, is_viewport=False)
        init_time = time.time()
        init_elapsed_time = init_time - start_time
        self.update_stats("Init Time", "%.2f" % init_elapsed_time)
        # Sync Scene
        self.session.render_update(depsgraph, scene, layer)
        self.session.set_resolution(width, height, True)
        OctaneBlender().use_shared_surface(False)
        render_pass_ids = utility.get_view_layer_render_pass_ids(layer)
        self.session.set_render_pass_ids(render_pass_ids)
        sync_time = time.time()
        sync_elapsed_time = sync_time - init_time
        self.update_stats("Scene Synced Time", "%.2f" % sync_elapsed_time)
        result = self.begin_result(0, 0, width, height, layer=layer.name)
        render_layer = result.layers[0]
        combined = render_layer.passes["Combined"]
        sample_status = ""
        combined_draw_data = RenderDrawData(consts.RenderPassID.Beauty,
                                            consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, width, height, combined)
        while True:
            is_task_completed = False
            if combined_draw_data.update_render_result(False):
                calculated_samples_per_pixel = combined_draw_data.calculated_samples_per_pixel
                tonemapped_samples_per_pixel = combined_draw_data.tonemapped_samples_per_pixel
                _region_samples_per_pixel = combined_draw_data.region_samples_per_pixel
                max_sample = combined_draw_data.max_samples_per_pixel
                current_sample = max(calculated_samples_per_pixel, tonemapped_samples_per_pixel)
                sample_status = "Sample: %d/%d" % (current_sample, max_sample)
                is_task_completed = current_sample >= max_sample
                self.update_result(result)
            render_time = time.time()
            render_elapsed_time = render_time - sync_time
            time_status = "Render time: %s" % utility.time_human_readable_from_seconds(render_elapsed_time)
            if sample_status == "":
                self.update_stats("", "%s" % time_status)
            else:
                self.update_stats("", "%s | %s" % (time_status, sample_status))
            if is_task_completed or self.test_break():
                break
            time.sleep(0.5)
        for render_pass in render_layer.passes:
            render_pass_id = utility.get_render_pass_id_by_name(render_pass.name)
            if render_pass.channels == 1:
                frame_data_type = consts.RenderFrameDataType.RENDER_FRAME_FLOAT_MONO
            else:
                frame_data_type = consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA
            render_pass_draw_data = RenderDrawData(render_pass_id, frame_data_type, width, height, render_pass)
            if render_pass_id == consts.RenderPassID.Beauty:
                combined_np_array = np.empty(len(combined.rect) * 4, dtype=np.float32)
                combined.rect.foreach_get(combined_np_array)
                render_pass.rect.foreach_set(combined_np_array)
            elif render_pass_id > consts.RenderPassID.Beauty:
                if render_pass.channels == 4:
                    if utility.is_denoise_render_pass(render_pass_id):
                        tonemapped_samples_per_pixel = 0
                        max_sample = 0
                        while True:
                            if render_pass_draw_data.update_render_result(False):
                                calculated_samples_per_pixel = render_pass_draw_data.calculated_samples_per_pixel
                                tonemapped_samples_per_pixel = render_pass_draw_data.tonemapped_samples_per_pixel
                                max_sample = render_pass_draw_data.max_samples_per_pixel
                                render_time = time.time()
                                render_elapsed_time = render_time - sync_time
                                time_status = "Render time: %s" % utility.time_human_readable_from_seconds(
                                    render_elapsed_time)
                                sample_status = "Denoising Sample: %d/%d/%d" % (
                                    calculated_samples_per_pixel, tonemapped_samples_per_pixel, max_sample)
                                self.update_stats("", "%s | %s" % (time_status, sample_status))
                                if tonemapped_samples_per_pixel == max_sample:
                                    break
                            self.report({'INFO'}, "Wait for the Render Result of Pass %s. Samples: %d/%d" % (
                                render_pass.name, tonemapped_samples_per_pixel, max_sample))
                            if self.test_break():
                                break
                            time.sleep(0.05)
                    else:
                        if not render_pass_draw_data.update_render_result(False):
                            self.report({'ERROR'}, "Cannot Get the Render Result of Pass %s" % render_pass.name)
                elif render_pass.channels == 1:
                    if not render_pass_draw_data.update_render_result(False):
                        self.report({'ERROR'}, "Cannot Get the Render Result of Pass %s" % render_pass.name)
            self.update_result(result)
            if self.test_break():
                break
        self.session.export_render_pass(depsgraph, scene, layer, render_layer)
        self.end_result(result)
        self.session.stop_render()

    def bake(self, depsgraph, obj, pass_type, pass_filter, width, height):
        pass

    # viewport render
    def view_update(self, context, depsgraph):
        active_engine = get_active_render_engine()
        if (active_engine is not None and active_engine is not self) or not self.is_active:
            self.update_stats("", "Final render or other rendered viewport is active! "
                                  "Please turn off them and try again!")
            if not self.is_active:
                utility.set_all_viewport_shading_type("SOLID", True)
            return
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.session.session_type = consts.SessionType.VIEWPORT
            if not self.session.is_render_started:
                set_active_render_engine(self)
                result = OctaneBlender().init_server()
                if result:
                    self.session.start_render(depsgraph.scene, is_viewport=True,
                                              resource_cache_type=utility.get_enum_int_value(depsgraph.scene.octane,
                                                                                             "resource_cache_type", 0))
                else:
                    self.update_stats("Error", "OctaneServer is not connected or activated")
            self.session.view_update(self, depsgraph, context)
        else:
            if not self.session:
                set_active_render_engine(self)
                engine.create(self, context.blend_data,
                              context.region, context.space_data, context.region_data)
                self._force_update_all_script_nodes()
            engine.reset(self, context.blend_data, depsgraph)
            engine.sync(self, depsgraph, context.blend_data)

    def view_draw(self, context, depsgraph):
        if not self.is_active:
            return
        # Draw viewport render
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.session.view_draw(self, depsgraph, context)
            region = context.region
            scene = depsgraph.scene
            self.draw_render_result(context.view_layer, region, scene)
        else:
            engine.draw(self, depsgraph, context.region, context.space_data, context.region_data)

    def check_redraw(self):
        if self.draw_data:
            self.tag_redraw()

    def free_draw_data(self):
        try:
            if self.draw_data is not None:
                self.draw_data.free(self)
        except AttributeError as _e:
            pass

    def immediate_fetch_draw_data(self):
        if self.draw_data is not None:
            self.draw_data.tag_immediate_fetch(True)

    def draw_render_result(self, view_layer, region, scene):
        if not self.session.is_render_started:
            return
        is_demo = self.session.is_demo_version()
        render_pass_id = self.session.get_current_preview_render_pass_id(view_layer)
        is_render_pass_shared_surface_supported = not (utility.is_grayscale_render_pass(render_pass_id)
                                                       or utility.is_cryptomatte_render_pass(render_pass_id)
                                                       or utility.is_output_aov_render_pass(render_pass_id))
        is_shared_surface_supported = (OctaneBlender().is_shared_surface_supported()
                                       and is_render_pass_shared_surface_supported)
        use_shared_surface = (self.session.use_shared_surface and is_shared_surface_supported)
        is_draw_data_just_created = False
        if region:
            # Get viewport dimensions
            if not self.draw_data or self.draw_data.needs_replacement(region.width, region.height, use_shared_surface):
                self.free_draw_data()
                self.draw_data = ViewportDrawData(is_demo, render_pass_id, region.width, region.height, self, scene,
                                                  use_shared_surface)
                is_draw_data_just_created = True
        if self.draw_data:
            self.draw_data.update(render_pass_id)
            if not is_draw_data_just_created:
                self.draw_data.draw(self, scene)

    def _update_all_script_nodes(self, obj):
        if not getattr(obj, 'node_tree', None) or not getattr(obj.node_tree, 'nodes', None):
            return
        for node in obj.node_tree.nodes.values():
            if node.bl_idname == 'ShaderNodeGroup':
                self._update_all_script_nodes(node)
            if node.bl_idname in ('ShaderNodeOctOSLTex', 'ShaderNodeOctOSLCamera', 'ShaderNodeOctOSLBakingCamera',
                                  'ShaderNodeOctOSLProjection', 'ShaderNodeOctVectron'):
                self.update_script_node(node)

    def _force_update_all_script_nodes(self):
        collections = (bpy.data.materials, bpy.data.textures, bpy.data.worlds)
        for collection in collections:
            for obj in collection.values():
                self._update_all_script_nodes(obj)

    def update_script_node(self, node):
        from octane.utils import osl
        osl.update_script_node(node, self.report)

    def update_render_passes(self, scene=None, view_layer=None):
        utility.add_view_layer_render_passes(scene, self, view_layer)


classes = (
    OctaneRender,
)


# Triggers when window's workspace is changed
workspace_change_owner = object()
workspace_change_subscribe_to = bpy.types.Window, "workspace"


def workspace_change_callback():
    utility.set_all_viewport_shading_type("SOLID")


def register():
    from bpy.utils import register_class
    path = os.path.dirname(__file__)
    user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', path='')))
    OctaneBlender().init(path, user_path)
    major, minor, patch = bpy.app.version
    OctaneBlender().set_blender_version(major, minor, patch)
    runtime_globals.register()
    from octane import preferences
    preferences.register()

    from octane import compatibilities
    from octane import utils
    from octane import properties_
    from octane import uis
    from octane import nodes
    from octane import operators_
    from octane import engine
    from octane.core import resource_cache

    utils.register()
    properties_.register()
    uis.register()
    nodes.register()
    operators_.register()

    for cls in classes:
        register_class(cls)

    from . import handlers
    bpy.app.handlers.version_update.append(compatibilities.do_versions)
    bpy.app.handlers.load_post.append(handlers.octane_load_post_handler)
    bpy.app.handlers.depsgraph_update_post.append(handlers.octane_depsgraph_update_post_handler)

    bpy.msgbus.subscribe_rna(
        key=workspace_change_subscribe_to,
        owner=workspace_change_owner,
        args=(),
        notify=workspace_change_callback,
    )
    bpy.msgbus.publish_rna(key=workspace_change_subscribe_to)


def unregister():
    from bpy.utils import unregister_class
    from octane import compatibilities
    from octane import utils
    from octane import preferences
    from octane import properties_
    from octane import uis
    from octane import nodes
    from octane import operators_
    from octane import engine
    from octane.core import resource_cache

    resource_cache.reset_resource_cache(None)
    OctaneBlender().exit()

    from . import handlers
    bpy.app.handlers.version_update.remove(compatibilities.do_versions)
    bpy.app.handlers.load_post.remove(handlers.octane_load_post_handler)
    bpy.app.handlers.depsgraph_update_post.remove(handlers.octane_depsgraph_update_post_handler)

    preferences.unregister()
    utils.unregister()
    properties_.unregister()
    uis.unregister()
    nodes.unregister()
    operators_.unregister()

    runtime_globals.unregister()

    for cls in classes:
        unregister_class(cls)

    bpy.msgbus.clear_by_owner(workspace_change_owner)
