# <pep8 compliant>
import bpy
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from octane.properties_.common import OctanePropertyGroup


class OctaneNodeTreePropertyGroup(OctanePropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.NodeTree.octane = PointerProperty(
            name="Octane NodeTree",
            description="",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.NodeTree.octane


_CLASSES = [
    OctaneNodeTreePropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
