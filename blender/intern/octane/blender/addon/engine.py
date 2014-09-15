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

import bpy


def init():
    import _octane
    import os.path

    path = os.path.dirname(__file__)
    user_path = os.path.dirname(os.path.abspath(bpy.utils.user_resource('CONFIG', '')))

    _octane.init(path, user_path)


def create(cls, engine, data, scene, region=0, v3d=0, rv3d=0):
    import _octane

    userpref = bpy.context.user_preferences.as_pointer()
    if region:
        cur_region = region.as_pointer()
    else:
        cur_region = 0
    if v3d:
        cur_v3d = v3d.as_pointer()
    else:
        cur_v3d = 0
    if rv3d:
        cur_rv3d = rv3d.as_pointer()
    else:
        cur_rv3d = 0

    cls.session = _octane.create(engine.as_pointer(), userpref, data.as_pointer(), scene.as_pointer(), cur_region, cur_v3d, cur_rv3d)


def free(cls, engine):
    if cls.session:
        import _octane
        _octane.free(cls.session)
#        del cls.session
        cls.session = 0


def render(cls, engine):
    import _octane
    _octane.render(cls.session)


def reset(cls, engine, data, scene):
    import _octane
    _octane.reset(cls.session, data.as_pointer(), scene.as_pointer())
    cls.session = 0


def update(cls, engine, data, scene):
    import _octane
    _octane.sync(cls.session)


def draw(cls, engine, region, v3d, rv3d):
    import _octane

    # draw render image
    _octane.draw(cls.session, v3d.as_pointer(), rv3d.as_pointer())


def available_devices():
    import _octane
    return _octane.available_devices()
