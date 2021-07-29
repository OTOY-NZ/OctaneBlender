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

/** \file blender/editors/space_mat_livedb/mat_livedb_draw.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#ifndef WIN32
#  include <dirent.h>
#  define GetCurrentDir _getcwd
#else
#  include "utf_winfunc.h"
#  define GetCurrentDir getcwd
#endif

#include <string.h>

#include "MEM_guardedalloc.h"

#include "BLI_path_util.h"
#include "BLI_fileops.h"
#ifdef WIN32
#  include "BLI_winstuff.h"
#endif

#include "DNA_object_types.h"
#include "DNA_mesh_types.h"

#include "BKE_context.h"
#include "BKE_main.h"
#include "BKE_node.h"
#include "BKE_material.h"
#include "BKE_scene.h"
#include "BKE_appdir.h"

#include "ED_screen.h"

#include "BIF_gl.h"
#include "BIF_glutil.h"

#include "BLT_translation.h"

#include "UI_interface.h"
#include "UI_interface_icons.h"
#include "UI_resources.h"
#include "UI_view2d.h"

#include "WM_api.h"
#include "WM_types.h"

#include "../../source/blender/nodes/NOD_shader.h"

static char new_name[256] = {0};

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Tree hight */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void mat_livedb_height(SpaceLDB *slivedb, ListBase *lb, int *h)
{
  LiveDbTreeElement *te = lb->first;
  while (te) {
    if (MAT_LIVEDB_ELEM_OPEN(te, slivedb))
      mat_livedb_height(slivedb, &te->subtree, h);
    if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
      *h += UI_UNIT_Y;
    else
      *h += MAT_LIVEDB_UI_UNIT_Y;
    te = te->next;
  }
} /* mat_livedb_height() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Tree width */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void mat_livedb_width(SpaceLDB *slivedb, ListBase *lb, int *w, short startx)
{
  LiveDbTreeElement *te = lb->first;
  while (te) {
    if (!MAT_LIVEDB_ELEM_OPEN(te, slivedb)) {
      short offsx = te->xend = startx + UI_UNIT_X * 3 +
                               UI_fontstyle_string_width(UI_FSTYLE_WIDGET, te->name);
      if (offsx > *w)
        *w = offsx;
    }
    mat_livedb_width(slivedb, &te->subtree, w, startx + UI_UNIT_X);
    te = te->next;
  }
} /* mat_livedb_width() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Get material callback */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void get_material_cb(bContext *C, void *poin, void *poin2)
{
  Scene *scene = CTX_data_scene(C);
  Main *bmain = CTX_data_main(C);
  bool not_set = true;
  Object *cur_object;
  Object *ob;
  Material *ma;

  cur_object = scene->basact ? scene->basact->object : 0;
  if (cur_object->actcol > 0) {
    ob = (Object *)cur_object;
    if (cur_object->totcol >= cur_object->actcol && ob->mat[cur_object->actcol - 1]) {
      bNodeTree *ntree = ob->mat[cur_object->actcol - 1]->nodetree;
      if (!ob->mat[cur_object->actcol - 1]->use_nodes)
        ob->mat[cur_object->actcol - 1]->use_nodes = true;
      if (ntree) {
        get_material(bmain, C, scene, ntree, (char *)poin, (int)poin2);
        not_set = false;
      }
    }
    if (not_set) {
      ID *id_me = cur_object->data;
      if (GS(id_me->name) == ID_ME) {
        Mesh *me = (Mesh *)id_me;
        if (me->totcol >= cur_object->actcol && me->mat[cur_object->actcol - 1]) {
          bNodeTree *ntree = me->mat[cur_object->actcol - 1]->nodetree;
          if (!me->mat[cur_object->actcol - 1]->use_nodes)
            me->mat[cur_object->actcol - 1]->use_nodes = true;
          if (ntree) {
            get_material(bmain, C, scene, ntree, (char *)poin, (int)poin2);
            not_set = false;
          }
        }
      }
    }
  }
  if (not_set) {
    ob = (Object *)cur_object;
    ma = BKE_material_add(bmain, DATA_("LDB Material"));

    ma->use_nodes = true;
    ma->nodetree = ntreeAddTree(NULL, "Shader Nodetree", ntreeType_Shader->idname);
    assign_material(bmain, ob, ma, ob->totcol + 1, BKE_MAT_ASSIGN_USERPREF);
    WM_event_add_notifier(C, NC_MATERIAL | NA_ADDED, ma);

    get_material(bmain, C, scene, ma->nodetree, (char *)poin, (int)poin2);
  }
} /* get_material_cb() */

#ifndef WIN32
#  pragma suppress(all_checks)
#else
#  pragma runtime_checks("s", off)
#endif
