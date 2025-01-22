# <pep8 compliant>

# noinspection PyUnresolvedReferences
from bl_ui.space_view3d import (
    VIEW3D_MT_editor_menus,
    VIEW3D_HT_header,
    VIEW3D_PT_overlay_bones,
    VIEW3D_PT_shading,
    draw_topbar_grease_pencil_layer_panel,
)
# noinspection PyUnresolvedReferences
from bpy.app.translations import (
    pgettext_iface as iface_,
)

import bpy
from octane import core
from octane.utils import runtime_globals

BLENDER_VIEW3D_HT_header_draw = None


def OCTANE_VIEW3D_HT_header_draw(self, context):
    layout = self.layout

    tool_settings = context.tool_settings
    view = context.space_data
    shading = view.shading

    layout.row(align=True).template_header()

    row = layout.row(align=True)
    obj = context.active_object
    mode_string = context.mode
    object_mode = 'OBJECT' if obj is None else obj.mode
    has_pose_mode = (
            (object_mode == 'POSE') or
            (object_mode == 'WEIGHT_PAINT' and context.pose_object is not None)
    )

    # Note: This is actually deadly in case enum_items have to be dynamically generated
    #       (because internal RNA array iterator will free everything immediately...).
    # XXX This is an RNA internal issue, not sure how to fix it.
    # Note: Tried to add an accessor to get translated UI strings instead of manual call
    #       to pgettext_iface below, but this fails because translated enum-items
    #       are always dynamically allocated.
    act_mode_item = bpy.types.Object.bl_rna.properties["mode"].enum_items[object_mode]
    act_mode_i18n_context = bpy.types.Object.bl_rna.properties["mode"].translation_context

    sub = row.row(align=True)
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

    # Grease Pencil v3
    if obj and obj.type == 'GREASEPENCIL':
        # Select mode for Editing
        if object_mode == 'EDIT':
            row = layout.row(align=True)
            row.operator(
                "grease_pencil.set_selection_mode",
                text="",
                icon='GP_SELECT_POINTS',
                depress=(tool_settings.gpencil_selectmode_edit == 'POINT'),
            ).mode = 'POINT'
            row.operator(
                "grease_pencil.set_selection_mode",
                text="",
                icon='GP_SELECT_STROKES',
                depress=(tool_settings.gpencil_selectmode_edit == 'STROKE'),
            ).mode = 'STROKE'
            row.operator(
                "grease_pencil.set_selection_mode",
                text="",
                icon='GP_SELECT_BETWEEN_STROKES',
                depress=(tool_settings.gpencil_selectmode_edit == 'SEGMENT'),
            ).mode = 'SEGMENT'

        if object_mode == 'SCULPT_GREASE_PENCIL':
            row = layout.row(align=True)
            row.prop(tool_settings, "use_gpencil_select_mask_point", text="")
            row.prop(tool_settings, "use_gpencil_select_mask_stroke", text="")
            row.prop(tool_settings, "use_gpencil_select_mask_segment", text="")

        if object_mode == 'VERTEX_GREASE_PENCIL':
            row = layout.row(align=True)
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_point", text="")
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_stroke", text="")
            row.prop(tool_settings, "use_gpencil_vertex_select_mask_segment", text="")

    overlay = view.overlay

    VIEW3D_MT_editor_menus.draw_collapsible(context, layout)

    layout.separator_spacer()

    if object_mode in {'PAINT_GREASE_PENCIL', 'SCULPT_GREASE_PENCIL'}:
        # Grease pencil
        if object_mode == 'PAINT_GREASE_PENCIL':
            sub = layout.row(align=True)
            sub.prop_with_popover(
                tool_settings,
                "gpencil_stroke_placement_view3d",
                text="",
                panel="VIEW3D_PT_grease_pencil_origin",
            )

        if object_mode in {'PAINT_GREASE_PENCIL', 'SCULPT_GREASE_PENCIL'}:
            sub = layout.row(align=True)
            sub.active = tool_settings.gpencil_stroke_placement_view3d != 'SURFACE'
            sub.prop_with_popover(
                tool_settings.gpencil_sculpt,
                "lock_axis",
                text="",
                panel="VIEW3D_PT_grease_pencil_lock",
            )

        draw_topbar_grease_pencil_layer_panel(context, layout)

        if object_mode == 'PAINT_GREASE_PENCIL':
            # FIXME: this is bad practice!
            # Tool options are to be displayed in the top-bar.
            tool = context.workspace.tools.from_space_view3d_mode(object_mode)
            if tool and tool.idname == "builtin_brush.Draw":
                settings = tool_settings.gpencil_sculpt.guide
                row = layout.row(align=True)
                row.prop(settings, "use_guide", text="", icon='GRID')
                sub = row.row(align=True)
                sub.active = settings.use_guide
                sub.popover(
                    panel="VIEW3D_PT_grease_pencil_guide",
                    text="Guides",
                )

    elif object_mode == 'SCULPT':
        # If the active tool supports it, show the canvas selector popover.
        from bl_ui.space_toolsystem_common import ToolSelectPanelHelper
        tool = ToolSelectPanelHelper.tool_active_from_context(context)

        is_paint_tool = False
        if tool.use_brushes:
            paint = tool_settings.sculpt
            brush = paint.brush
            if brush:
                is_paint_tool = brush.sculpt_tool in {'PAINT', 'SMEAR'}
        else:
            is_paint_tool = tool and tool.use_paint_canvas

        shading = VIEW3D_PT_shading.get_shading(context)
        color_type = shading.color_type

        row = layout.row()
        row.active = is_paint_tool and color_type == 'VERTEX'

        if context.preferences.experimental.use_sculpt_texture_paint:
            canvas_source = tool_settings.paint_mode.canvas_source
            icon = 'GROUP_VCOL' if canvas_source == 'COLOR_ATTRIBUTE' else canvas_source
            row.popover(panel="VIEW3D_PT_slots_paint_canvas", icon=icon)
        else:
            row.popover(panel="VIEW3D_PT_slots_color_attributes", icon='GROUP_VCOL')

        layout.popover(
            panel="VIEW3D_PT_sculpt_snapping",
            icon='SNAP_INCREMENT',
            text="",
            translate=False,
        )

        layout.popover(
            panel="VIEW3D_PT_sculpt_automasking",
            text="",
            icon=VIEW3D_HT_header._sculpt_automasking_icon(tool_settings.sculpt),
        )

    elif object_mode == 'VERTEX_PAINT':
        row = layout.row()
        row.popover(panel="VIEW3D_PT_slots_color_attributes", icon='GROUP_VCOL')
    elif object_mode == 'VERTEX_GREASE_PENCIL':
        draw_topbar_grease_pencil_layer_panel(context, layout)
    elif object_mode == 'WEIGHT_PAINT':
        row = layout.row()
        row.popover(panel="VIEW3D_PT_slots_vertex_groups", icon='GROUP_VERTEX')

        layout.popover(
            panel="VIEW3D_PT_sculpt_snapping",
            icon='SNAP_INCREMENT',
            text="",
            translate=False,
        )
    elif object_mode == 'WEIGHT_GREASE_PENCIL':
        row = layout.row()
        row.popover(panel="VIEW3D_PT_slots_vertex_groups", icon='GROUP_VERTEX')
        draw_topbar_grease_pencil_layer_panel(context, row)

    elif object_mode == 'TEXTURE_PAINT':
        tool_mode = tool_settings.image_paint.mode
        icon = 'MATERIAL' if tool_mode == 'MATERIAL' else 'IMAGE_DATA'

        row = layout.row()
        row.popover(panel="VIEW3D_PT_slots_projectpaint", icon=icon)
        row.popover(
            panel="VIEW3D_PT_mask",
            icon=VIEW3D_HT_header._texture_mask_icon(tool_settings.image_paint),
            text="")
    else:
        # Transform settings depending on tool header visibility
        VIEW3D_HT_header.draw_xform_template(layout, context)

    layout.separator_spacer()

    # Octane specific buttons
    row = layout.row(align=True)
    row.operator("octane.focus_picker", text="", icon_value=runtime_globals.OCTANE_ICONS['PICK af'].icon_id)
    row.operator("octane.whitebalance_picker", text="", icon_value=runtime_globals.OCTANE_ICONS['PICKWB'].icon_id)
    row.operator("octane.material_picker", text="", icon_value=runtime_globals.OCTANE_ICONS['PICK material'].icon_id)

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

    if mode_string == 'EDIT_MESH':
        sub.popover(panel="VIEW3D_PT_overlay_edit_mesh", text="", icon='EDITMODE_HLT')
    if mode_string == 'EDIT_CURVE':
        sub.popover(panel="VIEW3D_PT_overlay_edit_curve", text="", icon='EDITMODE_HLT')
    elif mode_string == 'SCULPT':
        sub.popover(panel="VIEW3D_PT_overlay_sculpt", text="", icon='SCULPTMODE_HLT')
    elif mode_string == 'SCULPT_CURVES':
        sub.popover(panel="VIEW3D_PT_overlay_sculpt_curves", text="", icon='SCULPTMODE_HLT')
    elif mode_string == 'PAINT_WEIGHT':
        sub.popover(panel="VIEW3D_PT_overlay_weight_paint", text="", icon='WPAINT_HLT')
    elif mode_string == 'PAINT_TEXTURE':
        sub.popover(panel="VIEW3D_PT_overlay_texture_paint", text="", icon='TPAINT_HLT')
    elif mode_string == 'PAINT_VERTEX':
        sub.popover(panel="VIEW3D_PT_overlay_vertex_paint", text="", icon='VPAINT_HLT')
    elif obj is not None and obj.type == 'GREASEPENCIL':
        sub.popover(panel="VIEW3D_PT_overlay_grease_pencil_options", text="", icon='OUTLINER_DATA_GREASEPENCIL')

    # Separate from `elif` chain because it may coexist with weight-paint.
    if (
            has_pose_mode or
            (object_mode in {'EDIT_ARMATURE', 'OBJECT'} and VIEW3D_PT_overlay_bones.is_using_wireframe(context))
    ):
        sub.popover(panel="VIEW3D_PT_overlay_bones", text="", icon='POSE_HLT')

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
    if context.engine == "octane" and core.ENABLE_OCTANE_ADDON_CLIENT:
        oct_shading = shading.octane
        row.prop(oct_shading, "shading_type", text="", expand=True)
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
    # if not core.ENABLE_OCTANE_ADDON_CLIENT:
    #     return
    global BLENDER_VIEW3D_HT_header_draw
    BLENDER_VIEW3D_HT_header_draw = bpy.types.VIEW3D_HT_header.draw
    bpy.types.VIEW3D_HT_header.draw = OCTANE_VIEW3D_HT_header_draw


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
    # if not core.ENABLE_OCTANE_ADDON_CLIENT:
    #     return
    bpy.types.VIEW3D_HT_header.draw = BLENDER_VIEW3D_HT_header_draw
