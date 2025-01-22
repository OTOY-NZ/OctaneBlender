# <pep8 compliant>

import bpy
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class
from octane.properties_.common import OctanePropertyGroup


class OctaneMaterialPropertyGroup(OctanePropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Material.octane = PointerProperty(
            name="Octane Material",
            description="",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Material.octane


_CLASSES = [
    OctaneMaterialPropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
