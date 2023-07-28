#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

import bpy
from bpy.app.handlers import persistent
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    PointerProperty,
    StringProperty,
    FloatVectorProperty,
    BoolVectorProperty,
    CollectionProperty
)
import os
from math import pi
import nodeitems_utils
from octane.utils import consts, utility, ocio
from operator import add

rotation_orders = (
    ('0', "XYZ", ""),
    ('1', "XZY", ""),
    ('2', "YXZ", ""),
    ('3', "YZX", ""),
    ('4', "ZXY", ""),
    ('5', "ZYX", ""),
)

default_material_orders = (
    ("0", "Diffuse", "OctaneDiffuseMaterial", 0),
    ("1", "Glossy", "OctaneGlossyMaterial", 1),
    ("2", "Specular", "OctaneSpecularMaterial", 2),
    ("3", "Mix", "OctaneMixMaterial", 3), 
    ("4", "Portal", "OctanePortalMaterial", 4), 
    ("5", "Toon", "OctaneToonMaterial", 5),
    ("6", "Metal", "OctaneMetallicMaterial", 6),
    ("7", "Universal", "OctaneUniversalMaterial", 7), 
    ("8", "ShadowCatcher", "OctaneShadowCatcherMaterial", 8), 
    ("9", "Layered", "OctaneLayeredMaterial", 9), 
    ("10", "Composite", "OctaneCompositeMaterial", 10), 
    ("11", "Hair", "OctaneHairMaterial", 11),
    ("12", "Clipping", "OctaneClippingMaterial", 12),
    ("13", "Null", "OctaneNullMaterial", 13),
    )

texture_node_layouts = (
    ('0', "Default", '', 0),
    ('1', "Octane", '', 1),    
    )

mesh_types = (
    ('0', "Global", ""),
    ('1', "Scatter", ""),
    ('2', "Movable proxy", ""),
    ('3', "Reshapable proxy", ""),
    )

object_mesh_types = (    
    ("Global", "Global", "During scene translation, all Meshes with this type collapse into one common Mesh. This increases the rendering speed, but the translation time is much slower and GPU memory usage is much higher. Use this mode if you render a heavy interior scene as a still image. If you have enough GPU memory to fit the entire scene as one common Mesh, it does not matter that the translation time takes much longer because rendering the image may case take hours. You an save time by using Global meshes in heavy still images, as the rendering speed is much faster if the scene is used as one common Mesh. The Viewport refreshes slower if you have a lot of Global meshes in scene", 0),
    ("Scatter", "Scatter", "Octane reloads Geometry objects with the Scatter type. This increases the scene translation speed and decreases GPU memory usage, but Objects with more scattering render with fewer samples per pixel", 1),
    ("Movable proxy", "Movable proxy", "Similar to Scatter, but only the geometry types with Movable Proxy are retranslated and reloaded into OctaneServer for every frame when you render an animation sequence", 2),
    ("Reshapable proxy", "Reshapable proxy", "Octane reloads the full Mesh and evaluates every frame. This is useful for deforming mesh types like fluids", 3),
    ("Auto", "Scatter/Movable", "Previously named Auto (Experimental), this option can manage both Scatter or Movable (animated on transformations only, not deformed) meshes. This option will retranslate objects with this type specified for every frame when rendering an animation sequence", 4),
)

bound_interp = (
    ('1', "None", ""),
    ('2', "Edge only", ""),
    ('3', "Edge and corner", ""),
    ('4', "Always sharp", ""),
    )

subd_scheme = (
    ('1', "Catmull Clark", ""),
    ('2', "Loop", ""),
    ('3', "Bilinear", ""),
    )

winding_orders = (
    ('0', "Clockwise", ""),
    ('1', "Counterclockwise", ""),
    )

hair_interpolations = (
    ('0', "Hair length", ""),
    ('1', "Segment count", ""),
    ('2', "Use hair Ws", ""),
    )

octane_preset_shaders = (
    ('None', "None", '', 0),
    ('Smoke', "Smoke", '', 1),
)

primitive_coordinate_modes = (
    ("Blender", "Blender", "", 0),
    ("Octane", "Octane", "", 1), 
)

# The various units we support during the geometry import. It's basically the unit used during the export of the geometry
geometry_import_scale = (
    ('millmeters', "millmeters", "", 1),
    ('centimeters', "centimeters", "", 2),
    ('decimeters', "decimeters", "", 3),
    ('meters', "meters", "", 4),
    ('decameters', "decamters", "", 5),
    ('hectometers', "hectometers", "", 6),
    ('kilometers', "kilometers", "", 7),
    ('inches', "inches", "", 8),
    ('feet', "feet", "", 9),
    ('yards', "yards", "", 10),
    ('furlongs', "furlongs", "", 11),
    ('miles', "miles", "", 12),
    ('DAZ Studio unit', "DAZ Studio unit", "", 13),
    ('Poser Native Unit', "Poser Native Unit", "", 14),
)

vdb_velocity_grid_types = (
    ('Vector grid', "Use vector grid", "", 0),
    ('Component grid', "Use component grid", "", 1),    
)

orbx_preview_types = (
    ('Built-in Mesh', 'Built-in Mesh', "The preview will be shown as Built-in Mesh. No external assets are required in this case", 0),
    ('External Alembic', 'External Alembic', "The previwe data will be shown as imported Alembic. The preview is exactly the same as the render results with animation support", 1), 
)

intermediate_color_space_types = (
    ('Linear sRGB', 'Linear sRGB', "Linear sRGB", 2),
    ('ACES2065-1', 'ACES2065-1', "ACES2065-1", 3), 
)

custom_aov_modes = (
    ('None', "None", "None", 4096),
    ('Custom AOV 1', "Custom AOV 1", "Custom AOV 1", 0),
    ('Custom AOV 2', "Custom AOV 2", "Custom AOV 2", 1),
    ('Custom AOV 3', "Custom AOV 3", "Custom AOV 3", 2),
    ('Custom AOV 4', "Custom AOV 4", "Custom AOV 4", 3),
    ('Custom AOV 5', "Custom AOV 5", "Custom AOV 5", 4),
    ('Custom AOV 6', "Custom AOV 6", "Custom AOV 6", 5),
    ('Custom AOV 7', "Custom AOV 7", "Custom AOV 7", 6),
    ('Custom AOV 8', "Custom AOV 8", "Custom AOV 8", 7),
    ('Custom AOV 9', "Custom AOV 9", "Custom AOV 9", 8),
    ('Custom AOV 10', "Custom AOV 10", "Custom AOV 10", 9),
    ('Custom AOV 11', "Custom AOV 11", "Custom AOV 11", 10),
    ('Custom AOV 12', "Custom AOV 12", "Custom AOV 12", 11),
    ('Custom AOV 13', "Custom AOV 13", "Custom AOV 13", 12),
    ('Custom AOV 14', "Custom AOV 14", "Custom AOV 14", 13),
    ('Custom AOV 15', "Custom AOV 15", "Custom AOV 15", 14),
    ('Custom AOV 16', "Custom AOV 16", "Custom AOV 16", 15),
    ('Custom AOV 17', "Custom AOV 17", "Custom AOV 17", 16),
    ('Custom AOV 18', "Custom AOV 18", "Custom AOV 18", 17),
    ('Custom AOV 19', "Custom AOV 19", "Custom AOV 19", 18),
    ('Custom AOV 20', "Custom AOV 20", "Custom AOV 20", 19),    
)

custom_aov_channel_modes = (
    ('All', "All", "All", 0),
    ('Red', "Red", "Red", 1),
    ('Green', "Green", "Green", 2),
    ('Blue', "Blue", "Blue", 3),
)

def format_octane_path(cur_path):
    import os    
    octane_path = ""
    try:
        if len(cur_path):
            cur_path = str(bpy.path.abspath(cur_path))            
            if not cur_path.endswith(os.sep):
                cur_path += os.sep            
        octane_path = cur_path                          
    except:
        pass  
    return octane_path  


def update_octane_localdb_path():
    from octane import core
    if core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        return
    import _octane    
    octane_localdb_path = ""
    try:
        octane_localdb_path = format_octane_path(str(bpy.context.preferences.addons[__package__].preferences.octane_localdb_path))                        
    except:
        pass
    _octane.update_octane_localdb(octane_localdb_path)   


def update_octane_texture_cache_path():
    from octane import core
    if core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        return    
    import _octane    
    octane_texture_cache_path = ""
    try:
        octane_texture_cache_path = format_octane_path(str(bpy.context.preferences.addons[__package__].preferences.octane_texture_cache_path))                        
    except:
        pass
    _octane.update_octane_texture_cache(octane_texture_cache_path)      
    

def update_octane_server_address():
    from octane import core
    if core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        return    
    import _octane
    import os
    octane_server_address = ""
    enable_relese_octane_license_when_exiting = False
    try:
        octane_server_address = str(bpy.context.preferences.addons[__package__].preferences.octane_server_address)  
        enable_relese_octane_license_when_exiting = bool(bpy.context.preferences.addons[__package__].preferences.enable_relese_octane_license_when_exiting)
    except:
        pass
    _octane.update_octane_server_address(octane_server_address, enable_relese_octane_license_when_exiting)   


def update_octane_params():
    from octane import core
    if core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
        return    
    import _octane
    default_material_id = 0
    try:
        default_material_id = int(bpy.context.preferences.addons[__package__].preferences.default_material_id)  
    except:
        pass
    _octane.set_octane_params(default_material_id)      


def update_octane_vdb_info(cls, context):
    cls.octane_vdb_helper = cls.is_octane_vdb and 'F$' in cls.imported_openvdb_file_path
    cls.octane_vdb_info.update(context)


def update_octane_data():
    update_octane_localdb_path()
    update_octane_texture_cache_path()
    update_octane_server_address()
    update_octane_params()

def OctaneSpecificNodeCollection_update_function(self, context):
    self.update_nodes(context)

def OctaneSpecificNodeCollection_sync_function(self, context):
    self.sync_geo_node_info(context)

class OctaneGeoNode(bpy.types.PropertyGroup):    
    name: StringProperty(name="Octane Geo Node Name")  

class OctaneGeoNodeCollection(bpy.types.PropertyGroup):    
    osl_geo_nodes: CollectionProperty(type=OctaneGeoNode)

    node_graph_tree: StringProperty(
            name="Node Graph",
            description="The node graph containing target osl geometric node",
            default="",
            update=OctaneSpecificNodeCollection_update_function,
            maxlen=512,
            )   

    osl_geo_node: StringProperty(
            name="Octane Geo Node",
            description="Octane Geo Node(Vectron or Scatter Tools)",
            default="",
            update=OctaneSpecificNodeCollection_sync_function,
            maxlen=512,
            ) 

    def sync_geo_node_info(self, context):
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                if hasattr(obj, "octane") and hasattr(obj.data, "octane"):
                    if len(obj.data.octane.octane_geo_node_collections.node_graph_tree) or len(obj.data.octane.octane_geo_node_collections.osl_geo_node):
                        obj.octane.node_graph_tree = obj.data.octane.octane_geo_node_collections.node_graph_tree
                        obj.octane.osl_geo_node = obj.data.octane.octane_geo_node_collections.osl_geo_node

    def update_nodes(self, context):  
        print('Update OSL GEO Nodes') 
        for i in range(0, len(self.osl_geo_nodes)):
            self.osl_geo_nodes.remove(0)  
        if bpy.data.materials:      
            for mat in bpy.data.materials.values():
                if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                    continue
                if mat.name != self.node_graph_tree:
                    continue
                for node in mat.node_tree.nodes.values():
                    if node.bl_idname.startswith("OctaneSDF") or node.bl_idname in ('OctaneProxy', 'OctaneVectron', 'ShaderNodeOctVectron', 'ShaderNodeOctScatterToolSurface', 'ShaderNodeOctScatterToolVolume', 'OctaneScatterOnSurface', 'OctaneScatterInVolume', ):
                        self.osl_geo_nodes.add()
                        self.osl_geo_nodes[-1].name = node.name
        self.sync_geo_node_info(context)


class OctaneVDBGridID(bpy.types.PropertyGroup):    
    name: StringProperty(name="Octane VDB Grid ID")  

class OctaneVDBInfo(bpy.types.PropertyGroup):
    vdb_vector_grid_id_container: CollectionProperty(type=OctaneVDBGridID)
    vdb_float_grid_id_container: CollectionProperty(type=OctaneVDBGridID)

    def update(self, context):
        def set_container(container, items):
            for i in range(0, len(container)):
                container.remove(0)
            for item in items:
                container.add()
                container[-1].name = item            
        scene = context.scene
        try:
            cur_obj = context.object
        except:
            cur_obj = None
        if cur_obj:
            if cur_obj.type == 'VOLUME':
                if cur_obj.data.octane.last_vdb_file_path == cur_obj.data.filepath:
                    return
                cur_obj.data.octane.last_vdb_file_path = cur_obj.data.filepath
                if not cur_obj.data.grids.is_loaded:
                    cur_obj.data.grids.load()
                if cur_obj.data.grids.is_loaded:
                    vdb_float_grid_ids = []
                    vdb_vector_grid_ids = []           
                    for grid in cur_obj.data.grids.values():
                        if grid.data_type == 'FLOAT':
                            vdb_float_grid_ids.append(grid.name)
                        elif grid.data_type == 'VECTOR_FLOAT':
                            vdb_vector_grid_ids.append(grid.name)
                    set_container(self.vdb_float_grid_id_container, vdb_float_grid_ids)
                    set_container(self.vdb_vector_grid_id_container, vdb_vector_grid_ids)               
            else:
                vdb_float_grid_ids = []
                vdb_vector_grid_ids = []
                from octane import core
                if core.ENABLE_OCTANE_ADDON_CLIENT:
                    from octane.core.client import OctaneBlender
                    response = OctaneBlender().utils_function(consts.UtilsFunctionType.FETCH_VDB_INFO, cur_obj.data.filepath)                    
                    if len(response):
                        content = ET.fromstring(response).get("content")
                        root_et = ET.fromstring(content)
                        float_grid_et = root_et.find("floatGrid")
                        for et in float_grid_et.findall("grid"):
                            vdb_float_grid_ids.append(et.text)                        
                        vector_grid_et = root_et.find("vectorGrid")
                        for et in vector_grid_et.findall("grid"):
                            vdb_vector_grid_ids.append(et.text)                                     
                else:
                    import _octane
                    vdb_float_grid_ids, vdb_vector_grid_ids = _octane.update_vdb_info(cur_obj.as_pointer(), context.blend_data.as_pointer(), scene.as_pointer()) 
                set_container(self.vdb_float_grid_id_container, vdb_float_grid_ids)
                set_container(self.vdb_vector_grid_id_container, vdb_vector_grid_ids)


class OctaneOCIOConfigName(bpy.types.PropertyGroup):    
    name: bpy.props.StringProperty(name="Octane OCIO Config Name")


class OctanePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    use_new_addon_nodes: BoolProperty(
        name="Experience the New Image and Ramp Nodes",
        description="Use the new addon style image and ramp nodes(reboot blender to take effect)",   
        default=True,
    )
    default_object_mesh_type: EnumProperty(
        name="Default Object Mesh Type",
        description="Object mesh type to use for default (Used for rendering speed optimization. See the manual.)(reboot blender to take effect)",   
        items=object_mesh_types,   
        default="Reshapable proxy",
    )    
    default_material_id: EnumProperty(
        name="Default Material Type",
        description="Material to use for default (rendering with Octane)(reboot blender to take effect)",   
        items=default_material_orders,   
        default="7", # Universal
    )
    default_texture_node_layout_id: EnumProperty(
        name="Texture Node Menu Layout",
        description="Layout of texture node menus(reboot blender to take effect)",   
        items=texture_node_layouts,
        default="1"     
    )

    default_use_blender_builtin_render_layer: BoolProperty(
        name="Use Blender Built-in Render Layer",
        description="Whether to use blender built-in render layer system for default(reboot blender to take effect)",   
        default=False,         
    )

    enable_empty_gpus_automatically: BoolProperty(
        name="Empty GPUs After Render",
        description="Empty GPU resources after rendering automatically",
        default=False,
    )

    enable_generate_default_uvs: BoolProperty(
        name="Generate Default UVs",
        description="Generate a default UV map",
        default=False,
    )

    enable_node_graph_upload_opt: BoolProperty(
        name="Node Graph Upload Optimization",
        description="Do not upload nodes that are not used",
        default=False,
    )  
    enable_mesh_upload_optimization: BoolProperty(
        name="Optimized Mesh Generation Mode",
        description="Do not regenerate & upload meshes(except reshapble ones) which are already cached",
        default=True,
    )   
    octane_localdb_path: StringProperty(
        name="Octane LocalDB Path",
        description="Customize octane localDB path. Leave empty to use default settings",
        default='',
        subtype='DIR_PATH',
    ) 
    octane_texture_cache_path: StringProperty(
        name="Octane Texture Cache Folder",
        description="Customize octane texture cache folder. Leave empty to use default settings",
        default='',
        subtype='DIR_PATH',
    )                
    enable_relese_octane_license_when_exiting: BoolProperty(
        name="Release Octane License After Exiting",
        description="Release Octane license after exiting blender",
        default=False,
    )       
    octane_server_address: StringProperty(
        name="Server address",
        description="Octane render-server address",
        default="127.0.0.1",
        maxlen=255,
    )     
    
    ocio_use_other_config_file: BoolProperty(
        name="Use other config file",
        description="Use other config file instead of environment config file",
        default=False,
        update=ocio.update_ocio_info,
    )  
    ocio_use_automatic: BoolProperty(
        name="Automatic(recommended)",
        description="Let Octane guess the intermediate settings automatically",
        default=True,
        update=ocio.update_ocio_info,
    )      
    ocio_config_file_path: StringProperty(
        name="OCIO Config File",
        description="OCIO Config File",
        default='',
        subtype='FILE_PATH',
        update=ocio.update_ocio_info,
    )      
    ocio_intermediate_color_space_octane: EnumProperty(
        name="Manual(Octane)",
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the same color space as the 'OCIO' box",
        items=intermediate_color_space_types,
        default='Linear sRGB',
        update=ocio.update_ocio_info,
    )
    ocio_intermediate_color_space_ocio: StringProperty(
        name="Manual(OCIO)",
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the same color space as the 'Octane' box",        
        default="",
        update=ocio.update_ocio_intermediate_color_space_ocio,
    )
    octane_format_ocio_intermediate_color_space_ocio: StringProperty(
        name="OCIO(Octane Format)",
        default="",
    )    
    ocio_intermediate_color_space_configs: CollectionProperty(type=OctaneOCIOConfigName)
    ocio_export_png_color_space_configs: CollectionProperty(type=OctaneOCIOConfigName)    
    ocio_export_exr_color_space_configs: CollectionProperty(type=OctaneOCIOConfigName) 
    ocio_view_configs: CollectionProperty(type=OctaneOCIOConfigName)
    ocio_look_configs: CollectionProperty(type=OctaneOCIOConfigName)
    ocio_export_look_configs: CollectionProperty(type=OctaneOCIOConfigName)            
    ocio_color_space_configs: CollectionProperty(type=OctaneOCIOConfigName)                        

    use_shared_surface: BoolProperty(
        name="Use Shared Surface for Viewport(recommended)",
        description="On Windows, Octane can now send back shared surface handles for render passes instead of just buffers, which makes viewport rendering faster.\n\
For multiple-GPUs platforms, Octane may change the 'Imaging' device during the viewport rendering. These changes are temporary and they will be reverted back after the viewport rendering",
        default=True,
    )

    def draw(self, context):
        from octane import core
        from octane.core.client import OctaneBlender
        if core.ENABLE_OCTANE_ADDON_CLIENT:
            layout = self.layout
            box = layout.box()
            box.label(text="General")
            box.row().prop(self, "default_object_mesh_type", expand=False)
            box = layout.box()
            box.label(text="Viewport Rendering")
            row = box.row()
            row.active = OctaneBlender().is_shared_surface_supported()
            row.prop(self, "use_shared_surface")
            if not row.active:
                box.row().label(text="Shared surface is not supported")
            return
        layout = self.layout
        layout.row().prop(self, "octane_server_address", expand=False) 
        layout.row().prop(self, "enable_relese_octane_license_when_exiting", expand=False)   
        layout.row().prop(self, "octane_localdb_path", expand=False)
        layout.row().prop(self, "default_object_mesh_type", expand=False)
        layout.row().prop(self, "octane_texture_cache_path", expand=False)
        layout.row().prop(self, "default_material_id", expand=False)
        layout.row().prop(self, "default_texture_node_layout_id", expand=False)
        layout.row().prop(self, "use_new_addon_nodes", expand=False)
        box = layout.box()
        box.label(text="Viewport Rendering")
        row = box.row()
        row.active = OctaneBlender().is_shared_surface_supported()
        row.prop(self, "use_shared_surface")
        if not row.active:
            box.row().label(text="Shared surface is not supported")
        box = layout.box()
        box.label(text="Octane Color Management")
        box.row().prop(self, "ocio_use_other_config_file")
        box.row().prop(self, "ocio_config_file_path")
        box.row().prop(self, "ocio_use_automatic")        
        row = box.row()
        row.active = not self.ocio_use_automatic
        row.prop(self, "ocio_intermediate_color_space_octane")
        row = box.row()
        row.active = not self.ocio_use_automatic
        row.prop_search(self, "ocio_intermediate_color_space_ocio", self, "ocio_intermediate_color_space_configs")           
        import _octane
        # _octane.update_default_mat_id(int(self.default_material_id))        
        # _octane.update_generate_default_uvs(int(self.enable_generate_default_uvs))        
        # _octane.update_octane_upload_opt(int(self.enable_node_graph_upload_opt), int(self.enable_mesh_upload_optimization))
        update_octane_data()


def OctaneMeshSettings_update_is_scatter_group_source(self, context):        
    if self.is_scatter_group_source:
        for name, mesh in bpy.data.meshes.items():
            if name != context.mesh.name and mesh.octane.scatter_group_id == self.scatter_group_id and mesh.octane.is_scatter_group_source:
                mesh.octane.is_scatter_group_source = False


class OctaneMeshSettings(bpy.types.PropertyGroup):

    winding_order: EnumProperty(
            name="Winding order",
            description="May be usable if you need to correct some Octane's triangulation artifacts. Alembic export requires clockwise order",
            items=winding_orders,
            default='0',
            )
    mesh_type: EnumProperty(
            name="Mesh type",
            description="Used for rendering speed optimization, see the manual",
            items=mesh_types,
            default='1',
            )
    is_scatter_group_source: BoolProperty(
            name="Used as source for current group",
            description="Use this object data(mesh and material) for current scatter group when rendering. If none of the meshes is set as source, a random source will be picked",
            update=OctaneMeshSettings_update_is_scatter_group_source,
            default=False,
            )
    scatter_group_id: IntProperty(
            name="Scatter group",
            description="Indicate which scatter group this mesh will be put in. Default -1 for independent group",
            min=-1, max=65535,
            default=-1,                
            )  
    scatter_instance_id: IntProperty(
            name="Scatter instance id",
            description="Indicate the instance id this mesh used",
            min=-1, max=65535,
            default=-1,                
            )   
    infinite_plane: BoolProperty(
            name="Infinite plane",
            description="Convert this mesh to infinite plane when rendering",
            default=False,
            )
    enable_mesh_volume_sdf: BoolProperty(
            name="Enable Mesh Volume SDF",
            description="Convert this mesh to Octane Mesh Volume SDF when rendering",
            default=False,
            )        
    mesh_volume_sdf_voxel_size: FloatProperty(
            name="Voxel size",
            description="Size of one voxel",
            min=0.001, max=1000.0,
            default=0.1,
            )     
    mesh_volume_sdf_border_thickness_inside: FloatProperty(
            name="Border thickness(inside)",
            description="Amount of voxels that will be generated on either side of the surface (inside)",
            min=1.0, max=100.0,
            default=3.0,
            )     
    mesh_volume_sdf_border_thickness_outside: FloatProperty(
            name="Border thickness(outside)",
            description="Amount of voxels that will be generated on either side of the surface (outside)",
            min=1.0, max=100.0,
            default=3.0,
            )                                                                                   
    enable_octane_sphere_attribute: BoolProperty(
            name="Enable Octane Sphere Attribute",
            description="Use color and float attributes with sphere primitives which adds on top of the current attribute support for triangles",
            default=False,
            )
    hide_original_mesh: BoolProperty(
            name="Hide Original Mesh",
            description="Hide original mesh when the Octane Sphere Primitive is enabled",
            default=False,
            )    
    octane_sphere_radius: FloatProperty(
            name="Octane Sphere Radius",
            description="The radius of the sphere primitive",
            min=0.00001, max=1000000.0, soft_max=1000000.0,
            default=0.1,
            )   
    use_randomized_radius: BoolProperty(
            name="Use Randomized Radius",
            description="Enable to use the randomized radiuses",
            default=False,
            )    
    octane_sphere_randomized_radius_seed: IntProperty(
            name="Random Seed",
            description="The random seed that used for radiuses",
            min=1, max=65535,
            default=1,   
            )      
    octane_sphere_randomized_radius_min: FloatProperty(
            name="Min Radius",
            description="The min randomized radius of the sphere primitive",
            min=0.00001, max=1000000.0, soft_max=1000000.0,
            default=0.1,
            )                
    octane_sphere_randomized_radius_max: FloatProperty(
            name="Max Radius",
            description="The max randomized radius of the sphere primitive",
            min=0.00001, max=1000000.0, soft_max=1000000.0,
            default=0.1,
            )                    
    tessface_in_preview: BoolProperty(
            name="TessFace in Preview",
            description="Enable tessfaces(if available) in interactive rendering mode",
            default=False,
            )
    open_subd_enable: BoolProperty(
            name="Enable OpenSubDiv",
            description="Subdivide mesh before rendering",
            default=False,
            )
    open_subd_scheme: EnumProperty(
            name="Scheme",
            description="",
            items=subd_scheme,
            default='1',
            )
    open_subd_level: IntProperty(
            name="Subd level",
            description="",
            min=0, max=10,
            default=0,
            )
    open_subd_sharpness: FloatProperty(
            name="Sharpness",
            description="",
            min=0.0, max=11.0, soft_max=11.0,
            default=0.0,
            )
    open_subd_bound_interp: EnumProperty(
            name="Boundary interp.",
            description="",
            items=bound_interp,
            default='3',
            )
    vis_general: FloatProperty(
            name="General visibility",
            description="",
            min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            )
    vis_cam: BoolProperty(
            name="Camera visibility",
            description="",
            default=True,
            )
    vis_shadow: BoolProperty(
            name="Shadow visibility",
            description="",
            default=True,
            )
    rand_color_seed: IntProperty(
            name="Random color seed",
            description="",
            min=0, max=65535,
            default=0,
            )
    layer_number: IntProperty(
            name="Layer number",
            description="Render layer number for current object. Will use the layer number from blender built-in render layer system if the value is 0",
            min=0, max=255,
            default=(0 if getattr(bpy.context.preferences.addons['octane'].preferences, 'default_use_blender_builtin_render_layer', True) else 1),
            )
    baking_group_id: IntProperty(
            name="Baking group",
            description="",
            min=1, max=65535,
            default=1,                
            )
    light_id_sunlight: BoolProperty(
            name="Sunlight",
            description="Sunlight",
            default=True,
            )           
    light_id_env: BoolProperty(
            name="Environment",
            description="Environment",
            default=True,
            )    
    light_id_pass_1: BoolProperty(
            name="Pass 1",
            description="Pass 1",
            default=True,
            ) 
    light_id_pass_2: BoolProperty(
            name="Pass 2",
            description="Pass 2",
            default=True,
            ) 
    light_id_pass_3: BoolProperty(
            name="Pass 3",
            description="Pass 3",
            default=True,
            ) 
    light_id_pass_4: BoolProperty(
            name="Pass 4",
            description="Pass 4",
            default=True,
            ) 
    light_id_pass_5: BoolProperty(
            name="Pass 5",
            description="Pass 5",
            default=True,
            ) 
    light_id_pass_6: BoolProperty(
            name="Pass 6",
            description="Pass 6",
            default=True,
            ) 
    light_id_pass_7: BoolProperty(
            name="Pass 7",
            description="Pass 7",
            default=True,
            ) 
    light_id_pass_8: BoolProperty(
            name="Pass 8",
            description="Pass 8",
            default=True,
            )

    resource_dirty_tag: BoolProperty(
            default=False,
            )
    resource_data_hash_tag: StringProperty(            
            default='',
            )

    octane_vdb_helper: BoolProperty(
            default=False,
            )
    octane_vdb_info: PointerProperty(
            name="Octane VDB Info Container",
            description="",
            type=OctaneVDBInfo,        
            )   
    is_octane_vdb: BoolProperty(
            name="Used as Octane VDB",
            description="Will use the imported OpenVDB file as source",
            default=False,
            update= lambda cls, context : update_octane_vdb_info(cls, context),
            )
    vdb_sdf: BoolProperty(
            name="SDF",
            description="SDF",
            default=False,
            )    
    imported_openvdb_file_path: StringProperty(
            name="OpenVDB File",
            description="Import the OpenVDB file. Use '$F$' to label the frame parts in vdb file path. E.g. $F$. => (0, 1, ... 100 ...). E.g. $4F$. => (0000, 0001, ... 0100 ...)",
            default='',
            update= lambda cls, context : update_octane_vdb_info(cls, context),
            subtype='FILE_PATH',
            )     
    openvdb_frame_speed_mutiplier: FloatProperty(
            name="Speed Multiplier",
            description="The speed multiplier will be used when filling vdb path with $F$ label. VDB_FRAME = CURRENT_FRAME * MULTIPLIER",
            min=0.0,
            default=1.0,
            )   
    openvdb_frame_start_playing_at: IntProperty(
            name="Start Playing at",
            description="In which specific frame on the general timeline it should start to show and play the OpenVDB sequence",
            default=1,
            )        
    openvdb_frame_start: IntProperty(
            name="Start",
            description="The start frame of vdb sequence",
            min=0,
            default=1,
            )
    openvdb_frame_end: IntProperty(
            name="End",
            description="The end frame of vdb sequence",
            min=0,
            default=250,
            )                                                              
    vdb_iso: FloatProperty(
            name="ISO",
            description="Isovalue used for when rendering openvdb level sets",
            min=0.0,
            default=0.04,
            )
    vdb_import_scale: EnumProperty(
        name="Import scale",
        description="The various units we support during the geometry import. It's basically the unit used during the export of the geometry",
        items=geometry_import_scale,
        default='meters',
    )    
    vdb_abs_scale: FloatProperty(
            name="Absorption scale",
            description="This scalar value scales the grid value used for absorption",
            min=0.0,
            default=1.0,
            )
    vdb_emiss_scale: FloatProperty(
            name="Emission scale",
            description="This scalar value scales the grid value used for temperature. Use this when temperature information in a grid is too low",
            min=0.0,
            default=1.0,
            )
    vdb_scatter_scale: FloatProperty(
            name="Scatter scale",
            description="This scalar value scales the grid value used for scattering",
            min=0.0,
            default=1.0,
            )
    vdb_vel_scale: FloatProperty(
            name="Velocity scale",
            description="This scalar value linearly scales velocity vectors in the velocity grid",
            min=0.0,
            default=1.0,
            )
    vdb_motion_blur_enabled: BoolProperty(
            name="Motion blur enabled",
            description="If TRUE, then any motion blur grids will be ignored",
            default=True,
            )    
    vdb_velocity_grid_type: EnumProperty(
        name="Velocity Grid Type",
        description="The grid used for motion blur. A single vec3s type grid or a component grid",
        items=vdb_velocity_grid_types,
        default='Vector grid',
    )    
    vdb_absorption_grid_id: StringProperty(
        name="Absorption grid",
        description="Name of the grid in a VDB to load for absorption",
        default="",
        maxlen=512,
    )  
    vdb_scattering_grid_id: StringProperty(
        name="Scattering grid",
        description="Name of the grid in a VDB to load for scattering",
        default="",
        maxlen=512,
    )  
    vdb_emission_grid_id: StringProperty(
        name="Emission grid",
        description="Name of the grid in a VDB to load for providing temperature information",
        default="",
        maxlen=512,
    )              
    vdb_vector_grid_id: StringProperty(
        name="Vector grid",
        description="Name of a vec3s type grid in the VDB to load for motion blur",
        default="",
        maxlen=512,
    )  
    vdb_x_components_grid_id: StringProperty(
        name="X Component grids",
        description="Name of a float grid in the VDB to use for the x-component of motion blur vectors",
        default="",
        maxlen=512,
    )   
    vdb_y_components_grid_id: StringProperty(
        name="Y Component grids",
        description="Name of a float grid in the VDB to use for the y-component of motion blur vectors",
        default="",
        maxlen=512,
    ) 
    vdb_z_components_grid_id: StringProperty(
        name="Z Component grids",
        description="Name of a float grid in the VDB to use for the z-component of motion blur vectors",
        default="",
        maxlen=512,
    )
    primitive_coordinate_mode: EnumProperty(
        name="Primitive Coordinate Mode",
        description="Primitive Coordinate Mode",
        items=primitive_coordinate_modes,
        default="Blender"
    )    
    enable_octane_offset_transform: BoolProperty(
        name="Octane Offset Transform enabled",
        description="If TRUE, then an offset transform will be applied(it would be useful in external VDB and Orbx transform adjustment)",
        default=False,
    ) 
    octane_offset_translation: FloatVectorProperty(
        name="Translation",                                
        subtype='TRANSLATION',
    )      
    octane_offset_rotation: FloatVectorProperty(
        name="Rotation",                             
        subtype='EULER',
    )    
    octane_offset_scale: FloatVectorProperty(
        name="Scale",                             
        subtype='XYZ',
        default=(1, 1, 1)
    )   
    octane_offset_rotation_order: EnumProperty(
        name="Rotation order",
        items=rotation_orders,
        default='2',
    )      

    hair_interpolation: EnumProperty(
            name="Hair W interpolation",
            description="Specifies the hair interpolation type. If \"Use hair Ws\" is chosen - you need to explicitly set the hairs root/tip W coordinates in Octane's part of particle settings",
            items=hair_interpolations,
            default='0',
            )

    use_auto_smooth: BoolProperty(
            name="Auto smooth",
            description="Curves autosmooth",
            default=False,
            )
    auto_smooth_angle: FloatProperty(
            subtype='ANGLE',
            name="Angle",
            description="Curves autosmooth angle",
            min=0.0, max=3.141593,
            default=1.55,
            )
    force_load_vertex_normals: BoolProperty(
            name="Force load vertex normals",
            description="Force to use vertex normals",
            default=False,
            )                         
    #Vectron
    octane_geo_node_collections: PointerProperty(
            name="Used as Octane Geometric Node",
            description="",
            type=OctaneGeoNodeCollection,
            )
    #Orbx
    imported_orbx_file_path: StringProperty(
            name="Orbx File Path",
            description="Import the Orbx file",
            default='',
            subtype='FILE_PATH',
            )
    orbx_preview_type: EnumProperty(
            name="Orbx Preview Data Type",
            description="The Data Type that used for the preview geometry(for the animated objects, please use the Alembic format)",
            items=orbx_preview_types,
            default='External Alembic',
            )
    converted_alembic_asset_path: StringProperty(
            name="External Alembic Asset Unpack Directory",
            description="The directory is used for unpacking the External Alembic Asset",
            default='',
            subtype='DIR_PATH',
            )
    point_cloud_lod: FloatProperty(
            name="Point Cloud Level of Detail",
            description="Adjust the level of details of the point cloud",
            min=1.0,
            max=100.0,
            default=100.0,
            subtype='PERCENTAGE',
            )   
    external_alembic_mesh_tag: BoolProperty(
            default=False,
            )
    octane_enable_sphere_attribute: BoolProperty(
        name="Enable Octane Sphere Attribute",
        description="Use color and float attributes with sphere primitives which adds on top of the current attribute support for triangles",        
        default=False,
    )
    octane_hide_original_mesh: BoolProperty(
        name="Hide Original Mesh",
        description="Hide original mesh when the Octane Sphere Primitive is enabled",
        default=False,
    )
    octane_use_randomized_radius: BoolProperty(
        name="Use Randomized Radius",
        description="Enable to use the randomized radiuses",
        default=False,
    )
    octane_sphere_randomized_radius_seed: IntProperty(
        name="Random Seed",
        description="The random seed that used for radiuses",
        min=1,
        max=65535,
        default=1,
    )
    octane_sphere_radius: FloatProperty(
        name="Octane Sphere Primitive Radius",
        description="The radius of the sphere primitive",
        min=0.0, max=1000000.0,
        default=0.0,
    )
    octane_sphere_randomized_radius_min: FloatProperty(
        name="Min Radius",
        description="The min randomized radius of the sphere primitive",
        min=0.0, max=1000000.0,
        default=0.0,
    )
    octane_sphere_randomized_radius_max: FloatProperty(
        name="Max Radius",
        description="The max randomized radius of the sphere primitive",
        min=0.0, max=1000000.0,
        default=0.0,
    )
    render_curve_as_octane_hair: BoolProperty(
        name="Render as the Octane Hair",
        description="Render this curve as the Octane hair",
        default=False,
    )
    use_octane_radius_setting: BoolProperty(
        name="Use Octane Hair Radius",
        description="Use the Octane hair radius settings instead of the curve's radius",
        default=False,
    )    
    hair_root_width: FloatProperty(
        name="Root thickness",
        description="Hair thickness at root",
        min=0.0, max=1000000.0,
        default=0.001,
        precision=4,
        step=0.1,
    )
    hair_tip_width: FloatProperty(
        name="Tip thickness",
        description="Hair thickness at tip",
        min=0.0, max=1000000.0,
        default=0.001,
        precision=4,
        step=0.1,
    )

    @classmethod
    def register(cls):
        bpy.types.Mesh.octane = PointerProperty(
                name="Octane Mesh Settings",
                description="",
                type=cls,
                )
        bpy.types.Curves.octane = PointerProperty(
                name="Octane Curve Settings",
                description="",
                type=cls,
                )        
        bpy.types.Curve.octane = PointerProperty(
                name="Octane Curve Settings",
                description="",
                type=cls,
                )
        bpy.types.MetaBall.octane = PointerProperty(
                name="Octane MetaBall Settings",
                description="",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Mesh.octane
        del bpy.types.Curves.octane
        del bpy.types.Curve.octane
        del bpy.types.MetaBall.octane


UNIT_CONVERT_MAP = {
    'millmeters': 0.001,
    'centimeters': 0.01,
    'decimeters': 0.1,
    'meters': 1,
    'decameters': 10,
    'hectometers': 100,
    'kilometers': 1000,
    'inches': 1 / 39.3701,
    'feet': 1 / 3.280841666667,
    'yards': 1 / 1.0936138888889999077,
    'furlongs': 1 / 0.00497096,
    'miles': 1 / 0.00062137123552453663,
    'DAZ Studio unit': 0.01,
    'Poser Native Unit': 2.6,
}

def update_octane_volume_import_scale(self, context):
    obj = None
    try:
        obj = bpy.context.view_layer.objects.active
    except:
        pass
    if obj:
        if len(obj.data.octane.last_vdb_import_scale) == 0:
            obj.data.octane.last_vdb_import_scale = 'meters'                     
        if obj.data.octane.apply_import_scale_to_blender_transfrom:  
            unit_scale = UNIT_CONVERT_MAP[obj.data.octane.vdb_import_scale] / UNIT_CONVERT_MAP[obj.data.octane.last_vdb_import_scale]                             
            obj.delta_scale = obj.delta_scale * unit_scale
            obj.data.octane.last_vdb_import_scale = obj.data.octane.vdb_import_scale
        else:
            obj.data.octane.last_vdb_import_scale = 'meters'        
        obj.data.update_tag()


def update_octane_volume_auto_apply_import_scale(self, context):
    obj = None
    try:
        obj = bpy.context.view_layer.objects.active
    except:
        pass
    if obj:
        if len(obj.data.octane.last_vdb_import_scale) == 0:
            obj.data.octane.last_vdb_import_scale = 'meters'                     
        if obj.data.octane.apply_import_scale_to_blender_transfrom:  
            unit_scale = UNIT_CONVERT_MAP[obj.data.octane.vdb_import_scale]                            
            obj.delta_scale = obj.delta_scale * unit_scale
            obj.data.octane.last_vdb_import_scale = obj.data.octane.vdb_import_scale
        else:
            unit_scale = UNIT_CONVERT_MAP[obj.data.octane.vdb_import_scale]
            obj.delta_scale = obj.delta_scale / unit_scale
            obj.data.octane.last_vdb_import_scale = 'meters'        
        obj.data.update_tag()


class OctaneVolumeSettings(bpy.types.PropertyGroup):

    resource_dirty_tag: BoolProperty(
            default=False,
            )
    resource_data_hash_tag: StringProperty(            
            default='',
            )

    octane_vdb_helper: BoolProperty(
            default=False,
            )
    octane_vdb_info: PointerProperty(
            name="Octane VDB Info Container",
            description="",
            type=OctaneVDBInfo,        
            )    
    vdb_sdf: BoolProperty(
            name="SDF",
            description="SDF",
            default=False,
            )    
    imported_openvdb_file_path: StringProperty(
            name="OpenVDB File",
            description="Import the OpenVDB file. Use '$F$' to label the frame parts in vdb file path. E.g. $F$. => (0, 1, ... 100 ...). E.g. $4F$. => (0000, 0001, ... 0100 ...)",
            default='',
            update= lambda cls, context : update_octane_vdb_info(cls, context),
            subtype='FILE_PATH',
            )  
    last_vdb_file_path: StringProperty(
            default="",
            )       
    openvdb_frame_speed_mutiplier: FloatProperty(
            name="Speed Multiplier",
            description="The speed multiplier will be used when filling vdb path with $F$ label. VDB_FRAME = CURRENT_FRAME * MULTIPLIER",
            min=0.0,
            default=1.0,
            )   
    openvdb_frame_start_playing_at: IntProperty(
            name="Start Playing at",
            description="In which specific frame on the general timeline it should start to show and play the OpenVDB sequence",
            default=1,
            )        
    openvdb_frame_start: IntProperty(
            name="Start",
            description="The start frame of vdb sequence",
            min=0,
            default=1,
            )
    openvdb_frame_end: IntProperty(
            name="End",
            description="The end frame of vdb sequence",
            min=0,
            default=250,
            )                                                              
    vdb_iso: FloatProperty(
            name="ISO",
            description="Isovalue used for when rendering openvdb level sets",
            min=0.0,
            default=0.04,
            )
    last_vdb_import_scale: StringProperty(
            default="",
            )     
    vdb_import_scale: EnumProperty(
            name="Import scale",
            description="The various units we support during the geometry import. It's basically the unit used during the export of the geometry",
            items=geometry_import_scale,
            default='meters',
            update=update_octane_volume_import_scale,
            )    
    apply_import_scale_to_blender_transfrom: BoolProperty(
            name="Auto Apply Import Scale to Blender Transform",
            description="If TRUE, the import scale will be applied to the Blender Delta Transform. This will help you to match the Viewport and Octane Preview results when using import scale",
            default=False,
            update=update_octane_volume_auto_apply_import_scale,
            )
    vdb_abs_scale: FloatProperty(
            name="Absorption scale",
            description="This scalar value scales the grid value used for absorption",
            min=0.0,
            default=1.0,
            )
    vdb_emiss_scale: FloatProperty(
            name="Emission scale",
            description="This scalar value scales the grid value used for temperature. Use this when temperature information in a grid is too low",
            min=0.0,
            default=1.0,
            )
    vdb_scatter_scale: FloatProperty(
            name="Scatter scale",
            description="This scalar value scales the grid value used for scattering",
            min=0.0,
            default=1.0,
            )
    vdb_vel_scale: FloatProperty(
            name="Velocity scale",
            description="This scalar value linearly scales velocity vectors in the velocity grid",
            min=0.0,
            default=1.0,
            )
    vdb_motion_blur_enabled: BoolProperty(
            name="Motion blur enabled",
            description="If TRUE, then any motion blur grids will be ignored",
            default=True,
            )    
    vdb_velocity_grid_type: EnumProperty(
        name="Velocity Grid Type",
        description="The grid used for motion blur. A single vec3s type grid or a component grid",
        items=vdb_velocity_grid_types,
        default='Vector grid',
    )    
    vdb_absorption_grid_id: StringProperty(
        name="Absorption grid",
        description="Name of the grid in a VDB to load for absorption",
        default="",
        maxlen=512,
    )  
    vdb_scattering_grid_id: StringProperty(
        name="Scattering grid",
        description="Name of the grid in a VDB to load for scattering",
        default="",
        maxlen=512,
    )  
    vdb_emission_grid_id: StringProperty(
        name="Emission grid",
        description="Name of the grid in a VDB to load for providing temperature information",
        default="",
        maxlen=512,
    )              
    vdb_vector_grid_id: StringProperty(
        name="Vector grid",
        description="Name of a vec3s type grid in the VDB to load for motion blur",
        default="",
        maxlen=512,
    )  
    vdb_x_components_grid_id: StringProperty(
        name="X Component grids",
        description="Name of a float grid in the VDB to use for the x-component of motion blur vectors",
        default="",
        maxlen=512,
    )   
    vdb_y_components_grid_id: StringProperty(
        name="Y Component grids",
        description="Name of a float grid in the VDB to use for the y-component of motion blur vectors",
        default="",
        maxlen=512,
    ) 
    vdb_z_components_grid_id: StringProperty(
        name="Z Component grids",
        description="Name of a float grid in the VDB to use for the z-component of motion blur vectors",
        default="",
        maxlen=512,
    )               
    enable_octane_offset_transform: BoolProperty(
        name="Use VDB Transformations",
        description="If TRUE, then an offset transform will be applied(it would be useful in external VDB transform adjustment)",
        default=True,
    ) 
    octane_offset_translation: FloatVectorProperty(
        name="Translation",                                
        subtype='TRANSLATION',
    )      
    octane_offset_rotation: FloatVectorProperty(
        name="Rotation",                             
        subtype='EULER',
    )    
    octane_offset_scale: FloatVectorProperty(
        name="Scale",                             
        subtype='XYZ',
        default=(1, 1, 1)
    )   
    octane_offset_rotation_order: EnumProperty(
        name="Rotation order",
        items=rotation_orders,
        default='2',
    )      


    @classmethod
    def register(cls):
        bpy.types.Volume.octane = PointerProperty(
                name="Octane Volume Settings",
                description="",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Volume.octane


class OctaneObjPropertiesSettings(bpy.types.PropertyGroup):

    visibility: BoolProperty(
            name="Visibility",
            description="Object visibility for Octane",
            default=True,
            )
    overwrite_scatter_instance_id: IntProperty(
            name="Overwrite instance id",
            description="Indicate the instance id this object used",
            min=0, max=65535,
            default=0,                
            )             

    @classmethod
    def register(cls):
        bpy.types.Object.octane_properties = PointerProperty(
                name="Octane Object Properties",
                description="Octane object properties",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane_properties


class OctaneMaterialSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Material.octane = PointerProperty(
                name="Octane Material Settings",
                description="Octane material settings",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Material.octane


classes = (
    OctaneOCIOConfigName,
    OctanePreferences,
    OctaneGeoNode,
    OctaneGeoNodeCollection,
    OctaneVDBGridID,
    OctaneVDBInfo,
    OctaneMeshSettings,
    OctaneObjPropertiesSettings,
    OctaneMaterialSettings,
    OctaneVolumeSettings,
)

@persistent
def load_handler(scene):
    pass

def register():    
    from bpy.utils import register_class    
    for cls in classes:
        register_class(cls)
    from octane import nodeitems_octane
    shader_node_categories = nodeitems_octane.shader_node_categories_based_functions
    texture_node_categories = nodeitems_octane.texture_node_categories_based_functions
    try:
        default_texture_node_layout_id = int(bpy.context.preferences.addons['octane'].preferences.default_texture_node_layout_id)  
        if default_texture_node_layout_id == 1:
            shader_node_categories = nodeitems_octane.shader_node_categories_based_octane
            texture_node_categories = nodeitems_octane.texture_node_categories_based_octane
    except:
        pass     
    # nodeitems_utils.register_node_categories("OCT_SHADER", shader_node_categories)    
    # nodeitems_utils.register_node_categories("OCT_TEXTURE", texture_node_categories)
    octane_server_address = str(bpy.context.preferences.addons['octane'].preferences.octane_server_address)
    update_octane_data()
    ocio.update_ocio_info()  
    bpy.app.handlers.load_post.append(load_handler)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    # nodeitems_utils.unregister_node_categories("OCT_SHADER")
    # nodeitems_utils.unregister_node_categories("OCT_TEXTURE")        
    bpy.app.handlers.load_post.remove(load_handler)