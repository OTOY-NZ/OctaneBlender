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
#include "BKE_appdir.h"
#include "BKE_material.h"

#include "BLT_translation.h"

#include "ED_render.h"
#include "ED_node.h"
#include "ED_screen.h"

#include "WM_api.h"
#include "WM_types.h"

#include "DNA_userdef_types.h"
#include "DNA_object_types.h"
#include "DNA_mesh_types.h"
#include "../../source/blender/nodes/NOD_shader.h"

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Connect two nodes */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static int connect_nodes(Main *bmain,
                         bNodeTree *ntree,
                         bNode *node_fr,
                         bNodeSocket *sock_fr,
                         bNode *node_to,
                         bNodeSocket *sock_to)
{
  bNodeLink *link = nodeAddLink(ntree, node_fr, sock_fr, node_to, sock_to);
  ntreeUpdateTree(bmain, ntree);
  // if (!(link->flag & NODE_LINK_VALID)) {
  //  nodeRemLink(ntree, link);
  //  return 0;
  //}
  return 1;
} /* connect_nodes() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Connect node output to another node input */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static int connect_node(
    Main *bmain, bNodeTree *ntree, bNode *node_fr, bNode *node_to, bNodeSocket *sock_to)
{
  bNodeSocket *sock_fr = node_fr->outputs.first;
  if (sock_fr && sock_to) {
    if (!connect_nodes(bmain, ntree, node_fr, sock_fr, node_to, sock_to))
      return 0;
  }
  return 1;
} /* connect_node() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Add LiveDB node recursion */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static MatItem *mat_livedb_add_mat_element(Main *bmain,
                                           bContext *C,
                                           bNodeTree *ntree,
                                           bNode *node_to,
                                           bNodeSocket *sock_to,
                                           MatItem **_item,
                                           char *file_path,
                                           float x_pos,
                                           float *y_pos)
{
  MatItem *ptr;
  MatItem *item = *_item;
  char tex_file_name[1024];

  bNodeSocket *sock;

  switch (item->type) {
    case MAT_LDB_VALUE_TYPE_EMPTY: {
      *_item = (MatItem *)((char *)item + item->size);
      break;
    }
    case MAT_LDB_VALUE_TYPE_FLINK: {
      ptr = (MatItem *)((char *)item - item->uint_vector[0]);
      mat_livedb_add_mat_element(bmain, C, ntree, node_to, 0, &ptr, file_path, 0, 0);

      *_item = (MatItem *)((char *)item + item->size);
      break;
    }
    case MAT_LDB_VALUE_TYPE_NLINK: {
      bNode *linked_node = *((bNode **)((MatItem *)((char *)item - item->uint_vector[0]))->data);

      connect_node(bmain, ntree, linked_node, node_to, sock_to);

      *_item = (MatItem *)((char *)item + item->size);
      break;
    }
    case MAT_LDB_VALUE_TYPE_NODE: {
      if (sock_to->type == SOCK_FLOAT && sock_to->default_value &&
          !strcmp(item->data, "ShaderNodeOctFloatTex")) {
        item = (MatItem *)((char *)item + item->size);

        ((bNodeSocketValueFloat *)sock_to->default_value)->value = item->float_vector[0];

        *_item = (MatItem *)((char *)item + item->size);
      }
      else if (sock_to->type == SOCK_RGBA && sock_to->default_value &&
               !strcmp(item->data, "ShaderNodeOctRGBSpectrumTex")) {
        item = (MatItem *)((char *)item + item->size);

        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[0] = item->float_vector[0];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[1] = item->float_vector[1];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[2] = item->float_vector[2];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[3] = item->float_vector[3];

        *_item = (MatItem *)((char *)item + item->size);
      }
      else {
        float cur_y_pos;
        int node_height = U.widget_unit;
        bool childs_present = false;
        bNode *node_fr = nodeAddNode(C, ntree, item->data);

        connect_node(bmain, ntree, node_fr, node_to, sock_to);

        *_item = (MatItem *)((char *)item + item->size);
        ptr = *_item;

        *((bNode **)item->data) = node_fr;

#ifdef WITH_OCTANE
        if (node_fr->type == SH_NODE_OCT_IMAGE_TEX ||
            node_fr->type == SH_NODE_OCT_FLOAT_IMAGE_TEX ||
            node_fr->type == SH_NODE_OCT_ALPHA_IMAGE_TEX ||
            node_fr->type == SH_NODE_OCT_INSTANCE_COLOR_TEX) {
          mat_livedb_add_mat_element(bmain, C, ntree, node_fr, 0, &ptr, file_path, 0, 0);
          node_height += (U.widget_unit * 2.5);
        }
#endif  // WITH_OCTANE

        node_fr->locx = x_pos - node_fr->width - LDB_NODES_H_GAP;
        node_fr->locy = cur_y_pos = *y_pos;

        for (sock = node_fr->inputs.first; sock; sock = sock->next) {
          if (!sock)
            continue;
          if (!childs_present)
            childs_present = true;
          node_height += U.widget_unit;

          mat_livedb_add_mat_element(
              bmain, C, ntree, node_fr, sock, &ptr, file_path, node_fr->locx, &cur_y_pos);
        }

#ifdef WITH_OCTANE
        if (node_fr->type == SH_NODE_OCT_GRADIENT_TEX ||
            node_fr->type == SH_NODE_OCT_TOON_RAMP_TEX) {
          mat_livedb_add_mat_element(bmain, C, ntree, node_fr, 0, &ptr, file_path, 0, 0);
          node_height += (U.widget_unit * 2.5);
        }
#endif  // WITH_OCTANE

        *_item = ptr;

        *y_pos -= (node_height + LDB_NODES_V_GAP);
        if (childs_present)
          *y_pos = (*y_pos < cur_y_pos ? *y_pos : cur_y_pos);
      }
      break;
    }
    case MAT_LDB_VALUE_TYPE_INT:
      if (sock_to->default_value)
        ((bNodeSocketValueInt *)sock_to->default_value)->value = item->int_vector[0];

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_INT2:
      if (sock_to->default_value) {
        ((bNodeSocketValueVector *)sock_to->default_value)->value[0] = item->int_vector[0];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[1] = item->int_vector[1];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_INT3:
      if (sock_to->default_value) {
        ((bNodeSocketValueVector *)sock_to->default_value)->value[0] = item->int_vector[0];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[1] = item->int_vector[1];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[2] = item->int_vector[2];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_INT4:
      if (sock_to->default_value) {
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[0] = item->int_vector[0];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[1] = item->int_vector[1];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[2] = item->int_vector[2];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[3] = item->int_vector[3];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_FLOAT:
      if (sock_to->default_value)
        ((bNodeSocketValueFloat *)sock_to->default_value)->value = item->float_vector[0];

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_FLOAT2:
      if (sock_to->default_value) {
        ((bNodeSocketValueVector *)sock_to->default_value)->value[0] = item->float_vector[0];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[1] = item->float_vector[1];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_FLOAT3:
      if (sock_to->default_value) {
        ((bNodeSocketValueVector *)sock_to->default_value)->value[0] = item->float_vector[0];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[1] = item->float_vector[1];
        ((bNodeSocketValueVector *)sock_to->default_value)->value[2] = item->float_vector[2];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_FLOAT4:
      if (sock_to->default_value) {
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[0] = item->float_vector[0];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[1] = item->float_vector[1];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[2] = item->float_vector[2];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[3] = item->float_vector[3];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_BOOL:
      if (sock_to->default_value)
        ((bNodeSocketValueBoolean *)sock_to->default_value)->value = item->int_vector[0];

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_STRING:
      if (sock_to->default_value)
        strcpy(((bNodeSocketValueString *)sock_to->default_value)->value, item->data);

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_COLOR:
      if (sock_to->default_value) {
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[0] = item->float_vector[0];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[1] = item->float_vector[1];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[2] = item->float_vector[2];
        ((bNodeSocketValueRGBA *)sock_to->default_value)->value[3] = item->float_vector[3];
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    case MAT_LDB_VALUE_TYPE_FILE: {
      char *file_name;
      FILE *file;
      struct Image *ima = (struct Image *)node_to->id;

      file_name = item->data + sizeof(uint32_t);

      if (file_name[0]) {
        strcpy(tex_file_name, file_path);
        strcat(tex_file_name, file_name);

        file = BLI_fopen(tex_file_name, "rb");
        if (!file) {
          file = BLI_fopen(tex_file_name, "wb");
          if (file) {
            if (!fwrite(item->data + sizeof(uint32_t) + strlen(file_name) + 1,
                        *((uint32_t *)item->data),
                        1,
                        file)) {
            }
            fclose(file);
          }
        }
        else
          fclose(file);
      }
      else
        tex_file_name[0] = 0;

      if (!ima)
        node_to->id = (struct ID *)BKE_image_load_exists(bmain, tex_file_name);

      *_item = (MatItem *)((char *)item + item->size);
      break;
    }
    case MAT_LDB_VALUE_TYPE_RAMP: {
      char *file_name;
      FILE *file;
      struct ColorBand *coba = (struct ColorBand *)node_to->storage;

      RampItem *ramp_item = (RampItem *)item->data;

      if (coba && ramp_item->pos_cnt > 1) {
        int i;
        coba->tot = ramp_item->pos_cnt;
        for (i = 0; i < ramp_item->pos_cnt; ++i) {
          coba->data[i].pos = ramp_item->pos_data[i * 4 + 0];
          coba->data[i].r = ramp_item->pos_data[i * 4 + 1];
          coba->data[i].g = ramp_item->pos_data[i * 4 + 2];
          coba->data[i].b = ramp_item->pos_data[i * 4 + 3];
          coba->data[i].a = 1.0;
        }
      }

      *_item = (MatItem *)((char *)item + item->size);
      break;
    }
    default:
      break;
  }
  return *_item;
} /* mat_livedb_add_mat_element */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Free job data */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void get_material_data_free(void *customdata)
{
  GetMaterialJob *mj = customdata;
  MEM_freeN(mj);
} /* get_material_free() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Get material from LiveDB */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
int get_material(
    Main *bmain, bContext *C, Scene *scene, bNodeTree *ntree, const char *address, int32_t mat_id)
{
  return 0;
} /* get_material() */

bNodeTree *mat_livedb_get_target_node_tree(struct bContext *C)
{
  Scene *scene = CTX_data_scene(C);
  Main *bmain = CTX_data_main(C);

  const char *address = "127.0.0.1";
  bNodeTree *target_ntree = NULL;

  bool not_set = true;
  Object *cur_object;
  Object *ob;
  Material *ma;

  ViewLayer *view_layer = CTX_data_view_layer(C);
  cur_object = OBACT(view_layer);

  if (not_set) {
    ob = (Object *)cur_object;
    ma = BKE_material_add(bmain, DATA_("LDB Material"));

    ma->use_nodes = true;
    ma->nodetree = ntreeAddTree(NULL, "Shader Nodetree", ntreeType_Shader->idname);
    if (ob) {
      BKE_object_material_slot_remove(bmain, ob);
      assign_material(bmain, ob, ma, ob->totcol + 1, BKE_MAT_ASSIGN_USERPREF);
    }
    WM_event_add_notifier(C, NC_MATERIAL | NA_ADDED, ma);
    target_ntree = ma->nodetree;
  }
  return target_ntree;
}

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* Start "Get material" job */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void get_livedb_material_startjob(void *customdata,
                                         short *stop,
                                         short *do_update,
                                         float *progress)
{
  Main *bmain;
  bContext *C;
  bNodeTree *ntree;
  MatItem *items = NULL;
  GetMaterialJob *mj = customdata;

  mj->stop = stop;
  mj->do_update = do_update;
  mj->progress = progress;

  ntree = mj->ntree;
  bmain = mj->bmain;
  C = mj->C;

  *progress = 0.0f;

  int cur_socket;
  MatItem *buf;
  uint32_t buf_size;

  cur_socket = mat_livedb_connect(mj->address);
  if (!cur_socket) {
    buf_size = 0;
    return;
  }

  if (!mat_livedb_request_material_new(cur_socket)) {
    buf_size = 0;
    mat_livedb_disconnect(cur_socket);
    return;
  }

  *progress = 0.5f;

  WM_report(RPT_INFO, "Connect to LiveDB successfully! Click import to start download!");

  bool is_close = false;
  while (!is_close) {
    buf = mat_livedb_receive_new(cur_socket, GET_LDB_MAT_NEW, &buf_size, &is_close);
    if (!buf)
      continue;
    if (!buf_size) {
      MEM_freeN(buf);
      continue;
    }
    items = buf;
    ntree = mat_livedb_get_target_node_tree(C);
    if (!ntree)
      continue;

    if (items) {

      bNode *node, *next;
      MatItem *cur_item = items;
      bNode *node_to;
      bNodeSocket *sock_to;
      char file_path[FILE_MAX];
      float cur_y_pos = 0;

      /* Remove all existing nodes */
      ED_preview_kill_jobs(CTX_wm_manager(C), bmain);
      for (node = ntree->nodes.first; node; node = next) {
        next = node->next;
        /* check id user here, nodeFreeNode is called for free dbase too */
        if (node->id)
          node->id->us--;
        nodeRemoveNode(bmain, ntree, node, true);
      }
      ntreeUpdateTree(bmain, ntree);

      node_to = nodeAddNode(C, ntree, "ShaderNodeOutputMaterial");
      node_to->locx = 0;
      node_to->locy = 0;

      for (sock_to = node_to->inputs.first; sock_to; sock_to = sock_to->next) {
        if (!sock_to || strcmp(sock_to->name, "Surface"))
          continue;
        break;
      }

      /* create file path */
      if (!strlen(G.main->name)) {
        char *cur_path = (char *)BKE_appdir_folder_id_create(BLENDER_USER_DATAFILES, 0);
        strcpy(file_path, cur_path);
        strcat(file_path, "/livedb/");
      }
      else {
        BLI_strncpy(file_path, "//livedb/", sizeof(file_path));
        BLI_path_abs(file_path, G.main->name);
      }
      strcat(file_path, mj->address);
      strcat(file_path, "/textures/");
      BLI_path_native_slash(file_path);
      BLI_dir_create_recursive(file_path);

      mat_livedb_add_mat_element(
          bmain, C, ntree, node_to, sock_to, &cur_item, file_path, 0, &cur_y_pos);

      ED_node_tree_update(C);
      ED_node_tag_update_nodetree(bmain, ntree, 0);

      MEM_freeN(items);

      WM_report(RPT_INFO, "Update successfully! Please check material panel or node editor!");
    }
  }

  mat_livedb_disconnect(cur_socket);

  *do_update = 1;
  *stop = 0;
  *progress = 1.0f;

  return;
} /* get_material_job() */

/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
/* End "Get material" job */
/* ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
static void get_livedb_material_endjob(void *customdata)
{
  GetMaterialJob *mj = customdata;

  bNodeTree *ntree = mj->ntree;
} /* get_material_endjob() */

int get_livedb_material(bContext *C, void *arg1, void *arg2)
{

  Scene *scene = CTX_data_scene(C);
  Main *bmain = CTX_data_main(C);

  const char *address = "127.0.0.1";
  bNodeTree *target_ntree = NULL;

  bool not_set = true;
  Object *cur_object;
  Object *ob;
  Material *ma;

  /* Setup job */
  wmJob *wm_job = WM_jobs_get(CTX_wm_manager(C),
                              CTX_wm_window(C),
                              scene,
                              "Get LiveDB Mat",
                              WM_JOB_PROGRESS,
                              WM_JOB_TYPE_RENDER);
  GetMaterialJob *mj = MEM_callocN(sizeof(GetMaterialJob), "get LiveDB mat job");

  mj->C = C;
  mj->bmain = bmain;
  mj->ntree = NULL;
  strcpy(mj->address, address);

  WM_jobs_customdata_set(wm_job, mj, get_material_data_free);
  WM_jobs_timer(wm_job, 0.1, NC_SCENE | ND_RENDER_RESULT, 0);
  WM_jobs_callbacks(wm_job, get_livedb_material_startjob, NULL, NULL, get_livedb_material_endjob);

  WM_jobs_start(CTX_wm_manager(C), wm_job);

  WM_cursor_wait(0);
  WM_event_add_notifier(C, NC_SCENE | ND_RENDER_RESULT, scene);
  return 1;
}
