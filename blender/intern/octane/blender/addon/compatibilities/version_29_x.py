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


def _ensure_default_value_saved(node_tree):
    # Somehow the default_value may not be saved in the .blend file without this code I guess it could be caused
    # by some optimizations on the Blender side This optimization works well if the default value of property is
    # unchanged. But if we change the default value in the future, the unsaved values will be updated to the new
    # default values, making inconsistent render results.
    for node in node_tree.nodes:
        for _input in node.inputs:
            if hasattr(_input, "default_value"):
                _input.default_value = _input.default_value


def ensure_default_value_saved(file_version):
    if not check_update(file_version, '29.16.1'):
        return
    for material in bpy.data.materials:
        if material.use_nodes:
            _ensure_default_value_saved(material.node_tree)
    for world in bpy.data.worlds:
        if world.use_nodes:
            _ensure_default_value_saved(world.node_tree)
    for light in bpy.data.lights:
        if light.use_nodes:
            _ensure_default_value_saved(light.node_tree)
    for node_group in bpy.data.node_groups:
        _ensure_default_value_saved(node_group)


def check_compatibility_octane_object(file_version):
    check_compatibility_octane_object_29_13_1(file_version)
    ensure_default_value_saved(file_version)
