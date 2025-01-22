# <pep8 compliant>

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class OCTANE_OT_sync_motion_blur_to_objects_in_collection(Operator):
    """Do you want to sync the motion blur to all the objects in the collection?"""
    bl_idname = "octane.sync_motion_blur_to_objects_in_collection"
    bl_label = "Do you want to sync the motion blur to all the objects in the collection?"
    bl_options = {'REGISTER', 'INTERNAL'}

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, context):
        ob = context.object
        use_motion_blur = ob.octane.use_motion_blur
        use_deform_motion = ob.octane.use_deform_motion
        if ob.instance_type == 'COLLECTION' and ob.instance_collection:
            for child in ob.instance_collection.all_objects:
                if hasattr(child, 'octane'):
                    child.octane.use_motion_blur = use_motion_blur
                    child.octane.use_deform_motion = use_deform_motion
        return {'FINISHED'}


_CLASSES = [
    OCTANE_OT_sync_motion_blur_to_objects_in_collection,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
