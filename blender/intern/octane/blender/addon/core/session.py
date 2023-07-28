import bpy
import numpy as np
import time
import math
import collections
import _thread
import threading
import weakref
import queue
from octane.utils import consts, utility
from octane import core
from octane.core.resource_cache import ResourceCache
from octane.core.caches import OctaneNodeCache, ImageCache, MaterialCache, LightCache, WorldCache, CompositeCache, RenderAOVCache, KernelCache, OctaneRenderTargetCache, SceneCache
from octane.core.object_cache import ObjectCache
from octane.core.client import OctaneBlender
from octane.core.octane_node import OctaneNode, CArray
from octane.nodes.base_node import OctaneBaseNode


class RenderSession(object):
    def __init__(self, engine):
        self.session_type = consts.SessionType.UNKNOWN
        self.use_shared_surface = utility.get_preferences().use_shared_surface and OctaneBlender().is_shared_surface_supported()
        # Minimum update gap(second)
        self.view_update_min_gap = utility.get_preferences().min_viewport_update_interval
        self.last_view_update_time = time.time()
        self.graph_time = 0
        self.need_motion_blur = False
        self.motion_blur_start_frame_offset = 0
        self.motion_blur_end_frame_offset = 0        
        self.motion_blur_time_offsets = set()
        self.object_cache = ObjectCache(self)
        self.image_cache = ImageCache(self)
        self.material_cache = MaterialCache(self)
        self.light_cache = LightCache(self)
        self.world_cache = WorldCache(self)
        self.composite_cache = CompositeCache(self)
        self.render_aov_cache = RenderAOVCache(self)
        self.kernel_cache = KernelCache(self)
        self.scene_cache = SceneCache(self)
        self.rendertarget_cache = OctaneRenderTargetCache(self)
        self.engine_weakref = weakref.ref(engine) if engine is not None else None        

    def __del__(self):
        self.clear()

    def clear(self):
        self.need_motion_blur = False
        self.motion_blur_time_offsets = None        
        self.object_cache = None
        self.image_cache = None        
        self.material_cache = None
        self.light_cache = None
        self.world_cache = None
        self.composite_cache = None
        self.render_aov_cache = None
        self.kernel_cache = None
        self.scene_cache = None
        self.rendertarget_cache = None
        self.engine_weakref = None

    def reset(self):
        self.need_motion_blur = False
        self.motion_blur_time_offsets.clear()        
        self.object_cache.reset()
        self.image_cache.reset()
        self.material_cache.reset()
        self.light_cache.reset()
        self.world_cache.reset()
        self.composite_cache.reset()
        self.render_aov_cache.reset()
        self.kernel_cache.reset()
        self.scene_cache.reset()
        self.rendertarget_cache.reset()

    def is_viewport(self):
        return self.session_type == consts.SessionType.VIEWPORT

    def is_final(self):
        return self.session_type == consts.SessionType.FINAL_RENDER

    def is_preview(self):
        return self.session_type == consts.SessionType.PREVIEW

    def is_export(self):
        return self.session_type == consts.SessionType.EXPORT

    def get_current_preview_render_pass_id(self, view_layer):
        if self.render_aov_cache:
            return self.render_aov_cache.get_current_preview_render_pass_id(view_layer)
        return consts.RenderPassId.BEAUTY

    def get_enabled_render_pass_ids(self, view_layer):
        if self.render_aov_cache:
            return self.render_aov_cache.get_enabled_render_pass_ids(view_layer)
        return [consts.RenderPassId.BEAUTY, ]

    def update_viewport_render_result(self):
        try:
            if self.engine_weakref and self.engine_weakref() is not None:
                self.engine_weakref().check_redraw()
        except:
            print("RenderSession Viewport Update Stopped")
            return
        return 0.05

    def start_render(self, cache_path=None, is_viewport=True, resource_cache_type=consts.ResourceCacheType.NONE):
        if cache_path is None:
            cache_path = bpy.app.tempdir
        OctaneBlender().update_server_settings(resource_cache_type, self.use_shared_surface)
        OctaneBlender().reset_render()
        ResourceCache().update_cached_node_resouce()
        OctaneBlender().start_render(cache_path)
        if is_viewport:
            bpy.app.timers.register(self.update_viewport_render_result)

    def stop_render(self):
        OctaneBlender().stop_render()
        ResourceCache().reset()

    def reset_render(self):
        self.reset()
        OctaneBlender().reset_render()

    def set_resolution(self, width, height):
        OctaneBlender().set_resolution(width, height)

    def update_graph_time(self):
        OctaneBlender().set_graph_time(self.graph_time)

    def set_render_pass_ids(self, render_pass_ids):
        OctaneBlender().set_render_pass_ids(render_pass_ids)

    def view_update(self, engine, depsgraph, context):
        current_view_update_time = time.time()
        scene = depsgraph.scene_eval
        view_layer = depsgraph.view_layer_eval
        need_redraw = False
        is_first_update = self.scene_cache.need_update_all
        # check diff
        self.image_cache.diff(depsgraph, scene, view_layer, context)
        self.object_cache.diff(depsgraph, scene, view_layer, context)
        self.material_cache.diff(depsgraph, scene, view_layer, context)        
        self.light_cache.diff(depsgraph, scene, view_layer, context)
        self.world_cache.diff(depsgraph, scene, view_layer, context)
        self.composite_cache.diff(depsgraph, scene, view_layer, context)
        self.render_aov_cache.diff(depsgraph, scene, view_layer, context)
        self.kernel_cache.diff(depsgraph, scene, view_layer, context)
        self.scene_cache.diff(depsgraph, scene, view_layer, context)
        if not is_first_update and current_view_update_time - self.last_view_update_time < self.view_update_min_gap:
            engine.tag_update()
            return
        self.last_view_update_time = current_view_update_time
        # update
        if self.image_cache.need_update:
            self.image_cache.update(depsgraph, scene, view_layer, context)
        if self.material_cache.need_update:
            self.material_cache.update(depsgraph, scene, view_layer, context)
            need_redraw = True
        if self.object_cache.need_update:
            self.object_cache.update(depsgraph, scene, view_layer, context)            
        if self.light_cache.need_update:
            self.light_cache.update(depsgraph, scene, view_layer, context)
            need_redraw = True            
        if self.world_cache.need_update:
            self.world_cache.update(depsgraph, scene, view_layer, context)
            need_redraw = True
        if self.composite_cache.need_update:
            self.composite_cache.update(depsgraph, scene, view_layer, context)
        if self.render_aov_cache.need_update:
            self.render_aov_cache.update(depsgraph, scene, view_layer, context)
        if self.kernel_cache.need_update:
            self.kernel_cache.update(depsgraph, scene, view_layer, context)
        if self.scene_cache.need_update:
            self.scene_cache.update(depsgraph, scene, view_layer, context)
        self.scene_cache.update_camera(depsgraph, scene, view_layer, context)
        # update render target
        if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
            self.rendertarget_cache.update(depsgraph, scene, view_layer, context)
            need_redraw = True
        # update graph time
        self.update_graph_time()            
        if need_redraw:
            engine.tag_redraw()

    def view_draw(self, depsgraph, context):
        scene = depsgraph.scene_eval
        view_layer = depsgraph.view_layer_eval
        region = context.region
        self.scene_cache.update_camera(depsgraph, scene, view_layer, context)
        self.set_resolution(region.width, region.height)
        # update render target
        if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
            self.rendertarget_cache.update(depsgraph, scene, view_layer, context)        

    def render_update(self, depsgraph, scene=None, view_layer=None):
        context = None
        if scene is None:
            scene = depsgraph.scene_eval
        if view_layer is None:
            view_layer = depsgraph.view_layer_eval
        # init motion blur settings
        self.init_motion_blur_settings(depsgraph, scene, view_layer, context)
        # check diff
        self.image_cache.diff(depsgraph, scene, view_layer, context)
        self.object_cache.diff(depsgraph, scene, view_layer, context)        
        self.material_cache.diff(depsgraph, scene, view_layer, context)
        self.light_cache.diff(depsgraph, scene, view_layer, context)
        self.world_cache.diff(depsgraph, scene, view_layer, context)
        self.composite_cache.diff(depsgraph, scene, view_layer, context)
        self.render_aov_cache.diff(depsgraph, scene, view_layer, context)
        self.kernel_cache.diff(depsgraph, scene, view_layer, context)
        self.scene_cache.diff(depsgraph, scene, view_layer, context)
        # update
        if self.material_cache.need_update:
            self.material_cache.update(depsgraph, scene, view_layer, context)        
        if self.object_cache.need_update:
            self.object_cache.update(depsgraph, scene, view_layer, context)
        if self.image_cache.need_update:
            self.image_cache.update(depsgraph, scene, view_layer, context)        
        if self.light_cache.need_update:
            self.light_cache.update(depsgraph, scene, view_layer, context)            
        if self.world_cache.need_update:
            self.world_cache.update(depsgraph, scene, view_layer, context)
        if self.composite_cache.need_update:
            self.composite_cache.update(depsgraph, scene, view_layer, context)
        if self.render_aov_cache.need_update:
            self.render_aov_cache.update(depsgraph, scene, view_layer, context)
        if self.kernel_cache.need_update:
            self.kernel_cache.update(depsgraph, scene, view_layer, context)
        if self.scene_cache.need_update:
            self.scene_cache.update(depsgraph, scene, view_layer, context)
        self.scene_cache.update_camera(depsgraph, scene, view_layer, context)
        # update motion blur
        self.update_motion_blur(depsgraph, scene, view_layer, context)        
        # update render target
        if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
            self.rendertarget_cache.update(depsgraph, scene, view_layer, context)
        # update graph time
        self.update_graph_time()

    def init_motion_blur_settings(self, depsgraph, scene, view_layer, context=None):
        self.need_motion_blur = scene.render.use_motion_blur and self.is_final()
        self.motion_blur_start_frame_offset = 0
        self.motion_blur_end_frame_offset = 0
        self.motion_blur_time_offsets.clear()
        if self.need_motion_blur:
            clamp_motion_blur_data_source = scene.octane.animation_settings.clamp_motion_blur_data_source
            frame_offset = math.ceil(scene.octane.animation_settings.shutter_time / 100.0)
            mb_direction = scene.octane.animation_settings.mb_direction
            if clamp_motion_blur_data_source:
                if mb_direction == "Before":
                    frame_offset = max(0, min(scene.frame_current - scene.frame_start, frame_offset))
                elif mb_direction == "Symmetric":
                    half_frame_offset = frame_offset / 2.0
                    half_frame_offset = max(0, min(scene.frame_end - scene.frame_current, min(scene.frame_current - scene.frame_start, half_frame_offset)))
                    frame_offset = half_frame_offset * 2
                elif mb_direction == "After":
                    frame_offset = max(0, min(scene.frame_end - scene.frame_current, frame_offset))
            if mb_direction == "Before":
                self.motion_blur_start_frame_offset = -frame_offset
                self.motion_blur_end_frame_offset = 0
                self.graph_time = 1.0
            elif mb_direction == "Symmetric":
                half_frame_offset = math.ceil(frame_offset / 2.0)
                self.motion_blur_start_frame_offset = -half_frame_offset
                self.motion_blur_end_frame_offset = half_frame_offset
                self.graph_time = 0.5
            elif mb_direction == "After":
                self.motion_blur_start_frame_offset = 0
                self.motion_blur_end_frame_offset = frame_offset
                self.graph_time = 0
                
    def update_motion_blur(self, depsgraph, scene, view_layer, context=None):                
        if not self.need_motion_blur:
            return False
        engine = self.engine_weakref()
        frame_current = scene.frame_current
        subframe_current = scene.frame_subframe
        for time_offset in sorted(list(self.motion_blur_time_offsets)):
            if time_offset == 0:
                continue
            motion_time = frame_current + subframe_current + time_offset
            motion_frame = math.floor(motion_time)
            motion_subframe = motion_time - motion_frame
            engine.frame_set(motion_frame, subframe=motion_subframe)
            self.scene_cache.update_camera_motion_blur_sample(time_offset, depsgraph, scene, view_layer, context)
            self.object_cache.update_motion_blur_sample(time_offset, depsgraph, scene, view_layer, context)
        engine.frame_set(frame_current, subframe=subframe_current)
        self.scene_cache.update_camera_motion_blur(depsgraph, scene, view_layer, context)
        self.object_cache.update_motion_blur(depsgraph, scene, view_layer, context)