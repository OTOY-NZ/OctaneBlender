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
    "name": "OctaneRender Engine (v. 20.4)",
    "author": "OTOY Inc.",
    "blender": (2, 80, 0),
    "location": "Info header, render engine menu",
    "description": "OctaneRender Engine integration",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#60Octane%20for%20Blender",
    "tracker_url": "",
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

from . import (
    engine,
    version_update
)


class OctaneRender(bpy.types.RenderEngine):
    bl_idname = 'octane'
    bl_label = "Octane"
    bl_use_shading_nodes = True
    bl_use_preview = True
    bl_use_exclude_layers = True
    bl_use_save_buffers = True
    bl_use_spherical_stereo = True

    def __init__(self):
        self.session = None
        self.is_viewport_active = False

    def __del__(self):        
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

    def bake(self, depsgraph, obj, pass_type, pass_filter, object_id, pixel_array, num_pixels, depth, result):
        pass

    # viewport render
    def view_update(self, context, depsgraph):
        if not self.check_active_status():
            self.report({'ERROR'}, "Viewport shading is active! Only one active render task is supported at the same time! Please turn off viewport shading and try again!")
            return
        if not self.session:
            engine.create(self, context.blend_data,
                          context.region, context.space_data, context.region_data)
            self._force_update_all_script_nodes()

        engine.reset(self, context.blend_data, depsgraph)        
        engine.sync(self, depsgraph, context.blend_data)

    def view_draw(self, context, depsgraph):
        if not self.check_active_status():
            self.report({'ERROR'}, "Viewport shading is active! Only one active render task is supported at the same time! Please turn off viewport shading and try again!")
            return
        engine.draw(self, depsgraph, context.region, context.space_data, context.region_data)

    def _update_all_script_nodes(self, obj):
        if not getattr(obj, 'node_tree', None) or not getattr(obj.node_tree, 'nodes', None):
            return
        for node in obj.node_tree.nodes.values():
            if node.bl_idname == 'ShaderNodeGroup':
                self._update_all_script_nodes(node)
            if node.bl_idname in ('ShaderNodeOctOSLTex', 'ShaderNodeOctOSLCamera', 'ShaderNodeOctOSLBakingCamera', 'ShaderNodeOctOSLProjection', 'ShaderNodeOctVectron'):
                self.update_script_node(node)

    def _force_update_all_script_nodes(self):
        collections = (bpy.data.materials, bpy.data.textures, )
        for collection in collections:        
            for obj in collection.values():
                self._update_all_script_nodes(obj)

    def update_script_node(self, node):
        from . import osl
        osl.update_script_node(node, self.report)

    def update_render_passes(self, scene, srl):
        engine.register_passes(self, scene, srl)


def engine_exit():
    engine.exit()


classes = (
    OctaneRender,
)


def register():
    from bpy.utils import register_class
    from . import ui
    from . import operators
    from . import properties
    from . import presets
    import atexit

    # Make sure we only registered the callback once.
    atexit.unregister(engine_exit)
    atexit.register(engine_exit)

    engine.init()

    properties.register()
    ui.register()
    operators.register()
    presets.register()

    for cls in classes:
        register_class(cls)

    bpy.app.handlers.version_update.append(version_update.do_versions)


def unregister():
    from bpy.utils import unregister_class
    from . import ui
    from . import operators
    from . import properties
    from . import presets
    import atexit

    bpy.app.handlers.version_update.remove(version_update.do_versions)

    ui.unregister()
    operators.unregister()
    properties.unregister()
    presets.unregister()

    for cls in classes:
        unregister_class(cls)
