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
#include <string.h>

#include "server.h"

OCT_NAMESPACE_BEGIN

char RenderServer::address[256] = "127.0.0.1";
char RenderServer::out_path[256] = "";


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Create server
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
RenderServer *RenderServer::create(RenderServerInfo& info, bool export_alembic, const char *_out_path, bool interactive) {
	RenderServer *server = new RenderServer(info.net_address, _out_path, export_alembic, interactive);

	if(server) server->info = info;

	return server;
} //create()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get available servers info
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
RenderServerInfo& RenderServer::get_info(void) {
	static RenderServerInfo server_info;
    server_info.description = "Octane render-server";
    server_info.pack_images = true;
    ::strcpy(server_info.net_address, address);

    return server_info;
} //get_info()

OCT_NAMESPACE_END

