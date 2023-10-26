import bpy
import xml.etree.ElementTree as ET
from bpy.types import Panel, Menu, Operator
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility
from octane import core


class OCTANE_MT_imager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/imager_presets"
    preset_operator = "script.execute_preset_octane"
    preset_operator_defaults = {"menu_idname" : "OCTANE_MT_imager_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_3dimager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/3dimager_presets"
    preset_operator = "script.execute_preset_octane"
    preset_operator_defaults = {"menu_idname" : "OCTANE_MT_3dimager_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_postprocess_presets(Menu):
    bl_label = "Postprocess presets"
    preset_subdir = "octane/postprocess_presets"
    preset_operator = "script.execute_preset_octane"
    preset_operator_defaults = {"menu_idname" : "OCTANE_MT_postprocess_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_3dpostprocess_presets(Menu):
    bl_label = "Postprocess presets"
    preset_subdir = "octane/3dpostprocess_presets"
    preset_operator = "script.execute_preset_octane"
    preset_operator_defaults = {"menu_idname" : "OCTANE_MT_3dpostprocess_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset



class OCTANE_CAMERA_PT_camera(common.OctanePropertyPanel, Panel):
    bl_label = "Octane camera"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera

    def draw(self, context):
        layout = self.layout

        cam = context.camera
        oct_cam = cam.octane

        row = layout.row(align=True)
        row.prop(oct_cam, "use_camera_dimension_as_preview_resolution")

        row = layout.row(align=True)
        row.prop(oct_cam, "used_as_universal_camera")
        sub = layout.column(align=True)

        if oct_cam.used_as_universal_camera:
            if cam.type == 'PANO':
                sub.prop(oct_cam, "universal_camera_mode")
            box = layout.box()
            box.label(text="Viewing angle")
            sub = box.row(align=True)
            sub.prop(oct_cam, "universal_perspective_correction")
            box = layout.box()
            box.label(text="Fisheye")
            sub = box.row(align=True)
            sub.prop(oct_cam, "fisheye_angle")
            sub = box.row(align=True)
            sub.prop(oct_cam, "fisheye_type")
            sub = box.row(align=True)
            sub.prop(oct_cam, "hard_vignette")        
            sub = box.row(align=True)
            sub.prop(oct_cam, "fisheye_projection_type")       
            box = layout.box()
            box.label(text="Panoramic")
            sub = box.column(align=True)
            sub.prop(oct_cam, "fov_x")
            sub.prop(oct_cam, "fov_y")  
            sub = box.row(align=True)          
            sub.prop(oct_cam, "cubemap_layout_type")
            sub = box.row(align=True)
            sub.prop(oct_cam, "equi_angular_cubemap")                
            box = layout.box()
            box.label(text="Distortion")
            sub = box.column(align=True)
            sub.prop(oct_cam, "use_distortion_texture")
            sub = box.row(align=True)
            sub.prop_search(oct_cam, "distortion_texture", bpy.data, "textures")       
            sub = box.column(align=True)
            sub.prop(oct_cam, "spherical_distortion")
            sub.prop(oct_cam, "barrel_distortion")
            sub.prop(oct_cam, "barrel_distortion_corners")
            box = layout.box()
            box.label(text="Aberration")
            sub = box.column(align=True)
            sub.prop(oct_cam, "spherical_aberration")
            sub.prop(oct_cam, "coma")            
            sub.prop(oct_cam, "astigmatism")
            sub.prop(oct_cam, "field_curvature")   
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
            sub = box.row(align=True)
            sub.prop(oct_cam, "aperture_shape_type")
            sub = box.column(align=True)
            sub.prop(oct_cam, "aperture_edge")        
            sub.prop(oct_cam, "aperture_blade_count")
            sub.prop(oct_cam, "aperture_rotation")
            sub.prop(oct_cam, "aperture_roundedness") 
            sub.prop(oct_cam, "central_obstruction")                     
            sub.prop(oct_cam, "notch_position")
            sub.prop(oct_cam, "notch_scale")
            sub = box.row(align=True)
            sub.prop_search(oct_cam, "custom_aperture_texture", bpy.data, "textures")
            box = layout.box()
            box.label(text="Optical vignette")
            sub = box.column(align=True)
            sub.prop(oct_cam, "optical_vignette_distance")
            sub.prop(oct_cam, "optical_vignette_scale")     
            box = layout.box()
            box.label(text="Split-focus diopter")
            sub = box.column(align=True)
            sub.prop(oct_cam, "enable_split_focus_diopter")
            sub = box.column(align=True)
            sub.prop(oct_cam, "diopter_focal_depth")
            sub.prop(oct_cam, "diopter_rotation")
            sub = box.row(align=True)
            sub.prop(oct_cam, "diopter_translation")
            sub = box.column(align=True)
            sub.prop(oct_cam, "diopter_boundary_width")
            sub.prop(oct_cam, "diopter_boundary_falloff")
            sub = box.row(align=True)
            sub.prop(oct_cam, "show_diopter_guide")
        else:            
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


class OCTANE_CAMERA_PT_imager(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Camera Imager(Render Mode)"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "use_render_camera_imager", text="")

    def draw(self, context):
        row = self.layout.row(align=True)
        row.menu("OCTANE_MT_imager_presets", text=OCTANE_MT_imager_presets.bl_label)
        row.operator("render.octane_imager_preset_add", text="", icon="ADD")
        row.operator("render.octane_imager_preset_add", text="", icon="REMOVE").remove_active = True
        context.camera.octane.imager.draw(context, self.layout, False)


class OCTANE_CAMERA_PT_imager_OCIO(common.OctanePropertyPanel, Panel):    
    bl_label = "OCIO"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_ocio(context, layout, True)


class OCTANE_CAMERA_PT_imager_Tonemapping(common.OctanePropertyPanel, Panel):
    bl_label = "Tone Mapping"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_tonemapping(context, layout, True)


class OCTANE_CAMERA_PT_imager_Denoiser(common.OctanePropertyPanel, Panel):
    bl_label = "Denoiser"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw_header(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_denoiser_header(context, layout, True)

    def draw(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_denoiser(context, layout, True)


class OCTANE_CAMERA_PT_imager_Upsampler(common.OctanePropertyPanel, Panel):
    bl_label = "Upsampler"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw_header(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_upsampler_header(context, layout, True)

    def draw(self, context):
        layout = self.layout
        context.camera.octane.imager.draw_upsampler(context, layout, True)


class OCTANE_VIEW3D_PT_imager(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Camera Imager(Preview Mode)"    
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}        

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "use_preview_camera_imager", text="")

    def draw(self, context):
        camera_data, camera_name = utility.find_active_imager_data(context.scene, context)
        layout = self.layout
        layout.active = (camera_name == "VIEW_3D")
        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dimager_presets", text=OCTANE_MT_3dimager_presets.bl_label)
        row.operator("render.octane_3dimager_preset_add", text="", icon="ADD")
        row.operator("render.octane_3dimager_preset_add", text="", icon="REMOVE").remove_active = True
        col = layout.column(align=True)
        col.prop(context.scene.octane, "use_preview_setting_for_camera_imager")
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw(context, layout, True)


class OCTANE_VIEW3D_PT_imager_OCIO(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'    
    bl_label = "OCIO"
    bl_parent_id = "OCTANE_VIEW3D_PT_imager"
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_ocio(context, layout, True)


class OCTANE_VIEW3D_PT_imager_Tonemapping(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'    
    bl_label = "Tone Mapping"
    bl_parent_id = "OCTANE_VIEW3D_PT_imager"
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_tonemapping(context, layout, True)


class OCTANE_VIEW3D_PT_imager_Denoiser(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'    
    bl_label = "Denoiser"
    bl_parent_id = "OCTANE_VIEW3D_PT_imager"
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}

    def draw_header(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_denoiser_header(context, layout, True)

    def draw(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_denoiser(context, layout, True)


class OCTANE_VIEW3D_PT_imager_Upsampler(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'    
    bl_label = "Upsampler"
    bl_parent_id = "OCTANE_VIEW3D_PT_imager"
    bl_category = "Octane"    
    COMPAT_ENGINES = {'octane'}

    def draw_header(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_upsampler_header(context, layout, True)

    def draw(self, context):
        layout = self.layout
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_upsampler(context, layout, True)                


class OCTANE_CAMERA_PT_post(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Post Processing"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera

    def draw_header(self, context):
        self.layout.prop(context.camera.octane, "postprocess", text="")

    def draw(self, context):
        row = self.layout.row(align=True)
        row.menu("OCTANE_MT_postprocess_presets", text=OCTANE_MT_postprocess_presets.bl_label)
        row.operator("render.octane_postprocess_preset_add", text="", icon="ADD")
        row.operator("render.octane_postprocess_preset_add", text="", icon="REMOVE").remove_active = True


class OCTANE_CAMERA_PT_post_image_processing(common.OctanePropertyPanel, Panel):
    bl_label = "Post image processing"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_post"

    def draw(self, context):
        context.camera.octane.post_processing.draw_post_image_processing(context, self.layout, False)



class OCTANE_VIEW3D_PT_post(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Postprocess(Preview Mode)"
    bl_category = "Octane"         
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'octane'}          

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data

    def draw_header(self, context):
        self.layout.prop(context.scene.oct_view_cam, "postprocess", text="")

    def draw(self, context):
        layout = self.layout
        camera_data, camera_name = utility.find_active_post_process_data(context.scene, context)
        layout.active = (camera_name == "VIEW_3D")
        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dpostprocess_presets", text=OCTANE_MT_3dpostprocess_presets.bl_label)
        row.operator("render.octane_3dpostprocess_preset_add", text="", icon="ADD")
        row.operator("render.octane_3dpostprocess_preset_add", text="", icon="REMOVE").remove_active = True
        col = layout.column(align=True)
        col.prop(context.scene.octane, "use_preview_post_process_setting")


class OCTANE_VIEW3D_PT_post_image_processing(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI' 
    bl_label = "Post image processing"
    bl_context = "data"
    bl_parent_id = "OCTANE_VIEW3D_PT_post"
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        oct_cam = context.scene.oct_view_cam
        oct_cam.post_processing.draw_post_image_processing(context, self.layout, True)


_CLASSES = [
    OCTANE_MT_imager_presets,
    OCTANE_MT_3dimager_presets,
    OCTANE_MT_postprocess_presets,
    OCTANE_MT_3dpostprocess_presets,
    OCTANE_CAMERA_PT_camera,
    OCTANE_CAMERA_PT_imager,
    OCTANE_CAMERA_PT_imager_OCIO,
    OCTANE_CAMERA_PT_imager_Tonemapping,
    OCTANE_CAMERA_PT_imager_Denoiser,
    OCTANE_CAMERA_PT_imager_Upsampler,
    OCTANE_VIEW3D_PT_imager,
    OCTANE_VIEW3D_PT_imager_OCIO,
    OCTANE_VIEW3D_PT_imager_Tonemapping,
    OCTANE_VIEW3D_PT_imager_Denoiser,
    OCTANE_VIEW3D_PT_imager_Upsampler,
    OCTANE_CAMERA_PT_post,
    OCTANE_CAMERA_PT_post_image_processing,
    OCTANE_VIEW3D_PT_post,
    OCTANE_VIEW3D_PT_post_image_processing,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)