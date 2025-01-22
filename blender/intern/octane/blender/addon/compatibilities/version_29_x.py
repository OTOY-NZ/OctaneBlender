# <pep8 compliant>
import bpy

from octane.compatibilities import check_update
from octane.utils import utility


def do_versions(file_version, _octane_version):
    check_compatibility_octane_object(file_version)


def check_compatibility_octane_object_29_13_1(file_version):
    if not check_update(file_version, "29.13.1"):
        return
    for ob in bpy.data.objects:
        ob_octane = ob.octane
        ob_data_octane = getattr(ob.data, "octane", None)
        if ob_data_octane is not None and getattr(ob_data_octane, "enable_octane_offset_transform", False):
            ob_octane.enable_octane_offset_transform = ob_data_octane.enable_octane_offset_transform
            ob_octane.octane_offset_translation = ob_data_octane.octane_offset_translation
            ob_octane.octane_offset_rotation = ob_data_octane.octane_offset_rotation
            ob_octane.octane_offset_scale = ob_data_octane.octane_offset_scale
            utility.set_enum_int_value(ob_octane,
                                       "octane_offset_rotation_order",
                                       int(ob_data_octane.octane_offset_rotation_order))


def check_compatibility_octane_object(file_version):
    check_compatibility_octane_object_29_13_1(file_version)
