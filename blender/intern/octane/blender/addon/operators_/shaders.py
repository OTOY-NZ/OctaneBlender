# <pep8 compliant>

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class OCTANE_OT_use_shading_nodes(Operator):
    """Enable nodes on a material, world or light"""
    bl_idname = "octane.use_shading_nodes"
    bl_label = "Use Nodes"

    @classmethod
    def poll(cls, context):
        return (getattr(context, "material", False) or getattr(context, "world", False) or
                getattr(context, "light", False))

    def execute(self, context):
        if context.material:
            context.material.use_nodes = True
        elif context.world:
            context.world.use_nodes = True
        elif context.light:
            context.light.use_nodes = True

        return {'FINISHED'}


_CLASSES = [
    OCTANE_OT_use_shading_nodes,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
