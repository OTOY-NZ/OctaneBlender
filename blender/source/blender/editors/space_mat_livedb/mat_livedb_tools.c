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
 * The Original Code is Copyright (C) 2004 Blender Foundation.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): Joshua Leung
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file blender/editors/space_mat_livedb/mat_livedb_tools.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#include <string.h>

#include "MEM_guardedalloc.h"

#include "BKE_context.h"
#include "ED_screen.h"
#include "ED_util.h"

#include "WM_api.h"
#include "WM_types.h"

#include "UI_interface.h"
#include "UI_view2d.h"

#include "RNA_access.h"
#include "RNA_define.h"


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Delete item callback */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_item_delete_cb(bContext *C, LiveDbTreeElement *te)
{
    if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_MATERIAL)
        *te->flag |= TE_DELETED;
} /* mat_livedb_item_delete_cb() */

#ifndef WIN32
#   pragma suppress(all_checks)
#else
#   pragma runtime_checks("s", off)
#endif
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Compress tree data (freee deleted items) */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_compress_tree(bContext *C)
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    size_t      store_len   = MEM_allocN_len(slivedb->treestore);
    size_t      new_len     = 0;
    LiveDbItem  *new_items;
    LiveDbItem  *new_item;
    LiveDbItem  *cur_item, *cur_category;

    for(cur_item = slivedb->treestore; (((char*)cur_item + cur_item->size) - slivedb->treestore) <= store_len; cur_item = (LiveDbItem*)((char*)cur_item + cur_item->size)) {
        if(TE_GET_TYPE(cur_item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            new_len += cur_item->size;
        else {
            if(!(cur_item->type & (TE_DELETED << 16))) {
                new_len += cur_item->size;
            }
        }
    }

    new_items = MEM_mallocN(new_len, "ldb tree");
    new_item  = new_items;

    for(cur_item = slivedb->treestore; (((char*)cur_item + cur_item->size) - slivedb->treestore) <= store_len; cur_item = (LiveDbItem*)((char*)cur_item + cur_item->size)) {
        if(TE_GET_TYPE(cur_item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY) {
            memcpy(new_item, cur_item, cur_item->size);
            cur_category = new_item;
            new_item = (LiveDbItem*)((char*)new_item + new_item->size);
        }
        else {
            if(cur_item->type & (TE_DELETED << 16))
                if(cur_category->cat_item.mat_cnt) --cur_category->cat_item.mat_cnt;
            else {
                memcpy(new_item, cur_item, cur_item->size);
                new_item = (LiveDbItem*)((char*)new_item + new_item->size);
            }
        }
    }
    MEM_freeN(slivedb->treestore);
    slivedb->treestore = new_items;
} /* mat_livedb_compress_tree() */
#ifndef WIN32
#   pragma unsuppress(all_checks)
#else
#   pragma runtime_checks("s", restore)
#endif

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Do item operation */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_do_item_operation(bContext *C, SpaceLDB *slivedb, ListBase *lb, void (*operation_cb)(bContext *C, LiveDbTreeElement *))
{
    LiveDbTreeElement *te;

    for (te = lb->first; te; te = te->next) {
        if (*te->flag & TE_SELECTED)
            operation_cb(C, te);
        if (MAT_LIVEDB_ELEM_OPEN(te, slivedb))
            mat_livedb_do_item_operation(C, slivedb, &te->subtree, operation_cb);
    }
} /* mat_livedb_do_item_operation() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB material operations menu data */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
enum {
    LDB_MAT_OP_ENDMARKER = 0,
    LDB_MAT_OP_DELETE,
    LDB_MAT_OP_RENAME
};

static EnumPropertyItem prop_material_op_types[] = {
    {LDB_MAT_OP_DELETE, "DELETE", 0, "Delete", ""},
    {LDB_MAT_OP_RENAME, "RENAME", 0, "Rename", ""},
    {LDB_MAT_OP_ENDMARKER, NULL, 0, NULL, NULL}
};

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB material operations menu */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_material_operation_exec(bContext *C, wmOperator *op)
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    const char  *str        = 0;
    int         event;

    /* check for invalid states */
    if (slivedb == 0)
        return OPERATOR_CANCELLED;

    event = RNA_enum_get(op->ptr, "type");

    if (event == LDB_MAT_OP_DELETE) {
        mat_livedb_do_item_operation(C, slivedb, &slivedb->tree, mat_livedb_item_delete_cb);

        mat_livedb_compress_tree(C);
        mat_livedb_free_tree(&slivedb->tree);
        ED_region_tag_redraw(ar);

        str = "Delete LiveDB Material";
    }
    else if (event == LDB_MAT_OP_RENAME) {
        mat_livedb_do_item_operation(C, slivedb, &slivedb->tree, mat_livedb_item_rename_cb);
        str = "Rename LiveDB Material";
    }

    ED_undo_push(C, str);

    return OPERATOR_FINISHED;
} /* mat_livedb_material_operation_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB material operations menu operator */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_material_operation(wmOperatorType *ot)
{
    ot->name        = "LiveDB Material Operation";
    ot->idname      = "MAT_LIVEDB_OT_material_operation";
    ot->description = "";
    ot->invoke      = WM_menu_invoke;
    ot->exec        = mat_livedb_material_operation_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    ot->flag        = 0;
    ot->prop        = RNA_def_enum(ot->srna, "type", prop_material_op_types, 0, "Material Operation", "");
} /* MAT_LIVEDB_OT_material_operation() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB group operations menu data */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
enum {
    LDB_GROUP_OP_ENDMARKER = 0,
    LDB_GROUP_OP_DELETE,
    LDB_GROUP_OP_RENAME,
    LDB_GROUP_OP_ADD_MAT
};

static EnumPropertyItem prop_group_op_types[] = {
    {LDB_GROUP_OP_DELETE, "DELETE",   0, "Delete Group", ""},
    {LDB_GROUP_OP_RENAME, "RENAME",   0, "Rename Group", ""},
    {LDB_GROUP_OP_ADD_MAT, "ADD_MATERIAL",     0, "Add Material to Group", ""},
    {LDB_GROUP_OP_ENDMARKER, NULL, 0, NULL, NULL}
};

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB group operations menu */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_group_operation_exec(bContext *C, wmOperator *op)
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    int event;

    /* check for invalid states */
    if (slivedb == 0)
        return OPERATOR_CANCELLED;

    event = RNA_enum_get(op->ptr, "type");

    switch (event) {
        case LDB_GROUP_OP_DELETE:
            mat_livedb_do_item_operation(C, slivedb, &slivedb->tree, mat_livedb_item_delete_cb);

            mat_livedb_compress_tree(C);
            mat_livedb_free_tree(&slivedb->tree);
            ED_region_tag_redraw(ar);
            break;
        case LDB_GROUP_OP_RENAME:
            mat_livedb_do_item_operation(C, slivedb, &slivedb->tree, mat_livedb_item_rename_cb);
            break;
        case LDB_GROUP_OP_ADD_MAT:
            mat_livedb_do_item_operation(C, slivedb, &slivedb->tree, mat_livedb_item_rename_cb);
            break;
        default:
            BLI_assert(0);
            return OPERATOR_CANCELLED;
    }

    ED_undo_push(C, prop_group_op_types[event].name);

    return OPERATOR_FINISHED;
} /* mat_livedb_group_operation_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB group operations menu operator */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_group_operation(wmOperatorType *ot)
{
    ot->name        = "Materials LiveDB Group Operation";
    ot->idname      = "MAT_LIVEDB_OT_group_operation";
    ot->description = "";
    ot->invoke      = WM_menu_invoke;
    ot->exec        = mat_livedb_group_operation_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    ot->flag        = 0;
    ot->prop        = RNA_def_enum(ot->srna, "type", prop_group_op_types, 0, "Group Operation", "");
} /* MAT_LIVEDB_OT_group_operation() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB operation event */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int do_mat_livedb_operation_event(bContext *C, ARegion *ar, SpaceLDB *slivedb, LiveDbTreeElement *te, const float mval[2])
{
    if (mval[1] > te->ys && mval[1] < te->ys + MAT_LIVEDB_UI_UNIT_Y) {
        /* select object that's clicked on and popup context menu */
        mat_livedb_set_flag(slivedb, &slivedb->tree, TE_ACTIVE, 0);
        *te->flag |= TE_ACTIVE;

        if (!(*te->flag & TE_SELECTED)) {
            if (mat_livedb_has_one_flag(slivedb, &slivedb->tree, TE_SELECTED, 1))
                mat_livedb_set_flag(slivedb, &slivedb->tree, TE_SELECTED, 0);

            *te->flag |= TE_SELECTED;
            /* redraw, same as mat_livedb_select function */
            slivedb->storeflag |= LDB_TREESTORE_REDRAW;
            ED_region_tag_redraw(ar);
        }

        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_MATERIAL)
            WM_operator_name_call(C, "MAT_LIVEDB_OT_material_operation", WM_OP_INVOKE_REGION_WIN, NULL);
        else
            WM_operator_name_call(C, "MAT_LIVEDB_OT_group_operation", WM_OP_INVOKE_REGION_WIN, NULL);

        return 1;
    }
    for (te = te->subtree.first; te; te = te->next) {
        if (do_mat_livedb_operation_event(C, ar, slivedb, te, mval))
            return 1;
    }
    return 0;
} /* do_mat_livedb_operation_event() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB operation */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_operation(bContext *C, wmOperator *UNUSED(op), const wmEvent *event)
{
    ARegion             *ar         = CTX_wm_region(C);
    SpaceLDB            *slivedb    = CTX_wm_space_mat_livedb(C);
    LiveDbTreeElement   *te;
    float               fmval[2];

    UI_view2d_region_to_view(&ar->v2d, event->mval[0], event->mval[1], fmval, fmval + 1);

    for (te = slivedb->tree.first; te; te = te->next) {
        if (do_mat_livedb_operation_event(C, ar, slivedb, te, fmval)) {
            break;
        }
    }
    return OPERATOR_FINISHED;
} /* mat_livedb_operation() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* LiveDB operation. Menu only. Calls other operators. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_operation(wmOperatorType *ot)
{
    ot->name        = "Execute Operation";
    ot->idname      = "MAT_LIVEDB_OT_operation";
    ot->description = "Context menu for item operations";
    ot->invoke      = mat_livedb_operation;
    ot->poll        = ED_operator_mat_livedb_active;
} /* MAT_LIVEDB_OT_operation() */
