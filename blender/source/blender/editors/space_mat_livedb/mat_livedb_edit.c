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

/** \file blender/editors/space_mat_livedb/mat_livedb_edit.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#include "BLI_blenlib.h"

#include "BKE_context.h"
#include "BKE_report.h"

#include "ED_screen.h"

#include "WM_api.h"
#include "WM_types.h"

#include "UI_interface.h"
#include "UI_view2d.h"

#include "RNA_access.h"
#include "RNA_define.h"


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Open/close recursion */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int do_mat_livedb_item_openclose(bContext *C, SpaceLDB *slivedb, LiveDbTreeElement *te, int all, const float mval[2])
{
    int CUR_UNIT_Y;
    if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
        CUR_UNIT_Y = UI_UNIT_Y;
    else
        CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;

    if (mval[1] > te->ys && mval[1] < te->ys + CUR_UNIT_Y) {
        /* all below close/open? */
        if (all) {
            *te->flag &= ~TE_CLOSED;
            mat_livedb_set_flag(slivedb, &te->subtree, TE_CLOSED, !mat_livedb_has_one_flag(slivedb, &te->subtree, TE_CLOSED, 1));
        }
        else {
            if (*te->flag & TE_CLOSED) *te->flag &= ~TE_CLOSED;
            else *te->flag |= TE_CLOSED;
        }
        return 1;
    }
    for (te = te->subtree.first; te; te = te->next) {
        if (do_mat_livedb_item_openclose(C, slivedb, te, all, mval)) 
            return 1;
    }
    return 0;
} /* do_mat_livedb_item_openclose() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle open/closed */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_item_openclose(bContext *C, wmOperator *op, const wmEvent *event)
{
    ARegion             *ar         = CTX_wm_region(C);
    SpaceLDB            *slivedb    = CTX_wm_space_mat_livedb(C);
    int                 all         = RNA_boolean_get(op->ptr, "all");
    LiveDbTreeElement   *te;
    float               fmval[2];
    
    UI_view2d_region_to_view(&ar->v2d, event->mval[0], event->mval[1], fmval, fmval + 1);
    
    for (te = slivedb->tree.first; te; te = te->next) {
        if (do_mat_livedb_item_openclose(C, slivedb, te, all, fmval)) 
            break;
    }
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_item_openclose() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle open/closed */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_item_openclose(wmOperatorType *ot)
{
    ot->name        = "Open/Close Item";
    ot->idname      = "MAT_LIVEDB_OT_item_openclose";
    ot->description = "Toggle whether item under cursor is opened or closed";
    ot->invoke      = mat_livedb_item_openclose;
    ot->poll        = ED_operator_mat_livedb_active;
    
    RNA_def_boolean(ot->srna, "all", 1, "All", "Close or open all items");
} /* MAT_LIVEDB_OT_item_openclose() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Rename item */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void do_item_rename(ARegion *ar, LiveDbTreeElement *te, ReportList *reports)
{
    if (TE_GET_TYPE(te->item->type) != MAT_LDB_TREE_ITEM_TYPE_MATERIAL)
        BKE_report(reports, RPT_WARNING, "Can edit only the material names.");
    else {
        *te->flag |= TE_TEXTBUT;
        ED_region_tag_redraw(ar);
    }
} /* do_item_rename() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Rename item callback */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_item_rename_cb(bContext *C, LiveDbTreeElement *te)
{
    ARegion     *ar         = CTX_wm_region(C);
    ReportList  *reports    = CTX_wm_reports(C);

    if(*te->flag & TE_ACTIVE) {
        *te->flag &= ~TE_ACTIVE;
        do_item_rename(ar, te, reports);
    }
} /* mat_livedb_item_rename_cb() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Rename item recursion */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int do_mat_livedb_item_rename(bContext *C, ARegion *ar, SpaceLDB *slivedb, LiveDbTreeElement *te, const float mval[2])
{	
    ReportList  *reports;
    int         CUR_UNIT_Y;

    if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
        CUR_UNIT_Y = UI_UNIT_Y;
    else
        CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;

    reports = CTX_wm_reports(C);
    
    if (mval[1] > te->ys && mval[1] < te->ys + CUR_UNIT_Y) {
        /* click on name */
        if (mval[0] > te->xs + UI_UNIT_X * 2 && mval[0] < te->xend) {
            do_item_rename(ar, te, reports);
            return 1;
        }
        return 0;
    }
    for (te = te->subtree.first; te; te = te->next) {
        if (do_mat_livedb_item_rename(C, ar, slivedb, te, mval)) return 1;
    }
    return 0;
} /* do_mat_livedb_item_rename() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Rename item */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_item_rename(bContext *C, wmOperator *UNUSED(op), const wmEvent *event)
{
    ARegion             *ar         = CTX_wm_region(C);
    SpaceLDB            *slivedb    = CTX_wm_space_mat_livedb(C);
    bool                change      = false;
    LiveDbTreeElement   *te;
    float               fmval[2];
    
    UI_view2d_region_to_view(&ar->v2d, event->mval[0], event->mval[1], fmval, fmval + 1);
    
    for (te = slivedb->tree.first; te; te = te->next) {
        if (do_mat_livedb_item_rename(C, ar, slivedb, te, fmval)) {
            change = true;
            break;
        }
    }
    return change ? OPERATOR_FINISHED : OPERATOR_PASS_THROUGH;
} /* mat_livedb_item_rename() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Rename item */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_item_rename(wmOperatorType *ot)
{
    ot->name        = "Rename Item";
    ot->idname      = "MAT_LIVEDB_OT_item_rename";
    ot->description = "Rename item under cursor";
    ot->invoke      = mat_livedb_item_rename;
    ot->poll        = ED_operator_mat_livedb_active;
} /* MAT_LIVEDB_OT_item_rename() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Count number of levels in tree */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_count_levels(SpaceLDB *slivedb, ListBase *lb, int curlevel)
{
    LiveDbTreeElement   *te;
    int                 level = curlevel, lev;
    
    for (te = lb->first; te; te = te->next) {
        lev = mat_livedb_count_levels(slivedb, &te->subtree, curlevel + 1);
        if (lev > level) level = lev;
    }
    return level;
} /* mat_livedb_count_levels() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Find the level where at least one given flag is set */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int mat_livedb_has_one_flag(SpaceLDB *slivedb, ListBase *lb, short flag, short curlevel)
{
    LiveDbTreeElement   *te;
    int                 level;
    
    for (te = lb->first; te; te = te->next) {
        if (*te->flag & flag) return curlevel;
        
        level = mat_livedb_has_one_flag(slivedb, &te->subtree, flag, curlevel + 1);
        if (level) return level;
    }
    return 0;
} /* mat_livedb_has_one_flag() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Set flag to all items */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_set_flag(SpaceLDB *slivedb, ListBase *lb, short flag, short set)
{
    LiveDbTreeElement *te;
    
    for (te = lb->first; te; te = te->next) {
        if (set == 0) *te->flag &= ~flag;
        else *te->flag |= flag;
        mat_livedb_set_flag(slivedb, &te->subtree, flag, set);
    }
} /* mat_livedb_set_flag() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle Expanded */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_toggle_expanded_exec(bContext *C, wmOperator *UNUSED(op))
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    
    if (mat_livedb_has_one_flag(slivedb, &slivedb->tree, TE_CLOSED, 1))
        mat_livedb_set_flag(slivedb, &slivedb->tree, TE_CLOSED, 0);
    else 
        mat_livedb_set_flag(slivedb, &slivedb->tree, TE_CLOSED, 1);
    
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_toggle_expanded_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle Expanded */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_expanded_toggle(wmOperatorType *ot)
{
    ot->name        = "Expand/Collapse All";
    ot->idname      = "MAT_LIVEDB_OT_expanded_toggle";
    ot->description = "Expand/Collapse all items";
    ot->exec        = mat_livedb_toggle_expanded_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    
    /* no undo or registry, UI option */
} /* MAT_LIVEDB_OT_expanded_toggle() */

/* Toggle Selected (LiveDB) ---------------------------------------- */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle Selected */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_toggle_selected_exec(bContext *C, wmOperator *UNUSED(op))
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    Scene       *scene      = CTX_data_scene(C);
    
    if (mat_livedb_has_one_flag(slivedb, &slivedb->tree, TE_SELECTED, 1))
        mat_livedb_set_flag(slivedb, &slivedb->tree, TE_SELECTED, 0);
    else 
        mat_livedb_set_flag(slivedb, &slivedb->tree, TE_SELECTED, 1);
    
    slivedb->storeflag |= LDB_TREESTORE_REDRAW;
    
    WM_event_add_notifier(C, NC_SCENE | ND_OB_SELECT, scene);
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_toggle_selected_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Toggle Selected */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_selected_toggle(wmOperatorType *ot)
{
    ot->name        = "Toggle Selected";
    ot->idname      = "MAT_LIVEDB_OT_selected_toggle";
    ot->description = "Toggle the Materials LiveDB selection of items";
    ot->exec        = mat_livedb_toggle_selected_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    
    /* no undo or registry, UI option */
} /* MAT_LIVEDB_OT_selected_toggle() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Scroll page up */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_scroll_page_up_exec(bContext *C, wmOperator *op)
{
    ARegion *ar = CTX_wm_region(C);
    int     dy  = BLI_rcti_size_y(&ar->v2d.mask);

    ar->v2d.cur.ymin += dy;
    ar->v2d.cur.ymax += dy;
    
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_scroll_page_up_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Scroll page up */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_scroll_page_up(wmOperatorType *ot)
{
    ot->name        = "Scroll Page Up";
    ot->idname      = "MAT_LIVEDB_OT_scroll_page_up";
    ot->description = "Scroll page up";
    ot->exec        = mat_livedb_scroll_page_up_exec;
    ot->poll        = ED_operator_mat_livedb_active;
} /* MAT_LIVEDB_OT_scroll_page_up() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Scroll page down */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_scroll_page_down_exec(bContext *C, wmOperator *op)
{
    ARegion *ar = CTX_wm_region(C);
    int     dy  = -BLI_rcti_size_y(&ar->v2d.mask);

    ar->v2d.cur.ymin += dy;
    ar->v2d.cur.ymax += dy;
    
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_scroll_page_down_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Scroll page down */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_scroll_page_down(wmOperatorType *ot)
{
    ot->name        = "Scroll Page Down";
    ot->idname      = "MAT_LIVEDB_OT_scroll_page_down";
    ot->description = "Scroll page down";
    ot->exec        = mat_livedb_scroll_page_down_exec;
    ot->poll        = ED_operator_mat_livedb_active;
} /* MAT_LIVEDB_OT_scroll_page_down() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Helper function for Show/Hide one level operator */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_openclose_level(SpaceLDB *slivedb, ListBase *lb, int curlevel, int level, int open)
{
    LiveDbTreeElement *te;
    
    for (te = lb->first; te; te = te->next) {
        if (open) {
            if (curlevel <= level) *te->flag &= ~TE_CLOSED;
        }
        else {
            if (curlevel >= level) *te->flag |= TE_CLOSED;
        }
        mat_livedb_openclose_level(slivedb, &te->subtree, curlevel + 1, level, open);
    }
} /* mat_livedb_openclose_level() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Show one level */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_show_one_level_exec(bContext *C, wmOperator *op)
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    int         level       = mat_livedb_has_one_flag(slivedb, &slivedb->tree, TE_CLOSED, 1);

    if (level) mat_livedb_openclose_level(slivedb, &slivedb->tree, 1, level, 1);
    
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_show_one_level_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Show one level */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_show_one_level(wmOperatorType *ot)
{
    ot->name        = "Show One Level";
    ot->idname      = "MAT_LIVEDB_OT_show_one_level";
    ot->description = "Expand all entries by one level";
    ot->exec        = mat_livedb_show_one_level_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    
    /* no undo or registry, UI option */
} /* MAT_LIVEDB_OT_show_one_level() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Hide one level */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_hide_one_level_exec(bContext *C, wmOperator *op)
{
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    ARegion     *ar         = CTX_wm_region(C);
    int         level       = mat_livedb_has_one_flag(slivedb, &slivedb->tree, TE_CLOSED, 1);

    if (level == 0) level = mat_livedb_count_levels(slivedb, &slivedb->tree, 0);
    if (level) mat_livedb_openclose_level(slivedb, &slivedb->tree, 1, level - 1, 0);
    
    ED_region_tag_redraw(ar);
    
    return OPERATOR_FINISHED;
} /* mat_livedb_hide_one_level_exec() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Hide one level */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_hide_one_level(wmOperatorType *ot)
{
    ot->name        = "Hide One Level";
    ot->idname      = "MAT_LIVEDB_OT_hide_one_level";
    ot->description = "Collapse all entries by one level";
    ot->exec        = mat_livedb_hide_one_level_exec;
    ot->poll        = ED_operator_mat_livedb_active;
    
    /* no undo or registry, UI option */
} /* MAT_LIVEDB_OT_hide_one_level() */
