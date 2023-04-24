#
# Copyright 2011-2019 Blender Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# <pep8 compliant>

import os
import bpy
import mathutils    
from bpy.app.handlers import persistent
from bpy.types import Operator
from bpy.props import StringProperty
from . import converters

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
        set_mesh_resource_cache_tag(obj, is_dirty) 

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
                view_layer.octane_aov_out_number = int(node.group_number)    
    except:
        pass

@persistent
def clear_resource_cache_system(self):
    import _octane
    from . import engine
    scene = bpy.context.scene
    oct_scene = scene.octane        
    if not engine.IS_RENDERING:
        print("Clear Octane Resource Cache System")
        # set_all_mesh_resource_cache_tags(True)
        _octane.command_to_octane(COMMAND_TYPES['CLEAR_RESOURCE_CACHE_SYSTEM'])

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
        import _octane
        scene = context.scene
        oct_scene = scene.octane   
        _octane.command_to_octane(self.command_type)   
        return {'FINISHED'} 

class OCTANE_OT_ShowOctaneNodeGraph(OCTANE_OT_BaseCommand):
    """Show Octane NodeGraph(VIEW Mode Only. Please DO NOT ADD or DELETE nodes.)"""
    bl_idname = "octane.show_octane_node_graph"
    bl_label = "Show Octane Node Graph"
    command_type = COMMAND_TYPES['SHOW_NODEGRAPH']

class OCTANE_OT_ShowOctaneViewport(OCTANE_OT_BaseCommand):
    """Show Octane Viewport(Suggest VIEW Mode Only. Camera navigation in the viewport would not synchronize to Blender viewport.)"""
    bl_idname = "octane.show_octane_viewport"
    bl_label = "Show Octane Viewport"
    command_type = COMMAND_TYPES['SHOW_OCTANE_VIEWPORT']

class OCTANE_OT_ShowOctaneNetworkPreference(OCTANE_OT_BaseCommand):
    """Show Octane Network Preference"""
    bl_idname = "octane.show_octane_network_preference"
    bl_label = "Show Octane Network Preference"
    command_type = COMMAND_TYPES['SHOW_NETWORK_PREFERENCE']       

class OCTANE_OT_StopRender(OCTANE_OT_BaseCommand):
    """Force to stop rendering and empty GPUs"""
    bl_idname = "octane.stop_render"
    bl_label = "Stop Render and Empty GPUs"
    command_type = COMMAND_TYPES['STOP_RENDERING']

class OCTANE_OT_ShowOctaneLog(OCTANE_OT_BaseCommand):
    """Show Octane Log"""
    bl_idname = "octane.show_octane_log"
    bl_label = "Show Octane Log"
    command_type = COMMAND_TYPES['SHOW_LOG']

class OCTANE_OT_ShowOctaneDeviceSetting(OCTANE_OT_BaseCommand):
    """Show Octane Device Setting"""
    bl_idname = "octane.show_octane_device_setting"
    bl_label = "Show Octane Device Setting"
    command_type = COMMAND_TYPES['SHOW_DEVICE_SETTINGS']

class OCTANE_OT_ActivateOctane(OCTANE_OT_BaseCommand):
    """Activate the Octane license"""
    bl_idname = "octane.activate"
    bl_label = "Open activation state dialog on OctaneServer"
    command_type = COMMAND_TYPES['ACTIVATE']


class OCTANE_OT_ClearResourceCache(OCTANE_OT_BaseCommand):
    """Clear the Resource Cache"""
    bl_idname = "octane.clear_resource_cache"
    bl_label = "Clear"
    command_type = COMMAND_TYPES['CLEAR_RESOURCE_CACHE_SYSTEM']

    @classmethod
    def poll(cls, context):        
        return True

    def execute(self, context):     
        clear_resource_cache_system(self)        
        return {'FINISHED'}     


class OCTANE_OT_ShowOctaneDB(OCTANE_OT_BaseCommand):
    """Show the Octane DB"""
    bl_idname = "octane.open_octanedb"
    bl_label = "Open Octane DB(LiveDB and LocalDB)"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        import _octane
        scene = context.scene
        oct_scene = scene.octane
        _octane.get_octanedb(scene.as_pointer(), context.as_pointer())
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
            converted_material = cur_material.copy()        
            converters.convert_to_octane_material(cur_material, converted_material) 
            if len(cur_obj.material_slots) < 1:                    
                cur_obj.data.materials.append(converted_material)
            else:                    
                cur_obj.material_slots[cur_obj.active_material_index].material = converted_material  
            converters.convert_all_related_material(cur_material, converted_material)            
        return {'FINISHED'} 

class OCTANE_OT_BaseExport(Operator):
    export_type = 0
    file_ext = '.orbx'
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')    

    def execute(self, context):
        import _octane
        scene = context.scene            
        data = context.blend_data.as_pointer()
        prefs = bpy.context.preferences.as_pointer()
        if not self.filepath.endswith(self.file_ext):
            self.filepath += self.file_ext
        _octane.export(scene.as_pointer(), context.as_pointer(), prefs, data, self.filepath, self.export_type)  
        return {'FINISHED'} 

    def invoke(self, context, event):
        filename = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        if filename == '':
            filename = 'octane_export'     
        filename = bpy.path.clean_name(filename)           
        self.filename = bpy.path.ensure_ext(filename, self.file_ext)    
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class OCTANE_OT_OrbxExport(OCTANE_OT_BaseExport):
    """Export current scene in Octane ORBX format"""
    export_type = EXPORT_TYPES['ORBX']
    file_ext = '.orbx'    
    bl_idname = "export.orbx"
    bl_label = "Octane Orbx(.orbx)"
    filter_glob: StringProperty(default="*.orbx", options={'HIDDEN'}) 
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')      

class OCTANE_OT_AlembicExport(OCTANE_OT_BaseExport):
    """Export current scene in Octane alembic format"""
    export_type = EXPORT_TYPES['ALEMBIC']
    file_ext = '.abc'    
    bl_idname = "export.abc"
    bl_label = "Octane Alembic(.abc)"   
    filter_glob: StringProperty(default="*.abc", options={'HIDDEN'})     
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype='FILE_NAME')   


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

    OCTANE_OT_UpdateOctaneGeoNodeCollections,
    OCTANE_OT_UpdateOSLCameraNodeCollections,
    OCTANE_OT_UpdateAovOutputGroupCollections,

    OCTANE_OT_SetMeshesType,
    OCTANE_OT_SetOctaneShader,
    OCTANE_OT_ConvertToOctaneMaterial,

    OCTANE_OT_OrbxExport,
    OCTANE_OT_AlembicExport,

    OCTANE_OT_OrbxPreivew,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    def menu_func(self, context):
        self.layout.operator_context = 'INVOKE_DEFAULT'
        self.layout.operator(OCTANE_OT_OrbxExport.bl_idname, text="Octane Orbx(.orbx)")
        self.layout.operator(OCTANE_OT_AlembicExport.bl_idname, text="Octane Alembic(.abc)")        
    bpy.types.TOPBAR_MT_file_export.append(menu_func)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
