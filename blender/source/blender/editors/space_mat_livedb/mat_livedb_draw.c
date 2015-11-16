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
#   include "BLI_winstuff.h"
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

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Tree hight */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_height(SpaceLDB *slivedb, ListBase *lb, int *h)
{
    LiveDbTreeElement *te = lb->first;
    while (te) {
        if (MAT_LIVEDB_ELEM_OPEN(te, slivedb))
            mat_livedb_height(slivedb, &te->subtree, h);
        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            *h += UI_UNIT_Y;
        else
            *h += MAT_LIVEDB_UI_UNIT_Y;
        te = te->next;
    }
} /* mat_livedb_height() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Tree width */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_width(SpaceLDB *slivedb, ListBase *lb, int *w, short startx)
{
    LiveDbTreeElement *te = lb->first;
    while (te) {
        if (!MAT_LIVEDB_ELEM_OPEN(te, slivedb)) {
            short offsx = te->xend = startx + UI_UNIT_X * 3 + UI_fontstyle_string_width(UI_FSTYLE_WIDGET, te->name);
            if (offsx > *w)
                *w = offsx;
        }
        mat_livedb_width(slivedb, &te->subtree, w, startx + UI_UNIT_X);
        te = te->next;
    }
} /* mat_livedb_width() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get material callback */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void get_material_cb(bContext *C, void *poin, void *poin2)
{
    Scene       *scene  = CTX_data_scene(C);
    Main        *bmain  = CTX_data_main(C);
    bool        not_set = true;
    Object      *cur_object;
    Object      *ob;
    Material    *ma;

    cur_object = scene->basact ? scene->basact->object : 0;
    if(cur_object->actcol > 0) {
        ob = (Object*)cur_object;
        if(cur_object->totcol >= cur_object->actcol && ob->mat[cur_object->actcol - 1]) {
            bNodeTree *ntree = ob->mat[cur_object->actcol - 1]->nodetree;
            if(!ob->mat[cur_object->actcol - 1]->use_nodes) ob->mat[cur_object->actcol - 1]->use_nodes = true;
            if (ntree) {
                get_material(bmain, C, scene, ntree, (char*)poin, (int)poin2);
                not_set = false;
            }
        }
        if(not_set) {
            ID *id_me = cur_object->data;
            if (GS(id_me->name) == ID_ME) {
                Mesh *me = (Mesh*)id_me;
                if(me->totcol >= cur_object->actcol && me->mat[cur_object->actcol - 1]) {
                    bNodeTree *ntree = me->mat[cur_object->actcol - 1]->nodetree;
                    if(!me->mat[cur_object->actcol - 1]->use_nodes) me->mat[cur_object->actcol - 1]->use_nodes = true;
                    if (ntree) {
                        get_material(bmain, C, scene, ntree, (char*)poin, (int)poin2);
                        not_set = false;
                    }
                }
            }
        }
    }
    if(not_set) {
        ob = (Object*)cur_object;
        ma = BKE_material_add(bmain, DATA_("LDB Material"));

        ma->use_nodes = true;
        ma->nodetree  = ntreeAddTree(NULL, "Shader Nodetree", ntreeType_Shader->idname);
        assign_material(ob, ma, ob->totcol + 1, BKE_MAT_ASSIGN_USERPREF);
        WM_event_add_notifier(C, NC_MATERIAL | NA_ADDED, ma);

        get_material(bmain, C, scene, ma->nodetree, (char*)poin, (int)poin2);
    }
} /* get_material_cb() */

#ifndef WIN32
#   pragma suppress(all_checks)
#else
#   pragma runtime_checks("s", off)
#endif
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Name button callback */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_namebutton_cb(bContext *C, void *itemp, char *oldname)
{
    Main        *mainvar    = CTX_data_main(C);
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    LiveDbItem  *item       = itemp;

    if (item) {
        if (TE_GET_TYPE(item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY) {
            /* TODO: implement for categories */
        }
        else {
            LiveDbItem  *cur_item;
            size_t      store_len = MEM_allocN_len(slivedb->treestore);
            int         size_diff = strlen(new_name) - strlen(oldname);

            LiveDbItem *new_items = MEM_mallocN(store_len + size_diff, "ldb tree");
            LiveDbItem *new_item  = new_items;

            for(cur_item = (LiveDbItem*)slivedb->treestore; (((char*)cur_item + cur_item->size) - slivedb->treestore) <= store_len; cur_item = (LiveDbItem*)((char*)cur_item + cur_item->size)) {
                if(TE_GET_TYPE(cur_item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY) {
                    memcpy(new_item, cur_item, cur_item->size);
                }
                else {
                    if(cur_item == item) {
                        char *cur_name, *cur_new_name;

                        new_item->size          = cur_item->size + size_diff;
                        new_item->type          = cur_item->type;
                        new_item->mat_item.id   = cur_item->mat_item.id;

                        strcpy(new_item->mat_item.name, new_name);
                        cur_name        = cur_item->mat_item.name + strlen(cur_item->mat_item.name) + 1;
                        cur_new_name    = new_item->mat_item.name + strlen(new_name) + 1;
                        strcpy(cur_new_name, cur_name);
                        cur_new_name    = cur_new_name + strlen(cur_name) + 1;
                        cur_name        = cur_name + strlen(cur_name) + 1;
                        strcpy(cur_new_name, cur_name);
                    }
                    else memcpy(new_item, cur_item, cur_item->size);
                }
                new_item = (LiveDbItem*)((char*)new_item + new_item->size);
            }
            new_name[0] = 0;
            MEM_freeN(slivedb->treestore);
            slivedb->treestore = (char*)new_items;

            mat_livedb_build_tree(mainvar, slivedb, 0);
        }
    }
} /* mat_livedb_namebutton_cb() */
#ifndef WIN32
#   pragma unsuppress(all_checks)
#else
#   pragma runtime_checks("s", restore)
#endif

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw material preview */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_draw_mat_preview(uiBlock *block, Scene *scene, ARegion *ar, SpaceLDB *slivedb, ListBase *lb)
{
    LiveDbTreeElement   *te;
    char                *file_path = (char*)BKE_appdir_folder_id_create(BLENDER_USER_DATAFILES, 0);

    strcat(file_path, "/livedb/");
    strcat(file_path, slivedb->server_address);
    strcat(file_path, "/previews/");
    BLI_dir_create_recursive(file_path);

    for (te = lb->first; te; te = te->next) {
        if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_MATERIAL && te->ys + 2 * MAT_LIVEDB_UI_UNIT_Y >= ar->v2d.cur.ymin && te->ys <= ar->v2d.cur.ymax) {
            unsigned int width, height;
            char* buf = mat_livedb_get_mat_preview(slivedb->server_address, te->item->mat_item.id, &width, &height, file_path);

            if(buf) {
                if(width && height) {
                    glEnable(GL_BLEND);
                    glColor4f(0.0, 0.0, 0.0, 0.0);

                    if (width != UI_UNIT_X || height != (MAT_LIVEDB_UI_UNIT_Y - 2)) {
                        float facx = (float)(MAT_LIVEDB_UI_UNIT_Y - 2) / (float)width;
                        float facy =  (float)(MAT_LIVEDB_UI_UNIT_Y - 2) / (float)height;
                        glPixelZoom(facx, facy);
                    }
                    glaDrawPixelsAuto((float)(ar->v2d.cur.xmax - MAT_LIVEDB_UI_UNIT_Y - 1),
                                      (float)te->ys + 1, width, height, GL_RGBA, GL_UNSIGNED_BYTE, GL_NEAREST, buf);

                    glPixelZoom(1.0f, 1.0f);
                    glDisable(GL_BLEND);
                }
                MEM_freeN(buf);
            }
        }
        else if (MAT_LIVEDB_ELEM_OPEN(te, slivedb)) mat_livedb_draw_mat_preview(block, scene, ar, slivedb, &te->subtree);
    }
} /* mat_livedb_draw_mat_preview() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw rename buttons */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_draw_rename_buttons(const bContext *C, uiBlock *block, ARegion *ar, SpaceLDB *slivedb, ListBase *lb)
{
    LiveDbTreeElement *te;
    int spx, dx, CUR_UNIT_Y;

    for (te = lb->first; te; te = te->next) {
        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            CUR_UNIT_Y = UI_UNIT_Y;
        else
            CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;
        if (te->ys + 2 * CUR_UNIT_Y >= ar->v2d.cur.ymin && te->ys <= ar->v2d.cur.ymax) {
            if (*te->flag & TE_TEXTBUT) {
                uiBut *bt;
                if(new_name[0] == 0) strcpy(new_name, te->name);

                dx = (int)UI_fontstyle_string_width(UI_FSTYLE_WIDGET, te->name);
                if (dx < 5 * UI_UNIT_X) dx = 5 * UI_UNIT_X;
                spx = te->xs + 1.8f * UI_UNIT_X;
                if (spx + dx + 0.5f * UI_UNIT_X > ar->v2d.cur.xmax) dx = ar->v2d.cur.xmax - spx - 0.5f * UI_UNIT_X;

                bt = uiDefBut(block, UI_BTYPE_TEXT, LDB_NAMEBUTTON, "", spx, (int)te->ys + UI_UNIT_Y * 3, dx + UI_UNIT_X, UI_UNIT_Y - 1, (void *)new_name, 1.0, 255.0f, 0, 0, "");
                UI_but_func_rename_set(bt, mat_livedb_namebutton_cb, te->item);

                /* returns false if button got removed */
                if (!UI_but_active_only(C, ar, block, bt)) {
                    *te->flag &= ~TE_TEXTBUT;
                    new_name[0] = 0;
                }
            }
        }
        if (MAT_LIVEDB_ELEM_OPEN(te, slivedb)) mat_draw_rename_buttons(C, block, ar, slivedb, &te->subtree);
    }
} /* mat_draw_rename_buttons() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw element icon */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_elem_draw_icon(float x, float y, LiveDbTreeElement *te)
{
    switch (TE_GET_TYPE(te->item->type)) {
        case MAT_LDB_TREE_ITEM_TYPE_CATEGORY:
            UI_icon_draw(x, y, ICON_FILE_FOLDER); break;
        case MAT_LDB_TREE_ITEM_TYPE_MATERIAL:
            UI_icon_draw(x, y, ICON_MATERIAL_DATA); break;
        default:
            UI_icon_draw(x, y, ICON_DOT); break;
    }
} /* mat_livedb_elem_draw_icon() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw content-info icons */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_draw_content_count_icons(ListBase *lb, int xmax, int *offsx, int ys)
{
    int cat_cnt = 0, mat_cnt = 0, string_width;
    LiveDbTreeElement   *te;
    char                cnt_str[16];
    float               ufac = UI_UNIT_X / 20.0f;

    if ((*offsx) - UI_UNIT_X > xmax) return;

    for (te = lb->first; te; te = te->next) {
        if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY) ++cat_cnt;
        else ++mat_cnt;
    }
    if (cat_cnt > 0) {
        snprintf(cnt_str, 16, "%d", cat_cnt);
        string_width = UI_fontstyle_string_width(UI_FSTYLE_WIDGET, cnt_str);

        UI_draw_roundbox_corner_set(UI_CNR_ALL);
        glColor4ub(220, 220, 255, 100);
        UI_draw_roundbox((float) *offsx - 4.0f * ufac,
                   (float)ys + 1.0f * ufac,
                   (float)*offsx + UI_UNIT_X + string_width,
                   (float)ys + UI_UNIT_Y - ufac,
                   (float)UI_UNIT_Y / 2.0f - ufac);
        glEnable(GL_BLEND); /* roundbox disables */

        UI_icon_draw((float)*offsx, (float)ys + 2 * ufac, ICON_FILE_FOLDER);

        (*offsx) += UI_UNIT_X;
        UI_ThemeColor(TH_TEXT);
        UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, (float)*offsx - 2 * ufac, (float)ys + 5 * ufac, cnt_str);

        offsx += (int)(UI_UNIT_X + string_width);
    }
    if (mat_cnt > 0) {
        snprintf(cnt_str, 16, "%d", mat_cnt);
        string_width = UI_fontstyle_string_width(UI_FSTYLE_WIDGET, cnt_str);

        UI_draw_roundbox_corner_set(UI_CNR_ALL);
        glColor4ub(220, 220, 255, 100);
        UI_draw_roundbox((float) *offsx - 4.0f * ufac,
                   (float)ys + 1.0f * ufac,
                   (float)*offsx + UI_UNIT_X + string_width,
                   (float)ys + UI_UNIT_Y - ufac,
                   (float)UI_UNIT_Y / 2.0f - ufac);
        glEnable(GL_BLEND); /* roundbox disables */

        UI_icon_draw((float)*offsx, (float)ys + 2 * ufac, ICON_MATERIAL);

        (*offsx) += UI_UNIT_X;
        UI_ThemeColor(TH_TEXT);
        UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, (float)*offsx - 2 * ufac, (float)ys + 5 * ufac, cnt_str);

        offsx += (int)(UI_UNIT_X + string_width);
    }
} /* mat_livedb_draw_content_count_icons() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Set coordinates of tree elements */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_set_coord_tree_element(SpaceLDB *slivedb, LiveDbTreeElement *te, int startx, int *starty)
{
    LiveDbTreeElement *ten;

    /* store coord and continue, we need coordinates for elements outside view too */
    te->xs = (float)startx;
    te->ys = (float)(*starty);

    for (ten = te->subtree.first; ten; ten = ten->next) {
        mat_livedb_set_coord_tree_element(slivedb, ten, startx + UI_UNIT_X, starty);
    }
} /* mat_livedb_set_coord_tree_element() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw tree element */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_draw_tree_element(bContext *C, uiBlock *block, ARegion *ar, SpaceLDB *slivedb, LiveDbTreeElement *te, int startx, int *starty, int *row_num)
{
    LiveDbTreeElement   *ten;
    float               ufac = UI_UNIT_X / 20.0f;
    int                 offsx = 0, active = 0;
    int                 CUR_UNIT_Y;

    if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
        CUR_UNIT_Y = UI_UNIT_Y;
    else
        CUR_UNIT_Y = MAT_LIVEDB_UI_UNIT_Y;

    *starty -= CUR_UNIT_Y;
    ++ *row_num;

    if (*starty + 2 * CUR_UNIT_Y >= ar->v2d.cur.ymin && *starty <= ar->v2d.cur.ymax) {
        int xmax = ar->v2d.cur.xmax;
        unsigned char alpha = 128;

        /* icons can be ui buts, we don't want it to overlap with material previews */
        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_MATERIAL)
            xmax -= MAT_LIVEDB_UI_UNIT_Y;

        glEnable(GL_BLEND);

        if(*row_num % 2) {
            UI_ThemeColorShade(TH_BACK, 6);
            glRecti(0, *starty + 1, ar->v2d.cur.xmax, *starty + CUR_UNIT_Y - 1);
        }

        if (*te->flag & TE_SELECTED) {
            float           col[4];
            unsigned char   col_circle[4];

            UI_GetThemeColor3fv(TH_SELECT_HIGHLIGHT, col);
            glColor3fv(col);
            glRecti(0, *starty + 1, (int)ar->v2d.cur.xmax, *starty + CUR_UNIT_Y - 1);

            /* active circle */
            UI_GetThemeColorType4ubv(TH_ACTIVE, SPACE_VIEW3D, col_circle);
            col_circle[3] = alpha;
            glColor4ubv((GLubyte *)col_circle);

            UI_draw_roundbox_corner_set(UI_CNR_ALL);
            UI_draw_roundbox((float)startx + UI_UNIT_X - ufac,
                       (float)*starty + (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY ? 1.0f : UI_UNIT_Y * 3),
                       (float)startx + 2.0f * UI_UNIT_X - 2.0f * ufac,
                       (float)*starty + CUR_UNIT_Y - 1.0f * ufac,
                       UI_UNIT_Y / 2.0f - 1.0f * ufac);
            glEnable(GL_BLEND); /* roundbox disables it */
        }

        /* start by highlighting search matches */
        if (SEARCHING_MAT_LIVEDB(slivedb) && (*te->flag & TE_SEARCHMATCH))
        {
            char col[4];
            UI_GetThemeColorType4ubv(TH_MATCH, SPACE_MAT_LIVEDB, col);
            col[3] = alpha;
            glColor4ubv((GLubyte *)col);
            glRecti(startx, *starty + 1, ar->v2d.cur.xmax, *starty + CUR_UNIT_Y - 1);
        }

        /* open/close icon, only when sublevels */
        if (te->subtree.first || (*te->flag & TE_LAZY_CLOSED)) {
            int icon_x;
            if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
                icon_x = startx;
            else
                icon_x = startx + 5 * ufac;

            if (MAT_LIVEDB_ELEM_OPEN(te, slivedb))
                UI_icon_draw((float)icon_x, (float)*starty + 2 * ufac, ICON_DISCLOSURE_TRI_DOWN);
            else
                UI_icon_draw((float)icon_x, (float)*starty + 2 * ufac, ICON_DISCLOSURE_TRI_RIGHT);
        }
        offsx += UI_UNIT_X;

        /* Element type icon */
        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            mat_livedb_elem_draw_icon((float)startx + offsx, (float)*starty, te);
        else
            mat_livedb_elem_draw_icon((float)startx + offsx, (float)*starty + UI_UNIT_X * 3, te);

        offsx += UI_UNIT_X;

        glDisable(GL_BLEND);

        /* name */
        if (active == 1) UI_ThemeColor(TH_TEXT_HI);
        else UI_ThemeColor(TH_TEXT);

        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, startx + offsx, *starty + 5 * ufac, te->name);
        else {
            uiBut *bt;

            UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, startx + offsx, *starty + UI_UNIT_X * 3 + 5 * ufac, te->name);
            UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, startx + offsx, *starty + UI_UNIT_X * 2 + 5 * ufac, te->nick_name);
            UI_fontstyle_draw_simple(UI_FSTYLE_WIDGET, startx + offsx, *starty + UI_UNIT_X + 5 * ufac, te->copyright);

            bt = uiDefIconBut(block, UI_BTYPE_ICON_TOGGLE, 0, ICON_WORLD,
                                xmax - UI_UNIT_X - 3, *starty + 1 * ufac, UI_UNIT_X, UI_UNIT_Y,
                                NULL, 0.0, 0.0, 1.0, 0.5f, "Get item");
            UI_but_func_set(bt, get_material_cb, (void*)slivedb->server_address, (void*)te->item->mat_item.id);
            UI_but_flag_enable(bt, UI_BUT_DRAG_LOCK);
        }

        offsx += (int)(UI_UNIT_X + UI_fontstyle_string_width(UI_FSTYLE_WIDGET, te->name));

        /* Closed item, we draw the category-info icons */
        if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY && !MAT_LIVEDB_ELEM_OPEN(te, slivedb)) {
            if (te->subtree.first) {
                int tempx = startx + offsx;

                /* divider */
                UI_ThemeColorShade(TH_BACK, -40);
                glRecti(tempx   - 10.0f * ufac,
                        *starty +  4.0f * ufac,
                        tempx   -  8.0f * ufac,
                        *starty + CUR_UNIT_Y - 4.0f * ufac);

                glEnable(GL_BLEND);
                glPixelTransferf(GL_ALPHA_SCALE, 0.5);

                mat_livedb_draw_content_count_icons(&te->subtree, xmax, &tempx, *starty);

                glPixelTransferf(GL_ALPHA_SCALE, 1.0);
                glDisable(GL_BLEND);
            }
        }
    }
    /* store coord and continue, we need coordinates for elements outside view too */
    te->xs   = (float)startx;
    te->ys   = (float)*starty;
    te->xend = startx + offsx;

    if (MAT_LIVEDB_ELEM_OPEN(te, slivedb)) {
        for (ten = te->subtree.first; ten; ten = ten->next)
            mat_livedb_draw_tree_element(C, block, ar, slivedb, ten, startx + UI_UNIT_X, starty, row_num);
    }
    else {
        for (ten = te->subtree.first; ten; ten = ten->next)
            mat_livedb_set_coord_tree_element(slivedb, te, startx, starty);
    }
} /* mat_livedb_draw_tree_element() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw hierarchy lines */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_draw_hierarchy(SpaceLDB *slivedb, ListBase *lb, int startx, int *starty)
{
    LiveDbTreeElement *te;
    int y1, y2;

    if (lb->first == NULL) return;

    y1 = y2 = *starty; /* for vertical lines between objects */
    if(startx == 14) y1 -= UI_UNIT_Y / 2;
    for (te = lb->first; te; te = te->next) {
        y2 = *starty;

        /* horizontal line */
        if (TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            glRecti(startx, *starty, startx + UI_UNIT_X / 3, *starty - 1);
        else
            glRecti(startx, *starty, startx + UI_UNIT_X / 3, *starty - 1);

        if(TE_GET_TYPE(te->item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY)
            *starty -= UI_UNIT_Y;
        else
            *starty -= MAT_LIVEDB_UI_UNIT_Y;

        if (MAT_LIVEDB_ELEM_OPEN(te, slivedb))
            mat_livedb_draw_hierarchy(slivedb, &te->subtree, startx + UI_UNIT_X, starty);
    }

    /* vertical line */
    te = lb->last;
    if (te->parent || lb->first != lb->last)
        glRecti(startx, y1 + UI_UNIT_Y / 2, startx + 1, y2);
} /* mat_livedb_draw_hierarchy() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Draw tree */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_draw_tree(bContext *C, uiBlock *block, ARegion *ar, SpaceLDB *slivedb)
{
    LiveDbTreeElement   *te;
    int                 starty, startx;
    int                 i = 0;

    glBlendFunc(GL_SRC_ALPHA,  GL_ONE_MINUS_SRC_ALPHA); /* only once */

    /* items themselves */
    starty = (int)ar->v2d.tot.ymax - LDB_Y_OFFSET;
    startx = 0;
    for (te = slivedb->tree.first; te; te = te->next) {
        mat_livedb_draw_tree_element(C, block, ar, slivedb, te, startx, &starty, &i);
    }

    /* gray hierarchy lines */
    UI_ThemeColorBlend(TH_BACK, TH_TEXT, 0.4f);
    starty = (int)ar->v2d.tot.ymax - UI_UNIT_Y / 2 - LDB_Y_OFFSET;
    startx = 14;
    mat_livedb_draw_hierarchy(slivedb, &slivedb->tree, startx, &starty);
} /* mat_livedb_draw_tree() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Main Entrypoint - Draw contents of LiveDB editor */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void draw_mat_livedb(const bContext *C)
{
    uiBlock     *block;
    Main        *mainvar    = CTX_data_main(C);
    Scene       *scene      = CTX_data_scene(C);
    ARegion     *ar         = CTX_wm_region(C);
    View2D      *v2d        = &ar->v2d;
    SpaceLDB    *slivedb    = CTX_wm_space_mat_livedb(C);
    int sizey = 0, sizex = 0, sizex_rna = 0;

    if(!slivedb) return;

    if(!strlen(slivedb->server_address)) strcpy(slivedb->server_address, "127.0.0.1");

    mat_livedb_build_tree(mainvar, slivedb, 0); /* always */

    /* get extents of data */
    mat_livedb_height(slivedb, &slivedb->tree, &sizey);
    mat_livedb_width(slivedb, &slivedb->tree, &sizex, 0);

    /* adds vertical offset */
    sizey += LDB_Y_OFFSET;

    /* update size of tot-rect (extents of data/viewable area) */
    UI_view2d_totRect_set(v2d, sizex, sizey);

    /* force display to pixel coords */
    v2d->flag |= (V2D_PIXELOFS_X | V2D_PIXELOFS_Y);
    /* set matrix for 2d-view controls */
    UI_view2d_view_ortho(v2d);

    /* draw LiveDB stuff */
    block = UI_block_begin(C, ar, __func__, UI_EMBOSS);
    mat_livedb_draw_tree((bContext *)C, block, ar, slivedb);
    mat_livedb_draw_mat_preview(block, scene, ar, slivedb, &slivedb->tree);

    /* draw edit buttons if nessecery */
    mat_draw_rename_buttons(C, block, ar, slivedb, &slivedb->tree);

    UI_block_end(C, block);
    UI_block_draw(C, block);

    /* clear flag that allows quick redraws */
    slivedb->storeflag &= ~LDB_TREESTORE_REDRAW;
} /* draw_mat_livedb() */
