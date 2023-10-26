import bgl
import gpu
import time
from gpu_extras.batch import batch_for_shader
from gpu_extras.presets import draw_texture_2d
from octane import core
from octane.core.client import OctaneBlender
from octane.utils import consts, utility
octane_blender = core.get_octane_blender_binary_module()


class ViewportDrawData(object):
    ENABLE_PROFILE = True
    ENABLE_MULTITHREAD = False
    MULTITHRAD_MIN_UPDATE_GAP = 0.03

    def __init__(self, render_pass_id, width, height, engine, scene, use_shared_surface):
        self.transparent = True
        if self.transparent:
            bufferdepth = 4
        else:
            bufferdepth = 3
        if use_shared_surface:
            self.texture_id = 0
            self.buffer = None
        else:
            self.texture_id = None
            self.buffer = gpu.types.Buffer("FLOAT", [width * height * bufferdepth])
        self.frame_buffer = octane_blender.FrameBuffer(render_pass_id, True, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, width, height, use_shared_surface, self.buffer)
        self.enable_multithread = self.ENABLE_MULTITHREAD and not use_shared_surface
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            OctaneBlender().update_mt_render_fetcher_settings(self.enable_multithread, self.MULTITHRAD_MIN_UPDATE_GAP)
        self.immediate_fetch = False
        self.offset_x = 0
        self.offset_y = 0
        self.last_render_pass_id = -1
        self.max_sample = scene.octane.max_preview_samples
        self.init(engine, scene)
        # Profile data
        self.total_update_count = 0
        self.render_result_update_count = 0
        self.total_update_time = 0
        self.render_result_update_time = 0

    def init(self, engine, scene):
        frame_buffer = self.frame_buffer
        width = frame_buffer.width
        height = frame_buffer.height        
        if frame_buffer.use_shared_surface:
            # Bind shader that converts from scene linear to display space,
            # use the scene's color management settings.
            engine.bind_display_space_shader(scene)
            shader_program = bgl.Buffer(bgl.GL_INT, 1)
            bgl.glGetIntegerv(bgl.GL_CURRENT_PROGRAM, shader_program)
            # Generate vertex array
            self.vertex_array = bgl.Buffer(bgl.GL_INT, 1)
            bgl.glGenVertexArrays(1, self.vertex_array)
            bgl.glBindVertexArray(self.vertex_array[0])
            texturecoord_location = bgl.glGetAttribLocation(shader_program[0], "texCoord")
            position_location = bgl.glGetAttribLocation(shader_program[0], "pos")
            bgl.glEnableVertexAttribArray(texturecoord_location)
            bgl.glEnableVertexAttribArray(position_location)
            # Generate geometry buffers for drawing textured quad
            position = [
                self.offset_x, self.offset_y,
                self.offset_x + width, self.offset_y,
                self.offset_x + width, self.offset_y + height,
                self.offset_x, self.offset_y + height
            ]
            position = bgl.Buffer(bgl.GL_FLOAT, len(position), position)
            texcoord = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
            texcoord = bgl.Buffer(bgl.GL_FLOAT, len(texcoord), texcoord)
            self.vertex_buffer = bgl.Buffer(bgl.GL_INT, 2)
            bgl.glGenBuffers(2, self.vertex_buffer)
            bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, self.vertex_buffer[0])
            bgl.glBufferData(bgl.GL_ARRAY_BUFFER, 32, position, bgl.GL_STATIC_DRAW)
            bgl.glVertexAttribPointer(position_location, 2, bgl.GL_FLOAT, bgl.GL_FALSE, 0, None)
            bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, self.vertex_buffer[1])
            bgl.glBufferData(bgl.GL_ARRAY_BUFFER, 32, texcoord, bgl.GL_STATIC_DRAW)
            bgl.glVertexAttribPointer(texturecoord_location, 2, bgl.GL_FLOAT, bgl.GL_FALSE, 0, None)
            bgl.glBindBuffer(bgl.GL_ARRAY_BUFFER, 0)
            bgl.glBindVertexArray(0)
            engine.unbind_display_space_shader()
        else:
            position = [
                (self.offset_x, self.offset_y),
                (self.offset_x + width, self.offset_y),
                (self.offset_x + width, self.offset_y + height),
                (self.offset_x, self.offset_y + height)
            ]
            self.shader = gpu.shader.from_builtin("2D_IMAGE")
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
                msg = "Sample: %d/%d/%d, Render time: %.2f (sec)" % (self.frame_buffer.calculated_samples_per_pixel, self.frame_buffer.tonemapped_samples_per_pixel, self.max_sample, self.frame_buffer.render_time)
            else:
                msg = "Denoising Sample: %d/%d, Render time: %.2f (sec)" % (self.frame_buffer.calculated_samples_per_pixel, self.max_sample, self.frame_buffer.render_time)
            print("Render Status: \nResolution: %d, %d\n%s\nUse Shared Surface: %d" % (self.frame_buffer.width, self.frame_buffer.height, msg, self.frame_buffer.use_shared_surface))
            print("Multithread: %d" % self.enable_multithread)
            print("Total Update Data: %.2f ms, %d, %.2f ms" % (self.total_update_time, self.total_update_count, (self.total_update_time / self.total_update_count) if self.total_update_count > 0 else 0))
            print("Render Result Update Data: %.2f ms, %d, %.2f ms" % (self.render_result_update_time, self.render_result_update_count, (self.render_result_update_time / self.render_result_update_count) if self.render_result_update_count > 0 else 0))        
        if self.frame_buffer.use_shared_surface:
            pass
        else:
            del self.buffer
        self.frame_buffer = None

    def free(self, engine):
        if self.frame_buffer.use_shared_surface:
            bgl.glDeleteBuffers(2, self.vertex_buffer)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)

    def tag_immediate_fetch(self, immediate_fetch):
        self.immediate_fetch = immediate_fetch

    def needs_replacement(self, width, height, use_shared_surface):
        if self.frame_buffer.width != width or self.frame_buffer.height != height or self.frame_buffer.use_shared_surface != use_shared_surface:
            return True
        return False

    def update(self, render_pass_id, scene):
        is_render_result_updated = False
        force_fetch = self.last_render_pass_id != render_pass_id
        self.last_render_pass_id = render_pass_id
        if self.ENABLE_PROFILE:
            self.total_update_count += 1
            start_time = time.time()
        self.frame_buffer.set_render_pass_id(render_pass_id)
        OctaneBlender().use_shared_surface(self.frame_buffer.use_shared_surface)
        immediate_fetch = not self.enable_multithread # or self.immediate_fetch
        if self.frame_buffer.update_render_result(force_fetch, immediate_fetch):
            if self.frame_buffer.use_shared_surface:
                self.update_texture_shared_surface()
            else:
                self.update_texture()
            self.update_statistics()
            is_render_result_updated = True
        if self.ENABLE_PROFILE:
            end_time = time.time()
            time_eslapse = (end_time - start_time) * 1000
            self.total_update_time += time_eslapse
            if is_render_result_updated:
                self.render_result_update_count += 1
                self.render_result_update_time += time_eslapse

    def draw(self, engine, scene):
        render_pass_id = self.frame_buffer.get_render_pass_id()
        is_denoise_render_pass = utility.is_denoise_render_pass(render_pass_id)
        is_scene_inited = OctaneBlender().get_scene_state() == consts.SceneState.INITIALIZED
        if is_scene_inited:
            if is_denoise_render_pass:
                sample_msg = "Denoising Sample: %d/%d/%d, Render time: %.2f (sec)" % (self.frame_buffer.calculated_samples_per_pixel, self.frame_buffer.tonemapped_samples_per_pixel, self.max_sample, self.frame_buffer.render_time)
            else:
                sample_msg = "Sample: %d/%d, Render time: %.2f (sec)" % (self.frame_buffer.calculated_samples_per_pixel, self.max_sample, self.frame_buffer.render_time)
        else:
            sample_msg = OctaneBlender().get_status_msg()
        used_memory = int(self.frame_buffer.used_memory / 1048576.0)
        free_memory = int(self.frame_buffer.free_memory / 1048576.0)
        total_memory = int(self.frame_buffer.total_memory / 1048576.0)
        msg = "Mem: %dM/%dM/%dM, Meshes: %d, Tris: %d | Tex: (Rgb32: %d, Rgb64: %d, grey8: %d, grey16: %d)" \
            % (used_memory, free_memory, total_memory, self.frame_buffer.instance_count, self.frame_buffer.tri_count, self.frame_buffer.used_rgba32_textures, self.frame_buffer.used_rgba64_textures, self.frame_buffer.used_y8_textures, self.frame_buffer.used_y16_Textures)
        msg = sample_msg + "\n" + msg
        if not is_scene_inited:
            if getattr(engine, "session", None):
                elapsed_time = engine.session.get_elapsed_time()
                elapsed_time_msg = utility.time_human_readable_from_seconds(elapsed_time)
                elapsed_time_msg = "Elapsed time: "+ elapsed_time_msg
                msg = msg + "\n"+ elapsed_time_msg
        engine.update_stats("Octane Render Statistics", msg)
        if not is_scene_inited:
            return
        if self.frame_buffer.calculated_samples_per_pixel == 0 and self.frame_buffer.tonemapped_samples_per_pixel == 0:
            return
        if self.frame_buffer.use_shared_surface:
            if self.transparent:
                bgl.glEnable(bgl.GL_BLEND)
                bgl.glBlendFunc(bgl.GL_ONE, bgl.GL_ONE_MINUS_SRC_ALPHA)
            engine.bind_display_space_shader(scene)
            bgl.glActiveTexture(bgl.GL_TEXTURE0)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture_id)
            bgl.glBindVertexArray(self.vertex_array[0])
            bgl.glDrawArrays(bgl.GL_TRIANGLE_FAN, 0, 4)
            bgl.glBindVertexArray(0)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)
            engine.unbind_display_space_shader()
            err = bgl.glGetError()
            if err != bgl.GL_NO_ERROR:
                print("GL Error:", err)
        else:
            if self.transparent:
                _format = "RGBA16F"
            else:
                _format = "RGB16F"            
            image = gpu.types.GPUTexture(size=(self.frame_buffer.width, self.frame_buffer.height), layers=0, is_cubemap=False, format=_format, data=self.buffer)
            self.shader.uniform_sampler("image", image)
            self.batch.draw(self.shader)

    def update_statistics(self):
        self.max_sample = self.frame_buffer.max_samples_per_pixel

    def update_texture(self):
        pass

    def update_texture_shared_surface(self, texture_id=None):
        if texture_id is None:
            texture_id = self.frame_buffer.gl_texture
        if self.texture_id != texture_id:
            self.texture_id = texture_id
            bgl.glActiveTexture(bgl.GL_TEXTURE0)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture_id)
            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_S, bgl.GL_CLAMP_TO_EDGE)
            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_T, bgl.GL_CLAMP_TO_EDGE)
            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
            bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST)
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)


class RenderDrawData(object):
    ENABLE_PROFILE = False

    def __init__(self, render_pass_id, frame_data_type, width, height, render_pass):
        self.frame_buffer = octane_blender.FrameBuffer(render_pass_id, False, frame_data_type, width, height, False, render_pass.as_pointer())

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
