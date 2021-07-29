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
from bpy_extras.node_utils import find_node_input
from . import engine
from . import converters

def panel_node_draw(layout, id_data, output_type, input_name):
    if not id_data.use_nodes:
        layout.operator("octane.use_shading_nodes", icon='NODETREE')
        return False

    ntree = id_data.node_tree

    node = ntree.get_output_node('octane')
    if node:
        input = find_node_input(node, input_name)
        if input:
            layout.template_node_view(ntree, node, input)
        else:
            layout.label(text="Incompatible output node")
    else:
        layout.label(text="No output node")

    return True

def osl_node_draw(layout, node_tree_name, node_name):
    if bpy.data.materials:      
        for mat in bpy.data.materials.values():
            if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                continue
            if mat.name != node_tree_name:
                continue
            for node in mat.node_tree.nodes.values():
                if node.name == node_name:
                    layout.label(text="Octane Geometric Node")
                    layout.template_node_view(mat.node_tree, node, None)
                    return True
    layout.label(text="No Octane Geometric Node")
    return False

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
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES


class OCTANE_RENDER_PT_kernel(OctaneButtonsPanel, Panel):
    bl_label = "Octane kernel"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        oct_scene = scene.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_kernel_presets", text=bpy.types.OCTANE_MT_kernel_presets.bl_label)
        row.operator("render.octane_kernel_preset_add", text="", icon="ADD")
        row.operator("render.octane_kernel_preset_add", text="", icon="REMOVE").remove_active = True

        def draw_samples():
            col.prop(oct_scene, "max_samples")
            col.prop(oct_scene, "max_preview_samples")           

        def draw_clay_mode():  
            col.prop(oct_scene, "clay_mode")

        def draw_toon_shadow_ambient():           
            col.prop(oct_scene, "toon_shadow_ambient")                

        def draw_parallel_samples():
            col.prop(oct_scene, "parallel_samples")           

        def draw_tile_samples():
            col.prop(oct_scene, "max_tile_samples")

        def draw_max_subdivision_level():
            col.prop(oct_scene, "max_subdivision_level")            

        def draw_ray_epsilon_and_filter_size():
            col.prop(oct_scene, "ray_epsilon")
            col.prop(oct_scene, "filter_size")
            
        def draw_ao_dist():
            col.prop(oct_scene, "ao_dist")

        def draw_alpha_shadows():
            col.prop(oct_scene, "alpha_shadows")

        def draw_irradiance_mode():
            col.prop(oct_scene, "irradiance_mode")      

        def draw_alpha_channel():
            col.prop(oct_scene, "alpha_channel")

        def draw_keep_environment():
            col.prop(oct_scene, "keep_environment")               

        def draw_path_term_power():
            col.prop(oct_scene, "path_term_power")  

        def draw_coherent_ratio():
            col.prop(oct_scene, "coherent_ratio")  

        def draw_static_noise():
            col.prop(oct_scene, "static_noise")  

        def draw_minimize_net_traffic():
            col.prop(oct_scene, "minimize_net_traffic")  

        def draw_emulate_old_volume_behavior():
            col.prop(oct_scene, "emulate_old_volume_behavior")  

        def draw_caustic_blur():
            col.prop(oct_scene, "caustic_blur")  

        def draw_gi_clamp():
            col.prop(oct_scene, "gi_clamp")              

        def draw_adaptive_sampling():
            col.prop(oct_scene, "adaptive_sampling")
            col.prop(oct_scene, "adaptive_noise_threshold")
            col.prop(oct_scene, "adaptive_min_samples")
            col.prop(oct_scene, "adaptive_group_pixels")            
            col.prop(oct_scene, "adaptive_expected_exposure")
            
        def draw_deep_image():
            col.prop(oct_scene, "deep_image")
            col.prop(oct_scene, "deep_render_passes")
            col.prop(oct_scene, "max_depth_samples")
            col.prop(oct_scene, "depth_tolerance")            

        def draw_max_diffuse_glossy_scatter_depth():
            col.prop(oct_scene, "max_diffuse_depth")
            col.prop(oct_scene, "max_glossy_depth")
            col.prop(oct_scene, "max_scatter_depth")            

        def draw_ai_light_and_light():
            col.prop(oct_scene, "ai_light_enable")
            col.prop(oct_scene, "ai_light_update") 
            col.prop(oct_scene, "light_ids_action")
            col.label(text="Light IDs:")
            row = col.row(align=True)
            row.prop(oct_scene, "light_id_sunlight", text="S", toggle=True)
            row.prop(oct_scene, "light_id_env", text="E", toggle=True)
            row.prop(oct_scene, "light_id_pass_1", text="1", toggle=True)
            row.prop(oct_scene, "light_id_pass_2", text="2", toggle=True)
            row.prop(oct_scene, "light_id_pass_3", text="3", toggle=True)        
            row.prop(oct_scene, "light_id_pass_4", text="4", toggle=True)
            row.prop(oct_scene, "light_id_pass_5", text="5", toggle=True)
            row.prop(oct_scene, "light_id_pass_6", text="6", toggle=True)
            row.prop(oct_scene, "light_id_pass_7", text="7", toggle=True)
            row.prop(oct_scene, "light_id_pass_8", text="8", toggle=True)   
            col.label(text="Light linking invert:")
            row = col.row(align=True)
            row.prop(oct_scene, "light_id_sunlight_invert", text="S", toggle=True)
            row.prop(oct_scene, "light_id_env_invert", text="E", toggle=True)
            row.prop(oct_scene, "light_id_pass_1_invert", text="1", toggle=True)
            row.prop(oct_scene, "light_id_pass_2_invert", text="2", toggle=True)
            row.prop(oct_scene, "light_id_pass_3_invert", text="3", toggle=True)        
            row.prop(oct_scene, "light_id_pass_4_invert", text="4", toggle=True)
            row.prop(oct_scene, "light_id_pass_5_invert", text="5", toggle=True)
            row.prop(oct_scene, "light_id_pass_6_invert", text="6", toggle=True)
            row.prop(oct_scene, "light_id_pass_7_invert", text="7", toggle=True)
            row.prop(oct_scene, "light_id_pass_8_invert", text="8", toggle=True)                

        col = layout.column(align=True)
        col.prop(oct_scene, "kernel_type")

        if oct_scene.kernel_type in ('0', '1', ):            
            # Direct lighting kernel
            col = layout.column(align=True)
            draw_clay_mode()

            box = layout.box()
            box.label(text="Quality")
            col = box.column(align=True)
            draw_samples()
            col.prop(oct_scene, "gi_mode")     
            col.prop(oct_scene, "specular_depth")
            col.prop(oct_scene, "glossy_depth")
            col.prop(oct_scene, "diffuse_depth")
            draw_ray_epsilon_and_filter_size()
            draw_ao_dist()
            col.prop_search(oct_scene, "ao_texture", bpy.data, "textures")   
            draw_alpha_shadows()
            draw_irradiance_mode()
            draw_max_subdivision_level()

            box = layout.box()
            box.label(text="Alpha channel")            
            col = box.column(align=True)   
            draw_alpha_channel()
            draw_keep_environment()  

            box = layout.box()
            box.label(text="Light")            
            col = box.column(align=True)     
            draw_ai_light_and_light()  

            box = layout.box()     
            box.label(text="Sampling")            
            col = box.column(align=True)  
            draw_path_term_power()
            draw_coherent_ratio()
            draw_static_noise()
            draw_parallel_samples()
            draw_tile_samples()
            draw_minimize_net_traffic()

            box = layout.box()
            box.label(text="Adaptive sampling")            
            col = box.column(align=True)  
            draw_adaptive_sampling()

            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image() 

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            box = layout.box()
            box.label(text="Compatibility settings")            
            col = box.column(align=True)                  
            draw_emulate_old_volume_behavior()             
        elif oct_scene.kernel_type == '2':
            # Path tracing kernel
            col = layout.column(align=True)
            draw_clay_mode()

            box = layout.box()
            box.label(text="Quality")
            col = box.column(align=True)
            draw_samples()
            draw_max_diffuse_glossy_scatter_depth()
            draw_ray_epsilon_and_filter_size()
            draw_alpha_shadows()
            draw_caustic_blur()
            draw_gi_clamp()
            draw_irradiance_mode()
            draw_max_subdivision_level()

            box = layout.box()
            box.label(text="Alpha channel")            
            col = box.column(align=True)   
            draw_alpha_channel()
            draw_keep_environment()  

            box = layout.box()
            box.label(text="Light")            
            col = box.column(align=True)     
            draw_ai_light_and_light()              

            box = layout.box()     
            box.label(text="Sampling")            
            col = box.column(align=True)  
            draw_path_term_power()
            draw_coherent_ratio()
            draw_static_noise()
            draw_parallel_samples()
            draw_tile_samples()
            draw_minimize_net_traffic()

            box = layout.box()
            box.label(text="Adaptive sampling")            
            col = box.column(align=True)  
            draw_adaptive_sampling()     
            
            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()                    

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            box = layout.box()
            box.label(text="Compatibility settings")            
            col = box.column(align=True)                  
            draw_emulate_old_volume_behavior()   
        elif oct_scene.kernel_type == '3':
            # PMC kernel
            col = layout.column(align=True)
            draw_clay_mode()

            box = layout.box()
            box.label(text="Quality")
            col = box.column(align=True)
            draw_samples()
            draw_max_diffuse_glossy_scatter_depth()
            draw_ray_epsilon_and_filter_size()
            draw_alpha_shadows()
            draw_caustic_blur()
            draw_gi_clamp()
            draw_irradiance_mode()
            draw_max_subdivision_level()

            box = layout.box()
            box.label(text="Alpha channel")            
            col = box.column(align=True)   
            draw_alpha_channel()
            draw_keep_environment()  

            box = layout.box()
            box.label(text="Light")            
            col = box.column(align=True)     
            draw_ai_light_and_light()     

            box = layout.box()     
            box.label(text="Sampling")            
            col = box.column(align=True)  
            draw_path_term_power()
            col.prop(oct_scene, "exploration")
            col.prop(oct_scene, "direct_light_importance")
            col.prop(oct_scene, "max_rejects")
            col.prop(oct_scene, "parallelism")
            col.prop(oct_scene, "work_chunk_size")

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            box = layout.box()
            box.label(text="Compatibility settings")            
            col = box.column(align=True)                  
            draw_emulate_old_volume_behavior() 
        elif oct_scene.kernel_type == '4':
            # Info channels kernel
            box = layout.box()
            box.label(text="Quality")
            col = box.column(align=True)
            draw_samples()
            col.prop(oct_scene, "info_channel_type")
            draw_ray_epsilon_and_filter_size()
            draw_ao_dist()
            draw_alpha_shadows()
            col.prop(oct_scene, "opacity_threshold")
            col.prop(oct_scene, "zdepth_max")
            col.prop(oct_scene, "uv_max")
            col.prop(oct_scene, "info_pass_uv_coordinate_selection")
            col.prop(oct_scene, "max_speed")
            col.prop(oct_scene, "sampling_mode")
            col.prop(oct_scene, "bump_normal_mapping")
            col.prop(oct_scene, "wf_bkface_hl")  
            draw_max_subdivision_level()

            box = layout.box()
            box.label(text="Alpha channel")            
            col = box.column(align=True)   
            draw_alpha_channel()

            box = layout.box()     
            box.label(text="Sampling")            
            col = box.column(align=True)  
            draw_parallel_samples()
            draw_tile_samples()
            draw_minimize_net_traffic()

            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()                
        else:
            pass



class OCTANE_RENDER_PT_server(OctaneButtonsPanel, Panel):
    bl_label = "Octane Server"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        oct_scene = scene.octane

        box = layout.box()
        box.label(text="Octane Settings:")
        sub = box.row()
        sub.prop(oct_scene, "priority_mode")        
        sub = box.row()
        sub.prop(oct_scene, "prefer_tonemap")               
        # sub = box.row()
        # sub.operator("octane.open_octanedb", text="Open OctaneDB")        
        sub = box.row()
        sub.operator("octane.show_octane_node_graph", text="Show Octane Node Graph")
        sub = box.row()
        sub.operator("octane.show_octane_log", text="Show Octane Log")
        sub = box.row()
        sub.operator("octane.stop_render", text="Stop Render")
        sub = box.row()
        sub.operator("octane.show_octane_device_setting", text="Device Preferences")
        sub.operator("octane.show_octane_network_preference", text="Network Preferences")
        sub = box.row()
        sub.operator("octane.activate", text="Activation state")

class OCTANE_RENDER_PT_out_of_core(OctaneButtonsPanel, Panel):
    bl_label = "Octane Out Of Core"
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


class OCTANE_RENDER_PT_motion_blur(OctaneButtonsPanel, Panel):
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
        row.prop(context.scene.octane, "mb_direction")
        row = layout.row()
        row.prop(context.scene.octane, "shutter_time")
        row = layout.row()
        row.prop(context.scene.octane, "subframe_start")
        row = layout.row()
        row.prop(context.scene.octane, "subframe_end")


class VIEW3D_PT_octimager(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Camera Imager(Preview Mode)"    
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}        

    @classmethod
    def poll(cls, context):
        return context.space_data and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "hdr_tonemap_preview_enable", text="")

    def draw(self, context):
        layout = self.layout

        view = context.space_data
        oct_cam = context.scene.oct_view_cam

        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dimager_presets", text=OCTANE_MT_3dimager_presets.bl_label)
        row.operator("render.octane_3dimager_preset_add", text="", icon="ADD")
        row.operator("render.octane_3dimager_preset_add", text="", icon="REMOVE").remove_active = True

        layout.active = bool(context.scene.octane.use_preview_setting_for_camera_imager or view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        sub = layout.column(align=True)
        sub.prop(context.scene.octane, "use_preview_setting_for_camera_imager")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "camera_imager_order")
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
        sub.prop(oct_cam, "custom_lut")
        sub.prop(oct_cam, "lut_strength")

        box = layout.box()
        box.label(text="Spectral AI Denoiser:")
        sub = box.column(align=True)

        sub.prop(oct_cam, 'enable_denoising')
        sub.prop(oct_cam, 'denoise_volumes')
        sub.prop(oct_cam, 'denoise_on_completion')
        sub.prop(oct_cam, 'min_denoiser_samples')
        sub.prop(oct_cam, 'max_denoiser_interval')
        sub.prop(oct_cam, 'denoiser_blend')

        box = layout.box()
        box.label(text="AI Up-Sampler:")
        sub = box.column(align=True)

        sub.prop(oct_cam.ai_up_sampler, 'sample_mode')
        sub.prop(oct_cam.ai_up_sampler, 'enable_ai_up_sampling')
        sub.prop(oct_cam.ai_up_sampler, 'up_sampling_on_completion')
        sub.prop(oct_cam.ai_up_sampler, 'min_up_sampler_samples')
        sub.prop(oct_cam.ai_up_sampler, 'max_up_sampler_interval')


class VIEW3D_PT_Octane_Postprocessing(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Postprocess(Preview Mode)"
    bl_category = "Octane"         
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'octane'}          

    @classmethod
    def poll(cls, context):
        return context.space_data and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.scene.oct_view_cam, "postprocess", text="")

    def draw(self, context):
        layout = self.layout
        view = context.space_data
        oct_cam = context.scene.oct_view_cam

        layout.active = bool(context.scene.octane.use_preview_post_process_setting or view.region_3d.view_perspective != 'CAMERA' or view.region_quadviews)
        sub = layout.column(align=True)
        sub.prop(context.scene.octane, "use_preview_post_process_setting")
        sub.prop(oct_cam, "cut_off")
        sub.prop(oct_cam, "bloom_power")
        sub.prop(oct_cam, "glare_power")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "glare_ray_count")
        sub.prop(oct_cam, "glare_angle")
        sub.prop(oct_cam, "glare_blur")
        sub.prop(oct_cam, "spectral_intencity")
        sub.prop(oct_cam, "spectral_shift")


class OCTANE_CAMERA_PT_cam(OctaneButtonsPanel, Panel):
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
        sub.prop(oct_cam, "keep_upright")

        col = layout.column(align=True)
        col.active = (cam.type != 'PANO')
        col.prop(oct_cam, "distortion")
        col.prop(oct_cam, "pixel_aspect")
        col.prop(oct_cam, "persp_corr")
        
        sub = layout.row(align=True)
        sub.prop(oct_cam, "use_fstop")
        sub.prop(oct_cam, "fstop")        

        box = layout.box()
        box.label(text="Depth of field:")
        sub = box.column(align=True)
        sub.prop(oct_cam, "autofocus")
        sub = box.row(align=True)
        sub.active = oct_cam.autofocus is False
        sub.prop(cam.dof, "focus_object", text="")
        sub = box.row(align=True)
        sub.active = oct_cam.autofocus is False and cam.dof.focus_object is None
        sub.prop(cam.dof, "focus_distance", text="Distance")
        sub = box.column(align=True)
        sub.prop(oct_cam, "aperture")
        sub.prop(oct_cam, "aperture_aspect")
        sub.prop(oct_cam, "aperture_edge")        
        sub.prop(oct_cam, "bokeh_sidecount")
        sub.prop(oct_cam, "bokeh_rotation")
        sub.prop(oct_cam, "bokeh_roundedness")

        box = layout.box()
        box.label(text="Stereo:")
        col = box.column(align=True)
        sub = box.row()
        sub.active = (cam.type != 'PANO')
        sub.prop(oct_cam, "stereo_mode")
        sub = box.row()
        #sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '1')
        sub.prop(oct_cam, "stereo_out")
        sub = box.row()
        #sub.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '1')
        sub.prop(oct_cam, "stereo_dist")
        sub.prop(oct_cam, "stereo_swap_eyes")
        sub = box.column(align=True)
        #sub.active = (cam.type == 'PANO')
        sub.prop(oct_cam, "stereo_dist_falloff")
        sub.prop(oct_cam, "blackout_lat")
        col = box.column(align=True)
        #col.active = (cam.type == 'PANO' or oct_cam.stereo_mode != '1')
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

        box = layout.box()
        box.label(text = "OSL Camera:")
        col = box.column(align = True)

        sub = col.row(align = True)
        sub.prop_search(oct_cam.osl_camera_node_collections, "osl_camera_material_tree", bpy.data, "materials")
        sub = col.row(align = True)        
        sub.prop_search(oct_cam.osl_camera_node_collections, "osl_camera_node", oct_cam.osl_camera_node_collections, "osl_camera_nodes")        
        sub.operator('update.osl_camera_nodes', text = 'Update')
        #sub.prop(oct_cam, 'osl_camera_node1')


class OCTANE_CAMERA_PT_imager(OctaneButtonsPanel, Panel):
    bl_label = "Octane Camera Imager(Render Mode)"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "hdr_tonemap_render_enable", text="")

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        row = layout.row(align=True)
        row.menu("OCTANE_MT_imager_presets", text=OCTANE_MT_imager_presets.bl_label)
        row.operator("render.octane_imager_preset_add", text="", icon="ADD")
        row.operator("render.octane_imager_preset_add", text="", icon="REMOVE").remove_active = True

        sub = layout.row()
        sub.prop(oct_cam, "camera_imager_order")

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
        sub.prop(oct_cam, "custom_lut")
        sub.prop(oct_cam, "lut_strength")

        box = layout.box()
        box.label(text="Spectral AI Denoiser:")
        sub = box.column(align=True)

        sub.prop(oct_cam, 'enable_denoising')
        sub.prop(oct_cam, 'denoise_volumes')
        sub.prop(oct_cam, 'denoise_on_completion')
        sub.prop(oct_cam, 'min_denoiser_samples')
        sub.prop(oct_cam, 'max_denoiser_interval')
        sub.prop(oct_cam, 'denoiser_blend')

        box = layout.box()
        box.label(text="AI Up-Sampler:")
        sub = box.column(align=True)

        sub.prop(oct_cam.ai_up_sampler, 'sample_mode')
        sub.prop(oct_cam.ai_up_sampler, 'enable_ai_up_sampling')
        sub.prop(oct_cam.ai_up_sampler, 'up_sampling_on_completion')
        sub.prop(oct_cam.ai_up_sampler, 'min_up_sampler_samples')
        sub.prop(oct_cam.ai_up_sampler, 'max_up_sampler_interval')


class OCTANE_CAMERA_PT_post(OctaneButtonsPanel, Panel):
    bl_label = "Octane postprocessor"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.camera and OctaneButtonsPanel.poll(context)

    def draw_header(self, context):
        self.layout.prop(context.camera.octane, "postprocess", text="")

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        sub = layout.column(align=True)
        sub.prop(oct_cam, "cut_off")
        sub.prop(oct_cam, "bloom_power")
        sub.prop(oct_cam, "glare_power")
        sub = layout.column(align=True)
        sub.prop(oct_cam, "glare_ray_count")
        sub.prop(oct_cam, "glare_angle")
        sub.prop(oct_cam, "glare_blur")
        sub.prop(oct_cam, "spectral_intencity")
        sub.prop(oct_cam, "spectral_shift")


class OCTANE_PT_mesh_properties(OctaneButtonsPanel, Panel):
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
        sub.operator("octane.set_meshes_type", text="")
        
        sub = layout.row(align=True)
        sub.prop(cdata, "force_load_vertex_normals")

        # box = layout.box()
        # box.label(text="Scatter Groups:")
        # sub = box.row(align=True)
        # sub.prop(cdata, "is_scatter_group_source", text="Used as source for current group")
        # sub = box.row(align=True)
        # sub.prop(cdata, "scatter_group_id")
        # sub.prop(cdata, "scatter_instance_id")

        sub = layout.row(align=True)
        sub.prop(cdata, "winding_order")
        sub = layout.row(align=True)
        sub.prop(cdata, "infinite_plane")        
        for modifier in context.object.modifiers:
            if modifier.type in ('SUBSURF', ):                
                sub = layout.row(align=True)        
                sub.prop(cdata, "tessface_in_preview")
                break
        # sub = layout.row(align=True)
        # sub.active = cdata.layer_number != 0
        # sub.prop(cdata, "layer_number")
        # sub = layout.row(align=True)
        # sub.prop(cdata, "baking_group_id")
        # sub = layout.row(align=True)
        # sub.prop(cdata, "rand_color_seed")
        # sub = layout.row(align=True)
        # sub.label(text="Light pass mask:")
        # sub = layout.row(align=True)
        # row = sub.row(align=True)        
        # row.prop(cdata, "light_id_sunlight", text="S", toggle=True)
        # row.prop(cdata, "light_id_env", text="E", toggle=True)
        # row.prop(cdata, "light_id_pass_1", text="1", toggle=True)
        # row.prop(cdata, "light_id_pass_2", text="2", toggle=True)
        # row.prop(cdata, "light_id_pass_3", text="3", toggle=True)        
        # row.prop(cdata, "light_id_pass_4", text="4", toggle=True)
        # row.prop(cdata, "light_id_pass_5", text="5", toggle=True)
        # row.prop(cdata, "light_id_pass_6", text="6", toggle=True)
        # row.prop(cdata, "light_id_pass_7", text="7", toggle=True)
        # row.prop(cdata, "light_id_pass_8", text="8", toggle=True)  
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

        # box = layout.box()
        # box.label(text="Visibility:")
        # sub = box.column(align=True)
        # sub.prop(cdata, "vis_general")
        # sub.prop(cdata, "vis_cam")
        # sub.prop(cdata, "vis_shadow")

        box = layout.box()
        box.label(text="Volume properties:")
        sub = box.column(align=True)     
        sub.prop(cdata, "is_octane_vdb")
        sub.prop(cdata, "vdb_sdf")
        sub.prop(cdata, "imported_openvdb_file_path")
        sub = box.row(align=True)
        sub.prop(cdata, "openvdb_frame_start")
        sub.prop(cdata, "openvdb_frame_end")   
        sub = box.row(align=True)     
        sub.prop(cdata, "openvdb_frame_start_playing_at")
        sub.prop(cdata, "openvdb_frame_speed_mutiplier")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_iso")
        sub.prop(cdata, "vdb_abs_scale")
        sub.prop(cdata, "vdb_emiss_scale")
        sub.prop(cdata, "vdb_scatter_scale")
        sub.prop(cdata, "vdb_vel_scale")

        box = layout.box()
        box.label(text="Octane Geometric Node:")        
        col = box.column(align = True)
        sub = col.row(align = True)
        sub.prop_search(cdata.octane_geo_node_collections, "node_graph_tree", bpy.data, "materials")
        sub.operator('update.octane_geo_nodes', icon='FILE_REFRESH')
        sub = col.row(align = True)        
        sub.prop_search(cdata.octane_geo_node_collections, "osl_geo_node", cdata.octane_geo_node_collections, "osl_geo_nodes")            
        osl_node_draw(box, str(cdata.octane_geo_node_collections.node_graph_tree), str(cdata.octane_geo_node_collections.osl_geo_node))

        box = layout.box()
        box.label(text="Orbx properties:")   
        sub = box.column(align=True)     
        sub.prop(cdata, "imported_orbx_file_path")


class OCTANE_RENDER_PT_HairSettings(OctaneButtonsPanel, Panel):
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
        row.prop(psys, "octane_min_curvature")

        layout.label(text="Thickness:")
        row = layout.row(align=True)
        row.prop(psys, "octane_root_width")
        row.prop(psys, "octane_tip_width")        

        layout.label(text="W coordinate:")
        row = layout.row(align=True)  
        row.prop(psys, "octane_w_min")
        row.prop(psys, "octane_w_max")            


class OCTANE_PT_context_material(OctaneButtonsPanel, Panel):
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
            is_sortable = len(ob.material_slots) > 1
            rows = 1
            if (is_sortable):
                rows = 4

            row = layout.row()

            row.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=rows)

            col = row.column(align=True)
            col.operator("object.material_slot_add", icon='ADD', text="")
            col.operator("object.material_slot_remove", icon='REMOVE', text="")

            col.menu("MATERIAL_MT_context_menu", icon='DOWNARROW_HLT', text="")

            if is_sortable:
                col.separator()

                col.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
                col.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

            if ob.mode == 'EDIT':
                row = layout.row(align=True)
                row.operator("object.material_slot_assign", text="Assign")
                row.operator("object.material_slot_select", text="Select")
                row.operator("object.material_slot_deselect", text="Deselect")

        split = layout.split(factor=0.65)

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


class OCTANE_MATERIAL_PT_surface(OctaneButtonsPanel, Panel):
    bl_label = "Surface"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        mat = context.material
        if not mat:
            return
        if not panel_node_draw(layout, mat, 'OUTPUT_MATERIAL', 'Surface'):
            layout.prop(mat, "diffuse_color")


class OCTANE_MATERIAL_PT_volume(OctaneButtonsPanel, Panel):
    bl_label = "Volume"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        mat = context.material
        if not mat:
            return
        if not panel_node_draw(layout, mat, 'OUTPUT_MATERIAL', 'Volume'):
            layout.prop(mat, "diffuse_color")


class OCTANE_MATERIAL_PT_settings(OctaneButtonsPanel, Panel):
    bl_label = "Settings"
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("octane.save_as_octanedb", text="Save As OctaneDB")


class OCTANE_MATERIAL_PT_converters(OctaneButtonsPanel, Panel):
    bl_label = "Converters"
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context) and converters.is_converter_applicable(context.material)

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("octane.convert_to_octane_material", text="Convert To Octane Materials")


class OCTANE_RENDER_PT_passes(OctaneButtonsPanel, Panel):
    bl_label = "Passes"
    bl_context = "view_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        layout = self.layout
        row = layout.row()
        row.prop(octane_view_layer, "current_preview_pass_type")


class OCTANE_RENDER_PT_passes_beauty(OctaneButtonsPanel, Panel):
    bl_label = "Beauty"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_beauty")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_emitters")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_env")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_sss")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_shadow")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_irradiance")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_noise")      
        
        layout.row().separator()
        
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(view_layer, "use_pass_oct_diff", text="Diffuse", toggle=True)
        row.prop(view_layer, "use_pass_oct_diff_dir", text="Direct", toggle=True)
        row.prop(view_layer, "use_pass_oct_diff_indir", text="Indirect", toggle=True)        
        row.prop(view_layer, "use_pass_oct_diff_filter", text="Filter", toggle=True)         

        layout.row().separator()

        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(view_layer, "use_pass_oct_reflect", text="Reflection", toggle=True)
        row.prop(view_layer, "use_pass_oct_reflect_dir", text="Direct", toggle=True)
        row.prop(view_layer, "use_pass_oct_reflect_indir", text="Indirect", toggle=True)        
        row.prop(view_layer, "use_pass_oct_reflect_filter", text="Filter", toggle=True)     

        layout.row().separator()

        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(view_layer, "use_pass_oct_refract", text="Refraction", toggle=True)
        row.prop(view_layer, "use_pass_oct_refract_filter", text="Refract Filter", toggle=True)

        layout.row().separator()

        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(view_layer, "use_pass_oct_transm", text="Transmission", toggle=True)
        row.prop(view_layer, "use_pass_oct_transm_filter", text="Transm Filter", toggle=True)        

        layout.row().separator()

        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(view_layer, "use_pass_oct_volume", text="Volume", toggle=True)
        row.prop(view_layer, "use_pass_oct_vol_mask", text="Mask", toggle=True)
        row.prop(view_layer, "use_pass_oct_vol_emission", text="Emission", toggle=True)        
        row.prop(view_layer, "use_pass_oct_vol_z_front", text="ZFront", toggle=True)
        row.prop(view_layer, "use_pass_oct_vol_z_back", text="ZBack", toggle=True)


class OCTANE_RENDER_PT_passes_denoiser(OctaneButtonsPanel, Panel):
    bl_label = "Denoiser"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_beauty", text="Beauty")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_diff_dir", text="DiffDir")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_diff_indir", text="DiffIndir")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_reflect_dir", text="ReflectDir")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_reflect_indir", text="ReflectIndir")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_emission", text="Emission")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_remainder", text="Remainder")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_vol", text="Volume")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_vol_emission", text="VolEmission")


class OCTANE_RENDER_PT_passes_postprocessing(OctaneButtonsPanel, Panel):
    bl_label = "Post processing"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_postprocess", text="Post processing")
        col = flow.column()
        col.prop(octane_view_layer, "pass_pp_env")


class OCTANE_RENDER_PT_passes_render_layer(OctaneButtonsPanel, Panel):
    bl_label = "Render layer"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=3, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_shadows", text="Shadow")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_black_shadow", text="BlackShadow")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_reflections", text="Reflections")


class OCTANE_RENDER_PT_passes_lighting(OctaneButtonsPanel, Panel):
    bl_label = "Lighting"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=3, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_ambient_light", text="Ambient")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_ambient_light_dir", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_ambient_light_indir", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_sunlight", text="Sunlight")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_sunlight_dir", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_sunlight_indir", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_1", text="Light Pass 1")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_1", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_1", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_2", text="Light Pass 2")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_2", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_2", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_3", text="Light Pass 3")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_3", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_3", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_4", text="Light Pass 4")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_4", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_4", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_5", text="Light Pass 5")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_5", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_5", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_6", text="Light Pass 6")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_6", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_6", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_7", text="Light Pass 7")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_7", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_7", text="Indirect")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_pass_8", text="Light Pass 8")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_dir_pass_8", text="Direct")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_light_indir_pass_8", text="Indirect")


class OCTANE_RENDER_PT_passes_cryptomatte(OctaneButtonsPanel, Panel):
    bl_label = "Cryptomatte"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_instance_id", text="Instance ID")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_mat_node_name", text="MatNodeName")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_mat_node", text="MatNode")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_mat_pin_node", text="MatPinNode")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_obj_node_name", text="ObjNodeName")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_obj_node", text="ObjNode")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_obj_pin_node", text="ObjPinNode")

        layout.row().separator()
        row = layout.row(align=True)
        row.prop(octane_view_layer, "cryptomatte_pass_channels")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "cryptomatte_seed_factor")


class OCTANE_RENDER_PT_passes_info(OctaneButtonsPanel, Panel):
    bl_label = "Info"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_z_depth")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_position")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_uv")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_tex_tangent")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_motion_vector")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_mat_id")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_obj_id")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_obj_layer_color")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_baking_group_id")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_light_pass_id")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_render_layer_id")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_render_layer_mask")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_wireframe")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_info_ao")

        layout.row().separator()

        split = layout.split(factor=0.15)
        split.use_property_split = False
        split.label(text="Normal")
        row = split.row(align=True)       
        row.prop(view_layer, "use_pass_oct_info_geo_normal", text="Geometric", toggle=True)         
        row.prop(view_layer, "use_pass_oct_info_smooth_normal", text="Smooth", toggle=True)
        row.prop(view_layer, "use_pass_oct_info_shading_normal", text="Shading", toggle=True)
        row.prop(view_layer, "use_pass_oct_info_tangent_normal", text="Tangent", toggle=True)

        layout.row().separator()
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_max_samples")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_sampling_mode")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_z_depth_max")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_uv_max")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_uv_coordinate_selection")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_max_speed")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_ao_distance")                        
        row = layout.row(align=True)
        row.prop(octane_view_layer, "info_pass_alpha_shadows")       


class OCTANE_RENDER_PT_passes_material(OctaneButtonsPanel, Panel):
    bl_label = "Material"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_mat_opacity")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_mat_roughness")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_mat_ior")

        layout.row().separator()

        split = layout.split(factor=0.15)
        split.use_property_split = False
        split.label(text="Filter")
        row = split.row(align=True)       
        row.prop(view_layer, "use_pass_oct_mat_diff_filter_info", text="Diffuse", toggle=True)         
        row.prop(view_layer, "use_pass_oct_mat_reflect_filter_info", text="Reflection", toggle=True)
        row.prop(view_layer, "use_pass_oct_mat_refract_filter_info", text="Refraction", toggle=True)
        row.prop(view_layer, "use_pass_oct_mat_transm_filter_info", text="Transmission", toggle=True)


class OCTANE_RENDER_PT_octane_layers(OctaneButtonsPanel, Panel):
    bl_label = "Octane render layers(Global)"
    bl_context = "view_layer"
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


class OCTANE_WORLD_PT_environment(OctaneButtonsPanel, Panel):
    bl_label = "Environment"
    bl_context = "world"

    @classmethod
    def poll(cls, context):
        return (context.world or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        world = context.world
        if not world:
            return
        panel_node_draw(layout, world, 'OUTPUT_WORLD', 'Octane Environment')


class OCTANE_WORLD_PT_visible_environment(OctaneButtonsPanel, Panel):
    bl_label = "Visible Environment"
    bl_context = "world"

    @classmethod
    def poll(cls, context):
        return (context.world or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        world = context.world
        if not world:
            return
        panel_node_draw(layout, world, 'OUTPUT_WORLD', 'Octane VisibleEnvironment')


class OCTANE_LIGHT_PT_light(OctaneButtonsPanel, Panel):
    bl_label = "Light"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.light and OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        light = context.light
        oct_light = light.octane

        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()

        if light.type == 'SPOT':
            layout.label(text="Not supported.")
            return

        if light.type == 'SUN':
            layout.label(text="Used as Toon Directional Light.")                 
            return                    

        if light.type == 'POINT':
            layout.label(text="Used as Toon Point Light.")           
            return              

        if light.type == 'AREA':
            col.prop(light, "shape", text="Shape")
            sub = col.column(align=True)

            if light.shape in {'SQUARE', 'DISK'}:
                sub.prop(light, "size")
            elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                sub.prop(light, "size", text="Size X")
                sub.prop(light, "size_y", text="Y")
            return

        if light.type == 'MESH':            
            col.prop(oct_light, "light_mesh")
            col.prop(oct_light, "use_external_mesh")
            col.prop(oct_light, "external_mesh_file")
            return                                


class OCTANE_LIGHT_PT_nodes(OctaneButtonsPanel, Panel):
    bl_label = "Nodes"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return context.light and context.light.type in ('POINT', 'SUN', 'AREA', 'MESH') and \
            OctaneButtonsPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        light = context.light
        panel_node_draw(layout, light, 'OUTPUT_LIGHT', 'Surface')


class OCTANE_OBJECT_PT_octane_settings(OctaneButtonsPanel, Panel):
    bl_label = "Octane Settings"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (OctaneButtonsPanel.poll(context) and
                ob and ((ob.type in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LIGHT'}) or
                        (ob.instance_type == 'COLLECTION' and ob.instance_collection)))

    def draw(self, context):
        pass


class OCTANE_OBJECT_PT_octane_settings_object_layer(OctaneButtonsPanel, Panel):
    bl_label = "Object layer"
    bl_parent_id = "OCTANE_OBJECT_PT_octane_settings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout        
        scene = context.scene
        ob = context.object
        octane_object = ob.octane

        sub = layout.row(align=True)
        sub.active = octane_object.render_layer_id != 0
        sub.prop(octane_object, "render_layer_id")
        sub = layout.row(align=True)
        sub.prop(octane_object, "general_visibility")
        sub = layout.row(align=True)        
        sub.prop(octane_object, "camera_visibility")
        sub.prop(octane_object, "shadow_visibility")

        split = layout.split(factor=0.15)
        split.use_property_split = False
        split.label(text="Light pass mask")
        row = split.row(align=True)       
        row.prop(octane_object, "light_id_sunlight", text="S", toggle=True)
        row.prop(octane_object, "light_id_env", text="E", toggle=True)
        row.prop(octane_object, "light_id_pass_1", text="1", toggle=True)
        row.prop(octane_object, "light_id_pass_2", text="2", toggle=True)
        row.prop(octane_object, "light_id_pass_3", text="3", toggle=True)        
        row.prop(octane_object, "light_id_pass_4", text="4", toggle=True)
        row.prop(octane_object, "light_id_pass_5", text="5", toggle=True)
        row.prop(octane_object, "light_id_pass_6", text="6", toggle=True)
        row.prop(octane_object, "light_id_pass_7", text="7", toggle=True)
        row.prop(octane_object, "light_id_pass_8", text="8", toggle=True)        
        sub = layout.row(align=True)
        sub.prop(octane_object, "random_color_seed")
        sub = layout.row(align=True)
        sub.prop(octane_object, "color")        


class OCTANE_OBJECT_PT_octane_settings_baking_settings(OctaneButtonsPanel, Panel):
    bl_label = "Baking settings"
    bl_parent_id = "OCTANE_OBJECT_PT_octane_settings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout        
        scene = context.scene
        ob = context.object
        octane_object = ob.octane

        sub = layout.row(align=True)
        sub.prop(octane_object, "baking_group_id")
        sub = layout.row(align=True)
        sub.prop(octane_object, "baking_uv_transform_rz")        
        sub = layout.row(align=True)
        sub.prop(octane_object, "baking_uv_transform_sx")
        sub.prop(octane_object, "baking_uv_transform_sy")
        sub = layout.row(align=True)
        sub.prop(octane_object, "baking_uv_transform_tx")
        sub.prop(octane_object, "baking_uv_transform_ty")                 


class OCTANE_OBJECT_PT_motion_blur(OctaneButtonsPanel, Panel):
    bl_label = "Motion Blur"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        ob = context.object
        if OctaneButtonsPanel.poll(context) and ob:
            if ob.type in {'MESH', 'CURVE', 'CURVE', 'SURFACE', 'FONT', 'META', 'CAMERA'}:
                return True
            if ob.instance_type == 'COLLECTION' and ob.instance_collection:
                return True
        return False

    def draw_header(self, context):
        layout = self.layout

        rd = context.scene.render
        # scene = context.scene

        layout.active = rd.use_motion_blur

        ob = context.object

        layout.prop(ob.octane, "use_motion_blur", text="")

    def draw(self, context):
        layout = self.layout

        rd = context.scene.render
        # scene = context.scene

        ob = context.object

        layout.active = (rd.use_motion_blur and ob.octane.use_motion_blur)

        row = layout.row()
        if ob.type != 'CAMERA':
            row.prop(ob.octane, "use_deform_motion", text="Deformation")
        row.prop(ob.octane, "motion_steps", text="Steps")


def get_panels():
    exclude_panels = {
        "DATA_PT_light",
        "DATA_PT_area",
        "DATA_PT_camera_dof",
    }

    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels


classes = (
    OCTANE_MT_kernel_presets,
    OCTANE_MT_environment_presets,
    OCTANE_MT_vis_environment_presets,
    OCTANE_MT_imager_presets,
    OCTANE_MT_3dimager_presets,

    OCTANE_RENDER_PT_kernel,
    OCTANE_RENDER_PT_server,
    OCTANE_RENDER_PT_out_of_core,
    OCTANE_RENDER_PT_motion_blur,

    VIEW3D_PT_octimager,
    VIEW3D_PT_Octane_Postprocessing,
    OCTANE_CAMERA_PT_cam,
    OCTANE_CAMERA_PT_imager,
    OCTANE_CAMERA_PT_post,
    OCTANE_PT_mesh_properties,
    OCTANE_RENDER_PT_HairSettings,
    OCTANE_PT_context_material,
    OCTANE_MATERIAL_PT_surface,
    OCTANE_MATERIAL_PT_volume,
    OCTANE_MATERIAL_PT_settings,
    OCTANE_MATERIAL_PT_converters,

    OCTANE_RENDER_PT_passes,
    OCTANE_RENDER_PT_passes_beauty,
    OCTANE_RENDER_PT_passes_denoiser,
    OCTANE_RENDER_PT_passes_postprocessing,
    OCTANE_RENDER_PT_passes_render_layer,
    OCTANE_RENDER_PT_passes_lighting,
    OCTANE_RENDER_PT_passes_cryptomatte,
    OCTANE_RENDER_PT_passes_info,
    OCTANE_RENDER_PT_passes_material,
    OCTANE_RENDER_PT_octane_layers,

    OCTANE_WORLD_PT_environment,
    OCTANE_WORLD_PT_visible_environment,

    OCTANE_LIGHT_PT_light,
    OCTANE_LIGHT_PT_nodes,

    OCTANE_OBJECT_PT_octane_settings,
    OCTANE_OBJECT_PT_octane_settings_object_layer,
    OCTANE_OBJECT_PT_octane_settings_baking_settings,
    OCTANE_OBJECT_PT_motion_blur,
)

def register():
    from bpy.utils import register_class
    for panel in get_panels():
        panel.COMPAT_ENGINES.add('octane')

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for panel in get_panels():
        if 'octane' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('octane')

    for cls in classes:
        unregister_class(cls)
