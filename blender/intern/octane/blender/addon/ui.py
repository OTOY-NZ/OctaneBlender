# <pep8 compliant>

from bpy.types import Panel

import bpy
from octane.utils import utility, consts
from . import converters


def osl_node_draw(context, layout, node_tree_name, node_name):
    if bpy.data.materials:
        for mat in bpy.data.materials.values():
            if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                continue
            if mat.name != node_tree_name:
                continue
            for node in mat.node_tree.nodes.values():
                if node.name == node_name:
                    layout.label(text="Octane Geometric Node")
                    utility.template_panel_ui_node_view(context, layout, mat.node_tree, node)
                    return True
    layout.label(text="No Octane Geometric Node")
    return False


class OctaneButtonsPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES


class OCTANE_PT_mesh_properties(OctaneButtonsPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if OctaneButtonsPanel.poll(context):
            if context.mesh or context.meta_ball:
                return True
        return False

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "octane_hide_original_mesh")
        col.prop(ob_data_octane, "infinite_plane")
        col.prop(ob_data_octane, "primitive_coordinate_mode")
        col.prop(ob_data_octane, "force_load_vertex_normals")
        col.prop(ob_data_octane, "winding_order")


class OCTANE_PT_mesh_properties_geometric_node(OctaneButtonsPanel, Panel):
    bl_label = "Geometric Node"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        row = col.row()
        row.prop_search(ob_data_octane.octane_geo_node_collections, "node_graph_tree", bpy.data, "materials")
        row.operator('update.octane_geo_nodes', icon='FILE_REFRESH')
        row = col.row()
        row.prop_search(ob_data_octane.octane_geo_node_collections, "osl_geo_node",
                        ob_data_octane.octane_geo_node_collections, "osl_geo_nodes")
        osl_node_draw(context, col, str(ob_data_octane.octane_geo_node_collections.node_graph_tree),
                      str(ob_data_octane.octane_geo_node_collections.osl_geo_node))


class OCTANE_PT_mesh_properties_open_subdivision(OctaneButtonsPanel, Panel):
    bl_label = "Open SubDivision"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "open_subd_enable", text="Enable")
        col.prop(ob_data_octane, "open_subd_scheme")
        col.prop(ob_data_octane, "open_subd_bound_interp")
        col.prop(ob_data_octane, "open_subd_level")
        col.prop(ob_data_octane, "open_subd_sharpness")


class OCTANE_PT_mesh_properties_sphere_attributes(OctaneButtonsPanel, Panel):
    bl_label = "Sphere Attributes"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "octane_enable_sphere_attribute")
        col.prop(ob_data_octane, "octane_sphere_radius")
        col.prop(ob_data_octane, "octane_use_randomized_radius")
        col.prop(ob_data_octane, "octane_sphere_randomized_radius_seed")
        col.prop(ob_data_octane, "octane_sphere_randomized_radius_min")
        col.prop(ob_data_octane, "octane_sphere_randomized_radius_max")


class OCTANE_PT_mesh_properties_orbx_properties(OctaneButtonsPanel, Panel):
    bl_label = "Orbx Properties"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "imported_orbx_file_path")
        col.prop(ob_data_octane, "enable_animation_time_transformation")
        col.prop(ob_data_octane, "animation_time_transformation_delay")
        col.prop(ob_data_octane, "animation_time_transformation_scale")
        col.prop(ob_data_octane, "orbx_preview_type")
        if ob_data_octane.orbx_preview_type == "External Alembic":
            row = col.row(align=True)
            row.prop(ob_data_octane, "converted_alembic_asset_path")
        row = col.row(align=True)
        row.operator("octane.generate_orbx_preview")


class OCTANE_PT_mesh_properties_mesh_volume(OctaneButtonsPanel, Panel):
    bl_label = "Mesh volume"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "enable_mesh_volume")
        col.prop(ob_data_octane, "enable_mesh_volume_sdf")
        col.prop(ob_data_octane, "mesh_volume_sdf_voxel_size")
        col.prop(ob_data_octane, "mesh_volume_sdf_border_thickness_inside")
        col.prop(ob_data_octane, "mesh_volume_sdf_border_thickness_outside")


class OCTANE_PT_mesh_properties_offset_transform(OctaneButtonsPanel, Panel):
    bl_label = "Offset Transform"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "enable_octane_offset_transform")
        col.prop(ob_data_octane, "octane_offset_translation")
        col.prop(ob_data_octane, "octane_offset_rotation_order")
        col.prop(ob_data_octane, "octane_offset_rotation")
        col.prop(ob_data_octane, "octane_offset_scale")


class OCTANE_PT_mesh_properties_legacy_settings(OctaneButtonsPanel, Panel):
    bl_label = "Legacy Settings"
    bl_parent_id = "OCTANE_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        if OctaneButtonsPanel.poll(context):
            ob = context.object
            ob_data = ob.data
            if ob_data is not None:
                ob_data_octane = ob_data.octane
                # For the versions after 21.12, we use OpenVDB in Blender volume
                # This section will be dropped, so we hide octane volume properties if it's not used
                if ob_data_octane.is_octane_vdb or len(ob_data_octane.imported_openvdb_file_path) > 0:
                    return True
        return False

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        cdata = ob_data_octane
        box = layout.box()
        box.label(text="Volume properties:")
        sub = box.column(align=True)
        sub.label(text="The new OpenVDB feature is supported in the Blender Volume object since Blender 2.83. Please "
                       "use that one for the new productions", icon='INFO')
        sub = box.column(align=True)
        sub.prop(cdata, "is_octane_vdb")
        sub.prop(cdata, "vdb_sdf")
        sub.prop(cdata, "imported_openvdb_file_path")
        sub.prop(cdata, "vdb_import_scale")
        sub = box.row(align=True)
        sub.prop(cdata, "openvdb_frame_start")
        sub.prop(cdata, "openvdb_frame_end")
        sub = box.row(align=True)
        sub.prop(cdata, "openvdb_frame_start_playing_at")
        # noinspection SpellCheckingInspection
        sub.prop(cdata, "openvdb_frame_speed_mutiplier")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_iso")
        sub.prop(cdata, "vdb_abs_scale")
        sub.prop(cdata, "vdb_emiss_scale")
        sub.prop(cdata, "vdb_scatter_scale")
        sub.prop_search(cdata, "vdb_absorption_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub.prop_search(cdata, "vdb_emission_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub.prop_search(cdata, "vdb_scattering_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_motion_blur_enabled")
        sub.prop(cdata, "vdb_velocity_grid_type")
        sub.prop(cdata, "vdb_vel_scale")
        if cdata.vdb_velocity_grid_type == 'Vector grid':
            sub.prop_search(cdata, "vdb_vector_grid_id", cdata.octane_vdb_info, "vdb_vector_grid_id_container")
        else:
            sub.prop_search(cdata, "vdb_x_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_y_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_z_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")


class OCTANE_PT_volume_properties(OctaneButtonsPanel, Panel):
    bl_label = "Octane properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if OctaneButtonsPanel.poll(context):
            if context.volume:
                return True
        return False

    def draw(self, context):
        cdata = context.volume.octane
        layout = self.layout

        modifiers = context.object.modifiers
        is_volume_modified = False
        for mod in modifiers:
            if mod.type in ('MESH_TO_VOLUME', 'VOLUME_DISPLACE'):
                is_volume_modified = True
                break

        if is_volume_modified:
            layout.label(text="Octane options does not work for modified volumes")
            return

        box = layout.box()
        box.label(text="Volume properties:")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_sdf")
        sub.prop(cdata, "vdb_import_scale")
        sub = box.column(align=True)
        # noinspection SpellCheckingInspection
        sub.prop(cdata, "apply_import_scale_to_blender_transfrom")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_iso")
        sub.prop(cdata, "border_thickness_inside")
        sub.prop(cdata, "border_thickness_outside")
        sub.prop(cdata, "vdb_abs_scale")
        sub.prop(cdata, "vdb_emiss_scale")
        sub.prop(cdata, "vdb_scatter_scale")
        sub.prop_search(cdata, "vdb_absorption_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub.prop_search(cdata, "vdb_emission_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub.prop_search(cdata, "vdb_scattering_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
        sub = box.column(align=True)
        sub.prop(cdata, "vdb_motion_blur_enabled")
        sub.prop(cdata, "vdb_velocity_grid_type")
        sub.prop(cdata, "vdb_vel_scale")
        if cdata.vdb_velocity_grid_type == 'Vector grid':
            sub.prop_search(cdata, "vdb_vector_grid_id", cdata.octane_vdb_info, "vdb_vector_grid_id_container")
        else:
            sub.prop_search(cdata, "vdb_x_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_y_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_z_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")

        box = layout.box()
        box.label(text="Octane Offset Transform:")
        sub = box.row(align=True)
        sub.prop(cdata, "enable_octane_offset_transform")
        sub = box.row(align=True)
        sub.prop(cdata, "octane_offset_translation")
        sub = box.row(align=True)
        sub.prop(cdata, "octane_offset_rotation_order")
        sub = box.row(align=True)
        sub.prop(cdata, "octane_offset_rotation")
        sub = box.row(align=True)
        sub.prop(cdata, "octane_offset_scale")


class OCTANE_RENDER_PT_SpherePrimitiveSettings(OctaneButtonsPanel, Panel):
    bl_label = "Octane Sphere Primitive Settings"
    bl_context = "particle"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        psys = context.particle_system
        engine = context.engine
        if psys is None:
            return False
        return engine == "octane"

    def draw(self, context):
        layout = self.layout

        psys = context.particle_system
        particle_settings = context.particle_settings

        is_active = psys.settings.type != 'HAIR' and (psys.settings.render_type != 'OBJECT'
                                                      and psys.settings.render_type != 'COLLECTION')

        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "use_as_octane_sphere_primitive")
        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "octane_velocity_multiplier")
        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "octane_sphere_size_multiplier")


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
            if is_sortable:
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
        utility.panel_ui_node_view(context, layout, mat, consts.OctaneOutputNodeSocketNames.SURFACE)


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
        utility.panel_ui_node_view(context, layout, mat, consts.OctaneOutputNodeSocketNames.VOLUME)


class OCTANE_MATERIAL_PT_settings(OctaneButtonsPanel, Panel):
    bl_label = "Settings"
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.material or context.object) and OctaneButtonsPanel.poll(context)

    def draw(self, _context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("octane.save_as_octanedb", text="Save As OctaneDB")


class OCTANE_MATERIAL_PT_converters(OctaneButtonsPanel, Panel):
    bl_label = "Converters"
    bl_context = "material"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return ((context.material or context.object) and OctaneButtonsPanel.poll(context)
                and converters.is_converter_applicable(context.material))

    def draw(self, _context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("octane.convert_to_octane_material", text="Convert To Octane Materials")


class OCTANE_OBJECT_PT_octane_settings(OctaneButtonsPanel, Panel):
    bl_label = "Octane Settings"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (OctaneButtonsPanel.poll(context) and
                ob and ((ob.type in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META', 'LIGHT', 'VOLUME'}) or
                        (ob.instance_type == 'COLLECTION' and ob.instance_collection)))

    def draw(self, context):
        layout = self.layout
        ob = context.object
        octane_object = ob.octane

        if ob and ob.type not in ('FONT',):
            sub = layout.row(align=True)
            sub.active = not utility.is_viewport_rendering()
            sub.prop(octane_object, "object_mesh_type")


class OCTANE_OBJECT_PT_octane_settings_object_layer(OctaneButtonsPanel, Panel):
    bl_label = "Object layer"
    bl_parent_id = "OCTANE_OBJECT_PT_octane_settings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        ob = context.object
        octane_object = ob.octane
        orbx_path = getattr(ob.data.octane, "imported_orbx_file_path", "")
        is_used_as_orbx_proxy = len(orbx_path) > 0
        if is_used_as_orbx_proxy:
            sub = layout.row(align=True)
            sub.label(text="This object is used as Orbx Proxy.")
            sub = layout.row(align=True)
            sub.label(text="Object Layer Data is only valid for the proxies without Placement or Group Nodes.")
        sub = layout.row(align=True)
        sub.active = octane_object.render_layer_id != 0
        sub.prop(octane_object, "render_layer_id")
        sub = layout.row(align=True)
        sub.prop(octane_object, "general_visibility")
        sub = layout.row(align=True)
        sub.prop(octane_object, "camera_visibility")
        sub.prop(octane_object, "shadow_visibility")
        sub.prop(octane_object, "dirt_visibility")
        sub.prop(octane_object, "curvature_visibility")

        box = layout.box()
        box.label(text="Light pass mask")
        row = box.row(align=True)
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
        row = box.row(align=True)
        row.prop(octane_object, "light_id_pass_9", text="9", toggle=True)
        row.prop(octane_object, "light_id_pass_10", text="10", toggle=True)
        row.prop(octane_object, "light_id_pass_11", text="11", toggle=True)
        row.prop(octane_object, "light_id_pass_12", text="12", toggle=True)
        row.prop(octane_object, "light_id_pass_13", text="13", toggle=True)
        row.prop(octane_object, "light_id_pass_14", text="14", toggle=True)
        row = box.row(align=True)
        row.prop(octane_object, "light_id_pass_15", text="15", toggle=True)
        row.prop(octane_object, "light_id_pass_16", text="16", toggle=True)
        row.prop(octane_object, "light_id_pass_17", text="17", toggle=True)
        row.prop(octane_object, "light_id_pass_18", text="18", toggle=True)
        row.prop(octane_object, "light_id_pass_19", text="19", toggle=True)
        row.prop(octane_object, "light_id_pass_20", text="20", toggle=True)

        sub = layout.row(align=True)
        sub.prop(octane_object, "random_color_seed")
        sub = layout.row(align=True)
        sub.prop(octane_object, "color")
        sub = layout.row(align=True)
        sub.prop(octane_object, "custom_aov")
        sub = layout.row(align=True)
        sub.prop(octane_object, "custom_aov_channel")


class OCTANE_OBJECT_PT_octane_settings_baking_settings(OctaneButtonsPanel, Panel):
    bl_label = "Baking settings"
    bl_parent_id = "OCTANE_OBJECT_PT_octane_settings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
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


class OCTANE_OBJECT_PT_octane_settings_scatter_settings(OctaneButtonsPanel, Panel):
    bl_label = "Scatter settings"
    bl_parent_id = "OCTANE_OBJECT_PT_octane_settings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        ob = context.object
        octane_object = ob.octane

        sub = layout.row(align=True)
        sub.prop(octane_object, "scatter_id_source_type")
        if octane_object.scatter_id_source_type == "Attribute":
            sub = layout.row(align=True)
            sub.prop(octane_object, "scatter_id_source_instance_attribute")


class OCTANE_RENDER_PT_output(OctaneButtonsPanel, Panel):
    bl_label = "Octane Output"
    bl_context = "output"

    def draw_header(self, context):
        layout = self.layout
        oct_scene = context.scene.octane
        layout.active = oct_scene.use_octane_export
        layout.prop(oct_scene, "use_octane_export", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        oct_scene = scene.octane
        preferences = utility.get_preferences()
        row = layout.row(align=True)
        row.prop(oct_scene, "reuse_blender_output_path")
        if oct_scene.reuse_blender_output_path:
            row = layout.row(align=True)
            row.prop(scene.render, "filepath", text="")
        else:
            row = layout.row(align=True)
            row.prop(oct_scene, "octane_output_path", text="Octane Specific Output Path")
        row = layout.row(align=True)
        row.prop(oct_scene, "octane_export_prefix_tag")
        row = layout.row(align=True)
        row.prop(oct_scene, "octane_export_postfix_tag")
        row = layout.row(align=True)
        row.prop(oct_scene, "octane_export_mode")
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        if oct_scene.octane_export_mode == "SEPARATE_IMAGE_FILES":
            col.prop(oct_scene, "octane_export_file_type")
            if oct_scene.octane_export_file_type in ("PNG", "TIFF"):
                col.prop(oct_scene, "octane_integer_bit_depth")
            elif oct_scene.octane_export_file_type == "EXR":
                col.prop(oct_scene, "octane_float_bit_depth")
        else:
            col.label(text="Exported File type: EXR")
            col.prop(oct_scene, "octane_float_bit_depth")
        ocio_export_color_space_configs = "ocio_export_png_color_space_configs" \
            if oct_scene.octane_export_file_type in ("PNG", "TIFF", "JPEG") \
            else "ocio_export_exr_color_space_configs"
        col.prop_search(oct_scene, "gui_octane_export_ocio_color_space_name",
                        preferences, ocio_export_color_space_configs)
        if oct_scene.octane_export_file_type in ("PNG", "TIFF", "JPEG"):
            if oct_scene.gui_octane_export_ocio_color_space_name not in (" sRGB(default) ", ""):
                col.prop_search(oct_scene, "gui_octane_export_ocio_look", preferences, "ocio_export_look_configs")
                row = col.row(heading="Force use tone map")
                row.prop(oct_scene, "octane_export_force_use_tone_map", text="")
            if oct_scene.octane_export_file_type == "TIFF":
                row = col.row(heading="Premultiplied Alpha")
                row.prop(oct_scene, "octane_export_premultiplied_alpha", text="")
                col.prop(oct_scene, "octane_tiff_compression_mode")
            if oct_scene.octane_export_file_type == "JPEG":
                col.prop(oct_scene, "octane_export_jpeg_quality")
        else:
            if oct_scene.gui_octane_export_ocio_color_space_name not in (" Linear sRGB(default) ",
                                                                         " ACES2065-1 ", " ACEScg ", ""):
                col.prop_search(oct_scene, "gui_octane_export_ocio_look", preferences, "ocio_export_look_configs")
            row = col.row(heading="Force use tone map")
            row.prop(oct_scene, "octane_export_force_use_tone_map", text="")
            row = col.row(heading="Premultiplied Alpha")
            row.prop(oct_scene, "octane_export_premultiplied_alpha", text="")
            if oct_scene.octane_export_mode == "DEEP_EXR":
                col.prop(oct_scene, "octane_deep_exr_compression_mode")
            else:
                col.prop(oct_scene, "octane_exr_compression_mode")
                if oct_scene.octane_exr_compression_mode in ("DWAA_LOSSY", "DWAB_LOSSY"):
                    col.prop(oct_scene, "octane_export_dwa_compression_level")
        row = col.row(heading="Exclude Beauty")
        row.prop(oct_scene, "exclude_default_beauty_passes", text="")


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
    OCTANE_RENDER_PT_output,

    OCTANE_PT_mesh_properties,
    OCTANE_PT_mesh_properties_geometric_node,
    OCTANE_PT_mesh_properties_open_subdivision,
    OCTANE_PT_mesh_properties_sphere_attributes,
    OCTANE_PT_mesh_properties_orbx_properties,
    OCTANE_PT_mesh_properties_mesh_volume,
    OCTANE_PT_mesh_properties_offset_transform,
    OCTANE_PT_mesh_properties_legacy_settings,

    OCTANE_PT_volume_properties,
    OCTANE_RENDER_PT_SpherePrimitiveSettings,
    OCTANE_PT_context_material,
    OCTANE_MATERIAL_PT_surface,
    OCTANE_MATERIAL_PT_volume,
    OCTANE_MATERIAL_PT_settings,
    OCTANE_MATERIAL_PT_converters,

    OCTANE_OBJECT_PT_octane_settings,
    OCTANE_OBJECT_PT_octane_settings_object_layer,
    OCTANE_OBJECT_PT_octane_settings_baking_settings,
    OCTANE_OBJECT_PT_octane_settings_scatter_settings,
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
