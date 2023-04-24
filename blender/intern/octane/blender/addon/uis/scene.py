import bpy
import xml.etree.ElementTree as ET
from bpy.types import Panel, Menu, Operator
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility
from octane import core


class OCTANE_MT_kernel_presets(Menu):
    bl_label = "Kernel presets"
    preset_subdir = "octane/kernel"
    preset_operator = "script.execute_preset"
    COMPAT_ENGINES = {'octane'}
    draw = Menu.draw_preset


class OCTANE_RENDER_PT_kernel(common.OctanePropertyPanel, Panel):
    bl_label = "Octane kernel"
    bl_context = "render"

    def draw(self, context):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            self.draw_addon_kernel(context)
        else:
            scene = context.scene
            octane_scene = scene.octane
            layout = self.layout
            row = layout.row()
            row.prop(octane_scene, "kernel_data_mode")
            if octane_scene.kernel_data_mode == "PROPERTY_PANEL":
                self.draw_legacy_kernel(context)
            else:
                self.draw_addon_kernel(context)

    def draw_addon_kernel(self, context):
        scene = context.scene
        octane_scene = scene.octane
        layout = self.layout
        row = layout.row()
        row.prop(octane_scene.kernel_node_graph_property, "node_tree", text="Kernel Node Tree", icon='NODETREE')
        node_tree = utility.find_active_kernel_node_tree(context.scene)
        utility.panel_ui_node_tree_view(context, layout, node_tree, consts.OctaneNodeTreeIDName.KERNEL)

    def draw_legacy_kernel(self, context):
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

        def draw_nested_dielectrics():
            col.prop(oct_scene, "nested_dielectrics")

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
            # col.prop(oct_scene, "emulate_old_volume_behavior")
            pass

        def draw_color():
            col.prop(oct_scene, "white_light_spectrum")
            # col.prop(oct_scene, "use_old_color_pipeline")

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

        def draw_photons():
            col.prop(oct_scene, "photon_depth")
            col.prop(oct_scene, "accurate_colors")
            col.prop(oct_scene, "photon_gather_radius")
            col.prop(oct_scene, "photon_gather_multiplier")
            col.prop(oct_scene, "photon_gather_samples")
            col.prop(oct_scene, "exploration_strength")

        col = layout.column(align=True)
        col.prop(oct_scene, "kernel_type")
        
        if oct_scene.kernel_type in ('0', '1', ):            
            # Direct lighting kernel            
            col = layout.column(align=True)
            col.prop(oct_scene, "gi_mode")
            
            draw_clay_mode()

            box = layout.box()
            box.label(text="Quality")
            col = box.column(align=True)
            draw_samples()
            # col.prop(oct_scene, "gi_mode")
            col.prop(oct_scene, "specular_depth")
            col.prop(oct_scene, "glossy_depth")
            col.prop(oct_scene, "diffuse_depth")
            draw_ray_epsilon_and_filter_size()
            draw_ao_dist()
            col.prop_search(oct_scene, "ao_texture", bpy.data, "textures")   
            draw_alpha_shadows()
            draw_nested_dielectrics()
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
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()

            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image() 

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            # box = layout.box()
            # box.label(text="Compatibility settings")            
            # col = box.column(align=True)                  
            # draw_emulate_old_volume_behavior()                       
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
            draw_nested_dielectrics()
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
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()    
            
            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()                    

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            # box = layout.box()
            # box.label(text="Compatibility settings")            
            # col = box.column(align=True)                  
            # draw_emulate_old_volume_behavior()            
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
            draw_nested_dielectrics()
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
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            # box = layout.box()
            # box.label(text="Compatibility settings")            
            # col = box.column(align=True)                  
            # draw_emulate_old_volume_behavior()            
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
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()

            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()
        elif oct_scene.kernel_type == '5':
            # Photon tracing kernel
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
            draw_nested_dielectrics()
            draw_irradiance_mode()
            draw_max_subdivision_level()

            box = layout.box()
            box.label(text="Photons")
            col = box.column(align=True)
            draw_photons()

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
            # draw_tile_samples()
            draw_minimize_net_traffic()

            box = layout.box()
            box.label(text="Adaptive sampling")            
            col = box.column(align=True)  
            draw_adaptive_sampling() 

            box = layout.box()
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()    
            
            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()                    

            box = layout.box()
            box.label(text="Toon Shading")            
            col = box.column(align=True)       
            draw_toon_shadow_ambient()

            # box = layout.box()
            # box.label(text="Compatibility settings")            
            # col = box.column(align=True)                  
            # draw_emulate_old_volume_behavior()
        else:
            pass


class OCTANE_RENDER_PT_motion_blur(common.OctanePropertyPanel, Panel):
    bl_label = "Motion Blur"
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        rd = context.scene.render
        self.layout.prop(rd, "use_motion_blur", text="")

    def draw(self, context):
        layout = self.layout
        rd = context.scene.render
        layout.active = rd.use_motion_blur
        context.scene.octane.animation_settings.draw(context, layout)


class OCTANE_RENDER_PT_server(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Server"
    bl_context = "render"

    def draw(self, context):        
        scene = context.scene
        oct_scene = scene.octane
        is_viewport_rendering = utility.is_viewport_rendering()
        layout = self.layout
        box = layout.box()
        box.label(text="Octane Resource Cache")
        col = box.column()
        col.active = not is_viewport_rendering
        col.prop(oct_scene, "resource_cache_type")
        col.prop(oct_scene, "dirty_resource_detection_strategy_type")
        col.operator("octane.clear_resource_cache", text="Clear")        
        col = layout.column()
        col.active = not is_viewport_rendering
        col.prop(oct_scene, "meshes_type")
        col = layout.column()
        col.prop(oct_scene, "maximize_instancing")
        col.prop(oct_scene, "clay_mode")
        col.prop(oct_scene, "priority_mode")
        col.prop(oct_scene, "subsample_mode")
        col = layout.column()
        col.operator("octane.show_octane_node_graph", text="Show Octane Node Graph")
        col.operator("octane.open_octanedb", text="Open OctaneDB")
        col.operator("octane.show_octane_log", text="Show Octane Log")
        col.operator("octane.show_octane_viewport", text="Show Octane Viewport")
        col.operator("octane.show_octane_device_setting", text="Device Preferences")
        col.operator("octane.show_octane_network_preference", text="Network Preferences")
        col.operator("octane.activate", text="Activation state")


class OCTANE_RENDER_PT_out_of_core(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Out Of Core"
    bl_context = "render"
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


class OCTANE_RENDER_PT_octane_view_layer(common.OctanePropertyPanel, Panel):
    bl_label = "Octane render layers(View Layer)"
    bl_context = "view_layer"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return super().poll(context)

    def draw_header(self, context):
        self.layout.prop(context.view_layer.octane, "layers_enable", text="")

    def draw(self, context):
        layout = self.layout
        context.view_layer.octane.draw(context, layout)


class OCTANE_RENDER_PT_octane_global_view_layers(common.OctanePropertyPanel, Panel):
    bl_label = "Octane render layers(Global)"
    bl_context = "view_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        self.layout.prop(context.scene.octane.render_layer, "layers_enable", text="")

    def draw(self, context):
        layout = self.layout
        context.scene.octane.render_layer.draw(context, layout)       


class OctaneRenderAOVNodeGraphPanel(common.OctanePropertyPanel):
    @classmethod
    def poll(cls, context):
        if not common.OctanePropertyPanel.poll(context):
            return False
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane
        return octane_view_layer.render_pass_style == "RENDER_AOV_GRAPH" 


class OCTANE_RENDER_PT_AOV_node_graph(OctaneRenderAOVNodeGraphPanel, Panel):
    bl_label = "Render AOV Node Graph"
    bl_context = "view_layer"

    def draw(self, context):
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane  
        layout = self.layout
        row = layout.row()
        row.prop(octane_view_layer, "render_pass_style")  
        row = layout.row()
        render_aov_node_graph_property = octane_view_layer.render_aov_node_graph_property
        row.prop(render_aov_node_graph_property, "node_tree", text="AOV Node Tree", icon='NODETREE')
        utility.panel_ui_node_tree_view(context, layout, render_aov_node_graph_property.node_tree, consts.OctaneNodeTreeIDName.RENDER_AOV)


class OctaneRenderPassesPanel(common.OctanePropertyPanel):
    @classmethod
    def poll(cls, context):
        if not common.OctanePropertyPanel.poll(context):
            return False
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane
        return octane_view_layer.render_pass_style == "RENDER_PASSES"


class OCTANE_RENDER_PT_passes(OctaneRenderPassesPanel, Panel):
    bl_label = "Passes"
    bl_context = "view_layer"

    def draw(self, context):
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        layout = self.layout
        row = layout.row()
        row.prop(octane_view_layer, "render_pass_style")        
        row = layout.row()
        row.prop(octane_view_layer, "current_preview_pass_type")
        if octane_view_layer.current_preview_pass_type == '10000':
            row = layout.row()
            row.prop(octane_view_layer, "current_aov_output_id")
            octane_aov_out_number = 0
            composite_node_graph_property = octane_view_layer.composite_node_graph_property
            if composite_node_graph_property.node_tree is not None:
                octane_aov_out_number = composite_node_graph_property.node_tree.max_aov_output_count
            if octane_aov_out_number < octane_view_layer.current_aov_output_id:                
                row = layout.row(align=True)
                row.label(text="Beauty pass output will be used as no valid results for the assigned index", icon='INFO')
                row = layout.row(align=True)
                row.label(text="Please set Octane AOV Outputs in the 'Octane Composite Editor'", icon='INFO')


class OCTANE_RENDER_PT_passes_beauty(OctaneRenderPassesPanel, Panel):
    bl_label = "Beauty"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
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


class OCTANE_RENDER_PT_passes_denoiser(OctaneRenderPassesPanel, Panel):
    bl_label = "Denoiser"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
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
        col.prop(view_layer, "use_pass_oct_denoise_remainder", text="Refraction")
        # col.prop(view_layer, "use_pass_oct_denoise_remainder", text="Remainder")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_vol", text="Volume")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_denoise_vol_emission", text="VolEmission")


class OCTANE_RENDER_PT_passes_postprocessing(OctaneRenderPassesPanel, Panel):
    bl_label = "Post processing"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_postprocess", text="Post processing")
        col = flow.column()
        col.prop(octane_view_layer, "pass_pp_env")


class OCTANE_RENDER_PT_passes_render_layer(OctaneRenderPassesPanel, Panel):
    bl_label = "Render layer"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=True, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_shadows", text="Shadow")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_black_shadow", text="BlackShadow")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_layer_reflections", text="Reflections")


class OCTANE_RENDER_PT_passes_lighting(OctaneRenderPassesPanel, Panel):
    bl_label = "Lighting"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=3, even_columns=True, even_rows=True, align=False)
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


class OCTANE_RENDER_PT_passes_cryptomatte(OctaneRenderPassesPanel, Panel):
    bl_label = "Cryptomatte"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_instance_id", text="InstanceID")
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
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_render_layer", text="RenderLayer")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_geometry_node_name", text="GeoNodeName")
        col = flow.column()
        col.prop(view_layer, "use_pass_oct_crypto_user_instance_id", text="UserInstanceID")

        layout.row().separator()
        row = layout.row(align=True)
        row.prop(octane_view_layer, "cryptomatte_pass_channels")
        row = layout.row(align=True)
        row.prop(octane_view_layer, "cryptomatte_seed_factor")


class OCTANE_RENDER_PT_passes_info(OctaneRenderPassesPanel, Panel):
    bl_label = "Info"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
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


class OCTANE_RENDER_PT_passes_material(OctaneRenderPassesPanel, Panel):
    bl_label = "Material"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        rd = scene.render
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
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


class OCTANE_RENDER_PT_AOV_Output_node_graph(common.OctanePropertyPanel, Panel):
    bl_label = "Octane AOV Output Group"
    bl_context = "view_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane
        layout = self.layout
        row = layout.row()
        composite_node_graph_property = octane_view_layer.composite_node_graph_property
        row.prop(composite_node_graph_property, "node_tree", text="AOV Output Node Tree", icon='NODETREE')
        utility.panel_ui_node_tree_view(context, layout, composite_node_graph_property.node_tree, consts.OctaneNodeTreeIDName.COMPOSITE)


class OCTANE_RENDER_PT_override(common.OctanePropertyPanel, Panel):
    bl_label = "Override"
    bl_options = {'DEFAULT_CLOSED'}
    bl_context = "view_layer"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        view_layer = context.view_layer
        layout.prop(view_layer, "material_override")


class OCTANE_VIEW3D_MT_presets_object_menu(bpy.types.Menu):
    bl_label = "Octane Preset"

    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return rd.engine == "octane"

    def draw(self, context):
        layout = self.layout
        layout.operator("octane.quick_add_octane_vectron", text="Vectron®")
        layout.operator("octane.quick_add_octane_box", text="Box")
        layout.operator("octane.quick_add_octane_capsule", text="Capsule")
        layout.operator("octane.quick_add_octane_cylinder", text="Cylinder")
        layout.operator("octane.quick_add_octane_prism", text="Prism")
        layout.operator("octane.quick_add_octane_sphere", text="Sphere")
        layout.operator("octane.quick_add_octane_torus", text="Torus")
        layout.operator("octane.quick_add_octane_tube", text="Tube")


def octane_presets_object_menu(self, context):
    rd = context.scene.render
    if rd.engine != "octane":
        return
    layout = self.layout
    layout.separator()
    layout.menu("OCTANE_VIEW3D_MT_presets_object_menu", text="Octane Presets")


_CLASSES = [
    OCTANE_MT_kernel_presets,
    OCTANE_RENDER_PT_kernel,
    OCTANE_RENDER_PT_motion_blur,
    OCTANE_RENDER_PT_server,
    OCTANE_RENDER_PT_out_of_core,
    OCTANE_RENDER_PT_octane_view_layer,
    OCTANE_RENDER_PT_octane_global_view_layers,
    OCTANE_RENDER_PT_AOV_node_graph,
    OCTANE_RENDER_PT_passes,
    OCTANE_RENDER_PT_passes_beauty,
    OCTANE_RENDER_PT_passes_denoiser,
    OCTANE_RENDER_PT_passes_postprocessing,
    OCTANE_RENDER_PT_passes_render_layer,
    OCTANE_RENDER_PT_passes_lighting,
    OCTANE_RENDER_PT_passes_cryptomatte,
    OCTANE_RENDER_PT_passes_info,
    OCTANE_RENDER_PT_passes_material,
    OCTANE_RENDER_PT_AOV_Output_node_graph,
    OCTANE_RENDER_PT_override,
    OCTANE_VIEW3D_MT_presets_object_menu,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)
    bpy.types.VIEW3D_MT_add.append(octane_presets_object_menu)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.VIEW3D_MT_add.remove(octane_presets_object_menu)