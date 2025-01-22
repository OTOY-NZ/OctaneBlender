# <pep8 compliant>
import bpy
from bpy.utils import register_class, unregister_class


def get_compact_blender_panels():
    exclude_panels = {
        "DATA_PT_light",
        "DATA_PT_area",
        "DATA_PT_camera_dof",
    }
    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)
    return panels


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
    for panel in get_compact_blender_panels():
        panel.COMPAT_ENGINES.add('octane')
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for panel in get_compact_blender_panels():
        if 'octane' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('octane')
    for cls in _CLASSES:
        unregister_class(cls)
