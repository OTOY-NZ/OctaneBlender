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

class OCTANE_MT_vis_environment_presets(Menu):
    bl_label = "Visible environment presets"
    preset_subdir = "octane/vis_environment"
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


class VIEW3D_PT_octimager(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane imager"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.space_data and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "hdr_tonemap_enable", text="")

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
        sub.prop(oct_cam, "response_type")

        sub = layout.column(align=True)
        sub.prop(oct_cam, "white_balance")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "exposure")
        sub.prop(oct_cam, "gamma")
        sub.prop(oct_cam, "vignetting")
        sub.prop(oct_cam, "saturation")
        sub.prop(oct_cam, "white_saturation")
        sub.prop(oct_cam, "hot_pix")
        sub.prop(oct_cam, "min_display_samples")
        sub.prop(oct_cam, "highlight_compression")
        sub.prop(oct_cam, "max_tonemap_interval")
        sub.prop(oct_cam, "dithering")
        sub.prop(oct_cam, "premultiplied_alpha")
        sub.prop(oct_cam, "neutral_response")
        sub.prop(oct_cam, "disable_partial_alpha")



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
        row.prop(oct_scene, "kernel_type")
        row = layout.row(align=True)
        row.active = (oct_scene.kernel_type == '1')
        row.prop(oct_scene, "gi_mode")
        row = layout.row(align=True)
        row.active = (oct_scene.kernel_type == '1')
        row.prop_search(oct_scene, "ao_texture", bpy.data, "textures")
        row = layout.row(align=True)
        row.active = (oct_scene.kernel_type == '4')
        row.prop(oct_scene, "info_channel_type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.label("Samples:")
        sub.prop(oct_scene, "max_samples")
        sub.prop(oct_scene, "max_preview_samples")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "parallel_samples")
        sub.prop(oct_scene, "max_tile_samples")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "zdepth_max")
        sub.prop(oct_scene, "uv_max")
        sub.prop(oct_scene, "max_speed")
        sub.prop(oct_scene, "opacity_threshold")
        sub.prop(oct_scene, "sampling_mode")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "max_diffuse_depth")
        sub.prop(oct_scene, "max_glossy_depth")
        sub.prop(oct_scene, "caustic_blur")
        sub.prop(oct_scene, "gi_clamp")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "alpha_channel")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "wf_bkface_hl")
        sub.prop(oct_scene, "ao_alpha_shadows")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "minimize_net_traffic")


        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1')
        sub.prop(oct_scene, "specular_depth")
        sub.prop(oct_scene, "glossy_depth")
        sub.prop(oct_scene, "diffuse_depth")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "ao_dist")

        sub = col.column(align=True)
        #sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3' or oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "filter_size")
        sub.prop(oct_scene, "ray_epsilon")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "exploration")
        sub.prop(oct_scene, "direct_light_importance")
        sub.prop(oct_scene, "max_rejects")
        sub.prop(oct_scene, "parallelism")
        sub.prop(oct_scene, "work_chunk_size")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2')
        sub.prop(oct_scene, "coherent_ratio")
        sub.prop(oct_scene, "max_depth_samples")
        sub.prop(oct_scene, "depth_tolerance")
        sub.prop(oct_scene, "static_noise")
        sub.prop(oct_scene, "deep_image")

        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '1' or oct_scene.kernel_type == '2' or oct_scene.kernel_type == '3')
        sub.prop(oct_scene, "path_term_power")
        sub.prop(oct_scene, "keep_environment")
        sub.prop(oct_scene, "alpha_shadows")
        sub = col.column(align=True)
        sub.active = (oct_scene.kernel_type == '4')
        sub.prop(oct_scene, "bump_normal_mapping")


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
        col.prop(rl, "use_pass_diffuse")
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

        col.prop(octane, "pass_sampling_mode")
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
        col.prop(octane, "layers_mode")
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

        sub = layout.column(align=True)
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "pan_mode")
        sub.prop(oct_cam, "fov_x")
        sub.prop(oct_cam, "fov_y")

        col = layout.column(align=True)
        col.active = (cam.type != 'PANO')
#        sub.prop(oct_cam, "ortho")
        box = col.box()
        #box.label(text=":")
        sub = box.row(align=True)
        sub.prop(oct_cam, "use_fstop")
        sub.prop(oct_cam, "fstop")
        sub.prop(oct_cam, "aperture")
        sub = col.column(align=True)
        sub.prop(oct_cam, "aperture_edge")
        sub.prop(oct_cam, "distortion")
        sub.prop(oct_cam, "persp_corr")

        sub = layout.column(align=True)
        sub.active = (cam.type != 'PANO')
        sub.prop(oct_cam, "pixel_aspect")
        sub.prop(oct_cam, "aperture_aspect")

        sub = layout.row(align=True)
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "keep_upright")

        sub = layout.column(align=True)
        sub.label("Focus:")
        sub.prop(oct_cam, "autofocus")
        sub = layout.row(align=True)
        sub.active = oct_cam.autofocus is False
        sub.prop(cam, "dof_object", text="")
        sub = layout.row(align=True)
        sub.active = oct_cam.autofocus is False and cam.dof_object is None
        sub.prop(cam, "dof_distance", text="Distance")

        layout.label("Stereo:")
        sub = layout.row()
        sub.active = (cam.type != 'PANO')
        sub.prop(oct_cam, "stereo_mode")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "stereo_out")
        sub = layout.row()
        sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub.prop(oct_cam, "stereo_dist")
        sub.prop(oct_cam, "stereo_swap_eyes")
        sub = layout.column()
        sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "stereo_dist_falloff")
        sub.prop(oct_cam, "blackout_lat")

        col = layout.column()
        col.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '0')
        sub = col.row()
        sub.prop(oct_cam, "left_filter")
        sub = col.row()
        sub.prop(oct_cam, "right_filter")

        box = layout.box()
        box.label(text="Baking:")
        col = box.column(align=True)

        sub = col.row(align=True)
        sub.prop(oct_cam, "baking_camera")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_revert")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_use_position")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_bkface_culling")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_tolerance")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_group_id")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_padding")
        sub = col.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uv_set")

        col1 = box.column(align=True)
        sub = col1.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uvbox_min_x")
        sub = col1.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uvbox_min_y")

        col1 = box.column(align=True)
        sub = col1.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uvbox_size_x")
        sub = col1.row(align=True)
        sub.active = (oct_cam.baking_camera == True)
        sub.prop(oct_cam, "baking_uvbox_size_y")


class OctaneCamera_PT_imager(OctaneButtonsPanel, Panel):
    bl_label = "Octane imager"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "hdr_tonemap_enable", text="")

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_imager_presets", text=bpy.types.OCTANE_MT_imager_presets.bl_label)
        row.operator("render.octane_imager_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_imager_preset_add", text="", icon="ZOOMOUT").remove_active = True

        sub = layout.row()
        sub.prop(oct_cam, "response_type")

        sub = layout.column(align=True)
        sub.prop(oct_cam, "white_balance")
        sub.prop(oct_cam, "exposure")
        sub.prop(oct_cam, "gamma")
        sub.prop(oct_cam, "vignetting")
        sub.prop(oct_cam, "saturation")
        sub.prop(oct_cam, "white_saturation")
        sub.prop(oct_cam, "hot_pix")
        sub.prop(oct_cam, "min_display_samples")
        sub.prop(oct_cam, "highlight_compression")
        sub.prop(oct_cam, "max_tonemap_interval")
        sub.prop(oct_cam, "dithering")
        sub.prop(oct_cam, "premultiplied_alpha")
        sub.prop(oct_cam, "neutral_response")
        sub.prop(oct_cam, "disable_partial_alpha")


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
        sub.prop(oct_cam, "bloom_power")
        sub.prop(oct_cam, "glare_power")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "glare_ray_count")
        sub.prop(oct_cam, "glare_angle")
        sub.prop(oct_cam, "glare_blur")
        sub.prop(oct_cam, "spectral_intencity")
        sub.prop(oct_cam, "spectral_shift")

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
        sub.prop(cdata, "winding_order")
        sub = layout.row(align=True)
        sub.prop(cdata, "layer_number")
        sub.prop(cdata, "baking_group_id")
        sub = layout.row(align=True)
        sub.prop(cdata, "rand_color_seed")
        sub = layout.row(align=True)
        sub.prop(cdata, "hair_interpolation")

        if context.curve:
            row = layout.row(align=True)
            sub = row.column(align=True)
            sub.prop(cdata, "use_auto_smooth")
            sub = row.column(align=True)
            sub.prop(cdata, "auto_smooth_angle")

        box = layout.box()
        box.label(text="OpenSubDiv:")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_enable", text="Enable")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_scheme")
        sub = box.row(align=True)
        sub.prop(cdata, "open_subd_bound_interp")
        sub = box.column(align=True)
        sub.prop(cdata, "open_subd_level")
        sub.prop(cdata, "open_subd_sharpness")

        box = layout.box()
        box.label(text="Visibility:")
        sub = box.column(align=True)
        sub.prop(cdata, "vis_general")
        sub.prop(cdata, "vis_cam")
        sub.prop(cdata, "vis_shadow")

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
        row.prop(oct_world, "env_type")
        row = layout.row(align=True)
        row.prop(oct_world, "env_power")

        row = layout.row(align=True)
#        row.prop(oct_world, "env_texture")
        row.prop_search(oct_world, "env_texture", bpy.data, "textures")

        row = layout.row(align=True)
        row.prop_search(oct_world, "env_medium", bpy.data, "textures")
        row = layout.row(align=True)
        row.prop(oct_world, "env_med_radius")

        row = layout.row(align=True)
        row.prop(oct_world, "env_importance_sampling")

        row = layout.row(align=True)
        row.active = (oct_world.env_type == '1')
        row.prop(oct_world, "env_daylight_type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1' and oct_world.env_daylight_type == '1')
        sub.label("Daylight:")
        sub.prop(oct_world, "env_longitude")
        sub.prop(oct_world, "env_latitude")
        sub.prop(oct_world, "env_day")
        sub.prop(oct_world, "env_month")
        sub.prop(oct_world, "env_gmtoffset")
        sub.prop(oct_world, "env_hour")

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_turbidity")
        sub.prop(oct_world, "env_northoffset")
        sub.prop(oct_world, "env_sun_size")

        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1' and oct_world.env_daylight_type == '0')
        sub.label("Sun direction:")
        sub.prop(oct_world, "env_sundir_x")
        sub.prop(oct_world, "env_sundir_y")
        sub.prop(oct_world, "env_sundir_z")

        sub = col.column(align=True)
        sub.label("Sky colors:")
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_sky_color", text="")
        sub.prop(oct_world, "env_sunset_color", text="")
        sub.prop(oct_world, "env_ground_color", text="")

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_ground_start_angle")
        sub.prop(oct_world, "env_ground_blend_angle")

        row = layout.row(align=True)
        row.active = (oct_world.env_type == '1')
        row.prop(oct_world, "env_model")


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
        row.menu("OCTANE_MT_vis_environment_presets", text=bpy.types.OCTANE_MT_vis_environment_presets.bl_label)
        row.operator("render.octane_vis_environment_preset_add", text="", icon="ZOOMIN")
        row.operator("render.octane_vis_environment_preset_add", text="", icon="ZOOMOUT").remove_active = True

        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_type")
        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_power")

        row = layout.row(align=True)
#        row.prop(oct_world, "env_vis_texture")
        row.prop_search(oct_world, "env_vis_texture", bpy.data, "textures")

        row = layout.row(align=True)
        row.prop_search(oct_world, "env_vis_medium", bpy.data, "textures")
        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_med_radius")

        row = layout.row(align=True)
        row.prop(oct_world, "env_vis_importance_sampling")

        row = layout.row(align=True)
        row.active = (oct_world.env_vis_type == '1')
        row.prop(oct_world, "env_vis_daylight_type")

        split = layout.split()
        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1' and oct_world.env_vis_daylight_type == '1')
        sub.label("Daylight:")
        sub.prop(oct_world, "env_vis_longitude")
        sub.prop(oct_world, "env_vis_latitude")
        sub.prop(oct_world, "env_vis_day")
        sub.prop(oct_world, "env_vis_month")
        sub.prop(oct_world, "env_vis_gmtoffset")
        sub.prop(oct_world, "env_vis_hour")

        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1')
        sub.prop(oct_world, "env_vis_turbidity")
        sub.prop(oct_world, "env_vis_northoffset")
        sub.prop(oct_world, "env_vis_sun_size")

        col = split.column()

        sub = col.column(align=True)
        sub.active = (oct_world.env_vis_type == '1' and oct_world.env_vis_daylight_type == '0')
        sub.label("Sun direction:")
        sub.prop(oct_world, "env_vis_sundir_x")
        sub.prop(oct_world, "env_vis_sundir_y")
        sub.prop(oct_world, "env_vis_sundir_z")

        sub = col.column(align=True)
        sub.label("Sky colors:")
        sub.active = (oct_world.env_vis_type == '1')
        sub.prop(oct_world, "env_vis_sky_color", text="")
        sub.prop(oct_world, "env_vis_sunset_color", text="")
        sub.prop(oct_world, "env_vis_ground_color", text="")

        sub = col.column(align=True)
        sub.active = (oct_world.env_type == '1')
        sub.prop(oct_world, "env_vis_ground_start_angle")
        sub.prop(oct_world, "env_vis_ground_blend_angle")

        row = layout.row(align=True)
        row.active = (oct_world.env_vis_type == '1')
        row.prop(oct_world, "env_vis_model")

        sub = layout.column(align=True)
        sub.label("Visible environment:")
        sub.prop(oct_world, "env_vis_backplate")
        sub.prop(oct_world, "env_vis_reflections")
        sub.prop(oct_world, "env_vis_refractions")


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

        row = layout.row()
        row.prop(opsys, "min_curvature")

        layout.label(text="Thickness:")
        row = layout.row(align=True)
        row.prop(opsys, "root_width")
        row.prop(opsys, "tip_width")

        layout.label(text="W coordinate:")
        row = layout.row(align=True)
        row.prop(opsys, "w_min")
        row.prop(opsys, "w_max")


def draw_device(self, context):
    scene = context.scene
    layout = self.layout

    if scene.render.engine == 'octane':
        oct_scene = scene.octane

        sub = layout.row()
        sub.prop(oct_scene, "anim_mode")

        import _octane
        box = layout.box()
        box.label(text="Octane GPUs:")
        col = box.column(align=True)
        devices = _octane.octane_devices(scene.as_pointer())
        i = 0
        for device in devices:
            sub = col.row(align=True)
            sub.prop(oct_scene, "devices", index=i, text=device)
            i = i + 1

        sub = layout.row()
        sub.prop(oct_scene, "viewport_hide")
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
    exclude_panels = {
        'DATA_PT_area',
        'DATA_PT_camera_dof',
        'DATA_PT_falloff_curve',
        'DATA_PT_lamp',
        'DATA_PT_preview',
        'DATA_PT_shadow',
        'DATA_PT_spot',
        'DATA_PT_sunsky',
        'MATERIAL_PT_context_material',
        'MATERIAL_PT_diffuse',
        'MATERIAL_PT_flare',
        'MATERIAL_PT_halo',
        'MATERIAL_PT_mirror',
        'MATERIAL_PT_options',
        'MATERIAL_PT_pipeline',
        'MATERIAL_PT_preview',
        'MATERIAL_PT_shading',
        'MATERIAL_PT_shadow',
        'MATERIAL_PT_specular',
        'MATERIAL_PT_sss',
        'MATERIAL_PT_strand',
        'MATERIAL_PT_transp',
        'MATERIAL_PT_volume_density',
        'MATERIAL_PT_volume_integration',
        'MATERIAL_PT_volume_lighting',
        'MATERIAL_PT_volume_options',
        'MATERIAL_PT_volume_shading',
        'MATERIAL_PT_volume_transp',
        'RENDERLAYER_PT_layer_options',
        'RENDERLAYER_PT_layer_passes',
        'RENDERLAYER_PT_views',
        'RENDER_PT_antialiasing',
        'RENDER_PT_bake',
        'RENDER_PT_motion_blur',
        'RENDER_PT_performance',
        'RENDER_PT_post_processing',
        'RENDER_PT_shading',
        'SCENE_PT_simplify',
        'TEXTURE_PT_context_texture',
        'WORLD_PT_ambient_occlusion',
        'WORLD_PT_environment_lighting',
        'WORLD_PT_gather',
        'WORLD_PT_indirect_lighting',
        'WORLD_PT_mist',
        'WORLD_PT_preview',
        'WORLD_PT_world'
        }

    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels


def register():
    bpy.types.RENDER_PT_render.append(draw_device)
    bpy.types.VIEW3D_HT_header.append(draw_pause)

    for panel in get_panels():
        panel.COMPAT_ENGINES.add('octane')


def unregister():
    bpy.types.RENDER_PT_render.remove(draw_device)
    bpy.types.VIEW3D_HT_header.remove(draw_pause)

    for panel in get_panels():
        if 'octane' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('octane')
