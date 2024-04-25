# <pep8 compliant>

from bpy.types import Panel, Menu

import bpy
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import runtime_globals, utility


class OCTANE_MT_imager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/imager_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_imager_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_3dimager_presets(Menu):
    bl_label = "Imager presets"
    preset_subdir = "octane/3dimager_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_3dimager_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_postprocess_presets(Menu):
    bl_label = "Postprocess presets"
    preset_subdir = "octane/postprocess_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_postprocess_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_MT_3dpostprocess_presets(Menu):
    bl_label = "Postprocess presets"
    preset_subdir = "octane/3dpostprocess_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_3dpostprocess_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_CAMERA_PT_camera(common.OctanePropertyPanel, Panel):
    bl_label = "Octane camera"
    bl_context = "data"
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        col.prop(oct_cam, "octane_camera_type")


class OCTANE_CAMERA_PT_camera_General(common.OctanePropertyPanel, Panel):
    bl_label = "Lens or Panoramic"
    bl_parent_id = "OCTANE_CAMERA_PT_camera"
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        cam = context.camera
        oct_cam = cam.octane
        return super().poll(context) and cam and oct_cam.octane_camera_type == "Lens or Panoramic"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        cam = context.camera
        oct_cam = cam.octane

        col = layout.column()
        row = col.row()
        row.active = (cam.type == "PANO")
        col.prop(oct_cam, "pan_mode")
        col.prop(oct_cam, "fov_x")
        col.prop(oct_cam, "fov_y", text="Y")
        row = col.row(heading="Keep upright")
        row.prop(oct_cam, "keep_upright", text="")

        row = col.row()
        row.active = (cam.type != "PANO")
        col.prop(oct_cam, "distortion")
        col.prop(oct_cam, "pixel_aspect")
        row = col.row(heading="Persp. correction")
        row.prop(oct_cam, "persp_corr", text="")

        row = col.row(heading="Use F-stop")
        row.prop(oct_cam, "use_fstop", text="")
        row = col.row()
        row.active = oct_cam.use_fstop
        row.prop(oct_cam, "fstop")


class OCTANE_CAMERA_PT_camera_General_Depth_of_Field(common.OctanePropertyPanel, Panel):
    bl_label = "Depth of field"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_General"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Autofocus")
        row.prop(oct_cam, "autofocus", text="")
        row = col.row(heading="Focus object")
        row.active = not oct_cam.autofocus
        row.prop(cam.dof, "focus_object")
        row = col.row(heading="Distance")
        row.active = not oct_cam.autofocus and cam.dof.focus_object is None
        row.prop(cam.dof, "focus_distance")
        row = col.row()
        row.active = not oct_cam.use_fstop
        row.prop(oct_cam, "aperture")
        col.prop(oct_cam, "aperture_aspect")
        col.prop(oct_cam, "aperture_edge")
        col.prop(oct_cam, "bokeh_sidecount")
        col.prop(oct_cam, "bokeh_rotation")
        col.prop(oct_cam, "bokeh_roundedness")


class OCTANE_CAMERA_PT_camera_General_Stereo(common.OctanePropertyPanel, Panel):
    bl_label = "Stereo"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_General"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        layout.active = (cam.type != "PANO")
        col = layout.column()
        col.prop(oct_cam, "stereo_mode")
        col.prop(oct_cam, "stereo_out")
        col.prop(oct_cam, "stereo_dist")
        row = col.row(heading="Swap eyes")
        row.prop(oct_cam, "stereo_swap_eyes")
        col.prop(oct_cam, "stereo_dist_falloff")
        col.prop(oct_cam, "blackout_lat")
        col.prop(oct_cam, "left_filter")
        col.prop(oct_cam, "right_filter")


class OCTANE_CAMERA_PT_camera_OSL(common.OctanePropertyPanel, Panel):
    bl_label = "Used as OSL Camera"
    bl_parent_id = "OCTANE_CAMERA_PT_camera"
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        cam = context.camera
        oct_cam = cam.octane
        return super().poll(context) and cam and oct_cam.octane_camera_type == "OSL"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row()
        row.prop_search(oct_cam.osl_camera_node_collections, "osl_camera_material_tree", bpy.data, "materials")
        row = col.row()
        row.prop_search(oct_cam.osl_camera_node_collections, "osl_camera_node", oct_cam.osl_camera_node_collections,
                        "osl_camera_nodes")
        row.operator("update.osl_camera_nodes", text="Update")


class OCTANE_CAMERA_PT_camera_Octane_Camera_data_node(common.OctanePropertyPanel, Panel):
    bl_label = "Camera data node"
    bl_parent_id = "OCTANE_CAMERA_PT_camera"
    bl_options = {"DEFAULT_CLOSED"}
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        cam = context.camera
        oct_cam = cam.octane

        col = layout.column()
        row = col.row(heading="Front projection")
        row.prop(oct_cam, "use_camera_dimension_as_preview_resolution", text="Always use camera resolution")


class OCTANE_CAMERA_PT_camera_Baking(common.OctanePropertyPanel, Panel):
    bl_label = "Used as Baking Camera"
    bl_parent_id = "OCTANE_CAMERA_PT_camera"
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        cam = context.camera
        oct_cam = cam.octane
        return super().poll(context) and cam and oct_cam.octane_camera_type == "Baking"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        col.prop(oct_cam, "baking_group_id")
        col.prop(oct_cam, "baking_uv_set")
        row = col.row(heading="Revert baking")
        row.prop(oct_cam, "baking_revert", text="")


class OCTANE_CAMERA_PT_camera_Baking_Padding(common.OctanePropertyPanel, Panel):
    bl_label = "Padding"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Baking"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row()
        row.prop(oct_cam, "baking_padding")
        row = col.row()
        row.prop(oct_cam, "baking_tolerance")


class OCTANE_CAMERA_PT_camera_Baking_UV_region(common.OctanePropertyPanel, Panel):
    bl_label = "UV region"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Baking"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        _row = col.row(heading="Minimum")
        col.prop(oct_cam, "baking_uvbox_min_x")
        col.prop(oct_cam, "baking_uvbox_min_y", text="Y")
        _row = col.row(heading="Size")
        col.prop(oct_cam, "baking_uvbox_size_x")
        col.prop(oct_cam, "baking_uvbox_size_y", text="Y")


class OCTANE_CAMERA_PT_camera_Baking_Baking_position(common.OctanePropertyPanel, Panel):
    bl_label = "Baking position"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Baking"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Use baking position")
        row.prop(oct_cam, "baking_use_position", text="")
        row = col.row(heading="Backface culling")
        row.prop(oct_cam, "baking_bkface_culling", text="")


class OCTANE_CAMERA_PT_camera_Universal(common.OctanePropertyPanel, Panel):
    bl_label = "Used as Universal Camera"
    bl_parent_id = "OCTANE_CAMERA_PT_camera"
    COMPAT_ENGINES = {"octane"}

    @classmethod
    def poll(cls, context):
        cam = context.camera
        oct_cam = cam.octane
        return super().poll(context) and cam and oct_cam.octane_camera_type == "Universal"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row()
        row.active = (cam.type == "PANO")
        row.prop(oct_cam, "universal_camera_mode")
        row = col.row(heading="Use F-stop")
        row.prop(oct_cam, "use_fstop", text="")
        row = col.row()
        row.active = oct_cam.use_fstop
        row.prop(oct_cam, "fstop")


class OCTANE_CAMERA_PT_camera_Universal_Viewing_angle(common.OctanePropertyPanel, Panel):
    bl_label = "Viewing angle"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Perspective correction")
        row.prop(oct_cam, "universal_perspective_correction", text="")


class OCTANE_CAMERA_PT_camera_Universal_Fisheye(common.OctanePropertyPanel, Panel):
    bl_label = "Fisheye"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        col.prop(oct_cam, "fisheye_angle")
        col.prop(oct_cam, "fisheye_type")
        row = col.row(heading="Hard vignette")
        row.prop(oct_cam, "hard_vignette", text="")
        col.prop(oct_cam, "fisheye_projection_type")


class OCTANE_CAMERA_PT_camera_Universal_Panoramic(common.OctanePropertyPanel, Panel):
    bl_label = "Panoramic"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        col.prop(oct_cam, "fov_x")
        col.prop(oct_cam, "fov_y", text="Y")
        col.prop(oct_cam, "cubemap_layout_type")
        row = col.row(heading="Equi-angular cubemap")
        row.prop(oct_cam, "equi_angular_cubemap", text="")


class OCTANE_CAMERA_PT_camera_Universal_Distortion(common.OctanePropertyPanel, Panel):
    bl_label = "Distortion"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Use distortion texture")
        row.prop(oct_cam, "use_distortion_texture", text="")
        row = col.row()
        row.prop_search(oct_cam, "distortion_texture", bpy.data, "textures")
        col.prop(oct_cam, "spherical_distortion")
        col.prop(oct_cam, "barrel_distortion")
        col.prop(oct_cam, "barrel_distortion_corners")


class OCTANE_CAMERA_PT_camera_Universal_Aberration(common.OctanePropertyPanel, Panel):
    bl_label = "Aberration"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        _row = col.row()
        col.prop(oct_cam, "spherical_aberration")
        col.prop(oct_cam, "coma")
        col.prop(oct_cam, "astigmatism")
        col.prop(oct_cam, "field_curvature")


class OCTANE_CAMERA_PT_camera_Universal_Depth_of_field(common.OctanePropertyPanel, Panel):
    bl_label = "Depth of field"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Autofocus")
        row.prop(oct_cam, "autofocus", text="")
        row = col.row(heading="Focus object")
        row.active = not oct_cam.autofocus
        row.prop(cam.dof, "focus_object")
        row = col.row(heading="Distance")
        row.active = not oct_cam.autofocus and cam.dof.focus_object is None
        row.prop(cam.dof, "focus_distance")
        row = col.row()
        row.active = not oct_cam.use_fstop
        row.prop(oct_cam, "aperture")
        col.prop(oct_cam, "aperture_aspect")
        col.prop(oct_cam, "aperture_shape_type")
        col.prop(oct_cam, "aperture_edge")
        col.prop(oct_cam, "aperture_blade_count")
        col.prop(oct_cam, "aperture_rotation")
        col.prop(oct_cam, "aperture_roundedness")
        col.prop(oct_cam, "central_obstruction")
        col.prop(oct_cam, "notch_position")
        col.prop(oct_cam, "notch_scale")
        row = col.row()
        row.prop_search(oct_cam, "custom_aperture_texture", bpy.data, "textures")


class OCTANE_CAMERA_PT_camera_Universal_Optical_vignette(common.OctanePropertyPanel, Panel):
    bl_label = "Optical vignette"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        col.prop(oct_cam, "optical_vignette_distance")
        col.prop(oct_cam, "optical_vignette_scale")


class OCTANE_CAMERA_PT_camera_Universal_Split_focus_diopter(common.OctanePropertyPanel, Panel):
    bl_label = "Split-focus diopter"
    bl_parent_id = "OCTANE_CAMERA_PT_camera_Universal"
    COMPAT_ENGINES = {"octane"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        cam = context.camera
        oct_cam = cam.octane
        col = layout.column()
        row = col.row(heading="Enable split-focus diopter")
        row.prop(oct_cam, "enable_split_focus_diopter", text="")
        col.prop(oct_cam, "diopter_focal_depth")
        col.prop(oct_cam, "diopter_rotation")
        col.prop(oct_cam, "diopter_translation")
        col.prop(oct_cam, "diopter_boundary_width")
        col.prop(oct_cam, "diopter_boundary_falloff")
        row = col.row(heading="Show diopter guide")
        row.prop(oct_cam, "show_diopter_guide", text="")


class OCTANE_CAMERA_PT_imager(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Imager(Render Mode)"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera and not runtime_globals.use_global_imager()

    def draw_header(self, context):
        self.layout.prop(context.scene.octane, "use_render_camera_imager", text="")

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_imager_used(context.scene)
        row = layout.row(align=True)
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
        layout.active = not utility.is_viewport_imager_used(context.scene)
        context.camera.octane.imager.draw_ocio(context, layout, True)


class OCTANE_CAMERA_PT_imager_Tonemapping(common.OctanePropertyPanel, Panel):
    bl_label = "Tone Mapping"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_imager_used(context.scene)
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
        layout.active = not utility.is_viewport_imager_used(context.scene)
        context.camera.octane.imager.draw_denoiser(context, layout, True)


class OCTANE_CAMERA_PT_imager_Upsampler(common.OctanePropertyPanel, Panel):
    bl_label = "Upsampler"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_imager"

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_imager_used(context.scene)
        context.camera.octane.imager.draw_upsampler(context, layout, True)


class OCTANE_VIEW3D_PT_override(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Imager and Postprocess Settings(Preview Mode) Override"
    bl_options = {"HIDE_HEADER"}
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data and not runtime_globals.use_global_imager()

    def draw(self, context):
        self.layout.row().prop(context.scene.octane, "use_preview_setting_for_camera_imager")
        self.layout.row().prop(context.scene.octane, "use_preview_post_process_setting")


class OCTANE_VIEW3D_PT_imager(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Imager" if runtime_globals.use_global_imager() else "Octane Imager(Preview Mode)"
    bl_options = {'DEFAULT_CLOSED'}
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data

    def draw_header(self, context):
        layout = self.layout
        layout.prop(context.scene.octane, "use_preview_camera_imager", text="")

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_imager_used(context.scene, context)
        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dimager_presets", text=OCTANE_MT_3dimager_presets.bl_label)
        row.operator("render.octane_3dimager_preset_add", text="", icon="ADD")
        row.operator("render.octane_3dimager_preset_add", text="", icon="REMOVE").remove_active = True
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
        layout.active = utility.is_viewport_imager_used(context.scene, context)
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
        layout.active = utility.is_viewport_imager_used(context.scene, context)
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
        layout.active = utility.is_viewport_imager_used(context.scene, context)
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_denoiser(context, layout, True)


class OCTANE_VIEW3D_PT_imager_Upsampler(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Upsampler"
    bl_parent_id = "OCTANE_VIEW3D_PT_imager"
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_imager_used(context.scene, context)
        oct_cam = context.scene.oct_view_cam
        oct_cam.imager.draw_upsampler(context, layout, True)


class OCTANE_CAMERA_PT_post(common.OctanePropertyPanel, Panel):
    bl_label = "Octane Post Processing"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.camera and not runtime_globals.use_global_imager()

    def draw_header(self, context):
        self.layout.prop(context.camera.octane, "postprocess", text="")

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_post_process_used(context.scene)
        row = layout.row(align=True)
        row.menu("OCTANE_MT_postprocess_presets", text=OCTANE_MT_postprocess_presets.bl_label)
        row.operator("render.octane_postprocess_preset_add", text="", icon="ADD")
        row.operator("render.octane_postprocess_preset_add", text="", icon="REMOVE").remove_active = True


class OCTANE_CAMERA_PT_post_image_processing(common.OctanePropertyPanel, Panel):
    bl_label = "Post image processing"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_post"

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_post_process_used(context.scene)
        context.camera.octane.post_processing.draw_post_image_processing(context, layout, False)


class OCTANE_CAMERA_PT_post_lens_effect(common.OctanePropertyPanel, Panel):
    bl_label = "Post processing lens effects"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_post"

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_post_process_used(context.scene)
        context.camera.octane.post_processing.draw_post_lens_effect(context, layout, False)


class OCTANE_CAMERA_PT_post_volume_effect(common.OctanePropertyPanel, Panel):
    bl_label = "Post processing volume effects"
    bl_context = "data"
    bl_parent_id = "OCTANE_CAMERA_PT_post"

    def draw(self, context):
        layout = self.layout
        layout.active = not utility.is_viewport_post_process_used(context.scene)
        context.camera.octane.post_processing.draw_post_volume_effects(context, self.layout, False)


class OCTANE_VIEW3D_PT_post(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Octane Postprocess" if runtime_globals.use_global_imager() else "Octane Postprocess(Preview Mode)"
    bl_category = "Octane"
    bl_options = {'DEFAULT_CLOSED'}
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data

    def draw_header(self, context):
        layout = self.layout
        layout.prop(context.scene.oct_view_cam, "postprocess", text="")

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_post_process_used(context.scene, context)
        row = layout.row(align=True)
        row.menu("OCTANE_MT_3dpostprocess_presets", text=OCTANE_MT_3dpostprocess_presets.bl_label)
        row.operator("render.octane_3dpostprocess_preset_add", text="", icon="ADD")
        row.operator("render.octane_3dpostprocess_preset_add", text="", icon="REMOVE").remove_active = True


class OCTANE_VIEW3D_PT_post_image_processing(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Post image processing"
    bl_context = "data"
    bl_parent_id = "OCTANE_VIEW3D_PT_post"
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_post_process_used(context.scene, context)
        oct_cam = context.scene.oct_view_cam
        oct_cam.post_processing.draw_post_image_processing(context, layout, True)


class OCTANE_VIEW3D_PT_post_lens_effect(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Post processing lens effects"
    bl_context = "data"
    bl_parent_id = "OCTANE_VIEW3D_PT_post"
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_post_process_used(context.scene, context)
        oct_cam = context.scene.oct_view_cam
        oct_cam.post_processing.draw_post_lens_effect(context, layout, True)


class OCTANE_VIEW3D_PT_post_volume_effects(common.OctanePropertyPanel, Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Post processing volume effects"
    bl_context = "data"
    bl_parent_id = "OCTANE_VIEW3D_PT_post"
    bl_category = "Octane"
    COMPAT_ENGINES = {'octane'}

    def draw(self, context):
        layout = self.layout
        layout.active = utility.is_viewport_post_process_used(context.scene, context)
        oct_cam = context.scene.oct_view_cam
        oct_cam.post_processing.draw_post_volume_effects(context, layout, True)


_CLASSES = [
    OCTANE_MT_imager_presets,
    OCTANE_MT_3dimager_presets,
    OCTANE_MT_postprocess_presets,
    OCTANE_MT_3dpostprocess_presets,
    OCTANE_CAMERA_PT_camera,
    OCTANE_CAMERA_PT_camera_General,
    OCTANE_CAMERA_PT_camera_General_Depth_of_Field,
    OCTANE_CAMERA_PT_camera_General_Stereo,
    OCTANE_CAMERA_PT_camera_OSL,
    # OCTANE_CAMERA_PT_camera_Octane_Camera_data_node,
    OCTANE_CAMERA_PT_camera_Baking,
    OCTANE_CAMERA_PT_camera_Baking_Padding,
    OCTANE_CAMERA_PT_camera_Baking_UV_region,
    OCTANE_CAMERA_PT_camera_Baking_Baking_position,
    OCTANE_CAMERA_PT_camera_Universal,
    OCTANE_CAMERA_PT_camera_Universal_Viewing_angle,
    OCTANE_CAMERA_PT_camera_Universal_Fisheye,
    OCTANE_CAMERA_PT_camera_Universal_Panoramic,
    OCTANE_CAMERA_PT_camera_Universal_Distortion,
    OCTANE_CAMERA_PT_camera_Universal_Aberration,
    OCTANE_CAMERA_PT_camera_Universal_Depth_of_field,
    OCTANE_CAMERA_PT_camera_Universal_Optical_vignette,
    OCTANE_CAMERA_PT_camera_Universal_Split_focus_diopter,
    OCTANE_CAMERA_PT_imager,
    OCTANE_CAMERA_PT_imager_OCIO,
    OCTANE_CAMERA_PT_imager_Tonemapping,
    OCTANE_CAMERA_PT_imager_Denoiser,
    OCTANE_CAMERA_PT_imager_Upsampler,
    OCTANE_VIEW3D_PT_override,
    OCTANE_VIEW3D_PT_imager,
    OCTANE_VIEW3D_PT_imager_OCIO,
    OCTANE_VIEW3D_PT_imager_Tonemapping,
    OCTANE_VIEW3D_PT_imager_Denoiser,
    OCTANE_VIEW3D_PT_imager_Upsampler,
    OCTANE_CAMERA_PT_post,
    OCTANE_CAMERA_PT_post_image_processing,
    OCTANE_CAMERA_PT_post_lens_effect,
    OCTANE_CAMERA_PT_post_volume_effect,
    OCTANE_VIEW3D_PT_post,
    OCTANE_VIEW3D_PT_post_image_processing,
    OCTANE_VIEW3D_PT_post_lens_effect,
    OCTANE_VIEW3D_PT_post_volume_effects,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
