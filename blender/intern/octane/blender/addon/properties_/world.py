# <pep8 compliant>

import bpy
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from octane.properties_ import legacy
from octane.properties_.common import OctanePropertyGroup


class OctaneWorldPropertyGroup(OctanePropertyGroup, legacy.OctaneLegacyWorldPropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.World.octane = PointerProperty(
            name="OctaneRender World Settings",
            description="OctaneRender world settings",
            type=cls,
        )


    @classmethod
    def unregister(cls):
        del bpy.types.World.octane


_CLASSES = [
    OctaneWorldPropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
