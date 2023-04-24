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
    "name": "OctaneRender Engine (v. 26.3)",
    "author": "OTOY Inc.",
    "blender": (3, 1, 2),
    "location": "Info header, render engine menu",
    "description": "OctaneRender Engine integration",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#60Octane%20for%20Blender",
    "tracker_url": "https://render.otoy.com/forum/viewforum.php?f=114",
    "support": 'OFFICIAL',
    "category": "Render"}

# Support 'reload' case.
if "bpy" in locals():
    import importlib
    if "engine" in locals():
        importlib.reload(engine)
    if "version_update" in locals():
        importlib.reload(version_update)        
    if "ui" in locals():
        importlib.reload(ui)
    if "operators" in locals():
        importlib.reload(operators)
    if "properties" in locals():
        importlib.reload(properties)
    if "presets" in locals():
        importlib.reload(presets)

import bpy
import blf
import bgl
import array
import gpu
import numpy as np
from gpu_extras.presets import draw_texture_2d

from . import (
    engine,
    version_update,    
)

from octane import core
from octane.core.client import OctaneClient
from octane.utils import consts

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
        self.addon_session = OctaneClient().create_session()
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.draw_data = OctaneDrawData((1, 1))
        self.is_viewport_active = False
        self.need_reset_render = True

    def __del__(self):
        if getattr(self, "addon_session", None):
            OctaneClient().free_session(self.addon_session)
            self.addon_session = None     
        engine.free(self)

    def check_active_status(self):
        if not self.is_viewport_active:
            if self.is_other_viewport_rendering_active():
                self.is_viewport_active = False                
            else:
                self.is_viewport_active = True
        return self.is_viewport_active

    def is_other_viewport_rendering_active(self):
        counter = 0
        for area in bpy.context.screen.areas:
            if area.type != "VIEW_3D":
                continue
            for space in area.spaces:
                if space.type != "VIEW_3D":
                    continue
                if space.shading.type == "RENDERED":
                    counter += 1
        return counter > 1

    # final render
    def update(self, data, depsgraph):
        if not self.session:
            engine.create(self, data)
        engine.reset(self, data, depsgraph)

    def render(self, depsgraph):        
        engine.render(self, depsgraph)

    def bake(self, depsgraph, obj, pass_type, pass_filter, width, height):
        pass

    # viewport render
    def view_update(self, context, depsgraph):
        oct_scene = context.scene.octane
        # Legacy updates
        if not core.ENABLE_OCTANE_ADDON_CLIENT or oct_scene.legacy_mode_enabled:
            if not self.check_active_status():
                self.report({'ERROR'}, "Viewport shading is active! Only one active render task is supported at the same time! Please turn off viewport shading and try again!")
                return
            if not self.session:
                engine.create(self, context.blend_data,
                              context.region, context.space_data, context.region_data)
                self._force_update_all_script_nodes()
            engine.reset(self, context.blend_data, depsgraph)
            engine.sync(self, depsgraph, context.blend_data)
        # Add-on mode updates
        if core.ENABLE_OCTANE_ADDON_CLIENT and oct_scene.addon_dev_enabled:
            self.addon_session.session_type = consts.SessionType.VIEWPORT
            need_reset_and_start_render = False
            if self.need_reset_render:
                self.need_reset_render = False
                need_reset_and_start_render = True
            if need_reset_and_start_render:
                self.addon_session.reset_render(self, context, depsgraph, True)
            self.addon_session.view_update(self, context, depsgraph)
            if need_reset_and_start_render:
                self.addon_session.start_render(self, context, depsgraph)            

    def view_draw(self, context, depsgraph):
        if not self.check_active_status():
            self.report({'ERROR'}, "Viewport shading is active! Only one active render task is supported at the same time! Please turn off viewport shading and try again!")
            return
        # Add-on mode updates
        oct_scene = context.scene.octane
        if core.ENABLE_OCTANE_ADDON_CLIENT and oct_scene.addon_dev_enabled:
            self.addon_session.view_draw(self, context, depsgraph)            
            region = context.region
            scene = depsgraph.scene
            self.draw_render_result(self.addon_session.render_result, region, scene)
        else:
            engine.draw(self, depsgraph, context.region, context.space_data, context.region_data)                

    def draw_render_result(self, render_result, region=None, scene=None):
        if region:
            # Get viewport dimensions
            dimensions = region.width, region.height
            if not self.draw_data or self.draw_data.dimensions != dimensions:
                self.draw_data = OctaneDrawData(dimensions)
        if self.draw_data:
            if scene is None:
                scene = bpy.context.scene
            # Bind shader that converts from scene linear to display space
            gpu.state.blend_set('ALPHA_PREMULT')
            self.bind_display_space_shader(scene)            
            self.draw_data.update(render_result)
            self.draw_data.draw()
            self.unbind_display_space_shader()
            gpu.state.blend_set('NONE')

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

    def update_render_passes(self, scene=None, renderlayer=None):
        engine.octane_register_passes(self, scene, renderlayer)


class OctaneDrawData(object):
    def __init__(self, dimensions):
        # Generate dummy float image buffer
        self.dimensions = dimensions
        width, height = dimensions
        # Generate texture
        self.texture = gpu.types.GPUTexture((width, height), format='RGBA16F')

    def __del__(self):
        del self.texture

    def update(self, render_result):
        width, height = self.dimensions
        pixel_size = width * height * 4
        if width != render_result.resolution[0] or height != render_result.resolution[1]:
            return
        render_result.lock_render_result()
        if render_result.viewport_float_pixel_array is None or len(render_result.viewport_float_pixel_array) != pixel_size:
            render_result.unlock_render_result() 
            return
        pixels = gpu.types.Buffer('FLOAT', pixel_size, render_result.viewport_float_pixel_array)        
        self.texture = gpu.types.GPUTexture((width, height), format='RGBA16F', data=pixels)
        render_result.unlock_render_result()        

    def draw(self):
        draw_texture_2d(self.texture, (0, 0), self.texture.width, self.texture.height)


classes = (
    OctaneRender,
)


def register():
    from bpy.utils import register_class
    from . import properties_
    from . import uis    
    from . import nodes

    from . import ui
    from . import operators
    from . import properties
    from . import presets    
    from . import engine    

    OctaneClient().start()
    engine.init()    

    properties_.register()
    uis.register()
    nodes.register()

    properties.register()
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
    from . import properties_
    from . import uis    
    from . import nodes

    from . import ui
    from . import operators
    from . import properties
    from . import presets

    OctaneClient().stop()
    engine.exit()

    bpy.app.handlers.version_update.remove(version_update.do_versions)
    bpy.app.handlers.load_post.remove(operators.clear_resource_cache_system)
    bpy.app.handlers.depsgraph_update_post.remove(operators.sync_octane_aov_output_number)
    bpy.app.handlers.depsgraph_update_post.remove(operators.update_resource_cache_tag)
    bpy.app.handlers.depsgraph_update_post.remove(operators.update_blender_volume_grid_info)
    
    properties_.unregister()
    uis.unregister()
    nodes.unregister()

    ui.unregister()
    operators.unregister()
    properties.unregister()
    presets.unregister()

    for cls in classes:
        unregister_class(cls)
