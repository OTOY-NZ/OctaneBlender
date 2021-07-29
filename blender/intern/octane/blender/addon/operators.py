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
}

EXPORT_TYPES = {    
    'ALEMBIC': 1,
    'ORBX': 2,    
}

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

classes = (
    OCTANE_OT_use_shading_nodes,

    OCTANE_OT_ShowOctaneNodeGraph,
    OCTANE_OT_ShowOctaneNetworkPreference,
    OCTANE_OT_StopRender,
    OCTANE_OT_ShowOctaneLog,
    OCTANE_OT_ShowOctaneDeviceSetting,
    OCTANE_OT_ActivateOctane,
    OCTANE_OT_ShowOctaneDB,
    OCTANE_OT_SaveOctaneDB,

    OCTANE_OT_UpdateOctaneGeoNodeCollections,
    OCTANE_OT_UpdateOSLCameraNodeCollections,

    OCTANE_OT_SetMeshesType,
    OCTANE_OT_SetOctaneShader,
    OCTANE_OT_ConvertToOctaneMaterial,

    OCTANE_OT_OrbxExport,
    OCTANE_OT_AlembicExport,
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
