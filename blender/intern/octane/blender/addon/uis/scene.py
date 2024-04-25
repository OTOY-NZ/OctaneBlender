# <pep8 compliant>

import platform

from bpy.types import Panel, Menu

import bpy
from bpy.utils import register_class, unregister_class
from octane.uis import common
from octane.utils import consts, utility


class OCTANE_MT_kernel_presets(Menu):
    bl_label = "Kernel presets"
    preset_subdir = "octane/kernel_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_kernel_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset

    @classmethod
    def post_cb(cls, context):
        from octane.utils import utility
        preset_name = cls.bl_label
        octane_scene = context.scene.octane
        kernel_json_node_tree_helper = octane_scene.kernel_json_node_tree_helper
        utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True,
                                                  generate_from_legacy_octane_property=False,
                                                  json_node_tree=kernel_json_node_tree_helper, preset_name=preset_name)


class OCTANE_MT_legacy_kernel_presets(Menu):
    bl_label = "Legacy Kernel presets"
    preset_subdir = "octane/kernel"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_legacy_kernel_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset

    @classmethod
    def post_cb(cls, _context):
        from octane.utils import utility
        preset_name = cls.bl_label
        utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True,
                                                  generate_from_legacy_octane_property=True, preset_name=preset_name)


class OCTANE_MT_renderpasses_presets(Menu):
    bl_label = "Render Passes presets"
    preset_subdir = "octane/renderpasses_presets"
    preset_operator = "script.execute_preset"
    preset_operator_defaults = {"menu_idname": "OCTANE_MT_renderpasses_presets"}
    COMPAT_ENGINES = {"octane"}
    draw = Menu.draw_preset


class OCTANE_RENDER_PT_kernel(common.OctanePropertyPanel, Panel):
    bl_label = "Octane kernel"
    bl_context = "render"

    def draw(self, context):
        pass


class OCTANE_RENDER_PT_kernel_preset(common.OctanePropertyPanel, Panel):
    bl_label = "Kernel Presets"
    bl_context = "render"
    bl_parent_id = "OCTANE_RENDER_PT_kernel"

    def draw(self, _context):
        layout = self.layout
        row = layout.row()
        row.menu("OCTANE_MT_kernel_presets", text=OCTANE_MT_kernel_presets.bl_label)
        row.operator("render.octane_kernel_preset_add", text="", icon="ADD")
        row.operator("render.octane_kernel_preset_add", text="", icon="REMOVE").remove_active = True


class OCTANE_RENDER_PT_kernel_legacy_preset(common.OctanePropertyPanel, Panel):
    bl_label = "Legacy Presets"
    bl_context = "render"
    bl_parent_id = "OCTANE_RENDER_PT_kernel_preset"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, _context):
        layout = self.layout
        row = layout.row()
        row.menu("OCTANE_MT_legacy_kernel_presets", text="Load the legacy panel kernel presets")


class OCTANE_RENDER_PT_kernel_nodetree(common.OctanePropertyPanel, Panel):
    bl_label = "Kernel NodeTree"
    bl_context = "render"
    bl_parent_id = "OCTANE_RENDER_PT_kernel"

    def draw(self, context):
        scene = context.scene
        octane_scene = scene.octane
        node_tree = utility.find_active_kernel_node_tree(scene)
        layout = self.layout
        row = layout.row()
        row.operator("octane.quick_add_kernel_nodetree", icon="NODETREE", text="New Default").create_new_window = True
        row.operator("octane.show_kernel_nodetree", icon="NODETREE", text="Show in NodeEditor").create_new_window = True
        row = layout.row()
        row.prop(octane_scene.kernel_node_graph_property, "node_tree", text="Kernel Node Tree", icon='NODETREE')
        utility.panel_ui_node_tree_view(context, layout, node_tree, consts.OctaneNodeTreeIDName.KERNEL,
                                        consts.OctaneOutputNodeSocketNames.KERNEL)


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
        col.prop(oct_scene, "enable_realtime")
        col.prop(oct_scene, "prefer_image_type")
        col.prop(oct_scene, "maximize_instancing")
        col.prop(oct_scene, "clay_mode")
        col.prop(oct_scene, "priority_mode")
        col.prop(oct_scene, "subsample_mode")
        col = layout.column()
        col.operator("octane.show_octane_node_graph", text="Show Octane Node Graph")
        col.operator("octane.open_octanedb", text="Open OctaneDB")
        col.operator("octane.show_octane_log", text="Show Octane Log")
        if platform.system() == "Windows":
            col.operator("octane.show_octane_viewport", text="Show Octane Viewport")
        col.operator("octane.show_octane_device_setting", text="Device Preferences")
        col.operator("octane.show_octane_network_preference", text="Network Preferences")
        col.operator("octane.activate", text="Activation state")
        # if True:
        #    col.operator("octane.toggle_record", text="Debug: Toggle Record")
        #    col.operator("octane.play_record", text="Debug: Play Record")


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
        layout.use_property_split = True
        layout.use_property_decorate = False
        col = layout.column()
        col.prop(octane_view_layer, "render_pass_style")
        render_aov_node_graph_property = octane_view_layer.render_aov_node_graph_property
        col.prop(render_aov_node_graph_property, "node_tree", text="AOV Node Tree", icon="NODETREE")
        utility.panel_ui_node_tree_view1(context, layout, render_aov_node_graph_property.node_tree,
                                         consts.OctaneNodeTreeIDName.RENDER_AOV)


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
        layout.use_property_split = True
        layout.use_property_decorate = False
        col = layout.column()
        col.prop(octane_view_layer, "render_pass_style")
        col.prop(octane_view_layer, "current_preview_pass_type")
        row = col.row()
        row.menu("OCTANE_MT_renderpasses_presets", text=OCTANE_MT_renderpasses_presets.bl_label)
        row.operator("render.octane_renderpasses_preset_add", text="", icon="ADD")
        row.operator("render.octane_renderpasses_preset_add", text="", icon="REMOVE").remove_active = True
        current_preview_pass_type = utility.get_enum_int_value(octane_view_layer, "current_preview_pass_type", 0)
        if current_preview_pass_type == consts.RENDER_PASS_OUTPUT_AOV_IDS_OFFSET:
            col.prop(octane_view_layer, "current_aov_output_id")
            aov_out_number = 0
            composite_node_graph_property = octane_view_layer.composite_node_graph_property
            if composite_node_graph_property.node_tree is not None:
                aov_out_number = composite_node_graph_property.node_tree.max_aov_output_count
            if aov_out_number < octane_view_layer.current_aov_output_id:
                row = col.row(align=True)
                row.label(text="No valid results for this AOV Output(Beauty will be used)", icon='INFO')
                row = col.row(align=True)
                row.label(text='Set Octane AOV Outputs in the "Octane Composite Editor"', icon='INFO')


class OCTANE_RENDER_PT_passes_beauty(OctaneRenderPassesPanel, Panel):
    bl_label = "Beauty"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_beauty")
        flow.prop(octane_view_layer, "use_pass_emitters")
        flow.prop(octane_view_layer, "use_pass_env")
        flow.prop(octane_view_layer, "use_pass_sss")
        flow.prop(octane_view_layer, "use_pass_shadow")
        flow.prop(octane_view_layer, "use_pass_irradiance")
        flow.prop(octane_view_layer, "use_pass_light_dir")
        flow.prop(octane_view_layer, "use_pass_noise")

        layout.row().separator()
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_diff", text="Diffuse", toggle=True)
        row.prop(octane_view_layer, "use_pass_diff_dir", text="Direct", toggle=True)
        row.prop(octane_view_layer, "use_pass_diff_indir", text="Indirect", toggle=True)
        row.prop(octane_view_layer, "use_pass_diff_filter", text="Filter", toggle=True)

        layout.row().separator()
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_reflect", text="Reflection", toggle=True)
        row.prop(octane_view_layer, "use_pass_reflect_dir", text="Direct", toggle=True)
        row.prop(octane_view_layer, "use_pass_reflect_indir", text="Indirect", toggle=True)
        row.prop(octane_view_layer, "use_pass_reflect_filter", text="Filter", toggle=True)

        layout.row().separator()
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_refract", text="Refraction", toggle=True)
        row.prop(octane_view_layer, "use_pass_refract_filter", text="Refract Filter", toggle=True)

        layout.row().separator()
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_transm", text="Transmission", toggle=True)
        row.prop(octane_view_layer, "use_pass_transm_filter", text="Transm Filter", toggle=True)

        layout.row().separator()
        _row = layout.row()
        split = layout.split(factor=1)
        split.use_property_split = False
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_volume", text="Volume", toggle=True)
        row.prop(octane_view_layer, "use_pass_vol_mask", text="Mask", toggle=True)
        row.prop(octane_view_layer, "use_pass_vol_emission", text="Emission", toggle=True)
        row.prop(octane_view_layer, "use_pass_vol_z_front", text="ZFront", toggle=True)
        row.prop(octane_view_layer, "use_pass_vol_z_back", text="ZBack", toggle=True)


class OCTANE_RENDER_PT_passes_denoiser(OctaneRenderPassesPanel, Panel):
    bl_label = "Denoiser"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_denoise_beauty", text="Beauty")
        flow.prop(octane_view_layer, "use_pass_denoise_diff_dir", text="DiffDir")
        flow.prop(octane_view_layer, "use_pass_denoise_diff_indir", text="DiffIndir")
        flow.prop(octane_view_layer, "use_pass_denoise_reflect_dir", text="ReflectDir")
        flow.prop(octane_view_layer, "use_pass_denoise_reflect_indir", text="ReflectIndir")
        flow.prop(octane_view_layer, "use_pass_denoise_emission", text="Emission")
        flow.prop(octane_view_layer, "use_pass_denoise_remainder", text="Refraction")
        flow.prop(octane_view_layer, "use_pass_denoise_vol", text="Volume")
        flow.prop(octane_view_layer, "use_pass_denoise_vol_emission", text="VolEmission")


class OCTANE_RENDER_PT_passes_postprocessing(OctaneRenderPassesPanel, Panel):
    bl_label = "Post processing"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_postprocess", text="Post processing")
        flow.prop(octane_view_layer, "use_pass_postfxmedia", text="Postfix media")
        flow.prop(octane_view_layer, "pass_pp_env")


class OCTANE_RENDER_PT_passes_render_layer(OctaneRenderPassesPanel, Panel):
    bl_label = "Render layer"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=True, align=False)
        flow.prop(octane_view_layer, "use_pass_layer_shadows", text="Shadow")
        flow.prop(octane_view_layer, "use_pass_layer_black_shadow", text="BlackShadow")
        flow.prop(octane_view_layer, "use_pass_layer_reflections", text="Reflections")


class OCTANE_RENDER_PT_passes_lighting(OctaneRenderPassesPanel, Panel):
    bl_label = "Lighting"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=3, even_columns=True, even_rows=True, align=False)
        flow.prop(octane_view_layer, "use_pass_ambient_light", text="Ambient")
        flow.prop(octane_view_layer, "use_pass_ambient_light_dir", text="Direct")
        flow.prop(octane_view_layer, "use_pass_ambient_light_indir", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_sunlight", text="Sunlight")
        flow.prop(octane_view_layer, "use_pass_sunlight_dir", text="Direct")
        flow.prop(octane_view_layer, "use_pass_sunlight_indir", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_1", text="Light Pass 1")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_1", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_1", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_2", text="Light Pass 2")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_2", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_2", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_3", text="Light Pass 3")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_3", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_3", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_4", text="Light Pass 4")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_4", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_4", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_5", text="Light Pass 5")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_5", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_5", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_6", text="Light Pass 6")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_6", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_6", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_7", text="Light Pass 7")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_7", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_7", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_8", text="Light Pass 8")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_8", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_8", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_9", text="Light Pass 9")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_9", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_9", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_10", text="Light Pass 10")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_10", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_10", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_11", text="Light Pass 11")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_11", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_11", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_12", text="Light Pass 12")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_12", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_12", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_13", text="Light Pass 13")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_13", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_13", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_14", text="Light Pass 14")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_14", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_14", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_15", text="Light Pass 15")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_15", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_15", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_16", text="Light Pass 16")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_16", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_16", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_17", text="Light Pass 17")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_17", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_17", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_18", text="Light Pass 18")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_18", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_18", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_19", text="Light Pass 19")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_19", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_19", text="Indirect")
        flow.prop(octane_view_layer, "use_pass_light_pass_20", text="Light Pass 20")
        flow.prop(octane_view_layer, "use_pass_light_dir_pass_20", text="Direct")
        flow.prop(octane_view_layer, "use_pass_light_indir_pass_20", text="Indirect")


class OCTANE_RENDER_PT_passes_cryptomatte(OctaneRenderPassesPanel, Panel):
    bl_label = "Cryptomatte"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_crypto_instance_id", text="InstanceID")
        flow.prop(octane_view_layer, "use_pass_crypto_mat_node_name", text="MatNodeName")
        flow.prop(octane_view_layer, "use_pass_crypto_mat_node", text="MatNode")
        flow.prop(octane_view_layer, "use_pass_crypto_mat_pin_node", text="MatPinNode")
        flow.prop(octane_view_layer, "use_pass_crypto_obj_node_name", text="ObjNodeName")
        flow.prop(octane_view_layer, "use_pass_crypto_obj_node", text="ObjNode")
        flow.prop(octane_view_layer, "use_pass_crypto_obj_pin_node", text="ObjPinNode")
        # flow.prop(octane_view_layer, "use_pass_crypto_render_layer", text="RenderLayer")
        # flow.prop(octane_view_layer, "use_pass_crypto_geometry_node_name", text="GeoNodeName")
        # flow.prop(octane_view_layer, "use_pass_crypto_user_instance_id", text="UserInstanceID")

        layout.row().separator()
        layout.use_property_split = True
        layout.use_property_decorate = False
        col = layout.column(align=True)
        col.prop(octane_view_layer, "cryptomatte_pass_channels")
        col.prop(octane_view_layer, "cryptomatte_seed_factor")


class OCTANE_RENDER_PT_passes_info(OctaneRenderPassesPanel, Panel):
    bl_label = "Info"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_info_z_depth")
        flow.prop(octane_view_layer, "use_pass_info_position")
        flow.prop(octane_view_layer, "use_pass_info_uv")
        flow.prop(octane_view_layer, "use_pass_info_tex_tangent")
        flow.prop(octane_view_layer, "use_pass_info_motion_vector")
        flow.prop(octane_view_layer, "use_pass_info_mat_id")
        flow.prop(octane_view_layer, "use_pass_info_obj_id")
        flow.prop(octane_view_layer, "use_pass_info_obj_layer_color")
        flow.prop(octane_view_layer, "use_pass_info_baking_group_id")
        flow.prop(octane_view_layer, "use_pass_info_light_pass_id")
        flow.prop(octane_view_layer, "use_pass_info_render_layer_id")
        flow.prop(octane_view_layer, "use_pass_info_render_layer_mask")
        flow.prop(octane_view_layer, "use_pass_info_wireframe")
        flow.prop(octane_view_layer, "use_pass_info_ao")

        layout.row().separator()
        split = layout.split(factor=0.15)
        split.use_property_split = False
        split.label(text="Normal")
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_info_geo_normal", text="Geometric", toggle=True)
        row.prop(octane_view_layer, "use_pass_info_smooth_normal", text="Smooth", toggle=True)
        row.prop(octane_view_layer, "use_pass_info_shading_normal", text="Shading", toggle=True)
        row.prop(octane_view_layer, "use_pass_info_tangent_normal", text="Tangent", toggle=True)

        layout.row().separator()
        layout.use_property_split = True
        layout.use_property_decorate = False
        col = layout.column(align=True)
        col.prop(octane_view_layer, "info_pass_max_samples")
        col.prop(octane_view_layer, "info_pass_sampling_mode")
        col.prop(octane_view_layer, "info_pass_opacity_threshold")
        col.prop(octane_view_layer, "info_pass_z_depth_max")
        col.prop(octane_view_layer, "info_pass_uv_max")
        col.prop(octane_view_layer, "info_pass_uv_coordinate_selection")
        col.prop(octane_view_layer, "info_pass_max_speed")
        col.prop(octane_view_layer, "info_pass_ao_distance")
        col.prop(octane_view_layer, "info_pass_alpha_shadows")
        col.prop(octane_view_layer, "info_pass_bump")
        col.prop(octane_view_layer, "shading_enabled")
        col.prop(octane_view_layer, "highlight_backfaces")


class OCTANE_RENDER_PT_passes_material(OctaneRenderPassesPanel, Panel):
    bl_label = "Material"
    bl_context = "view_layer"
    bl_parent_id = "OCTANE_RENDER_PT_passes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        view_layer = context.view_layer
        octane_view_layer = view_layer.octane

        flow = layout.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=False, align=False)
        flow.prop(octane_view_layer, "use_pass_mat_opacity")
        flow.prop(octane_view_layer, "use_pass_mat_roughness")
        flow.prop(octane_view_layer, "use_pass_mat_ior")

        layout.row().separator()
        split = layout.split(factor=0.15)
        split.use_property_split = False
        split.label(text="Filter")
        row = split.row(align=True)
        row.prop(octane_view_layer, "use_pass_mat_diff_filter_info", text="Diffuse", toggle=True)
        row.prop(octane_view_layer, "use_pass_mat_reflect_filter_info", text="Reflection", toggle=True)
        row.prop(octane_view_layer, "use_pass_mat_refract_filter_info", text="Refraction", toggle=True)
        row.prop(octane_view_layer, "use_pass_mat_transm_filter_info", text="Transmission", toggle=True)


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
        utility.panel_ui_node_tree_view1(context, layout, composite_node_graph_property.node_tree,
                                         consts.OctaneNodeTreeIDName.COMPOSITE)


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

    def draw(self, _context):
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


def octane_presets_light_menu(self, context):
    rd = context.scene.render
    if rd.engine != "octane":
        return
    self.layout.separator()
    self.layout.operator("octane.quick_add_octane_toon_point_light", icon="LIGHT_POINT", text="Octane Toon Point Light")
    self.layout.operator("octane.quick_add_octane_toon_directional_light", icon="LIGHT_SUN",
                         text="Octane Toon Directional Light")
    self.layout.separator()
    self.layout.operator("octane.quick_add_octane_spot_light", icon="LIGHT_SPOT", text="Octane SpotLight")
    self.layout.operator("octane.quick_add_octane_area_light", icon="LIGHT_AREA", text="Octane Area Light")
    self.layout.operator("octane.quick_add_octane_sphere_light", icon="LIGHT_POINT", text="Octane Sphere Light")
    self.layout.operator("octane.quick_add_octane_mesh_light", icon="LIGHT_AREA", text="Octane Mesh Light")
    self.layout.operator("octane.quick_add_octane_directional_light", icon="LIGHT_SUN", text="Octane Directional Light")
    self.layout.operator("octane.quick_add_octane_analytical_light", icon="LIGHT_AREA", text="Octane Analytical Light")


_CLASSES = [
    OCTANE_MT_kernel_presets,
    OCTANE_MT_legacy_kernel_presets,
    OCTANE_MT_renderpasses_presets,
    OCTANE_RENDER_PT_kernel,
    OCTANE_RENDER_PT_kernel_preset,
    OCTANE_RENDER_PT_kernel_legacy_preset,
    OCTANE_RENDER_PT_kernel_nodetree,
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
    bpy.types.VIEW3D_MT_light_add.append(octane_presets_light_menu)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.VIEW3D_MT_add.remove(octane_presets_object_menu)
    bpy.types.VIEW3D_MT_light_add.remove(octane_presets_light_menu)
