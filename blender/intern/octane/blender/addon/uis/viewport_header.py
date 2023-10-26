import bpy
from bpy.types import (
    Header,
    Menu,
    Panel,
)
from bl_ui.properties_paint_common import (
    UnifiedPaintPanel,
    brush_basic_texpaint_settings,
    brush_basic_gpencil_weight_settings,
)
from bl_ui.properties_grease_pencil_common import (
    AnnotationDataPanel,
    AnnotationOnionSkin,
    GreasePencilMaterialsPanel,
    GreasePencilVertexcolorPanel,
)
from bl_ui.space_toolsystem_common import (
    ToolActivePanelHelper,
)
from bpy.app.translations import (
    pgettext_iface as iface_,
    pgettext_tip as tip_,
    contexts as i18n_contexts,
)
from bl_ui.space_view3d import (
    VIEW3D_MT_editor_menus, 
    VIEW3D_HT_header
)
from octane import core


_VIEW3D_HT_header_draw = None


def Octane_VIEW3D_HT_header_draw(self, context):
    layout = self.layout

    tool_settings = context.tool_settings
    view = context.space_data
    shading = view.shading

    layout.row(align=True).template_header()

    row = layout.row(align=True)
    obj = context.active_object
    # mode_string = context.mode
    object_mode = 'OBJECT' if obj is None else obj.mode
    has_pose_mode = (
        (object_mode == 'POSE') or
        (object_mode == 'WEIGHT_PAINT' and context.pose_object is not None)
    )

    # Note: This is actually deadly in case enum_items have to be dynamically generated
    #       (because internal RNA array iterator will free everything immediately...).
    # XXX This is an RNA internal issue, not sure how to fix it.
    # Note: Tried to add an accessor to get translated UI strings instead of manual call
    #       to pgettext_iface below, but this fails because translated enumitems
    #       are always dynamically allocated.
    act_mode_item = bpy.types.Object.bl_rna.properties["mode"].enum_items[object_mode]
    act_mode_i18n_context = bpy.types.Object.bl_rna.properties["mode"].translation_context

    sub = row.row(align=True)
    sub.ui_units_x = 5.5
    sub.operator_menu_enum(
        "object.mode_set", "mode",
        text=iface_(act_mode_item.name, act_mode_i18n_context),
        icon=act_mode_item.icon,
    )
    del act_mode_item

    layout.template_header_3D_mode()

    # Contains buttons like Mode, Pivot, Layer, Mesh Select Mode...
    if obj:
        # Particle edit
        if object_mode == 'PARTICLE_EDIT':
            row = layout.row()
            row.prop(tool_settings.particle_edit, "select_mode", text="", expand=True)
        elif object_mode in {'EDIT', 'SCULPT_CURVES'} and obj.type == 'CURVES':
            curves = obj.data

            row = layout.row(align=True)
            domain = curves.selection_domain
            row.operator(
                "curves.set_selection_domain",
                text="",
                icon='CURVE_BEZCIRCLE',
                depress=(domain == 'POINT'),
            ).domain = 'POINT'
            row.operator(
                "curves.set_selection_domain",
                text="",
                icon='CURVE_PATH',
                depress=(domain == 'CURVE'),
            ).domain = 'CURVE'

    # Grease Pencil
    if obj and obj.type == 'GPENCIL' and context.gpencil_data:
        gpd = context.gpencil_data

        if gpd.is_stroke_paint_mode:
            row = layout.row()
            sub = row.row(align=True)
            sub.prop(tool_settings, "use_gpencil_draw_onback", text="", icon='MOD_OPACITY')
            sub.separator(factor=0.4)
            sub.prop(tool_settings, "use_gpencil_automerge_strokes", text="")
            sub.separator(factor=0.4)
            sub.prop(tool_settings, "use_gpencil_weight_data_add", text="", icon='WPAINT_HLT')
            sub.separator(factor=0.4)
            sub.prop(tool_settings, "use_gpencil_draw_additive", text="", icon='FREEZE')

        # Select mode for Editing
        if gpd.use_stroke_edit_mode:
            row = layout.row(align=True)
            row.prop_enum(tool_settings, "gpencil_selectmode_edit", text="", value='POINT')
            row.prop_enum(tool_settings, "gpencil_selectmode_edit", text="", value='STROKE')

            subrow = row.row(align=True)
            subrow.enabled = not gpd.use_curve_edit
            subrow.prop_enum(tool_settings, "gpencil_selectmode_edit", text="", value='SEGMENT')

            # Curve edit submode
            row = layout.row(align=True)
            row.prop(gpd, "use_curve_edit", text="",
                     icon='IPO_BEZIER')
            sub = row.row(align=True)
            sub.active = gpd.use_curve_edit
            sub.popover(
                panel="VIEW3D_PT_gpencil_curve_edit",
                text="Curve Editing",
            )

        # Select mode for Sculpt
        if gpd.is_stroke_sculpt_mode:
            row = layout.row(align=True)
            row.prop(tool_settings, "use_gpencil_select_mask_point", text="")
            row.prop(tool_settings, "use_gpencil_select_mask_stroke", text="")
            row.prop(tool_settings, "use_gpencil_select_mask_segment", text="")

        # Select mode for Vertex Paint
        if gpd.is_stroke_vertex_mode:
            row = layout.row(align=True)
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_point", text="")
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_stroke", text="")
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_segment", text="")

        if gpd.is_stroke_paint_mode:
            row = layout.row(align=True)
            row.prop(gpd, "use_multiedit", text="", icon='GP_MULTIFRAME_EDITING')

        if (
                gpd.use_stroke_edit_mode or
                gpd.is_stroke_sculpt_mode or
                gpd.is_stroke_weight_mode or
                gpd.is_stroke_vertex_mode
        ):
            row = layout.row(align=True)
            row.prop(gpd, "use_multiedit", text="", icon='GP_MULTIFRAME_EDITING')

            sub = row.row(align=True)
            sub.enabled = gpd.use_multiedit
            sub.popover(
                panel="VIEW3D_PT_gpencil_multi_frame",
                text="Multiframe",
            )

    overlay = view.overlay

    VIEW3D_MT_editor_menus.draw_collapsible(context, layout)

    layout.separator_spacer()

    if object_mode in {'PAINT_GPENCIL', 'SCULPT_GPENCIL'}:
        # Grease pencil
        if object_mode == 'PAINT_GPENCIL':
            layout.prop_with_popover(
                tool_settings,
                "gpencil_stroke_placement_view3d",
                text="",
                panel="VIEW3D_PT_gpencil_origin",
            )

        if object_mode in {'PAINT_GPENCIL', 'SCULPT_GPENCIL'}:
            layout.prop_with_popover(
                tool_settings.gpencil_sculpt,
                "lock_axis",
                text="",
                panel="VIEW3D_PT_gpencil_lock",
            )

        if object_mode == 'PAINT_GPENCIL':
            # FIXME: this is bad practice!
            # Tool options are to be displayed in the topbar.
            if context.workspace.tools.from_space_view3d_mode(object_mode).idname == "builtin_brush.Draw":
                settings = tool_settings.gpencil_sculpt.guide
                row = layout.row(align=True)
                row.prop(settings, "use_guide", text="", icon='GRID')
                sub = row.row(align=True)
                sub.active = settings.use_guide
                sub.popover(
                    panel="VIEW3D_PT_gpencil_guide",
                    text="Guides",
                )
        if object_mode == 'SCULPT_GPENCIL':
            layout.popover(
                panel="VIEW3D_PT_gpencil_sculpt_automasking",
                text="",
                icon='MOD_MASK',
            )
    elif object_mode == 'SCULPT':
        layout.popover(
            panel="VIEW3D_PT_sculpt_automasking",
            text="",
            icon='MOD_MASK',
        )
    else:
        # Transform settings depending on tool header visibility
        VIEW3D_HT_header.draw_xform_template(layout, context)

    layout.separator_spacer()

    # Viewport Settings
    layout.popover(
        panel="VIEW3D_PT_object_type_visibility",
        icon_value=view.icon_from_show_object_viewport,
        text="",
    )

    # Gizmo toggle & popover.
    row = layout.row(align=True)
    # FIXME: place-holder icon.
    row.prop(view, "show_gizmo", text="", toggle=True, icon='GIZMO')
    sub = row.row(align=True)
    sub.active = view.show_gizmo
    sub.popover(
        panel="VIEW3D_PT_gizmo_display",
        text="",
    )

    # Overlay toggle & popover.
    row = layout.row(align=True)
    row.prop(overlay, "show_overlays", icon='OVERLAY', text="")
    sub = row.row(align=True)
    sub.active = overlay.show_overlays
    sub.popover(panel="VIEW3D_PT_overlay", text="")

    row = layout.row()
    row.active = (object_mode == 'EDIT') or (shading.type in {'WIREFRAME', 'SOLID'})

    # While exposing `shading.show_xray(_wireframe)` is correct.
    # this hides the key shortcut from users: #70433.
    if has_pose_mode:
        draw_depressed = overlay.show_xray_bone
    elif shading.type == 'WIREFRAME':
        draw_depressed = shading.show_xray_wireframe
    else:
        draw_depressed = shading.show_xray
    row.operator(
        "view3d.toggle_xray",
        text="",
        icon='XRAY',
        depress=draw_depressed,
    )

    row = layout.row(align=True)
    if context.engine == "octane":
        scene = context.scene
        oct_scene = scene.octane
        row.prop(oct_scene, "octane_shading_type", text="", expand=True)
    else:
        row.prop(shading, "type", text="", expand=True)
    sub = row.row(align=True)
    # TODO, currently render shading type ignores mesh two-side, until it's supported
    # show the shading popover which shows double-sided option.

    # sub.enabled = shading.type != 'RENDERED'
    sub.popover(panel="VIEW3D_PT_shading", text="")


_CLASSES = [
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        return
    _VIEW3D_HT_header_draw = bpy.types.VIEW3D_HT_header.draw
    bpy.types.VIEW3D_HT_header.draw = Octane_VIEW3D_HT_header_draw


def unregister():
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        return    
    for cls in _CLASSES:
        unregister_class(cls)
    bpy.types.VIEW3D_HT_header.draw = _VIEW3D_HT_header_draw