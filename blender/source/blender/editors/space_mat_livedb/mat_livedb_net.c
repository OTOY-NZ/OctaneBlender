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

/** \file blender/editors/space_mat_livedb/mat_livedb_net.c
 *  \ingroup spmat_livedb
 */

#include "mat_livedb_intern.h"

#undef htonl
#undef ntohl

#ifndef WIN32
#  include <unistd.h>
#  include <sys/types.h>
#  include <sys/socket.h>
#  include <netinet/ip.h>
#  include <netdb.h>
#  define GetCurrentDir _getcwd
#else
#  include "winsock2.h"
#  include <direct.h>
#  include "utf_winfunc.h"
#  define GetCurrentDir getcwd
#endif

#undef max
#undef min
#undef rad2

#pragma push_macro("htonl")
#define htonl 1
#pragma push_macro("ntohl")
#define ntohl 1

#include "MEM_guardedalloc.h"

#include "BLI_math.h"
#include "BLI_blenlib.h"
#ifdef WIN32
#   include "BLI_winstuff.h"
#endif

#include "BKE_global.h"
#include "BKE_main.h"

#pragma pop_macro("htonl")
#pragma pop_macro("ntohl")

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Connect the LiveDB at specific IP or domain name. Returns the socket. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_connect(const char *address)
{
    int     cur_socket;
    struct  hostent *host;
    struct  sockaddr_in sa;

    host = gethostbyname(address);
    if(!host || host->h_length != sizeof(struct in_addr)) {
        return -1;
    }
    cur_socket = socket(AF_INET, SOCK_STREAM, 0);
    if(cur_socket < 0) return -1;

    memset(&sa, 0, sizeof(sa));
    sa.sin_family = AF_INET;
    sa.sin_port = htons(0);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);
    if(bind(cur_socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
        close(cur_socket);
#else
        closesocket(cur_socket);
#endif
        return -1;
    }
    sa.sin_port = htons(LIVEDB_PORT);
    sa.sin_addr = *(struct in_addr*) host->h_addr;
    if(connect(cur_socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
        close(cur_socket);
#else
        closesocket(cur_socket);
#endif
        return -1;
    }
    return cur_socket;
} /* mat_livedb_connect() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Disconnect LiveDB. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void mat_livedb_disconnect(int _socket)
{
#ifndef WIN32
    close(_socket);
#else
    closesocket(_socket);
#endif
} /* mat_livedb_disconnect() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Send not parametrised request to LiveDB. Returns boolean success. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_request(int _socket, uint64_t _type) {
    char buffer[sizeof(uint64_t) * 2];

    *(uint64_t*)buffer = _type;
    *(uint64_t*)(buffer + sizeof(uint64_t)) = 0;

    if(send(_socket, (const char*)buffer, (unsigned int)sizeof(uint64_t) * 2, 0) != (sizeof(uint64_t) * 2)) return 0;
    else return 1;
} /* mat_livedb_request() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Send the "Get material preview" request to LiveDB. Returns boolean success. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_request_preview(int _socket, int32_t mat_id) {
    char buffer[sizeof(uint64_t) * 2 + sizeof(int32_t)];

    *(uint64_t*)buffer = GET_LDB_MAT_PREVIEW;
    *(uint64_t*)(buffer + sizeof(uint64_t))     = sizeof(int32_t);
    *(int32_t*)(buffer + sizeof(uint64_t) * 2)  = mat_id;

    if(send(_socket, (const char*)buffer, (unsigned int)sizeof(uint64_t) * 2 + sizeof(int32_t), 0) != (sizeof(uint64_t) * 2 + sizeof(int32_t))) return 0;
    else return 1;
} /* mat_livedb_request_preview() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Send the "Get material" request to LiveDB. Returns boolean success. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static int mat_livedb_request_material(int _socket, int32_t mat_id)
{
    char buffer[sizeof(uint64_t) * 2 + sizeof(int32_t)];

    *(uint64_t*)buffer = GET_LDB_MAT;
    *(uint64_t*)(buffer + sizeof(uint64_t))     = sizeof(int32_t);
    *(int32_t*)(buffer + sizeof(uint64_t) * 2)  = mat_id;

    if(send(_socket, (const char*)buffer, (unsigned int)sizeof(uint64_t) * 2 + sizeof(int32_t), 0) != (sizeof(uint64_t) * 2 + sizeof(int32_t))) return 0;
    else return 1;
} /* mat_livedb_request_material() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get the reply from LiveDB. Returns dynamically allocated buffer. Responsibility of caller to free it. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
static void* mat_livedb_receive(int _socket, uint64_t _type, uint32_t *buf_size) {
    uint64_t    header[2];
    char        *buffer;
    uint64_t    type;

    if(recv(_socket, (char*)header, sizeof(uint64_t)*2, MSG_WAITALL) != sizeof(uint64_t)*2)
        return 0;
    else {
        type = header[0];
        if(type != _type) {
            *buf_size = 0;
            if(type == 4) {
                uint32_t string_size = (uint32_t)header[1];
                if(string_size) {
                    buffer = MEM_mallocN(string_size, "error msg");

                    if(recv(_socket, buffer, string_size, MSG_WAITALL) == string_size) {
                        fprintf(stderr, "Octane: ERROR getting LiveDB material.");
                        if(strlen(buffer+1) > 0) fprintf(stderr, " Server response:\n%s\n", buffer+1);
                        else fprintf(stderr, "\n");
                    }

                    MEM_freeN(buffer);
                }
            }
            return 0;
        }
        else *buf_size = (uint32_t)header[1];
    }

    if(*buf_size) {
        buffer = MEM_mallocN(*buf_size, "ldb tree");

        if(recv(_socket, buffer, *buf_size, MSG_WAITALL) != *buf_size) {
            *buf_size = 0;
            MEM_freeN(buffer);
            return 0;
        }
    }
    else return 0;

    return buffer;
} /* mat_livedb_receive() */



/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get serialized LiveDB tree buffer from server. Responsibility of caller to free it. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
LiveDbItem* mat_livedb_get_tree(const char *address, uint32_t *buf_size)
{
    int         cur_socket;
    LiveDbItem  *buf;

    cur_socket = mat_livedb_connect(address);
    if(cur_socket < 0) {
        *buf_size = 0;
        return 0;
    }

    if(!mat_livedb_request(cur_socket, GET_LDB_CAT)) {
        *buf_size = 0;
        mat_livedb_disconnect(cur_socket);
        return 0;
    }

    buf = mat_livedb_receive(cur_socket, GET_LDB_CAT, buf_size);

    mat_livedb_disconnect(cur_socket);

    if(!buf) return 0;
    else if(!*buf_size) {
        MEM_freeN(buf);
        return 0;
    }
    else return buf;
} /* mat_livedb_get_tree() */

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get material preview image buffer from LiveDB. Responsibility of caller to free it. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
unsigned char* mat_livedb_get_mat_preview(const char *address, int32_t id, unsigned int *width, unsigned int *height, const char *_file_path)
{
    long            file_size;
    int             cur_socket;
    unsigned char   *buf = 0, *img_buf = 0;
    FILE            *hFile;
    char            file_path[FILE_MAX];

    /* create file path */
    snprintf(file_path, FILE_MAX, "%s%d.raw", _file_path, id);

    hFile = BLI_fopen(file_path, "rb");
    if(hFile) {
        fseek(hFile, 0, SEEK_END);
        file_size = ftell(hFile);
        rewind(hFile);

        img_buf = MEM_mallocN(file_size, "ldb preview");
        if(!img_buf) return 0;

        if(fread(img_buf, file_size, 1, hFile))
            *width = *height = (unsigned int)sqrtf(file_size / 4);
        else {
            MEM_freeN(img_buf);
            buf         = 0;
            file_size   = 0;
        }
        fclose(hFile);
    }
    else {
        img_buf     = 0;
        file_size   = 0;
    }

    if(!img_buf) {
        uint32_t buf_size;

        cur_socket = mat_livedb_connect(address);
        if(cur_socket < 0) return 0;

        if(!mat_livedb_request_preview(cur_socket, id)) {
            mat_livedb_disconnect(cur_socket);
            return 0;
        }

        buf = mat_livedb_receive(cur_socket, GET_LDB_MAT_PREVIEW, &buf_size);

        mat_livedb_disconnect(cur_socket);

        if(!buf || !buf_size) {
            if(buf) MEM_freeN(buf);
            *width = *height = 0;
            return 0;
        }
        else {
            *width   = ((uint32_t*)buf)[0];
            *height  = ((uint32_t*)buf)[1];

            file_size = *width * *height * 4;
            img_buf = MEM_mallocN(file_size, "ldb preview");
            if(!img_buf) {
                MEM_freeN(buf);
                *width = *height = 0;
                return 0;
            }
            memcpy(img_buf, buf + sizeof(uint32_t) * 2, file_size);
            MEM_freeN(buf);

            hFile = BLI_fopen(file_path, "wb");
            if(hFile) {
                if(!fwrite(img_buf, file_size, 1, hFile)) {
                    fclose(hFile);
                    MEM_freeN(img_buf);
                    *width = *height = 0;
                    return 0;
                }
                fclose(hFile);
            }
            else {
                MEM_freeN(img_buf);
                *width = *height = 0;
                return 0;
            }
        }
    }
    return img_buf;
} //mat_livedb_get_mat_preview()

/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
/* Get serialized material from LiveDB. */
/* /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */
MatItem* mat_livedb_get_material(const char *address, int32_t mat_id, uint32_t *buf_size)
{
    int     cur_socket;
    MatItem *buf;

    cur_socket = mat_livedb_connect(address);
    if(!cur_socket) {
        *buf_size = 0;
        return 0;
    }

    if(!mat_livedb_request_material(cur_socket, mat_id)) {
        *buf_size = 0;
        mat_livedb_disconnect(cur_socket);
        return 0;
    }

    buf = mat_livedb_receive(cur_socket, GET_LDB_MAT, buf_size);

    mat_livedb_disconnect(cur_socket);

    if(!buf) return 0;
    else if(!*buf_size) {
        MEM_freeN(buf);
        return 0;
    }
    else return buf;
} /* mat_livedb_get_material() */
