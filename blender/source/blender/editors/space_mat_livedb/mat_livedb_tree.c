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

/** \file blender/editors/space_mat_livedb/mat_livedb_tree.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#include <string.h>

#if defined WIN32 && !defined _LIBC  || defined __sun
# include "BLI_fnmatch.h" /* use fnmatch included in blenlib */
#else
#  ifndef _GNU_SOURCE
#    define _GNU_SOURCE
#  endif
# include <fnmatch.h>
#endif

#include "MEM_guardedalloc.h"
#include "BLI_blenlib.h"
#include "BLF_translation.h"
#include "BKE_main.h"
#include "ED_screen.h"


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Cleanup tree storage */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_storage_cleanup(SpaceLDB *slivedb)
{
    if (slivedb->treestore) {
        MEM_freeN(slivedb->treestore);
        slivedb->treestore = 0;
    }
} /* mat_livedb_storage_cleanup() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Free tree memory */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_free_tree(ListBase *lb)
{
    while (lb->first) {
        LiveDbTreeElement *te = lb->first;

        mat_livedb_free_tree(&te->subtree);
        BLI_remlink(lb, te);
        MEM_freeN(te);
    }
} /* mat_livedb_free_tree() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Cleanup the tree and storage memory */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_cleanup_tree(SpaceLDB *slivedb)
{
    mat_livedb_free_tree(&slivedb->tree);
    mat_livedb_storage_cleanup(slivedb);
} /* mat_livedb_cleanup_tree() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Search name */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_filter_has_name(LiveDbTreeElement *te, const char *name, int flags)
{
#if 0
    int found = 0;

    /* determine if match */
    if (flags & SO_FIND_CASE_SENSITIVE) {
        if (flags & SO_FIND_COMPLETE)
            found = strcmp(te->name, name) == 0;
        else
            found = strstr(te->name, name) != NULL;
    }
    else {
        if (flags & SO_FIND_COMPLETE)
            found = BLI_strcasecmp(te->name, name) == 0;
        else
            found = BLI_strcasestr(te->name, name) != NULL;
    }
#else
    int fn_flag = 0;
    int found   = 0;

    if ((flags & LDB_FIND_CASE_SENSITIVE) == 0)
        fn_flag |= FNM_CASEFOLD;

    if (flags & LDB_FIND_COMPLETE)
        found = fnmatch(name, te->name, fn_flag) == 0;
    else {
        char fn_name[sizeof(((struct SpaceLDB *)0)->search_string) + 2];
        BLI_snprintf(fn_name, sizeof(fn_name), "*%s*", name);
        found = fnmatch(fn_name, te->name, fn_flag) == 0;
    }
    return found;
#endif
} /* mat_livedb_filter_has_name() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Filter tree */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_filter_tree(SpaceLDB *slivedb, ListBase *lb)
{
    LiveDbTreeElement *te, *ten;

    /* although we don't have any search string, we return TRUE since the entire tree is ok then... */
    if (slivedb->search_string[0] == 0) return 1;

    for (te = lb->first; te; te = ten) {
        ten = te->next;

        if (!mat_livedb_filter_has_name(te, slivedb->search_string, slivedb->search_flags)) {
            *te->flag &= ~TE_SEARCHMATCH;

            if (!mat_livedb_filter_tree(slivedb, &te->subtree)) {
                mat_livedb_free_tree(&te->subtree);
                BLI_remlink(lb, te);
                MEM_freeN(te);
            }
        }
        else {
            *te->flag |= TE_SEARCHMATCH;
            mat_livedb_filter_tree(slivedb, &te->subtree);
        }
    }
    /* if there are still items in the list, that means that there were still some matches */
    return (lb->first != 0);
} /* mat_livedb_filter_tree() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Add element to the tree */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_add_element(SpaceLDB *slivedb, ListBase *lb, LiveDbItem **_item, LiveDbTreeElement *parent)
{
    LiveDbTreeElement   *te;
    LiveDbItem          *ptr;
    LiveDbItem          *item = *_item;

    te = MEM_callocN(sizeof(LiveDbTreeElement), "tree elem");
    BLI_addtail(lb, te);

    /* FIXME: So far using some already existing bytes in serialized data for the flags */
#ifdef __BIG_ENDIAN__
    te->flag = ((short*)(&item->type));
#else
    te->flag = ((short*)(&item->type)) + 1;
#endif

    if(!(*te->flag & TE_IS_USED)) {
        *te->flag = TE_IS_USED;
        *te->flag |= TE_CLOSED;
    }

    if (SEARCHING_MAT_LIVEDB(slivedb)) *te->flag |= TE_CHILDSEARCH;

    te->item    = item;
    te->parent  = parent;

    if (!item || TE_GET_TYPE(item->type) == MAT_LDB_TREE_ITEM_TYPE_NONE) {
        strcpy(te->name, IFACE_("(empty)"));
        *_item = (char*)item + item->size;
        return;
    }
    else if (TE_GET_TYPE(item->type) == MAT_LDB_TREE_ITEM_TYPE_MATERIAL) {
        char *cur_string = item->mat_item.name;

        int cur_size = strlen(cur_string) + 1;
        strncpy(te->name, cur_string, (cur_size < 256 ? cur_size : 256));
        cur_string += cur_size;

        cur_size = strlen(cur_string) + 1;
        strncpy(te->nick_name, cur_string, (cur_size < 256 ? cur_size : 256));
        cur_string += cur_size;

        cur_size = strlen(cur_string);
        if(cur_size) {
            strcpy(te->copyright, "© ");
            strncat(te->copyright, cur_string, 252);
        }
        else te->copyright[0] = 0;

        *_item = (char*)item + item->size;
    }
    else if (TE_GET_TYPE(item->type) == MAT_LDB_TREE_ITEM_TYPE_CATEGORY) {
        uint32_t a, cnt;

        int cur_size = strlen(item->cat_item.name) + 1;
        strncpy(te->name, item->cat_item.name, (cur_size < 256 ? cur_size : 256));

        *_item = (char*)item + item->size;
        ptr = *_item;

        cnt = item->cat_item.cat_cnt;
        for (a = 0; a < cnt; ++a)
            mat_livedb_add_element(slivedb, &te->subtree, &ptr, te);

        cnt = item->cat_item.mat_cnt;
        for (a = 0; a < cnt; ++a)
            mat_livedb_add_element(slivedb, &te->subtree, &ptr, te);

        *_item = ptr;
    }
    return;
} /* mat_livedb_add_element() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Main entry point for building the tree data-structure that the LiveDB represents */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_build_tree(Main *mainvar, SpaceLDB *slivedb, int reload)
{
    int         i, cat_cnt, mat_cnt;
    LiveDbItem  *cur_item;
    uint32_t    buf_size;
    static char cur_address[256] = {0};

    /* Are we looking for something - we want to tag parents to filter child matches
     * - this variable is only set once per tree build */
    if (slivedb->search_string[0] != 0)
        slivedb->search_flags |= LDB_SEARCH_RECURSIVE;
    else
        slivedb->search_flags &= ~LDB_SEARCH_RECURSIVE;

    if (slivedb->tree.first && (slivedb->storeflag & LDB_TREESTORE_REDRAW))
        return;

    mat_livedb_free_tree(&slivedb->tree);

    if(strcmp(cur_address, slivedb->server_address)) {
        size_t len = strlen(slivedb->server_address) + 1;
        strncpy(cur_address, slivedb->server_address, (len < 256 ? len : 256));
        if(!reload) reload = 1;
    }
    if (reload && slivedb->treestore) {
        MEM_freeN(slivedb->treestore);
        slivedb->treestore = 0;
    }
    if (!slivedb->treestore)
        slivedb->treestore = mat_livedb_get_tree(slivedb->server_address, &buf_size);

    if(slivedb->treestore) {
        cur_item = slivedb->treestore;
        cat_cnt  = cur_item->cat_item.cat_cnt;
        mat_cnt  = cur_item->cat_item.mat_cnt;

        /* Skip root */
        cur_item = (char*)cur_item + cur_item->size;

        for (i = 0; i < cat_cnt; ++i)
            mat_livedb_add_element(slivedb, &slivedb->tree, &cur_item, 0);

        for (i = 0; i < mat_cnt; ++i)
            mat_livedb_add_element(slivedb, &slivedb->tree, &cur_item, 0);

        mat_livedb_filter_tree(slivedb, &slivedb->tree);
    }
} /* mat_livedb_build_tree() */
