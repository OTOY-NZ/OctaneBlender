# <pep8 compliant>

import os
import bpy
import mathutils
import xml.etree.ElementTree as ET
from bpy_extras.io_utils import ExportHelper
from bpy.app.handlers import persistent
from bpy.types import Operator
from bpy.props import IntProperty, BoolProperty, StringProperty
from octane import core
from octane.utils import consts, utility

COMMAND_TYPES = {
	'SHOW_NODEGRAPH': 1,
	'SHOW_NETWORK_PREFERENCE': 2,
	'STOP_RENDERING': 3,
	'SHOW_LOG': 4,
	'SHOW_DEVICE_SETTINGS': 5,
	'SHOW_OCTANEDB': 6,	
	'ACTIVATE': 7,
    'SAVE_OCTANEDB': 8,
    'SHOW_OCTANE_VIEWPORT': 9,
    'CLEAR_RESOURCE_CACHE_SYSTEM': 10,
}

EXPORT_TYPES = {
    'ALEMBIC': 1,
    'ORBX': 2,    
}


def set_mesh_resource_cache_tag(obj, is_dirty):    
    if obj and obj.type in ('MESH', ):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            if hasattr(cur_octane_mesh_data, 'resource_dirty_tag'):            
                cur_octane_mesh_data.resource_dirty_tag = is_dirty

def generate_resource_data_hash_tag(obj):
    resource_data_hash_tag = ''
    if obj and obj.type in ('MESH', ):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            material_resource_hash_tag = ''
            sphere_primitive_hash_tag = ''
            for mat in obj.material_slots:
                material_resource_hash_tag += (mat.name + ",")            
            sphere_primitive_hash_tag_1 = "[%d-%d-%f]" % (obj.data.octane_enable_sphere_attribute, obj.data.octane_hide_original_mesh, obj.data.octane_sphere_radius)
            sphere_primitive_hash_tag_2 = "[%d-%d-%f-%f]" % (obj.data.octane_use_randomized_radius, obj.data.octane_sphere_randomized_radius_seed, obj.data.octane_sphere_randomized_radius_min, obj.data.octane_sphere_randomized_radius_max)
            sphere_primitive_hash_tag = sphere_primitive_hash_tag_1 + sphere_primitive_hash_tag_2
            resource_data_hash_tag = material_resource_hash_tag + sphere_primitive_hash_tag
    return resource_data_hash_tag

def is_resource_data_hash_tag_updated(obj, cur_resource_data_hash_tag):
    if obj and obj.type in ('MESH', ):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            return cur_resource_data_hash_tag != cur_octane_mesh_data.resource_data_hash_tag
    return True

def update_resource_data_hash_tag_updated(obj, cur_resource_data_hash_tag):
    if obj and obj.type in ('MESH', ):
        cur_octane_mesh_data = getattr(obj.data, 'octane', None)
        if cur_octane_mesh_data:
            cur_octane_mesh_data.resource_data_hash_tag = cur_resource_data_hash_tag

def get_dirty_resources():
    resources = []
    for obj in bpy.data.objects:
        if obj and obj.type in ('MESH', ):
            resource_data_hash_tag = generate_resource_data_hash_tag(obj)             
            is_dirty = is_resource_data_hash_tag_updated(obj, resource_data_hash_tag)
            update_resource_data_hash_tag_updated(obj, resource_data_hash_tag)  
            if is_dirty:
                resources.append(obj.data.name)
            else:
                if len(obj.particle_systems):
                    resources.append(obj.data.name)
                else:
                    cur_octane_mesh_data = getattr(obj.data, 'octane', None)
                    if cur_octane_mesh_data:
                        if getattr(cur_octane_mesh_data, 'resource_dirty_tag', False):     
                            resources.append(obj.data.name)    
    return resources                       

def set_all_mesh_resource_cache_tags(is_dirty):
    for obj in bpy.data.objects:
        if obj.mode == "OBJECT":
            set_mesh_resource_cache_tag(obj, is_dirty)
        else:
            set_mesh_resource_cache_tag(obj, True)

@persistent
def sync_octane_aov_output_number(self):
    try:
        view_layer = bpy.context.view_layer
        octane_view_layer = view_layer.octane
        composite_node_tree_name = octane_view_layer.aov_output_group_collection.composite_node_tree
        aov_output_group_name = octane_view_layer.aov_output_group_collection.aov_output_group_node
        if composite_node_tree_name in bpy.data.node_groups:
            if aov_output_group_name in bpy.data.node_groups[composite_node_tree_name].nodes:
                bpy.data.node_groups[composite_node_tree_name].check_validity()
                node = bpy.data.node_groups[composite_node_tree_name].nodes[aov_output_group_name]
                octane_view_layer.aov_out_number = int(node.group_number)
    except:
        pass


@persistent
def update_resource_cache_tag(scene):
    obj = None
    try:
        obj = bpy.context.view_layer.objects.active
    except:
        pass
    from . import engine
    if obj and not engine.IS_RENDERING:
        scene = bpy.context.scene
        oct_scene = scene.octane
        if oct_scene.dirty_resource_detection_strategy_type == 'Edit Mode':
            if obj.mode == 'EDIT':
                set_mesh_resource_cache_tag(obj, True)
        else:
            set_mesh_resource_cache_tag(obj, True)


@persistent
def update_blender_volume_grid_info(scene):
    obj = None
    try:
        obj = bpy.context.view_layer.objects.active
    except:
        pass
    if obj and obj.type == 'VOLUME':
        obj.data.octane.octane_vdb_info.update(bpy.context)


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


class OCTANE_OT_BaseCommand(Operator):
    command_type = 0
    bl_register = True
    bl_undo = False	

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane import core
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.client import OctaneBlender
            OctaneBlender().utils_function(self.command_type, "")
            return {'FINISHED'} 
        else:
            import _octane
            scene = context.scene
            oct_scene = scene.octane
            _octane.command_to_octane(self.command_type)   
            return {'FINISHED'}

class OCTANE_OT_ShowOctaneNodeGraph(OCTANE_OT_BaseCommand):
    """Show Octane NodeGraph(VIEW Mode Only. Please DO NOT ADD or DELETE nodes.)"""
    bl_idname = "octane.show_octane_node_graph"
    bl_label = "Show Octane Node Graph"
    command_type = consts.UtilsFunctionType.SHOW_NODEGRAPH

class OCTANE_OT_ShowOctaneViewport(OCTANE_OT_BaseCommand):
    """Show Octane Viewport(Suggest VIEW Mode Only. Camera navigation in the viewport would not synchronize to Blender viewport.)"""
    bl_idname = "octane.show_octane_viewport"
    bl_label = "Show Octane Viewport"
    command_type = consts.UtilsFunctionType.SHOW_VIEWPORT

class OCTANE_OT_ShowOctaneNetworkPreference(OCTANE_OT_BaseCommand):
    """Show Octane Network Preference(For the Studio+ License Only)"""
    bl_idname = "octane.show_octane_network_preference"
    bl_label = "Show Octane Network Preference"
    command_type = consts.UtilsFunctionType.SHOW_NETWORK_PREFERENCE

class OCTANE_OT_StopRender(OCTANE_OT_BaseCommand):
    """Force to stop rendering and empty GPUs"""
    bl_idname = "octane.stop_render"
    bl_label = "Stop Render and Empty GPUs"
    command_type = consts.UtilsFunctionType.STOP_RENDERING

class OCTANE_OT_ShowOctaneLog(OCTANE_OT_BaseCommand):
    """Show Octane Log"""
    bl_idname = "octane.show_octane_log"
    bl_label = "Show Octane Log"
    command_type = consts.UtilsFunctionType.SHOW_LOG

class OCTANE_OT_ShowOctaneDeviceSetting(OCTANE_OT_BaseCommand):
    """Show Octane Device Setting"""
    bl_idname = "octane.show_octane_device_setting"
    bl_label = "Show Octane Device Setting"
    command_type = consts.UtilsFunctionType.SHOW_DEVICE_SETTINGS

class OCTANE_OT_ActivateOctane(OCTANE_OT_BaseCommand):
    """Activate the Octane license"""
    bl_idname = "octane.activate"
    bl_label = "Open activation state dialog on OctaneServer"
    command_type = consts.UtilsFunctionType.SHOW_ACTIVATION

class OCTANE_OT_ToggleRecord(OCTANE_OT_BaseCommand):
    """DEBUG: Toggle Record"""
    bl_idname = "octane.toggle_record"
    bl_label = "Toggle Record"
    command_type = consts.UtilsFunctionType.TOGGLE_RECORD

class OCTANE_OT_PlayRecord(OCTANE_OT_BaseCommand):
    """DEBUG: Play Record"""
    bl_idname = "octane.play_record"
    bl_label = "Play Record"
    command_type = consts.UtilsFunctionType.PLAY_RECORD


class OCTANE_OT_ClearResourceCache(Operator):
    """Clear the Resource Cache"""
    bl_idname = "octane.clear_resource_cache"
    bl_label = "Clear"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane.core import resource_cache
        resource_cache.reset_resource_cache(None)
        return {'FINISHED'}     


class OCTANE_OT_ShowOctaneDB(OCTANE_OT_BaseCommand):
    """Show the Octane DB"""
    bl_idname = "octane.open_octanedb"
    bl_label = "Open Octane DB(LiveDB and LocalDB)"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane.core.octanedb import OctaneDBManager
        OctaneDBManager().open_octanedb()
        return {'FINISHED'} 


class OCTANE_OT_SaveOctaneDB(bpy.types.Operator):
    """Save current material as OctaneDB"""
    bl_idname = "octane.save_as_octanedb"
    bl_label = "Save as OctaneDB"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        scene = context.scene
        oct_scene = scene.octane                
        cur_obj = bpy.context.object
        if cur_obj and len(cur_obj.material_slots):                    
            cur_material = cur_obj.material_slots[cur_obj.active_material_index].material
            data = context.blend_data.as_pointer()
            prefs = bpy.context.preferences.as_pointer()                   
            ret = _octane.export_localdb(scene.as_pointer(), context.as_pointer(), prefs, data, cur_material.as_pointer())   
        return {'FINISHED'}  


class OCTANE_OT_UpdateOSLCameraNodeCollections(bpy.types.Operator):
    bl_idname = 'update.osl_camera_nodes'
    bl_label = ''
    def invoke(self, context, event):
        cam = context.camera
        oct_cam = cam.octane
        oct_cam.osl_camera_node_collections.update_nodes(context)
        return {'FINISHED'}

class OCTANE_OT_UpdateAovOutputGroupCollections(bpy.types.Operator):
    bl_idname = 'update.aov_output_group_nodes'
    bl_label = ''
    def invoke(self, context, event):
        view_layer = context.view_layer
        oct_view_layer = view_layer.octane
        oct_view_layer.aov_output_group_collection.update_nodes(context)
        return {'FINISHED'}        

class OCTANE_OT_UpdateOctaneGeoNodeCollections(bpy.types.Operator):
    bl_idname = 'update.octane_geo_nodes'
    bl_label = ''
    def invoke(self, context, event):
        current_object = context.active_object
        if current_object and current_object.data and getattr(current_object.data, 'octane', None):
            current_object.data.octane.octane_geo_node_collections.update_nodes(context)
        return {'FINISHED'}

class OCTANE_OT_SetMeshesType(Operator):
    """Set selected meshes to the same type"""
    bl_idname = "octane.set_meshes_type"
    bl_label = "To selected"
    bl_register = True
    bl_undo = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        data = context.blend_data
        sel_len = len(bpy.context.selected_objects)
        if sel_len > 1:
            _octane.set_meshes_type(data.as_pointer(), int(bpy.context.object.data.octane.mesh_type))
        return {'FINISHED'}

class OCTANE_OT_SetOctaneShader(Operator):
    """Set selected object to preset octane shader"""
    bl_idname = "octane.set_preset_octane_shader"
    bl_label = "Assign"
    bl_register = True
    bl_undo = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        ob = context.object
        shader_name = context.material.octane.preset_shader_type
        if shader_name != 'None':
            mat_name = 'Octane%sTemplate' % shader_name
            path = os.path.dirname(__file__) + '/libraries/materials/' + shader_name + ".blend"
            with bpy.data.libraries.load(path, link=False) as (data_from, data_to):  
                data_to.materials = data_from.materials               
            for mat in data_to.materials:                                         
                assigned_mat = mat.copy()
                if len(ob.material_slots) < 1:                    
                    ob.data.materials.append(assigned_mat)
                else:                    
                    ob.material_slots[ob.active_material_index].material = assigned_mat                    
        return {'FINISHED'}

class OCTANE_OT_ConvertToOctaneMaterial(bpy.types.Operator):
    """Try to convert current material to compatiable Octane material if possible. Do nothing if not applicable"""
    bl_idname = "octane.convert_to_octane_material"
    bl_label = "Convert to Octane material"
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
        from octane.properties_.scene import OctaneProgressWidget
        if show:
            OctaneProgressWidget.show(context)
            OctaneProgressWidget.set_progress(context, value)
            OctaneProgressWidget.update(context)
        else:
            OctaneProgressWidget.set_progress(context, 0)
            OctaneProgressWidget.update(context)
            OctaneProgressWidget.hide()

    def start(self, context):
        self.__class__.IS_OPERATOR_RUNNING = True

    def start_modal_operator(self, context):
        from octane.properties_.scene import OctaneProgressWidget        
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
    def poll(cls, context):
        return not cls.IS_OPERATOR_RUNNING

    def modal(self, context, event):
        from octane import converters
        from octane.nodes.base_node_tree import NodeTreeHandler
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
                            self.processed_material_names.add(cur_material.name)
                            converters.convert_to_octane_material(_object, idx)
                self.processed_object_names.add(_object.name)
                current_progress = len(self.processed_object_names) * 100.0 / len(context.scene.objects)
                current_progress = max(0.01, min(99, current_progress))
                self.set_progress(context, True, current_progress)
                NodeTreeHandler.update_node_tree_count(context.scene)                
                done = False
                break
            self.done = done
        return {"PASS_THROUGH"}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = layout.row()
        row.prop(self, "converter_mode")

    def execute(self, context):
        from octane import converters
        self.start(context)
        scene = context.scene
        oct_scene = scene.octane                
        cur_obj = bpy.context.object
        if self.converter_mode == "MATERIAL":
            if cur_obj and len(cur_obj.material_slots):
                converters.convert_to_octane_material(cur_obj, cur_obj.active_material_index)
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
                                converters.convert_to_octane_material(_object, idx)
                self.complete(context)
                return {"FINISHED"}


class OCTANE_OT_BaseExport(Operator, ExportHelper):
    export_type = 0
    filename_ext = '.orbx'
    filepath: StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ORBX_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ORBX_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ORBX_END

    def execute(self, context):
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            from octane.core.session import RenderSession
            from octane.core.client import OctaneBlender
            if not self.filepath.endswith(self.filename_ext):
                self.filepath += self.filename_ext
            session = RenderSession(None)
            session.session_type = consts.SessionType.EXPORT
            session.start_render(context.scene, is_viewport=False)
            OctaneBlender().utils_function(consts.UtilsFunctionType.RENDER_STOP, "")
            frame_start = context.scene.frame_start
            frame_end = context.scene.frame_end
            for frame in range(frame_start, frame_end + 1):
                context.scene.frame_set(frame)                        
                depsgraph = context.evaluated_depsgraph_get()
                scene = depsgraph.scene_eval
                layer = depsgraph.view_layer_eval
                width = utility.render_resolution_x(scene)
                height = utility.render_resolution_y(scene)
                session.render_update(depsgraph, scene, layer)
                session.set_resolution(width, height, True)
                if frame == scene.frame_start:
                    OctaneBlender().utils_function(self.EXPORT_START, self.filepath)
                OctaneBlender().utils_function(self.EXPORT_WRITE_FRAME, self.filepath)
                # print("self.EXPORT_WRITE_FRAME", self.EXPORT_WRITE_FRAME)
                # print("Export Frame: %d / [%d, %d]" % (frame, frame_start, frame_end))
            response = OctaneBlender().utils_function(self.EXPORT_END, self.filepath)
            success = False
            if len(response):
                success = int(ET.fromstring(response).get("result"))
            if success:
                self.report({"INFO"}, "Export Success: %s" % self.filepath)
            else:
                self.report({'ERROR'}, "Export Error: %s" % self.filepath)
            session.stop_render()
            return {'FINISHED'}
        else:
            import _octane
            scene = context.scene            
            data = context.blend_data.as_pointer()
            prefs = bpy.context.preferences.as_pointer()
            if not self.filepath.endswith(self.filename_ext):
                self.filepath += self.filename_ext
            _octane.export(scene.as_pointer(), context.as_pointer(), prefs, data, self.filepath, self.export_type)
            return {'FINISHED'}             

    def invoke(self, context, event):
        filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        if filename == '':
            filename = 'octane_export'     
        filename = bpy.path.clean_name(filename)           
        self.filename = bpy.path.ensure_ext(filename, self.filename_ext)    
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class OCTANE_OT_OrbxExport(OCTANE_OT_BaseExport):
    """Export current scene in Octane ORBX format"""
    export_type = EXPORT_TYPES['ORBX']
    filename_ext = '.orbx'    
    bl_idname = "export.orbx"
    bl_label = "Octane Orbx(.orbx)"
    bl_description = "Export current scene in Octane ORBX format"
    filter_glob: StringProperty(default="*.orbx", options={'HIDDEN'}) 
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ORBX_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ORBX_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ORBX_END

class OCTANE_OT_AlembicExport(OCTANE_OT_BaseExport):
    """Export current scene in Octane alembic format"""
    export_type = EXPORT_TYPES['ALEMBIC']
    filename_ext = '.abc'    
    bl_idname = "export.abc"
    bl_label = "Octane Alembic(.abc)"   
    bl_description = "Export current scene in Octane Alembic format"
    filter_glob: StringProperty(default="*.abc", options={'HIDDEN'})     
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')   
    EXPORT_START = consts.UtilsFunctionType.EXPORT_ALEMBIC_START
    EXPORT_WRITE_FRAME = consts.UtilsFunctionType.EXPORT_ALEMBIC_WRITE_FRAME
    EXPORT_END = consts.UtilsFunctionType.EXPORT_ALEMBIC_END

class OCTANE_OT_OrbxPreivew(Operator):
    """Generate Orbx Preview Mesh(The current mesh data will be replaced with the preview data. The current object's delta matrix may be updated according to the orbx settings.)"""
    bl_idname = "octane.generate_orbx_preview"
    bl_label = "Generate Orbx Preview"
    bl_register = True
    bl_undo = True

    def clear_abc(self, imported_abc):
        pending_nodes = []
        resource_names = []
        pending_nodes.append(imported_abc)
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            resource_names.append(cur_node.name)
            for sub_node in cur_node.children:
                pending_nodes.append(sub_node)
        for name in resource_names:
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)

    def find_mesh_data(self, imported_abc):
        pending_nodes = []
        pending_nodes_matrix = []
        mesh_and_matrix_data = []
        pending_nodes.append(imported_abc)
        pending_nodes_matrix.append(imported_abc.matrix_world)
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            if cur_node.type == "MESH":
                mesh_and_matrix_data.append((cur_node.data, cur_node.matrix_world.inverted()))
            for sub_node in cur_node.children:
                pending_nodes.append(sub_node)
        return mesh_and_matrix_data    

    def reorganize_alembic_mesh_data(self, current_obj, imported_abc):
        default_matrix = mathutils.Matrix()
        empty_mesh_data = current_obj.data.copy()
        empty_mesh_data.clear_geometry()
        empty_mesh_data.name = "[OrbxPreview]%s" % current_obj.name
        children_names = []
        for child in current_obj.children:
            children_names.append(child.name)
        for name in children_names:
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink=True)           
        current_obj.data = empty_mesh_data
        pending_nodes = []
        pending_nodes.append(imported_abc)
        empty_resources = []
        while len(pending_nodes):
            cur_node = pending_nodes.pop(0)
            if cur_node.type == "EMPTY":
                if cur_node.matrix_world == default_matrix:
                    for sub_node in cur_node.children:
                        pending_nodes.append(sub_node)
                    empty_resources.append(cur_node.name)
                else:
                    cur_node.parent = current_obj
            if cur_node.type == "MESH":
                cur_node.parent = current_obj
                cur_node.data.octane.external_alembic_mesh_tag = True
                if len(cur_node.constraints) == 0:
                    constraint = cur_node.constraints.new("TRANSFORM")
                    constraint.target = current_obj
                    constraint.to_min_x = constraint.to_max_x = cur_node.location.x
                    constraint.to_min_y = constraint.to_max_y = cur_node.location.y
                    constraint.to_min_z = constraint.to_max_z = cur_node.location.z
                    constraint.to_min_x_rot = constraint.to_max_x_rot = cur_node.rotation_euler.x
                    constraint.to_min_y_rot = constraint.to_max_y_rot = cur_node.rotation_euler.y
                    constraint.to_min_z_rot = constraint.to_max_z_rot = cur_node.rotation_euler.z
                    constraint.to_min_x_scale = constraint.to_max_x_scale = cur_node.scale.x
                    constraint.to_min_y_scale = constraint.to_min_y_scale = cur_node.scale.y
                    constraint.to_min_z_scale = constraint.to_min_z_scale = cur_node.scale.z     
                    constraint.mix_mode = 'REPLACE'
                    constraint.target_space = 'LOCAL'
                    constraint.owner_space = 'LOCAL'
                cur_node.data.update_tag()
        return empty_resources

    def copy_mesh_data_from_abc(self, current_obj, imported_abc):    
        import mathutils    
        imported_abc.matrix_world = mathutils.Matrix()
        mesh_data_list = self.find_mesh_data(imported_abc)
        if len(mesh_data_list):
            current_obj.data = mesh_data_list[0][0]
            current_obj.data.octane.enable_octane_offset_transform = True
            offset_matrix = mesh_data_list[0][1]
            current_obj.data.octane.octane_offset_translation = offset_matrix.to_translation()
            current_obj.data.octane.octane_offset_rotation = offset_matrix.to_euler('YXZ')
            current_obj.data.octane.octane_offset_scale = offset_matrix.to_scale()
            current_obj.data.octane.octane_offset_rotation_order = '2'

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        import os
        import time
        current_obj = context.active_object
        current_obj_name = current_obj.name
        if current_obj.data and len(current_obj.data.octane.imported_orbx_file_path):
            orbx_path = current_obj.data.octane.imported_orbx_file_path
            orbx_path = bpy.path.abspath(orbx_path)
            if (os.path.exists(orbx_path)):                
                abc_filename = 'ORBX_PREVIEW_%s_%d.abc' % (current_obj_name, int(time.time()) % 10000)
                if current_obj.data.octane.orbx_preview_type == "External Alembic":
                    if len(current_obj.data.octane.converted_alembic_asset_path) == 0:
                        base_dir = bpy.path.abspath("//")
                        if base_dir == '':
                            abc_dir = bpy.context.preferences.filepaths.temporary_directory
                        else:
                            abc_dir = base_dir
                    else:
                        abc_dir = bpy.path.abspath(current_obj.data.octane.converted_alembic_asset_path)
                else:
                    abc_dir = bpy.app.tempdir
                abc_path = os.path.join(abc_dir, abc_filename)
                try:
                    if (os.path.exists(abc_path)):
                        os.remove(abc_path)
                except:
                    pass
                abc_path = bpy.path.abspath(abc_path)
                _octane.orbx_preview(orbx_path, abc_path, bpy.context.scene.render.fps)
                if (os.path.exists(abc_path)):
                    bpy.ops.wm.alembic_import(filepath=abc_path, validate_meshes=True, as_background_job=False, set_frame_range=False)
                    imported_abc = context.active_object
                    imported_abc_name = imported_abc.name
                    current_obj = bpy.data.objects[current_obj_name]
                    imported_abc = bpy.data.objects[imported_abc_name]
                    if current_obj.data.octane.orbx_preview_type == "External Alembic":
                        empty_resources = self.reorganize_alembic_mesh_data(current_obj, imported_abc)
                        for resource_name in empty_resources:
                            bpy.data.objects.remove(bpy.data.objects[resource_name], do_unlink=True)    
                    else:
                        self.copy_mesh_data_from_abc(current_obj, imported_abc)
                        self.clear_abc(imported_abc)
                    current_obj.data.octane.imported_orbx_file_path = orbx_path
                    current_obj.select_set(True)                    
                    # os.remove(abc_path)
        return {'FINISHED'}


class OCTANE_OT_SaveAsAddonFile(Operator):
    """Save this file as an OctaneBlender Addon compatible blend file"""
    bl_idname = "octane.save_as_addon_file"
    bl_label = "Save As"
    postfix = "_addon"
    filename: StringProperty()
    filepath: StringProperty(subtype="FILE_PATH")

    def convert_to_addon_file(self, context):
        for node_tree in bpy.data.node_groups:
            utility.convert_to_addon_node_tree(node_tree, node_tree, context, self.report)        
        for material in bpy.data.materials:
            if material.node_tree and material.use_nodes:
                utility.convert_to_addon_node_tree(material, material.node_tree, context, self.report)
        for world in bpy.data.worlds:
            if world.node_tree and world.use_nodes:
                utility.convert_to_addon_node_tree(world, world.node_tree, context, self.report)
        for light in bpy.data.lights:
            if light.node_tree and light.use_nodes:
                utility.convert_to_addon_node_tree(light, light.node_tree, context, self.report)

    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=self.filepath, check_existing=True, copy=False)
        self.convert_to_addon_file(context)
        bpy.ops.wm.save_mainfile(filepath=self.filepath, check_existing=False)
        return {'FINISHED'}          

    def invoke(self, context, event):
        filename = bpy.path.basename(bpy.data.filepath)
        if filename == "":
            filename = "octane_addon_file"                
        filename = bpy.path.display_name(filename, has_ext=False, title_case=False)
        filename = os.path.splitext(filename)[0]
        filename = filename + self.postfix
        filename = bpy.path.clean_name(filename)
        self.filename = bpy.path.ensure_ext(filename, ".blend")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class OCTANE_OT_LoadOctaneStartup(Operator):
    """Load the Octane Startup blend file"""
    bl_idname = "octane.load_octane_startup"
    bl_label = "Load Octane Startup"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        addon_folder = utility.get_addon_folder()
        path = os.path.join(addon_folder, r"assets/startup.blend")
        path = bpy.path.abspath(path)
        bpy.ops.wm.read_homefile(filepath=path)
        return {"FINISHED"}


class OCTANE_OT_QuickAddOctaneGeometry(Operator):
    geometry_node_bl_idname = ""
    default_object_name = ""
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from octane.nodes.base_node_tree import NodeTreeHandler
        bpy.ops.mesh.primitive_cube_add()
        proxy_object = context.active_object
        proxy_object.name = "OctaneGeometry[%s]" % self.default_object_name
        proxy_object.display_type = "WIRE"        
        material = bpy.data.materials.new(proxy_object.name + "_Material")
        material.use_nodes = True
        NodeTreeHandler._on_material_new(material.node_tree, material)
        NodeTreeHandler.update_node_tree_count(context.scene)
        proxy_object.data.materials.append(material)
        geometry_node = material.node_tree.nodes.new(self.geometry_node_bl_idname)
        owner_type = utility.get_node_tree_owner_type(material)
        active_output_node = utility.find_active_output_node(material.node_tree, owner_type)
        default_material_node = active_output_node.inputs["Surface"].links[0].from_node
        material.node_tree.links.new(geometry_node.outputs[0], active_output_node.inputs["Displacement"])
        for socket in geometry_node.inputs:
            if socket.octane_pin_type == consts.PinType.PT_MATERIAL:
                material.node_tree.links.new(default_material_node.outputs[0], socket)
        utility.beautifier_nodetree_layout_by_owner(material)
        octane_geo_node_collections = proxy_object.data.octane.octane_geo_node_collections
        octane_geo_node_collections.node_graph_tree = material.name
        octane_geo_node_collections.osl_geo_node = geometry_node.name
        return {"FINISHED"}


class OCTANE_OT_QuickAddOctaneVectron(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Vectron® to the scene"""
    bl_idname = "octane.quick_add_octane_vectron"
    bl_label = "Vectron®"
    geometry_node_bl_idname = "OctaneVectron"
    default_object_name = "Vectron"

class OCTANE_OT_QuickAddOctaneBox(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Box to the scene"""
    bl_idname = "octane.quick_add_octane_box"
    bl_label = "Box"
    geometry_node_bl_idname = "OctaneSDFBox"
    default_object_name = "Box"

class OCTANE_OT_QuickAddOctaneCapsule(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Capsule to the scene"""
    bl_idname = "octane.quick_add_octane_capsule"
    bl_label = "Capsule"
    geometry_node_bl_idname = "OctaneSDFCapsule"
    default_object_name = "Capsule"

class OCTANE_OT_QuickAddOctaneCylinder(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Cylinder to the scene"""
    bl_idname = "octane.quick_add_octane_cylinder"
    bl_label = "Cylinder"
    geometry_node_bl_idname = "OctaneSDFCylinder"
    default_object_name = "Cylinder"

class OCTANE_OT_QuickAddOctanePrism(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Prism to the scene"""
    bl_idname = "octane.quick_add_octane_prism"
    bl_label = "Prism"
    geometry_node_bl_idname = "OctaneSDFPrism"
    default_object_name = "Prism"

class OCTANE_OT_QuickAddOctaneSphere(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Sphere to the scene"""
    bl_idname = "octane.quick_add_octane_sphere"
    bl_label = "Sphere"
    geometry_node_bl_idname = "OctaneSDFSphere"
    default_object_name = "Sphere"

class OCTANE_OT_QuickAddOctaneTorus(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Torus to the scene"""
    bl_idname = "octane.quick_add_octane_torus"
    bl_label = "Torus"
    geometry_node_bl_idname = "OctaneSDFTorus"
    default_object_name = "Torus"

class OCTANE_OT_QuickAddOctaneTube(OCTANE_OT_QuickAddOctaneGeometry):
    """Add an Octane Tube to the scene"""
    bl_idname = "octane.quick_add_octane_tube"
    bl_label = "Tube"
    geometry_node_bl_idname = "OctaneSDFTube"
    default_object_name = "Tube"


class OCTANE_OT_QuickAddOctaneLight(Operator):
    bl_register = True
    bl_undo = False
    light_typename = ""

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        pass

    def execute(self, context):
        # Create new light datablock.
        light_data = bpy.data.lights.new(name=self.bl_label, type=self.light_typename)
        # Create new object with our light datablock.
        light_object = bpy.data.objects.new(name=self.bl_label, object_data=light_data)
        # Link light object to the active collection of current view layer,
        # so that it'll appear in the current scene.
        view_layer = context.view_layer
        view_layer.active_layer_collection.collection.objects.link(light_object)
        # Place light to a specified location.
        light_object.location = context.scene.cursor.location
        # And finally select it and make it active.
        bpy.ops.object.select_all(action="DESELECT")
        light_object.select_set(True)
        view_layer.objects.active = light_object
        self.update_octane_light(light_data)
        return {"FINISHED"}


class OCTANE_OT_QuickAddOctaneToonPointLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane ToonPoint Light to the scene"""
    bl_idname = "octane.quick_add_octane_toon_point_light"
    bl_label = "Octane Toon Point Light"
    light_typename = "POINT"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_point_light_type = "Toon Point"
        light_data.shadow_soft_size = 0.0
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneToonDirectionalLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane ToonDirectional Light to the scene"""
    bl_idname = "octane.quick_add_octane_toon_directional_light"
    bl_label = "Octane Toon Directional Light"
    light_typename = "SUN"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_directional_light_type = "Toon Directional"
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneDirectionalLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane Directional Light to the scene"""
    bl_idname = "octane.quick_add_octane_directional_light"
    bl_label = "Octane Directional Light"
    light_typename = "SUN"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_directional_light_type = "Directional"
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneSpotLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane SpotLight to the scene"""
    bl_idname = "octane.quick_add_octane_spot_light"    
    bl_label = "Octane SpotLight"
    light_typename = "SPOT"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneAreaLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane Area Light to the scene"""
    bl_idname = "octane.quick_add_octane_area_light"    
    bl_label = "Octane Area Light"
    light_typename = "AREA"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        light_data.size = 1.0
        light_data.use_nodes = True
        

class OCTANE_OT_QuickAddOctaneSphereLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane Sphere Light to the scene"""
    bl_idname = "octane.quick_add_octane_sphere_light"    
    bl_label = "Octane Sphere Light"
    light_typename = "POINT"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_point_light_type = "Sphere"
        light_data.shadow_soft_size = 1.0
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneMeshLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane Mesh Light to the scene"""
    bl_idname = "octane.quick_add_octane_mesh_light"    
    bl_label = "Octane Mesh Light"
    light_typename = "AREA"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.used_as_octane_mesh_light = True
        light_data.size = 0
        light_data.use_nodes = True


class OCTANE_OT_QuickAddOctaneAnalyticalLight(OCTANE_OT_QuickAddOctaneLight):
    """Add an Octane Analytical Light to the scene"""
    bl_idname = "octane.quick_add_octane_analytical_light"
    bl_label = "Octane Analytical Light"
    light_typename = "POINT"
    bl_register = True
    bl_undo = False 

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_point_light_type = "Analytical"
        light_data.shadow_soft_size = 0.0
        light_data.use_nodes = True


def new_menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(OCTANE_OT_LoadOctaneStartup.bl_idname, text="Octane Default Startup")


def export_menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(OCTANE_OT_OrbxExport.bl_idname, text="Octane Orbx(.orbx)")
    self.layout.operator(OCTANE_OT_AlembicExport.bl_idname, text="Octane Alembic(.abc)")
    if not core.ENABLE_OCTANE_ADDON_CLIENT:
        self.layout.operator(OCTANE_OT_SaveAsAddonFile.bl_idname, text="OctaneBlender Addon(.blend)")


classes = (
    OCTANE_OT_use_shading_nodes,

    OCTANE_OT_ShowOctaneNodeGraph,
    OCTANE_OT_ShowOctaneViewport,
    OCTANE_OT_ShowOctaneNetworkPreference,
    OCTANE_OT_StopRender,
    OCTANE_OT_ShowOctaneLog,
    OCTANE_OT_ShowOctaneDeviceSetting,
    OCTANE_OT_ActivateOctane,
    OCTANE_OT_ShowOctaneDB,
    OCTANE_OT_SaveOctaneDB,
    OCTANE_OT_ClearResourceCache,
    OCTANE_OT_ToggleRecord,
    OCTANE_OT_PlayRecord,

    OCTANE_OT_UpdateOctaneGeoNodeCollections,
    OCTANE_OT_UpdateOSLCameraNodeCollections,
    OCTANE_OT_UpdateAovOutputGroupCollections,

    OCTANE_OT_SetMeshesType,
    OCTANE_OT_SetOctaneShader,
    OCTANE_OT_ConvertToOctaneMaterial,

    OCTANE_OT_OrbxExport,
    OCTANE_OT_AlembicExport,

    OCTANE_OT_OrbxPreivew,

    OCTANE_OT_SaveAsAddonFile,
    OCTANE_OT_LoadOctaneStartup,

    OCTANE_OT_QuickAddOctaneVectron,
    OCTANE_OT_QuickAddOctaneBox,
    OCTANE_OT_QuickAddOctaneCapsule,
    OCTANE_OT_QuickAddOctaneCylinder,
    OCTANE_OT_QuickAddOctanePrism,
    OCTANE_OT_QuickAddOctaneSphere,
    OCTANE_OT_QuickAddOctaneTorus,
    OCTANE_OT_QuickAddOctaneTube,

    OCTANE_OT_QuickAddOctaneToonPointLight,
    OCTANE_OT_QuickAddOctaneToonDirectionalLight,
    OCTANE_OT_QuickAddOctaneDirectionalLight,
    OCTANE_OT_QuickAddOctaneSpotLight,
    OCTANE_OT_QuickAddOctaneAreaLight,
    OCTANE_OT_QuickAddOctaneSphereLight,
    OCTANE_OT_QuickAddOctaneMeshLight,
    OCTANE_OT_QuickAddOctaneAnalyticalLight,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.TOPBAR_MT_file_new.append(new_menu_func)
    bpy.types.TOPBAR_MT_file_export.append(export_menu_func)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    bpy.types.TOPBAR_MT_file_new.remove(new_menu_func)
    bpy.types.TOPBAR_MT_file_export.remove(export_menu_func)
