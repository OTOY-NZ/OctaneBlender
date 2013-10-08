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

/** \file blender/editors/space_mat_livedb/mat_livedb_select.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#ifndef WIN32
#include <sys/types.h>
#endif

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
/* LiveDB Selection (gray-blue highlight for rows) */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_select(SpaceLDB *slivedb, ListBase *lb, short *selecting, float *mval)
{
    LiveDbTreeElement   *te;
    int                 change = 0;

    for (te = lb->first; te; te = te->next) {
        int CUR_UNIT_Y;
        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            CUR_UNIT_Y = UI_UNIT_Y;
        else
            CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;

        if (mval[1] > te->ys && mval[1] < te->ys + CUR_UNIT_Y) {
            /* -1 value means toggle testing for now... */
            if (*selecting == -1) {
                if (*te->flag & TE_SELECTED)
                    *selecting = 0;
                else
                    *selecting = 1;
            }

            /* set selection */
            if (*selecting)
                *te->flag |= TE_SELECTED;
            else
                *te->flag &= ~TE_SELECTED;

            change |= 1;
            break;
        }
        else if (MAT_LIVEDB_ELEM_OPEN(te, slivedb)) {
            /* Only try selecting sub-elements if we haven't hit the right element yet */
            change |= mat_livedb_select(slivedb, &te->subtree, selecting, mval);
        }
    }
    return change;
} /* mat_livedb_select() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Activate item recursion */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int do_mat_livedb_item_activate(SpaceLDB *slivedb, LiveDbTreeElement *te, bool extend, const float mval[2])
{
    int CUR_UNIT_Y;
    if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
        CUR_UNIT_Y = UI_UNIT_Y;
    else
        CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;

    if (mval[1] > te->ys && mval[1] < te->ys + CUR_UNIT_Y) {
        int openclose = 0;

        /* open close icon */
        if (mval[0] > te->xs && mval[0] < te->xs + UI_UNIT_X)
            openclose = 1;

        if (openclose) {
            if (extend) {
                *te->flag &= ~TE_CLOSED;
                mat_livedb_set_flag(slivedb, &te->subtree, TE_CLOSED, !mat_livedb_has_one_flag(slivedb, &te->subtree, TE_CLOSED, 1));
            }
            else {
                if (*te->flag & TE_CLOSED) *te->flag &= ~TE_CLOSED;
                else *te->flag |= TE_CLOSED;
            }
            return 1;
        }
    }
    for (te = te->subtree.first; te; te = te->next) {
        if (do_mat_livedb_item_activate(slivedb, te, extend, mval)) return 1;
    }
    return 0;
} /* do_mat_livedb_item_activate() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Activate item */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int mat_livedb_item_do_activate(bContext *C, int x, int y, bool extend)
{
    ARegion             *ar         = CTX_wm_region(C);
    SpaceLDB            *slivedb    = CTX_wm_space_mat_livedb(C);
    LiveDbTreeElement   *te;
    float               fmval[2];

    UI_view2d_region_to_view(&ar->v2d, x, y, fmval, fmval + 1);

    for (te = slivedb->tree.first; te; te = te->next) {
        if (do_mat_livedb_item_activate(slivedb, te, extend, fmval)) break;
    }

    if (te) {
        ED_undo_push(C, "Materials LiveDB click event");
    }
    else {
        short selecting = -1;
        /* select relevant row */
        if (mat_livedb_select(slivedb, &slivedb->tree, &selecting, fmval)) {
            slivedb->storeflag |= LDB_TREESTORE_REDRAW;
        }
    }

    ED_region_tag_redraw(ar);

    return OPERATOR_FINISHED;
} /* mat_livedb_item_do_activate() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Event can enterkey, then it opens/closes */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_item_activate(bContext *C, wmOperator *op, const wmEvent *event)
{
    bool    extend  = RNA_boolean_get(op->ptr, "extend");
    int     x       = event->mval[0];
    int     y       = event->mval[1];

    return mat_livedb_item_do_activate(C, x, y, extend);
} /* mat_livedb_item_activate() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Activate item */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_item_activate(wmOperatorType *ot)
{
    ot->name        = "Activate Item";
    ot->idname      = "MAT_LIVEDB_OT_item_activate";
    ot->description = "Handle mouse clicks to activate/select items";
    ot->invoke      = mat_livedb_item_activate;
    ot->poll        = ED_operator_mat_livedb_active;

    RNA_def_boolean(ot->srna, "extend", true, "Extend", "Extend selection for activation");
} /* MAT_LIVEDB_OT_item_activate() */
