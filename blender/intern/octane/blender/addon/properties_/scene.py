# <pep8 compliant>

from bl_operators.presets import AddPresetBase
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, \
    FloatVectorProperty, BoolVectorProperty, CollectionProperty
from bpy.types import Operator

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.render_settings.animation_settings import OctaneAnimationSettingsShutterAlignment
from octane.nodes.render_settings.render_layer import OctaneRenderLayerMode
from octane.properties_.common import OctanePropertyGroup
from octane.utils import consts, ocio, utility

rotation_orders = (
    ('0', "XYZ", ""),
    ('1', "XZY", ""),
    ('2', "YXZ", ""),
    ('3', "YZX", ""),
    ('4', "ZXY", ""),
    ('5', "ZYX", ""),
)

info_pass_sampling_modes = (
    ('0', "Distributed rays", "", 0),
    ('1', "Non-distributed with pixel filtering", "", 1),
    ('2', "Non-distributed without pixel filtering", "", 2),
)

cryptomatte_pass_channel_modes = (
    ('2', "2", "", 2),
    ('4', "4", "", 4),
    ('6', "6", "", 6),
    ('8', "8", "", 8),
    ('10', "10", "", 10),
)

octane_export_with_deep_image_modes = (
    ("SEPARATE_IMAGE_FILES", "Export separate image files", "Export separate image files",
     consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_SEPARATE),
    ("MULTILAYER_EXR", "Export multilayer EXR", "Export multilayer EXR",
     consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_MULTILAYER),
    ("DEEP_EXR", "Export deep EXR", "Export deep EXR",
     consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_DEEP_EXR),
)
octane_export_without_deep_image_modes = (
    ("SEPARATE_IMAGE_FILES", "Export separate image files", "Export separate image files",
     consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_SEPARATE),
    ("MULTILAYER_EXR", "Export multilayer EXR", "Export multilayer EXR",
     consts.ExportRenderPassMode.EXPORT_RENDER_PASS_MODE_MULTILAYER),
)

octane_shading_type_modes = (
    ("WIREFRAME", "WIREFRAME", "Toggle wireframe shading", "SHADING_WIRE", 2),
    ("SOLID", "SOLID", "Toggle solid shading", "SHADING_SOLID", 3),
    ("RENDERED", "RENDERED", "Toggle rendered shading", "SHADING_RENDERED", 6),
)


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

    def update_nodes(self, _context):
        for i in range(0, len(self.composite_node_trees)):
            self.composite_node_trees.remove(0)
        if bpy.data.node_groups:
            for node_tree in bpy.data.node_groups.values():
                if getattr(node_tree, "bl_idname", "") == consts.OctaneNodeTreeIDName.COMPOSITE:
                    self.composite_node_trees.add()
                    self.composite_node_trees[-1].name = node_tree.name
        for i in range(0, len(self.aov_output_group_nodes)):
            self.aov_output_group_nodes.remove(0)
        if bpy.data.node_groups:
            for node_tree in bpy.data.node_groups.values():
                if getattr(node_tree, "bl_idname", "") != consts.OctaneNodeTreeIDName.COMPOSITE:
                    continue
                if node_tree.name != self.composite_node_tree:
                    continue
                for node in node_tree.nodes.values():
                    if node.bl_idname == "ShaderNodeOctAovOutputGroup":
                        self.aov_output_group_nodes.add()
                        self.aov_output_group_nodes[-1].name = node.name


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


def sync_baking_transform(_self=None, _context=None):
    scene = bpy.context.scene
    oct_scene = scene.octane
    baking_layer_settings = oct_scene.baking_layer_settings
    oct_cam = bpy.data.cameras['Camera'].octane
    if baking_layer_settings.get_baking_layer_by_idx(oct_cam.baking_group_id) is None:
        baking_layer_settings.add_new_baking_layer(oct_cam.baking_group_id)
    for transform in baking_layer_settings.baking_layer_transform_collections.values():
        if transform.id == oct_cam.baking_group_id:
            oct_cam.baking_uvw_translation = transform.translation
            oct_cam.baking_uvw_rotation = transform.rotation
            oct_cam.baking_uvw_scale = transform.scale
            oct_cam.baking_uvw_rotation_order = transform.rotation_order


class OctaneBakingLayerTransformCollection(bpy.types.PropertyGroup):
    baking_layer_transform_collections: CollectionProperty(type=OctaneBakingLayerTransform)

    def update_cur_baking_layer_id(self, _context):
        # make sure it is initialized
        if not self._delay_init():
            return
        if self.get_baking_layer_by_idx(self.cur_baking_layer_id) is None:
            self.add_new_baking_layer(self.cur_baking_layer_id)
        # self._debug_show_all_baking_layer_info()
        cur_baking_transform = self.get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            self['cur_baking_layer_id'] = cur_baking_transform.id
            self['cur_baking_layer_translation'] = cur_baking_transform.translation
            self['cur_baking_layer_rotation'] = cur_baking_transform.rotation
            self['cur_baking_layer_scale'] = cur_baking_transform.scale
            self['cur_baking_layer_rotation_order'] = cur_baking_transform.rotation_order
        sync_baking_transform()

    # init default baking layer
    cur_baking_layer_id: IntProperty(
        name="Baking Layer ID",
        description="ID of the baking layer",
        update=update_cur_baking_layer_id,
        min=1, max=65535,
        default=1,
    )

    def update_cur_baking_layer_transform(self, _context):
        # make sure it is initialized
        if not self._delay_init():
            return
        cur_baking_transform = self.get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            cur_baking_transform.translation = self['cur_baking_layer_translation']
            cur_baking_transform.rotation = self['cur_baking_layer_rotation']
            cur_baking_transform.scale = self['cur_baking_layer_scale']
            cur_baking_transform.rotation_order = str(self['cur_baking_layer_rotation_order'])
        sync_baking_transform()

    cur_baking_layer_translation: FloatVectorProperty(
        name="Translation",
        description="Translation that affects the way the UVs from that object layer are projected into the UV space "
                    "when rendered using the baking camera",
        update=update_cur_baking_layer_transform,
        subtype='TRANSLATION',
    )
    cur_baking_layer_rotation: FloatVectorProperty(
        name="Rotation",
        description="Rotation that affects the way the UVs from that object layer are projected into the UV space "
                    "when rendered using the baking camera",
        update=update_cur_baking_layer_transform,
        subtype='EULER',
    )
    cur_baking_layer_scale: FloatVectorProperty(
        name="Scale",
        description="Scale that affects the way the UVs from that object layer are projected into the UV space when "
                    "rendered using the baking camera",
        update=update_cur_baking_layer_transform,
        subtype='XYZ',
        default=(1, 1, 1)
    )
    cur_baking_layer_rotation_order: EnumProperty(
        name="Rotation order",
        description="Rotation order that affects the way the UVs from that object layer are projected into the UV "
                    "space when rendered using the baking camera",
        update=update_cur_baking_layer_transform,
        items=rotation_orders,
        default='2',
    )

    def init(self):
        if not len(self.baking_layer_transform_collections):
            next_new_baking_layer = self.baking_layer_transform_collections.add()
            next_new_baking_layer.id = 1

    def add_new_baking_layer(self, idx):
        next_new_baking_layer = self.baking_layer_transform_collections.add()
        next_new_baking_layer.id = idx

    def get_baking_layer_by_idx(self, idx):
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
        if self.get_baking_layer_by_idx(1) is None:
            self.add_new_baking_layer(1)
            return False
        if (not self.__contains__('cur_baking_layer_translation')
                or not self.__contains__('cur_baking_layer_rotation')
                or not self.__contains__('cur_baking_layer_scale')
                or not self.__contains__('cur_baking_layer_rotation_order')):
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

    def update_scene(self, context):
        context.scene.update_tag()
        bpy.app.timers.register(self.update_post, first_interval=0.05)

    def update_post(self):
        bpy.context.scene.update_tag()

    node_tree: PointerProperty(
        name="Kernel Node Graph",
        description="Select the kernel node graph(can be created in the 'Kernel Editor'",
        type=bpy.types.NodeTree,
        poll=poll_kernel_tree,
        update=update_scene,
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
        description="Select the Octane composite node graph(can be created in the 'Octane Composite Editor'",
        type=bpy.types.NodeTree,
        poll=poll_composite_node_tree,
    )


class OctaneAnimationSettingsPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {consts.NodeType.NT_ANIMATION_SETTINGS: ["mb_direction", ]}
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
    emulate_old_motion_blur_behavior: BoolProperty(
        name="Old motion blur behavior",
        description="Emulate the behavior of of Octane Blender motion blur of version 27.8",
        default=False,
    )
    clamp_motion_blur_data_source: BoolProperty(
        name="Auto Clamp Mode",
        description="Clamp motion blur data source within the start-frame and end-frame",
        default=True,
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
        row = layout.row()
        row.prop(self, "emulate_old_motion_blur_behavior")
        row = layout.row()
        row.prop(self, "clamp_motion_blur_data_source")

    def sync_custom_data(self, octane_node, scene, region, v3d, rv3d, session_type):
        if session_type == consts.SessionType.EXPORT:
            shutter_time = self.shutter_time / 100.0
        else:
            if self.emulate_old_motion_blur_behavior:
                shutter_time = scene.render.fps * self.shutter_time / 100.0
            else:
                shutter_time = scene.render.fps * min(1.0, self.shutter_time / 100.0)
        octane_node.set_pin_id(consts.PinID.P_SHUTTER_TIME, False, "", shutter_time)
        # octane_node.set_pin_id(consts.PinID.P_SHUTTER_TIME, False, "", self.shutter_time / 100.0)
        octane_node.set_pin_id(consts.PinID.P_SUBFRAME_START, False, "", self.subframe_start / 100.0)
        octane_node.set_pin_id(consts.PinID.P_SUBFRAME_END, False, "", self.subframe_end / 100.0)

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        utility.cast_legacy_enum_property(self, "mb_direction", OctaneAnimationSettingsShutterAlignment.items,
                                          legacy_data, "mb_direction")
        utility.sync_legacy_property(self, "shutter_time", legacy_data, "shutter_time")
        utility.sync_legacy_property(self, "subframe_start", legacy_data, "subframe_start")
        utility.sync_legacy_property(self, "subframe_end", legacy_data, "subframe_end")


class OctaneGlobalRenderLayerPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {
        consts.NodeType.NT_RENDER_LAYER: ["layers_enable", "layers_current", "layers_invert", "layers_mode", ]}
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
        description="All the non-active render layers become the active render layer and the active render layer "
                    "becomes inactive",
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
                    "will be made invisible. But side effects(shadows, reflections...)will be recorded in the render "
                    "layer passes\n"
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


class OctaneRenderLayerPropertyGroup(OctanePropertyGroup):
    PROPERTY_CONFIGS = {
        consts.NodeType.NT_RENDER_LAYER: ["layers_enable", "layers_current", "layers_invert", "layers_mode", ],
        consts.NodeType.NT_RENDER_PASSES: [
            "pass_raw",
            "use_pass_beauty", "use_pass_emitters", "use_pass_env",
            "use_pass_denoise_albedo", "use_pass_denoise_normal",
            "use_pass_diff", "use_pass_diff_dir", "use_pass_diff_indir", "use_pass_diff_filter",
            "use_pass_reflect", "use_pass_reflect_dir", "use_pass_reflect_indir", "use_pass_reflect_filter",
            "use_pass_refract", "use_pass_refract_filter",
            "use_pass_transm", "use_pass_transm_filter",
            "use_pass_sss", "use_pass_shadow",
            "use_pass_irradiance", "use_pass_light_dir", "use_pass_volume", "use_pass_vol_mask",
            "use_pass_vol_emission", "use_pass_vol_z_front", "use_pass_vol_z_back", "use_pass_noise",
            "use_pass_denoise_beauty", "use_pass_denoise_diff_dir", "use_pass_denoise_diff_indir",
            "use_pass_denoise_reflect_dir", "use_pass_denoise_reflect_indir", "use_pass_denoise_emission",
            "use_pass_denoise_remainder", "use_pass_denoise_vol", "use_pass_denoise_vol_emission",
            "use_pass_postprocess", "use_pass_postfxmedia", "pass_pp_env",
            "use_pass_layer_shadows", "use_pass_layer_black_shadow", "use_pass_layer_reflections",
            "use_pass_ambient_light", "use_pass_ambient_light_dir", "use_pass_ambient_light_indir",
            "use_pass_sunlight", "use_pass_sunlight_dir", "use_pass_sunlight_indir",
            "use_pass_light_pass_1", "use_pass_light_dir_pass_1", "use_pass_light_indir_pass_1",
            "use_pass_light_pass_2", "use_pass_light_dir_pass_2", "use_pass_light_indir_pass_2",
            "use_pass_light_pass_3", "use_pass_light_dir_pass_3", "use_pass_light_indir_pass_3",
            "use_pass_light_pass_4", "use_pass_light_dir_pass_4", "use_pass_light_indir_pass_4",
            "use_pass_light_pass_5", "use_pass_light_dir_pass_5", "use_pass_light_indir_pass_5",
            "use_pass_light_pass_6", "use_pass_light_dir_pass_6", "use_pass_light_indir_pass_6",
            "use_pass_light_pass_7", "use_pass_light_dir_pass_7", "use_pass_light_indir_pass_7",
            "use_pass_light_pass_8", "use_pass_light_dir_pass_8", "use_pass_light_indir_pass_8",
            "use_pass_light_pass_9", "use_pass_light_dir_pass_9", "use_pass_light_indir_pass_9",
            "use_pass_light_pass_10", "use_pass_light_dir_pass_10", "use_pass_light_indir_pass_10",
            "use_pass_light_pass_11", "use_pass_light_dir_pass_11", "use_pass_light_indir_pass_11",
            "use_pass_light_pass_12", "use_pass_light_dir_pass_12", "use_pass_light_indir_pass_12",
            "use_pass_light_pass_13", "use_pass_light_dir_pass_13", "use_pass_light_indir_pass_13",
            "use_pass_light_pass_14", "use_pass_light_dir_pass_14", "use_pass_light_indir_pass_14",
            "use_pass_light_pass_15", "use_pass_light_dir_pass_15", "use_pass_light_indir_pass_15",
            "use_pass_light_pass_16", "use_pass_light_dir_pass_16", "use_pass_light_indir_pass_16",
            "use_pass_light_pass_17", "use_pass_light_dir_pass_17", "use_pass_light_indir_pass_17",
            "use_pass_light_pass_18", "use_pass_light_dir_pass_18", "use_pass_light_indir_pass_18",
            "use_pass_light_pass_19", "use_pass_light_dir_pass_19", "use_pass_light_indir_pass_19",
            "use_pass_light_pass_20", "use_pass_light_dir_pass_20", "use_pass_light_indir_pass_20",
            "cryptomatte_pass_channels", "cryptomatte_seed_factor",
            "use_pass_crypto_instance_id", "use_pass_crypto_mat_node_name", "use_pass_crypto_mat_node",
            "use_pass_crypto_mat_pin_node",
            "use_pass_crypto_obj_node_name", "use_pass_crypto_obj_node", "use_pass_crypto_obj_pin_node",
            "use_pass_crypto_render_layer", "use_pass_crypto_geometry_node_name", "use_pass_crypto_user_instance_id",
            "info_pass_max_samples", "info_pass_sampling_mode",
            "info_pass_bump", "info_pass_opacity_threshold",
            "use_pass_info_geo_normal", "use_pass_info_smooth_normal", "use_pass_info_shading_normal",
            "use_pass_info_tangent_normal",
            "use_pass_info_z_depth", "info_pass_z_depth_max",
            "use_pass_info_position",
            "use_pass_info_uv", "info_pass_uv_max", "info_pass_uv_coordinate_selection",
            "use_pass_info_tex_tangent",
            "use_pass_info_motion_vector", "info_pass_max_speed",
            "use_pass_info_mat_id", "use_pass_info_obj_id", "use_pass_info_obj_layer_color",
            "use_pass_info_baking_group_id", "use_pass_info_light_pass_id",
            "use_pass_info_render_layer_id", "use_pass_info_render_layer_mask", "use_pass_info_wireframe",
            "use_pass_info_ao", "info_pass_ao_distance", "info_pass_alpha_shadows",
            "use_pass_mat_opacity", "use_pass_mat_roughness", "use_pass_mat_ior",
            "use_pass_mat_diff_filter_info", "use_pass_mat_reflect_filter_info", "use_pass_mat_refract_filter_info",
            "use_pass_mat_transm_filter_info",
        ]
    }
    PROPERTY_NAME_TO_PIN_SYMBOL_MAP = {
        # NT_RENDER_LAYER
        "layers_enable": "enabled",
        "layers_current": "layerId",
        "layers_invert": "invert",
        "layers_mode": "mode",
        # NT_RENDER_PASSES
        "pass_raw": "renderPassesRaw",
        "use_pass_beauty": "",
        "use_pass_emitters": "renderPassEmit",
        "use_pass_env": "renderPassEnvironment",
        "use_pass_denoise_albedo": "renderPassDenoiseAlbedo",
        "use_pass_denoise_normal": "renderPassDenoiseNormal",
        "use_pass_diff": "renderPassDiffuse",
        "use_pass_diff_dir": "renderPassDiffuseDirect",
        "use_pass_diff_indir": "renderPassDiffuseIndirect",
        "use_pass_diff_filter": "renderPassDiffuseFilter",
        "use_pass_reflect": "renderPassReflection",
        "use_pass_reflect_dir": "renderPassReflectionDirect",
        "use_pass_reflect_indir": "renderPassReflectionIndirect",
        "use_pass_reflect_filter": "renderPassReflectionFilter",
        "use_pass_refract": "renderPassRefraction",
        "use_pass_refract_filter": "renderPassRefractionFilter",
        "use_pass_transm": "renderPassTransmission",
        "use_pass_transm_filter": "renderPassTransmissionFilter",
        "use_pass_sss": "renderPassSSS",
        "use_pass_shadow": "renderPassShadow",
        "use_pass_irradiance": "renderPassIrradiance",
        "use_pass_light_dir": "renderPassLightDirection",
        "use_pass_volume": "renderPassVolume",
        "use_pass_vol_mask": "renderPassVolumeMask",
        "use_pass_vol_emission": "renderPassVolumeEmission",
        "use_pass_vol_z_front": "renderPassVolumeZDepthFront",
        "use_pass_vol_z_back": "renderPassVolumeZDepthBack",
        "use_pass_noise": "renderPassNoise",
        "use_pass_denoise_beauty": "",
        "use_pass_denoise_diff_dir": "renderPassDiffuseDirectDenoiserOutput",
        "use_pass_denoise_diff_indir": "renderPassDiffuseIndirectDenoiserOutput",
        "use_pass_denoise_reflect_dir": "renderPassReflectionDirectDenoiserOutput",
        "use_pass_denoise_reflect_indir": "renderPassReflectionIndirectDenoiserOutput",
        "use_pass_denoise_emission": "renderPassEmissionDenoiserOutput",
        "use_pass_denoise_remainder": "renderPassRemainderDenoiserOutput",
        "use_pass_denoise_vol": "renderPassVolumeDenoiserOutput",
        "use_pass_denoise_vol_emission": "renderPassVolumeEmissionDenoiserOutput",
        "use_pass_postprocess": "renderPassPostProcessing",
        "use_pass_postfxmedia": "renderPassPostFxMedia",
        "pass_pp_env": "postProcEnvironment",
        "use_pass_layer_shadows": "renderPassLayerShadows",
        "use_pass_layer_black_shadow": "renderPassLayerBlackShadows",
        "use_pass_layer_reflections": "renderPassLayerReflections",
        "use_pass_ambient_light": "renderPassAmbientLight",
        "use_pass_ambient_light_dir": "renderPassAmbientLightDirect",
        "use_pass_ambient_light_indir": "renderPassAmbientLightIndirect",
        "use_pass_sunlight": "renderPassSunLight",
        "use_pass_sunlight_dir": "renderPassSunLightDirect",
        "use_pass_sunlight_indir": "renderPassSunLightIndirect",
        "use_pass_light_pass_1": "renderPassLight1",
        "use_pass_light_dir_pass_1": "renderPassLight1Direct",
        "use_pass_light_indir_pass_1": "renderPassLight1Indirect",
        "use_pass_light_pass_2": "renderPassLight2",
        "use_pass_light_dir_pass_2": "renderPassLight2Direct",
        "use_pass_light_indir_pass_2": "renderPassLight2Indirect",
        "use_pass_light_pass_3": "renderPassLight3",
        "use_pass_light_dir_pass_3": "renderPassLight3Direct",
        "use_pass_light_indir_pass_3": "renderPassLight3Indirect",
        "use_pass_light_pass_4": "renderPassLight4",
        "use_pass_light_dir_pass_4": "renderPassLight4Direct",
        "use_pass_light_indir_pass_4": "renderPassLight4Indirect",
        "use_pass_light_pass_5": "renderPassLight5",
        "use_pass_light_dir_pass_5": "renderPassLight5Direct",
        "use_pass_light_indir_pass_5": "renderPassLight5Indirect",
        "use_pass_light_pass_6": "renderPassLight6",
        "use_pass_light_dir_pass_6": "renderPassLight6Direct",
        "use_pass_light_indir_pass_6": "renderPassLight6Indirect",
        "use_pass_light_pass_7": "renderPassLight7",
        "use_pass_light_dir_pass_7": "renderPassLight7Direct",
        "use_pass_light_indir_pass_7": "renderPassLight7Indirect",
        "use_pass_light_pass_8": "renderPassLight8",
        "use_pass_light_dir_pass_8": "renderPassLight8Direct",
        "use_pass_light_indir_pass_8": "renderPassLight8Indirect",
        "use_pass_light_pass_9": "renderPassLight9",
        "use_pass_light_dir_pass_9": "renderPassLight9Direct",
        "use_pass_light_indir_pass_9": "renderPassLight9Indirect",
        "use_pass_light_pass_10": "renderPassLight10",
        "use_pass_light_dir_pass_10": "renderPassLight10Direct",
        "use_pass_light_indir_pass_10": "renderPassLight10Indirect",
        "use_pass_light_pass_11": "renderPassLight11",
        "use_pass_light_dir_pass_11": "renderPassLight11Direct",
        "use_pass_light_indir_pass_11": "renderPassLight11Indirect",
        "use_pass_light_pass_12": "renderPassLight12",
        "use_pass_light_dir_pass_12": "renderPassLight12Direct",
        "use_pass_light_indir_pass_12": "renderPassLight12Indirect",
        "use_pass_light_pass_13": "renderPassLight13",
        "use_pass_light_dir_pass_13": "renderPassLight13Direct",
        "use_pass_light_indir_pass_13": "renderPassLight13Indirect",
        "use_pass_light_pass_14": "renderPassLight14",
        "use_pass_light_dir_pass_14": "renderPassLight14Direct",
        "use_pass_light_indir_pass_14": "renderPassLight14Indirect",
        "use_pass_light_pass_15": "renderPassLight15",
        "use_pass_light_dir_pass_15": "renderPassLight15Direct",
        "use_pass_light_indir_pass_15": "renderPassLight15Indirect",
        "use_pass_light_pass_16": "renderPassLight16",
        "use_pass_light_dir_pass_16": "renderPassLight16Direct",
        "use_pass_light_indir_pass_16": "renderPassLight16Indirect",
        "use_pass_light_pass_17": "renderPassLight17",
        "use_pass_light_dir_pass_17": "renderPassLight17Direct",
        "use_pass_light_indir_pass_17": "renderPassLight17Indirect",
        "use_pass_light_pass_18": "renderPassLight18",
        "use_pass_light_dir_pass_18": "renderPassLight18Direct",
        "use_pass_light_indir_pass_18": "renderPassLight18Indirect",
        "use_pass_light_pass_19": "renderPassLight19",
        "use_pass_light_dir_pass_19": "renderPassLight19Direct",
        "use_pass_light_indir_pass_19": "renderPassLight19Indirect",
        "use_pass_light_pass_20": "renderPassLight20",
        "use_pass_light_dir_pass_20": "renderPassLight20Direct",
        "use_pass_light_indir_pass_20": "renderPassLight20Indirect",
        "cryptomatte_pass_channels": "renderPassCryptomatteCount",
        "cryptomatte_seed_factor": "renderPassCryptomatteSeedFactor",
        "use_pass_crypto_instance_id": "renderPassCryptomatteInstance",
        "use_pass_crypto_mat_node_name": "renderPassCryptomatteMaterialNodeName",
        "use_pass_crypto_mat_node": "renderPassCryptomatteMaterialNode",
        "use_pass_crypto_mat_pin_node": "renderPassCryptomatteMaterialPinName",
        "use_pass_crypto_obj_node_name": "renderPassCryptomatteObjectNodeName",
        "use_pass_crypto_obj_node": "renderPassCryptomatteObjectNode",
        "use_pass_crypto_obj_pin_node": "renderPassCryptomatteObjectPinName",
        "use_pass_crypto_render_layer": "renderPassCryptomatteRenderLayer",
        "use_pass_crypto_geometry_node_name": "renderPassCryptomatteGeometryNodeName",
        "use_pass_crypto_user_instance_id": "renderPassCryptomatteUserInstance",
        "info_pass_max_samples": "renderPassInfoMaxSamples",
        "info_pass_sampling_mode": "samplingMode",
        "info_pass_bump": "bump",
        "info_pass_opacity_threshold": "opacity",
        "use_pass_info_geo_normal": "renderPassGeometricNormal",
        "use_pass_info_smooth_normal": "renderPassVertexNormal",
        "use_pass_info_shading_normal": "renderPassShadingNormal",
        "use_pass_info_tangent_normal": "renderPassTangentNormal",
        "use_pass_info_z_depth": "renderPassZDepth",
        "info_pass_z_depth_max": "Z_depth_max",
        "info_pass_z_depth_environment": "environmentDepth",
        "use_pass_info_position": "renderPassPosition",
        "use_pass_info_uv": "renderPassUvCoord",
        "info_pass_uv_max": "UV_max",
        "info_pass_uv_coordinate_selection": "uvSet",
        "use_pass_info_tex_tangent": "renderPassTangentU",
        "use_pass_info_motion_vector": "renderPassMotionVector",
        "info_pass_max_speed": "maxSpeed",
        "use_pass_info_mat_id": "renderPassMaterialId",
        "use_pass_info_obj_id": "renderPassObjectId",
        "use_pass_info_obj_layer_color": "renderPassObjectLayerColor",
        "use_pass_info_baking_group_id": "renderPassBakingGroupId",
        "use_pass_info_light_pass_id": "renderPassLightPassId",
        "use_pass_info_render_layer_id": "renderPassRenderLayerId",
        "use_pass_info_render_layer_mask": "renderPassRenderLayerMask",
        "use_pass_info_wireframe": "renderPassWireframe",
        "shading_enabled": "shadingEnabled",
        "highlight_backfaces": "highlightBackfaces",
        "use_pass_info_ao": "renderPassAmbientOcclusion",
        "info_pass_ao_distance": "aodist",
        "info_pass_alpha_shadows": "aoAlphaShadows",
        "use_pass_mat_opacity": "renderPassOpacity",
        "use_pass_mat_roughness": "renderPassRoughness",
        "use_pass_mat_ior": "renderPassIor",
        "use_pass_mat_diff_filter_info": "renderPassDiffuseFilterInfo",
        "use_pass_mat_reflect_filter_info": "renderPassReflectionFilterInfo",
        "use_pass_mat_refract_filter_info": "renderPassRefractionFilterInfo",
        "use_pass_mat_transm_filter_info": "renderPassTransmissionFilterInfo",
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
        description="All the non-active render layers become the active render layer and the active render layer "
                    "becomes inactive",
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
                    "will be made invisible. But side effects(shadows, reflections...)will be recorded in the render "
                    "layer passes\n"
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
    aov_out_number: IntProperty(
        name="AOV Outputs Number",
        description="Number of AOV outputs",
        min=0, max=16,
        default=0,
    )
    use_pass_beauty: BoolProperty(
        name="Beauty",
        description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit "
                    "by the camera ray",
        default=False,
    )
    use_pass_emitters: BoolProperty(
        name="Emitters",
        description="Contains all samples where the camera ray hits an emitter",
        default=False,
    )
    use_pass_env: BoolProperty(
        name="Environment",
        description="Contains the environment of the scene",
        default=False,
    )
    use_pass_denoise_albedo: BoolProperty(
        name="DenoiseAlbedo",
        description="Records the albedo values for the first bounce of the camera path, but also of subsequent "
                    "bounces if the first bounces are all specular",
        default=False,
    )
    use_pass_denoise_normal: BoolProperty(
        name="DenoiseNormal",
        description="Records the normal values for the first bounce of the camera path, but also of subsequent "
                    "bounces if the first bounces are all specular",
        default=False,
    )
    use_pass_diff: BoolProperty(
        name="Diff",
        description="Contains all samples where a diffuse material is lit either directly or indirectly",
        default=False,
    )
    use_pass_diff_dir: BoolProperty(
        name="DiffDir",
        description="Contains all samples where a diffuse material is directly lit",
        default=False,
    )
    use_pass_diff_indir: BoolProperty(
        name="DiffIndir",
        description="Contains all samples where a diffuse material is indirectly lit (GI)",
        default=False,
    )
    use_pass_diff_filter: BoolProperty(
        name="DiffFilter",
        description="The diffuse texture color of the diffuse and glossy material",
        default=False,
    )
    use_pass_reflect: BoolProperty(
        name="Reflect",
        description="Contains all samples where either direct or indirect light is reflected.directly or indirectly",
        default=False,
    )
    use_pass_reflect_dir: BoolProperty(
        name="ReflectDir",
        description="Contains all samples where direct light is reflected",
        default=False,
    )
    use_pass_reflect_indir: BoolProperty(
        name="ReflectIndir",
        description="Contains all samples where indirect light is reflected",
        default=False,
    )
    use_pass_reflect_filter: BoolProperty(
        name="ReflectFilter",
        description="The reflection texture color of the specular and glossy material",
        default=False,
    )
    use_pass_refract: BoolProperty(
        name="Refract",
        description="Contains all samples where the camera ray was refracted "
                    "by a specular material on the first bounce",
        default=False,
    )
    use_pass_refract_filter: BoolProperty(
        name="RefractFilter",
        description="The refraction texture color of the specular material",
        default=False,
    )
    use_pass_transm: BoolProperty(
        name="Transm",
        description="Contains all samples where the camera ray is transmitted by a diffuse material "
                    "on the first bounce",
        default=False,
    )
    use_pass_transm_filter: BoolProperty(
        name="TransmFilter",
        description="The transmission texture color of the diffuse material",
        default=False,
    )
    use_pass_sss: BoolProperty(
        name="SSS",
        description="Contains all samples that scattered in a volume visible from the camera",
        default=False,
    )
    use_pass_shadow: BoolProperty(
        name="Shadow",
        description="Contains all direct light shadows that are calculated on the first path bounce. "
                    "This includes sun light, but excludes sky light or texture environment if importance sampling is "
                    "disabled or the texture environment doesn't consist of an image",
        default=False,
    )
    use_pass_layer_shadows: BoolProperty(
        name="LayerShadows",
        description="Contains shadows cast by objects in the active render layer on objects in the other render "
                    "layers. Combines black shadows and colored shadows in a single image",
        default=False,
    )
    use_pass_layer_black_shadow: BoolProperty(
        name="LayerBlackShadow",
        description="Contains shadows cast by opaque objects in the active render layer on objects in the other "
                    "render layers. NOTE: this render pass doesn't work if the alpha channel is disabled",
        default=False,
    )
    use_pass_layer_reflections: BoolProperty(
        name="LayerReflections",
        description="Contains light reflected by the objects in the active layer on the objects "
                    "in all the other layers",
        default=False,
    )
    use_pass_irradiance: BoolProperty(
        name="Irradiance",
        description="Contains the irradiance on the surface",
        default=False,
    )
    use_pass_light_dir: BoolProperty(
        name="LightDir",
        description="Estimates the dominant direction from where most of the light is coming",
        default=False,
    )
    use_pass_volume: BoolProperty(
        name="Volume",
        description="Contains all samples that scattered in a volume",
        default=False,
    )
    use_pass_vol_mask: BoolProperty(
        name="VolMask",
        description="Contains absorption color and the contribution amount of a volume sample. This is a "
                    "multiplication pass, so to composite volume passes you should be doing something like "
                    "allOtherBeautyPasses * volumeMask + volume + volumeEmission",
        default=False,
    )
    use_pass_vol_emission: BoolProperty(
        name="VolEmission",
        description="Contains all samples where the camera ray hit a volume emitter",
        default=False,
    )
    use_pass_vol_z_front: BoolProperty(
        name="VolZFront",
        description="Contains the front depth of all volume samples",
        default=False,
    )
    use_pass_vol_z_back: BoolProperty(
        name="VolZBack",
        description="Contains the back depth of all volume samples",
        default=False,
    )
    use_pass_noise: BoolProperty(
        name="Noise",
        description="Contains the noise estimate value. Green color if the noise estimate is lesser than the "
                    "threshold. Will be black if adaptive sampling is disabled",
        default=False,
    )
    use_pass_denoise_beauty: BoolProperty(
        name="DenoiserBeauty",
        description="",
        default=False,
    )
    use_pass_denoise_diff_dir: BoolProperty(
        name="DenoiserDiffDir",
        description="Contains the denoised result of diffuse direct render passes",
        default=False,
    )
    use_pass_denoise_diff_indir: BoolProperty(
        name="DenoiserDiffIndir",
        description="Contains the denoised result of diffuse indirect render pass",
        default=False,
    )
    use_pass_denoise_reflect_dir: BoolProperty(
        name="DenoiserReflectDir",
        description="Contains the denoised result of reflection direct render pass",
        default=False,
    )
    use_pass_denoise_reflect_indir: BoolProperty(
        name="DenoiserReflectIndir",
        description="Contains the denoised result of reflection indirect render pass",
        default=False,
    )
    use_pass_denoise_emission: BoolProperty(
        name="DenoiserEmission",
        description="Contains the denoised result of emission render pass",
        default=False,
    )
    use_pass_denoise_remainder: BoolProperty(
        name="DenoiserRemainder",
        description="Contains the denoised result of transmission and subsurface render passes",
        default=False,
    )
    use_pass_denoise_vol: BoolProperty(
        name="DenoiserVolume",
        description="Contains the denoised result of volume render pass",
        default=False,
    )
    use_pass_denoise_vol_emission: BoolProperty(
        name="DenoiserVolumeEmission",
        description="Contains the denoised result of volume emission render pass",
        default=False,
    )
    use_pass_postprocess: BoolProperty(
        name="PostProcess",
        description="Contains the post-processing applied to the beauty pass. When enabled, no post-processing is "
                    "applied to the beauty pass itself",
        default=False,
    )
    use_pass_postfxmedia: BoolProperty(
        name="Postfix media",
        description="Contains the postfx media rendering applied to the beauty pass. When enabled, no postfx media "
                    "rendering is added to the beauty pass itself",
        default=False,
    )
    use_pass_ambient_light: BoolProperty(
        name="AmbientLight",
        description="Captures the ambient light (sky and environment) in the scene",
        default=False,
    )
    use_pass_ambient_light_dir: BoolProperty(
        name="AmbientLightDir",
        description="Captures the indirect ambient light (sky and environment) in the scene",
        default=False,
    )
    use_pass_ambient_light_indir: BoolProperty(
        name="AmbientLightIndir",
        description="Captures the indirect ambient light (sky and environment) in the scene",
        default=False,
    )
    use_pass_sunlight: BoolProperty(
        name="OctSunlight",
        description="Captures the sunlight in the scene",
        default=False,
    )
    use_pass_sunlight_dir: BoolProperty(
        name="SunLightDir",
        description="Captures the sunlight in the scene",
        default=False,
    )
    use_pass_sunlight_indir: BoolProperty(
        name="SunLightIndir",
        description="Captures the sunlight in the scene",
        default=False,
    )
    use_pass_light_pass_1: BoolProperty(
        name="LightPass1",
        description="Captures the light of the emitters with light pass ID 1",
        default=False,
    )
    use_pass_light_dir_pass_1: BoolProperty(
        name="LightDirPass1",
        description="Captures the light of the emitters with light pass ID 1",
        default=False,
    )
    use_pass_light_indir_pass_1: BoolProperty(
        name="LightIndirPass1",
        description="Captures the light of the emitters with light pass ID 1",
        default=False,
    )
    use_pass_light_pass_2: BoolProperty(
        name="LightPass2",
        description="Captures the light of the emitters with light pass ID 2",
        default=False,
    )
    use_pass_light_dir_pass_2: BoolProperty(
        name="LightDirPass2",
        description="Captures the light of the emitters with light pass ID 2",
        default=False,
    )
    use_pass_light_indir_pass_2: BoolProperty(
        name="LightIndirPass2",
        description="Captures the light of the emitters with light pass ID 2",
        default=False,
    )
    use_pass_light_pass_3: BoolProperty(
        name="LightPass3",
        description="Captures the light of the emitters with light pass ID 3",
        default=False,
    )
    use_pass_light_dir_pass_3: BoolProperty(
        name="LightDirPass3",
        description="Captures the light of the emitters with light pass ID 3",
        default=False,
    )
    use_pass_light_indir_pass_3: BoolProperty(
        name="LightIndirPass3",
        description="Captures the light of the emitters with light pass ID 3",
        default=False,
    )
    use_pass_light_pass_4: BoolProperty(
        name="LightPass4",
        description="Captures the light of the emitters with light pass ID 4",
        default=False,
    )
    use_pass_light_dir_pass_4: BoolProperty(
        name="LightDirPass4",
        description="Captures the light of the emitters with light pass ID 4",
        default=False,
    )
    use_pass_light_indir_pass_4: BoolProperty(
        name="LightIndirPass4",
        description="Captures the light of the emitters with light pass ID 4",
        default=False,
    )
    use_pass_light_pass_5: BoolProperty(
        name="LightPass5",
        description="Captures the light of the emitters with light pass ID 5",
        default=False,
    )
    use_pass_light_dir_pass_5: BoolProperty(
        name="LightDirPass5",
        description="Captures the light of the emitters with light pass ID 5",
        default=False,
    )
    use_pass_light_indir_pass_5: BoolProperty(
        name="LightIndirPass5",
        description="Captures the light of the emitters with light pass ID 5",
        default=False,
    )
    use_pass_light_pass_6: BoolProperty(
        name="LightPass6",
        description="Captures the light of the emitters with light pass ID 6",
        default=False,
    )
    use_pass_light_dir_pass_6: BoolProperty(
        name="LightDirPass6",
        description="Captures the light of the emitters with light pass ID 6",
        default=False,
    )
    use_pass_light_indir_pass_6: BoolProperty(
        name="LightIndirPass6",
        description="Captures the light of the emitters with light pass ID 6",
        default=False,
    )
    use_pass_light_pass_7: BoolProperty(
        name="LightPass7",
        description="Captures the light of the emitters with light pass ID 7",
        default=False,
    )
    use_pass_light_dir_pass_7: BoolProperty(
        name="LightDirPass7",
        description="Captures the light of the emitters with light pass ID 7",
        default=False,
    )
    use_pass_light_indir_pass_7: BoolProperty(
        name="LightIndirPass7",
        description="Captures the light of the emitters with light pass ID 7",
        default=False,
    )
    use_pass_light_pass_8: BoolProperty(
        name="LightPass8",
        description="Captures the light of the emitters with light pass ID 8",
        default=False,
    )
    use_pass_light_dir_pass_8: BoolProperty(
        name="LightDirPass8",
        description="Captures the light of the emitters with light pass ID 8",
        default=False,
    )
    use_pass_light_indir_pass_8: BoolProperty(
        name="LightIndirPass8",
        description="Captures the light of the emitters with light pass ID 8",
        default=False,
    )
    use_pass_light_pass_9: BoolProperty(
        name="LightPass9",
        description="Captures the light of the emitters with light pass ID 9",
        default=False,
    )
    use_pass_light_dir_pass_9: BoolProperty(
        name="LightDirPass9",
        description="Captures the light of the emitters with light pass ID 9",
        default=False,
    )
    use_pass_light_indir_pass_9: BoolProperty(
        name="LightIndirPass9",
        description="Captures the light of the emitters with light pass ID 9",
        default=False,
    )
    use_pass_light_pass_10: BoolProperty(
        name="LightPass10",
        description="Captures the light of the emitters with light pass ID 10",
        default=False,
    )
    use_pass_light_dir_pass_10: BoolProperty(
        name="LightDirPass10",
        description="Captures the light of the emitters with light pass ID 10",
        default=False,
    )
    use_pass_light_indir_pass_10: BoolProperty(
        name="LightIndirPass10",
        description="Captures the light of the emitters with light pass ID 10",
        default=False,
    )
    use_pass_light_pass_11: BoolProperty(
        name="LightPass11",
        description="Captures the light of the emitters with light pass ID 11",
        default=False,
    )
    use_pass_light_dir_pass_11: BoolProperty(
        name="LightDirPass11",
        description="Captures the light of the emitters with light pass ID 11",
        default=False,
    )
    use_pass_light_indir_pass_11: BoolProperty(
        name="LightIndirPass11",
        description="Captures the light of the emitters with light pass ID 11",
        default=False,
    )
    use_pass_light_pass_12: BoolProperty(
        name="LightPass12",
        description="Captures the light of the emitters with light pass ID 12",
        default=False,
    )
    use_pass_light_dir_pass_12: BoolProperty(
        name="LightDirPass12",
        description="Captures the light of the emitters with light pass ID 12",
        default=False,
    )
    use_pass_light_indir_pass_12: BoolProperty(
        name="LightIndirPass12",
        description="Captures the light of the emitters with light pass ID 12",
        default=False,
    )
    use_pass_light_pass_13: BoolProperty(
        name="LightPass13",
        description="Captures the light of the emitters with light pass ID 13",
        default=False,
    )
    use_pass_light_dir_pass_13: BoolProperty(
        name="LightDirPass13",
        description="Captures the light of the emitters with light pass ID 13",
        default=False,
    )
    use_pass_light_indir_pass_13: BoolProperty(
        name="LightIndirPass13",
        description="Captures the light of the emitters with light pass ID 13",
        default=False,
    )
    use_pass_light_pass_14: BoolProperty(
        name="LightPass14",
        description="Captures the light of the emitters with light pass ID 14",
        default=False,
    )
    use_pass_light_dir_pass_14: BoolProperty(
        name="LightDirPass14",
        description="Captures the light of the emitters with light pass ID 14",
        default=False,
    )
    use_pass_light_indir_pass_14: BoolProperty(
        name="LightIndirPass14",
        description="Captures the light of the emitters with light pass ID 14",
        default=False,
    )
    use_pass_light_pass_15: BoolProperty(
        name="LightPass15",
        description="Captures the light of the emitters with light pass ID 15",
        default=False,
    )
    use_pass_light_dir_pass_15: BoolProperty(
        name="LightDirPass15",
        description="Captures the light of the emitters with light pass ID 15",
        default=False,
    )
    use_pass_light_indir_pass_15: BoolProperty(
        name="LightIndirPass15",
        description="Captures the light of the emitters with light pass ID 15",
        default=False,
    )
    use_pass_light_pass_16: BoolProperty(
        name="LightPass16",
        description="Captures the light of the emitters with light pass ID 16",
        default=False,
    )
    use_pass_light_dir_pass_16: BoolProperty(
        name="LightDirPass16",
        description="Captures the light of the emitters with light pass ID 16",
        default=False,
    )
    use_pass_light_indir_pass_16: BoolProperty(
        name="LightIndirPass16",
        description="Captures the light of the emitters with light pass ID 16",
        default=False,
    )
    use_pass_light_pass_17: BoolProperty(
        name="LightPass17",
        description="Captures the light of the emitters with light pass ID 17",
        default=False,
    )
    use_pass_light_dir_pass_17: BoolProperty(
        name="LightDirPass17",
        description="Captures the light of the emitters with light pass ID 17",
        default=False,
    )
    use_pass_light_indir_pass_17: BoolProperty(
        name="LightIndirPass17",
        description="Captures the light of the emitters with light pass ID 17",
        default=False,
    )
    use_pass_light_pass_18: BoolProperty(
        name="LightPass18",
        description="Captures the light of the emitters with light pass ID 18",
        default=False,
    )
    use_pass_light_dir_pass_18: BoolProperty(
        name="LightDirPass18",
        description="Captures the light of the emitters with light pass ID 18",
        default=False,
    )
    use_pass_light_indir_pass_18: BoolProperty(
        name="LightIndirPass18",
        description="Captures the light of the emitters with light pass ID 18",
        default=False,
    )
    use_pass_light_pass_19: BoolProperty(
        name="LightPass19",
        description="Captures the light of the emitters with light pass ID 19",
        default=False,
    )
    use_pass_light_dir_pass_19: BoolProperty(
        name="LightDirPass19",
        description="Captures the light of the emitters with light pass ID 19",
        default=False,
    )
    use_pass_light_indir_pass_19: BoolProperty(
        name="LightIndirPass19",
        description="Captures the light of the emitters with light pass ID 19",
        default=False,
    )
    use_pass_light_pass_20: BoolProperty(
        name="LightPass20",
        description="Captures the light of the emitters with light pass ID 20",
        default=False,
    )
    use_pass_light_dir_pass_20: BoolProperty(
        name="LightDirPass20",
        description="Captures the light of the emitters with light pass ID 20",
        default=False,
    )
    use_pass_light_indir_pass_20: BoolProperty(
        name="LightIndirPass20",
        description="Captures the light of the emitters with light pass ID 20",
        default=False,
    )
    use_pass_crypto_instance_id: BoolProperty(
        name="CryptoInstanceID",
        description="Cryptomatte channels for instance IDs",
        default=False,
    )
    use_pass_crypto_mat_node_name: BoolProperty(
        name="CryptoMatNodeName",
        description="Cryptomatte channels using material node names",
        default=False,
    )
    use_pass_crypto_mat_node: BoolProperty(
        name="CryptoMatNode",
        description="Cryptomatte channels using distinct material nodes",
        default=False,
    )
    use_pass_crypto_mat_pin_node: BoolProperty(
        name="CryptoMatPinNode",
        description="Cryptomatte channels using material pin names",
        default=False,
    )
    use_pass_crypto_obj_node_name: BoolProperty(
        name="CryptoObjNodeName",
        description="Cryptomatte channels using object layer node names",
        default=False,
    )
    use_pass_crypto_obj_node: BoolProperty(
        name="CryptoObjNode",
        description="Cryptomatte channels using distinct object layer nodes",
        default=False,
    )
    use_pass_crypto_obj_pin_node: BoolProperty(
        name="CryptoObjPinNode",
        description="Cryptomatte channels using object layer pin names",
        default=False,
    )
    use_pass_crypto_render_layer: BoolProperty(
        name="CryptoRenderLayer",
        description="Cryptomatte channels using render layers",
        default=False,
    )
    use_pass_crypto_geometry_node_name: BoolProperty(
        name="CryptoGeometryNodeName",
        description="Cryptomatte channels using geometry node names",
        default=False,
    )
    use_pass_crypto_user_instance_id: BoolProperty(
        name="CryptoUserInstanceID",
        description="Cryptomatte channels using user instance id",
        default=False,
    )
    use_pass_info_geo_normal: BoolProperty(
        name="GeoNormal",
        description="Assigns a colour for the geometry normal at the position hit by the camera ray",
        default=False,
    )
    use_pass_info_smooth_normal: BoolProperty(
        name="SmoothNormal",
        description="Assigns a colour for the smooth normal at the position hit by the camera ray",
        default=False,
    )
    use_pass_info_shading_normal: BoolProperty(
        name="ShadingNormal",
        description="Assigns a colour for the shading normal at the position hit by the camera ray",
        default=False,
    )
    use_pass_info_tangent_normal: BoolProperty(
        name="TangentNormal",
        description="Assigns a colour for the tangent (local) normal at the position hit by the camera ray",
        default=False,
    )
    use_pass_info_z_depth: BoolProperty(
        name="ZDepth",
        description="Assigns a gray value proportional to the camera ray hit distance",
        default=False,
    )
    use_pass_info_position: BoolProperty(
        name="Position",
        description="Assigns RGB values according the intersection point of the camera ray",
        default=False,
    )
    use_pass_info_uv: BoolProperty(
        name="UV",
        description="Assigns RGB values according the geometry's texture coordinates",
        default=False,
    )
    use_pass_info_tex_tangent: BoolProperty(
        name="TexTangent",
        description="The tangent vector of U texture coordinates (Dp du)",
        default=False,
    )
    use_pass_info_motion_vector: BoolProperty(
        name="MotionVector",
        description="Renders the motion vectors as 2D vectors in screen space",
        default=False,
    )
    use_pass_info_mat_id: BoolProperty(
        name="MatID",
        description="Assigns RGB values according the material mapped to the geometry",
        default=False,
    )
    use_pass_info_obj_id: BoolProperty(
        name="ObjID",
        description="Colours each distinct object in the scene with a colour based on it's ID",
        default=False,
    )
    use_pass_info_obj_layer_color: BoolProperty(
        name="ObjLayerColor",
        description="The color specified in the object layer node",
        default=False,
    )
    use_pass_info_baking_group_id: BoolProperty(
        name="BakingGroupID",
        description="Colours each distinct baking group in the scene with a colour based on it's ID",
        default=False,
    )
    use_pass_info_light_pass_id: BoolProperty(
        name="LightPassID",
        description="Colours emitters based on their light pass ID",
        default=False,
    )
    use_pass_info_render_layer_id: BoolProperty(
        name="RenderLayerID",
        description="Colours objects on the same layer with the same color based on the render layer ID",
        default=False,
    )
    use_pass_info_render_layer_mask: BoolProperty(
        name="RenderLayerMask",
        description="Mask for geometry on the active render layer",
        default=False,
    )
    use_pass_info_wireframe: BoolProperty(
        name="Wireframe",
        description="Wireframe display of the geometry",
        default=False,
    )
    use_pass_info_ao: BoolProperty(
        name="AO",
        description="Assigns a colour to the camera ray's hit point proportional to the amount of occlusion by other "
                    "geometry",
        default=False,
    )
    use_pass_mat_opacity: BoolProperty(
        name="Opacity",
        description="Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry",
        default=False,
    )
    use_pass_mat_roughness: BoolProperty(
        name="Roughness",
        description="Material roughness at the camera ray's hit point",
        default=False,
    )
    use_pass_mat_ior: BoolProperty(
        name="IOR",
        description="Material index of refraction at the camera ray's hit point",
        default=False,
    )
    use_pass_mat_diff_filter_info: BoolProperty(
        name="DiffFilterInfo",
        description="The diffuse texture color of the diffuse and glossy material",
        default=False,
    )
    use_pass_mat_reflect_filter_info: BoolProperty(
        name="ReflectFilterInfo",
        description="The reflection texture color of the specular and glossy material",
        default=False,
    )
    use_pass_mat_refract_filter_info: BoolProperty(
        name="RefractFilterInfo",
        description="The refraction texture color of the specular material",
        default=False,
    )
    use_pass_mat_transm_filter_info: BoolProperty(
        name="TransmFilterInfo",
        description="The transmission texture color of the diffuse material",
        default=False,
    )
    use_passes: BoolProperty(
        name="Render passes",
        description="",
        default=False,
    )

    def update_info_pass_max_samples(self, context):
        oct_scene = context.scene.octane
        oct_scene.info_pass_max_samples = self.info_pass_max_samples

    info_pass_max_samples: IntProperty(
        name="Info pass max samples",
        description="The maximum number of samples for the info passes (excluding AO)",
        min=1, max=1024,
        default=128,
        update=update_info_pass_max_samples,
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
    shading_enabled: BoolProperty(
        name="Enable shading",
        description="If enabled, the wireframe will be rendered on slightly shaded objects",
        default=True,
    )
    highlight_backfaces: BoolProperty(
        name="Highlight backfaces",
        description="If enabled, the backfaces will be tinted red",
        default=False,
    )
    info_pass_z_depth_max: FloatProperty(
        name="Z-depth max",
        description="The Z-depth value at which the AOV values become white / 1. LDR exports will clamp at that "
                    "depth, but HDR exports will write values > 1 for larger depth",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=5.0,
        step=10,
        precision=4,
    )
    info_pass_z_depth_environment: FloatProperty(
        name="Environment depth",
        description="The Z-depth value that will be used for the environment/background",
        min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
        default=1000.0,
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
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum "
                    "movement of 1 screen width in the shutter interval",
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
        description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit "
                    "by the camera ray",
        default=False,
    )
    pass_pp_env: BoolProperty(
        name="Include environment",
        description="When enabled, the environment render pass is included when doing post-processing. This option "
                    "only applies when the environment render pass and alpha channel are enabled",
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
        description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. "
                    "Low values result in pitting artefacts at feathered edges, while large values the values can "
                    "result in artefacts in places with coverage for lots of different IDs",
        min=4, max=25,
        default=10,
    )
    # noinspection PyRedundantParentheses
    octane_render_pass_types = (
        ("0", "Combined", "Combined pass", 0),
        ("43", "Denoiser Beauty", "Denoiser Beauty pass", 43),
        (None),
        ("123", "Denoise albedo", "Denoise albedo pass", 123),
        ("40", "Denoise normal", "Denoise normal pass", 40),
        ("3", "Diffuse", "Diffuse pass", 3),
        ("4", "Diffuse direct", "Diffuse direct pass", 4),
        ("5", "Diffuse indirect", "Diffuse indirect pass", 5),
        ("6", "Diffuse filter", "Diffuse filter pass", 6),
        ("1", "Emitters", "Emitters pass", 1),
        ("2", "Environment", "Environment pass", 2),
        ("7", "Reflection", "Reflection pass", 7),
        ("8", "Reflection direct", "Reflection direct pass", 8),
        ("9", "Reflection indirect", "Reflection indirect pass", 9),
        ("10", "Reflection filter", "Reflection filter pass", 10),
        ("11", "Refraction", "Refraction pass pass", 11),
        ("12", "Refraction filter", "Refraction filter pass pass", 12),
        ("15", "Subsurface scattering", "Subsurface scattering pass", 15),
        ("13", "Transmission", "Transmission pass", 13),
        ("14", "Transmission filter", "Transmission filter pass", 14),
        (None),
        ("35", "Volume", "Volume pass", 35),
        ("36", "Volume Mask", "Volume Mask pass", 36),
        ("37", "Volume Emission", "Volume Emission pass", 37),
        ("38", "Volume Z-Depth Front", "Volume Z-Depth Front pass", 38),
        ("39", "Volume Z-Depth Back", "Volume Z-Depth Back pass", 39),
        (None),
        ("44", "Denoiser DiffDir", "Denoiser Diffuse Direct pass", 44),
        ("45", "Denoiser DiffIndir", "Denoiser Diffuse Indirect pass", 45),
        ("46", "Denoiser ReflectDir", "Denoiser Reflection Direct pass", 46),
        ("47", "Denoiser ReflectIndir", "Denoiser Reflection Indirect pass", 47),
        ("49", "Denoiser Refraction", "Denoiser Refraction(Remainder) pass", 49),
        ("76", "Denoiser Emission", "Denoiser Emission pass", 76),
        ("74", "Denoiser Volume", "Denoiser Volume pass", 74),
        ("75", "Denoiser Volume Emission", "Denoiser Volume Emission pass", 75),
        (None),
        ("18", "Black layer shadows", "Layer black shadows pass", 18),
        ("20", "Layer reflections", "Layer reflections pass", 20),
        ("17", "Layer shadows", "Layer shadows pass", 17),
        ("", "Auxiliary", "", 0),
        ("10000", "AOV Output", "AOV Outputs", 10000),
        (None),
        ("2001", "Cryptomatte MaterialName", "Cryptomatte channels for material node names", 2001),
        ("2006", "Cryptomatte MaterialNode", "Cryptomatte channels using distinct material nodes", 2006),
        ("2002", "Cryptomatte MaterialPinName", "Cryptomatte channels for material pin names", 2002),
        ("2003", "Cryptomatte ObjectName", "Cryptomatte channels for object layer node names", 2003),
        ("2004", "Cryptomatte ObjectNode", "Cryptomatte channels using distinct object layer nodes", 2004),
        ("2007", "Cryptomatte ObjectPinName", "Cryptomatte channels for object layer pin names", 2007),
        ("2005", "Cryptomatte InstanceID", "Cryptomatte channels for instance IDs", 2005),
        ("2009", "Cryptomatte RenderLayer", "Cryptomatte channels for render layers", 2009),
        ("2010", "Cryptomatte UserInstanceID", "Cryptomatte channels for user instance IDs", 2010),
        ("2008", "Cryptomatte GeometryNodeName", "Cryptomatte channels for geometry node names", 2008),
        (None),
        ("33", "Irradiance", "Irradiance pass", 33),
        ("34", "Light Direction", "Light Direction pass", 34),
        ("31", "Noise", "Noise pass", 31),
        ("84", "Postfix media", "Postfix media pass", 84),
        ("16", "Post processing", "Post processing pass", 16),
        ("32", "Shadow", "Shadow pass", 32),
        ("", "Info", "", 0),
        ("1010", "Ambient occlusion", "Ambient occlusion pass", 1010),
        ("1017", "Baking group ID", "Colours each distinct baking group in the scene with a colour based on it's ID",
         1017),
        ("1020", "Diffuse Filter(info)", "The diffuse texture color of the diffuse and glossy material", 1020),
        ("1019", "Index of refraction", "Material index of refraction at the camera ray's hit point", 1019),
        ("1014", "Light pass ID", "Light pass ID pass", 1014),
        ("1004", "Material ID", "Material ID pass", 1004),
        ("1011", "Motion vector", "Motion vector pass", 1011),
        ("1000", "Normal(geometric)", "Geometric normals pass", 1000),
        ("1001", "Normal(shading)", "Shading normals pass", 1001),
        ("1008", "Normal(smooth)", "Smooth normals pass", 1008),
        ("1015", "Normal(tangent)", "Tangent normals pass", 1015),
        ("1009", "Object ID", "Object ID pass", 1009),
        ("1024", "Object layer color", "The color specified in the object layer node", 1024),
        ("1016", "Opacity",
         "Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry", 1016),
        ("1002", "Position", "Position pass", 1002),
        ("1021", "Reflection Filter(info)", "The reflection texture color of the specular and glossy material", 1021),
        ("1022", "Refraction Filter(info)", "The refraction texture color of the specular material", 1022),
        ("1012", "Render layer ID",
         "Colours objects on the same layer with the same color based on the render layer ID", 1012),
        ("1013", "Render layer mask", "Mask for geometry on the active render layer", 1013),
        ("1018", "Roughness", "Material roughness at the camera ray's hit point", 1018),
        ("1006", "Texture tangent", "Tangent U pass", 1006),
        ("1023", "Transm Filter(info)", "The transmission texture color of the diffuse material", 1023),
        ("1005", "UV coordinates", "UV coordinates pass", 1005),
        ("1007", "Wireframe", "Wireframe pass", 1007),
        ("1003", "Z-depth", "Z-depth pass", 1003),
        ("", "Light", "", 0),
        ("21", "Ambient light", "Ambient light pass", 21),
        ("22", "Sunlight", "Sunlight pass", 22),
        ("23", "Light pass 1", "Light pass 1", 23),
        ("24", "Light pass 2", "Light pass 2", 24),
        ("25", "Light pass 3", "Light pass 3", 25),
        ("26", "Light pass 4", "Light pass 4", 26),
        ("27", "Light pass 5", "Light pass 5", 27),
        ("28", "Light pass 6", "Light pass 6", 28),
        ("29", "Light pass 7", "Light pass 7", 29),
        ("30", "Light pass 8", "Light pass 8", 30),
        ("85", "Light pass 9", "Light pass 9", 85),
        ("86", "Light pass 10", "Light pass 10", 86),
        ("87", "Light pass 11", "Light pass 11", 87),
        ("88", "Light pass 12", "Light pass 12", 88),
        ("89", "Light pass 13", "Light pass 13", 89),
        ("90", "Light pass 14", "Light pass 14", 90),
        ("91", "Light pass 15", "Light pass 15", 91),
        ("92", "Light pass 16", "Light pass 16", 92),
        ("93", "Light pass 17", "Light pass 17", 93),
        ("94", "Light pass 18", "Light pass 18", 94),
        ("95", "Light pass 19", "Light pass 19", 95),
        ("96", "Light pass 20", "Light pass 20", 96),
        (None),
        ("54", "Ambient light direct", "Ambient light direct pass", 54),
        ("56", "Sunlight direct", "Sunlight direct pass", 56),
        ("58", "Light pass 1 direct", "Light pass 1 direct", 58),
        ("59", "Light pass 2 direct", "Light pass 2 direct", 59),
        ("60", "Light pass 3 direct", "Light pass 3 direct", 60),
        ("61", "Light pass 4 direct", "Light pass 4 direct", 61),
        ("62", "Light pass 5 direct", "Light pass 5 direct", 62),
        ("63", "Light pass 6 direct", "Light pass 6 direct", 63),
        ("64", "Light pass 7 direct", "Light pass 7 direct", 64),
        ("65", "Light pass 8 direct", "Light pass 8 direct", 65),
        ("97", "Light pass 9 direct", "Light pass 9 direct", 97),
        ("98", "Light pass 10 direct", "Light pass 10 direct", 98),
        ("99", "Light pass 11 direct", "Light pass 11 direct", 99),
        ("100", "Light pass 12 direct", "Light pass 12 direct", 100),
        ("101", "Light pass 13 direct", "Light pass 13 direct", 101),
        ("102", "Light pass 14 direct", "Light pass 14 direct", 102),
        ("103", "Light pass 15 direct", "Light pass 15 direct", 103),
        ("104", "Light pass 16 direct", "Light pass 16 direct", 104),
        ("105", "Light pass 17 direct", "Light pass 17 direct", 105),
        ("106", "Light pass 18 direct", "Light pass 18 direct", 106),
        ("107", "Light pass 19 direct", "Light pass 19 direct", 107),
        ("108", "Light pass 20 direct", "Light pass 20 direct", 108),
        (None),
        ("55", "Ambient light indirect", "Ambient light indirect pass", 55),
        ("57", "Sunlight indirect", "Sunlight indirect pass", 57),
        ("66", "Light pass 1 indirect", "Light pass 1 indirect", 66),
        ("67", "Light pass 2 indirect", "Light pass 2 indirect", 67),
        ("68", "Light pass 3 indirect", "Light pass 3 indirect", 68),
        ("69", "Light pass 4 indirect", "Light pass 4 indirect", 69),
        ("70", "Light pass 5 indirect", "Light pass 5 indirect", 70),
        ("71", "Light pass 6 indirect", "Light pass 6 indirect", 71),
        ("72", "Light pass 7 indirect", "Light pass 7 indirect", 72),
        ("73", "Light pass 8 indirect", "Light pass 8 indirect", 73),
        ("109", "Light pass 9 indirect", "Light pass 9 indirect", 109),
        ("110", "Light pass 10 indirect", "Light pass 10 indirect", 110),
        ("111", "Light pass 11 indirect", "Light pass 11 indirect", 111),
        ("112", "Light pass 12 indirect", "Light pass 12 indirect", 112),
        ("113", "Light pass 13 indirect", "Light pass 13 indirect", 113),
        ("114", "Light pass 14 indirect", "Light pass 14 indirect", 114),
        ("115", "Light pass 15 indirect", "Light pass 15 indirect", 115),
        ("116", "Light pass 16 indirect", "Light pass 16 indirect", 116),
        ("117", "Light pass 17 indirect", "Light pass 17 indirect", 117),
        ("118", "Light pass 18 indirect", "Light pass 18 indirect", 118),
        ("119", "Light pass 19 indirect", "Light pass 19 indirect", 119),
        ("120", "Light pass 20 indirect", "Light pass 20 indirect", 120),

    )
    current_preview_pass_type: EnumProperty(
        name="Preview pass type",
        description="Pass used for preview rendering",
        items=octane_render_pass_types,
        default='0',
    )
    current_aov_output_id: IntProperty(
        name="Preview AOV Output ID",
        description="The ID of the AOV Outputs for preview(beauty pass output will be used if no valid results for "
                    "the assigned index)",
        min=1, max=16,
        default=1,
    )
    aov_output_group_collection: PointerProperty(
        name="Octane Aov Output Group Collection",
        description="",
        type=OctaneAovOutputGroupCollection,
    )
    render_passes_style = (
        ("RENDER_PASSES", "Classic Render Passes",
         "The classic render passes style but the new render AOVs won't be available there", 0),
        ("RENDER_AOV_GRAPH", "Render AOV Node Graph", "The render AOV node graph with the AOV features", 1),
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

    def sync_custom_data(self, octane_node, scene, region, v3d, rv3d, session_type):
        if self.render_pass_style != "RENDER_PASSES":
            return
        current_preview_pass_type = utility.get_enum_int_value(self, "current_preview_pass_type",
                                                               consts.RenderPassID.Beauty)
        current_preview_pass_pin_name = ""
        if current_preview_pass_type in consts.OCTANE_PASS_ID_TO_NODE_PIN_NAME:
            current_preview_pass_pin_name = consts.OCTANE_PASS_ID_TO_NODE_PIN_NAME[current_preview_pass_type]
        if octane_node.node_type == consts.NodeType.NT_RENDER_PASSES:
            octane_node.set_pin_name(current_preview_pass_pin_name, False, "", True)
        elif octane_node.node_type == consts.NodeType.NT_BLENDER_NODE_GRAPH_NODE:
            render_pass_configs = octane_node.render_pass_configs
            for idx, property_name in enumerate(self.octane_property_name_list):
                if not hasattr(self, property_name):
                    continue
                pin_symbol = self.octane_property_pin_symbol_list[idx]
                if pin_symbol not in render_pass_configs:
                    continue
                config = render_pass_configs[pin_symbol]
                node_type = config["node_type"]
                pin_index = config["pin_index"]
                pin_type = config["pin_type"]
                socket_type, _, _ = self.octane_property_type_list[idx]
                property_value = getattr(self, property_name, None)
                if socket_type == consts.SocketType.ST_ENUM:
                    property_value = self.rna_type.properties[property_name].enum_items[property_value].value
                if pin_symbol == current_preview_pass_pin_name:
                    property_value = True
                octane_node.node.set_pin(consts.OctaneDataBlockSymbolType.PIN_INDEX, pin_index, pin_symbol, socket_type,
                                         pin_type, node_type, False, "", property_value)

    def update_legacy_data(self, context, legacy_data, is_viewport=None):
        self.layers_mode = self.LEGACY_LAYER_MODE_CONVERTOR.get(getattr(legacy_data, "octane_render_layers_mode", ""),
                                                                "Normal")
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


class OctaneRenderPropertyGroup(bpy.types.PropertyGroup):
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
    # OCTANE COLOR MANAGEMENT
    # ################################################################################################
    show_blender_color_management: BoolProperty(
        name="Show Blender Color Management",
        description="Show the Blender's built-in Color Management Panel. \nBy default, we recommend reset the Blender "
                    "Color Management as 'no-op'(do nothing) and use the Octane's Color Management exclusively. In "
                    "this case,"
        "we hide the Blender Color Management so it won't confuse users\n But you can always choose the Blender's "
        "Color Management if you like. \nJust do not use both of them at the same time",
        default=True,
    )
    # ################################################################################################
    # OCTANE OPTIMIZATION
    # ################################################################################################
    octane_opt_mesh_generation: BoolProperty(
        name="Use Opt. Mesh Generation Mode in Preview",
        description="[PREVIEW MODE] Do not regenerate & upload meshes(except reshapable ones) which are already cached",
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
    kernel_data_modes = (
        ("PROPERTY_PANEL", "Classic Property Panel", "The classic property panel", 0),
        ('NODETREE', "Kernel NodeTree", "The kernel node tree", 1),
    )
    kernel_data_mode: EnumProperty(
        name="Kernel Data Mode",
        description="Use the classic Kernel or the new Kernel Nodetree",
        items=kernel_data_modes,
        default="PROPERTY_PANEL",
    )
    kernel_json_node_tree_helper: StringProperty(
        name="Kernel Json Node Tree",
        default="",
        maxlen=65535,
    )

    # ################################################################################################
    # OCTANE ANIMATION SETTINGS
    # ################################################################################################
    animation_settings: PointerProperty(
        name="Octane Animation Settings",
        description="",
        type=OctaneAnimationSettingsPropertyGroup,
    )
    # ################################################################################################
    # OCTANE RENDER LAYER
    # ################################################################################################
    render_layer: PointerProperty(
        name="Octane Render Layer",
        description="",
        type=OctaneGlobalRenderLayerPropertyGroup,
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
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum "
                    "movement of 1 screen width in the shutter interval",
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
        description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit "
                    "by the camera ray",
        default=False,
    )
    pass_pp_env: BoolProperty(
        name="Include environment",
        description="When enabled, the environment render pass is included when doing post-processing. This option "
                    "only applies when the environment render pass and alpha channel are enabled",
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
        description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. "
                    "Low values result in pitting artefacts at feathered edges, while large values the values can"
                    "result in artefacts in places with coverage for lots of different IDs",
        min=4, max=25,
        default=10,
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
        description="All the non-active render layers become the active render layer and the active render layer "
                    "becomes inactive",
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
                    "will be made invisible. But side effects(shadows, reflections...)will be recorded in the render "
                    "layer passes\n"
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
        default=8192,
    )
    out_of_core_gpu_headroom: IntProperty(
        name="GPU headroom (MB)",
        description="To run the render kernels successfully, there needs to be some amount of free GPU memory. This"
                    "setting determines how much GPU memory the render engine will leave available when uploading the"
                    "images. The"
        "default value should work for most scenes",
        min=1,
        default=300,
    )
    # ################################################################################################
    # OCTANE COMMON
    # ################################################################################################
    octane_task_progress: FloatProperty(
        name="Octane Task Progress",
        description="Octane task is running now, you can use 'ESC' to cancel it. \nThis value is used for displaying "
                    "the task progress so please do not modify this value manually",
        default=0.0,
        precision=0,
        min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
        subtype='PERCENTAGE',
    )
    viewport_hide: BoolProperty(
        name="Viewport hide priority",
        description="Hide from final render objects hidden in viewport",
        default=False,
    )
    prefer_image_types = (
        ("DEFAULT", "Octane Default", "Render as Octane default settings", 0),
        ("LDR", "LDR", "Render as LDR(tonemapped) image if applicable", 1),
        ("HDR", "HDR", "Render as HDR image if applicable", 2),
    )
    prefer_image_type: EnumProperty(
        name="Prefer Image Type",
        description="",
        items=prefer_image_types,
        default="DEFAULT",
    )
    prefer_tonemap: BoolProperty(
        name="Prefer tonemap if applicable",
        description="Render as tonemapped image if applicable",
        default=True,
    )
    export_with_object_layers: BoolProperty(
        name="Export with object layers",
        description="Export with object layers properties. If disabled, all object layer properties will be removed "
                    "and the whole scene will be put in a single object layer",
        default=True,
    )
    maximize_instancing: BoolProperty(
        name="Maximize Instancing",
        description="If enabled, Octane will try to collect and group instances into scatter as much as possible",
        default=True,
    )

    def update_octane_shading_type(self, context):
        view = context.space_data
        if view and getattr(view, "shading", False):
            if view.shading.type != self.octane_shading_type:
                view.shading.type = self.octane_shading_type

    octane_shading_type: EnumProperty(
        name="Octane Shading Type",
        description="",
        items=octane_shading_type_modes,
        default="SOLID",
        update=update_octane_shading_type,
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
    enable_realtime: BoolProperty(
        name="Enable Real-time in viewport rendering",
        description="Enable Octane real-time mode in viewport rendering",
        default=False,
    )
    resource_cache_types = (
        ('None', "None", "Disable resource cache system", consts.ResourceCacheType.NONE),
        ('Texture Only', "Texture Only", "Only cache the textures in RAM", consts.ResourceCacheType.TEXTURE_ONLY),
        ('Geometry Only', "Geometry Only", "Only cache the geometries in RAM", consts.ResourceCacheType.GEOMETRY_ONLY),
        ('All', "All", "Cache the textures and geometries in RAM", consts.ResourceCacheType.ALL),
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
        description="The Maximum subdivision level that should be applied on the geometries in the scene. Setting "
                    "zero will disable the subdivision",
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
        description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders "
                    "incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled",
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
        description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are "
                    "ignored",
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
        description="Specifies the number of samples that are run in parallel. A small number means less parallel "
                    "samples, less memory usage and it makes caustics visible faster, but renders probably slower. A "
                    "large number"
                    "means more memory usage, slower visible caustics and probably a higher speed",
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
        description="Ambient occlusion environment texture, which is used for AO rays. If not specified, "
                    "the environment will be used instead",
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
        description="The subsample mode should be used in rendering",
        items=sub_sample_modes,
        default='2x2 subsampling',
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
        description="Specifies the number of samples that are run in parallel. A small number means less parallel "
                    "samples and less memory usage, but potentially slower speed. A large number means more memory "
                    "usage and potentially a higher speed",
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
        description="If enabled, the work is distributed to the network render slaves in such a way to minimize the "
                    "amount of data that is sent to the network render master",
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
        description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value"
                    "increases the memory usage on the system, but doesn't affect memory usage on the system and may "
                    "increase render speed",
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
        ('6', "Texture tangent", "", 6),
        ('7', "Wireframe", "", 7),
        ('8', "Smooth normals", "", 8),
        ('9', "Object layer ID", "", 9),
        ('10', "Ambient occlusion", "", 10),
        ('11', "Motion vector", "", 11),
        ('12', "Render layer ID", "", 12),
        ('13', "Render layer Mask", "", 13),
        ('14', "Light pass ID", "", 14),
        ('15', "Tangent normal", "", 15),
        ('16', "Opacity", "", 16),
        ('17', "Baking group ID", "", 17),
        ('18', "Roughness", "", 18),
        ('19', "Index of reflection", "", 19),
        ('20', "Diffuse filter color", "", 20),
        ('21', "Reflection filter color", "", 21),
        ('22', "Refraction filter color", "", 22),
        ('23', "Transmission filter color", "", 23),
        ('24', "Object layer color", "", 24),
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
        description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum "
                    "movement of 1 screen width in the shutter interval",
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
        description="Runs the kernel more coherently which makes it usually faster, but may require at least a few "
                    "hundred samples/pixel to get rid of visible artifacts",
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
    use_preview_camera_imager: BoolProperty(
        name="Enable Imager in Interactive Mode",
        description="Tick to enable Octane Imager in interactive preview mode",
        default=True,
    )
    use_render_camera_imager: BoolProperty(
        name="Enable Imager in Render Mode",
        description="Tick to enable Octane Imager in render mode",
        default=True,
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
        name="Use for all cameras (Imager)",
        description="If enabled, we always use the imager below for all cameras(ignore settings in other cameras). We "
                    "recommend that you keep it on unless you need multiple different imager configurations in the "
                    "scene",
        default=True,
    )
    use_preview_post_process_setting: BoolProperty(
        name="Use for all cameras (PostProcess)",
        description="If enabled, we always use the postprocess below for all cameras(ignore settings in other "
                    "cameras). We recommend that you keep it on unless you need multiple different postprocess "
                    "configurations in the scene",
        default=True,
    )
    adaptive_sampling: BoolProperty(
        name="Adaptive sampling",
        description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image "
                    "parts",
        default=False,
    )
    adaptive_noise_threshold: FloatProperty(
        name="Noise threshold",
        description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the "
                    "adaptive sampling or the noise render pass is enabled",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.03,
        step=3,
        precision=4,
    )
    adaptive_expected_exposure: FloatProperty(
        name="Expected exposure",
        description="The expected exposure should be approximately the same value as the exposure in the image or 0 "
                    "to ignore these settings. Only valid if adaptive sampling is enabled",
        min=0.0, soft_min=0.0, max=10000, soft_max=4096.0,
        default=0.0,
        step=0.1,
        precision=4,
    )
    adaptive_min_samples: IntProperty(
        name="Min. adaptive samples",
        description="Minimum number of samples per pixel until adaptive sampling kicks inunto estimate initial noise "
                    "level. Higher the value for high quality, but will increase render time. Only valid if adaptive "
                    "sampling is enabled",
        min=2, soft_min=2, max=1000000, soft_max=1024,
        default=256,
    )
    adaptive_group_pixels_mode = (
        ('1', "None", "",),
        ('2', "2 x 2", ""),
        ('4', "4 x 4", ""),
    )
    adaptive_group_pixels: EnumProperty(
        name="Group pixels",
        description="Size of the pixel groups that are evaluated together "
                    "to decide whether sampling should stop or not",
        items=adaptive_group_pixels_mode,
        default='2',
    )
    adaptive_group_pixels1_mode = (
        ('1', "None", "", 1),
        ('2', "2 x 2", "", 2),
        ('4', "4 x 4", "", 4),
    )
    adaptive_group_pixels1: EnumProperty(
        name="Group pixels",
        description="Size of the pixel groups that are evaluated together "
                    "to decide whether sampling should stop or not",
        items=adaptive_group_pixels1_mode,
        default='2',
    )
    gui_octane_export_ocio_color_space_name: StringProperty(
        name="Color space",
        description="Choose intermediate color space to allow conversions with OCIO. "
                    "This should correspond to the same color space as the 'Octane' box",
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
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the "
                    "same color space as the 'Octane' box",
        default="",
    )
    octane_export_ocio_look: StringProperty(
        name="OCIO look",
        description="OCIO look to apply",
        default="",
    )
    octane_export_force_use_tone_map: BoolProperty(
        name="Force use tone map",
        description="Whether to apply Octane's built-in tone mapping (before applying any OCIO look(s)) when using an "
                    "OCIO view. This may produce undesirable results due to an intermediate reduction to the sRGB"
                    "color space",
        default=False,
    )
    octane_export_premultiplied_alpha: BoolProperty(
        name="Premultiplied Alpha",
        description="Premultiplied Alpha",
        default=False,
    )
    octane_export_dwa_compression_level: IntProperty(
        name="DWA compression level",
        description="DWA compression level",
        min=0, max=2000,
        default=45,
    )
    octane_export_jpeg_quality: IntProperty(
        name="Quality",
        description="Jpeg quality",
        min=1, max=100,
        default=75,
    )
    use_octane_export: BoolProperty(
        name="Enable Octane Export",
        description="Enable Octane Export",
        default=False,
    )
    reuse_blender_output_path: BoolProperty(
        name="Reuse Blender's Output Path",
        description="Whether to use the 'Output Path' in the Blender Output panel. If not, you can use a new output "
                    "path for Octane Outputs. E.g. put the Octane Outputs in a different folder from Blender default "
                    "Outputs",
        default=True,
    )
    octane_output_path: StringProperty(
        name="Octane Output Path",
        description="An independent output path that's used for Octane Outputs only. In this way, you can put Octane"
                    "outputs and Blender default outputs in two different places",
        default="",
        subtype="FILE_PATH",
    )
    octane_export_prefix_tag: StringProperty(
        name="Octane Prefix Tag",
        description="Octane export prefix tag. If given, this name will be concatenated to the file name as prefix(to"
                    "distinguish the Blender outputs and Octane export outputs)",
        default="",
    )
    octane_export_postfix_tag: StringProperty(
        name="Octane Postfix Tag",
        description="""Octane export postfix. If given, this name will be concatenated to the file name as postfix.\n"""
                    """###   Frame number. e.g. image_##_test.png translates to image_01_test.png\n"""
                    """$OCTANE_PASS$   Octane pass name.\n"""
                    """$VIEW_LAYER$   Blender viewlayer name""",
        default="",
    )

    def octane_export_mode_enum_items_callback(self, context):
        if utility.is_deep_image_enabled(getattr(context, "scene", None)):
            return octane_export_with_deep_image_modes
        else:
            return octane_export_without_deep_image_modes

    octane_export_mode: EnumProperty(
        name="Octane Export Mode",
        description="Export image as separate files, multilayer EXR, or deep EXR",
        items=octane_export_mode_enum_items_callback,
    )
    octane_export_file_types = (
        ("PNG", "PNG", "", 0),
        ("JPEG", "JPEG", "", 2),
        ("TIFF", "TIFF", "", 3),
        ("EXR", "EXR", "", 1),
    )
    octane_export_file_type: EnumProperty(
        name="File type",
        description="File type",
        items=octane_export_file_types,
        default="PNG",
    )
    octane_integer_bit_depth_modes = (
        ("8_BIT", "8-bit(integer)", "8-bit(integer)(default)", 0),
        ("16_BIT", "16-bit(integer)", "16-bit(integer)", 1),
    )
    octane_png_bit_depth: EnumProperty(
        name="Bit depth",
        description="Bit depth",
        items=octane_integer_bit_depth_modes,
        default="8_BIT",
    )
    octane_integer_bit_depth: EnumProperty(
        name="Bit depth",
        description="Bit depth",
        items=octane_integer_bit_depth_modes,
        default="8_BIT",
    )
    octane_float_bit_depth_modes = (
        ("16_BIT", "16-bit(floating point)", "16-bit(floating point)(default)", 0),
        ("32_BIT", "32-bit(floating point)", "32-bit(floating point)", 1),
    )
    octane_exr_bit_depth: EnumProperty(
        name="Bit depth",
        description="Bit depth",
        items=octane_float_bit_depth_modes,
        default="16_BIT",
    )
    octane_float_bit_depth: EnumProperty(
        name="Bit depth",
        description="Bit depth",
        items=octane_float_bit_depth_modes,
        default="16_BIT",
    )
    octane_exr_compression_modes = (
        ("UNCOMPRESSED", "Uncompressed", "no compression", 1),
        ("RLE_LOSSLESS", "RLE(lossless)", "run length encoding (lossless)", 2),
        ("ZIPS_LOSSLESS", "ZIPS(lossless)", "zlib compression, one scan line at a time (lossless)", 3),
        ("ZIP_LOSSLESS", "ZIP(lossless)", "zlib compression in blocks of 16 scan lines (lossless)(default)", 4),
        ("PIZ_LOSSLESS", "PIZ(lossless)", "piz-based wavelet compression (lossless)", 5),
        ("PXR24_LOSSY", "PXR24(lossy)", "lossy 24-bit float compression (lossy)", 6),
        ("B44_LOSSY", "B44(lossy)", "lossy 4-by-4 pixel block compression (lossy)", 7),
        ("B44A_LOSSY", "B44A(lossy)", "lossy 4-by-4 pixel block compression (lossy)", 8),
        ("DWAA_LOSSY", "DWAA(lossy)", "lossy DCT based compression in blocks of 32 scanlines", 9),
        ("DWAB_LOSSY", "DWAB(lossy)", "lossy DCT based compression in blocks of 256 scanlines", 10),
    )
    octane_exr_compression_mode: EnumProperty(
        name="Compression",
        description="EXR compression type",
        items=octane_exr_compression_modes,
        default="ZIP_LOSSLESS",
    )
    octane_deep_exr_compression_modes = (
        ("UNCOMPRESSED", "Uncompressed", "no compression", 1),
        ("RLE_LOSSLESS", "RLE(lossless)", "run length encoding (lossless)", 2),
        ("ZIPS_LOSSLESS", "ZIPS(lossless)", "zlib compression, one scan line at a time (lossless)(default)", 3),
    )
    octane_deep_exr_compression_mode: EnumProperty(
        name="Compression",
        description="Deep EXR compression type",
        items=octane_deep_exr_compression_modes,
        default="ZIPS_LOSSLESS",
    )
    octane_tiff_compression_modes = (
        ("TIFF_COMPRESSION_NO_COMPRESSION", "Uncompressed", "no compression", 1),
        ("TIFF_COMPRESSION_DEFLATE", "Zlib(deflate)", "zlib compression", 2),
        ("TIFF_COMPRESSION_LZW", "LZW", "lzw compression", 3),
        ("TIFF_COMPRESSION_PACK_BITS", "Packbits", "packbits compression", 4),
    )
    octane_tiff_compression_mode: EnumProperty(
        name="Compression",
        description="Compression type for TIFF file export",
        items=octane_tiff_compression_modes,
        default="TIFF_COMPRESSION_LZW",
    )
    exclude_default_beauty_passes: BoolProperty(
        name="Exclude Beauty",
        description="Exclude the default-added 'Beauty' pass when exporting files",
        default=False,
    )
    white_light_spectrum_modes = (
        ('D65', "D65", "D65", 1),
        ('Legacy/flat', "Legacy/flat", "Legacy/flat", 0),
    )
    white_light_spectrum: EnumProperty(
        name="White light spectrum",
        description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, "
                    "black body emitters). This determines the spectrum that will produce white (before white "
                    "balance) in the"
        "final image. Use D65 to adapt to a reasonable daylight 'white' color. Use Legacy/flat to preserve the "
        "appearance of old projects (spectral emitters will appear rather blue)",
        items=white_light_spectrum_modes,
        default='D65',
    )
    use_old_color_pipeline: BoolProperty(
        name="Use old color pipeline",
        description="Use the old behavior for converting colors to and from spectra and for applying white balance."
                    "Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut"
                    "will be"
                    "rendered inaccurately)",
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
        description="Maximal amount of photon gather samples per pixel between photon tracing passes. This is similar"
                    "to max. tile samples, but it also affects the quality of caustics rendered. Higher values give "
                    "more samples"
                    "per second at the expense of caustic quality",
        min=1, max=64,
        default=2,
    )
    exploration_strength: FloatProperty(
        name="Exploration strength",
        description="The higher this value, the more the photon sampling is influenced by which photons are actually "
                    "gathered",
        min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
        default=0.8,
        step=3,
        precision=3,
    )

    # LEGACY COMPATIBILITY
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


class AddPresetRenderPasses(AddPresetBase, Operator):
    """Add Octane Render Passes preset"""
    bl_idname = "render.octane_renderpasses_preset_add"
    bl_label = "Add Render Passes preset"
    preset_menu = "OCTANE_MT_renderpasses_presets"
    preset_defines = [
        "octane = bpy.context.view_layer.octane"
    ]
    preset_values = ["octane." + item
                     for item in OctaneRenderLayerPropertyGroup.PROPERTY_CONFIGS[consts.NodeType.NT_RENDER_PASSES]]
    preset_subdir = "octane/renderpasses_presets"


class AddPresetKernel(AddPresetBase, Operator):
    """Add Octane Kernel preset"""
    bl_idname = "render.octane_kernel_preset_add"
    bl_label = "Add Kernel preset"
    preset_menu = "OCTANE_MT_kernel_presets"
    preset_defines = [
        "octane = bpy.context.scene.octane"
    ]
    preset_values = [
        "octane.kernel_json_node_tree_helper",
    ]
    preset_subdir = "octane/kernel_presets"

    def pre_cb(self, context):
        scene = context.scene
        octane_scene = scene.octane
        node_tree = utility.find_active_kernel_node_tree(scene)
        octane_scene.kernel_json_node_tree_helper = utility.dump_json_node_tree(node_tree)


_CLASSES = [
    KernelNodeGraphPropertyGroup,
    RenderAOVNodeGraphPropertyGroup,
    CompositeNodeGraphPropertyGroup,
    OctaneAovOutputGroupNode,
    OctaneAovOutputGroupCollection,
    OctaneBakingLayerTransform,
    OctaneBakingLayerTransformCollection,
    OctaneAnimationSettingsPropertyGroup,
    OctaneGlobalRenderLayerPropertyGroup,
    OctaneRenderLayerPropertyGroup,
    OctaneRenderPropertyGroup,
    AddPresetRenderPasses,
    AddPresetKernel,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
