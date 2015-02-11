# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contributor(s): Jacques Beaurain.
#
# ***** END GPL LICENSE BLOCK *****

set(INC
	../include
	../../blenkernel
	../../blenlib
	../../blenfont
	../../imbuf
	../../makesdna
	../../makesrna
	../../windowmanager
	../../gpu
	../../../../intern/guardedalloc
	../../../../intern/opennl/extern
	../../../../intern/utfconv
	../../../../intern/glew-mx
)

set(INC_SYS
	${GLEW_INCLUDE_PATH}
)

set(SRC
	mat_livedb_draw.c
	mat_livedb_edit.c
	mat_livedb_ops.c
	mat_livedb_select.c
	mat_livedb_tools.c
	mat_livedb_tree.c
	mat_livedb_nodes.c
	mat_livedb_net.c
	space_mat_livedb.c

	mat_livedb_intern.h
)

if(WITH_INTERNATIONAL)
	add_definitions(-DWITH_INTERNATIONAL)
endif()

blender_add_lib(bf_editor_space_mat_livedb "${SRC}" "${INC}" "${INC_SYS}")
