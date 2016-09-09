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

import bpy

from bpy.types import Panel, Menu, Operator

from . import types, engine

class SetMeshesType(Operator):
    """Set selected meshes to the same type"""
    bl_idname = "octane.set_meshes_type"
    bl_label = "To selected"
    bl_register = True
    bl_undo = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        data = context.blend_data
        sel_len = len(bpy.context.selected_objects)
        if sel_len > 1:
            _octane.set_meshes_type(data.as_pointer(), int(bpy.context.object.data.octane.mesh_type))
        return {'FINISHED'}

class Reset(Operator):
    """Reload scene"""
    bl_idname = "octane.reload"
    bl_label = "Reload"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        _octane.reload(types.OctaneRender.session)
        return {'FINISHED'}

class ActivateOctane(Operator):
    """Activate the Octane license"""
    bl_idname = "octane.activate"
    bl_label = "Open activation state dialog on OctaneServer"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        _octane.activate(bpy.context.scene.as_pointer())
        return {'FINISHED'}


class OCTANE_MT_kernel_presets(Menu):
    bl_label = "Kernel presets"
    preset_subdir = "octane/kernel"
    preset_operator = "script.execute_preset"
    COMPAT_ENGINES = {'octane'}
    draw = Menu.draw_preset


class OCTANE_MT_environment_presets(Menu):
    bl_label = "Environment presets"
    preset_subdir = "octane/environment"
    preset_operator = "script.execute_preset"
    COMPAT_ENGINES = {'octane'}
    draw = Menu.draw_preset

class OCTANE_MT_imager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/imager_presets"
    preset_operator = "script.execute_preset"
    COMPAT_ENGINES = {'octane'}
    draw = Menu.draw_preset

class OCTANE_MT_3dimager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/3dimager_presets"
    preset_operator = "script.execute_preset"
    COMPAT_ENGINES = {'octane'}
    draw = Menu.draw_preset


class OctaneButtonsPanel():
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"

    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return rd.engine == 'octane'


class VIEW3D_PT_octcam(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane camera"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.space_data and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        view = context.space_data
        oct_cam = context.scene.oct_view_cam

        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dimager_presets", text=bpy.types.OCTANE_MT_3dimager_presets.bl_label)
        row.operator("render.octane_3dimager_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_3dimager_preset_add", text="", icon="ZOOMOUT").remove_active = True

        layout.active = bool(view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        sub = layout.column(align=True)
        sub.prop(oct_cam, "response_type", text="Response type")

        sub = layout.column(align=True)
        sub.prop(oct_cam, "white_balance", text="White balance")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "exposure", text="Exposure")
        sub.prop(oct_cam, "gamma", text="Gamma")
        sub.prop(oct_cam, "vignetting", text="Vignetting")
        sub.prop(oct_cam, "saturation", text="Saturation")
        sub.prop(oct_cam, "white_saturation", text="White saturation")
        sub.prop(oct_cam, "hot_pix", text="Hot pix. removal")
        sub.prop(oct_cam, "min_display_samples", text="Min. display samples")
        sub.prop(oct_cam, "highlight_compression", text="Highlight compression")
        sub.prop(oct_cam, "max_tonemap_interval", text="Max. tonemap interval")
        sub.prop(oct_cam, "dithering", text="Dithering")
        sub.prop(oct_cam, "premultiplied_alpha", text="Premultiplied alpha")
        sub.prop(oct_cam, "neutral_response", text="Neutral response")
        sub.prop(oct_cam, "disable_partial_alpha", text="Disable partial alpha")



class OctaneRender_PT_kernel(OctaneButtonsPanel, Panel):
    bl_label = "Octane kernel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        oct_scene = scene.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_kernel_presets", text=bpy.types.OCTANE_MT_kernel_presets.bl_label)
        row.operator("render.octane_kernel_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_kernel_preset_add", text="", icon="ZOOMOUT").remove_active = True

        row = layout.row(align=True)
        row.prop(oct_scene, "kernel_type", text="Kernel")
        row = layout.row(align=True)
        row.active = (oct_scene.kernel_type == '1')
        row.prop(oct_scene, "gi_mode", text="GImode")
        row = layout.row(align=True)
        row.active = (oct_scene.kernel_type == '4')
        row.prop(oct_scene, "info_channel_type", text="Info-channel type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.label("Samples:")
        sub.prop(oct_scene, "max_samples", text="Max. samples")
        sub.prop(oct_scene, "max_preview_samples", text="Prev. samples")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "parallel_samples", text="Parallel samples")
        sub.prop(oct_scene, "max_tile_samples", text="Max. tile samples")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "zdepth_max", text="Z-Depth max.")
        sub.prop(oct_scene, "uv_max", text="UV max.")
        sub.prop(oct_scene, "ray_epsilon", text="Ray epsilon")
        sub.prop(oct_scene, "distributed_tracing", text="Distributed ray tracing")
        sub.prop(oct_scene, "max_speed", text="Max speed")
        sub.prop(oct_scene, "opacity_threshold", text="Opacity threshold")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "max_diffuse_depth", text="Max. diffuse depth")
        sub.prop(oct_scene, "max_glossy_depth", text="Max. glossy depth")
        sub.prop(oct_scene, "caustic_blur", text="Caustic blur")
        sub.prop(oct_scene, "gi_clamp", text="GI clamp")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "alpha_channel", text="Alpha channel")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "wf_bktrace_hl", text="Wireframe backtrace highlighting")
        sub.prop(oct_scene, "ao_alpha_shadows", text="AO alpha shadows")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "minimize_net_traffic", text="Minimize net traffic")


        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1')
        sub.prop(oct_scene, "specular_depth", text="Specular depth")
        sub.prop(oct_scene, "glossy_depth", text="Glossy depth")
        sub.prop(oct_scene, "diffuse_depth", text="Diffuse depth")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "ao_dist", text="AOdist")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "filter_size", text="Filter size")
        sub.prop(oct_scene, "ray_epsilon", text="Ray epsilon")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "exploration", text="Exploration")
        sub.prop(oct_scene, "direct_light_importance", text="Direct light imp.")
        sub.prop(oct_scene, "max_rejects", text="Max. rejects")
        sub.prop(oct_scene, "parallelism", text="Parallelism")
        sub.prop(oct_scene, "work_chunk_size", text="Work chunk size")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2')
        sub.prop(oct_scene, "coherent_ratio", text="Coherent ratio")
        sub.prop(oct_scene, "max_depth_samples", text="Max. depth samples")
        sub.prop(oct_scene, "depth_tolerance", text="Depth tolerance")
        sub.prop(oct_scene, "static_noise", text="Static noise")
        sub.prop(oct_scene, "deep_image", text="Deep image")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "path_term_power", text="Path term. power")
        sub.prop(oct_scene, "keep_environment", text="Keep environment")
        sub.prop(oct_scene, "alpha_shadows", text="Alpha shadows")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "bump_normal_mapping", text="Bump and normal mapping")


class OctaneRender_PT_server(OctaneButtonsPanel, Panel):
    bl_label = "Octane server"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        oct_scene = scene.octane

        box = layout.box()
        box.label(text="Render server:")
        sub = box.row()
        sub.prop(oct_scene, "server_address")
        sub = box.row()
        sub.operator("octane.activate", text="Activation state")



class OctaneRender_PT_motion_blur(OctaneButtonsPanel, Panel):
    bl_label = "Motion Blur"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        rd = context.scene.render
        self.layout.prop(rd, "use_motion_blur", text="")

    def draw(self, context):
        layout = self.layout

        rd = context.scene.render
        layout.active = rd.use_motion_blur

        row = layout.row()
        row.prop(context.scene.octane, "mb_type")
        row = layout.row()
        row.active = (context.scene.octane.mb_type == '0')
        row.prop(context.scene.octane, "mb_direction")
        row = layout.row()
        row.prop(rd, "motion_blur_shutter")
        row = layout.row()
        row.active = (context.scene.octane.mb_type == '1')
        row.prop(rd, "motion_blur_samples")


class OctaneRender_PT_layer_options(OctaneButtonsPanel, Panel):
    bl_label = "Layer"
    bl_context = "render_layer"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        rl = rd.layers.active

        split = layout.split()

        col = split.column()
        col.prop(scene, "layers", text="Scene")
        col.prop(rl, "layers_exclude", text="Exclude")

        col = split.column()
        col.prop(rl, "layers", text="Layer")
        col.prop(rl, "layers_zmask", text="Mask Layer")

        split = layout.split()

        col = split.column()
        col.label(text="Material:")
        col.prop(rl, "material_override", text="")

        col = split.column()
        col.label(text="Samples override:")
        col.prop(rl, "samples")


class OctaneRender_PT_layer_passes(OctaneButtonsPanel, Panel):
    bl_label = "Render Passes"
    bl_context = "render_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "use_passes", text="")

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        octane = scene.octane
        rd = scene.render
        rl = rd.layers.active

        col = layout.column()
        col.prop(octane, "cur_pass_type")

        col.prop(rl, "use_pass_combined")
        col.prop(rl, "use_pass_emit")
        col.prop(rl, "use_pass_environment")
        col.prop(rl, "use_pass_diffuse_direct")
        col.prop(rl, "use_pass_diffuse_indirect")

        row = col.row()
        row.prop(rl, "use_pass_reflection")
        row.prop(octane, "reflection_pass_subtype")

        col.prop(rl, "use_pass_refraction")
        col.prop(rl, "use_pass_transmission_color", text="Transmission")
        col.prop(rl, "use_pass_subsurface_color", text="SSS")

        row = col.row()
        row.prop(rl, "use_pass_normal")
        row.prop(octane, "normal_pass_subtype")

        col.prop(rl, "use_pass_z")
        col.prop(rl, "use_pass_material_index")
        col.prop(rl, "use_pass_uv")
        col.prop(rl, "use_pass_object_index")
        col.prop(rl, "use_pass_ambient_occlusion")

        row = col.row()
        row.prop(rl, "use_pass_shadow")
        row.prop(octane, "shadows_pass_subtype")

        sub = col.column(align=True)
        sub.prop(octane, "pass_max_samples")
        sub.prop(octane, "pass_z_depth_max")
        sub.prop(octane, "pass_uv_max")
        sub.prop(octane, "pass_max_speed")
        sub.prop(octane, "pass_ao_distance")
        sub.prop(octane, "pass_opacity_threshold")

        col.prop(octane, "pass_distributed_tracing")
        col.prop(octane, "pass_alpha_shadows")
        col.prop(octane, "pass_raw")
        col.prop(octane, "pass_pp_env")
        col.prop(octane, "pass_bump")


class OctaneRender_PT_octane_layers(OctaneButtonsPanel, Panel):
    bl_label = "Octane render layers"
    bl_context = "render_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "layers_enable", text="")

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        octane = scene.octane

        col = layout.column()
        col.prop(octane, "layers_current")
        col.prop(octane, "layers_invert")


class OctaneRender_PT_views(OctaneButtonsPanel, Panel):
    bl_label = "Views"
    bl_context = "render_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        rd = context.scene.render
        self.layout.prop(rd, "use_multiview", text="")

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        rv = rd.views.active

        layout.active = rd.use_multiview
        basic_stereo = (rd.views_format == 'STEREO_3D')

        row = layout.row()
        row.prop(rd, "views_format", expand=True)

        if basic_stereo:
            row = layout.row()
            row.template_list("RENDERLAYER_UL_renderviews", "name", rd, "stereo_views", rd.views, "active_index", rows=2)

            row = layout.row()
            row.label(text="File Suffix:")
            row.prop(rv, "file_suffix", text="")

        else:
            row = layout.row()
            row.template_list("RENDERLAYER_UL_renderviews", "name", rd, "views", rd.views, "active_index", rows=2)

            col = row.column(align=True)
            col.operator("scene.render_view_add", icon='ZOOMIN', text="")
            col.operator("scene.render_view_remove", icon='ZOOMOUT', text="")

            row = layout.row()
            row.label(text="Camera Suffix:")
            row.prop(rv, "camera_suffix", text="")


class OctaneRender_PT_octane_out_of_core(OctaneButtonsPanel, Panel):
    bl_label = "Octane out of core"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "out_of_core_enable", text="")

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        octane = scene.octane

        col = layout.column()
        col.prop(octane, "out_of_core_limit")
        col.prop(octane, "out_of_core_gpu_headroom")


class OctaneCamera_PT_cam(OctaneButtonsPanel, Panel):
    bl_label = "Octane camera"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        sub = layout.row(align=True)
        sub.prop(oct_cam, "baking_camera", text="Baking camera")
        sub = layout.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uv_set", text="UV set")

        sub = layout.column(align=True)
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "pan_mode", text="Pan mode")
        sub.prop(oct_cam, "fov_x", text="FOV X")
        sub.prop(oct_cam, "fov_y", text="FOV Y")

        sub = layout.column(align=True)
        sub.active = (cam.type != 'PANO')
#        sub.prop(oct_cam, "ortho", text="Orthographic")
        sub.prop(oct_cam, "aperture", text="Aperture")
        sub.prop(oct_cam, "aperture_edge", text="Aperture edge")
        sub.prop(oct_cam, "distortion", text="Distortion")
        sub.prop(oct_cam, "persp_corr", text="Persp. correction")

        sub = layout.column(align=True)
        sub.active = (cam.type != 'PANO')
        sub.prop(oct_cam, "pixel_aspect", text="Pixel aspect")
        sub.prop(oct_cam, "aperture_aspect", text="Aperture aspect")

        sub = layout.row(align=True)
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "keep_upright", text="Keep upright")

        sub = layout.column(align=True)
        sub.label("Focus:")
        sub.prop(oct_cam, "autofocus", text="Autofocus")
        sub = layout.row(align=True)
        sub.active = oct_cam.autofocus is False
        sub.prop(cam, "dof_object", text="")
        sub = layout.row(align=True)
        sub.active = oct_cam.autofocus is False and cam.dof_object is None
        sub.prop(cam, "dof_distance", text="Distance")

        layout.label("Stereo:")
        sub = layout.row()
        sub.active = (cam.type != 'PANO')
        sub.prop(oct_cam, "stereo_mode", text="Stereo mode")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "stereo_out", text="Stereo output")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "stereo_dist", text="Eye distance")
        sub.prop(oct_cam, "stereo_swap_eyes", text="Swap eyes")
        sub = layout.column()
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "stereo_dist_falloff", text="Eye dist. falloff")
        sub.prop(oct_cam, "blackout_lat", text="Pano blackout lat.")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "left_filter", text="Left filter")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "right_filter", text="Right filter")


class OctaneCamera_PT_imager(OctaneButtonsPanel, Panel):
    bl_label = "Octane imager"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_imager_presets", text=bpy.types.OCTANE_MT_imager_presets.bl_label)
        row.operator("render.octane_imager_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_imager_preset_add", text="", icon="ZOOMOUT").remove_active = True

        sub = layout.row()
        sub.prop(oct_cam, "response_type", text="Response type")

        sub = layout.column(align=True)
        sub.prop(oct_cam, "white_balance", text="White balance")
        sub.prop(oct_cam, "exposure", text="Exposure")
        sub.prop(oct_cam, "gamma", text="Gamma")
        sub.prop(oct_cam, "vignetting", text="Vignetting")
        sub.prop(oct_cam, "saturation", text="Saturation")
        sub.prop(oct_cam, "white_saturation", text="White saturation")
        sub.prop(oct_cam, "hot_pix", text="Hot pix. removal")
        sub.prop(oct_cam, "min_display_samples", text="Min. display samples")
        sub.prop(oct_cam, "highlight_compression", text="Highlight compression")
        sub.prop(oct_cam, "max_tonemap_interval", text="Max. tonemap interval")
        sub.prop(oct_cam, "dithering", text="Dithering")
        sub.prop(oct_cam, "premultiplied_alpha", text="Premultiplied alpha")
        sub.prop(oct_cam, "neutral_response", text="Neutral response")
        sub.prop(oct_cam, "disable_partial_alpha", text="Disable partial alpha")


class OctaneCamera_PT_post(OctaneButtonsPanel, Panel):
    bl_label = "Octane postprocessor"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        sub = layout.column(align=True)
        sub.prop(oct_cam, "postprocess", text="Enable")
        sub.prop(oct_cam, "bloom_power", text="Bloom power")
        sub.prop(oct_cam, "glare_power", text="Glare power")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "glare_ray_count", text="Glare ray count")
        sub.prop(oct_cam, "glare_angle", text="Glare angle")
        sub.prop(oct_cam, "glare_blur", text="Glare blur")
        sub.prop(oct_cam, "spectral_intencity", text="Spectral intencity")
        sub.prop(oct_cam, "spectral_shift", text="Spectral shift")

class Octane_PT_post_processing(OctaneButtonsPanel, Panel):
    bl_label = "Post Processing"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        rd = context.scene.render

        split = layout.split()

        col = split.column()
        col.prop(rd, "use_compositing")
        col.prop(rd, "use_sequencer")

        col = split.column()
        col.prop(rd, "dither_intensity", text="Dither", slider=True)


class Octane_PT_context_material(OctaneButtonsPanel, Panel):
    bl_label = ""
    bl_context = "material"
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        mat = context.material
        ob = context.object
        slot = context.material_slot
        space = context.space_data

        if ob:
            row = layout.row()

            row.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=2)

            col = row.column(align=True)
            col.operator("object.material_slot_add", icon='ZOOMIN', text="")
            col.operator("object.material_slot_remove", icon='ZOOMOUT', text="")

            col.menu("MATERIAL_MT_specials", icon='DOWNARROW_HLT', text="")

            if ob.mode == 'EDIT':
                row = layout.row(align=True)
                row.operator("object.material_slot_assign", text="Assign")
                row.operator("object.material_slot_select", text="Select")
                row.operator("object.material_slot_deselect", text="Deselect")

        split = layout.split(percentage=0.65)

        if ob:
            split.template_ID(ob, "active_material", new="material.new")
            row = split.row()

            if slot:
                row.prop(slot, "link", text="")
            else:
                row.label()
        elif mat:
            split.template_ID(space, "pin_id")
            split.separator()


class OctaneMaterial_PT_preview(OctaneButtonsPanel, Panel):
    bl_label = "Preview"
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.material and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        self.layout.template_preview(context.material)

class Octane_PT_mesh_properties(OctaneButtonsPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if OctaneButtonsPanel.poll(context):
            if context.mesh or context.curve or context.meta_ball:
                return True

        return False

    def draw(self, context):
        layout = self.layout

        mesh = context.mesh
        curve = context.curve
        mball = context.meta_ball

        if mesh:
            cdata = mesh.octane
        elif curve:
            cdata = curve.octane
        elif mball:
            cdata = mball.octane

        sub = layout.row(align=True)
        sub.prop(cdata, "mesh_type")
        sub.operator("octane.set_meshes_type", "", "", True, 'MESH_DATA')
        sub = layout.row(align=True)
        sub.prop(cdata, "layer_number", text="Layer number")
        sub.prop(cdata, "baking_group_id", text="Baking group")

        box = layout.box()
        box.label(text="OpenSubDiv:")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_enable", text="Enable")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_scheme", text="Scheme")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_bound_interp", text="Boundary interp.")
        sub = box.column(align=True)
        sub.prop(cdata, "open_subd_level", text="Level")
        sub.prop(cdata, "open_subd_sharpness", text="Sharpness")

        sub = layout.column(align=True)
        sub.prop(cdata, "vis_general")
        sub.prop(cdata, "vis_cam")
        sub.prop(cdata, "vis_shadow")
        sub.prop(cdata, "rand_color_seed")

        box = layout.box()
        box.label(text="Volume properties:")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_iso")
        sub.prop(cdata, "vdb_abs_scale")
        sub.prop(cdata, "vdb_emiss_scale")
        sub.prop(cdata, "vdb_scatter_scale")
        sub.prop(cdata, "vdb_vel_scale")


class OctaneObject_PT_octane_properties(OctaneButtonsPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return False
        ob = context.object
        return OctaneButtonsPanel.poll(context) and ob and ob.type in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LAMP'}  # todo: 'LAMP'

    def draw(self, context):
        layout = self.layout

        ob = context.object
        props = ob.octane_properties

        flow = layout.column_flow()

        flow.prop(props, "visibility")


def find_node(material, nodetype):
    if material and material.node_tree:
        ntree = material.node_tree
        for node in ntree.nodes:
            if getattr(node, "type", None) == nodetype:
                return node
    return None


def find_node_input(node, name):
    for input in node.inputs:
        if input.name == name:
            return input
    return None


def panel_node_draw(layout, id_data, output_type, input_name):
    if not id_data.use_nodes:
        layout.prop(id_data, "use_nodes", icon='NODETREE')
        return False

    ntree = id_data.node_tree

    node = find_node(id_data, output_type)
    if not node:
        layout.label(text="No output node.")
    else:
        input = find_node_input(node, input_name)
        layout.template_node_view(ntree, node, input)

    return True


class OctaneLamp_PT_lamp(OctaneButtonsPanel, Panel):
    bl_label = "Lamp"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.lamp and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp
        oct_lamp = lamp.octane
        cscene = context.scene.octane

        layout.prop(lamp, "type", expand=True)

        if lamp.type in {'HEMI', 'POINT', 'SUN', 'SPOT'}:
            layout.label(text="Not supported.")
        else:
            split = layout.split()
            col = split.column(align=True)

            if lamp.type in {'POINT', 'SUN', 'SPOT'}:
                col.prop(lamp, "size")
            elif lamp.type == 'AREA':
                col.prop(lamp, "shape", text="")
                sub = col.column(align=True)

                if lamp.shape == 'SQUARE':
                    sub.prop(lamp, "size")
                elif lamp.shape == 'RECTANGLE':
                    sub.prop(lamp, "size", text="Size X")
                    sub.prop(lamp, "size_y", text="Size Y")

            col = split.column()
            col.prop(oct_lamp, "enable")
            col.prop(oct_lamp, "mesh_type")


class OctaneLamp_PT_nodes(OctaneButtonsPanel, Panel):
    bl_label = "Nodes"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.lamp and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp
        if not panel_node_draw(layout, lamp, 'OUTPUT_LAMP', 'Surface'):
            layout.prop(lamp, "color")


class OctaneLamp_PT_spot(OctaneButtonsPanel, Panel):
    bl_label = "Spot Shape"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        return (lamp and lamp.type == 'SPOT') and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp

        split = layout.split()

        col = split.column()
        sub = col.column()
        sub.prop(lamp, "spot_size", text="Size")
        sub.prop(lamp, "spot_blend", text="Blend", slider=True)

        col = split.column()
        col.prop(lamp, "show_cone")


class OctaneWorld_PT_settings(OctaneButtonsPanel, Panel):
    bl_label = "Octane environment"
    bl_context = "world"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.world and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout
#        obj = context.object

        world = context.world
        oct_world = world.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_environment_presets", text=bpy.types.OCTANE_MT_environment_presets.bl_label)
        row.operator("render.octane_environment_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_environment_preset_add", text="", icon="ZOOMOUT").remove_active = True

        row = layout.row(align=True)
        row.prop(oct_world, "env_type", text="Type")
        row = layout.row(align=True)
        row.prop(oct_world, "env_power", text="Power")
        
        row = layout.row(align=True)
#        row.prop(oct_world, "env_texture", text="Texture")
        row.prop_search(oct_world, "env_texture",  bpy.data, "textures")

        row = layout.row(align=True)
        row.prop_search(oct_world, "env_medium",  bpy.data, "textures")
        row = layout.row(align=True)
        row.prop(oct_world, "env_med_radius", text="Medium radius")

        row = layout.row(align=True)
        row.prop(oct_world, "env_importance_sampling", text="Importance sampling")

        row = layout.row(align=True)
        row.active = (oct_world.env_type == '1')
        row.prop(oct_world, "env_daylight_type", text="Daylight type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1' and oct_world.env_daylight_type == '1')
        sub.label("Daylight:")
        sub.prop(oct_world, "env_longitude", text="Longitude")
        sub.prop(oct_world, "env_latitude", text="Latitude")
        sub.prop(oct_world, "env_day", text="Day")
        sub.prop(oct_world, "env_month", text="Month")
        sub.prop(oct_world, "env_gmtoffset", text="GMT offset")
        sub.prop(oct_world, "env_hour", text="Hour")

        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1' and oct_world.env_daylight_type == '0')
        sub.label("Sun direction:")
        sub.prop(oct_world, "env_sundir_x", text="Sun direction X")
        sub.prop(oct_world, "env_sundir_y", text="Sun direction Y")
        sub.prop(oct_world, "env_sundir_z", text="Sun direction Z")
        
        split = layout.split()
        col = split.column()
        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_turbidity", text="Turbidity")
        sub.prop(oct_world, "env_northoffset", text="North offset")
        sub.prop(oct_world, "env_sun_size", text="Sun size")

        col = split.column()

        sub = col.column(align=True)
        sub.label("Sky-Sunset colors:")
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_sky_color", text="")
        sub.prop(oct_world, "env_sunset_color", text="")

        row = layout.row(align=True)
        row.active = (oct_world.env_type == '1')
        row.prop(oct_world, "env_model", text="Model")


class OctaneVisibleWorld_PT_settings(OctaneButtonsPanel, Panel):
    bl_label = "Octane visible environment"
    bl_context = "world"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.world and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.world.octane, "use_vis_env", text="")

    def draw(self, context):
        layout = self.layout
#        obj = context.object

        world = context.world
        oct_world = world.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_environment_presets", text=bpy.types.OCTANE_MT_environment_presets.bl_label)
        row.operator("render.octane_environment_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_environment_preset_add", text="", icon="ZOOMOUT").remove_active = True

        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_type", text="Type")
        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_power", text="Power")
        
        row = layout.row(align=True)
#        row.prop(oct_world, "env_vis_texture", text="Texture")
        row.prop_search(oct_world, "env_vis_texture",  bpy.data, "textures")

        row = layout.row(align=True)
        row.prop_search(oct_world, "env_vis_medium",  bpy.data, "textures")
        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_med_radius", text="Medium radius")

        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_importance_sampling", text="Importance sampling")

        row = layout.row(align=True)
        row.active = (oct_world.env_vis_type == '1')
        row.prop(oct_world, "env_vis_daylight_type", text="Daylight type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1' and oct_world.env_vis_daylight_type == '1')
        sub.label("Daylight:")
        sub.prop(oct_world, "env_vis_longitude", text="Longitude")
        sub.prop(oct_world, "env_vis_latitude", text="Latitude")
        sub.prop(oct_world, "env_vis_day", text="Day")
        sub.prop(oct_world, "env_vis_month", text="Month")
        sub.prop(oct_world, "env_vis_gmtoffset", text="GMT offset")
        sub.prop(oct_world, "env_vis_hour", text="Hour")

        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1' and oct_world.env_vis_daylight_type == '0')
        sub.label("Sun direction:")
        sub.prop(oct_world, "env_vis_sundir_x", text="Sun direction X")
        sub.prop(oct_world, "env_vis_sundir_y", text="Sun direction Y")
        sub.prop(oct_world, "env_vis_sundir_z", text="Sun direction Z")
        
        split = layout.split()
        col = split.column()
        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1')
        sub.prop(oct_world, "env_vis_turbidity", text="Turbidity")
        sub.prop(oct_world, "env_vis_northoffset", text="North offset")
        sub.prop(oct_world, "env_vis_sun_size", text="Sun size")

        col = split.column()

        sub = col.column(align=True)
        sub.label("Sky-Sunset colors:")
        sub.active = (oct_world.env_vis_type == '1')
        sub.prop(oct_world, "env_vis_sky_color", text="")
        sub.prop(oct_world, "env_vis_sunset_color", text="")

        row = layout.row(align=True)
        row.active = (oct_world.env_vis_type == '1')
        row.prop(oct_world, "env_vis_model", text="Model")

        sub = layout.column(align=True)
        sub.label("Visible environment:")
        sub.prop(oct_world, "env_vis_backplate", text="Backplate")
        sub.prop(oct_world, "env_vis_reflections", text="Reflections")
        sub.prop(oct_world, "env_vis_refractions", text="Refractions")


class OctaneMaterial_PT_surface(OctaneButtonsPanel, Panel):
    bl_label = "Surface"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return context.material and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        mat = context.material
        if not panel_node_draw(layout, mat, 'OUTPUT_MATERIAL', 'Surface'):
            layout.prop(mat, "diffuse_color")


class OctaneTexture_PT_context(OctaneButtonsPanel, Panel):
    bl_label = ""
    bl_context = "texture"
    bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout

        tex = context.texture
        space = context.space_data
        pin_id = space.pin_id
        use_pin_id = space.use_pin_id
        user = context.texture_user

        if not use_pin_id or not isinstance(pin_id, bpy.types.Texture):
            pin_id = None

        if not pin_id:
            layout.template_texture_user()

        if user:
            layout.separator()

            split = layout.split(percentage=0.65)
            col = split.column()

            if pin_id:
                col.template_ID(space, "pin_id")
            elif user:
                col.template_ID(user, "texture", new="texture.new")

            if tex:
                split = layout.split(percentage=0.2)
                split.label(text="Type:")
                split.prop(tex, "type", text="")


class OctaneTexture_PT_nodes(OctaneButtonsPanel, Panel):
    bl_label = "Nodes"
    bl_context = "texture"

    @classmethod
    def poll(cls, context):
        tex = context.texture
        return (tex and tex.use_nodes) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        tex = context.texture
        panel_node_draw(layout, tex, 'OUTPUT_TEXTURE', 'Color')


class OctaneTexture_PT_node(OctaneButtonsPanel, Panel):
    bl_label = "Node"
    bl_context = "texture"

    @classmethod
    def poll(cls, context):
        node = context.texture_node
        return node and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        node = context.texture_node
        ntree = node.id_data
        layout.template_node_view(ntree, node, None)


class OctaneTexture_PT_mapping(OctaneButtonsPanel, Panel):
    bl_label = "Mapping"
    bl_context = "texture"

    @classmethod
    def poll(cls, context):
        tex = context.texture
        node = context.texture_node
        return (node or (tex and tex.use_nodes)) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        # tex = context.texture
        node = context.texture_node

        mapping = node.texture_mapping

        row = layout.row()

        row.column().prop(mapping, "translation")
        row.column().prop(mapping, "rotation")
        row.column().prop(mapping, "scale")

        layout.label(text="Projection:")

        row = layout.row()
        row.prop(mapping, "mapping_x", text="")
        row.prop(mapping, "mapping_y", text="")
        row.prop(mapping, "mapping_z", text="")


class OctaneTexture_PT_colors(OctaneButtonsPanel, Panel):
    bl_label = "Color"
    bl_context = "texture"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        # tex = context.texture
        # node = context.texture_node
        return False
        #return (node or (tex and tex.use_nodes)) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        # tex = context.texture
        node = context.texture_node

        mapping = node.color_mapping

        split = layout.split()

        col = split.column()
        col.label(text="Blend:")
        col.prop(mapping, "blend_type", text="")
        col.prop(mapping, "blend_factor", text="Factor")
        col.prop(mapping, "blend_color", text="")

        col = split.column()
        col.label(text="Adjust:")
        col.prop(mapping, "brightness")
        col.prop(mapping, "contrast")
        col.prop(mapping, "saturation")

        layout.separator()

        layout.prop(mapping, "use_color_ramp", text="Ramp")
        if mapping.use_color_ramp:
            layout.template_color_ramp(mapping, "color_ramp", expand=True)


class OctaneParticle_PT_HairSettings(OctaneButtonsPanel, Panel):
    bl_label = "Octane Hair Settings"
    bl_context = "particle"

    @classmethod
    def poll(cls, context):
        psys = context.particle_system
        return psys and OctaneButtonsPanel.poll(context) and psys.settings.type == 'HAIR'

    def draw(self, context):
        layout = self.layout

        psys = context.particle_settings
        opsys = psys.octane

        layout.label(text="Thickness:")
        row = layout.row()
        row.prop(opsys, "root_width", text="Root")
        row.prop(opsys, "tip_width", text="Tip")
        row = layout.row()
        row.prop(opsys, "min_curvature")


def draw_device(self, context):
    scene = context.scene
    layout = self.layout

    if scene.render.engine == 'octane':
        oct_scene = scene.octane

        sub = layout.row()
        sub.prop(oct_scene, "anim_mode")
        sub = layout.row()
        sub.prop(oct_scene, "export_scene")
        layout.prop(oct_scene, "devices")
        sub = layout.row()
        sub.prop(oct_scene, "viewport_hide")
        sub.prop(oct_scene, "deep_image")
        layout.prop(oct_scene, "meshes_type", expand=True)


def draw_pause(self, context):
    layout = self.layout
    scene = context.scene

    if scene.render.engine == "octane":
        view = context.space_data

        if view.viewport_shade == 'RENDERED':
            oct_scene = scene.octane
            layername = scene.render.layers.active.name
            layout.prop(oct_scene, "preview_pause", icon="PAUSE", text="")
            layout.operator("octane.reload", "", "", True, 'FILE_REFRESH')
            layout.prop(oct_scene, "preview_active_layer", icon="RENDERLAYERS", text=layername)


def get_panels():
    types = bpy.types
    panels = [
        "RENDER_PT_render",
        "RENDER_PT_output",
        "RENDER_PT_encoding",
        "RENDER_PT_dimensions",
        "RENDER_PT_stamp",

        "RENDER_PT_freestyle",
        "RENDERLAYER_PT_layers",
        "RENDERLAYER_PT_freestyle",
        "RENDERLAYER_PT_freestyle_lineset",
        "RENDERLAYER_PT_freestyle_linestyle",
        
        "SCENE_PT_scene",
        "SCENE_PT_color_management",
        "SCENE_PT_custom_props",
        "SCENE_PT_audio",
        "SCENE_PT_unit",
        "SCENE_PT_keying_sets",
        "SCENE_PT_keying_set_paths",
        "SCENE_PT_physics",
        "WORLD_PT_context_world",
        "WORLD_PT_custom_props",
        "DATA_PT_context_mesh",
        "DATA_PT_context_camera",
        "DATA_PT_context_lamp",
        "DATA_PT_context_speaker",
        "DATA_PT_normals",
        "DATA_PT_texture_space",
        "DATA_PT_curve_texture_space",
        "DATA_PT_mball_texture_space",
        "DATA_PT_vertex_groups",
        "DATA_PT_shape_keys",
        "DATA_PT_uv_texture",
        "DATA_PT_vertex_colors",
        "DATA_PT_camera",
        "DATA_PT_camera_display",
        "DATA_PT_camera_safe_areas",
        "DATA_PT_lens",
        "DATA_PT_speaker",
        "DATA_PT_distance",
        "DATA_PT_cone",
        "DATA_PT_customdata",
        "DATA_PT_custom_props_mesh",
        "DATA_PT_custom_props_camera",
        "DATA_PT_custom_props_lamp",
        "DATA_PT_custom_props_speaker",
        "DATA_PT_custom_props_arm",
        "DATA_PT_custom_props_curve",
        "DATA_PT_custom_props_lattice",
        "DATA_PT_custom_props_metaball",
        "TEXTURE_PT_preview",
        "TEXTURE_PT_custom_props",
        "TEXTURE_PT_clouds",
        "TEXTURE_PT_wood",
        "TEXTURE_PT_marble",
        "TEXTURE_PT_magic",
        "TEXTURE_PT_blend",
        "TEXTURE_PT_stucci",
        "TEXTURE_PT_image",
        "TEXTURE_PT_image_sampling",
        "TEXTURE_PT_image_mapping",
        "TEXTURE_PT_musgrave",
        "TEXTURE_PT_voronoi",
        "TEXTURE_PT_distortednoise",
        "TEXTURE_PT_voxeldata",
        "TEXTURE_PT_pointdensity",
        "TEXTURE_PT_pointdensity_turbulence",
        "TEXTURE_PT_mapping",
        "TEXTURE_PT_ocean",
        "TEXTURE_PT_influence",
        "TEXTURE_PT_colors",
        "PARTICLE_PT_context_particles",
        "PARTICLE_PT_custom_props",
        "PARTICLE_PT_emission",
        "PARTICLE_PT_hair_dynamics",
        "PARTICLE_PT_cache",
        "PARTICLE_PT_velocity",
        "PARTICLE_PT_rotation",
        "PARTICLE_PT_physics",
        "SCENE_PT_rigid_body_world",
        "SCENE_PT_rigid_body_cache",
        "SCENE_PT_rigid_body_field_weights",
        "PARTICLE_PT_boidbrain",
        "PARTICLE_PT_render",
        "PARTICLE_PT_draw",
        "PARTICLE_PT_children",
        "PARTICLE_PT_field_weights",
        "PARTICLE_PT_force_fields",
        "PARTICLE_PT_vertexgroups",
        "MATERIAL_PT_custom_props",
        "MATERIAL_PT_freestyle_line",
        "BONE_PT_custom_props",
        "OBJECT_PT_custom_props",
        ]

    return [getattr(types, p) for p in panels if hasattr(types, p)]


def register():
    bpy.types.RENDER_PT_render.append(draw_device)
    bpy.types.VIEW3D_HT_header.append(draw_pause)

    for panel in get_panels():
        panel.COMPAT_ENGINES.add('octane')


def unregister():
    bpy.types.RENDER_PT_render.remove(draw_device)
    bpy.types.VIEW3D_HT_header.remove(draw_pause)

    for panel in get_panels():
        panel.COMPAT_ENGINES.remove('octane')
