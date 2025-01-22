# <pep8 compliant>
import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class

from octane.uis.common import OctanePropertyPanel
from octane.utils import utility


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


class OCTANE_MESH_PT_mesh_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Mesh Properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if OctanePropertyPanel.poll(context):
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


class OCTANE_MESH_PT_mesh_properties_geometric_node(OctanePropertyPanel, Panel):
    bl_label = "Geometric Node"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
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
        row.operator('octane.update_octane_geo_nodes', icon='FILE_REFRESH')
        row = col.row()
        row.prop_search(ob_data_octane.octane_geo_node_collections, "osl_geo_node",
                        ob_data_octane.octane_geo_node_collections, "osl_geo_nodes")
        osl_node_draw(context, col, str(ob_data_octane.octane_geo_node_collections.node_graph_tree),
                      str(ob_data_octane.octane_geo_node_collections.osl_geo_node))


class OCTANE_MESH_PT_mesh_properties_open_subdivision(OctanePropertyPanel, Panel):
    bl_label = "Open SubDivision"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
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


class OCTANE_MESH_PT_mesh_properties_sphere_attributes(OctanePropertyPanel, Panel):
    bl_label = "Sphere Attributes"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
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


class OCTANE_MESH_PT_mesh_properties_orbx_properties(OctanePropertyPanel, Panel):
    bl_label = "Orbx Properties"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
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


class OCTANE_MESH_PT_mesh_properties_mesh_volume(OctanePropertyPanel, Panel):
    bl_label = "Mesh volume"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
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
        row = col.row(align=True)
        row.prop(ob_data_octane, "enable_mesh_volume_sdf")
        row.active = not ob_data_octane.enable_mesh_volume
        col.prop(ob_data_octane, "mesh_volume_sdf_voxel_size")
        col.prop(ob_data_octane, "mesh_volume_sdf_border_thickness_inside")
        col.prop(ob_data_octane, "mesh_volume_sdf_border_thickness_outside")


class OCTANE_MESH_PT_mesh_properties_offset_transform(OctanePropertyPanel, Panel):
    bl_label = "Offset Transform"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return False

    def draw(self, context):
        return


class OCTANE_MESH_PT_mesh_properties_legacy_properties(OctanePropertyPanel, Panel):
    bl_label = "Legacy Properties"
    bl_parent_id = "OCTANE_MESH_PT_mesh_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        if OctanePropertyPanel.poll(context):
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
        box.label(text="Volume Properties:")
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
        if cdata.vdb_velocity_grid_type == 'Vector Grid':
            sub.prop_search(cdata, "vdb_vector_grid_id", cdata.octane_vdb_info, "vdb_vector_grid_id_container")
        else:
            sub.prop_search(cdata, "vdb_x_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_y_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_z_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")


class OCTANE_VOLUME_PT_volume_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Volume Properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if OctanePropertyPanel.poll(context):
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
        box.label(text="Volume Properties:")
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
        if cdata.vdb_velocity_grid_type == 'Vector Grid':
            sub.prop_search(cdata, "vdb_vector_grid_id", cdata.octane_vdb_info, "vdb_vector_grid_id_container")
        else:
            sub.prop_search(cdata, "vdb_x_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_y_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")
            sub.prop_search(cdata, "vdb_z_components_grid_id", cdata.octane_vdb_info, "vdb_float_grid_id_container")


class OCTANE_CURVE_PT_curve_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Curve Properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if super().poll(context):
            if context.curve:
                return True
        return False

    def draw(self, context):
        layout = self.layout
        curve = context.curve
        cdata = curve.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(cdata, "render_curve_as_octane_hair")
        if cdata.render_curve_as_octane_hair:
            col.prop(cdata, "hair_root_width")
            col.prop(cdata, "hair_tip_width")


class OCTANE_CURVE_PT_curve_properties_open_subdivision(OctanePropertyPanel, Panel):
    bl_label = "Open SubDivision"
    bl_parent_id = "OCTANE_CURVE_PT_curve_properties"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        ob_data_octane = ob_data.octane
        if ob_data_octane.render_curve_as_octane_hair:
            return
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(ob_data_octane, "open_subd_enable", text="Enable")
        col.prop(ob_data_octane, "open_subd_scheme")
        col.prop(ob_data_octane, "open_subd_bound_interp")
        col.prop(ob_data_octane, "open_subd_level")
        col.prop(ob_data_octane, "open_subd_sharpness")


class OCTANE_CURVES_PT_curves_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Curves Properties"
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        if super().poll(context):
            if context.curves:
                return True
        return False

    def draw(self, context):
        layout = self.layout
        curves = context.curves
        cdata = curves.octane
        col = layout.column(align=True)
        col.prop(cdata, "use_octane_radius_setting")
        if cdata.use_octane_radius_setting:
            sub = col.column(align=True)
            sub.prop(cdata, "hair_root_width")
            sub.prop(cdata, "hair_tip_width")


_CLASSES = [
    OCTANE_MESH_PT_mesh_properties,
    OCTANE_MESH_PT_mesh_properties_geometric_node,
    OCTANE_MESH_PT_mesh_properties_open_subdivision,
    OCTANE_MESH_PT_mesh_properties_sphere_attributes,
    OCTANE_MESH_PT_mesh_properties_orbx_properties,
    OCTANE_MESH_PT_mesh_properties_mesh_volume,
    OCTANE_MESH_PT_mesh_properties_offset_transform,
    OCTANE_MESH_PT_mesh_properties_legacy_properties,
    OCTANE_VOLUME_PT_volume_properties,
    OCTANE_CURVE_PT_curve_properties,
    OCTANE_CURVE_PT_curve_properties_open_subdivision,
    OCTANE_CURVES_PT_curves_properties,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
