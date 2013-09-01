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

    data = data.as_pointer()
    userpref = bpy.context.user_preferences.as_pointer()
    scene = scene.as_pointer()
    if region:
        region = region.as_pointer()
    if v3d:
        v3d = v3d.as_pointer()
    if rv3d:
        rv3d = rv3d.as_pointer()

    cls.session = _octane.create(engine.as_pointer(), userpref, data, scene, region, v3d, rv3d)


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
    data = data.as_pointer()
    scene = scene.as_pointer()
    _octane.reset(cls.session, data, scene)
    cls.session = 0


def update(cls, engine, data, scene):
    import _octane
    _octane.sync(cls.session)


def draw(cls, engine, region, v3d, rv3d):
    import _octane
    v3d = v3d.as_pointer()
    rv3d = rv3d.as_pointer()

    # draw render image
    _octane.draw(cls.session, v3d, rv3d)


def available_devices():
    import _octane
    return _octane.available_devices()
