#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

bl_info = {
    "name": "OctaneBlender (v. 27.7)",
    "author": "OTOY Inc.",
    "version": (27, 7),
    "blender": (3, 3, 0),
    "location": "Info header, render engine menu",
    "description": "OctaneBlender",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#60Octane%20for%20Blender",
    "tracker_url": "https://render.otoy.com/forum/viewforum.php?f=114",
    "support": 'OFFICIAL',
    "category": "Render"    
}

import bpy
import blf
import bgl
import array
import gpu
import numpy as np
import os
import time
from gpu_extras.presets import draw_texture_2d
from octane import version_update
from octane import core
from octane.core.client import OctaneBlender
from octane.utils import consts, utility


class OctaneRender(bpy.types.RenderEngine):
    bl_idname = 'octane'
    bl_label = "Octane"    
    bl_use_shading_nodes = True
    bl_use_shading_nodes_custom = False
    bl_use_preview = False
    bl_use_exclude_layers = True
    bl_use_save_buffers = True
    bl_use_spherical_stereo = True

    def __init__(self):
        self.session = None
        self.draw_data = None
        self.is_viewport_active = False
        self.is_octane_render_start = False
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.create_session()
      
    def __del__(self):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.free_session()
        else:
            engine.free(self)

    def create_session(self):
        from octane.core.session import RenderSession
        self.session = RenderSession(self)

    def free_session(self):
        try:
            if self.is_octane_render_start:
                self.is_octane_render_start = False
                if self.session.session_type == consts.SessionType.VIEWPORT:
                    self.session.stop_render()
            if self.session is not None:
                self.session.clear()
        except:
            pass

    # final render
    def update(self, data, depsgraph):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            return
        if not self.session:
            engine.create(self, data)
        engine.reset(self, data, depsgraph)

    def render(self, depsgraph):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.final_render(depsgraph)
        else:
            engine.render(self, depsgraph)

    def final_render(self, depsgraph):
        self.session.session_type = consts.SessionType.FINAL_RENDER
        self.is_octane_render_start = True
        scene = depsgraph.scene_eval
        width = utility.render_resolution_x(scene)
        height = utility.render_resolution_y(scene)
        for layer_index, layer in enumerate(scene.view_layers):
            dummy_result = self.begin_result(0, 0, 1, 1, layer=layer.name)
            if not layer.use:
                self.end_result(dummy_result, cancel=True, do_merge_results=False)
                continue
            self.end_result(dummy_result, cancel=True, do_merge_results=False)
            utility.add_render_passes(self, scene, layer)
            self.render_layer(depsgraph, scene, layer, width, height)
            if self.test_break():
                break
        self.is_octane_render_start = False

    def render_layer(self, depsgraph, scene, layer, width, height):
        start_time = time.time()
        # self.session.reset_render()
        # Init Scene
        self.session.start_render(is_viewport=False)
        init_time = time.time()
        init_elapsed_time = init_time - start_time
        self.update_stats("Init Time", "%.2f" % init_elapsed_time)
        # Sync Scene
        self.session.render_update(depsgraph, scene, layer)
        self.session.set_resolution(width, height)
        render_pass_ids = self.session.get_enabled_render_pass_ids(layer)
        self.session.set_render_pass_ids(render_pass_ids)
        sync_time = time.time()
        sync_elapsed_time = sync_time - init_time
        self.update_stats("Scene Synced Time", "%.2f" % sync_elapsed_time)
        statistics = {}
        pixel_num = width * height
        result = self.begin_result(0, 0, width, height)
        render_layer = result.layers[0]
        combined = render_layer.passes["Combined"]
        sample_status = ""
        while True:
            is_task_completed = False
            if OctaneBlender().get_render_result(consts.RenderPassId.BEAUTY, False, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, combined.as_pointer(), statistics):
                calculated_sample_per_pixel = statistics["calculated_sample_per_pixel"]
                tonemapped_sample_per_pixel = statistics["tonemapped_sample_per_pixel"]
                region_sample_per_pixel = statistics["region_sample_per_pixel"]
                max_sample = statistics["max_sample_per_pixel"]
                current_sample = max(calculated_sample_per_pixel, tonemapped_sample_per_pixel)
                sample_status = "Sample: %d/%d" % (current_sample, max_sample)                
                is_task_completed = current_sample >= max_sample
                self.update_result(result)
            render_time = time.time() 
            render_elapsed_time = render_time - sync_time
            time_status = "Render time: %s" % utility.time_human_readable_from_seconds(render_elapsed_time)
            if sample_status == "":
                self.update_stats("", "%s" % (time_status))
            else:
                self.update_stats("", "%s | %s" % (time_status, sample_status))
            if is_task_completed or self.test_break():
                break
            time.sleep(0.5)
        for render_pass in render_layer.passes:
            render_pass_id = utility.get_render_pass_id_by_legacy_render_pass_name(render_pass.name)
            if render_pass_id == consts.RenderPassId.BEAUTY:
                combined_np_array = np.empty(shape=(len(combined.rect), 4), dtype=np.float32)
                combined.rect.foreach_get(combined_np_array)
                render_pass.rect = combined_np_array              
            elif render_pass_id > consts.RenderPassId.BEAUTY:
                if render_pass.channels == 4:
                    if render_pass.name.startswith("OctDenoiser"):
                        while True:
                            if OctaneBlender().get_render_result(render_pass_id, False, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, render_pass.as_pointer(), statistics):
                                calculated_sample_per_pixel = statistics["calculated_sample_per_pixel"]
                                tonemapped_sample_per_pixel = statistics["tonemapped_sample_per_pixel"]
                                max_sample = statistics["max_sample_per_pixel"]
                                render_time = time.time() 
                                render_elapsed_time = render_time - sync_time
                                time_status = "Render time: %s" % utility.time_human_readable_from_seconds(render_elapsed_time)
                                sample_status = "Denoising Sample: %d/%d/%d" % (calculated_sample_per_pixel, tonemapped_sample_per_pixel, max_sample)
                                self.update_stats("", "%s | %s" % (time_status, sample_status))
                                if tonemapped_sample_per_pixel == max_sample:
                                    break                            
                            self.report({'INFO'}, "Wait for the Render Result of Pass %s. Samples: %d/%d" % (render_pass.name, tonemapped_sample_per_pixel, max_sample))
                            time.sleep(0.5)
                    else:
                        if not OctaneBlender().get_render_result(render_pass_id, False, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, render_pass.as_pointer(), statistics):
                            self.report({'ERROR'}, "Cannot Get the Render Result of Pass %s" % render_pass.name)
                elif render_pass.channels == 1:
                    if not OctaneBlender().get_render_result(render_pass_id, False, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_MONO, render_pass.as_pointer(), statistics):
                        self.report({'ERROR'}, "Cannot Get the Render Result of Pass %s" % render_pass.name)
            self.update_result(result)
        self.end_result(result)
        self.session.stop_render()

    def bake(self, depsgraph, obj, pass_type, pass_filter, width, height):
        pass

    # viewport render
    def view_update(self, context, depsgraph):
        # Update on data changes for viewport render
        if utility.is_multiple_viewport_rendering():
            self.report({'ERROR'}, "Multiple rendered viewports are active! Only one active render task is supported at the same time! Please turn off viewport shading and try again!")
            return        
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.session.session_type = consts.SessionType.VIEWPORT
            OctaneBlender().init_server()
            if not self.is_octane_render_start:
                self.session.start_render()
                self.is_octane_render_start = True
            self.session.view_update(self, depsgraph, context)
        else:
            if not self.session:
                engine.create(self, context.blend_data,
                              context.region, context.space_data, context.region_data)
                self._force_update_all_script_nodes()
            engine.reset(self, context.blend_data, depsgraph)
            engine.sync(self, depsgraph, context.blend_data)            

    def view_draw(self, context, depsgraph):
        # Draw viewport render
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.session.view_draw(depsgraph, context)
            region = context.region
            scene = depsgraph.scene
            self.draw_render_result(context.view_layer, region, scene)
        else:
            engine.draw(self, depsgraph, context.region, context.space_data, context.region_data)              

    def check_redraw(self):
        if self.draw_data:
            self.tag_redraw()

    def draw_render_result(self, view_layer, region, scene):
        if region:
            # Get viewport dimensions
            if not self.draw_data or self.draw_data.needs_replacement(region.width, region.height):
                self.draw_data = OctaneDrawData(region.width, region.height, self, scene)
        if self.draw_data:
            render_pass_id = self.session.get_current_preview_render_pass_id(view_layer)
            self.draw_data.update(render_pass_id, scene)
            self.draw_data.draw(self, scene)

    def _update_all_script_nodes(self, obj):
        if not getattr(obj, 'node_tree', None) or not getattr(obj.node_tree, 'nodes', None):
            return
        for node in obj.node_tree.nodes.values():
            if node.bl_idname == 'ShaderNodeGroup':
                self._update_all_script_nodes(node)
            if node.bl_idname in ('ShaderNodeOctOSLTex', 'ShaderNodeOctOSLCamera', 'ShaderNodeOctOSLBakingCamera', 'ShaderNodeOctOSLProjection', 'ShaderNodeOctVectron'):
                self.update_script_node(node)

    def _force_update_all_script_nodes(self):
        collections = (bpy.data.materials, bpy.data.textures, bpy.data.worlds)
        for collection in collections:        
            for obj in collection.values():
                self._update_all_script_nodes(obj)

    def update_script_node(self, node):
        from . import osl
        osl.update_script_node(node, self.report)

    def update_render_passes(self, scene=None, view_layer=None):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            utility.add_render_passes(self, scene, view_layer)
        else:
            engine.octane_register_passes(self, scene, view_layer)


class OctaneDrawData(object):
    def __init__(self, width, height, engine, scene):
        self.calculated_sample_per_pixel = 0
        self.tonemapped_sample_per_pixel = 0
        self.region_sample_per_pixel = 0
        self.current_change_level = 0
        self.max_sample = scene.octane.max_preview_samples
        self.statistics = {}
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0
        self.transparent = True
        if self.transparent:
            bufferdepth = 4
            self.buffertype = bgl.GL_RGBA
        else:
            bufferdepth = 3
            self.buffertype = bgl.GL_RGB
        self.buffer = bgl.Buffer(bgl.GL_FLOAT, [self.width * self.height * bufferdepth])
        self.init_opengl(engine, scene)

    def init_opengl(self, engine, scene):
        # Create texture
        self.texture = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenTextures(1, self.texture)
        self.texture_id = self.texture[0]

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
        width = self.width
        height = self.height
        position = [
            self.offset_x, self.offset_y,
            self.offset_x + width, self.offset_y,
            self.offset_x + width, self.offset_y + height,
            self.offset_x, self.offset_y + height
        ]
        position = bgl.Buffer(bgl.GL_FLOAT, len(position), position)
        texcoord = [0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0]
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

    def __del__(self):
        bgl.glDeleteBuffers(2, self.vertex_buffer)
        bgl.glDeleteVertexArrays(1, self.vertex_array)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)
        bgl.glDeleteTextures(1, self.texture)

    def needs_replacement(self, width, height):
        if self.width != width or self.height != height:
            return True
        return False

    def update(self, render_pass_id, scene):
        if OctaneBlender().get_render_result(render_pass_id, True, consts.RenderFrameDataType.RENDER_FRAME_FLOAT_RGBA, self.buffer, self.statistics):
            self.update_texture(scene)
            self.update_render_status(scene)

    def update_render_status(self, scene):
        self.calculated_sample_per_pixel = self.statistics["calculated_sample_per_pixel"]
        self.tonemapped_sample_per_pixel = self.statistics["tonemapped_sample_per_pixel"]
        self.region_sample_per_pixel = self.statistics["region_sample_per_pixel"]
        self.max_sample = self.statistics["max_sample_per_pixel"]
        self.current_change_level = self.statistics["change_level"]

    def draw(self, engine, scene):
        is_denoise_render_pass = utility.is_denoise_render_pass(self.statistics.get("render_pass_id"))
        if is_denoise_render_pass:
            msg = "Sample: %d/%d/%d, Render time: %.2f (sec)" % (self.calculated_sample_per_pixel, self.tonemapped_sample_per_pixel, self.max_sample, self.statistics.get("render_time", 0))
        else:
            msg = "Denoising Sample: %d/%d, Render time: %.2f (sec)" % (self.calculated_sample_per_pixel, self.max_sample, self.statistics.get("render_time", 0))
        engine.update_stats("Octane Render Statistics", msg)

        if self.calculated_sample_per_pixel == 0 and self.tonemapped_sample_per_pixel == 0:
            return

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

        if self.transparent:
            bgl.glDisable(bgl.GL_BLEND)

    def update_texture(self, scene):
        if self.transparent:
            gl_format = bgl.GL_RGBA
            internal_format = bgl.GL_RGBA32F
        else:
            gl_format = bgl.GL_RGB
            internal_format = bgl.GL_RGB32F

        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.texture_id)
        bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, internal_format, self.width, self.height,
                         0, gl_format, bgl.GL_FLOAT, self.buffer)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_S, bgl.GL_CLAMP_TO_EDGE)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_WRAP_T, bgl.GL_CLAMP_TO_EDGE)

        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, 0)


classes = (
    OctaneRender,
)


def register():
    from bpy.utils import register_class    

    path = os.path.dirname(__file__)
    user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', path='')))
    OctaneBlender().init(path, user_path)

    from octane import properties
    properties.register()

    from octane import properties_
    from octane import uis    
    from octane import nodes
    from octane import ui
    from octane import operators    
    from octane import presets
    from octane import engine    
    properties_.register()    
    uis.register()
    nodes.register()
    
    ui.register()
    operators.register()
    presets.register()

    for cls in classes:
        register_class(cls)

    bpy.app.handlers.version_update.append(version_update.do_versions)
    bpy.app.handlers.load_post.append(operators.clear_resource_cache_system)
    bpy.app.handlers.depsgraph_update_post.append(operators.sync_octane_aov_output_number)
    bpy.app.handlers.depsgraph_update_post.append(operators.update_resource_cache_tag)
    bpy.app.handlers.depsgraph_update_post.append(operators.update_blender_volume_grid_info)


def unregister():
    from bpy.utils import unregister_class
    from octane import properties
    from octane import properties_
    from octane import uis    
    from octane import nodes
    from octane import ui
    from octane import operators    
    from octane import presets
    from octane import engine

    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        import _octane
        _octane.command_to_octane(operators.COMMAND_TYPES['CLEAR_RESOURCE_CACHE_SYSTEM'])
    OctaneBlender().exit()

    bpy.app.handlers.version_update.remove(version_update.do_versions)
    bpy.app.handlers.load_post.remove(operators.clear_resource_cache_system)
    bpy.app.handlers.depsgraph_update_post.remove(operators.sync_octane_aov_output_number)
    bpy.app.handlers.depsgraph_update_post.remove(operators.update_resource_cache_tag)
    bpy.app.handlers.depsgraph_update_post.remove(operators.update_blender_volume_grid_info)
    
    properties_.unregister()
    properties.unregister()
    uis.unregister()
    nodes.unregister()

    ui.unregister()
    operators.unregister()    
    presets.unregister()

    for cls in classes:
        unregister_class(cls)
