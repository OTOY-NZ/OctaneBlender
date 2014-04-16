/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2008 Blender Foundation.
 * All rights reserved.
 *
 *
 * Contributor(s): Blender Foundation
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file blender/editors/space_mat_livedb/mat_livedb_ops.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#include "DNA_space_types.h"
#include "RNA_access.h"
#include "WM_api.h"
#include "WM_types.h"


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Registration */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_operatortypes(void)
{
    WM_operatortype_append(MAT_LIVEDB_OT_item_activate);
    WM_operatortype_append(MAT_LIVEDB_OT_item_openclose);
    WM_operatortype_append(MAT_LIVEDB_OT_item_rename);
    WM_operatortype_append(MAT_LIVEDB_OT_operation);
    WM_operatortype_append(MAT_LIVEDB_OT_material_operation);
    WM_operatortype_append(MAT_LIVEDB_OT_group_operation);

    WM_operatortype_append(MAT_LIVEDB_OT_show_one_level);
    WM_operatortype_append(MAT_LIVEDB_OT_hide_one_level);
    WM_operatortype_append(MAT_LIVEDB_OT_scroll_page_up);
    WM_operatortype_append(MAT_LIVEDB_OT_scroll_page_down);

    WM_operatortype_append(MAT_LIVEDB_OT_selected_toggle);
    WM_operatortype_append(MAT_LIVEDB_OT_expanded_toggle);
} /* mat_livedb_operatortypes() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Registration */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_keymap(struct wmKeyConfig *keyconf)
{
    wmKeyMapItem    *kmi;
    wmKeyMap        *keymap = WM_keymap_find(keyconf, "MatLiveDB", SPACE_MAT_LIVEDB, 0);

    kmi = WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_activate", LEFTMOUSE, KM_CLICK, 0, 0);
    RNA_boolean_set(kmi->ptr, "extend", 0);

    kmi = WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_activate", LEFTMOUSE, KM_CLICK, KM_SHIFT, 0);
    RNA_boolean_set(kmi->ptr, "extend", 1);

    kmi = WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_openclose", RETKEY, KM_PRESS, 0, 0);
    RNA_boolean_set(kmi->ptr, "all", 0);
    kmi = WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_openclose", RETKEY, KM_PRESS, KM_SHIFT, 0);
    RNA_boolean_set(kmi->ptr, "all", 1);

    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_rename", LEFTMOUSE, KM_DBL_CLICK, 0, 0);
    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_item_rename", LEFTMOUSE, KM_PRESS, KM_CTRL, 0);
    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_operation", RIGHTMOUSE, KM_PRESS, 0, 0);

    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_scroll_page_down", PAGEDOWNKEY, KM_PRESS, 0, 0);
    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_scroll_page_up", PAGEUPKEY, KM_PRESS, 0, 0);

    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_show_one_level", PADPLUSKEY, KM_PRESS, 0, 0);
    WM_keymap_add_item(keymap, "MAT_LIVEDB_OT_hide_one_level", PADMINUS, KM_PRESS, 0, 0);

    WM_keymap_verify_item(keymap, "MAT_LIVEDB_OT_selected_toggle", AKEY, KM_PRESS, 0, 0);
    WM_keymap_verify_item(keymap, "MAT_LIVEDB_OT_expanded_toggle", AKEY, KM_PRESS, KM_SHIFT, 0);
} /* mat_livedb_keymap() */
