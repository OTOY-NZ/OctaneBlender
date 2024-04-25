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
#include "node_util.hh"

#include "BKE_image.h"
#include "BKE_node_runtime.hh"
#include "BKE_texture.h"

static bNodeSocketTemplate sh_node_in[] = {
    {SOCK_FLOAT,
     N_("Density"),
     100.0f,
     0.0f,
     0.0f,
     0.0f,
     0.001f,
     10000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Vol. step length"),
     4.0f,
     0.0f,
     0.0f,
     0.0f,
     0.001f,
     10000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Vol. shadow ray step length"),
     4.0f,
     0.0f,
     0.0f,
     0.0f,
     0.001f,
     10000.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Lock step length pins"),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_SHADER,
     N_("Sample position displacement"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_RGBA,
     N_("Absorption Tex"),
     0.72f,
     0.72f,
     0.72f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_BOOLEAN,
     N_("Invert abs."),
     1.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_RGBA,
     N_("Scattering Tex"),
     0.f,
     0.f,
     0.f,
     1.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_FLOAT,
     N_("Phase"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     -1.0f,
     1.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    {SOCK_SHADER,
     N_("Emission"),
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     PROP_NONE,
     SOCK_NO_INTERNAL_LINK},
    /****** LEGACY SOCKETS *****/
    {SOCK_FLOAT,
     N_("Absorption"),
     0.5f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_FLOAT,
     N_("Scattering"),
     0.5f,
     0.0f,
     0.0f,
     0.0f,
     0.0f,
     1.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {SOCK_FLOAT,
     N_("Scale"),
     100.0f,
     0.0f,
     0.0f,
     0.0f,
     0.001f,
     10000.0f,
     PROP_NONE,
     SOCK_HIDDEN | SOCK_UNAVAIL | SOCK_AUTO_HIDDEN__DEPRECATED},
    {-1, ""}};

static bNodeSocketTemplate sh_node_out[] = {
    {SOCK_SHADER, N_("OutMedium")},
    {SOCK_SHADER,
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

void register_node_type_medium_oct_scattering(void)
{
  static bNodeType ntype;

  if (ntype.type != SH_NODE_OCT_SCATTER_MED)
    sh_node_type_base(
        &ntype, SH_NODE_OCT_SCATTER_MED, "Scattering Medium", NODE_CLASS_OCT_MEDIUM);
  blender::bke::node_type_socket_templates(&ntype, sh_node_in, sh_node_out);
  node_type_size_preset(&ntype, blender::bke::eNodeSizePreset::DEFAULT);
  ntype.initfunc = (node_octane_medium_init);
  // node_type_exec(&ntype, 0, 0, 0);
  ntype.updatefunc = (node_octane_medium_update);
  

  nodeRegisterType(&ntype);
} /* register_node_type_medium_oct_scattering() */
