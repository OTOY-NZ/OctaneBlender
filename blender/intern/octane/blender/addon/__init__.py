#
# Copyright 2011, Blender Foundation.
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

# <pep8 compliant>

bl_info = {
    "name": "OctaneRender Engine (v. 9.10)",
    "author": "OTOY Inc.",
    "blender": (2, 76, 0),
    "location": "Info header, render engine menu",
    "description": "OctaneRender Engine integration",
    "warning": "",
    "wiki_url": "https://docs.otoy.com/#34Introduction%20%E2%80%93%20Blender%20Plugin",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Render"}

import bpy
from . import types, ui, properties, engine, presets


def register():
    from . import ui
    from . import properties
    from . import presets

    engine.init()

    properties.register()
    ui.register()
    presets.register()
    bpy.utils.register_module(__name__)


def unregister():
    from . import ui
    from . import properties
    from . import presets

    ui.unregister()
    properties.unregister()
    presets.unregister()
    bpy.utils.unregister_module(__name__)
