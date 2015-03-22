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

/** \file blender/editors/space_mat_livedb/mat_livedb_intern.h
 *  \ingroup spmat_livedb
 */

#ifndef __MAT_LIVEDB_INTERN_H__
#define __MAT_LIVEDB_INTERN_H__

#include "RNA_types.h"
#include "DNA_listBase.h"
#include "DNA_space_types.h"


static unsigned short LIVEDB_PORT = 5131;

/* Network packet types */
#define GET_LDB_CAT         1
#define GET_LDB_MAT_PREVIEW 2
#define GET_LDB_MAT         3

#define MAT_LDB_TREE_ITEM_TYPE_NONE      0
#define MAT_LDB_TREE_ITEM_TYPE_CATEGORY  1
#define MAT_LDB_TREE_ITEM_TYPE_MATERIAL  2

#define MAT_LDB_VALUE_TYPE_EMPTY     0
#define MAT_LDB_VALUE_TYPE_NODE      1
#define MAT_LDB_VALUE_TYPE_INT       2
#define MAT_LDB_VALUE_TYPE_INT2      3
#define MAT_LDB_VALUE_TYPE_INT3      4
#define MAT_LDB_VALUE_TYPE_INT4      5
#define MAT_LDB_VALUE_TYPE_FLOAT     6
#define MAT_LDB_VALUE_TYPE_FLOAT2    7
#define MAT_LDB_VALUE_TYPE_FLOAT3    8
#define MAT_LDB_VALUE_TYPE_FLOAT4    9
#define MAT_LDB_VALUE_TYPE_BOOL      10
#define MAT_LDB_VALUE_TYPE_STRING    11
#define MAT_LDB_VALUE_TYPE_COLOR     12
#define MAT_LDB_VALUE_TYPE_FILE      13
#define MAT_LDB_VALUE_TYPE_NLINK     14
#define MAT_LDB_VALUE_TYPE_FLINK     15
#define MAT_LDB_VALUE_TYPE_RAMP      16

struct wmOperatorType;
struct wmKeyConfig;
struct bContext;
struct bNodeTree;
struct Main;
#pragma pack(push)

#pragma pack (4)
typedef struct MaterialItem {
    int32_t  id;
    char     name[1];
} MaterialItem;

#pragma pack (4)
typedef struct CategoryItem {
    uint32_t cat_cnt;
    uint32_t mat_cnt;
    char     name[1];
} CategoryItem;

#pragma pack (4)
typedef struct RampItem {
    uint32_t pos_cnt;
    float    pos_data[1];
} RampItem;

#pragma pack (4)
typedef struct LiveDbItem {
    uint32_t type;
    uint32_t size;
    union {
        CategoryItem cat_item;
        MaterialItem mat_item;
    };
} LiveDbItem;

typedef struct LiveDbTreeElement {
    struct LiveDbTreeElement *next, *prev, *parent;
    ListBase subtree;
    float xs, ys;       // do selection
    short xend;         // width of item display, for select
    short *flag;

    char name[256];
    char nick_name[256];
    char copyright[256];

    LiveDbItem *item;
}  LiveDbTreeElement;

#pragma pack (8)
typedef struct MatItem {
    int32_t type;
    uint32_t size;
    union {
        float    float_vector[4];
        int32_t  int_vector[4];
        uint32_t uint_vector[4];
        char     data[1];
    };
} MatItem;

typedef struct GetMaterialJob {
	short *stop, *do_update;
	float *progress;

    struct bContext     *C;
    struct Main         *bmain;
    struct bNodeTree    *ntree;
    int32_t             mat_id;
    char                address[FILE_MAX];
} GetMaterialJob;

/* LiveDbTreeElement->flag */
#define TE_ACTIVE       1
#define TE_LAZY_CLOSED  2
#define TE_IS_USED      4
#define TE_CLOSED		8
#define TE_SELECTED	    16
#define TE_TEXTBUT		32
#define TE_CHILDSEARCH  64
#define TE_SEARCHMATCH  128
#define TE_DELETED      256

#define TE_GET_TYPE(x)  ((x) & 0x0000FFFF)

/* button events */
#define LDB_NAMEBUTTON       1

/* size constants */
#define LDB_Y_OFFSET 2
#define MAT_LIVEDB_UI_UNIT_Y (UI_UNIT_Y * 4)
#define LDB_NODES_H_GAP 100
#define LDB_NODES_V_GAP 100

#define SEARCHING_MAT_LIVEDB(sov)   (sov->search_flags & LDB_SEARCH_RECURSIVE)

/* is the currrent element open? if so we also show children */
#define MAT_LIVEDB_ELEM_OPEN(telm, sv)    ( (*telm->flag & TE_CLOSED) == 0 || (SEARCHING_MAT_LIVEDB(sv) && (*telm->flag & TE_CHILDSEARCH)) )


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_tree.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_free_tree(ListBase *lb);
void mat_livedb_cleanup_tree(struct SpaceLDB *slivedb);
void mat_livedb_build_tree(struct Main *mainvar, struct SpaceLDB *slivedb, int reload);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_draw.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void draw_mat_livedb(const struct bContext *C);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_select.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int mat_livedb_item_do_activate(struct bContext *C, int x, int y, bool extend);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_edit.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int  mat_livedb_has_one_flag(struct SpaceLDB *slivedb, ListBase *lb, short flag, short curlevel);
void mat_livedb_set_flag(struct SpaceLDB *slivedb, ListBase *lb, short flag, short set);
void mat_livedb_item_rename_cb(struct bContext *C, LiveDbTreeElement *te);

void MAT_LIVEDB_OT_item_activate(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_item_openclose(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_item_rename(struct wmOperatorType *ot);

void MAT_LIVEDB_OT_show_one_level(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_hide_one_level(struct wmOperatorType *ot);

void MAT_LIVEDB_OT_selected_toggle(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_expanded_toggle(struct wmOperatorType *ot);

void MAT_LIVEDB_OT_scroll_page_up(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_scroll_page_down(struct wmOperatorType *ot);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_tools.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void MAT_LIVEDB_OT_operation(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_material_operation(struct wmOperatorType *ot);
void MAT_LIVEDB_OT_group_operation(struct wmOperatorType *ot);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_ops.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
void mat_livedb_operatortypes(void);
void mat_livedb_keymap(struct wmKeyConfig *keyconf);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_nodes.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int get_material(struct Main *bmain, struct bContext *C, Scene *scene, struct bNodeTree *ntree, const char *address, int32_t mat_id);

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* mat_livedb_net.c */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
struct LiveDbItem*  mat_livedb_get_tree(const char *address, uint32_t *buf_size);
unsigned char*      mat_livedb_get_mat_preview(const char *address, int32_t id, unsigned int *width, unsigned int *height, const char *_file_path);
struct MatItem*     mat_livedb_get_material(const char *address, int32_t mat_id, uint32_t *buf_size);

#pragma pack(pop)

#endif /* __MAT_LIVEDB_INTERN_H__ */
