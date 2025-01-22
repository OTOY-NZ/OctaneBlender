# <pep8 compliant>

import os
from xml.etree import ElementTree
import bpy
import mathutils
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from bpy_extras import view3d_utils
from octane import is_render_engine_active
from octane.utils import consts, utility


class OCTANE_OT_material_picker(Operator):
    """Pick the material with the mouse"""
    bl_idname = "octane.material_picker"
    bl_label = "Octane Material Picker"

    def material_picker(self, context, coord):
        scene = context.scene
        region = context.region
        rv3d = context.region_data
        viewlayer = context.view_layer
        dg = context.evaluated_depsgraph_get()
        view_vector = view3d_utils.region_2d_to_vector_3d(region, rv3d, coord)
        ray_origin = view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)
        result, location, normal, index, obj, matrix = scene.ray_cast(dg, ray_origin, view_vector)
        if result:
            for o in context.selected_objects:
                o.select_set(False)
            eval_obj = dg.id_eval_get(obj)
            viewlayer.objects.active = obj.original
            material_idx = eval_obj.data.polygons[index].material_index
            obj.original.active_material_index = material_idx

    def modal(self, context, event):
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        elif event.type in {'LEFTMOUSE', 'PRESS'}:
            context.window.cursor_set("DEFAULT")
            self.material_picker(context, (event.mouse_region_x, event.mouse_region_y))
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.window.cursor_set("DEFAULT")
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, _event):
        if context.area.type == 'VIEW_3D':
            context.window.cursor_set("EYEDROPPER")
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run material picker")
            return {'CANCELLED'}


class OCTANE_OT_focus_picker(Operator):
    """Pick the focus with the mouse"""
    bl_idname = "octane.focus_picker"
    bl_label = "Octane Focus Picker"

    @classmethod
    def poll(cls, context):
        return utility.is_viewport_in_camera_view(context)

    def object_picker(self, context, coord):
        scene = context.scene
        camera = scene.camera
        region = context.region
        rv3d = context.region_data
        dg = context.evaluated_depsgraph_get()
        view_vector = view3d_utils.region_2d_to_vector_3d(region, rv3d, coord)
        ray_origin = view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)
        result, location, normal, index, obj, matrix = scene.ray_cast(dg, ray_origin, view_vector)
        if result:
            camera.data.octane.autofocus = False
            camera.data.dof.focus_object = None
            camera.data.dof.focus_distance = (camera.location - location).length
            scene.update_tag()
            camera.update_tag()

    def modal(self, context, event):
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        elif event.type in {'LEFTMOUSE', 'PRESS'}:
            context.window.cursor_set("DEFAULT")
            self.object_picker(context, (event.mouse_region_x, event.mouse_region_y))
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.window.cursor_set("DEFAULT")
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, _event):
        if context.area.type == 'VIEW_3D':
            context.window.cursor_set("EYEDROPPER")
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run focus picker")
            return {'CANCELLED'}


class OCTANE_OT_whitebalance_picker(Operator):
    """Pick the white balance with the mouse"""
    bl_idname = "octane.whitebalance_picker"
    bl_label = "Octane White Balance Picker"

    @classmethod
    def poll(cls, _context):
        return is_render_engine_active()

    def whitebalance_picker(self, context, event):
        from octane.core.client import OctaneBlender
        scene = context.scene
        region = context.region
        rv3d = context.region_data
        viewlayer = context.view_layer
        x, y = event.mouse_region_x, event.mouse_region_y
        y = region.height - y
        request_et = ElementTree.Element("CryptomattePicker")
        request_et.set("positionX", str(x))
        request_et.set("positionY", str(y))
        xml_data = ElementTree.tostring(request_et, encoding="unicode")
        response = OctaneBlender().utils_function(consts.UtilsFunctionType.UTILS_FUNC_GIZMOS_PICK_WHITEBALANCE, xml_data)
        if len(response):
            response_content = ElementTree.fromstring(response).get("content")
            color = [float(f) for f in response_content.split(" ")]
            camera_data, _ = utility.find_active_imager_data(scene, context)
            if camera_data is not None:
                camera_data.imager.white_balance = color
                scene.update_tag()
                context.scene.camera.update_tag()

    def modal(self, context, event):
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        elif event.type in {'LEFTMOUSE', 'PRESS'}:
            context.window.cursor_set("DEFAULT")
            self.whitebalance_picker(context, event)
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.window.cursor_set("DEFAULT")
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, _event):
        if context.area.type == 'VIEW_3D':
            context.window.cursor_set("EYEDROPPER")
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active View3D not found, cannot run white balance picker")
            return {'CANCELLED'}


# def menu_func(self, context):
#     self.layout.operator(OCTANE_OT_material_picker.bl_idname, text="Material Picker")


_CLASSES = [
    OCTANE_OT_material_picker,
    OCTANE_OT_focus_picker,
    OCTANE_OT_whitebalance_picker,
]


def register():
    for cls in _CLASSES:
        register_class(cls)
    # bpy.types.VIEW3D_MT_view.append(menu_func)


def unregister():
    # bpy.types.VIEW3D_MT_view.remove(menu_func)
    for cls in _CLASSES:
        unregister_class(cls)
