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

#ifndef _MEMLEAKS_CHECK_H_
#define _MEMLEAKS_CHECK_H_

#ifdef WIN32
#   ifdef _DEBUG
#       define DBG_NEW new ( _NORMAL_BLOCK , __FILE__ , __LINE__ )

#	    define _CRTDBG_MAP_ALLOC
#	    define _CRTDBG_MAP_ALLOC_NEW
#	    include <stdlib.h>
#	    include <crtdbg.h>

#       define new DBG_NEW
#   endif //#ifdef _DEBUG
#endif //#ifdef WIN32

#endif //#ifndef _MEMLEAKS_CHECK_H_
