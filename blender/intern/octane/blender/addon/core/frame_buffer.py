# <pep8 compliant>

import time
import gpu
from gpu_extras.batch import batch_for_shader
from octane import core
from octane.core.client import OctaneBlender
from octane.utils import consts, utility

octane_blender = core.get_octane_blender_binary_module()


class ViewportDrawData(object):
    ENABLE_PROFILE = True
    ENABLE_MULTITHREAD = False
    MULTITHREADING_MIN_UPDATE_GAP = 0.03

    def __init__(self, is_demo, render_pass_id, width, height, _engine, scene, use_shared_surface):
        self.shader = None
        self.batch = None
        self.is_demo = is_demo
        self.transparent = True
        if self.transparent:
            buffer_depth = 4
        else:
            buffer_depth = 3
        if use_shared_surface:
            self.texture_id = 0
            self.buffer = None
        else:
            self.texture_id = None
            self.buffer = gpu.types.Buffer("FLOAT", [width * height * buffer_depth])
        self.frame_buffer = octane_blender.FrameBuffer(render_pass_id, True,
                                                       consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA,
                                                       width, height, use_shared_surface, self.buffer)
        self.enable_multithread = self.ENABLE_MULTITHREAD and not use_shared_surface
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            OctaneBlender().update_mt_render_fetcher_settings(self.enable_multithread,
                                                              self.MULTITHREADING_MIN_UPDATE_GAP)
        self.immediate_fetch = False
        self.offset_x = 0
        self.offset_y = 0
        self.last_render_pass_id = -1
        self.max_sample = scene.octane.max_preview_samples
        self.init()
        # Profile data
        self.total_update_count = 0
        self.render_result_update_count = 0
        self.total_update_time = 0
        self.render_result_update_time = 0

    def init(self):
        frame_buffer = self.frame_buffer
        width = frame_buffer.width
        height = frame_buffer.height
        if frame_buffer.use_shared_surface:
            data = [
                self.offset_x, self.offset_y, 0.0, 1.0,
                self.offset_x + width, self.offset_y, 1.0, 1.0,
                self.offset_x + width, self.offset_y + height, 1.0, 0.0,
                self.offset_x, self.offset_y + height, 0.0, 0.0,
            ]
            self.frame_buffer.init(data)
        else:
            position = [
                (self.offset_x, self.offset_y),
                (self.offset_x + width, self.offset_y),
                (self.offset_x + width, self.offset_y + height),
                (self.offset_x, self.offset_y + height)
            ]
            self.shader = gpu.shader.from_builtin("IMAGE")
            self.batch = batch_for_shader(
                self.shader, "TRI_FAN",
                {
                    "pos": position,
                    "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                },
            )

    def __del__(self):
        if self.ENABLE_PROFILE:
            render_pass_id = self.frame_buffer.get_render_pass_id()
            is_denoise_render_pass = utility.is_denoise_render_pass(render_pass_id)
            if is_denoise_render_pass:
                msg = "Sample: %d/%d/%d, Render time: %.2f (sec)" % (self.frame_buffer.calculated_samples_per_pixel,
                                                                     self.frame_buffer.tonemapped_samples_per_pixel,
                                                                     self.max_sample, self.frame_buffer.render_time)
            else:
                msg = ("Denoising Sample: %d/%d, Render time: %.2f (sec)" %
                       (self.frame_buffer.calculated_samples_per_pixel,
                        self.max_sample,
                        self.frame_buffer.render_time))
            print("Render Status: \nResolution: %d, %d\n%s\nUse Shared Surface: %d" %
                  (self.frame_buffer.width, self.frame_buffer.height,
                   msg, self.frame_buffer.use_shared_surface))
            print("Multithread: %d" % self.enable_multithread)
            print("Total Update Data: %.2f ms, %d, %.2f ms" %
                  (self.total_update_time, self.total_update_count,
                   (self.total_update_time / self.total_update_count) if self.total_update_count > 0 else 0))
            if self.render_result_update_count > 0:
                per_update_time = self.render_result_update_time / self.render_result_update_count
            else:
                per_update_time = 0
            print("Render Result Update Data: %.2f ms, %d, %.2f ms" %
                  (self.render_result_update_time, self.render_result_update_count, per_update_time))
        if self.frame_buffer.use_shared_surface:
            self.frame_buffer.deinit()
        else:
            del self.buffer
        self.frame_buffer = None

    def free(self, engine):
        pass

    def tag_immediate_fetch(self, immediate_fetch):
        self.immediate_fetch = immediate_fetch

    def needs_replacement(self, width, height, use_shared_surface):
        if (self.frame_buffer.width != width or self.frame_buffer.height != height
                or self.frame_buffer.use_shared_surface != use_shared_surface):
            return True
        return False

    def update(self, render_pass_id):
        is_render_result_updated = False
        force_fetch = self.last_render_pass_id != render_pass_id
        self.last_render_pass_id = render_pass_id
        if self.ENABLE_PROFILE:
            self.total_update_count += 1
            start_time = time.time()
        self.frame_buffer.set_render_pass_id(render_pass_id)
        OctaneBlender().use_shared_surface(self.frame_buffer.use_shared_surface)
        immediate_fetch = not self.enable_multithread  # or self.immediate_fetch
        if self.frame_buffer.update_render_result(force_fetch, immediate_fetch):
            self.update_statistics()
            is_render_result_updated = True
        if self.ENABLE_PROFILE:
            end_time = time.time()
            # noinspection PyUnboundLocalVariable
            time_elapse = (end_time - start_time) * 1000
            self.total_update_time += time_elapse
            if is_render_result_updated:
                self.render_result_update_count += 1
                self.render_result_update_time += time_elapse

    def draw(self, engine, scene):
        if not (getattr(engine, "is_active", False) and getattr(getattr(engine, "session", None), "is_render_started", False)):
            return
        is_demo_limited = self.is_demo
        if is_demo_limited:
            if self.frame_buffer.width <= 1000 and self.frame_buffer.height <= 600:
                is_demo_limited = False
        render_pass_id = self.frame_buffer.get_render_pass_id()
        is_denoise_render_pass = utility.is_denoise_render_pass(render_pass_id)
        is_scene_inited = OctaneBlender().get_scene_state() == consts.SceneState.INITIALIZED
        if is_scene_inited:
            if is_denoise_render_pass:
                sample_msg = "Denoising Sample: %d/%d/%d, Render time: %.2f (sec)" % (
                    self.frame_buffer.calculated_samples_per_pixel, self.frame_buffer.tonemapped_samples_per_pixel,
                    self.max_sample, self.frame_buffer.render_time)
            else:
                sample_msg = "Sample: %d/%d, Render time: %.2f (sec)" % (
                    self.frame_buffer.calculated_samples_per_pixel, self.max_sample, self.frame_buffer.render_time)
        else:
            sample_msg = OctaneBlender().get_status_msg()
        used_memory = int(self.frame_buffer.used_memory / 1048576.0)
        free_memory = int(self.frame_buffer.free_memory / 1048576.0)
        total_memory = int(self.frame_buffer.total_memory / 1048576.0)
        msg = "Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: (Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d)" \
              % (used_memory, free_memory, total_memory, self.frame_buffer.instance_count, self.frame_buffer.tri_count,
                 self.frame_buffer.used_rgba32_textures, self.frame_buffer.used_rgba64_textures,
                 self.frame_buffer.used_y8_textures, self.frame_buffer.used_y16_Textures)
        msg = sample_msg + "\n" + msg
        if not is_scene_inited:
            if getattr(engine, "session", None):
                elapsed_time = engine.session.get_elapsed_time()
                elapsed_time_msg = utility.time_human_readable_from_seconds(elapsed_time)
                elapsed_time_msg = "Elapsed time: " + elapsed_time_msg
                msg = msg + "\n" + elapsed_time_msg
        if is_demo_limited:
            msg = ("Demo version does not support the current resolution. Please use smaller resolutions(< 1000 * 600) "
                   "and try again.")
            engine.update_stats("Octane Render Statistics", msg)
            return
        else:
            engine.update_stats("Octane Render Statistics", msg)
        if not is_scene_inited:
            return
        if self.frame_buffer.calculated_samples_per_pixel == 0 and self.frame_buffer.tonemapped_samples_per_pixel == 0:
            return
        if self.frame_buffer.use_shared_surface:
            if abs(self.frame_buffer.width - self.frame_buffer.gl_texture_width) > 64 or abs(
                    self.frame_buffer.height - self.frame_buffer.gl_texture_height) > 64:
                return
        if self.frame_buffer.use_shared_surface:
            engine.bind_display_space_shader(scene)
            error = self.frame_buffer.draw(self.transparent)
            engine.unbind_display_space_shader()
            if error != 0:  # GL_NO_ERROR
                print("GL Error:", error)
        else:
            if self.transparent:
                _format = "RGBA16F"
            else:
                _format = "RGB16F"
            image = gpu.types.GPUTexture(size=(self.frame_buffer.width, self.frame_buffer.height), layers=0,
                                         is_cubemap=False, format=_format, data=self.buffer)
            self.shader.uniform_sampler("image", image)
            self.batch.draw(self.shader)

    def update_statistics(self):
        self.max_sample = self.frame_buffer.max_samples_per_pixel


class RenderDrawData(object):
    ENABLE_PROFILE = False

    def __init__(self, render_pass_id, frame_data_type, width, height, render_pass):
        self.frame_buffer = octane_blender.FrameBuffer(render_pass_id, False, frame_data_type, width, height, False,
                                                       render_pass.as_pointer())

    def update_render_result(self, force_fetch):
        return self.frame_buffer.update_render_result(force_fetch, True)

    @property
    def calculated_samples_per_pixel(self):
        return self.frame_buffer.calculated_samples_per_pixel

    @property
    def tonemapped_samples_per_pixel(self):
        return self.frame_buffer.tonemapped_samples_per_pixel

    @property
    def region_samples_per_pixel(self):
        return self.frame_buffer.region_samples_per_pixel

    @property
    def max_samples_per_pixel(self):
        return self.frame_buffer.max_samples_per_pixel
