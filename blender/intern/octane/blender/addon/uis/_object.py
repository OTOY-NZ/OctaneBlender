# <pep8 compliant>

from bpy.utils import register_class, unregister_class
from bpy.types import Panel
from octane.uis.common import OctanePropertyPanel
from octane.utils import utility


class OCTANE_OBJECT_PT_object_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Object Properties"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (OctanePropertyPanel.poll(context) and
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


class OCTANE_OBJECT_PT_object_properties_object_layer(OctanePropertyPanel, Panel):
    bl_label = "Object Layer"
    bl_parent_id = "OCTANE_OBJECT_PT_object_properties"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        ob = context.object
        octane_object = ob.octane
        orbx_path = ""
        is_object_layer_applicable = True
        if ob.data is not None:
            if ob.type == "MESH":
                orbx_path = getattr(ob.data.octane, "imported_orbx_file_path", "")
                try:
                    is_object_layer_applicable = ob.data.octane.octane_geo_node_collections.is_object_layer_applicable()
                except:  # noqa
                    is_object_layer_applicable = False
        if not is_object_layer_applicable:
            sub = layout.row(align=True)
            sub.label(text="This object is used as Octane Scatter or SDF Domain.")
            sub = layout.row(align=True)
            sub.label(text="Object Layer Data is not applicable in this case.")
            return
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
        sub.prop(octane_object, "round_edge_visibility")

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


class OCTANE_OBJECT_PT_object_properties_baking(OctanePropertyPanel, Panel):
    bl_label = "Baking"
    bl_parent_id = "OCTANE_OBJECT_PT_object_properties"
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


class OCTANE_OBJECT_PT_object_properties_scattering(OctanePropertyPanel, Panel):
    bl_label = "Scattering"
    bl_parent_id = "OCTANE_OBJECT_PT_object_properties"
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


class OCTANE_OBJECT_PT_motion_blur(OctanePropertyPanel, Panel):
    bl_label = "Motion Blur"
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        rd = context.scene.render
        layout.active = rd.use_motion_blur
        ob = context.object
        layout.prop(ob.octane, "use_motion_blur", text="")

    def draw(self, context):
        layout = self.layout
        rd = context.scene.render
        ob = context.object
        layout.active = (rd.use_motion_blur and ob.octane.use_motion_blur)
        row = layout.row()
        if ob.type != 'CAMERA':
            row.prop(ob.octane, "use_deform_motion", text="Deformation")
        row.prop(ob.octane, "motion_steps", text="Steps")
        if ob.instance_type == 'COLLECTION' and ob.instance_collection:
            row = layout.row()
            row.operator("octane.sync_motion_blur_to_objects_in_collection",
                         text="Sync Settings to Children Objects")
        # if ob.octane.use_deform_motion and getattr(getattr(ob, "data", None), "use_auto_smooth", False):
        #     row = layout.row()
        #     row.label(text="Deformation motion blur may not work on objects with Auto Smooth", icon="INFO")


class OCTANE_OBJECT_PT_offset_transform(OctanePropertyPanel, Panel):
    bl_label = "Offset Transform"
    bl_parent_id = "OCTANE_OBJECT_PT_object_properties"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        ob = context.object
        ob_data = ob.data
        if ob_data is None:
            return
        octane_object = ob.octane
        col = layout.column(align=True)
        col.use_property_split = True
        col.use_property_decorate = False
        col.prop(octane_object, "enable_octane_offset_transform")
        col.prop(octane_object, "octane_offset_translation")
        col.prop(octane_object, "octane_offset_rotation_order")
        col.prop(octane_object, "octane_offset_rotation")
        col.prop(octane_object, "octane_offset_scale")


_CLASSES = [
    OCTANE_OBJECT_PT_object_properties,
    OCTANE_OBJECT_PT_object_properties_object_layer,
    OCTANE_OBJECT_PT_object_properties_baking,
    OCTANE_OBJECT_PT_object_properties_scattering,
    OCTANE_OBJECT_PT_motion_blur,
    OCTANE_OBJECT_PT_offset_transform,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
