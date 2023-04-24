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
 * The Original Code is Copyright (C) 2005 Blender Foundation.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): Robin Allen
 *
 * ***** END GPL LICENSE BLOCK *****
 */

#include "node_shader_util.hh"

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_FLOAT,
     N_("Latitude"),
     -37.043659f,
     0.0f,
     0.0f,
     0.0f,
     -90.0f,
     90.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Longtitude"),
     174.50917f,
     0.0f,
     0.0f,
     0.0f,
     -180.0f,
     180.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT, N_("Month"), 3, 0, 0, 0, 1, 12, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_INT, N_("Day"), 1, 0, 0, 0, 1, 31, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Local time"),
     10.f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     24.f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_INT, N_("GMT offset"), 12, 0, 0, 0, -12, 12, PROP_NONE, SOCK_NO_INTERNAL_LINK},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_VECTOR, N_("OutValue")},
    {SOCK_VECTOR,
     N_("OutTex"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

void register_node_type_val_oct_sun_direction(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_VALUE_SUN_DIRECTION)
    node_type_base(&ntype,
                   SH_NODE_OCT_VALUE_SUN_DIRECTION,
                   "Sun Direction",
                   NODE_CLASS_OCT_VALUE);
  node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size(&ntype, 160, 160, 500);
  node_type_init(&ntype, 0);
  node_type_exec(&ntype, 0, 0, 0);
  

  nodeRegisterType(&ntype);
}
