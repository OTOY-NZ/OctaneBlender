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

/** \file blender/editors/space_mat_livedb/mat_livedb_nodes.c
 *  \ingroup spmat_livedb
 */

#ifndef WIN32
#  define GetCurrentDir _getcwd
#else
#  include <direct.h>
#  include "utf_winfunc.h"
#  define GetCurrentDir getcwd
#endif

#include "mat_livedb_intern.h"

#include <string.h>

#include "MEM_guardedalloc.h"

#include "BLI_blenlib.h"

#include "BKE_image.h"
#include "BKE_context.h"
#include "BKE_global.h"
#include "BKE_main.h"
#include "BKE_node.h"

#include "ED_render.h"
#include "ED_node.h"
#include "ED_screen.h"

#include "WM_api.h"
#include "WM_types.h"

#include "DNA_userdef_types.h"

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Connect two nodes */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int connect_nodes(Main *bmain, bNodeTree *ntree, bNode *node_fr, bNodeSocket *sock_fr, bNode *node_to, bNodeSocket *sock_to)
{
    bNodeLink *link = nodeAddLink(ntree, node_fr, sock_fr, node_to, sock_to);
    ntreeUpdateTree(bmain, ntree);
    if (!(link->flag & NODE_LINK_VALID)) {
        nodeRemLink(ntree, link);
        return 0;
    }
    return 1;
} /* connect_nodes() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Connect node output to another node input */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int connect_node(Main *bmain, bNodeTree *ntree, bNode *node_fr, bNode *node_to, bNodeSocket *sock_to)
{
    bNodeSocket *sock_fr = node_fr->outputs.first;
    if (sock_fr && sock_to) {
        if(!connect_nodes(bmain, ntree, node_fr, sock_fr, node_to, sock_to))
            return 0;
    }
    return 1;
} /* connect_node() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Add LiveDB node recursion */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static MatItem *mat_livedb_add_mat_element(Main *bmain, bContext *C, bNodeTree *ntree, bNode *node_to, bNodeSocket *sock_to, MatItem **_item, char* file_path, float x_pos, float *y_pos)
{
    MatItem          *ptr;
    MatItem          *item = *_item;
    char             tex_file_name[1024];

    bNodeSocket             *sock;
    bNodeSocketValueFloat   *sock_float;
    bNodeSocketValueInt     *sock_int;
    bNodeSocketValueBoolean *sock_bool;
    bNodeSocketValueVector  *sock_vector;
    bNodeSocketValueRGBA    *sock_rgba;
    bNodeSocketValueString  *sock_string;

    switch (item->type) {
        case MAT_LDB_VALUE_TYPE_EMPTY: {
            *_item = (char*)item + item->size;
            break;
        }
        case MAT_LDB_VALUE_TYPE_FLINK: {
            ptr = (MatItem*) ((char*)item - item->uint_vector[0]);
            mat_livedb_add_mat_element(bmain, C, ntree, node_to, 0, &ptr, file_path, 0, 0);

            *_item = (char*)item + item->size;
            break;
        }
        case MAT_LDB_VALUE_TYPE_NLINK: {
            bNode *linked_node = *((bNode**) ((MatItem*)((char*)item - item->uint_vector[0]))->data);

            connect_node(bmain, ntree, linked_node, node_to, sock_to);

            *_item = (char*)item + item->size;
            break;
        }
        case MAT_LDB_VALUE_TYPE_NODE: {
            if(sock_to->type == SOCK_FLOAT && sock_to->default_value && !strcmp(item->data, "ShaderNodeOctFloatTex")) {
                item = (char*)item + item->size;

                ((bNodeSocketValueFloat*)sock_to->default_value)->value = item->float_vector[0];

                *_item = (char*)item + item->size;
            }
            else if(sock_to->type == SOCK_RGBA && sock_to->default_value && !strcmp(item->data, "ShaderNodeOctRGBSpectrumTex")) {
                item = (char*)item + item->size;

                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[0] = item->float_vector[0];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[1] = item->float_vector[1];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[2] = item->float_vector[2];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[3] = item->float_vector[3];

                *_item = (char*)item + item->size;
            }
            else {
                float   cur_y_pos;
                int     node_height     = U.widget_unit;
                bool    childs_present  = false;
                bNode   *node_fr        = nodeAddNode(C, ntree, item->data);

                connect_node(bmain, ntree, node_fr, node_to, sock_to);

                *_item = (char*)item + item->size;
                ptr = *_item;

                *((bNode**)item->data) = node_fr;

                if(node_fr->type == SH_NODE_OCT_IMAGE_TEX || node_fr->type == SH_NODE_OCT_FLOAT_IMAGE_TEX || node_fr->type == SH_NODE_OCT_ALPHA_IMAGE_TEX) {
                    mat_livedb_add_mat_element(bmain, C, ntree, node_fr, 0, &ptr, file_path, 0, 0);
                    node_height += (U.widget_unit * 2.5);
                }

                node_fr->locx = x_pos - node_fr->width - LDB_NODES_H_GAP;
                node_fr->locy = cur_y_pos = *y_pos;

                for (sock = node_fr->inputs.first; sock; sock = sock->next) {
                    if(!sock) continue;
                    if(!childs_present) childs_present = true;
                    node_height += U.widget_unit;

                    mat_livedb_add_mat_element(bmain, C, ntree, node_fr, sock, &ptr, file_path, node_fr->locx, &cur_y_pos);
                }
                *_item = ptr;

                *y_pos -= (node_height + LDB_NODES_V_GAP);
                if(childs_present) *y_pos = (*y_pos < cur_y_pos ? *y_pos : cur_y_pos);
            }
            break;
        }
        case MAT_LDB_VALUE_TYPE_INT:
            if(sock_to->default_value)
                ((bNodeSocketValueInt*)sock_to->default_value)->value = item->int_vector[0];

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_INT2:
            if(sock_to->default_value) {
                ((bNodeSocketValueVector*)sock_to->default_value)->value[0] = item->int_vector[0];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[1] = item->int_vector[1];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_INT3:
            if(sock_to->default_value) {
                ((bNodeSocketValueVector*)sock_to->default_value)->value[0] = item->int_vector[0];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[1] = item->int_vector[1];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[2] = item->int_vector[2];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_INT4:
            if(sock_to->default_value) {
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[0] = item->int_vector[0];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[1] = item->int_vector[1];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[2] = item->int_vector[2];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[3] = item->int_vector[3];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_FLOAT:
            if(sock_to->default_value)
                ((bNodeSocketValueFloat*)sock_to->default_value)->value = item->float_vector[0];

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_FLOAT2:
            if(sock_to->default_value) {
                ((bNodeSocketValueVector*)sock_to->default_value)->value[0] = item->float_vector[0];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[1] = item->float_vector[1];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_FLOAT3:
            if(sock_to->default_value) {
                ((bNodeSocketValueVector*)sock_to->default_value)->value[0] = item->float_vector[0];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[1] = item->float_vector[1];
                ((bNodeSocketValueVector*)sock_to->default_value)->value[2] = item->float_vector[2];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_FLOAT4:
            if(sock_to->default_value) {
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[0] = item->float_vector[0];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[1] = item->float_vector[1];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[2] = item->float_vector[2];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[3] = item->float_vector[3];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_BOOL:
            if(sock_to->default_value)
                ((bNodeSocketValueBoolean*)sock_to->default_value)->value = item->int_vector[0];

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_STRING:
            if(sock_to->default_value)
                strcpy(((bNodeSocketValueString*)sock_to->default_value)->value, item->data);

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_COLOR:
            if(sock_to->default_value) {
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[0] = item->float_vector[0];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[1] = item->float_vector[1];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[2] = item->float_vector[2];
                ((bNodeSocketValueRGBA*)sock_to->default_value)->value[3] = item->float_vector[3];
            }

            *_item = (char*)item + item->size;
            break;
        case MAT_LDB_VALUE_TYPE_FILE: {
            char* file_name;
            FILE *file;
            struct Image *ima = (struct Image*)node_to->id;

            file_name = item->data + sizeof(uint32_t);
            strcpy(tex_file_name, file_path);
            strcat(tex_file_name, file_name);

            file = BLI_fopen(tex_file_name, "rb");
            if(!file) {
                file = BLI_fopen(tex_file_name, "wb");
                if(file) {
                    if(!fwrite(item->data + sizeof(uint32_t) + strlen(file_name) + 1, *((uint32_t*)item->data), 1, file)) {
                    }
                    fclose(file);
                }
            }
            else fclose(file);

            if(!ima)
                node_to->id = BKE_image_load_exists(tex_file_name);

            *_item = (char*)item + item->size;
            break;
        }
        default:
            break;
    }
    return *_item;
} /* mat_livedb_add_mat_element */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Free job data */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void get_material_data_free(void *customdata)
{
    GetMaterialJob *mj = customdata;
    MEM_freeN(mj);
} /* get_material_free() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Start "Get material" job */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void get_material_startjob(void *customdata, short *stop, short *do_update, float *progress)
{
    Main            *bmain;
    bContext        *C;
    bNodeTree       *ntree;
    MatItem         *items;
    uint32_t        buf_size;
    GetMaterialJob  *mj = customdata;

    mj->stop        = stop;
    mj->do_update   = do_update;
    mj->progress    = progress;

    ntree   = mj->ntree;
    bmain   = mj->bmain;
    C       = mj->C;

    *progress = 0.1f;

    items = mat_livedb_get_material(mj->address, mj->mat_id, &buf_size);

    *progress = 0.9f;

    if(items) {
        bNode       *node, *next;
        MatItem     *cur_item = items;
        bNode       *node_to;
        bNodeSocket *sock_to;
        char        file_path[FILE_MAX];
        float       cur_y_pos = 0;

        /* Remove all existing nodes */
        ED_preview_kill_jobs(C);
        for (node = ntree->nodes.first; node; node = next) {
            next = node->next;
            /* check id user here, nodeFreeNode is called for free dbase too */
            if (node->id) node->id->us--;
            nodeFreeNode(ntree, node);
        }
        ntreeUpdateTree(bmain, ntree);

        node_to = nodeAddNode(C, ntree, "ShaderNodeOutputMaterial");
        node_to->locx = 0;
        node_to->locy = 0;

        for (sock_to = node_to->inputs.first; sock_to; sock_to = sock_to->next) {
            if(!sock_to || strcmp(sock_to->name, "Surface")) continue;
            break;
        }

        /* create file path */
        if(!strlen(G.main->name)) {
            char *cur_path = BLI_get_folder_create(BLENDER_USER_DATAFILES, 0);
            strcpy(file_path, cur_path);
            strcat(file_path, "/livedb/");
        }
        else {
            BLI_strncpy(file_path, "//livedb/", sizeof(file_path));
            BLI_path_abs(file_path, G.main->name);
        }
        strcat(file_path, mj->address);
        strcat(file_path, "/textures/");
        BLI_dir_create_recursive(file_path);

        mat_livedb_add_mat_element(bmain, C, ntree, node_to, sock_to, &cur_item, file_path, 0, &cur_y_pos);

        ED_node_tree_update(C);
        ED_node_tag_update_nodetree(bmain, ntree);

        MEM_freeN(items);
    }

    *do_update  = TRUE;
    *stop       = 0;
    *progress   = 1.0f;

    return;
} /* get_material_job() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* End "Get material" job */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void get_material_endjob(void *customdata)
{
    GetMaterialJob *mj = customdata;
} /* get_material_endjob() */


/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get material from LiveDB */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
int get_material(Main *bmain, bContext *C, Scene *scene, bNodeTree *ntree, const char *address, int32_t mat_id)
{
    /* Setup job */
    wmJob           *wm_job = WM_jobs_get(CTX_wm_manager(C), CTX_wm_window(C), scene, "Get LDB Material", WM_JOB_PROGRESS, WM_JOB_TYPE_RENDER);
    GetMaterialJob  *mj     = MEM_callocN(sizeof(GetMaterialJob), "get LDB mat job");

    mj->C       = C;
    mj->bmain   = bmain;
    mj->ntree   = ntree;
    mj->mat_id  = mat_id;
    strcpy(mj->address, address);

    WM_jobs_customdata_set(wm_job, mj, get_material_data_free);
    WM_jobs_timer(wm_job, 0.1, NC_SCENE | ND_RENDER_RESULT, 0);
    WM_jobs_callbacks(wm_job, get_material_startjob, NULL, NULL, get_material_endjob);

    WM_jobs_start(CTX_wm_manager(C), wm_job);

    WM_cursor_wait(0);
    WM_event_add_notifier(C, NC_SCENE | ND_RENDER_RESULT, scene);

    return 1;
} /* get_material() */
