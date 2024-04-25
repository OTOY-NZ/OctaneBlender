# <pep8 compliant>

from bpy.utils import register_class, unregister_class


class OctanePropertyPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = {'octane'}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES


_CLASSES = [
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
