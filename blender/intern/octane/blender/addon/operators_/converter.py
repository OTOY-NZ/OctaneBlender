# <pep8 compliant>

import bpy
from bpy.utils import register_class, unregister_class
from bpy.types import Operator
from octane.utils.converters import convert_to_octane_material
from octane.nodes.base_node_tree import NodeTreeHandler
from octane.uis.widget import OctaneProgressWidget


class OCTANE_OT_convert_to_octane_material(Operator):
    """Try to convert current material to compatible Octane material if possible. Do nothing if not applicable"""
    bl_idname = "octane.convert_to_octane_material"
    bl_label = "Convert to Octane Material"
    bl_register = True
    bl_undo = False
    USE_PROGRESS_BAR = True
    IS_OPERATOR_RUNNING = False

    def __init__(self):
        super().__init__()
        self.timer = None
        self.done = False
        self.processed_object_names = set()
        self.processed_material_names = set()

    converter_modes = (
        ("MATERIAL", "Only the selected material", "Only the selected material", 0),
        ("SELECTED_OBJECTS", "All materials in the selected objects", "All materials in the selected objects", 1),
        ("SCENE", "All materials in this Scene", "All materials in this Scene", 2),
    )
    converter_mode: bpy.props.EnumProperty(
        name="Converter Type",
        description="Converter Mode",
        items=converter_modes,
        default="MATERIAL",
    )

    def set_progress(self, context, show, value):
        if show:
            OctaneProgressWidget.show(context)
            OctaneProgressWidget.set_progress(context, value)
            OctaneProgressWidget.update(context)
        else:
            OctaneProgressWidget.set_progress(context, 0)
            OctaneProgressWidget.update(context)
            OctaneProgressWidget.hide()

    def start(self, _context):
        self.__class__.IS_OPERATOR_RUNNING = True

    def start_modal_operator(self, context):
        from octane.uis.widget import OctaneProgressWidget
        self.done = False
        self.processed_object_names = set()
        self.processed_material_names = set()
        OctaneProgressWidget.set_task_text(context, "Octane Material Converter")
        self.set_progress(context, True, 0)
        context.window_manager.modal_handler_add(self)
        self.timer = context.window_manager.event_timer_add(0.1, window=context.window)

    def complete(self, context):
        from octane.nodes.base_node_tree import NodeTreeHandler
        NodeTreeHandler.update_node_tree_count(context.scene)
        self.__class__.IS_OPERATOR_RUNNING = False

    def complete_modal_operator(self, context):
        self.complete(context)
        context.window_manager.event_timer_remove(self.timer)
        self.set_progress(context, False, 0)
        self.__class__.IS_OPERATOR_RUNNING = False

    @classmethod
    def poll(cls, _context):
        return not cls.IS_OPERATOR_RUNNING

    def modal(self, context, event):
        if self.done or event.type in {"ESC"}:
            self.complete_modal_operator(context)
            return {"FINISHED"}
        if event.type == 'TIMER':
            done = True
            selected_objs = bpy.context.selected_objects
            for _object in context.scene.objects:
                if _object.name in self.processed_object_names:
                    continue
                if self.converter_mode == "SELECTED_OBJECTS" and _object not in selected_objs:
                    pass
                else:
                    for idx in range(len(_object.material_slots)):
                        cur_material = getattr(_object.material_slots[idx], "material", None)
                        if cur_material:
                            if cur_material.name in self.processed_material_names:
                                continue
                            self.processed_material_names.add(cur_material.name)
                            convert_to_octane_material(_object, idx)
                self.processed_object_names.add(_object.name)
                current_progress = len(self.processed_object_names) * 100.0 / len(context.scene.objects)
                current_progress = max(0.01, min(99.0, current_progress))
                self.set_progress(context, True, current_progress)
                NodeTreeHandler.update_node_tree_count(context.scene)
                done = False
                break
            self.done = done
        return {"PASS_THROUGH"}

    def invoke(self, context, _event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, _context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "converter_mode")

    def execute(self, context):
        self.start(context)
        cur_obj = bpy.context.object
        if self.converter_mode == "MATERIAL":
            if cur_obj and len(cur_obj.material_slots):
                convert_to_octane_material(cur_obj, cur_obj.active_material_index)
            self.complete(context)
            return {"FINISHED"}
        else:
            if self.USE_PROGRESS_BAR:
                self.start_modal_operator(context)
                return {"RUNNING_MODAL"}
            else:
                for _object in context.scene.objects:
                    selected_objs = bpy.context.selected_objects
                    if self.converter_mode == "SELECTED_OBJECTS" and _object not in selected_objs:
                        pass
                    else:
                        for idx in range(len(_object.material_slots)):
                            cur_material = getattr(_object.material_slots[idx], "material", None)
                            if cur_material:
                                self.processed_material_names.add(cur_material.name)
                                convert_to_octane_material(_object, idx)
                self.complete(context)
                return {"FINISHED"}


_CLASSES = [
    OCTANE_OT_convert_to_octane_material,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
