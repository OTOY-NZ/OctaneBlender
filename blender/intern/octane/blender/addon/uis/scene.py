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
            self.draw_legacy_kernel(context)

    def draw_addon_kernel(self, context):
        scene = context.scene
        octane_scene = scene.octane
        layout = self.layout
        row = layout.row()
        row.prop(octane_scene.kernel_node_graph_property, "node_tree", text="Kernel Node Tree", icon='NODETREE')
        node_tree = utility.find_active_kernel_node_tree(context)
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
            col.prop(oct_scene, "emulate_old_volume_behavior")

        def draw_color():
            col.prop(oct_scene, "white_light_spectrum")
            col.prop(oct_scene, "use_old_color_pipeline")

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
            box.label(text="Color")
            col = box.column(align=True)
            draw_color()

            box = layout.box()
            box.label(text="Deep Image")            
            col = box.column(align=True)       
            draw_deep_image()                            
        else:
            pass


_CLASSES = [
    OCTANE_MT_kernel_presets,
    OCTANE_RENDER_PT_kernel,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)