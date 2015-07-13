/*
 * Copyright 2011, Blender Foundation.
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
 */

#ifndef __SERVER_H__
#define __SERVER_H__

#ifndef OCTANE_SERVER_MAJOR_VERSION
#   define OCTANE_SERVER_MAJOR_VERSION 9
#endif
#ifndef OCTANE_SERVER_MINOR_VERSION
#   define OCTANE_SERVER_MINOR_VERSION 0
#endif
#define OCTANE_SERVER_VERSION_NUMBER (((OCTANE_SERVER_MAJOR_VERSION & 0x0000FFFF) << 16) | (OCTANE_SERVER_MINOR_VERSION & 0x0000FFFF))

#define SEND_CHUNK_SIZE     67108864

#if !defined(__APPLE__)
#  undef htonl
#  undef ntohl
#endif

#ifndef WIN32
#  include <unistd.h> // for read close
#  include <sys/types.h>
#  include <sys/socket.h>
#  include <netinet/ip.h>
#  include <netdb.h>
#  if defined(__APPLE__)
#    include <arpa/inet.h>
#  endif
#else
#  include "winsock2.h"
#  include <io.h> // for open close read
#endif

#undef max
#undef min

#pragma push_macro("htonl")
#define htonl 1
#pragma push_macro("ntohl")
#define ntohl 1

#include "camera.h"
#include "nodes.h"
#include "passes.h"
#include "kernel.h"
#include "server.h"
#include "buffers.h"
#include "environment.h"

#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

#include "util_string.h"
#include "util_thread.h"
#include "util_types.h"
#include "util_lists.h"
#include "util_progress.h"
#include "blender_util.h"

#include "nodes.h"
#include "blender_session.h"

#pragma pop_macro("htonl")
#pragma pop_macro("ntohl")

#include "BLI_math_color.h"
#include "BLI_fileops.h"
#include "DNA_ID.h"

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

using std::cout;
using std::exception;

static const int SERVER_PORT = 5130;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
enum PacketType {
    NONE = 0,

    GET_LDB_CAT,
    GET_LDB_MAT_PREVIEW,
    GET_LDB_MAT,

    ERROR_PACKET,
    DESCRIPTION,
    SET_LIC_DATA,
    RESET,
    CLEAR,
    START,
    STOP,
    START_FRAME_LOAD,
    FINISH_FRAME_LOAD,
    UPDATE,
    PAUSE,
    GET_IMAGE,
    GET_SAMPLES,

    LOAD_GPU,
    LOAD_PASSES,
    LOAD_KERNEL,
    LOAD_RENDER_REGION,
    LOAD_THIN_LENS_CAMERA,
    LOAD_PANORAMIC_CAMERA,
    //LOAD_IMAGER,
    //LOAD_POSTPROCESSOR,
    LOAD_SUNSKY,
    LOAD_FILE,

    FIRST_NAMED_PACKET,
    LOAD_GLOBAL_MESH = FIRST_NAMED_PACKET,
    DEL_GLOBAL_MESH,
    LOAD_LOCAL_MESH,
    DEL_LOCAL_MESH,
    LOAD_GEO_MAT,
    DEL_GEO_MAT,
    LOAD_GEO_SCATTER,
    DEL_GEO_SCATTER,
    LOAD_IMAGE_FILE,

    LOAD_MATERIAL_FIRST,
    LOAD_DIFFUSE_MATERIAL = LOAD_MATERIAL_FIRST,
    LOAD_GLOSSY_MATERIAL,
    LOAD_SPECULAR_MATERIAL,
    LOAD_MIX_MATERIAL,
    LOAD_PORTAL_MATERIAL,
    LOAD_MATERIAL_LAST = LOAD_PORTAL_MATERIAL,
    DEL_MATERIAL,

    LOAD_TEXTURE_FIRST,
    LOAD_FLOAT_TEXTURE = LOAD_TEXTURE_FIRST,
    LOAD_RGB_SPECTRUM_TEXTURE,
    LOAD_GAUSSIAN_SPECTRUM_TEXTURE,
    LOAD_CHECKS_TEXTURE,
    LOAD_MARBLE_TEXTURE,
    LOAD_RIDGED_FRACTAL_TEXTURE,
    LOAD_SAW_WAVE_TEXTURE,
    LOAD_SINE_WAVE_TEXTURE,
    LOAD_TRIANGLE_WAVE_TEXTURE,
    LOAD_TURBULENCE_TEXTURE,
    LOAD_CLAMP_TEXTURE,
    LOAD_COSINE_MIX_TEXTURE,
    LOAD_INVERT_TEXTURE,
    LOAD_MIX_TEXTURE,
    LOAD_MULTIPLY_TEXTURE,
    LOAD_IMAGE_TEXTURE,
    LOAD_IMAGE_TEXTURE_DATA,
    LOAD_ALPHA_IMAGE_TEXTURE,
    LOAD_ALPHA_IMAGE_TEXTURE_DATA,
    LOAD_FLOAT_IMAGE_TEXTURE,
    LOAD_FLOAT_IMAGE_TEXTURE_DATA,
    LOAD_FALLOFF_TEXTURE,
    LOAD_COLOR_CORRECT_TEXTURE,
    LOAD_DIRT_TEXTURE,
    LOAD_GRADIENT_TEXTURE,
    LOAD_DISPLACEMENT_TEXTURE,
    LOAD_RANDOM_COLOR_TEXTURE,
    LOAD_POLYGON_SIDE_TEXTURE,
    LOAD_NOISE_TEXTURE,
    LOAD_TEXTURE_LAST = LOAD_NOISE_TEXTURE,
    DEL_TEXTURE,

    LOAD_EMISSION_FIRST,
    LOAD_BLACKBODY_EMISSION = LOAD_EMISSION_FIRST,
    LOAD_TEXTURE_EMISSION,
    LOAD_EMISSION_LAST = LOAD_TEXTURE_EMISSION,
    DEL_EMISSION,

    LOAD_TRANSFORM_FIRST,
    LOAD_SCALE_TRANSFORM = LOAD_TRANSFORM_FIRST,
    LOAD_ROTATION_TRANSFORM,
    LOAD_FULL_TRANSFORM,
    LOAD_2D_TRANSFORM,
    LOAD_3D_TRANSFORM,
    LOAD_TRANSFORM_LAST = LOAD_3D_TRANSFORM,
    DEL_TRANSFORM,

    LOAD_MEDIUM_FIRST,
    LOAD_ABSORPTION_MEDIUM = LOAD_MEDIUM_FIRST,
    LOAD_SCATTERING_MEDIUM,
    LOAD_MEDIUM_LAST = LOAD_SCATTERING_MEDIUM,
    DEL_MEDIUM,

    LOAD_PROJECTION_FIRST,
    LOAD_PROJECTION_XYZ = LOAD_PROJECTION_FIRST,
    LOAD_PROJECTION_BOX,
    LOAD_PROJECTION_CYL,
    LOAD_PROJECTION_PERSP,
    LOAD_PROJECTION_SPHERICAL,
    LOAD_PROJECTION_UVW,
    LOAD_PROJECTION_LAST = LOAD_PROJECTION_UVW,
    DEL_PROJECTION,

    LOAD_VALUE_FIRST,
    LOAD_VALUE_FLOAT = LOAD_VALUE_FIRST,
    LOAD_VALUE_INT,
    LOAD_VALUE_LAST = LOAD_VALUE_INT,
    DEL_VALUE,

    LAST_NAMED_PACKET = DEL_VALUE,

    LAST_PACKET_TYPE = LAST_NAMED_PACKET
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Send data class
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef struct RPCSend {
    RPCSend(int socket_, uint64_t buf_size_, PacketType type_, const char* szName = 0) : type(type_), socket(socket_), buf_pointer(0) {
        buf_size = buf_size_ + sizeof(uint64_t)*2;
        size_t name_len, name_buf_len;

        if(szName) {
            name_len = strlen(szName);
            if(name_len > 245) name_len = 245;
            name_buf_len = name_len+1+1;
            name_buf_len += sizeof(uint64_t) - name_buf_len%sizeof(uint64_t);
            buf_size += name_buf_len;
        }
        else {
            name_len = 0;
            name_buf_len = 0;
        }
        buf_pointer = buffer = new uint8_t[buf_size];

        *reinterpret_cast<uint64_t*>(buf_pointer) = static_cast<uint64_t>(type_);
        buf_pointer += sizeof(uint64_t);
        *reinterpret_cast<uint64_t*>(buf_pointer) = buf_size - sizeof(uint64_t)*2;
        buf_pointer += sizeof(uint64_t);
        if(szName) {
            *reinterpret_cast<uint8_t*>(buf_pointer) = static_cast<uint8_t>(name_buf_len);
#ifndef WIN32
            strncpy(reinterpret_cast<char*>(buf_pointer+1), szName, name_len+1);
#else
            strncpy_s(reinterpret_cast<char*>(buf_pointer+1), name_len+1, szName, name_len);
#endif
            buf_pointer += name_buf_len;
        }
    }
    ~RPCSend() {
        if(buffer) delete[] buffer;
    }

    inline RPCSend& operator<<(float& val) {
        if(buffer && (buf_pointer+sizeof(float) <= buffer+buf_size)) {
            *reinterpret_cast<float*>(buf_pointer) = val;
            buf_pointer += sizeof(float);
        }
        return *this;
    }

    inline RPCSend& operator<<(float3& val) {
        if(buffer && (buf_pointer+sizeof(float3) <= buffer+buf_size)) {
            *reinterpret_cast<float3*>(buf_pointer) = val;
            buf_pointer += sizeof(float3);
        }
        return *this;
    }

    inline RPCSend& operator<<(double& val) {
        if(buffer && (buf_pointer+sizeof(double) <= buffer+buf_size)) {
            *reinterpret_cast<double*>(buf_pointer) = val;
            buf_pointer += sizeof(double);
        }
        return *this;
    }

    inline RPCSend& operator<<(int64_t& val) {
        if(buffer && (buf_pointer+sizeof(int64_t) <= buffer+buf_size)) {
            *reinterpret_cast<int64_t*>(buf_pointer) = val;
            buf_pointer += sizeof(int64_t);
        }
        return *this;
    }

    inline RPCSend& operator<<(uint64_t& val) {
        if(buffer && (buf_pointer+sizeof(uint64_t) <= buffer+buf_size)) {
            *reinterpret_cast<uint64_t*>(buf_pointer) = val;
            buf_pointer += sizeof(uint64_t);
        }
        return *this;
    }

    inline RPCSend& operator<<(uint32_t& val) {
        if(buffer && (buf_pointer+sizeof(uint32_t) <= buffer+buf_size)) {
            *reinterpret_cast<uint32_t*>(buf_pointer) = val;
            buf_pointer += sizeof(uint32_t);
        }
        return *this;
    }

    inline RPCSend& operator<<(int32_t& val) {
        if(buffer && (buf_pointer+sizeof(int32_t) <= buffer+buf_size)) {
            *reinterpret_cast<int32_t*>(buf_pointer) = val;
            buf_pointer += sizeof(int32_t);
        }
        return *this;
    }

    inline RPCSend& operator<<(bool& val) {
        if(buffer && (buf_pointer+sizeof(int32_t) <= buffer+buf_size)) {
            *reinterpret_cast<uint32_t*>(buf_pointer) = val;
            buf_pointer += sizeof(uint32_t);
        }
        return *this;
    }

    inline RPCSend& operator<<(char* val) {
        if(buffer) {
            size_t len = strlen(val);
            if(buf_pointer+len+2 > buffer+buf_size) return *this;
            if(len > 4096) len = 4096;
            *reinterpret_cast<uint8_t*>(buf_pointer) = static_cast<uint8_t>(len);
            buf_pointer += sizeof(uint8_t);
#ifndef WIN32
            strncpy(reinterpret_cast<char*>(buf_pointer), val, len+1);
#else
            strncpy_s(reinterpret_cast<char*>(buf_pointer), len+1, val, len);
#endif
            buf_pointer += len+1;
        }
        return *this;
    }

    inline RPCSend& operator<<(const char* val) {
        if(!val) return this->operator<<("");
        else return this->operator<<(const_cast<char*>(val));
    }

    inline RPCSend& operator<<(string& val) {
        return this->operator<<(val.c_str());
    }

    bool write_buffer(void* buf, uint64_t len) {
        if(buffer && (buf_pointer+len <= buffer+buf_size)) {
            memcpy(buf_pointer, buf, static_cast<size_t>(len));
            buf_pointer += len;
            return true;
        }
        else return false;
    }

    bool write_float3_buffer(float3* buf, uint64_t len) {
        if(buffer && (buf_pointer + len*sizeof(float)*3 <= buffer+buf_size)) {
            register float* ptr = (float*)buf_pointer;
            for(register uint64_t i=0; i<len; ++i) {
                *(ptr++) = buf[i].x;
                *(ptr++) = buf[i].y;
                *(ptr++) = buf[i].z;
            }
            buf_pointer = (uint8_t*)ptr;
            return true;
        }
        else return false;
    }

    bool write_float2_buffer(float2* buf, uint64_t len) {
        if(buffer && (buf_pointer + len*sizeof(float) * 2 <= buffer + buf_size)) {
            register float* ptr = (float*)buf_pointer;
            for(register uint64_t i = 0; i < len; ++i) {
                *(ptr++) = buf[i].x;
                *(ptr++) = buf[i].y;
            }
            buf_pointer = (uint8_t*)ptr;
            return true;
        }
        else return false;
    }

    bool write() {
        if(!buffer) return false;

        unsigned int header_size = sizeof(uint64_t) * 2;
        if(::send(socket, (const char*)buffer, header_size, 0) < 0)
            return false;

        uint64_t data_buf_size          = buf_size - header_size;
        unsigned int chunks_cnt         = static_cast<unsigned int>(data_buf_size / SEND_CHUNK_SIZE);
        unsigned int last_chunk_size    = data_buf_size % SEND_CHUNK_SIZE;
        for(unsigned int i=0; i < chunks_cnt; ++i) {
            if(::send(socket, (const char*)buffer + header_size + i * SEND_CHUNK_SIZE, SEND_CHUNK_SIZE, 0) < 0) {
                return false;
            }
        }
        if(last_chunk_size && ::send(socket, (const char*)buffer + header_size + chunks_cnt * SEND_CHUNK_SIZE, last_chunk_size, 0) < 0)
            return false;

        delete[] buffer;
        buffer      = 0;
        buf_size    = 0;
        buf_pointer = 0;

        return true;
    }

    inline bool write_file(string &path) {
        if(!buffer || !buf_size || !path.length()) return false;
        bool ret = false;
        uint8_t *buf = 0;
        int64_t file_size = 0;

        FILE *hFile = BLI_fopen(path.c_str(), "rb");
        if(!hFile) goto exit3;
#ifndef WIN32
    	    fseek(hFile, 0, SEEK_END);
    	    file_size = ftell(hFile);
#else
    	    _fseeki64(hFile, 0, SEEK_END);
    	    file_size = _ftelli64(hFile);
#endif
        rewind(hFile);

        reinterpret_cast<uint64_t*>(buffer)[1] = file_size;
        if(::send(socket, (const char*)buffer, sizeof(uint64_t) * 2, 0) < 0)
            goto exit2;

        buf = new uint8_t[file_size > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : file_size];
        while(buf && file_size) {
            unsigned int size_to_read = (file_size > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : file_size);

            if(!fread(buf, size_to_read, 1, hFile))
                goto exit1;

            if(::send(socket, (const char*)buf, size_to_read, 0) < 0)
                goto exit1;

            file_size -= size_to_read;
        }
        ret = true;
exit1:
        if(buf) delete[] buf;
exit2:
        fclose(hFile);
exit3:
        delete[] buffer;
        buf_pointer = buffer = 0;
        type = NONE;
        buf_size = 0;

        return ret;
    }

private:
    RPCSend() {}

    PacketType  type;
    int         socket;
    uint8_t     *buffer;
    uint64_t    buf_size;
    uint8_t     *buf_pointer;
} RPCSend;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Receive data class
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typedef struct RPCReceive {
    RPCReceive(int socket_) : socket(socket_), buffer(0), buf_pointer(0) {
        uint64_t uiTmp[2];
        if(::recv(socket_, (char*)uiTmp, sizeof(uint64_t)* 2, MSG_WAITALL) != sizeof(uint64_t)* 2) {
            type = NONE;
            buf_size = 0;
            return;
        }
        else {
            type = static_cast<PacketType>(uiTmp[0]);
            buf_size = uiTmp[1];
        }

        if(buf_size > 0) {
            unsigned int chunks_cnt = static_cast<unsigned int>(buf_size / SEND_CHUNK_SIZE);
            int last_chunk_size = static_cast<int>(buf_size % SEND_CHUNK_SIZE);

            if(type == LOAD_FILE) {
                buf_pointer = buffer = new uint8_t[buf_size > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : buf_size];
                if(!buffer) {
                    delete[] buffer;
                    buf_pointer = buffer = 0;
                    type = NONE;
                    buf_size = 0;
                    return;
                }
            }
            else {
                buf_pointer = buffer = new uint8_t[buf_size];
                for(unsigned int i = 0; i < chunks_cnt; ++i) {
                    if(::recv(socket_, (char*)buffer + i * SEND_CHUNK_SIZE, SEND_CHUNK_SIZE, MSG_WAITALL) != SEND_CHUNK_SIZE) {
                        delete[] buffer;
                        buf_pointer = buffer = 0;
                        type = NONE;
                        buf_size = 0;
                        return;
                    }
                }
                if(last_chunk_size && ::recv(socket_, (char*)buffer + chunks_cnt * SEND_CHUNK_SIZE, last_chunk_size, MSG_WAITALL) != last_chunk_size) {
                    delete[] buffer;
                    buf_pointer = buffer = 0;
                    type = NONE;
                    buf_size = 0;
                    return;
                }
            }
        }
        if(buffer && type >= FIRST_NAMED_PACKET && type <= LAST_NAMED_PACKET) {
            uint8_t len = *reinterpret_cast<uint8_t*>(buf_pointer);
            //buf_pointer += sizeof(uint8_t);

            name = reinterpret_cast<char*>(buf_pointer + 1);
            buf_pointer += len;
            //buf_size -= len;
        }
    }

    ~RPCReceive() {
        if(buffer) delete[] buffer;
    }

    inline bool read_file(std::string &path, int *err) {
        *err = 0;
        if(!buffer || !buf_size || !path.length()) return false;

        if(path[path.length() - 1] == '/' || path[path.length() - 1] == '\\')
            path.operator+=(name);

        FILE *hFile = BLI_fopen(path.c_str(), "wb");
        if(!hFile) {
            *err = errno;
            return false;
        }

        uint64_t cur_size = buf_size;
        while(cur_size) {
            int size_to_read = (cur_size > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : static_cast<int>(cur_size));
            if(::recv(socket, (char*)buffer, size_to_read, MSG_WAITALL) != size_to_read) {
                *err = errno;
                fclose(hFile);
                delete[] buffer;
                buf_pointer = buffer = 0;
                type = NONE;
                buf_size = 0;
                return false;
            }
            fwrite(buffer, size_to_read, 1, hFile);
            cur_size -= size_to_read;
        }
        delete[] buffer;
        buf_pointer = buffer = 0;
        type = NONE;
        buf_size = 0;
        fclose(hFile);

        return true;
    }

    inline RPCReceive& operator>>(float& val) {
        if(buffer && (buf_pointer+sizeof(float) <= buffer+buf_size)) {
            val = *reinterpret_cast<float*>(buf_pointer);
            buf_pointer += sizeof(float);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(double& val) {
        if(buffer && (buf_pointer+sizeof(double) <= buffer+buf_size)) {
            val = *reinterpret_cast<double*>(buf_pointer);
            buf_pointer += sizeof(double);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(bool& val) {
        if(buffer && (buf_pointer+sizeof(uint32_t) <= buffer+buf_size)) {
            val = (*reinterpret_cast<uint32_t*>(buf_pointer) != 0);
            buf_pointer += sizeof(uint32_t);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(int64_t& val) {
        if(buffer && (buf_pointer+sizeof(int64_t) <= buffer+buf_size)) {
            val = *reinterpret_cast<int64_t*>(buf_pointer);
            buf_pointer += sizeof(int64_t);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(uint64_t& val) {
        if(buffer && (buf_pointer+sizeof(uint64_t) <= buffer+buf_size)) {
            val = *reinterpret_cast<uint64_t*>(buf_pointer);
            buf_pointer += sizeof(uint64_t);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(uint32_t& val) {
        if(buffer && (buf_pointer+sizeof(uint32_t) <= buffer+buf_size)) {
            val = *reinterpret_cast<uint32_t*>(buf_pointer);
            buf_pointer += sizeof(uint32_t);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(int32_t& val) {
        if(buffer && (buf_pointer+sizeof(int32_t) <= buffer+buf_size)) {
            val = *reinterpret_cast<int32_t*>(buf_pointer);
            buf_pointer += sizeof(int32_t);
        }
        else val = 0;
        return *this;
    }

    inline RPCReceive& operator>>(char*& val) {
        if(buffer && (buf_pointer+1 <= buffer+buf_size)) {
            uint8_t len = *reinterpret_cast<uint8_t*>(buf_pointer);
            buf_pointer += sizeof(uint8_t);
            if(buf_pointer+len+1 > buffer+buf_size) {
                val = "";
                return *this;
            }
            val = reinterpret_cast<char*>(buf_pointer);
            buf_pointer += len+1;
        }
        else val = "";
        return *this;
    }

    inline RPCReceive& operator>>(string& val) {
        if(buffer && (buf_pointer+1 <= buffer+buf_size)) {
            uint8_t len = *reinterpret_cast<uint8_t*>(buf_pointer);
            buf_pointer += sizeof(uint8_t);
            if(buf_pointer+len+1 > buffer+buf_size) {
                val = "";
                return *this;
            }
            val = reinterpret_cast<char*>(buf_pointer);
            buf_pointer += len+1;
        }
        else val = "";
        return *this;
    }

    void* read_buffer(uint64_t len) {
        if(buffer && (buf_pointer+len <= buffer+buf_size)) {
            void* ret = reinterpret_cast<void*>(buf_pointer);
            buf_pointer += len;
            return ret;
        }
        else return 0;
    }

    int         socket;
    PacketType  type;
    char*       name;

private:
    RPCReceive() {}

    uint8_t  *buffer;
    uint64_t buf_size;
    uint8_t  *buf_pointer;
} RPCReceive;



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render Server info structures
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class RenderServerInfo {
public:
	string  description;
	bool    pack_images;
    char    net_address[256];

	RenderServerInfo() {
		pack_images = false;
        ::strcpy(net_address, "127.0.0.1");
	}
}; //RenderServerInfo

class ImageStatistics {
public:
    uint32_t cur_samples;
    uint64_t used_vram, free_vram, total_vram;
    float spp;
    uint32_t tri_cnt, meshes_cnt;
    uint32_t rgb32_cnt, rgb64_cnt, grey8_cnt, grey16_cnt;
    uint32_t net_gpus, used_net_gpus;
    int32_t expiry_time;
}; //ImageStatistics

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render Server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class RenderServer {
    uint8_t*            image_buf;
    float*              float_img_buf;

    int32_t     cur_w, cur_h, cur_reg_w, cur_reg_h;
    uint32_t    m_Export_alembic;
    bool        m_bInteractive;
    bool        unpacked_msg;

protected:
	RenderServer() {}

	string error_msg;

public:
    enum fail_reasons {
        NONE = -1,
        UNKNOWN,
        WRONG_VERSION,
        NO_CONNECTION,
        NOT_ACTIVATED
    };

    Passes::PassTypes   cur_pass_type;

    static char         address[256];
    static char         out_path[256];
    thread_mutex        socket_mutex;
    thread_mutex        img_buf_mutex;
	RenderServerInfo    info;
    fail_reasons        fail_reason;

    int socket;

    // Create the render-server object, connected to the server
    // addr - server address
    RenderServer(const char *addr, const char *_out_path, bool export_alembic, bool interactive) : image_buf(0), float_img_buf(0), cur_w(0), cur_h(0), cur_reg_w(0), cur_reg_h(0), socket(-1),
                                                                                                   m_Export_alembic(export_alembic), m_bInteractive(interactive), fail_reason(NONE), cur_pass_type(Passes::PASS_NONE) {
        struct  hostent *host;
        struct  sockaddr_in sa;

        strcpy(out_path, _out_path);

        strcpy(address, addr);
        host = gethostbyname(addr);
        if(!host || host->h_length != sizeof(struct in_addr)) {
            throw exception();
        }
        socket = ::socket(AF_INET, SOCK_STREAM, 0);
        if(socket < 0) throw exception();

        memset(&sa, 0, sizeof(sa));
        sa.sin_family = AF_INET;
        sa.sin_port = htons(0);
        sa.sin_addr.s_addr = htonl(INADDR_ANY);
        if(::bind(socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
            close(socket);
#else
            closesocket(socket);
#endif
            throw exception();
        }
        sa.sin_port = htons(SERVER_PORT);
        sa.sin_addr = *(struct in_addr*) host->h_addr;
        if(::connect(socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
            close(socket);
#else
            closesocket(socket);
#endif
            fail_reason = NO_CONNECTION;
            socket = -1;
        }
    } //RenderServer()

    ~RenderServer() {
        if(m_bInteractive) clear();

        if(socket >= 0)
#ifndef WIN32
            close(socket);
#else
            closesocket(socket);
#endif
        if(image_buf) delete[] image_buf;
        if(float_img_buf) delete[] float_img_buf;
    } //~RenderServer()

    // Get the last error message
	inline const string& error_message() {
        return error_msg;
    } //error_message()

	inline void clear_error_message() {
        error_msg.clear();
    } //clear_error_message()



    // Get server compatibility
    inline bool check_server_version() {
        if(socket < 0) return false;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, 0, DESCRIPTION);
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != DESCRIPTION) {
            fail_reason = UNKNOWN;

            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR getting render-server version.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
            return false;
        }
        else {
            uint32_t maj_num, min_num;
            bool active;
            rcv >> maj_num >> min_num >> active;

            if(maj_num != OCTANE_SERVER_MAJOR_VERSION || min_num != OCTANE_SERVER_MINOR_VERSION) {
                fail_reason = WRONG_VERSION;
                fprintf(stderr, "Octane: ERROR: Wrong version of render-server (%d.%d), %d.%d is needed\n",
                        maj_num, min_num, OCTANE_SERVER_MAJOR_VERSION, OCTANE_SERVER_MINOR_VERSION);

                if(socket >= 0)
#ifndef WIN32
                    close(socket);
#else
                    closesocket(socket);
#endif
                socket = -1;
                return false;
            }
            else if(!active) {
                fail_reason = NOT_ACTIVATED;
                fprintf(stderr, "Octane: ERROR: server license is not activated.\n");

                if(socket >= 0)
#ifndef WIN32
                    close(socket);
#else
                    closesocket(socket);
#endif
                socket = -1;
                return false;
            }
            else {
                fail_reason = NONE;
                return true;
            }
        }
    } //check_server_version()

    // Activate the Octane license on server
    inline int activate(string& sStandLogin, string& sStandPass, string& sLogin, string& sPass) {
        if(socket < 0) return 0;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, sStandLogin.length()+2 + sStandPass.length()+2 + sLogin.length()+2 + sPass.length()+2, SET_LIC_DATA);
        snd << sStandLogin << sStandPass << sLogin << sPass;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != SET_LIC_DATA) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR of the license activation on render-server.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
            return 0;
        }
        else return 1;
    } //activate()

    // Reset the server project (SOFT reset).
    // GPUs - the GPUs which should be used by server, as bit map
    inline void reset(uint32_t GPUs, float frame_time_sampling) {
        if(socket < 0) return;

        unpacked_msg = false;

        thread_scoped_lock socket_lock(socket_mutex);

        int path_len = m_Export_alembic ? strlen(out_path) : 0;

        RPCSend snd(socket, sizeof(float) + sizeof(uint32_t) * 2 + path_len + 2, RESET);
        snd << frame_time_sampling << GPUs << m_Export_alembic;
        if(m_Export_alembic) snd << out_path;

        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != RESET) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR resetting render server.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //reset()

    // Clear the server project.
    inline void clear() {
        if(socket < 0) return;

        unpacked_msg = false;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, 0, CLEAR);
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != CLEAR) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR clearing render server.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //clear()

    // GPUs - the GPUs which should be used by server, as bit map
    inline void load_GPUs(uint32_t GPUs) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, sizeof(uint32_t), LOAD_GPU);
        snd << GPUs;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != LOAD_GPU) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR setting GPUs on render server.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //load_GPUs()

    // Update current render project on the server.
    inline bool update() {
        if(socket < 0) return false;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, 0, UPDATE);
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != UPDATE) {
            return false;
        }
        else return true;
    } //update()

    // Start the render process on the server.
    // w - the width of the the rendered image needed 
    // h - the height of the the rendered image needed
    inline void start_render(int32_t w, int32_t h, uint32_t img_type, bool out_of_core_enabled, int32_t out_of_core_mem_limit, int32_t out_of_core_gpu_headroom) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, sizeof(int32_t) * 5 + sizeof(uint32_t), START);
        snd << out_of_core_enabled << out_of_core_mem_limit << out_of_core_gpu_headroom << w << h << img_type;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != START) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR starting render.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //start_render()

    // Stop the render process on the server.
    // Mostly needed to close the alembic animation sequence on the server.
    inline void stop_render(float fps) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, m_Export_alembic ? sizeof(float) : 0, STOP);
        if(m_Export_alembic) snd << fps;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != STOP) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR stopping render.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
        else if(m_Export_alembic && strlen(out_path)) {
            int err;
            RPCReceive rcv(socket);
            std::string s_out_path(out_path);
            
            if(rcv.type != LOAD_FILE) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR downloading alembic file from server.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
            else if(!rcv.read_file(s_out_path, &err)) {
                char *err_str;
                fprintf(stderr, "Octane: ERROR downloading alembic file from server.");
                if(err && (err_str = strerror(err)) && err_str[0]) fprintf(stderr, " Description: %s\n", err_str);
                else fprintf(stderr, "\n");
            }
        }
    } //stop_render()

    inline void pause_render(int32_t pause) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, sizeof(int32_t), PAUSE);
        snd << pause;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != PAUSE) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR pause render.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //pause_render()

    inline void start_frame_load() {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, 0, START_FRAME_LOAD);
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != START_FRAME_LOAD) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR starting frame load.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //start_frame_load()

    inline void finish_frame_load(bool update) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        RPCSend snd(socket, sizeof(int32_t), FINISH_FRAME_LOAD);
        snd << update;
        snd.write();

        RPCReceive rcv(socket);
        if(rcv.type != FINISH_FRAME_LOAD) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR finishing frame load.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //finish_frame_load()

    // Load camera to render server.
    // cam - camera data structure
    inline void load_camera(Camera* cam) {
        if(socket < 0 || cam->is_hidden) return;

        thread_scoped_lock socket_lock(socket_mutex);

        int32_t response_type       = static_cast<int32_t>(cam->response_type);
        int32_t min_display_samples = static_cast<int32_t>(cam->min_display_samples);
        int32_t glare_ray_count     = static_cast<int32_t>(cam->glare_ray_count);

        if(cam->type == CAMERA_PANORAMA) {
            {
                RPCSend snd(socket, sizeof(float3)*4 + sizeof(float)*25 + sizeof(int32_t)*9, LOAD_PANORAMIC_CAMERA);
                snd << cam->eye_point << cam->look_at << cam->up << cam->left_filter << cam->right_filter << cam->white_balance 

                    << cam->fov_x << cam->fov_y << cam->near_clip_depth << cam->exposure
                    << cam->gamma << cam->vignetting << cam->saturation << cam->hot_pix << cam->white_saturation
                    << cam->bloom_power << cam->glare_power << cam->glare_angle << cam->glare_blur << cam->spectral_shift << cam->spectral_intencity << cam->highlight_compression
                    << cam->blackout_lat << cam->stereo_dist << cam->stereo_dist_falloff

                    << cam->pan_type << response_type << min_display_samples << glare_ray_count << cam->stereo_out
                    
                    << cam->premultiplied_alpha << cam->dithering << cam->postprocess << cam->keep_upright;
                snd.write();
            }

            RPCReceive rcv(socket);
            if(rcv.type != LOAD_PANORAMIC_CAMERA) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR loading camera.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
        else {
            {
                RPCSend snd(socket, sizeof(float3)*6 + sizeof(float)*26 + sizeof(int32_t)*11, LOAD_THIN_LENS_CAMERA);
                snd << cam->eye_point << cam->look_at << cam->up << cam->left_filter << cam->right_filter << cam->white_balance 

                    << cam->aperture << cam->aperture_edge << cam->distortion << cam->focal_depth << cam->near_clip_depth << cam->lens_shift_x << cam->lens_shift_y
                    << cam->stereo_dist << cam->fov << cam->exposure << cam->gamma << cam->vignetting
                    << cam->saturation << cam->hot_pix << cam->white_saturation
                    << cam->bloom_power << cam->glare_power << cam->glare_angle << cam->glare_blur << cam->spectral_shift << cam->spectral_intencity << cam->highlight_compression
                    << cam->pixel_aspect << cam->aperture_aspect

                    << response_type << min_display_samples << glare_ray_count << cam->stereo_mode << cam->stereo_out

                    << cam->ortho << cam->autofocus
                    << cam->premultiplied_alpha << cam->dithering
                    << cam->postprocess << cam->persp_corr;
                snd.write();
            }

            RPCReceive rcv(socket);
            if(rcv.type != LOAD_THIN_LENS_CAMERA) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR loading camera.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //load_camera()

    // Load passes to render server.
    // passes - passes data structure
    // interactive - current rendering mode
    void load_passes(Passes* passes, bool interactive) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        {
            RPCSend snd(socket, sizeof(float)*5 + sizeof(int32_t)*46, LOAD_PASSES);
            uint32_t cur_pass_type = static_cast<uint32_t>(passes->cur_pass_type);
            snd << passes->pass_filter_size << passes->pass_z_depth_max << passes->pass_uv_max << passes->pass_max_speed << passes->pass_ao_distance
                << passes->use_passes << cur_pass_type << passes->pass_max_samples << passes->pass_ao_max_samples << passes->pass_distributed_tracing << passes->pass_alpha_shadows

                << passes->combined_pass << passes->emitters_pass << passes->environment_pass << passes->diffuse_direct_pass << passes->diffuse_indirect_pass << passes->reflection_direct_pass << passes->reflection_indirect_pass
                << passes->refraction_pass << passes->transmission_pass << passes->subsurf_scattering_pass << passes->post_processing_pass

                << passes->geom_normals_pass << passes->shading_normals_pass << passes->vertex_normals_pass << passes->position_pass << passes->z_depth_pass << passes->material_id_pass << passes->uv_coordinates_pass
                << passes->tangents_pass << passes->wireframe_pass << passes->object_id_pass << passes->ao_pass << passes->motion_vector_pass
                << passes->layer_shadows_pass << passes->layer_black_shadows_pass << passes->layer_color_shadows_pass << passes->layer_reflections_pass
                << passes->layer_id_pass << passes->layer_mask_pass
                << passes->light_pass_id_pass
                << passes->ambient_light_pass << passes->sunlight_pass << passes->light1_pass << passes->light2_pass << passes->light3_pass
                << passes->light4_pass << passes->light5_pass << passes->light6_pass << passes->light7_pass << passes->light8_pass;
            snd.write();
        }

        RPCReceive rcv(socket);
        if(rcv.type != LOAD_PASSES) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR loading render passes.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //load_passes()

    // Load kernel to render server.
    // kernel - kernel data structure
    // interactive - Max. Samples will be set according to mode choosen
    void load_kernel(Kernel* kernel, bool interactive) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        int32_t kernel_type = static_cast<int32_t>(kernel->kernel_type);
        switch(kernel->kernel_type) {
        case Kernel::DIRECT_LIGHT:
        {
            RPCSend snd(socket, sizeof(float) * 6 + sizeof(int32_t) * 13, LOAD_KERNEL);
            int32_t gi_mode = static_cast<int32_t>(kernel->gi_mode);
            snd << kernel_type << (interactive ? kernel->max_preview_samples : kernel->max_samples) << kernel->shuttertime << kernel->filter_size << kernel->ray_epsilon << kernel->path_term_power << kernel->coherent_ratio << kernel->ao_dist
                << kernel->alpha_channel << kernel->alpha_shadows << kernel->static_noise << kernel->keep_environment
                << kernel->specular_depth << kernel->glossy_depth << gi_mode << kernel->diffuse_depth << kernel->layers_enable << kernel->layers_current << kernel->layers_invert;
            snd.write();
        }
            break;
        case Kernel::PATH_TRACE:
        {
            RPCSend snd(socket, sizeof(float) * 7 + sizeof(int32_t) * 11, LOAD_KERNEL);
            snd << kernel_type << (interactive ? kernel->max_preview_samples : kernel->max_samples) << kernel->shuttertime << kernel->filter_size << kernel->ray_epsilon << kernel->path_term_power << kernel->coherent_ratio << kernel->caustic_blur << kernel->gi_clamp
                << kernel->alpha_channel << kernel->alpha_shadows << kernel->static_noise << kernel->keep_environment
                << kernel->max_diffuse_depth << kernel->max_glossy_depth << kernel->layers_enable << kernel->layers_current << kernel->layers_invert;
            snd.write();
        }
            break;
        case Kernel::PMC:
        {
            RPCSend snd(socket, sizeof(float) * 8 + sizeof(int32_t) * 12, LOAD_KERNEL);
            snd << kernel_type << (interactive ? kernel->max_preview_samples : kernel->max_samples) << kernel->shuttertime << kernel->filter_size << kernel->ray_epsilon << kernel->path_term_power << kernel->exploration << kernel->direct_light_importance << kernel->caustic_blur << kernel->gi_clamp
                << kernel->alpha_channel << kernel->alpha_shadows << kernel->keep_environment
                << kernel->max_diffuse_depth << kernel->max_glossy_depth << kernel->max_rejects << kernel->parallelism << kernel->layers_enable << kernel->layers_current << kernel->layers_invert;
            snd.write();
        }
            break;
        case Kernel::INFO_CHANNEL:
        {
            RPCSend snd(socket, sizeof(float) * 7 + sizeof(int32_t) * 11, LOAD_KERNEL);
            int32_t info_channel_type = static_cast<int32_t>(kernel->info_channel_type);
            snd << kernel_type << info_channel_type << kernel->shuttertime << kernel->filter_size << kernel->zdepth_max << kernel->uv_max << kernel->ray_epsilon << kernel->ao_dist << kernel->max_speed
                << kernel->alpha_channel << kernel->bump_normal_mapping << kernel->alpha_shadows
                << kernel->wf_bktrace_hl << kernel->distributed_tracing << (interactive ? kernel->max_preview_samples : kernel->max_samples) << kernel->layers_enable << kernel->layers_current << kernel->layers_invert;
            snd.write();
        }
            break;
        default:
        {
            RPCSend snd(socket, sizeof(int32_t) * 5 + sizeof(float), LOAD_KERNEL);
            int32_t def_kernel_type = static_cast<int32_t>(Kernel::DEFAULT);
            snd << def_kernel_type << def_kernel_type << kernel->shuttertime << kernel->layers_enable << kernel->layers_current << kernel->layers_invert;
            snd.write();
        }
            break;
        }

        RPCReceive rcv(socket);
        if(rcv.type != LOAD_KERNEL) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR loading kernel.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //load_kernel()

    // Set region of image to render
    void set_render_region(Camera* cam) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        {
            RPCSend snd(socket, sizeof(uint32_t) * 4, LOAD_RENDER_REGION);
            if(cam->use_border)
                snd << cam->border.x << cam->border.y << cam->border.z << cam->border.w;
            else {
                uint32_t tmp = 0;
                snd << tmp << tmp << tmp << tmp;
            }
            snd.write();
        }

        RPCReceive rcv(socket);
        if(rcv.type != LOAD_RENDER_REGION) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR setting render region.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //set_render_region()

    // Load environment to render server.
    // env - environment data structure
    void load_environment(Environment* env) {
        if(socket < 0) return;

        thread_scoped_lock socket_lock(socket_mutex);

        if(env->type == 0) {
            RPCSend snd(socket, sizeof(uint32_t) * 3 + sizeof(float) + env->texture.length() + 2, LOAD_SUNSKY);
            snd << env->type << env->type << env->power << env->importance_sampling << env->texture.c_str();
            snd.write();
        }
        else {
            if(env->daylight_type == 0) {
                RPCSend snd(socket, sizeof(uint32_t) * 3 + sizeof(float) * 13 + sizeof(int32_t) + env->texture.length()+2, LOAD_SUNSKY);
                snd << env->type << env->daylight_type << env->sun_vector.x << env->sun_vector.y << env->sun_vector.z << env->power << env->turbidity << env->northoffset
                    << env->sun_size << env->sky_color.x << env->sky_color.y << env->sky_color.z << env->sunset_color.x << env->sunset_color.y << env->sunset_color.z
                    << env->model << env->importance_sampling << env->texture.c_str();
                snd.write();
            }
            else {
                RPCSend snd(socket, sizeof(uint32_t) * 3 + sizeof(float) * 13 + sizeof(int32_t) * 4 + env->texture.length()+2, LOAD_SUNSKY);
                snd << env->type << env->daylight_type << env->longitude << env->latitude << env->hour << env->power << env->turbidity << env->northoffset
                    << env->sun_size << env->sky_color.x << env->sky_color.y << env->sky_color.z << env->sunset_color.x << env->sunset_color.y << env->sunset_color.z
                    << env->model << env->month << env->day << env->gmtoffset << env->importance_sampling << env->texture.c_str();
                snd.write();
            }
        }
        RPCReceive rcv(socket);
        if(rcv.type != LOAD_SUNSKY) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR loading environment.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //load_environment()

    // Load scatter node to server. Subject to change at the time. Should be more complicated. Multiple matrices in one scatter will be implemented later.
    // scatter_name - transforms name
    // mesh_name    - name of mesh scattered
    // matrices     - matrices array
    // mat_cnt      - count of matrices
    // shader_names - names of shaders assigned to transforms
    inline void load_scatter(string& scatter_name, string& mesh_name, float* matrices, uint64_t mat_cnt, bool movable, vector<string>& shader_names, uint32_t frame_idx, uint32_t total_frames) {
        if(socket < 0) return;
        thread_scoped_lock socket_lock(socket_mutex);

        uint64_t shaders_cnt = shader_names.size();
        
        {
            uint64_t size = sizeof(uint64_t) + mesh_name.length() + 2;
            for(uint64_t n=0; n<shaders_cnt; ++n)
                size += shader_names[n].length()+2;

            RPCSend snd(socket, size, LOAD_GEO_MAT, (scatter_name+"_m__").c_str());
            snd << shaders_cnt << mesh_name;
            for(uint64_t n=0; n<shaders_cnt; ++n)
                snd << shader_names[n];
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != LOAD_GEO_MAT) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR loading materials of transform.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }

        {
            uint64_t size = sizeof(uint64_t)
                + sizeof(int32_t) //Movable
                + sizeof(uint32_t) * 2 //Frame index
                + scatter_name.length() + 4 + 2 + sizeof(float) * 12 * mat_cnt;

            RPCSend snd(socket, size, LOAD_GEO_SCATTER, (scatter_name+"_s__").c_str());
            std::string tmp = scatter_name+"_m__";
            snd << mat_cnt;
            snd.write_buffer(matrices, sizeof(float)*12*mat_cnt);
            snd << movable << frame_idx << total_frames << tmp;
            snd.write();
        }
        RPCReceive rcv(socket);
        if(rcv.type != LOAD_GEO_SCATTER) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR loading transform.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
        }
    } //load_scatter()
    inline void delete_scatter(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_GEO_SCATTER, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_GEO_SCATTER) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting transform.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_scatter()

    // Load mesh to render server.
    inline void load_mesh(          bool            global, uint32_t frame_idx, uint32_t total_frames,
                                    uint64_t        mesh_cnt,
                                    char            **names,
                                    uint64_t        *shaders_count,
                                    vector<string>  *shader_names,
                                    float3          **points,
                                    uint64_t        *points_size,
                                    float3          **normals,
                                    uint64_t        *normals_size,
                                    int             **points_indices,
                                    int             **normals_indices,
                                    uint64_t        *points_indices_size,
                                    uint64_t        *normals_indices_size,
                                    int             **vert_per_poly,
                                    uint64_t        *vert_per_poly_size,
                                    int             **poly_mat_index,
                                    float3          **uvs,
                                    uint64_t        *uvs_size,
                                    int             **uv_indices,
                                    uint64_t        *uv_indices_size,
                                    float3          **hair_points,
                                    uint64_t        *hair_points_size,
                                    int32_t         **vert_per_hair,
                                    uint64_t        *vert_per_hair_size,
                                    float           **hair_thickness,
                                    int32_t         **hair_mat_indices,
                                    float2          **hair_uvs,
                                    bool            *open_subd_enable,
                                    int32_t         *open_subd_scheme,
                                    int32_t         *open_subd_level,
                                    float           *open_subd_sharpness,
                                    int32_t         *open_subd_bound_interp,
                                    int32_t         *layer_number,
                                    float           *general_vis,
                                    bool            *cam_vis,
                                    bool            *shadow_vis,
                                    bool            *reshapable) {
            if(socket < 0) return;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                uint64_t size = sizeof(uint64_t) //Meshes count;
                    + sizeof(uint32_t) * 2 //Frame index
                    + sizeof(int32_t) * 4 * mesh_cnt + sizeof(float) * 1 * mesh_cnt //Subdivision addributes
                    + sizeof(int32_t) * 4 * mesh_cnt + sizeof(float) * 1 * mesh_cnt //Visibility and reshapable addributes
                    + sizeof(uint64_t) * 10 * mesh_cnt;
                for(unsigned long i=0; i<mesh_cnt; ++i) {
                    size +=
                    + points_size[i]*sizeof(float)*3
                    + normals_size[i]*sizeof(float)*3
                    + points_indices_size[i]*sizeof(int32_t)
                    + normals_indices_size[i]*sizeof(int32_t)
                    + + 2*vert_per_poly_size[i]*sizeof(int32_t)
                    + uvs_size[i]*sizeof(float)*3
                    + uv_indices_size[i] * sizeof(int32_t)
                    + hair_points_size[i] * sizeof(float) * 3
                    + vert_per_hair_size[i] * sizeof(int32_t)
                    + hair_points_size[i] * sizeof(float)
                    + vert_per_hair_size[i] * sizeof(int32_t)
                    + vert_per_hair_size[i] * sizeof(float) * 2;

                    if(!global) size += strlen(names[i])+2;
                    for(unsigned int n=0; n<shaders_count[i]; ++n)
                        size += shader_names[i][n].length()+2;
                }

                RPCSend snd(socket, size, global ? LOAD_GLOBAL_MESH : LOAD_LOCAL_MESH, names[0]);

                snd << mesh_cnt << frame_idx << total_frames;

                for(unsigned long i=0; i<mesh_cnt; ++i) {
                    if(!hair_points_size[i] && (!points_size[i] || !normals_size[i] || !points_indices_size[i] || !vert_per_poly_size[i] || !uvs_size[i] || !uv_indices_size[i])) return;

                    snd << points_size[i]
                        << normals_size[i]
                        << points_indices_size[i]
                        << normals_indices_size[i]
                        << vert_per_poly_size[i]
                        << uvs_size[i]
                        << uv_indices_size[i]
                        << shaders_count[i]
                        << hair_points_size[i]
                        << vert_per_hair_size[i];
                }

                for(unsigned long i=0; i<mesh_cnt; ++i) {
                    snd.write_float3_buffer(points[i], points_size[i]);
                    if(normals_size[i]) snd.write_float3_buffer(normals[i], normals_size[i]);
                    if(uvs_size[i]) snd.write_float3_buffer(uvs[i], uvs_size[i]);
                    if(hair_points_size[i]) snd.write_float3_buffer(hair_points[i], hair_points_size[i]);
                    if(vert_per_hair_size[i]) snd.write_float2_buffer(hair_uvs[i], vert_per_hair_size[i]);
                    if(hair_points_size[i]) snd.write_buffer(hair_thickness[i], hair_points_size[i] * sizeof(float));
                    snd << open_subd_sharpness[i] << general_vis[i];
                }

                for(unsigned long i=0; i<mesh_cnt; ++i) {
                    snd.write_buffer(points_indices[i], points_indices_size[i] * sizeof(int32_t));
                    snd.write_buffer(vert_per_poly[i], vert_per_poly_size[i] * sizeof(int32_t));
                    snd.write_buffer(poly_mat_index[i], vert_per_poly_size[i] * sizeof(int32_t));
                    if(normals_indices_size[i]) snd.write_buffer(normals_indices[i], normals_indices_size[i] * sizeof(int32_t));
                    if(uv_indices_size[i]) snd.write_buffer(uv_indices[i], uv_indices_size[i] * sizeof(int32_t));
                    if(vert_per_hair_size[i]) snd.write_buffer(vert_per_hair[i], vert_per_hair_size[i] * sizeof(int32_t));
                    if(vert_per_hair_size[i]) snd.write_buffer(hair_mat_indices[i], vert_per_hair_size[i] * sizeof(int32_t));
                    snd << open_subd_enable[i] << open_subd_scheme[i] << open_subd_level[i] << open_subd_bound_interp[i] << layer_number[i] << cam_vis[i] << shadow_vis[i] << reshapable[i];
                }
                for(unsigned long i=0; i<mesh_cnt; ++i) {
                    if(!global) snd << names[i];
                    for(unsigned int n=0; n<shaders_count[i]; ++n)
                        snd << shader_names[i][n];
                }

                snd.write();
            }

            RPCReceive rcv(socket);
            if(rcv.type != (global ? LOAD_GLOBAL_MESH : LOAD_LOCAL_MESH)) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR loading mesh.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
    } //load_mesh()
    inline void delete_mesh(bool global, string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, (global ? DEL_GLOBAL_MESH : DEL_LOCAL_MESH), name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != (global ? DEL_GLOBAL_MESH : DEL_LOCAL_MESH)) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting mesh.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_mesh()

    inline bool wait_error(PacketType type) {
        if(socket < 0) return false;

        RPCReceive rcv(socket);
        if(rcv.type != type) {
            rcv >> error_msg;
            fprintf(stderr, "Octane: ERROR loading node.");
            if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
            else fprintf(stderr, "\n");
            return false;
        }
        else return true;
    } //wait_error()

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // MATERIALS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_diffuse_mat(OctaneDiffuseMaterial* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 9 + sizeof(int32_t) * 2
            + node->diffuse.length() + 2
            + node->transmission.length() + 2
            + node->bump.length() + 2
            + node->normal.length() + 2
            + node->opacity.length() + 2
            + node->rounding.length() + 2
            + node->emission.length() + 2
            + node->medium.length() + 2
            + node->displacement.length() + 2
            + node->roughness.length() + 2;

        const char* mat_name = node->name.c_str();

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_DIFFUSE_MATERIAL, mat_name);
            snd << node->diffuse_default_val.x << node->diffuse_default_val.y << node->diffuse_default_val.z
                << node->transmission_default_val << node->bump_default_val << node->normal_default_val << node->opacity_default_val << node->rounding_default_val << node->roughness_default_val
                << node->smooth << node->matte << node->diffuse.c_str() << node->transmission.c_str() << node->bump.c_str()
                << node->normal.c_str() << node->opacity.c_str() << node->rounding.c_str() << node->emission.c_str() << node->medium.c_str() << node->displacement.c_str() << node->roughness.c_str();
            snd.write();
        }
        wait_error(LOAD_DIFFUSE_MATERIAL);
    } //load_diffuse_mat()

    inline void load_glossy_mat(OctaneGlossyMaterial* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 10 + sizeof(float) * 2 + sizeof(int32_t) * 1
            + node->diffuse.length() + 2
            + node->specular.length() + 2
            + node->roughness.length() + 2
            + node->filmwidth.length() + 2
            + node->bump.length() + 2
            + node->normal.length() + 2
            + node->opacity.length() + 2
            + node->filmindex.length() + 2
            + node->index.length() + 2
            + node->rounding.length() + 2
            + node->displacement.length() + 2;

        const char* mat_name = node->name.c_str();

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_GLOSSY_MATERIAL, mat_name);
            snd << node->diffuse_default_val.x << node->diffuse_default_val.y << node->diffuse_default_val.z
                << node->specular_default_val << node->roughness_default_val << node->filmwidth_default_val << node->bump_default_val
                << node->normal_default_val << node->opacity_default_val << node->filmindex_default_val << node->index_default_val << node->rounding_default_val
                << node->smooth
                << node->filmindex.c_str() << node->index.c_str() << node->rounding.c_str()
                << node->diffuse.c_str() << node->specular.c_str() << node->roughness.c_str()
                << node->filmwidth.c_str() << node->bump.c_str() << node->normal.c_str() << node->opacity.c_str() << node->displacement.c_str();
            snd.write();
        }
        wait_error(LOAD_GLOSSY_MATERIAL);
    } //load_glossy_mat()

    inline void load_specular_mat(OctaneSpecularMaterial* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 10 + sizeof(float) * 3 + sizeof(int32_t) * 3
            + node->reflection.length() + 2
            + node->transmission.length() + 2
            + node->filmwidth.length() + 2
            + node->bump.length() + 2
            + node->normal.length() + 2
            + node->opacity.length() + 2
            + node->roughness.length() + 2
            + node->medium.length() + 2
            + node->filmindex.length() + 2
            + node->index.length() + 2
            + node->dispersion_coef_B.length() + 2
            + node->rounding.length() + 2
            + node->displacement.length() + 2;

        const char* mat_name = node->name.c_str();

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_SPECULAR_MATERIAL, mat_name);
            snd << node->reflection_default_val.x << node->reflection_default_val.y << node->reflection_default_val.z
                << node->transmission_default_val << node->filmwidth_default_val << node->bump_default_val << node->normal_default_val
                << node->opacity_default_val << node->roughness_default_val << node->filmindex_default_val << node->index_default_val << node->dispersion_coef_B_default_val << node->rounding_default_val
                << node->smooth << node->refraction_alpha << node->fake_shadows
                << node->filmindex.c_str() << node->index.c_str() << node->dispersion_coef_B.c_str() << node->rounding.c_str()
                << node->reflection.c_str() << node->transmission.c_str() << node->filmwidth.c_str() << node->bump.c_str()
                << node->normal.c_str() << node->opacity.c_str() << node->roughness.c_str() << node->medium.c_str() << node->displacement.c_str();
            snd.write();
        }
        wait_error(LOAD_SPECULAR_MATERIAL);
    } //load_specular_mat()

    inline void load_mix_mat(OctaneMixMaterial* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->amount.length() + 2
            + node->material1.length() + 2
            + node->material2.length() + 2
            + node->displacement.length() + 2;

        const char* mat_name = node->name.c_str();

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_MIX_MATERIAL, mat_name);
            snd << node->amount_default_val << node->amount.c_str() << node->material2.c_str() << node->material1.c_str() << node->displacement.c_str();
            snd.write();
        }
        wait_error(LOAD_MIX_MATERIAL);
    } //load_mix_mat()

    inline void load_portal_mat(OctanePortalMaterial* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t);

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PORTAL_MATERIAL, node->name.c_str());
            snd << node->enabled;
            snd.write();
        }
        wait_error(LOAD_PORTAL_MATERIAL);
    } //load_portal_mat()

    inline void delete_material(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_MATERIAL, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_MATERIAL) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting material.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_material()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // TEXTURES
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_float_tex(OctaneFloatTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float);

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_FLOAT_TEXTURE, node->name.c_str());
            snd << node->value;
            snd.write();
        }
        wait_error(LOAD_FLOAT_TEXTURE);
    } //load_float_tex()

    inline void load_rgb_spectrum_tex(OctaneRGBSpectrumTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_RGB_SPECTRUM_TEXTURE, node->name.c_str());
            snd << node->value[0] << node->value[1] << node->value[2];
            snd.write();
        }
        wait_error(LOAD_RGB_SPECTRUM_TEXTURE);
    } //load_rgb_spectrum_tex()

    inline void load_gaussian_spectrum_tex(OctaneGaussianSpectrumTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3
            + node->WaveLength.length() + 2
            + node->Width.length() + 2
            + node->Power.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_GAUSSIAN_SPECTRUM_TEXTURE, node->name.c_str());
            snd << node->WaveLength_default_val << node->Width_default_val << node->Power_default_val
                << node->WaveLength.c_str() << node->Width.c_str() << node->Power.c_str();
            snd.write();
        }
        wait_error(LOAD_GAUSSIAN_SPECTRUM_TEXTURE);
    } //load_gaussian_spectrum_tex()

    inline void load_checks_tex(OctaneChecksTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) + node->Transform.length() + 2 + node->Projection.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_CHECKS_TEXTURE, node->name.c_str());
            snd << node->Transform_default_val << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_CHECKS_TEXTURE);
    } //load_checks_tex()

    inline void load_marble_tex(OctaneMarbleTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 4 + sizeof(int32_t)
            + node->Power.length() + 2
            + node->Offset.length() + 2
            + node->Omega.length() + 2
            + node->Variance.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2
            + node->Octaves.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_MARBLE_TEXTURE, node->name.c_str());
            snd << node->Power_default_val << node->Offset_default_val << node->Omega_default_val << node->Variance_default_val
                << node->Octaves_default_val << node->Octaves.c_str()
                << node->Power.c_str() << node->Offset.c_str() << node->Omega.c_str() << node->Variance.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_MARBLE_TEXTURE);
    } //load_marble_tex()

    inline void load_ridged_fractal_tex(OctaneRidgedFractalTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3 + sizeof(int32_t)
            + node->Power.length() + 2
            + node->Offset.length() + 2
            + node->Lacunarity.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2
            + node->Octaves.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_RIDGED_FRACTAL_TEXTURE, node->name.c_str());
            snd << node->Power_default_val << node->Offset_default_val << node->Lacunarity_default_val
                << node->Octaves_default_val << node->Octaves.c_str()
                << node->Power.c_str() << node->Offset.c_str() << node->Lacunarity.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_RIDGED_FRACTAL_TEXTURE);
    } //load_ridged_fractal_tex()

    inline void load_saw_wave_tex(OctaneSawWaveTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->Offset.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_SAW_WAVE_TEXTURE, node->name.c_str());
            snd << node->Offset_default_val
                << node->Offset.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_SAW_WAVE_TEXTURE);
    } //load_saw_wave_tex()

    inline void load_sine_wave_tex(OctaneSineWaveTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->Offset.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_SINE_WAVE_TEXTURE, node->name.c_str());
            snd << node->Offset_default_val
                << node->Offset.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_SINE_WAVE_TEXTURE);
    } //load_sine_wave_tex()

    inline void load_triangle_wave_tex(OctaneTriangleWaveTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->Offset.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_TRIANGLE_WAVE_TEXTURE, node->name.c_str());
            snd << node->Offset_default_val
                << node->Offset.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_TRIANGLE_WAVE_TEXTURE);
    } //load_triangle_wave_tex()

    inline void load_turbulence_tex(OctaneTurbulenceTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 4 + sizeof(int32_t) * 3
            + node->Power.length() + 2
            + node->Offset.length() + 2
            + node->Omega.length() + 2
            + node->Gamma.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2
            + node->Octaves.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_TURBULENCE_TEXTURE, node->name.c_str());
            snd << node->Power_default_val << node->Offset_default_val << node->Omega_default_val << node->Gamma_default_val << node->Octaves_default_val
                << node->Turbulence << node->Invert
                << node->Octaves.c_str() << node->Power.c_str() << node->Offset.c_str() << node->Omega.c_str() << node->Gamma.c_str() << node->Transform.c_str() << node->Projection.c_str();
            snd.write();
        }
        wait_error(LOAD_TURBULENCE_TEXTURE);
    } //load_turbulence_tex()

    inline void load_clamp_tex(OctaneClampTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3
            + node->Input.length() + 2
            + node->Min.length() + 2
            + node->Max.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_CLAMP_TEXTURE, node->name.c_str());
            snd << node->Input_default_val << node->Min_default_val << node->Max_default_val
                << node->Input.c_str() << node->Min.c_str() << node->Max.c_str();
            snd.write();
        }
        wait_error(LOAD_CLAMP_TEXTURE);
    } //load_clamp_tex()

    inline void load_cosine_mix_tex(OctaneCosineMixTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->Amount.length() + 2
            + node->Texture1.length() + 2
            + node->Texture2.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_COSINE_MIX_TEXTURE, node->name.c_str());
            snd << node->Amount_default_val
                << node->Amount.c_str() << node->Texture1.c_str() << node->Texture2.c_str();
            snd.write();
        }
        wait_error(LOAD_COSINE_MIX_TEXTURE);
    } //load_cosine_mix_tex()

    inline void load_invert_tex(OctaneInvertTexture* node) {
        if(socket < 0) return;

        uint64_t size = node->Texture.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_INVERT_TEXTURE, node->name.c_str());
            snd << node->Texture.c_str();
            snd.write();
        }
        wait_error(LOAD_INVERT_TEXTURE);
    } //load_invert_tex()

    inline void load_mix_tex(OctaneMixTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float)
            + node->Amount.length() + 2
            + node->Texture1.length() + 2
            + node->Texture2.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_MIX_TEXTURE, node->name.c_str());
            snd << node->Amount_default_val
                << node->Amount.c_str() << node->Texture1.c_str() << node->Texture2.c_str();
            snd.write();
        }
        wait_error(LOAD_MIX_TEXTURE);
    } //load_mix_tex()

    inline void load_multiply_tex(OctaneMultiplyTexture* node) {
        if(socket < 0) return;

        uint64_t size = node->Texture1.length() + 2
            + node->Texture2.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_MULTIPLY_TEXTURE, node->name.c_str());
            snd << node->Texture1.c_str() << node->Texture2.c_str();
            snd.write();
        }
        wait_error(LOAD_MULTIPLY_TEXTURE);
    } //load_multiply_tex()

    inline void load_falloff_tex(OctaneFalloffTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3
            + node->Normal.length() + 2
            + node->Grazing.length() + 2
            + node->Index.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_FALLOFF_TEXTURE, node->name.c_str());
            snd << node->Normal_default_val << node->Grazing_default_val << node->Index_default_val
                << node->Normal.c_str() << node->Grazing.c_str() << node->Index.c_str();
            snd.write();
        }
        wait_error(LOAD_FALLOFF_TEXTURE);
    } //load_falloff_tex()

    inline void load_colorcorrect_tex(OctaneColorCorrectTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 5 + sizeof(int32_t)
            + node->Texture.length() + 2
            + node->Brightness.length() + 2
            + node->Gamma.length() + 2
            + node->Hue.length() + 2
            + node->Saturation.length() + 2
            + node->Contrast.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_COLOR_CORRECT_TEXTURE, node->name.c_str());
            snd << node->Brightness_default_val << node->Gamma_default_val << node->Hue_default_val << node->Saturation_default_val << node->Contrast_default_val
                << node->Invert
                << node->Gamma.c_str() << node->Hue.c_str() << node->Saturation.c_str() << node->Contrast.c_str()
                << node->Texture.c_str() << node->Brightness.c_str();
            snd.write();
        }
        wait_error(LOAD_COLOR_CORRECT_TEXTURE);
    } //load_colorcorrect_tex()

    inline string get_file_name(string &full_path) {
        size_t sl1 = full_path.rfind('/');
        size_t sl2 = full_path.rfind('\\');
        string file_name;
        if(sl1 == string::npos && sl2 == string::npos) {
            file_name = full_path;
        }
        else {
            if(sl1 == string::npos)
                sl1 = sl2;
            else if(sl2 != string::npos)
                sl1 = sl1 > sl2 ? sl1 : sl2;
            file_name = full_path.substr(sl1 + 1);
        }
        return file_name;
    }

    inline uint64_t get_file_time(string &full_path) {
        if(!full_path.length()) return 0;

        struct stat attrib;
        stat(full_path.c_str(), &attrib);

        return static_cast<uint64_t>(attrib.st_mtime);
    }

    inline bool send_file(string &file_path, string &file_name) {
        FILE *hFile = BLI_fopen(file_path.c_str(), "rb");
        if(hFile) {
            fseek(hFile, 0, SEEK_END);
            uint32_t ulFileSize = ftell(hFile);
            rewind(hFile);

            char* pCurPtr = new char[ulFileSize];

            if(!fread(pCurPtr, ulFileSize, 1, hFile)) {
                fclose(hFile);
                delete[] pCurPtr;
                return false;
            }
            fclose(hFile);

            RPCSend snd(socket, sizeof(uint32_t) + ulFileSize, LOAD_IMAGE_FILE, file_name.c_str());
            snd << ulFileSize;
            snd.write_buffer(pCurPtr, ulFileSize);
            snd.write();
            delete[] pCurPtr;

            {
                RPCReceive rcv(socket);
                if(rcv.type != LOAD_IMAGE_FILE) {
                    rcv >> error_msg;
                    fprintf(stderr, "Octane: ERROR loading image file.");
                    if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                    else fprintf(stderr, "\n");
                    return false;
                }
            }
            return true;
        }
        else return false;
    }

    inline void load_image_tex(OctaneImageTexture* node) {
        if(socket < 0) return;

        void *pixels = 0;
        bool is_float;
        int32_t width, height, depth, components, img_size;
        if(node->builtin_data) {
            builtin_image_info(node->FileName, node->builtin_data, is_float, width, height, depth, components);

            if(components == 1 || components == 4) {
                img_size = width * height * components;
                if(is_float) {
                    pixels = new float[img_size];
                    builtin_image_float_pixels(node->FileName, node->builtin_data, (float*)pixels);
                }
                else {
                    pixels = new uint8_t[img_size];
                    builtin_image_pixels(node->FileName, node->builtin_data, (uint8_t*)pixels);
                }
            }
        }

        if(pixels) {
            if(!unpacked_msg) {
                unpacked_msg = true;
                fprintf(stderr, "\nOctane: rendering of UNPACKED textures would be faster, as they are cached on the Octane server.\n\n");
            }

            uint64_t size = sizeof(float) * 2 + sizeof(int32_t) * 6 + img_size * (is_float ? sizeof(float) : 1)
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_IMAGE_TEXTURE_DATA, node->name.c_str());
                snd << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << width << height << components << is_float << node->Invert;
                if(is_float)
                    snd.write_buffer(pixels, img_size * sizeof(float));
                else
                    snd.write_buffer(pixels, img_size);
                snd << node->Gamma.c_str() << node->BorderMode.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }
            if(is_float)
                delete[] (float*)pixels;
            else
                delete[] (uint8_t*)pixels;

            wait_error(LOAD_IMAGE_TEXTURE_DATA);
        }
        else {
            uint64_t mod_time = get_file_time(node->FileName);
            string file_name  = get_file_name(node->FileName);

            uint64_t size = sizeof(uint64_t) + sizeof(float) * 2 + sizeof(int32_t) * 2
                + file_name.length() + 2
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_IMAGE_TEXTURE, node->name.c_str());
                snd << mod_time << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << node->Invert
                    << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }

            bool file_is_needed;
            {
                RPCReceive rcv(socket);
                if(rcv.type != LOAD_IMAGE_TEXTURE)
                    file_is_needed = true;
                else
                    file_is_needed = false;
            }

            if(file_is_needed && send_file(node->FileName, file_name)) {
                {
                    RPCSend snd(socket, size, LOAD_IMAGE_TEXTURE, node->name.c_str());
                    snd << mod_time << node->Power_default_val << node->Gamma_default_val
                        << node->BorderMode_default_val << node->Invert
                        << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                    snd.write();
                }
                {
                    RPCReceive rcv(socket);
                    if(rcv.type != LOAD_IMAGE_TEXTURE) {
                        rcv >> error_msg;
                        fprintf(stderr, "Octane: ERROR loading image texture.");
                        if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                        else fprintf(stderr, "\n");
                    }
                }
            }
        }
    } //load_image_tex()

    inline void load_float_image_tex(OctaneFloatImageTexture* node) {
        if(socket < 0) return;

        void *pixels = 0;
        bool is_float;
        int32_t width, height, depth, components, img_size;
        if(node->builtin_data) {
            builtin_image_info(node->FileName, node->builtin_data, is_float, width, height, depth, components);

            if(components == 1 || components == 4) {
                img_size = width * height * components;
                if(is_float) {
                    pixels = new float[img_size];
                    builtin_image_float_pixels(node->FileName, node->builtin_data, (float*)pixels);
                }
                else {
                    pixels = new uint8_t[img_size];
                    builtin_image_pixels(node->FileName, node->builtin_data, (uint8_t*)pixels);
                }
            }
        }

        if(pixels) {
            if(!unpacked_msg) {
                unpacked_msg = true;
                fprintf(stderr, "\nOctane: rendering of UNPACKED textures would be faster, as they are cached on the Octane server.\n\n");
            }

            uint64_t size = sizeof(float) * 2 + sizeof(int32_t) * 6 + img_size * (is_float ? sizeof(float) : 1)
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_FLOAT_IMAGE_TEXTURE_DATA, node->name.c_str());
                snd << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << width << height << components << is_float << node->Invert;
                if(is_float)
                    snd.write_buffer(pixels, img_size * sizeof(float));
                else
                    snd.write_buffer(pixels, img_size);
                snd << node->Gamma.c_str() << node->BorderMode.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }
            if(is_float)
                delete[] (float*)pixels;
            else
                delete[] (uint8_t*)pixels;

            wait_error(LOAD_FLOAT_IMAGE_TEXTURE_DATA);
        }
        else {
            uint64_t mod_time = get_file_time(node->FileName);
            string file_name  = get_file_name(node->FileName);

            uint64_t size = sizeof(uint64_t) + sizeof(float) * 2 + sizeof(int32_t) * 2
                + file_name.length() + 2
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_FLOAT_IMAGE_TEXTURE, node->name.c_str());
                snd << mod_time << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << node->Invert
                    << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }

            bool file_is_needed;
            {
                RPCReceive rcv(socket);
                if(rcv.type != LOAD_FLOAT_IMAGE_TEXTURE)
                    file_is_needed = true;
                else
                    file_is_needed = false;
            }

            if(file_is_needed && send_file(node->FileName, file_name)) {
                {
                    RPCSend snd(socket, size, LOAD_FLOAT_IMAGE_TEXTURE, node->name.c_str());
                    snd << mod_time << node->Power_default_val << node->Gamma_default_val
                        << node->BorderMode_default_val << node->Invert
                        << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                    snd.write();
                }
                {
                    RPCReceive rcv(socket);
                    if(rcv.type != LOAD_FLOAT_IMAGE_TEXTURE) {
                        rcv >> error_msg;
                        fprintf(stderr, "Octane: ERROR loading float image texture.");
                        if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                        else fprintf(stderr, "\n");
                    }
                }
            }
        }
    } //load_float_image_tex()

    inline void load_alpha_image_tex(OctaneAlphaImageTexture* node) {
        if(socket < 0) return;

        void *pixels = 0;
        bool is_float;
        int32_t width, height, depth, components, img_size;
        if(node->builtin_data) {
            builtin_image_info(node->FileName, node->builtin_data, is_float, width, height, depth, components);

            if(components == 1 || components == 4) {
                img_size = width * height * components;
                if(is_float) {
                    pixels = new float[img_size];
                    builtin_image_float_pixels(node->FileName, node->builtin_data, (float*)pixels);
                }
                else {
                    pixels = new uint8_t[img_size];
                    builtin_image_pixels(node->FileName, node->builtin_data, (uint8_t*)pixels);
                }
            }
        }

        if(pixels) {
            if(!unpacked_msg) {
                unpacked_msg = true;
                fprintf(stderr, "\nOctane: rendering of UNPACKED textures would be faster, as they are cached on the Octane server.\n\n");
            }

            uint64_t size = sizeof(float) * 2 + sizeof(int32_t) * 6 + img_size * (is_float ? sizeof(float) : 1)
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_ALPHA_IMAGE_TEXTURE_DATA, node->name.c_str());
                snd << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << width << height << components << is_float << node->Invert;
                if(is_float)
                    snd.write_buffer(pixels, img_size * sizeof(float));
                else
                    snd.write_buffer(pixels, img_size);
                snd << node->Gamma.c_str() << node->BorderMode.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }
            if(is_float)
                delete[] (float*)pixels;
            else
                delete[] (uint8_t*)pixels;

            wait_error(LOAD_ALPHA_IMAGE_TEXTURE_DATA);
        }
        else {
            uint64_t mod_time = get_file_time(node->FileName);
            string file_name  = get_file_name(node->FileName);

            uint64_t size = sizeof(uint64_t) + sizeof(float) * 2 + sizeof(int32_t) * 2
                + file_name.length() + 2
                + node->Power.length() + 2
                + node->Projection.length() + 2
                + node->Transform.length() + 2
                + node->Gamma.length() + 2
                + node->BorderMode.length() + 2;

            thread_scoped_lock socket_lock(socket_mutex);

            {
                RPCSend snd(socket, size, LOAD_ALPHA_IMAGE_TEXTURE, node->name.c_str());
                snd << mod_time << node->Power_default_val << node->Gamma_default_val
                    << node->BorderMode_default_val << node->Invert
                    << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                snd.write();
            }

            bool file_is_needed;
            {
                RPCReceive rcv(socket);
                if(rcv.type != LOAD_ALPHA_IMAGE_TEXTURE)
                    file_is_needed = true;
                else
                    file_is_needed = false;
            }

            if(file_is_needed && send_file(node->FileName, file_name)) {
                {
                    RPCSend snd(socket, size, LOAD_ALPHA_IMAGE_TEXTURE, node->name.c_str());
                    snd << mod_time << node->Power_default_val << node->Gamma_default_val
                        << node->BorderMode_default_val << node->Invert
                        << node->Gamma.c_str() << node->BorderMode.c_str() << file_name.c_str() << node->Power.c_str() << node->Transform.c_str() << node->Projection.c_str();
                    snd.write();
                }
                {
                    RPCReceive rcv(socket);
                    if(rcv.type != LOAD_ALPHA_IMAGE_TEXTURE) {
                        rcv >> error_msg;
                        fprintf(stderr, "Octane: ERROR loading alpha image texture.");
                        if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                        else fprintf(stderr, "\n");
                    }
                }
            }
        }
    } //load_alpha_image_tex()

    inline void load_dirt_tex(OctaneDirtTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 4 + sizeof(int32_t)
            + node->Strength.length() + 2
            + node->Details.length() + 2
            + node->Radius.length() + 2
            + node->Tolerance.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_DIRT_TEXTURE, node->name.c_str());
            snd << node->Strength_default_val << node->Details_default_val << node->Radius_default_val << node->Tolerance_default_val
                << node->InvertNormal
                << node->Strength.c_str() << node->Details.c_str() << node->Radius.c_str() << node->Tolerance.c_str();
            snd.write();
        }
        wait_error(LOAD_DIRT_TEXTURE);
    } //load_dirt_tex()

    inline void load_gradient_tex(OctaneGradientTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t) * 2
            + node->pos_data.size() * sizeof(float)
            + node->color_data.size() * sizeof(float)
            + node->texture.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            int32_t grad_cnt = node->pos_data.size();

            RPCSend snd(socket, size, LOAD_GRADIENT_TEXTURE, node->name.c_str());
            snd << grad_cnt << node->Smooth;
            snd.write_buffer(&node->pos_data[0], sizeof(float) * node->pos_data.size());
            snd.write_buffer(&node->color_data[0], sizeof(float) * node->color_data.size());
            snd << node->texture.c_str();
            snd.write();
        }
        wait_error(LOAD_GRADIENT_TEXTURE);
    } //load_gradient_tex()

    inline void load_random_color_tex(OctaneRandomColorTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Seed.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_RANDOM_COLOR_TEXTURE, node->name.c_str());
            snd << node->Seed_default_val
                << node->Seed.c_str();
            snd.write();
        }
        wait_error(LOAD_RANDOM_COLOR_TEXTURE);
    } //load_random_color_tex()

    inline void load_polygon_side_tex(OctanePolygonSideTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t);

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_POLYGON_SIDE_TEXTURE, node->name.c_str());
            snd << node->Invert;
            snd.write();
        }
        wait_error(LOAD_POLYGON_SIDE_TEXTURE);
    } //load_polygon_side_tex()

    inline void load_noise_tex(OctaneNoiseTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3 + sizeof(int32_t) * 3
            + node->noise_type.length() + 2
            + node->Octaves.length() + 2
            + node->Omega.length() + 2
            + node->Transform.length() + 2
            + node->Projection.length() + 2
            + node->Gamma.length() + 2
            + node->Contrast.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_NOISE_TEXTURE, node->name.c_str());
            snd << node->Omega_default_val << node->Gamma_default_val << node->Contrast_default_val
                << node->noise_type_default_val << node->Octaves_default_val << node->Invert
                << node->noise_type.c_str() << node->Octaves.c_str() << node->Omega.c_str() << node->Transform.c_str()
                << node->Projection.c_str() << node->Gamma.c_str() << node->Contrast.c_str();
            snd.write();
        }
        wait_error(LOAD_NOISE_TEXTURE);
    } //load_noise_tex()

    inline void load_displacement_tex(OctaneDisplacementTexture* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 2 + sizeof(int32_t)
            + node->texture.length() + 2
            + node->Height.length() + 2
            + node->Offset.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_DISPLACEMENT_TEXTURE, node->name.c_str());
            snd << node->Height_default_val << node->Offset_default_val
                << node->DetailsLevel
                << node->texture.c_str() << node->Height.c_str() << node->Offset.c_str();
            snd.write();
        }
        wait_error(LOAD_DISPLACEMENT_TEXTURE);
    } //load_displacement_tex()

    inline void delete_texture(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_TEXTURE, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_TEXTURE) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting texture.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_texture()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // EMISSIONS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_bbody_emission(OctaneBlackBodyEmission* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 5 + sizeof(int32_t) * 4
            + node->TextureOrEff.length() + 2
            + node->Power.length() + 2
            + node->Temperature.length() + 2
            + node->Distribution.length() + 2
            + node->SamplingRate.length() + 2
            + node->LightPassID.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_BLACKBODY_EMISSION, node->name.c_str());
            snd << node->TextureOrEff_default_val << node->Power_default_val << node->Temperature_default_val << node->Distribution_default_val << node->SamplingRate_default_val
                << node->LightPassID_default_val << node->SurfaceBrightness << node->Normalize << node->CastIllumination
                << node->TextureOrEff.c_str() << node->Power.c_str() << node->Temperature.c_str() << node->Distribution.c_str() << node->SamplingRate.c_str() << node->LightPassID.c_str();
            snd.write();
        }
        wait_error(LOAD_BLACKBODY_EMISSION);
    } //load_bbody_emission()

    inline void load_texture_emission(OctaneTextureEmission* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 4 + sizeof(int32_t) * 3
            + node->TextureOrEff.length() + 2
            + node->Power.length() + 2
            + node->Distribution.length() + 2
            + node->SamplingRate.length() + 2
            + node->LightPassID.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_TEXTURE_EMISSION, node->name.c_str());
            snd << node->TextureOrEff_default_val << node->Power_default_val << node->Distribution_default_val << node->SamplingRate_default_val
                << node->LightPassID_default_val << node->SurfaceBrightness << node->CastIllumination
                << node->TextureOrEff.c_str() << node->Power.c_str() << node->Distribution.c_str() << node->SamplingRate.c_str() << node->LightPassID.c_str();
            snd.write();
        }
        wait_error(LOAD_TEXTURE_EMISSION);
    } //load_texture_emission()

    inline void delete_emission(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_EMISSION, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_EMISSION) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting emission.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_emission()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // MEDIUMS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_absorption_medium(OctaneAbsorptionMedium* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 2
            + node->Absorption.length() + 2
            + node->Scale.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_ABSORPTION_MEDIUM, node->name.c_str());
            snd << node->Absorption_default_val << node->Scale_default_val
                << node->Absorption.c_str() << node->Scale.c_str();
            snd.write();
        }
        wait_error(LOAD_ABSORPTION_MEDIUM);
    } //load_absorption_medium()

    inline void load_scattering_medium(OctaneScatteringMedium* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 4
            + node->Absorption.length() + 2
            + node->Scattering.length() + 2
            + node->Phase.length() + 2
            + node->Emission.length() + 2
            + node->Scale.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_SCATTERING_MEDIUM, node->name.c_str());
            snd << node->Absorption_default_val << node->Scattering_default_val << node->Phase_default_val << node->Scale_default_val
                << node->Absorption.c_str() << node->Scattering.c_str() << node->Phase.c_str() << node->Emission.c_str() << node->Scale.c_str();
            snd.write();
        }
        wait_error(LOAD_SCATTERING_MEDIUM);
    } //load_scattering_medium()

    inline void delete_medium(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_MEDIUM, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_MEDIUM) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting medium.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_medium()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // TRANSFORMS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_rotation_transform(OctaneRotationTransform* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3 + sizeof(int32_t)
            + node->Rotation.length() + 2
            + node->RotationOrder.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_ROTATION_TRANSFORM, node->name.c_str());
            snd << node->Rotation_default_val.x << node->Rotation_default_val.y << node->Rotation_default_val.z << node->RotationOrder_default_val << node->Rotation << node->RotationOrder;
            snd.write();
        }
        wait_error(LOAD_ROTATION_TRANSFORM);
    } //load_rotation_transform()

    inline void load_scale_transform(OctaneScaleTransform* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3
            + node->Scale.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_SCALE_TRANSFORM, node->name.c_str());
            snd << node->Scale_default_val.x << node->Scale_default_val.y << node->Scale_default_val.z << node->Scale;
            snd.write();
        }
        wait_error(LOAD_SCALE_TRANSFORM);
    } //load_scale_transform()

    inline void load_full_transform(OctaneFullTransform* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 9 + sizeof(int32_t);

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_FULL_TRANSFORM, node->name.c_str());
            snd << node->Rotation.x << node->Rotation.y << node->Rotation.z
                << node->Scale.x << node->Scale.y << node->Scale.z
                << node->Translation.x << node->Translation.y << node->Translation.z
                << node->RotationOrder_default_val;
            snd.write();
        }
        wait_error(LOAD_FULL_TRANSFORM);
    } //load_full_transform()

    inline void load_3d_transform(Octane3DTransform* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 9 + sizeof(int32_t)
            + node->Rotation.length() + 2
            + node->Scale.length() + 2
            + node->Translation.length() + 2
            + node->RotationOrder.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_3D_TRANSFORM, node->name.c_str());
            snd << node->Rotation_default_val.x << node->Rotation_default_val.y << node->Rotation_default_val.z
                << node->Scale_default_val.x << node->Scale_default_val.y << node->Scale_default_val.z
                << node->Translation_default_val.x << node->Translation_default_val.y << node->Translation_default_val.z
                << node->RotationOrder_default_val
                << node->Rotation << node->Scale << node->Translation << node->RotationOrder;
            snd.write();
        }
        wait_error(LOAD_3D_TRANSFORM);
    } //load_3d_transform()

    inline void load_2d_transform(Octane2DTransform* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 6
            + node->Rotation.length() + 2
            + node->Scale.length() + 2
            + node->Translation.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_2D_TRANSFORM, node->name.c_str());
            snd << node->Rotation_default_val.x << node->Rotation_default_val.y
                << node->Scale_default_val.x << node->Scale_default_val.y
                << node->Translation_default_val.x << node->Translation_default_val.y
                << node->Rotation << node->Scale << node->Translation;
            snd.write();
        }
        wait_error(LOAD_2D_TRANSFORM);
    } //load_2d_transform()

    inline void delete_transform(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_TRANSFORM, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_TRANSFORM) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting transform.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_transform()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // PROJECTIONS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_xyz_projection(OctaneOctXYZProjection* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Transform.length() + 2
            + node->CoordinateSpace.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_XYZ, node->name.c_str());
            snd << node->CoordinateSpace_default_val
                << node->CoordinateSpace.c_str() << node->Transform.c_str();
            snd.write();
        }
        wait_error(LOAD_PROJECTION_XYZ);
    } //load_xyz_projection()

    inline void load_box_projection(OctaneOctBoxProjection* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Transform.length() + 2
            + node->CoordinateSpace.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_BOX, node->name.c_str());
            snd << node->CoordinateSpace_default_val
                << node->CoordinateSpace.c_str() << node->Transform.c_str();
            snd.write();
        }
        wait_error(LOAD_PROJECTION_BOX);
    } //load_box_projection()

    inline void load_cyl_projection(OctaneOctCylProjection* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Transform.length() + 2
            + node->CoordinateSpace.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_CYL, node->name.c_str());
            snd << node->CoordinateSpace_default_val
                << node->CoordinateSpace.c_str() << node->Transform.c_str();
            snd.write();
        }
        wait_error(LOAD_PROJECTION_CYL);
    } //load_cyl_projection()

    inline void load_persp_projection(OctaneOctPerspProjection* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Transform.length() + 2
            + node->CoordinateSpace.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_PERSP, node->name.c_str());
            snd << node->CoordinateSpace_default_val
                << node->CoordinateSpace.c_str() << node->Transform.c_str();
            snd.write();
        }
        wait_error(LOAD_PROJECTION_PERSP);
    } //load_persp_projection()

    inline void load_spherical_projection(OctaneOctSphericalProjection* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t)
            + node->Transform.length() + 2
            + node->CoordinateSpace.length() + 2;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_SPHERICAL, node->name.c_str());
            snd << node->CoordinateSpace_default_val
                << node->CoordinateSpace.c_str() << node->Transform.c_str();
            snd.write();
        }
        wait_error(LOAD_PROJECTION_SPHERICAL);
    } //load_spherical_projection()

    inline void load_uvw_projection(OctaneOctUVWProjection* node) {
        if(socket < 0) return;

        uint64_t size = 0;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_PROJECTION_UVW, node->name.c_str());
            snd.write();
        }
        wait_error(LOAD_PROJECTION_UVW);
    } //load_uvw_projection()

    inline void delete_projection(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_PROJECTION, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_PROJECTION) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting projection.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_projection()



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // VALUES
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void load_float_value(OctaneOctFloatValue* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(float) * 3;

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_VALUE_FLOAT, node->name.c_str());
            snd << node->Value.x << node->Value.y << node->Value.z;
            snd.write();
        }
        wait_error(LOAD_VALUE_FLOAT);
    } //load_float_value()

    inline void load_int_value(OctaneOctIntValue* node) {
        if(socket < 0) return;

        uint64_t size = sizeof(int32_t);

        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, size, LOAD_VALUE_INT, node->name.c_str());
            snd << node->Value;
            snd.write();
        }
        wait_error(LOAD_VALUE_INT);
    } //load_int_value()

    inline void delete_value(string& name) {
        if(socket < 0 || !m_bInteractive) return;
        thread_scoped_lock socket_lock(socket_mutex);
        {
            RPCSend snd(socket, 0, DEL_VALUE, name.c_str());
            snd.write();
        }
        {
            RPCReceive rcv(socket);
            if(rcv.type != DEL_VALUE) {
                rcv >> error_msg;
                fprintf(stderr, "Octane: ERROR deleting value node.");
                if(error_msg.length() > 0) fprintf(stderr, " Server response:\n%s\n", error_msg.c_str());
                else fprintf(stderr, "\n");
            }
        }
    } //delete_value()



    //FIXME: The partial buffer is not needed here ("y" parameter)...
    inline bool get_8bit_pixels(uchar4* mem, int y, int w, int h) {
        if(w <= 0) w = 4;
        if(h <= 0) h = 4;
        thread_scoped_lock img_buf_lock(img_buf_mutex);

        if(!image_buf || cur_w != w || cur_h != (h-y)) {
            if(image_buf) delete[] image_buf;
            size_t len  = w * (h-y) * 4;
            image_buf   = new unsigned char[len];

            cur_w = w;
            cur_h = h-y;
            memset(image_buf, 1, len);
            memcpy(mem + y*w, image_buf, cur_w * cur_h * 4);
            return false;
        }
        memcpy(mem + y*w, image_buf, cur_w * cur_h * 4);
        return true;
    } //get_8bit_pixels()

    inline bool get_image_buffer(ImageStatistics &image_stat, uint32_t img_type, Passes::PassTypes type, Progress &progress) {
        if(socket < 0) return false;

        thread_scoped_lock socket_lock(socket_mutex);

        while(true) {
            if(progress.get_cancel()) return false;
            {
                RPCSend snd(socket, sizeof(int32_t)*3 + sizeof(uint32_t), GET_IMAGE);
                int32_t cur_type = static_cast<int32_t>(type);
                snd << img_type << cur_w << cur_h << cur_type;
                snd.write();
            }

            RPCReceive rcv(socket);
            if(rcv.type == GET_IMAGE) {
                uint32_t uiW, uiH, uiSamples;
                rcv >> image_stat.used_vram >> image_stat.free_vram >> image_stat.total_vram >> image_stat.spp >> image_stat.expiry_time >> image_stat.tri_cnt >> image_stat.meshes_cnt >> image_stat.rgb32_cnt
                    >> image_stat.rgb64_cnt >> image_stat.grey8_cnt >> image_stat.grey16_cnt >> uiSamples >> uiW >> uiH >> image_stat.net_gpus >> image_stat.used_net_gpus;

                if(uiSamples) image_stat.cur_samples = uiSamples;

                thread_scoped_lock img_buf_lock(img_buf_mutex);
                if(img_type == 0) {
                    if(!image_buf || static_cast<uint32_t>(cur_w) != uiW || static_cast<uint32_t>(cur_h) != uiH) return false;

                    size_t  len     = uiW * uiH * 4;
                    uint8_t *ucBuf  = (uint8_t*)rcv.read_buffer(len);

                    memcpy(image_buf, ucBuf, len);
                    cur_pass_type = type;
                }
                else {
                    if(!float_img_buf || static_cast<uint32_t>(cur_reg_w) != uiW || static_cast<uint32_t>(cur_reg_h) != uiH) return false;

                    size_t len = uiW * uiH * 4;
                    float* fBuf = (float*)rcv.read_buffer(len * sizeof(float));

                    if(type == Passes::COMBINED) {
                        for(register size_t i=0; i<len; i+=4)
                            srgb_to_linearrgb_v4(&float_img_buf[i], &fBuf[i]);
                    }
                    else memcpy(float_img_buf, fBuf, len * sizeof(float));
                    cur_pass_type = type;
                }
                break;
            }
            else return false;
        }
        return true;
    } //get_image_buffer()

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Get Image-buffer of given pass
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline bool get_pass_rect(Passes::PassTypes type, int components, float *pixels, int w, int h, int reg_w, int reg_h) {
        if(w <= 0) w = 4;
        if(h <= 0) h = 4;
        if(reg_w <= 0) reg_w = 4;
        if(reg_h <= 0) reg_h = 4;
        thread_scoped_lock img_buf_lock(img_buf_mutex);
        if(!float_img_buf || cur_w != w || cur_h != h || cur_reg_w != reg_w || cur_reg_h != reg_h) {
            if(float_img_buf) delete[] float_img_buf;
            size_t len = reg_w * reg_h * 4;
            float_img_buf = new float[len];

            cur_w     = w;
            cur_h     = h;
            cur_reg_w = reg_w;
            cur_reg_h = reg_h;
            memset(float_img_buf, 0, len * sizeof(float));
            memset(pixels, 0, reg_w * reg_h * components * sizeof(float));
            return false;
        }

        size_t pixel_size = cur_reg_w * cur_reg_h;
        float* in = float_img_buf;

        if(components == 1) {
            switch(type) {
            case Passes::Z_DEPTH:
	            for(int i = 0; i < pixel_size; i++, in += 4, pixels++)
		            *pixels = *in;
                break;
            case Passes::MATERIAL_ID:
                for(int i = 0; i < pixel_size; i++, in += 4, pixels++)
                    *pixels = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) | ((uint32_t)(in[2] * 255));
                break;
            default:
                for(int i = 0; i < pixel_size; i++, in += 4, pixels++)
                    *pixels = *in;
                break;
            }
	    } //if(components == 1)
	    else if(components == 3) {
		    for(int i = 0; i < pixel_size; i++, in += 4, pixels += 3) {
			    pixels[0] = in[0];
			    pixels[1] = in[1];
			    pixels[2] = in[2];
		    }
	    } //else if(components == 3)
	    else if(components == 4) {
            memcpy(pixels, float_img_buf, pixel_size * sizeof(float) * 4);
	    } //else if(components == 4)
	    return true;
    } //get_pass_rect()


	static RenderServer*        create(RenderServerInfo& info, bool export_alembic, const char *_out_path, bool interactive = false);
    static RenderServerInfo&    get_info(void);

private:
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // 
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline int builtin_image_frame(const string &builtin_name) {
        int last = builtin_name.find_last_of('@');
        return atoi(builtin_name.substr(last + 1, builtin_name.size() - last - 1).c_str());
    } //builtin_image_frame()

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // 
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void builtin_image_info(const string &builtin_name, void *builtin_data, bool &is_float, int &width, int &height, int &depth, int &channels) {
        /* empty image */
        is_float = false;
        width = 0;
        height = 0;
        depth = 0;
        channels = 0;

        if(!builtin_data)
            return;

        /* recover ID pointer */
        PointerRNA ptr;
        RNA_id_pointer_create((ID*)builtin_data, &ptr);
        BL::ID b_id(ptr);

        if(b_id.is_a(&RNA_Image)) {
            /* image data */
            BL::Image b_image(b_id);

            is_float = b_image.is_float();
            width = b_image.size()[0];
            height = b_image.size()[1];
            depth = b_image.depth();
            channels = b_image.channels();
        }
    } //builtin_image_info()

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // 
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline bool builtin_image_pixels(const string &builtin_name, void *builtin_data, unsigned char *pixels) {
        if(!builtin_data)
            return false;

        int frame = builtin_image_frame(builtin_name);

        PointerRNA ptr;
        RNA_id_pointer_create((ID*)builtin_data, &ptr);
        BL::Image b_image(ptr);

        int width = b_image.size()[0];
        int height = b_image.size()[1];
        int channels = b_image.channels();

        unsigned char *image_pixels;
        image_pixels = image_get_pixels_for_frame(b_image, frame);

        if(image_pixels) {
            memcpy(pixels, image_pixels, width * height * channels * sizeof(unsigned char));
            MEM_freeN(image_pixels);
        }
        else {
            if(channels == 1) {
                memset(pixels, 0, width * height * sizeof(unsigned char));
            }
            else {
                unsigned char *cp = pixels;
                for(int i = 0; i < width * height; i++, cp += channels) {
                    cp[0] = 255;
                    cp[1] = 0;
                    cp[2] = 255;
                    if(channels == 4)
                        cp[3] = 255;
                }
            }
        }

        /* premultiply, byte images are always straight for blender */
        unsigned char *cp = pixels;
        for(int i = 0; i < width * height; i++, cp += channels) {
            cp[0] = (cp[0] * cp[3]) >> 8;
            cp[1] = (cp[1] * cp[3]) >> 8;
            cp[2] = (cp[2] * cp[3]) >> 8;
        }

        return true;
    } //builtin_image_pixels()

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // 
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline bool builtin_image_float_pixels(const string &builtin_name, void *builtin_data, float *pixels) {
        if(!builtin_data)
            return false;

        PointerRNA ptr;
        RNA_id_pointer_create((ID*)builtin_data, &ptr);
        BL::ID b_id(ptr);

        if(b_id.is_a(&RNA_Image)) {
            /* image data */
            BL::Image b_image(b_id);
            int frame = builtin_image_frame(builtin_name);

            int width = b_image.size()[0];
            int height = b_image.size()[1];
            int channels = b_image.channels();

            float *image_pixels;
            image_pixels = image_get_float_pixels_for_frame(b_image, frame);

            if(image_pixels) {
                memcpy(pixels, image_pixels, width * height * channels * sizeof(float));
                MEM_freeN(image_pixels);
            }
            else {
                if(channels == 1) {
                    memset(pixels, 0, width * height * sizeof(float));
                }
                else {
                    float *fp = pixels;
                    for(int i = 0; i < width * height; i++, fp += channels) {
                        fp[0] = 1.0f;
                        fp[1] = 0.0f;
                        fp[2] = 1.0f;
                        if(channels == 4)
                            fp[3] = 1.0f;
                    }
                }
            }

            return true;
        }

        return false;
    } //builtin_image_float_pixels()
}; //RenderServer

OCT_NAMESPACE_END

#endif /* __SERVER_H__ */

