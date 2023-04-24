import bpy
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty, BoolVectorProperty, CollectionProperty
from bpy.utils import register_class, unregister_class
from octane.properties_ import common
from octane.utils import consts, ocio, utility

object_mesh_types = (    
    ('Global', "Global", "", 0),
    ('Scatter', "Scatter", "", 1),
    ('Movable proxy', "Movable proxy", "", 2),
    ('Reshapable proxy', "Reshapable proxy", "", 3),
    ('Auto', "Auto", "", 4),
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

class OctaneObjectSettings(bpy.types.PropertyGroup):
    render_layer_id: IntProperty(
        name="Render layer ID",
        description="Render layer number for current object. Will use the layer number from blender built-in render layer system if the value is 0",
        min=1, max=255,
        default=1,
    )
    general_visibility: FloatProperty(
        name="General visibility",
        description="",
        min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
    )    
    camera_visibility: BoolProperty(
        name="Camera Visibility",
        description="",
        default=True
    )
    shadow_visibility: BoolProperty(
        name="Shadow Visibility",
        description="",
        default=True
    )
    dirt_visibility: BoolProperty(
        name="Dirt Visibility",
        description="",
        default=True
    )
    curvature_visibility: BoolProperty(
        name="Curvature Visibility",
        description="",
        default=True
    )                
    random_color_seed: IntProperty(
        name="Random color seed",
        description="Random color seed",
        min=0, max=65535,
        default=0,
    )    
    color: FloatVectorProperty(
        name="Color",
        description="The color that is rendered in the object layer render pass",
        min=0.0, max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype='COLOR',
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

    baking_group_id: IntProperty(
        name="Baking group ID",
        description="",
        min=1, max=65535,
        default=1,                
    )
    baking_uv_transform_rz: FloatProperty(
        name="R.Z",
        description="Rotation Z",
        min=-360, max=360,
        default=0,                
    )
    baking_uv_transform_sx: FloatProperty(
        name="S.X",
        description="Scale X",
        min=-0.001, max=1000,
        default=1,                
    )    
    baking_uv_transform_sy: FloatProperty(
        name="S.Y",
        description="Scale Y",
        min=-0.001, max=1000,
        default=1,                
    )   
    baking_uv_transform_tx: FloatProperty(
        name="T.X",
        description="Translation X",
        default=0,                
    )    
    baking_uv_transform_ty: FloatProperty(
        name="T.Y",
        description="Translation Y",
        default=0,                
    )      
    custom_aov: EnumProperty(
        name="Custom AOV",
        description="If a custom AOV is selected, it will write a mask to it where the material is visible",
        items=custom_aov_modes,
        default='None',
    )  
    custom_aov_channel: EnumProperty(
        name="Custom AOV Channel",
        description="If a custom AOV is selected, the selected channel(s) will receive the mask",
        items=custom_aov_channel_modes,
        default='All',
    )           

    use_motion_blur: BoolProperty(
        name="Use Motion Blur",
        description="Use motion blur for this object",
        default=False,
    )
    use_deform_motion: BoolProperty(
        name="Use Deformation Motion",
        description="Use deformation motion blur for this object",
        default=False,
    )
    motion_steps: IntProperty(
        name="Motion Steps",
        description="Control accuracy of motion blur, more steps gives more memory usage (actual number of steps is 2^(steps - 1))",
        min=1, soft_max=8,
        default=1,
    )   
    object_mesh_type: EnumProperty(
        name="Object Type",
        description="Used for rendering speed optimization, see the manual",
        items=object_mesh_types,
        default='Auto',
    )   
    node_graph_tree: StringProperty(
        name="Node Graph",
        default="",
        maxlen=512,
    )    
    osl_geo_node: StringProperty(
        name="Octane Geo Node",
        default="",
        maxlen=512,
    )

    @classmethod
    def register(cls):
        bpy.types.Object.octane = PointerProperty(
            name="Octane Object Settings",
            description="Octane object settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane


_CLASSES = [
    OctaneObjectSettings,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)