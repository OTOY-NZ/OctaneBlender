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
#  include <sys/types.h>
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

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* LiveDB Selection (gray-blue highlight for rows) */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static int mat_livedb_select(SpaceLDB *slivedb, ListBase *lb, short *selecting, float *mval)
{
  LiveDbTreeElement *te;
  int change = 0;

  for (te = lb->first; te; te = te->next) {
    int CUR_UNIT_Y;
    if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
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
