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

#include <stdlib.h>

#include "buffers.h"
#include "OctaneClient.h"

#include <OpenImageIO/imageio.h>
#ifndef NOPNG
#	ifdef WIN32
#		include "png.h"
#	else
#		include <png.h>
#	endif
#endif // NOPNG

#include "util_opengl.h"
#include "util_types.h"

#include "BKE_global.h"
#include "BKE_main.h"
#include "BLI_sys_types.h"
#include "BLI_fileops.h"
#include "BLI_path_util.h"

OCT_NAMESPACE_BEGIN

using namespace OIIO_NAMESPACE;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
BufferParams::BufferParams() {
	offset_x    = 0;
	offset_y    = 0;
	full_width  = 0;
	full_height = 0;
} //BufferParams()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if buffer sizes and passes are nod equal
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BufferParams::modified(const BufferParams& params) {
	return !(full_width    == params.full_width
            && full_height == params.full_height
            && use_border  == params.use_border
            && border      == params.border
            && offset_x    == params.offset_x
		    && offset_y    == params.offset_y);
} //modified()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DISPLAY BUFFER
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
DisplayBuffer::DisplayBuffer(::OctaneEngine::OctaneClient *server_) {
    rgba        = 0;
	server      = server_;
	transparent = true; //TODO: determine from background
} //DisplayBuffer(RenderServer *server_)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
DisplayBuffer::~DisplayBuffer() {
	free_buffers();
} //~DisplayBuffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Free the Image-buffer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void DisplayBuffer::free_buffers() {
    //if(rgba) {
    //    delete[] rgba;
    //    rgba = 0;
    //}
} //free()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Reset Info and reallocate Image-buffer
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void DisplayBuffer::reset(BufferParams& params_) {
	params = params_;

    free_buffers();
    //if(params.full_width > 0 && params.full_height > 0)
    //    rgba = new uint8_t[params.full_width * params.full_height];
} //reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Do the OpenGL draw of the Image-buffer chunk
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool DisplayBuffer::draw() {
    int reg_width  = params.use_border ? params.border.z - params.border.x : params.full_width,
        reg_height = params.use_border ? params.border.w - params.border.y : params.full_height;

	if(params.full_width > 0 && params.full_height > 0) {
        int components_cnt;
        if(!server->getImgBuffer8bit(components_cnt, rgba, params.full_width, params.full_height, reg_width, reg_height)) return false;
        if(!rgba) return false;

        GLenum imgFormat;
        switch(components_cnt) {
            case 1:
                imgFormat = GL_LUMINANCE;
                break;
            case 2:
                imgFormat = GL_LUMINANCE_ALPHA;
                break;
            case 3:
                imgFormat = GL_RGB;
                break;
            case 4:
                imgFormat = GL_RGBA;
                break;
            default:
                imgFormat = GL_LUMINANCE;
                break;
        }

		glPushMatrix();
        glTranslatef(std::max(0, params.offset_x), std::max(0, params.offset_y), 0.0f);
        glTranslatef(0, 0, 0.0f);

        if(transparent) {
		    glEnable(GL_BLEND);
		    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);
	    }

	    glPixelZoom(1.0f, 1.0f);
        int iViewport[4];
        glGetIntegerv(GL_VIEWPORT, iViewport);

        if(params.use_border) {
            glViewport(iViewport[0] + std::min(0, params.offset_x) + params.border.x, iViewport[1] + std::min(0, params.offset_y) + (iViewport[3] - params.border.y - reg_height),
                       std::min(static_cast<uint32_t>(reg_width), iViewport[2] - std::min(0, params.offset_x) - params.border.x), std::min(static_cast<uint32_t>(reg_height), iViewport[3] - std::min(0, params.offset_y) - params.border.y));
	        glRasterPos2f(0, 0);

	        glDrawPixels(reg_width, reg_height, imgFormat, GL_UNSIGNED_BYTE, rgba);
        }
        else {
            glViewport(iViewport[0] + std::min(0, params.offset_x), iViewport[1] + std::min(0, params.offset_y), iViewport[2] - std::min(0, params.offset_x), iViewport[3] - std::min(0, params.offset_y));
	        glRasterPos2f(0, 0);

	        glDrawPixels(params.full_width, params.full_height, imgFormat, GL_UNSIGNED_BYTE, rgba);
        }
        glViewport(iViewport[0], iViewport[1], iViewport[2], iViewport[3]);

	    if(transparent) glDisable(GL_BLEND);
		glPopMatrix();
	}
    return true;
} //draw()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Write the Image to the file
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void DisplayBuffer::write(const string& filename) {
#ifndef NOPNG
	int w = params.full_width;
	int h = params.full_height;
    int reg_width  = params.use_border ? params.border.z - params.border.x : params.full_width,
        reg_height = params.use_border ? params.border.w - params.border.y : params.full_height;

	if(w == 0 || h == 0) return;

	// Read buffer from server
    int components_cnt;
	if(!server->getImgBuffer8bit(components_cnt, rgba, w, h, reg_width, reg_height)) return;
    if(!rgba) return;

    int imgFormat;
    switch(components_cnt) {
        case 1:
            imgFormat = PNG_COLOR_TYPE_GRAY;
            break;
        case 2:
            imgFormat = PNG_COLOR_TYPE_GRAY_ALPHA;
            break;
        case 3:
            imgFormat = PNG_COLOR_TYPE_RGB;
            break;
        case 4:
            imgFormat = PNG_COLOR_TYPE_RGBA;
            break;
        default:
            imgFormat = PNG_COLOR_TYPE_GRAY;
            break;
    }

	// Write image
    std::string full_path = filename + "interactive_session.png";

    unsigned char *buf          = rgba;
	unsigned rowbytes           = reg_width * 4;
	unsigned char **rows_buf    = new unsigned char*[reg_height * sizeof(unsigned char*)];

	for(int i = 0; i < reg_height; ++i) rows_buf[i] = &buf[(reg_height - i - 1) * rowbytes];
	png_structp png_ptr = NULL;
	png_infop info_ptr  = NULL;
	png_bytep *rows     = rows_buf;

#if not defined(MAX_PATH)
#   define MAX_PATH 512
#endif
    char abs_path[MAX_PATH];
    strncpy(abs_path, full_path.c_str(), MAX_PATH);
	BLI_path_abs(abs_path, G.main->name);

    FILE *fp = NULL;
    if(!(fp = BLI_fopen(abs_path, "wb"))) goto fail;

    if(!png_ptr) {
        if(!(png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL))) goto fail;
    }

    if(!info_ptr) {
        if(!(info_ptr = png_create_info_struct(png_ptr))) goto fail;
    }

    if(setjmp(png_jmpbuf(png_ptr))) goto fail;
    png_init_io(png_ptr, fp);
    png_set_IHDR(png_ptr, info_ptr, reg_width, reg_height, 8, imgFormat, PNG_INTERLACE_NONE, PNG_COMPRESSION_TYPE_BASE, PNG_FILTER_TYPE_BASE);
    png_write_info(png_ptr, info_ptr);
    png_write_image(png_ptr, rows);
    png_write_end(png_ptr, NULL);
    png_destroy_write_struct(&png_ptr, &info_ptr);

	fclose(fp);
    delete[] rows_buf;
    return;

fail:	
	if(fp) fclose(fp);
	if(png_ptr || info_ptr) png_destroy_write_struct(&png_ptr, &info_ptr);
    delete[] rows_buf;
#endif // NOPNG
} //write()

OCT_NAMESPACE_END

