# <pep8 compliant>

import math
import os
import time
import traceback
import weakref
from xml.etree import ElementTree

import bpy
from octane.core.caches import ImageCache, MaterialCache, LightCache, WorldCache, CompositeCache, RenderAOVCache, \
    KernelCache, OctaneRenderTargetCache, SceneCache
from octane.core.client import OctaneBlender
from octane.core.object_cache import ObjectCache
from octane.core.resource_cache import ResourceCache
from octane.utils import consts, logger, ocio, utility


class RenderSession(object):
    def __init__(self, engine):
        self.session_type = consts.SessionType.UNKNOWN
        self.octane_version_type = consts.VersionType.UNKNOWN
        self.session_init_time = time.time()
        self.render_start_time = time.time()
        self.is_render_started = False
        self.use_shared_surface = (utility.get_preferences().use_shared_surface
                                   and OctaneBlender().is_shared_surface_supported(True))
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

    def is_demo_version(self):
        return self.octane_version_type == consts.VersionType.DEMO

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
        self.session_init_time = time.time()
        self.render_start_time = time.time()
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
        octane_view_layer = view_layer.octane
        if octane_view_layer.render_pass_style == "RENDER_PASSES":
            return utility.get_current_preview_render_pass_id(view_layer)
        else:
            if self.render_aov_cache:
                return self.render_aov_cache.get_current_preview_render_pass_id(view_layer)
        return consts.RenderPassID.Beauty

    def update_viewport_render_result(self):
        try:
            if self.engine_weakref and self.engine_weakref() is not None:
                self.engine_weakref().check_redraw()
        except Exception as e:
            logger.exception(e, "RenderSession Viewport Update Stopped: %s" % e)
            return
        return 0.05

    def start_render(self, scene, cache_path=None, is_viewport=True, resource_cache_type=consts.ResourceCacheType.NONE):
        if cache_path is None:
            cache_path = bpy.app.tempdir
        tonemap_buffer_type = consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_LDR
        color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB
        if not is_viewport:
            octane_scene = scene.octane
            if octane_scene.prefer_image_type == "DEFAULT":
                if utility.is_active_imager_enabled(scene):
                    tonemap_buffer_type = consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_LDR
                    color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB
                else:
                    tonemap_buffer_type = consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_HDR_FLOAT
                    color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_LINEAR_SRGB
            elif octane_scene.prefer_image_type == "LDR":
                tonemap_buffer_type = consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_LDR
                color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB
            elif octane_scene.prefer_image_type == "HDR":
                tonemap_buffer_type = consts.TonemapBufferType.TONEMAP_BUFFER_TYPE_HDR_FLOAT
                color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_LINEAR_SRGB
        ocio.update_ocio_info()
        self.fetch_octane_version()
        OctaneBlender().update_server_settings(resource_cache_type, self.use_shared_surface,
                                               tonemap_buffer_type, color_space_type)
        OctaneBlender().reset_render()
        ResourceCache().update_cached_node_resource()
        OctaneBlender().start_render(cache_path, is_viewport, self.use_shared_surface)
        if is_viewport:
            bpy.app.timers.register(self.update_viewport_render_result)
            # Fix the problem that Octane's shading type does not be updated when users use shortcut to start a
            # preview render session
            utility.update_octane_viewport_shading_type("RENDERED")
            OctaneBlender().update_change_manager(False, False)
        self.is_render_started = True
        self.render_start_time = time.time()

    def stop_render(self):
        OctaneBlender().update_change_manager(True, True)
        OctaneBlender().stop_render()
        ResourceCache().reset()
        self.is_render_started = False
        # Fix the problem that Octane's shading type does not be updated when users use shortcut to start a preview
        # render session
        utility.update_octane_viewport_shading_type()
        OctaneBlender().utils_function(consts.UtilsFunctionType.RENDER_STOP, "")
        return True

    def reset_render(self):
        self.reset()
        OctaneBlender().reset_render()

    def get_elapsed_time(self):
        return time.time() - self.render_start_time

    def set_resolution(self, width, height, update_now=True):
        camera_border_box = self.scene_cache.camera_border_box
        if camera_border_box is not None:
            use_border = True
            # border_width = camera_border_box.right - camera_border_box.left
            # border_height = camera_border_box.top - camera_border_box.bottom
            region_left = int(camera_border_box.left * width)
            region_bottom = int(camera_border_box.bottom * height)
            region_right = int(camera_border_box.right * width)
            region_top = int(camera_border_box.top * height)
            region_width = region_right - region_left
            region_height = region_top - region_bottom
            region_start_x = region_left
            region_start_y = height - region_bottom - region_height
        else:
            use_border = False
            region_start_x = 0
            region_start_y = 0
            region_width = 65535
            region_height = 65535
        OctaneBlender().set_resolution(width, height, use_border, False,
                                       region_start_x, region_start_y, region_width, region_height, update_now)

    def update_graph_time(self, scene):
        if not self.need_motion_blur:
            fps = scene.render.fps / scene.render.fps_base
            self.graph_time = (scene.frame_current / fps if fps > 0 else 0)
        OctaneBlender().set_graph_time(self.graph_time)

    def set_render_pass_ids(self, render_pass_ids, update_now=True):
        OctaneBlender().set_render_pass_ids(render_pass_ids, update_now)

    def report_traceback(self, msg, update_now=True):
        self.set_status_msg("Found an error during rendering...\n%s" % msg, update_now)

    def set_status_msg(self, status_msg, update_now=True):
        OctaneBlender().set_status_msg(status_msg, update_now)

    def get_status_msg(self):
        return OctaneBlender().get_status_msg()

    def view_update(self, engine, depsgraph, context):
        if not self.is_render_started:
            return
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
        if not is_first_update:
            if current_view_update_time - self.last_view_update_time < self.view_update_min_gap:
                engine.tag_update()
                return
        if not OctaneBlender().try_lock_update_mutex():
            engine.tag_update()
            return
        self.last_view_update_time = current_view_update_time
        update_now = False
        try:
            # update
            OctaneBlender().set_batch_state(True, update_now)
            self.set_status_msg("Uploading and evaluating scene in Octane...", update_now)
            if self.image_cache.need_update:
                self.image_cache.update(depsgraph, scene, view_layer, context, update_now)
            if self.material_cache.need_update:
                self.material_cache.update(depsgraph, scene, view_layer, context, update_now)
                need_redraw = True
            self.set_status_msg("Uploading and evaluating objects in Octane...", update_now)
            if self.object_cache.need_update:
                self.object_cache.update(depsgraph, scene, view_layer, context, update_now)
                need_redraw = True
            self.set_status_msg("Uploading and evaluating lights in Octane...", update_now)
            if self.light_cache.need_update:
                self.light_cache.update(depsgraph, scene, view_layer, context, update_now)
                need_redraw = True
            self.set_status_msg("Uploading and evaluating worlds in Octane...", update_now)
            if self.world_cache.need_update:
                self.world_cache.update(depsgraph, scene, view_layer, context, update_now)
                need_redraw = True
            self.set_status_msg("Uploading and evaluating composite node trees in Octane...", update_now)
            if self.composite_cache.need_update:
                self.composite_cache.update(depsgraph, scene, view_layer, context, update_now)
            self.set_status_msg("Uploading and evaluating render aov node trees in Octane...", update_now)
            if self.render_aov_cache.need_update:
                self.render_aov_cache.update(depsgraph, scene, view_layer, context, update_now)
            self.set_status_msg("Uploading and evaluating kernel node trees in Octane...", update_now)
            if self.kernel_cache.need_update:
                self.kernel_cache.update(depsgraph, scene, view_layer, context, update_now)
            self.set_status_msg("Uploading and evaluating scene settings in Octane...", update_now)
            if self.scene_cache.need_update:
                self.scene_cache.update(depsgraph, scene, view_layer, context, update_now)
            render_pass_ids = utility.get_view_layer_render_pass_ids(view_layer)
            render_pass_ids.insert(0, self.get_current_preview_render_pass_id(view_layer))
            self.set_render_pass_ids(render_pass_ids, update_now)
            self.set_status_msg("Uploading and evaluating camera in Octane...", update_now)
            need_update_camera = self.scene_cache.update_camera(depsgraph, scene, view_layer, context, update_now)
            if need_update_camera:
                need_redraw = True
            # update render target
            self.set_status_msg("Uploading and evaluating render targets in Octane...", update_now)
            if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
                self.rendertarget_cache.update(depsgraph, scene, view_layer, context, update_now)
                need_redraw = True
            OctaneBlender().send_batch_updates(update_now)
            OctaneBlender().set_batch_state(False, update_now)
            # update graph time
            self.update_graph_time(scene)
            # update change manager
            OctaneBlender().update_change_manager(False, True)
            if is_first_update:
                OctaneBlender().set_scene_state(consts.SceneState.INITIALIZED, update_now)
            self.set_status_msg("Waiting for image...", update_now)
        except Exception as e:
            logger.exception(e)
            self.report_traceback(traceback.format_exc(), update_now)
        finally:
            # Always unlock the mutex
            OctaneBlender().unlock_update_mutex()
        if need_redraw:
            engine.immediate_fetch_draw_data()
            engine.tag_redraw()

    def view_draw(self, engine, depsgraph, context):
        if not self.is_render_started:
            return
        if not OctaneBlender().try_lock_update_mutex():
            engine.tag_update()
            return
        update_now = False
        try:
            need_redraw = False
            scene = depsgraph.scene_eval
            view_layer = depsgraph.view_layer_eval
            region = context.region
            if self.scene_cache.update_camera(depsgraph, scene, view_layer, context, update_now):
                need_redraw = True
            if self.scene_cache.is_active_camera_changed:
                engine.tag_update()
            self.set_resolution(region.width, region.height, update_now)
            OctaneBlender().update_change_manager(False, True)
            # update render target
            if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
                self.rendertarget_cache.update(depsgraph, scene, view_layer, context)
                need_redraw = True
            if need_redraw:
                engine.immediate_fetch_draw_data()
        except Exception as e:
            logger.exception(e)
            self.report_traceback("Exception: %s\n%s" % (e, traceback.format_exc()), update_now)
        finally:
            # Always unlock the mutex
            OctaneBlender().unlock_update_mutex()

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
        update_now = True
        if self.material_cache.need_update:
            self.material_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.object_cache.need_update:
            self.object_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.image_cache.need_update:
            self.image_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.light_cache.need_update:
            self.light_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.world_cache.need_update:
            self.world_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.composite_cache.need_update:
            self.composite_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.render_aov_cache.need_update:
            self.render_aov_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.kernel_cache.need_update:
            self.kernel_cache.update(depsgraph, scene, view_layer, context, update_now)
        if self.scene_cache.need_update:
            self.scene_cache.update(depsgraph, scene, view_layer, context, update_now)
        self.scene_cache.update_camera(depsgraph, scene, view_layer, context, update_now)
        # update motion blur
        self.update_motion_blur(depsgraph, scene, view_layer, context, update_now)
        # update render target
        if self.rendertarget_cache.diff(depsgraph, scene, view_layer, context):
            self.rendertarget_cache.update(depsgraph, scene, view_layer, context)
        # update graph time
        self.update_graph_time(scene)

    def init_motion_blur_settings(self, _depsgraph, scene, _view_layer, _context=None):
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
                    half_frame_offset = max(0, min(scene.frame_end - scene.frame_current,
                                                   min(scene.frame_current - scene.frame_start, half_frame_offset)))
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

    def update_motion_blur(self, depsgraph, scene, view_layer, context=None, update_now=True):
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
            self.scene_cache.update_camera_motion_blur_sample(time_offset, depsgraph,
                                                              scene, view_layer, context, update_now)
            self.object_cache.update_motion_blur_sample(time_offset, depsgraph,
                                                        scene, view_layer, context, update_now)
        engine.frame_set(frame_current, subframe=subframe_current)
        self.scene_cache.update_camera_motion_blur(depsgraph, scene, view_layer, context, update_now)
        self.object_cache.update_motion_blur(depsgraph, scene, view_layer, context, update_now)

    def export_render_pass(self, _depsgraph, scene, _view_layer, render_layer):
        octane_scene = scene.octane
        enable_octane_output = octane_scene.use_octane_export
        if not enable_octane_output:
            return
        root_et = ElementTree.Element("exportRenderPass")
        if octane_scene.octane_export_mode == "SEPARATE_IMAGE_FILES":
            export_mode = consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_SEPARATE
        elif octane_scene.octane_export_mode == "MULTILAYER_EXR":
            export_mode = consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_MULTILAYER
        elif octane_scene.octane_export_mode == "DEEP_EXR":
            export_mode = consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_DEEP_EXR
        else:
            export_mode = consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_SEPARATE
        root_et.set("exportMode", str(export_mode))
        root_et.set("premultipleAlpha", str(int(octane_scene.octane_export_premultiplied_alpha)))
        force_use_tone_map = octane_scene.octane_export_force_use_tone_map
        ocio_color_space_name = octane_scene.octane_export_ocio_color_space_name
        ocio_look = octane_scene.octane_export_ocio_look
        ocio_look, _ = ocio.resolve_octane_ocio_look(ocio_look)
        if ocio_color_space_name == "sRGB(default)":
            ocio_look = "None"
            force_use_tone_map = True
        elif ocio_color_space_name in ("Linear sRGB(default)", "ACES2065-1", "ACEScg"):
            ocio_look = ""
        root_et.set("forceToneMapping", str(int(force_use_tone_map)))
        root_et.set("ocioColorSpaceName", ocio_color_space_name)
        root_et.set("ocioLookName", ocio_look)
        octane_exr_compression_mode = utility.get_enum_int_value(octane_scene,
                                                                 "octane_deep_exr_compression_mode"
                                                                 if octane_scene.octane_export_mode == "DEEP_EXR"
                                                                 else "octane_exr_compression_mode",
                                                                 0)
        root_et.set("compressionType", str(octane_exr_compression_mode))
        root_et.set("compressionLevel", str(octane_scene.octane_export_dwa_compression_level))
        root_et.set("jpegQuality", str(octane_scene.octane_export_jpeg_quality))
        root_et.set("tiffCompressionMode", str(utility.get_enum_int_value(octane_scene,
                                                                          "octane_tiff_compression_mode",
                                                                          1)))
        image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_PNG_8
        if octane_scene.octane_export_file_type == "PNG":
            if octane_scene.octane_integer_bit_depth == "8_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_PNG_8
            elif octane_scene.octane_integer_bit_depth == "16_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_PNG_16
        elif octane_scene.octane_export_file_type == "TIFF":
            if octane_scene.octane_integer_bit_depth == "8_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_TIFF_8
            elif octane_scene.octane_integer_bit_depth == "16_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_TIFF_16
        elif octane_scene.octane_export_file_type == "EXR":
            if octane_scene.octane_float_bit_depth == "16_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_EXR_16
            elif octane_scene.octane_float_bit_depth == "32_BIT":
                image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_EXR_32
        elif octane_scene.octane_export_file_type == "JPEG":
            image_type = consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_JPEG
        root_et.set("imageSaveFormat", str(image_type))
        if ocio_color_space_name == "sRGB(default)":
            color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB
        elif ocio_color_space_name == "Linear sRGB(default)":
            color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_LINEAR_SRGB
        elif ocio_color_space_name == "ACES2065-1":
            color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_ACES2065_1
        elif ocio_color_space_name == "ACEScg":
            color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_ACESCG
        elif ocio_color_space_name == "":
            if image_type in (consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_PNG_8,
                              consts.ImageSaveFormat.IMAGE_SAVE_FORMAT_PNG_16):
                color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_SRGB
            else:
                color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_LINEAR_SRGB
        else:
            color_space_type = consts.NamedColorSpace.NAMED_COLOR_SPACE_OCIO
        root_et.set("colorSpaceType", str(color_space_type))
        # File path
        if octane_scene.reuse_blender_output_path:
            filepath = scene.render.filepath
        else:
            filepath = octane_scene.octane_output_path
        raw_export_file_path = bpy.path.abspath(filepath)
        # File path, with frame number
        file_path_with_frame = utility.blender_path_frame(raw_export_file_path, scene.frame_current, 4)
        file_dir = os.path.dirname(file_path_with_frame)
        # File name, without suffix
        file_name_with_frame = bpy.path.display_name_from_filepath(file_path_with_frame)
        octane_prefix_tag = octane_scene.octane_export_prefix_tag \
            if len(octane_scene.octane_export_prefix_tag) else "[OctaneExport]"
        octane_postfix_tag = octane_scene.octane_export_postfix_tag
        # octane_prefix_tag + File name + octane_postfix_tag, without suffix
        processed_file_name = octane_prefix_tag + file_name_with_frame + octane_postfix_tag
        processed_file_name = utility.blender_path_frame(processed_file_name, scene.frame_current)
        renderlayer_name = render_layer.name
        if consts.OCTANE_EXPORT_VIEW_LAYER_TAG in processed_file_name:
            processed_file_name = processed_file_name.replace(consts.OCTANE_EXPORT_VIEW_LAYER_TAG, renderlayer_name)
        else:
            if len(renderlayer_name) > 0 and len(scene.view_layers) > 1:
                processed_file_name = processed_file_name + "_" + renderlayer_name
        if octane_scene.octane_export_mode == "SEPARATE_IMAGE_FILES":
            pass
        else:
            # Do not need the pass name in the output
            if consts.OCTANE_EXPORT_OCTANE_PASS_TAG in processed_file_name:
                processed_file_name = processed_file_name.replace(consts.OCTANE_EXPORT_OCTANE_PASS_TAG, "")
        final_full_path = os.path.join(file_dir, processed_file_name)
        root_et.set("fullPath", str(final_full_path))
        root_et.set("dirPath", file_dir)
        # Render Passes
        render_passes_et = ElementTree.SubElement(root_et, "renderPasses")
        is_export_valid = False
        for render_pass in render_layer.passes:
            # Do not include 'Combined' Pass
            if render_pass.name == "Combined":
                continue
            if octane_scene.exclude_default_beauty_passes and render_pass.name == "Beauty":
                continue
            render_pass_et = ElementTree.SubElement(render_passes_et, "renderPass")
            render_pass_id = utility.get_render_pass_id_by_name(render_pass.name)
            render_pass_filename = processed_file_name
            if consts.OCTANE_EXPORT_OCTANE_PASS_TAG in render_pass_filename:
                render_pass_filename = render_pass_filename.replace(consts.OCTANE_EXPORT_OCTANE_PASS_TAG,
                                                                    render_pass.name)
            else:
                render_pass_filename = render_pass_filename + "_" + render_pass.name
            render_pass_et.set("fileName", render_pass_filename)
            render_pass_et.set("name", render_pass.name)
            render_pass_et.set("id", str(render_pass_id))
            is_export_valid = True
        if is_export_valid:
            xml_data = ElementTree.tostring(root_et, encoding="unicode")
            _response = OctaneBlender().utils_function(consts.UtilsFunctionType.EXPORT_RENDER_PASS, xml_data)

    def fetch_octane_version(self):
        request_et = ElementTree.Element("OctaneVersionInfo")
        xml_data = ElementTree.tostring(request_et, encoding="unicode")
        response_data = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_VERSION_INFO, xml_data)
        if len(response_data):
            content = ElementTree.fromstring(response_data).get("content")
            content_et = ElementTree.fromstring(content)
            _octane_version = content_et.get("octaneVersion")
            _octane_name = content_et.get("octaneName")
            is_demo = (content_et.get("isDemoVersion") == "true")
            is_studio = (content_et.get("isSubscriptionVersion") == "true")
            if is_demo:
                self.octane_version_type = consts.VersionType.DEMO
            elif is_studio:
                self.octane_version_type = consts.VersionType.STUDIO
            else:
                self.octane_version_type = consts.VersionType.PRIME
