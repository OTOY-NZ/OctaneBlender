import bpy
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty, BoolVectorProperty, CollectionProperty
from bpy.utils import register_class, unregister_class
from octane.nodes.render_settings.animation_settings import OctaneAnimationSettingsShutterAlignment
from octane.nodes.render_settings.render_layer import OctaneRenderLayerMode
from octane.properties_ import common
from octane.utils import consts, ocio, utility
from octane import core

rotation_orders = (
    ('0', "XYZ", ""),
    ('1', "XZY", ""),
    ('2', "YXZ", ""),
    ('3', "YZX", ""),
    ('4', "ZXY", ""),
    ('5', "ZYX", ""),
)

info_pass_sampling_modes = (
    ('0', "Distributed rays", ""),
    ('1', "Non-distributed with pixel filtering", ""),
    ('2', "Non-distributed without pixel filtering", ""),
)

cryptomatte_pass_channel_modes = (
    ('2', "2", "", 2),
    ('4', "4", "", 4),
    ('6', "6", "", 6),
    ('8', "8", "", 8),
    ('10', "10", "", 10),        
)


class OctaneOCIOConfigName(bpy.types.PropertyGroup):    
    name: bpy.props.StringProperty(name="Octane OCIO Config Name")


class OctaneAovOutputGroupNode(bpy.types.PropertyGroup):    
    name: StringProperty(name="Node Name")   


class OctaneAovOutputGroupCollection(bpy.types.PropertyGroup):    
    composite_node_trees: CollectionProperty(type=OctaneAovOutputGroupNode)
    aov_output_group_nodes: CollectionProperty(type=OctaneAovOutputGroupNode)

    composite_node_tree: StringProperty(
        name="Octane Composite Node Tree",
        description="Octane composite node tree containing target Aov Output Group node",
        default="",
        update=lambda self, context: self.update_nodes(context),
        maxlen=512,
    )   

    aov_output_group_node: StringProperty(
        name="Aov Output Group Node",
        description="Aov Output Group Node",
        default="",
        update=lambda self, context: self.update_nodes(context),
        maxlen=512,
    )   

    def update_nodes(cls, context):   
        for i in range(0, len(cls.composite_node_trees)):
            cls.composite_node_trees.remove(0)
        if bpy.data.node_groups:      
            for node_tree in bpy.data.node_groups.values():
                if getattr(node_tree, "bl_idname", "") == consts.OctaneNodeTreeIDName.COMPOSITE:
                    cls.composite_node_trees.add()
                    cls.composite_node_trees[-1].name = node_tree.name
        for i in range(0, len(cls.aov_output_group_nodes)):
            cls.aov_output_group_nodes.remove(0)  
        if bpy.data.node_groups:      
            for node_tree in bpy.data.node_groups.values():
                if getattr(node_tree, "bl_idname", "") != consts.OctaneNodeTreeIDName.COMPOSITE:
                    continue
                if node_tree.name != cls.composite_node_tree:
                    continue
                for node in node_tree.nodes.values():
                    if node.bl_idname == "ShaderNodeOctAovOutputGroup":                        
                        cls.aov_output_group_nodes.add()
                        cls.aov_output_group_nodes[-1].name = node.name


class OctaneBakingLayerTransform(bpy.types.PropertyGroup):
    id: IntProperty(
            name="Baking Layer ID",
            min=1, max=65535,
            default=1,                
            )   
    translation: FloatVectorProperty(
            name="Translation",                                
            subtype='TRANSLATION',
            )      
    rotation: FloatVectorProperty(
            name="Rotation",                             
            subtype='EULER',
            )    
    scale: FloatVectorProperty(
            name="Scale",                             
            subtype='XYZ',
            default=(1, 1, 1)
            )  
    rotation_order: EnumProperty(
            name="Rotation order",
            items=rotation_orders,
            default='2',
            )

def sync_baking_transform(self, context):
    scene = bpy.context.scene
    oct_scene = scene.octane
    baking_layer_settings = oct_scene.baking_layer_settings  
    oct_cam = bpy.data.cameras['Camera'].octane    
    if baking_layer_settings._get_baking_layer_by_idx(oct_cam.baking_group_id) is None:
        baking_layer_settings._add_new_baking_layer(oct_cam.baking_group_id)
    for transform in baking_layer_settings.baking_layer_transform_collections.values():
        if transform.id == oct_cam.baking_group_id:
            oct_cam.baking_uvw_translation = transform.translation
            oct_cam.baking_uvw_rotation = transform.rotation
            oct_cam.baking_uvw_scale = transform.scale
            oct_cam.baking_uvw_rotation_order = transform.rotation_order


class OctaneBakingLayerTransformCollection(bpy.types.PropertyGroup):    
    baking_layer_transform_collections: CollectionProperty(type=OctaneBakingLayerTransform)

    def update_cur_baking_layer_id(self, context):
        #make sure it is initialized
        if not self._delay_init():
            return
        if self._get_baking_layer_by_idx(self.cur_baking_layer_id) is None:
            self._add_new_baking_layer(self.cur_baking_layer_id)
        # self._debug_show_all_baking_layer_info()
        cur_baking_transform = self._get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            self['cur_baking_layer_id'] = cur_baking_transform.id
            self['cur_baking_layer_translation'] = cur_baking_transform.translation
            self['cur_baking_layer_rotation'] = cur_baking_transform.rotation
            self['cur_baking_layer_scale'] = cur_baking_transform.scale
            self['cur_baking_layer_rotation_order'] = cur_baking_transform.rotation_order
        sync_baking_transform()

    #init default baking layer
    cur_baking_layer_id: IntProperty(
            name="Baking Layer ID",
            description="ID of the baking layer",
            update=update_cur_baking_layer_id,
            min=1, max=65535,
            default=1,
            )

    def update_cur_baking_layer_transform(self, context):
        #make sure it is initialized
        if not self._delay_init():
            return
        cur_baking_transform = self._get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            cur_baking_transform.translation = self['cur_baking_layer_translation']
            cur_baking_transform.rotation = self['cur_baking_layer_rotation']
            cur_baking_transform.scale = self['cur_baking_layer_scale']
            cur_baking_transform.rotation_order = str(self['cur_baking_layer_rotation_order'])
        sync_baking_transform()

    cur_baking_layer_translation: FloatVectorProperty(
            name="Translation",
            description="Translation that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",   
            update = update_cur_baking_layer_transform,                             
            subtype='TRANSLATION',
            )      
    cur_baking_layer_rotation: FloatVectorProperty(
            name="Rotation",
            description="Rotation that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = update_cur_baking_layer_transform,
            subtype='EULER',
            )    
    cur_baking_layer_scale: FloatVectorProperty(
            name="Scale",
            description="Scale that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = update_cur_baking_layer_transform,
            subtype='XYZ',
            default=(1, 1, 1)
            )        
    cur_baking_layer_rotation_order: EnumProperty(
            name="Rotation order",
            description="Rotation order that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = update_cur_baking_layer_transform,
            items=rotation_orders,
            default='2',
            )       

    def init(self):
        if not len(self.baking_layer_transform_collections):      
            next_new_baking_layer = self.baking_layer_transform_collections.add()
            next_new_baking_layer.id = 1

    def _add_new_baking_layer(self, idx):
        next_new_baking_layer = self.baking_layer_transform_collections.add()
        next_new_baking_layer.id = idx

    def _get_baking_layer_by_idx(self, idx):
        for baking_layer_transform in self.baking_layer_transform_collections.values():
            if idx == baking_layer_transform.id:
                return baking_layer_transform
        return None        

    def _debug_show_all_baking_layer_info(self):
        for baking_layer_transform in self.baking_layer_transform_collections.values():
            print("Baking Group ID: ", baking_layer_transform.id)
            print(baking_layer_transform.translation)
            print(baking_layer_transform.rotation)
            print(baking_layer_transform.scale)
            print("Rotation Order: ", baking_layer_transform.rotation_order)

    def _delay_init(self):
        if self._get_baking_layer_by_idx(1) is None:
            self._add_new_baking_layer(1)
            return False       
        if not self.__contains__('cur_baking_layer_translation') or not self.__contains__('cur_baking_layer_rotation') or not self.__contains__('cur_baking_layer_scale') or not self.__contains__('cur_baking_layer_rotation_order'):
            self['cur_baking_layer_translation'] = self.cur_baking_layer_translation
            self['cur_baking_layer_rotation'] = self.cur_baking_layer_rotation
            self['cur_baking_layer_scale'] = self.cur_baking_layer_scale
            self['cur_baking_layer_rotation_order'] = self.cur_baking_layer_rotation_order
        return True

    @classmethod
    def register(cls):
        pass

    @classmethod
    def unregister(cls):
        pass


class KernelNodeGraphPropertyGroup(bpy.types.PropertyGroup):
    def poll_kernel_tree(self, node_tree):
        return node_tree.bl_idname == consts.OctaneNodeTreeIDName.KERNEL
    node_tree: PointerProperty(
        name="Kernel Node Graph",
        description="Select the kernel node graph(can be created in the 'Kernel Editor'",
        type=bpy.types.NodeTree,
        poll=poll_kernel_tree,
    )


class RenderAOVNodeGraphPropertyGroup(bpy.types.PropertyGroup):  
    def poll_render_aov_node_tree(self, node_tree):
        return node_tree.bl_idname == consts.OctaneNodeTreeIDName.RENDER_AOV
    node_tree: PointerProperty(
        name="Render AOV Node Graph",
        description="Select the render AOV node graph(can be created in the 'Octane Render AOV Editor'",
        type=bpy.types.NodeTree,
        poll=poll_render_aov_node_tree,
    )


class CompositeNodeGraphPropertyGroup(bpy.types.PropertyGroup):  
    def poll_composite_node_tree(self, node_tree):
        return node_tree.bl_idname == consts.OctaneNodeTreeIDName.COMPOSITE
    node_tree: PointerProperty(
        name="Composite Node Graph",
        description="Select the Octane composite node graph(can be created in the 'Octane Composte Editor'",
        type=bpy.types.NodeTree,
        poll=poll_composite_node_tree,
    )


class OctaneAnimationSettings(bpy.types.PropertyGroup, common.OctanePropertySettings):
    PROPERTY_CONFIGS = {consts.NodeType.NT_ANIMATION_SETTINGS: ["mb_direction",]}
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "mb_direction": "shutterAlignment",
    }

    mb_direction: EnumProperty(
        name="Shutter alignment",
        description="Specifies how the shutter interval is aligned to the current time",
        items=OctaneAnimationSettingsShutterAlignment.items,
        default="After",
    )
    shutter_time: FloatProperty(
        name="Shutter time",
        description="The shutter time percentage relative to the duration of a single frame",                
        default=20.0,                
        precision=0,
        min=0.0, soft_min=0.0, max=100000.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )
    subframe_start: FloatProperty(
        name="Subframe start",
        description="Minimum sub-frame % time to sample",                
        default=0.0,
        precision=0,
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )  
    subframe_end: FloatProperty(
        name="Subframe end",
        description="Maximum sub-frame % time to sample",                
        default=100.0,
        precision=0,
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )

    def draw(self, context, layout, is_viewport=None):
        row = layout.row()
        row.prop(self, "mb_direction")
        row = layout.row()
        row.prop(self, "shutter_time")
        row = layout.row()
        row.prop(self, "subframe_start")
        row = layout.row()
        row.prop(self, "subframe_end")

    def sync_custom_data(self, octane_node, scene, region, v3d, rv3d, is_viewport):
        octane_node.set_pin_id(consts.PinID.P_SHUTTER_TIME, False, "", scene.render.fps * self.shutter_time / 100.0)
        # octane_node.set_pin_id(consts.PinID.P_SHUTTER_TIME, False, "", self.shutter_time / 100.0)
        octane_node.set_pin_id(consts.PinID.P_SUBFRAME_START, False, "", self.subframe_start / 100.0)
        octane_node.set_pin_id(consts.PinID.P_SUBFRAME_END, False, "", self.subframe_end / 100.0)

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        utility.cast_legacy_enum_property(self, "mb_direction", OctaneAnimationSettingsShutterAlignment.items, legacy_data, "mb_direction")
        utility.sync_legacy_property(self, "shutter_time", legacy_data, "shutter_time")
        utility.sync_legacy_property(self, "subframe_start", legacy_data, "subframe_start")
        utility.sync_legacy_property(self, "subframe_end", legacy_data, "subframe_end")


class OctaneGlobalRenderLayer(bpy.types.PropertyGroup, common.OctanePropertySettings):
    PROPERTY_CONFIGS = {consts.NodeType.NT_RENDER_LAYER: ["layers_enable", "layers_current", "layers_invert", "layers_mode",]}
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "layers_enable": "enabled",
        "layers_current": "layerId",
        "layers_invert": "invert",
        "layers_mode": "mode",
    }

    layers_enable: BoolProperty(
        name="Enable",
        description="Tick to enable Octane render layers",
        default=False,
    )
    layers_current: IntProperty(
        name="Active layer ID",
        description="ID of the active render layer",
        min=1, max=255,
        default=1,
    )
    layers_invert: BoolProperty(
        name="Invert",
        description="All the non-active render layers become the active render layer and the active render layer becomes inactive",
        default=False,
    )
    layers_mode: EnumProperty(
        name="Mode",
        description="The render mode that should be used to render layers:\n"
            "\n"
            "'Normal':"
            " The beauty passes contain the active layer only and the render layer passes (shadows,"
            " reflections...) record the side-effects of the active render layer for those samples/pixels"
            " that are not obstructed by the active render layer.\n"
            "\n"
            "'Hide inactive layers':"
            " All geometry that is not on an active layer will be made invisible. No side effects"
            " will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n"
            "\n"
            "'Only side effects':"
            " The active layer will be made invisible and the render layer passes (shadows, reflections...)"
            " record the side-effects of the active render layer. The beauty passes will be empty.\n"
            " This is useful to capture all side-effects without having the active layer obstructing those.\n"
            "\n"
            "'Hide from camera':"
            " Similar to 'Hide inactive layers' All geometry that is not on an active layer"
            " will be made invisible. But side effects(shadows, reflections...)will be recorded in the render layer passes\n"
            "\n",
        items=OctaneRenderLayerMode.items,
        default="Normal",
    )

    def draw(self, context, layout, is_viewport=None):
        col = layout.column()
        col.prop(self, "layers_mode")
        col.prop(self, "layers_current")
        col.prop(self, "layers_invert")        

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        utility.cast_legacy_enum_property(self, "layers_mode", OctaneRenderLayerMode.items, legacy_data, "layers_mode")
        utility.sync_legacy_property(self, "layers_enable", legacy_data, "layers_enable")
        utility.sync_legacy_property(self, "layers_current", legacy_data, "layers_current")
        utility.sync_legacy_property(self, "layers_invert", legacy_data, "layers_invert")        



class OctaneRenderLayer(bpy.types.PropertyGroup, common.OctanePropertySettings):
    PROPERTY_CONFIGS = {
        consts.NodeType.NT_RENDER_LAYER: ["layers_enable", "layers_current", "layers_invert", "layers_mode",]
    }
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        "layers_enable": "enabled",
        "layers_current": "layerId",
        "layers_invert": "invert",
        "layers_mode": "mode",
    }
    LEGACY_LAYER_MODE_CONVERTOR = {
        "OCT_RENDER_LAYER_MODE_NORMAL": "Normal",
        "OCT_RENDER_LAYER_MODE_HIDE_INACTIVE_LAYERS": "Hide inactive layers",
        "OCT_RENDER_LAYER_MODE_ONLY_SIDE_EFFECTS": "Only side effects",
        "OCT_RENDER_LAYER_MODE_HIDE_FROM_CAMERA": "Hide from camera",
    }


    layers_enable: BoolProperty(
        name="Use Octane Render Layer",
        description="Render current layer with the Octane layer system",
        default=False,
    )
    layers_current: IntProperty(
        name="Active layer ID",
        description="ID of the active render layer",
        min=1, max=255,
        default=1,
    )
    layers_invert: BoolProperty(
        name="Invert",
        description="All the non-active render layers become the active render layer and the active render layer becomes inactive",
        default=False,
    )
    layers_mode: EnumProperty(
        name="Mode",
        description="The render mode that should be used to render layers:\n"
            "\n"
            "'Normal':"
            " The beauty passes contain the active layer only and the render layer passes (shadows,"
            " reflections...) record the side-effects of the active render layer for those samples/pixels"
            " that are not obstructed by the active render layer.\n"
            "\n"
            "'Hide inactive layers':"
            " All geometry that is not on an active layer will be made invisible. No side effects"
            " will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n"
            "\n"
            "'Only side effects':"
            " The active layer will be made invisible and the render layer passes (shadows, reflections...)"
            " record the side-effects of the active render layer. The beauty passes will be empty.\n"
            " This is useful to capture all side-effects without having the active layer obstructing those.\n"
            "\n"
            "'Hide from camera':"
            " Similar to 'Hide inactive layers' All geometry that is not on an active layer"
            " will be made invisible. But side effects(shadows, reflections...)will be recorded in the render layer passes\n"
            "\n",
        items=OctaneRenderLayerMode.items,
        default="Normal",
    )
    render_aov_node_graph_property: PointerProperty(
        name="Render AOV Node Graph Property",
        description="",
        type=RenderAOVNodeGraphPropertyGroup,
    )
    composite_node_graph_property: PointerProperty(
        name="Composite Node Graph Property",
        description="",
        type=CompositeNodeGraphPropertyGroup,
    )

    use_passes: BoolProperty(
        name="Render passes",
        description="",
        default=False,
    )
    info_pass_max_samples: IntProperty(
        name="Info pass max samples",
        description="The maximum number of samples for the info passes (excluding AO)",
        min=1, max=1024,
        default=128,
    )
    info_pass_sampling_mode: EnumProperty(
        name="Sampling mode",
        description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
            "'Distributed rays':"
            " Enables motion blur and DOF, and also enables pixel filtering.\n"
            "'Non-distributed with pixel filtering':"
            " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
            "'Non-distributed without pixel filtering':"
            " Disables motion blur and DOF, and disables pixel filtering for all render passes"
            " except for render layer mask and ambient occlusion\n",
        items=info_pass_sampling_modes,
        default='0',
    )
    info_pass_z_depth_max: FloatProperty(
        name="Z-depth max",
        description="Z-depth value mapped to white (0 is mapped to black)",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=5.0,
        step=10,
        precision=4,
    )
    info_pass_uv_max: FloatProperty(
        name="UV max",
        description="UV coordinate value mapped to maximum intensity",
        min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
        default=1.0,
        step=10,
        precision=5,
    )
    info_pass_uv_coordinate_selection: IntProperty(
        name="UV coordinate selection",
        description="Determines which set of UV coordinates to use",
        min=1, max=3,
        default=1,
    )        
    info_pass_max_speed: FloatProperty(
        name="Max speed",
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
        min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
        default=1.0,
        step=10,
        precision=5,
    )
    info_pass_ao_distance: FloatProperty(
        name="AO distance",
        description="Ambient occlusion distance",
        min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
        default=3.0,
        step=10,
        precision=2,
    )
    info_pass_alpha_shadows: BoolProperty(
        name="AO alpha shadows",
        description="Take into account alpha maps when calculating ambient occlusion",
        default=False,
    )
    pass_raw: BoolProperty(
        name="Raw",
        description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray",
        default=False,
    )
    pass_pp_env: BoolProperty(
        name="Include environment",
        description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled",
        default=False,
    )
    info_pass_bump: BoolProperty(
        name="Bump and normal mapping",
        description="Take bump and normal mapping into account for shading normal output and wireframe shading",
        default=True,
    )
    info_pass_opacity_threshold: FloatProperty(
        name="Opacity threshold",
        description="Geometry with opacity higher or equal to this value is treated as totally opaque",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    cryptomatte_pass_channels: EnumProperty(
        name="Channels",
        description="Amount of cryptomatte channels to render",
        items=cryptomatte_pass_channel_modes,
        default='2',
    )
    cryptomatte_seed_factor: IntProperty(
        name="Cryptomatte seed factor",
        description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. Low values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs",
        min=4, max=25,
        default=10,
    )
    octane_render_pass_types = (
        ('0', "Combined", "Combined pass", 0),

        ('1', "Emitters", "Emitters pass", 1),
        ('2', "Environment", "Environment pass", 2),

        ('3', "Diffuse", "Diffuse pass", 3),
        ('4', "Diffuse direct", "Diffuse direct pass", 4),
        ('5', "Diffuse indirect", "Diffuse indirect pass", 5),
        ('6', "Diffuse filter", "Diffuse filter pass", 6),

        ('7', "Reflection", "Reflection pass", 7),
        ('8', "Reflection direct", "Reflection direct pass", 8),
        ('9', "Reflection indirect", "Reflection indirect pass", 9),
        ('10', "Reflection filter", "Reflection filter pass", 10),

        ('11', "Refraction", "Refraction pass pass", 11),
        ('12', "Refraction filter", "Refraction filter pass pass", 12),
        ('13', "Transmission", "Transmission pass", 13),
        ('14', "Transmission filter", "Transmission filter pass", 14),

        ('15', "Subsurface scattering", "Subsurface scattering pass", 15),
        ('16', "Post processing", "Post processing pass", 16),

        ('17', "Layer shadows", "Layer shadows pass", 17),
        ('18', "Layer black shadows", "Layer black shadows pass", 18),
        ('20', "Layer reflections", "Layer reflections pass", 20),

        ('21', "Ambient light", "Ambient light pass", 21),
        ('22', "Sunlight", "Sunlight pass", 22),
        ('23', "Light pass 1", "Light pass 1", 23),
        ('24', "Light pass 2", "Light pass 2", 24),
        ('25', "Light pass 3", "Light pass 3", 25),
        ('26', "Light pass 4", "Light pass 4", 26),
        ('27', "Light pass 5", "Light pass 5", 27),
        ('28', "Light pass 6", "Light pass 6", 28),
        ('29', "Light pass 7", "Light pass 7", 29),
        ('30', "Light pass 8", "Light pass 8", 30),
        ('31', "Noise", "Noise pass", 31),
        ('32', "Shadow", "Shadow pass", 32),
        ('33', "Irradiance", "Irradiance pass", 33),
        ('34', "Light Direction", "Light Direction pass", 34),
        ('35', "Volume", "Volume pass", 35),
        ('36', "Volume Mask", "Volume Mask pass", 36),
        ('37', "Volume Emission", "Volume Emission pass", 37),
        ('38', "Volume Z-Depth Front", "Volume Z-Depth Front pass", 38),
        ('39', "Volume Z-Depth Back", "Volume Z-Depth Back pass", 39),

        ('43', "Denoiser Beauty", "Denoiser Beauty pass", 43),
        ('44', "Denoiser DiffDir", "Denoiser Diffuse Direct pass", 44),
        ('45', "Denoiser DiffIndir", "Denoiser Diffuse Indirect pass", 45),
        ('46', "Denoiser ReflectDir", "Denoiser Reflection Direct pass", 46),
        ('47', "Denoiser ReflectIndir", "Denoiser Reflection Indirect pass", 47),
        #('48', "Denoiser Refraction", "Denoiser Refraction pass"),
        ('49', "Denoiser Refraction", "Denoiser Refraction(Remainder) pass", 49),
        ('76', "Denoiser Emission", "Denoiser Emission pass", 76),
        ('74', "Denoiser Volume", "Denoiser Volume pass", 74),
        ('75', "Denoiser Volume Emission", "Denoiser Volume Emission pass", 75),

        ('54', "Ambient light direct", "Ambient light direct pass", 54),
        ('55', "Ambient light indirect", "Ambient light indirect pass", 55),
        ('56', "Sunlight direct", "Sunlight direct pass", 56),
        ('57', "Sunlight indirect", "Sunlight indirect pass", 57),
        ('58', "Light pass 1 direct", "Light pass 1 direct", 58),    
        ('59', "Light pass 2 direct", "Light pass 2 direct", 59),
        ('60', "Light pass 3 direct", "Light pass 3 direct", 60),
        ('61', "Light pass 4 direct", "Light pass 4 direct", 61),
        ('62', "Light pass 5 direct", "Light pass 5 direct", 62),
        ('63', "Light pass 6 direct", "Light pass 6 direct", 63),
        ('64', "Light pass 7 direct", "Light pass 7 direct", 64),
        ('65', "Light pass 8 direct", "Light pass 8 direct", 65),   
        ('66', "Light pass 1 indirect", "Light pass 1 indirect", 66),    
        ('67', "Light pass 2 indirect", "Light pass 2 indirect", 67),
        ('68', "Light pass 3 indirect", "Light pass 3 indirect", 68),
        ('69', "Light pass 4 indirect", "Light pass 4 indirect", 69),
        ('70', "Light pass 5 indirect", "Light pass 5 indirect", 70),
        ('71', "Light pass 6 indirect", "Light pass 6 indirect", 71),
        ('72', "Light pass 7 indirect", "Light pass 7 indirect", 72),
        ('73', "Light pass 8 indirect", "Light pass 8 indirect", 73),       

        ('1000', "Geometric normals", "Geometric normals pass", 1000),
        ('1001', "Shading normals", "Shading normals pass", 1001),
        ('1002', "Position", "Position pass", 1002),
        ('1003', "Z-depth", "Z-depth pass", 1003),
        ('1004', "Material id", "Material id pass", 1004),
        ('1005', "UV coordinates", "UV coordinates pass", 1005),
        ('1006', "Tangents", "Tangents pass", 1006),
        ('1007', "Wireframe", "Wireframe pass", 1007),
        ('1008', "Smooth normals", "Smooth normals pass", 1008),
        ('1009', "Object id", "Object id pass", 1009),    
        ('1010', "Ambient occlusion", "Ambient occlusion pass", 1010),
        ('1011', "Motion vector", "Motion vector pass", 1011),
        ('1012', "Render layer ID", "Colours objects on the same layer with the same color based on the render layer ID", 1012),
        ('1013', "Render layer mask", "Mask for geometry on the active render layer", 1013),
        ('1014', "Light pass ID", "Light pass ID pass", 1014),
        ('1015', "Tangent normals", "Tangent normals pass", 1015),
        ('1016', "Info Opacity", "Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry", 1016),
        ('1017', "Baking group ID", "Colours each distinct baking group in the scene with a colour based on it's ID", 1017),
        ('1018', "Info Roughness", "Material roughness at the camera ray's hit point", 1018),
        ('1019', "Info IOR", "Material index of refraction at the camera ray's hit point", 1019),
        ('1020', "Info DiffFilter", "The diffuse texture color of the diffuse and glossy material", 1020),
        ('1021', "Info ReflectFilter", "The reflection texture color of the specular and glossy material", 1021),
        ('1022', "Info RefractFilter", "The refraction texture color of the specular material", 1022),    
        ('1023', "Info TransmFilter", "The transmission texture color of the diffuse material", 1023),    
        ('1024', "Object layer color", "The color specified in the object layer node", 1024),

        ('2001', "Cryptomatte MaterialName", "Cryptomatte channels for material node names", 2001), 
        ('2006', "Cryptomatte MaterialNode", "Cryptomatte channels using distinct material nodes", 2006),    
        ('2002', "Cryptomatte MaterialPinName", "Cryptomatte channels for material pin names", 2002), 
        ('2003', "Cryptomatte ObjectName", "Cryptomatte channels for object layer node names", 2003), 
        ('2004', "Cryptomatte ObjectNode", "Cryptomatte channels using distinct object layer nodes", 2004),    
        ('2007', "Cryptomatte ObjectPinName", "Cryptomatte channels for object layer pin names", 2007), 
        # Not suitable for the legacy render pass system
        # ('2009', "Cryptomatte RenderLayer", "Cryptomatte channels for render layers", 2009), 

        ('2005', "Cryptomatte InstanceID", "Cryptomatte channels for instance IDs", 2005),    
        # Not suitable for the legacy render pass system
        # ('2008', "Cryptomatte GeometryNodeName", "Cryptomatte channels for geometry node names", 2008), 
        # ('2010', "Cryptomatte UserInstanceID", "Cryptomatte channels for user instance IDs", 2010), 

        ('10000', "AOV Output", "AOV Outputs", 10000),   
    )    
    current_preview_pass_type: EnumProperty(
        name="Preview pass type",
        description="Pass used for preview rendering",
        items=octane_render_pass_types,
        default='0',
    )
    current_aov_output_id: IntProperty(
        name="Preivew AOV Output ID",
        description="The ID of the AOV Outputs for preview(beauty pass output will be used if no valid results for the assigned index)",
        min=1, max=16,
        default=1,
    )
    aov_output_group_collection: PointerProperty(
        name="Octane Aov Output Group Collection",
        description="",
        type=OctaneAovOutputGroupCollection,
    )
    render_passes_style = (
        ('RENDER_PASSES', "Classic Render Passes", "The classic render passes style but the new render AOVs won't be available there", 0),
        ('RENDER_AOV_GRAPH', "Render AOV Node Graph", "The render AOV node graph with the AOV features", 1),
    )    
    render_pass_style: EnumProperty(
        name="Render Passes Style",
        description="Use the classic Render Passes or the new Render AOV Graph",
        items=render_passes_style,
        default="RENDER_PASSES",
        update=utility.update_render_passes
    )

    def draw(self, context, layout, is_viewport=None):
        col = layout.column()
        col.prop(self, "layers_mode")
        col.prop(self, "layers_current")
        col.prop(self, "layers_invert")        

    def update_legacy_data(self, context, legacy_data, is_viewport=None): 
        self.layers_mode = self.LEGACY_LAYER_MODE_CONVERTOR.get(getattr(legacy_data, "octane_render_layers_mode", ""), "Normal")
        utility.sync_legacy_property(self, "layers_enable", legacy_data, "use_octane_render_layers")
        utility.sync_legacy_property(self, "layers_current", legacy_data, "octane_render_layer_active_id")
        utility.sync_legacy_property(self, "layers_invert", legacy_data, "octane_render_layers_invert")

    @classmethod
    def register(cls):
        bpy.types.ViewLayer.octane = PointerProperty(
            name="Octane RenderLayer Settings",
            description="Octane RenderLayer settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.ViewLayer.octane


class OctaneRenderSettings(bpy.types.PropertyGroup):

# ################################################################################################
# OCTANE BLENDER RENDER VERSION
# ################################################################################################        
    octane_blender_version: StringProperty(
        name="",
        description="",
        default="",
        maxlen=128,
    )
    octane_version: IntProperty(
        name="",
        default=0,
    )
# ################################################################################################
# OCTANE OPTIMIZATION
# ################################################################################################        
    octane_opt_mesh_generation: BoolProperty(
        name="Use Opt. Mesh Generation Mode in Preview",
        description="[PREVIEW MODE] Do not regenerate & upload meshes(except reshapble ones) which are already cached",
        default=False,
    )
# ################################################################################################
# OCTANE KERNEL
# ################################################################################################            
    kernel_node_graph_property: PointerProperty(
        name="Kernel Node Graph",
        description="Select the kernel node graph(can be created in the 'Kernel Editor'",
        type=KernelNodeGraphPropertyGroup,
    )
# ################################################################################################
# OCTANE ANIMATION SETTINGS
# ################################################################################################  
    animation_settings: PointerProperty(
        name="Octane Animation Settings",
        description="",
        type=OctaneAnimationSettings,
    )
# ################################################################################################
# OCTANE RENDER LAYER
# ################################################################################################  
    render_layer: PointerProperty(
        name="Octane Render Layer",
        description="",
        type=OctaneGlobalRenderLayer,
    )
# ################################################################################################
# OCTANE RENDER PASSES
# ################################################################################################
    use_passes: BoolProperty(
        name="Render passes",
        description="",
        default=False,
    )
    info_pass_max_samples: IntProperty(
        name="Info pass max samples",
        description="The maximum number of samples for the info passes (excluding AO)",
        min=1, max=1024,
        default=128,
    )
    info_pass_sampling_mode: EnumProperty(
        name="Sampling mode",
        description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
            "'Distributed rays':"
            " Enables motion blur and DOF, and also enables pixel filtering.\n"
            "'Non-distributed with pixel filtering':"
            " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
            "'Non-distributed without pixel filtering':"
            " Disables motion blur and DOF, and disables pixel filtering for all render passes"
            " except for render layer mask and ambient occlusion\n",
        items=info_pass_sampling_modes,
        default='0',
    )
    info_pass_z_depth_max: FloatProperty(
        name="Z-depth max",
        description="Z-depth value mapped to white (0 is mapped to black)",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=5.0,
        step=10,
        precision=4,
    )
    info_pass_uv_max: FloatProperty(
        name="UV max",
        description="UV coordinate value mapped to maximum intensity",
        min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
        default=1.0,
        step=10,
        precision=5,
    )
    info_pass_uv_coordinate_selection: IntProperty(
        name="UV coordinate selection",
        description="Determines which set of UV coordinates to use",
        min=1, max=3,
        default=1,
    )        
    info_pass_max_speed: FloatProperty(
        name="Max speed",
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
        min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
        default=1.0,
        step=10,
        precision=5,
    )
    info_pass_ao_distance: FloatProperty(
        name="AO distance",
        description="Ambient occlusion distance",
        min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
        default=3.0,
        step=10,
        precision=2,
    )
    info_pass_alpha_shadows: BoolProperty(
        name="AO alpha shadows",
        description="Take into account alpha maps when calculating ambient occlusion",
        default=False,
    )
    pass_raw: BoolProperty(
        name="Raw",
        description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray",
        default=False,
    )
    pass_pp_env: BoolProperty(
        name="Include environment",
        description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled",
        default=False,
    )
    info_pass_bump: BoolProperty(
        name="Bump and normal mapping",
        description="Take bump and normal mapping into account for shading normal output and wireframe shading",
        default=True,
    )
    info_pass_opacity_threshold: FloatProperty(
        name="Opacity threshold",
        description="Geometry with opacity higher or equal to this value is treated as totally opaque",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=10,
        precision=3,
    )
    cryptomatte_pass_channels: EnumProperty(
        name="Channels",
        description="Amount of cryptomatte channels to render",
        items=cryptomatte_pass_channel_modes,
        default='2',
    )
    cryptomatte_seed_factor: IntProperty(
        name="Cryptomatte seed factor",
        description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. Low values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs",
        min=4, max=25,
        default=10,
    )   
    pass_types = (
        ('0', "Combined", "Combined pass"),

        ('1', "Emitters", "Emitters pass"),
        ('2', "Environment", "Environment pass"),

        ('3', "Diffuse", "Diffuse pass"),
        ('4', "Diffuse direct", "Diffuse direct pass"),
        ('5', "Diffuse indirect", "Diffuse indirect pass"),
        ('6', "Diffuse filter", "Diffuse filter pass"),

        ('7', "Reflection", "Reflection pass"),
        ('8', "Reflection direct", "Reflection direct pass"),
        ('9', "Reflection indirect", "Reflection indirect pass"),
        ('10', "Reflection filter", "Reflection filter pass"),

        ('11', "Refraction", "Refraction pass pass"),
        ('12', "Refraction filter", "Refraction filter pass pass"),
        ('13', "Transmission", "Transmission pass"),
        ('14', "Transmission filter", "Transmission filter pass"),

        ('15', "Subsurface scattering", "Subsurface scattering pass"),
        ('16', "Post processing", "Post processing pass"),

        ('17', "Layer shadows", "Layer shadows pass"),
        ('18', "Layer black shadows", "Layer black shadows pass"),
        ('20', "Layer reflections", "Layer reflections pass"),

        ('21', "Ambient light", "Ambient light pass"),
        ('22', "Sunlight", "Sunlight pass"),
        ('23', "Light pass 1", "Light pass 1"),
        ('24', "Light pass 2", "Light pass 2"),
        ('25', "Light pass 3", "Light pass 3"),
        ('26', "Light pass 4", "Light pass 4"),
        ('27', "Light pass 5", "Light pass 5"),
        ('28', "Light pass 6", "Light pass 6"),
        ('29', "Light pass 7", "Light pass 7"),
        ('30', "Light pass 8", "Light pass 8"),
        ('31', "Noise", "Noise pass"),
        ('32', "Shadow", "Shadow pass"),
        ('33', "Irradiance", "Irradiance pass"),
        ('34', "Light Direction", "Light Direction pass"),
        ('35', "Volume", "Volume pass"),
        ('36', "Volume Mask", "Volume Mask pass"),
        ('37', "Volume Emission", "Volume Emission pass"),
        ('38', "Volume Z-Depth Front", "Volume Z-Depth Front pass"),
        ('39', "Volume Z-Depth Back", "Volume Z-Depth Back pass"),

        ('43', "Denoiser Beauty", "Denoiser Beauty pass"),
        ('44', "Denoiser DiffDir", "Denoiser Diffuse Direct pass"),
        ('45', "Denoiser DiffIndir", "Denoiser Diffuse Indirect pass"),
        ('46', "Denoiser ReflectDir", "Denoiser Reflection Direct pass"),
        ('47', "Denoiser ReflectIndir", "Denoiser Reflection Indirect pass"),
        #('48', "Denoiser Refraction", "Denoiser Refraction pass"),
        ('49', "Denoiser Refraction", "Denoiser Refraction(Remainder) pass"),
        ('76', "Denoiser Emission", "Denoiser Emission pass"),
        ('74', "Denoiser Volume", "Denoiser Volume pass"),
        ('75', "Denoiser Volume Emission", "Denoiser Volume Emission pass"),

        ('54', "Ambient light direct", "Ambient light direct pass"),
        ('55', "Ambient light indirect", "Ambient light indirect pass"),
        ('56', "Sunlight direct", "Sunlight direct pass"),
        ('57', "Sunlight indirect", "Sunlight indirect pass"),
        ('58', "Light pass 1 direct", "Light pass 1 direct"),    
        ('59', "Light pass 2 direct", "Light pass 2 direct"),
        ('60', "Light pass 3 direct", "Light pass 3 direct"),
        ('61', "Light pass 4 direct", "Light pass 4 direct"),
        ('62', "Light pass 5 direct", "Light pass 5 direct"),
        ('63', "Light pass 6 direct", "Light pass 6 direct"),
        ('64', "Light pass 7 direct", "Light pass 7 direct"),
        ('65', "Light pass 8 direct", "Light pass 8 direct"),   
        ('66', "Light pass 1 indirect", "Light pass 1 indirect"),    
        ('67', "Light pass 2 indirect", "Light pass 2 indirect"),
        ('68', "Light pass 3 indirect", "Light pass 3 indirect"),
        ('69', "Light pass 4 indirect", "Light pass 4 indirect"),
        ('70', "Light pass 5 indirect", "Light pass 5 indirect"),
        ('71', "Light pass 6 indirect", "Light pass 6 indirect"),
        ('72', "Light pass 7 indirect", "Light pass 7 indirect"),
        ('73', "Light pass 8 indirect", "Light pass 8 indirect"),       

        ('1000', "Geometric normals", "Geometric normals pass"),
        ('1001', "Shading normals", "Shading normals pass"),
        ('1002', "Position", "Position pass"),
        ('1003', "Z-depth", "Z-depth pass"),
        ('1004', "Material id", "Material id pass"),
        ('1005', "UV coordinates", "UV coordinates pass"),
        ('1006', "Tangents", "Tangents pass"),
        ('1007', "Wireframe", "Wireframe pass"),
        ('1008', "Smooth normals", "Smooth normals pass"),
        ('1009', "Object id", "Object id pass"),    
        ('1010', "Ambient occlusion", "Ambient occlusion pass"),
        ('1011', "Motion vector", "Motion vector pass"),
        ('1012', "Render layer ID", "Colours objects on the same layer with the same color based on the render layer ID"),
        ('1013', "Render layer mask", "Mask for geometry on the active render layer"),
        ('1014', "Light pass ID", "Light pass ID pass"),
        ('1015', "Tangent normals", "Tangent normals pass"),
        ('1016', "Info Opacity", "Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry"),
        ('1017', "Baking group ID", "Colours each distinct baking group in the scene with a colour based on it's ID"),
        ('1018', "Info Roughness", "Material roughness at the camera ray's hit point"),
        ('1019', "Info IOR", "Material index of refraction at the camera ray's hit point"),
        ('1020', "Info DiffFilter", "The diffuse texture color of the diffuse and glossy material"),
        ('1021', "Info ReflectFilter", "The reflection texture color of the specular and glossy material"),
        ('1022', "Info RefractFilter", "The refraction texture color of the specular material"),    
        ('1023', "Info TransmFilter", "The transmission texture color of the diffuse material"),    
        ('1024', "Object layer color", "The color specified in the object layer node"),

        ('2001', "Cryptomatte MaterialName", "Cryptomatte channels for material node names"), 
        ('2006', "Cryptomatte MaterialNode", "Cryptomatte channels using distinct material nodes"),    
        ('2002', "Cryptomatte MaterialPinName", "Cryptomatte channels for material pin names"), 

        ('2003', "Cryptomatte ObjectName", "Cryptomatte channels for object layer node names"), 
        ('2004', "Cryptomatte ObjectNode", "Cryptomatte channels using distinct object layer nodes"),    
        ('2007', "Cryptomatte ObjectPinName", "Cryptomatte channels for object layer pin names"), 
        # Not suitable for the legacy render pass system
        # ('2009', "Cryptomatte RenderLayer", "Cryptomatte channels for render layers"), 
        
        ('2005', "Cryptomatte InstanceID", "Cryptomatte channels for instance IDs"),    
        # Not suitable for the legacy render pass system
        # ('2008', "Cryptomatte GeometryNodeName", "Cryptomatte channels for geometry node names"), 
        # ('2010', "Cryptomatte UserInstanceID", "Cryptomatte channels for user instance IDs"), 
    )
    cur_pass_type: EnumProperty(
        name="Preview pass type",
        description="Pass used for preview rendering",
        items=pass_types,
        default='0',
    )
# ################################################################################################
# OCTANE BAKING LAYER TRANSFORMS
# ################################################################################################
    baking_layer_settings: PointerProperty(
        name="Octane Baking Layer Transforms",
        description="",
        type=OctaneBakingLayerTransformCollection,
    )
# ################################################################################################
# OCTANE LAYERS
# ################################################################################################
    layers_enable: BoolProperty(
        name="Enable",
        description="Tick to enable Octane render layers",
        default=False,
    )
    layers_current: IntProperty(
        name="Active layer ID",
        description="ID of the active render layer",
        min=1, max=255,
        default=1,
    )
    layers_invert: BoolProperty(
        name="Invert",
        description="All the non-active render layers become the active render layer and the active render layer becomes inactive",
        default=False,
    )
    layer_modes = (
        ('0', "Normal", ""),
        ('1', "Hide inactive layers", ""),
        ('2', "Only side effects", ""),
        ('3', "Hide from camera", ""),
    )
    layers_mode: EnumProperty(
        name="Mode",
        description="The render mode that should be used to render layers:\n"
            "\n"
            "'Normal':"
            " The beauty passes contain the active layer only and the render layer passes (shadows,"
            " reflections...) record the side-effects of the active render layer for those samples/pixels"
            " that are not obstructed by the active render layer.\n"
            "\n"
            "'Hide inactive layers':"
            " All geometry that is not on an active layer will be made invisible. No side effects"
            " will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n"
            "\n"
            "'Only side effects':"
            " The active layer will be made invisible and the render layer passes (shadows, reflections...)"
            " record the side-effects of the active render layer. The beauty passes will be empty.\n"
            " This is useful to capture all side-effects without having the active layer obstructing those.\n"
            "\n"
            "'Hide from camera':"
            " Similar to 'Hide inactive layers' All geometry that is not on an active layer"
            " will be made invisible. But side effects(shadows, reflections...)will be recorded in the render layer passes\n"
            "\n",
        items=layer_modes,
        default='0',
    )
# ################################################################################################
# OCTANE OUT OF CORE
# ################################################################################################
    out_of_core_enable: BoolProperty(
        name="Enable out of core",
        description="Tick to enable Octane out of core",
        default=False,
    )
    out_of_core_limit: IntProperty(
        name="Out of core memory limit (MB)",
        description="Maximal amount of memory to be used for out-of-core textures",
        min=1,
        default=4096,
    )
    out_of_core_gpu_headroom: IntProperty(
        name="GPU headroom (MB)",
        description="To run the render kernels successfully, there needs to be some amount of free GPU memory. This setting determines how much GPU memory the render engine will leave available when uploading the images. The default value should work for most scenes",
        min=1,
        default=300,
    )
# ################################################################################################
# OCTANE COMMON
# ################################################################################################
    viewport_hide: BoolProperty(
        name="Viewport hide priority",
        description="Hide from final render objects hidden in viewport",
        default=False,
    )
    prefer_tonemap: BoolProperty(
        name="Prefer tonemap if applicable",
        description="Render as tonemapped image if applicable",
        default=True,
    )
    export_with_object_layers: BoolProperty(
        name="Export with object layers",
        description="Export with object layers properties. If disabled, all object layer properties will be removed and the whole scene will be put in a single object layer",
        default=True,
    ) 
    maximize_instancing: BoolProperty(
        name="Maximize Instancing",
        description="If enabled, Octane will try to collect and group instances into scatter as much as possible",
        default=True,
    )
    meshes_render_types = (
        ('0', "Global", ""),
        ('1', "Scatter", ""),
        ('2', "Movable", ""),
        ('3', "Reshapable", ""),
        ('4', "As is", ""),
    )
    meshes_type: EnumProperty(
        name="Render all meshes as",
        description="Override all meshes type by this type during rendering",
        items=meshes_render_types,
        default='4',
    )
    resource_cache_types = (
        ('None', "None", "Disable resource cache system", 0),
        ('Texture Only', "Texture Only", "Only cache the textures in RAM", 1),    
        ('Geometry Only', "Geometry Only", "Only cache the geometries in RAM", 2),
        ('All', "All", "Cache the textures and geometries in RAM", 127),        
    )
    resource_cache_type: EnumProperty(
        name="Resource Cache System",
        description="Cache the textures and geometries in RAM so to make the viewport rendering initialization faster",
        items=resource_cache_types,
        default='All',
    )
    dirty_resource_detection_strategy_types = (
        ('Edit Mode', "Edit Mode", "A mesh will be marked as dirty and reloaded once the edit mode is on", 0),
        ('Select', "Select", "A mesh will be marked as dirty and reloaded once it is selected", 1),
    )
    dirty_resource_detection_strategy_type: EnumProperty(
        name="Dirty Resource Detection Strategy",
        description="The strategy used in detecting whether a mesh is dirty so a reloading is required",
        items=dirty_resource_detection_strategy_types,
        default='Edit Mode',
    )
    priority_modes = (
        ('Low', "Low", "", 0),
        ('Medium', "Medium", "", 1),
        ('High', "High", "", 2),
    )
    priority_mode: EnumProperty(
        name="Render Priority",
        description="Render priority that should be used for rendering",
        items=priority_modes,
        default='High',
    )
    anim_modes = (
        ('0', "Full", ""),
        ('1', "Movable proxies", ""),
        ('2', "Camera only", ""),
    )
    anim_mode: EnumProperty(
        name="Animation mode",
        description="Optimize animation rendering speed (use in conjunction with Octane mesh types, see the manual)",
        items=anim_modes,
        default='0',
    )
    devices: BoolVectorProperty(
        name="GPU",
        description="Devices to use for rendering",
        default=(True, False, False, False, False, False, False, False),
        size=8,
    )
    stand_login: StringProperty(
        name="Stand",
        description="Octane standalone login",
        default="",
        maxlen=128,
    )
    stand_pass: StringProperty(
        name="",
        description="Octane standalone password",
        default="",
        maxlen=128,
    )
    server_login: StringProperty(
        name="Plugin",
        description="Octane render-server login",
        default="",
        maxlen=128,
    )
    server_pass: StringProperty(
        name="",
        description="Octane render-server password",
        default="",
        maxlen=128,
    )
    mb_types = (
        ('0', "Internal", ""),
        ('1', "Subframe", ""),
    )
    mb_type: EnumProperty(
        name="Motion blur type",
        description="",
        items=mb_types,
        default='1',
    )
    mb_directions = (
        ('0', "After", ""),
        ('1', "Before", ""),
        ('2', "Symmetric", ""),
    )    
    mb_direction: EnumProperty(
        name="Shutter alignment",
        description="Specifies how the shutter interval is aligned to the current time",
        items=mb_directions,
        default='0',
    )
    shutter_time: FloatProperty(
        name="Shutter time",
        description="The shutter time percentage relative to the duration of a single frame",                
        default=20.0,                
        precision=0,
        min=0.0, soft_min=0.0, max=100000.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )
    subframe_start: FloatProperty(
        name="Subframe start",
        description="Minimum sub-frame % time to sample",                
        default=0.0,
        precision=0,
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )  
    subframe_end: FloatProperty(
        name="Subframe end",
        description="Maximum sub-frame % time to sample",                
        default=100.0,
        precision=0,
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )
    kernel_types = (
        ('0', "Default", ""),
        ('1', "Direct light", ""),
        ('2', "Path trace", ""),
        ('3', "PMC", ""),
        ('4', "Info-channel", ""),
        ('5', "Photon tracing", ""),
    )
    kernel_type: EnumProperty(
        name="Kernel type",
        description="",
        items=kernel_types,
        default='2',
    )
    max_samples: IntProperty(
        name="Max. samples",
        description="Number of samples to render for each pixel",
        min=1, max=100000,
        default=500,
    )
    max_preview_samples: IntProperty(
        name="Max. preview samples",
        description="Number of samples to render for each pixel for preview",
        min=1, max=100000,
        default=100,
    )
    max_subdivision_level: IntProperty(
        name="Max. subdivision level",
        description="The Maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision",
        min=0, max=10,
        default=10,
    )    
    filter_size: FloatProperty(
        name="Filter size",
        description="Film splatting width (to reduce aliasing)",
        min=1.0, soft_min=1.0, max=16.0, soft_max=16.0,
        default=1.2,
        step=10,
        precision=2,
    )
    ray_epsilon: FloatProperty(
        name="Ray epsilon",
        description="Shadow ray offset distance to avoid self-intersection",
        min=0.000001, soft_min=0.000001, max=0.1, soft_max=0.1,
        default=0.0001,
        step=10,
        precision=6,
    )
    alpha_channel: BoolProperty(
        name="Alpha channel",
        description="Enables a compositing alpha channel",
        default=False,
    )
    alpha_shadows: BoolProperty(
        name="Alpha shadows",
        description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled",
        default=True,
    )
    keep_environment: BoolProperty(
        name="Keep environment",
        description="Keeps environment with enabled alpha channel",
        default=False,
    )
    irradiance_mode: BoolProperty(
        name="Irradiance mode",
        description="Render the first surface as a white diffuse material",
        default=False,
    )
    nested_dielectrics: BoolProperty(
        name="Nested dielectrics",
        description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored",
        default=True,
    )              
    ai_light_enable: BoolProperty(
        name="AI light",
        description="Enables AI light",
        default=False,
    )   
    ai_light_update: BoolProperty(
        name="AI light update",
        description="Enables dynamic AI light update",
        default=True,
    )    
    ai_light_strength: FloatProperty(
        name="AI light strength",
        description="The strength for dynamic AI light update",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.8,
        step=1,
        precision=3,
    )
    light_ids_action_type = (
        ('Disable', "Disable", '', 1),
        ('Enable', "Enable", '', 0),
    )
    light_ids_action: EnumProperty(
        name="Light IDs action",
        description="The action to be taken on selected lights IDs",
        items=light_ids_action_type,
        default='Disable',
    )    
    light_id_sunlight: BoolProperty(
        name="Sunlight",
        description="Sunlight",
        default=False,
    )           
    light_id_env: BoolProperty(
        name="Environment",
        description="Environment",
        default=False,
    )    
    light_id_pass_1: BoolProperty(
        name="Pass 1",
        description="Pass 1",
        default=False,
    ) 
    light_id_pass_2: BoolProperty(
        name="Pass 2",
        description="Pass 2",
        default=False,
    ) 
    light_id_pass_3: BoolProperty(
        name="Pass 3",
        description="Pass 3",
        default=False,
    ) 
    light_id_pass_4: BoolProperty(
        name="Pass 4",
        description="Pass 4",
        default=False,
    ) 
    light_id_pass_5: BoolProperty(
        name="Pass 5",
        description="Pass 5",
        default=False,
    ) 
    light_id_pass_6: BoolProperty(
        name="Pass 6",
        description="Pass 6",
        default=False,
    ) 
    light_id_pass_7: BoolProperty(
        name="Pass 7",
        description="Pass 7",
        default=False,
    ) 
    light_id_pass_8: BoolProperty(
        name="Pass 8",
        description="Pass 8",
        default=False,
    )      
    light_id_sunlight_invert: BoolProperty(
        name="Sunlight",
        description="Sunlight",
        default=False,
    )           
    light_id_env_invert: BoolProperty(
        name="Environment",
        description="Environment",
        default=False,
    )    
    light_id_pass_1_invert: BoolProperty(
        name="Pass 1",
        description="Pass 1",
        default=False,
    ) 
    light_id_pass_2_invert: BoolProperty(
        name="Pass 2",
        description="Pass 2",
        default=False,
    ) 
    light_id_pass_3_invert: BoolProperty(
        name="Pass 3",
        description="Pass 3",
        default=False,
    ) 
    light_id_pass_4_invert: BoolProperty(
        name="Pass 4",
        description="Pass 4",
        default=False,
    ) 
    light_id_pass_5_invert: BoolProperty(
        name="Pass 5",
        description="Pass 5",
        default=False,
    ) 
    light_id_pass_6_invert: BoolProperty(
        name="Pass 6",
        description="Pass 6",
        default=False,
    ) 
    light_id_pass_7_invert: BoolProperty(
        name="Pass 7",
        description="Pass 7",
        default=False,
    ) 
    light_id_pass_8_invert: BoolProperty(
        name="Pass 8",
        description="Pass 8",
        default=False,
    ) 
    caustic_blur: FloatProperty(
        name="Caustic blur",
        description="Caustic blur for noise reduction",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=1,
        precision=3,
    )
    affect_roughness: FloatProperty(
        name="Affect roughness",
        description="The percentage of roughness affecting subsequent layers' roughness",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.2,
        step=1,
        precision=3,
    )       
    parallelism: IntProperty(
        name="Parallelism",
        description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed",
        min=1, max=4,
        default=4,
    )
    specular_depth: IntProperty(
        name="Specular depth",
        description="The maximum path depth for which specular reflections/refractions are allowed",
        min=1, max=1024,
        default=5,
    )
    glossy_depth: IntProperty(
        name="Glossy depth",
        description="The maximum path depth for which glossy reflections are allowed",
        min=1, max=1024,
        default=2,
    )
    ao_dist: FloatProperty(
        name="AOdist",
        description="Maximum distance for environment ambient occlusion",
        min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
        default=3.0,
        step=1,
        precision=2,
    )
    ao_texture: StringProperty(
        name="AO ambient texture",
        description="Ambient occlusion environment texture, which is used for AO rays. If not specified, the environment will be used instead",
        default="",
        maxlen=512,
    )
    gi_modes = (
        ('0', "None", "", 0),
        # ('1', "Ambient", ""),
        # ('2', "Sample environment", ""),
        ('3', "Ambient occlusion", "", 3),
        ('4', "Diffuse", "", 4),
    )
    gi_mode: EnumProperty(
        name="GImode",
        description="Determines how global illumination is approximated",
        items=gi_modes,
        default='3',
    )
    clay_modes = (
        ('None', "None", "", 0),
        ('Grey', "Grey", "", 1),
        ('Color', "Color", "", 2),
    )
    clay_mode: EnumProperty(
        name="Clay Mode",
        description="The clay mode should be used in rendering",
        items=clay_modes,
        default='None',
    )
    sub_sample_modes = (
        ('No subsampling', "No subsampling", "", 1),
        ('2x2 subsampling', "2x2 subsampling", "", 2),
        ('4x4 subsampling', "4x4 subsampling", "", 4),    
    )    
    subsample_mode: EnumProperty(
        name="Subsample Mode",
        description="The subsampe mode should be used in rendering",
        items=sub_sample_modes,
        default='No subsampling',
    )          
    gi_clamp: FloatProperty(
        name="GI clamp",
        description="GI clamp reducing fireflies",
        min=0.001, soft_min=0.001, max=1000000.0, soft_max=1000000.0,
        default=1000000,
        step=1,
        precision=3,
    )
    diffuse_depth: IntProperty(
        name="Diffuse depth",
        description="The maximum path depth for which diffuse reflections are allowed",
        min=1, max=8,
        default=2,
    )
    max_diffuse_depth: IntProperty(
        name="Max. diffuse depth",
        description="The maximum path depth for which diffuse reflections are allowed",
        min=1, max=2048,
        default=8,
    )
    max_glossy_depth: IntProperty(
        name="Max. glossy depth",
        description="The maximum path depth for which specular reflections/refractions are allowed",
        min=1, max=2048,
        default=24,
    )
    max_scatter_depth: IntProperty(
        name="Max. scatter depth",
        description="The maximum path depth for which scattering is allowed",
        min=1, max=256,
        default=8,
    )                
    parallel_samples: IntProperty(
        name="Parallel samples",
        description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed",
        min=1, max=32,
        default=32,
    )
    max_tile_samples: IntProperty(
        name="Max. tile samples",
        description="The maximum samples we calculate until we switch to a new tile",
        min=1, max=64,
        default=64,
    )
    minimize_net_traffic: BoolProperty(
        name="Minimize net traffic",
        description="If enabled, the work is distributed to the network render slaves in such a way to minimize the amount of data that is sent to the network render master",
        default=True,
    )
    emulate_old_volume_behavior: BoolProperty(
        name="Emulate old volume behavior",
        description="Emulate the behavior of of emission and scattering of version 4.0 and earlier",
        default=False,
    )        
    deep_image: BoolProperty(
        name="Deep image",
        description="Render and save deep image file into output folder after frame render is finished",
        default=False,
    )
    deep_render_passes: BoolProperty(
        name="Deep image passes",
        description="Include render passes in deep pixels",
        default=False,
    )    
    max_depth_samples: IntProperty(
        name="Max. depth samples",
        description="Maximum number of depth samples per pixels",
        min=1, max=32,
        default=8,
    )
    depth_tolerance: FloatProperty(
        name="Depth tolerance",
        description="Depth samples whose relative depth difference falls below the tolerance value are merged together",
        min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
        default=0.05,
        step=1,
        precision=3,
    )
    work_chunk_size: IntProperty(
        name="Work chunk size",
        description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value increases the memory usage on the system, but doesn't affect memory usage on the system and may increase render speed",
        min=1, max=64,
        default=8,
    )
    toon_shadow_ambient: FloatVectorProperty(
        name="Toon shadow ambient",
        description="The ambient modifier of toon shadowing",
        min=0.0, max=1.0,
        default=(0.5, 0.5, 0.5),
        subtype='COLOR',
    )     
    ao_alpha_shadows: BoolProperty(
        name="AO alpha shadows",
        description="Take into account alpha maps when calculating ambient occlusion",
        default=False,
    )
    opacity_threshold: FloatProperty(
        name="Opacity threshold",
        description="Geometry with opacity higher or equal to this value is treated as totally opaque",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
        step=1,
        precision=3,
    )
    exploration: FloatProperty(
        name="Exploration strength",
        description="Effort on investigating good paths",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.7,
        step=10,
        precision=2,
    )
    direct_light_importance: FloatProperty(
        name="Direct light imp.",
        description="Computational effort on direct lighting",
        min=0.01, soft_min=0.01, max=1.0, soft_max=1.0,
        default=0.1,
        step=1,
        precision=2,
    )
    max_rejects: IntProperty(
        name="Max. rejects",
        description="Maximum number of consecutive rejects",
        min=100, max=10000,
        default=500,
    )
    info_channel_types = (
        ('0', "Geometric normals", "", 0),
        ('1', "Shading normals", "", 1),
        ('2', "Position", "", 2),
        ('3', "Z-Depth", "", 3),
        ('4', "Material ID", "", 4),
        ('5', "Textures coordinates", "", 5),
        ('6',"Texture tangent", "", 6),
        ('7', "Wireframe", "", 7),
        ('8', "Smooth normals", "", 8),
        ('9', "Object layer ID", "", 9),
        ('10',"Ambient occlusion", "", 10),
        ('11',"Motion vector", "", 11),
        ('12',"Render layer ID", "", 12),
        ('13',"Render layer Mask", "", 13),
        ('14',"Light pass ID", "", 14),
        ('15',"Tangent normal", "", 15),
        ('16',"Opacity", "", 16),
        ('17',"Baking group ID", "", 17),
        ('18',"Roughness", "", 18),
        ('19',"Index of reflection", "", 19),
        ('20',"Diffuse filter color", "", 20),
        ('21',"Reflection filter color", "", 21),
        ('22',"Refraction filter color", "", 22),
        ('23',"Transmission filter color", "", 23),
        ('24',"Object layer color", "", 24),
    )    
    info_channel_type: EnumProperty(
        name="Info-channel type",
        description="",
        items=info_channel_types,
        default='0',
    )
    zdepth_max: FloatProperty(
        name="Z-Depth max.",
        description="",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=5.0,
        step=100,
        precision=3,
    )
    uv_max: FloatProperty(
        name="UV max.",
        description="UV coordinate value mapped to maximum intensity",
        min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
        default=1.0,
        step=1,
        precision=5,
    )
    sampling_mode: EnumProperty(
        name="Sampling mode",
        description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
            "'Distributed rays':"
            " Enables motion blur and DOF, and also enables pixel filtering.\n"
            "'Non-distributed with pixel filtering':"
            " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
            "'Non-distributed without pixel filtering':"
            " Disables motion blur and DOF, and disables pixel filtering for all render passes"
            " except for render layer mask and ambient occlusion\n",
        items=info_pass_sampling_modes,
        default='0',
    )
    max_speed: FloatProperty(
        name="Max speed",
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
        min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
        default=1.0,
        step=100,
        precision=3,
    )
    bump_normal_mapping: BoolProperty(
        name="Bump and normal mapping",
        description="Take bump and normal mapping into account for shading normal output and wireframe shading",
        default=False,
    )
    wf_bkface_hl: BoolProperty(
        name="Wireframe backface highlighting",
        description="Show faces seen from the backside of the face normal in a different color in wireframe mode",
        default=False,
    )
    path_term_power: FloatProperty(
        name="Path term. power",
        description="Path may get terminated when ray power is less then this value",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.3,
        step=10,
        precision=2,
    )
    coherent_ratio: FloatProperty(
        name="Coherent ratio",
        description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.0,
        step=10,
        precision=2,
    )
    static_noise: BoolProperty(
        name="Static noise",
        description="If enabled, the noise patterns are kept stable between frames",
        default=False,
    )

    progressive: BoolProperty(
        name="Progressive",
        description="Use progressive sampling of lighting",
        default=True,
    )
    preview_pause: BoolProperty(
        name="Pause Preview",
        description="Pause viewport preview",
        default=False,
    )
    preview_active_layer: BoolProperty(
        name="Preview Active Layer",
        description="Preview active render layer in viewport",
        default=False,
    )
    hdr_tonemap_preview_enable: BoolProperty(
        name="Enable HDR tonemapping in Interactive Mode",
        description="Tick to enable Octane HDR tonemapping in interactive preview mode",
        default=True,
    )
    hdr_tonemap_render_enable: BoolProperty(
        name="Enable HDR tonemapping in Render Mode",
        description="Tick to enable Octane HDR tonemapping in render mode",
        default=True,
    )        
    use_preview_setting_for_camera_imager: BoolProperty(
        name="Override",
        description="If enabled, we use this setting in all cases(ignore what is set in octane cameras)",
        default=False,
    )  
    use_preview_post_process_setting: BoolProperty(
        name="Override",
        description="If enabled, we use this setting in all cases(ignore what is set in octane cameras)",
        default=False,
    )  
    adaptive_sampling: BoolProperty(
        name="Adaptive sampling",
        description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image parts",
        default=False,
    )
    adaptive_noise_threshold: FloatProperty(
        name="Noise threshold",
        description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.03,
        step=3,
        precision=4,
    )
    adaptive_expected_exposure: FloatProperty(
        name="Expected exposure",
        description="The expected exposure should be approximately the same value as the exposure in the image or 0 to ignore these settings. Only valid if adaptive sampling is enabled",
        min=0.0, soft_min=0.0, max=10000, soft_max=4096.0,
        default=0.0,
        step=0.1,
        precision=4,
    )
    adaptive_min_samples: IntProperty(
        name="Min. adaptive samples",
        description="Minimum number of samples per pixel until adaptive sampling kicks inunto estimate initial noise level. Higher the value for high quality, but will increase render time. Only valid if adaptive sampling is enabled",
        min=2, soft_min=2, max=1000000, soft_max=1024,
        default=256,
    )
    adaptive_group_pixels = (
        ('1', "None", ""),
        ('2', "2 x 2", ""),
        ('4', "4 x 4", ""),
    )    
    adaptive_group_pixels: EnumProperty(
        name="Group pixels",
        description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not",
        items=adaptive_group_pixels,
        default='2',
    )
    gui_octane_export_ocio_color_space_name: StringProperty(
        name="Color space",
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the same color space as the 'Octane' box",        
        default="",
        update=ocio.update_octane_export_ocio_params,
    )  
    gui_octane_export_ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply",        
        default="",
        update=ocio.update_octane_export_ocio_params,
    ) 
    octane_export_ocio_color_space_name: StringProperty(
        name="Color space",
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the same color space as the 'Octane' box",        
        default="",
    )  
    octane_export_ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply",        
        default="",
    )                                                 
    octane_export_force_use_tone_map: BoolProperty(
        name="Force use tone map",
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB color space",
        default=False,
    )
    octane_export_premultiplied_alpha: BoolProperty(
        name="Premultiplied Aplha",
        description="Premultiplied Aplha",
        default=False,
    )    
    octane_export_dwa_compression_level: IntProperty(
        name="DWA compression level",
        description="DWA compression level",
        min=0, max=2000, 
        default=45,
    )    
    white_light_spectrum_modes = (
        ('D65', "D65", "D65", 1),
        ('Legacy/flat', "Legacy/flat", "Legacy/flat", 0),
    )
    white_light_spectrum: EnumProperty(
        name="White light spectrum",
        description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, black body emitters). This determines the spectrum that will produce white (before white balance) in the final image. Use D65 to adapt to a reasonable daylight 'white' color. Use Legacy/flat to preserve the appearance of old projects (spectral emitters will appear rather blue)",
        items=white_light_spectrum_modes,
        default='D65',
    )    
    use_old_color_pipeline: BoolProperty(
        name="Use old color pipeline",
        description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)",
        default=False,
    )     
    need_upgrade_octane_output_tag: BoolProperty(
        name="Need to Upgrade Octane Output Tag",
        description="",
        default=True,
    )
    photon_depth: IntProperty(
        name="Photon depth",
        description="The maximum path depth for photons",
        min=2, max=16, 
        default=8,
    )
    accurate_colors: BoolProperty(
        name="Accurate colors",
        description="If enabled colors will be more accurate but noise will converge more slowly",
        default=False,
    )
    photon_gather_radius: FloatProperty(
        name="Photon gathering radius",
        description="The maximum radius where photons can contribute",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.01,
        step=3,
        precision=4,
    )
    photon_gather_multiplier: FloatProperty(
        name="Photon count multiplier",
        description="Approximate ratio between photons and camera rays",
        min=0.25, soft_min=0.25, max=8.0, soft_max=8.0,
        default=4.0,
        step=3,
        precision=2,
    )        
    photon_gather_samples: IntProperty(
        name="Photon gather samples",
        description="Maximal amount of photon gather samples per pixel between photon tracing passes. This is similar to max. tile samples, but it also affects the quality of caustics rendered. Higher values give more samples per second at the expense of caustic quality",
        min=1, max=64, 
        default=2,
    )    
    exploration_strength: FloatProperty(
        name="Exploration strength",
        description="The higher this value, the more the photon sampling is influenced by which photons are actually gathered",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.8,
        step=3,
        precision=3,
    )

    #LEGACY COMPATIBILITY
    hdr_tonemap_enable: BoolProperty(
        name="Tonemapped HDR",
        description="",
        default=False,
    )    

    @classmethod
    def register(cls):
        bpy.types.Scene.octane = PointerProperty(
            name="Octane Render Settings",
            description="Octane render settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        pass


_CLASSES = [
    KernelNodeGraphPropertyGroup,
    RenderAOVNodeGraphPropertyGroup,
    CompositeNodeGraphPropertyGroup,
    OctaneOCIOConfigName,
    OctaneAovOutputGroupNode,
    OctaneAovOutputGroupCollection,    
    OctaneBakingLayerTransform,
    OctaneBakingLayerTransformCollection,    
    OctaneAnimationSettings,
    OctaneGlobalRenderLayer,
    OctaneRenderLayer,
    OctaneRenderSettings,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)