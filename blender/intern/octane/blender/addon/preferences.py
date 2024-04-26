# <pep8 compliant>

from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    StringProperty,
    CollectionProperty
)

import bpy
from octane.core.client import OctaneBlender
from octane.utils import logger, ocio, runtime_globals, utility

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

object_mesh_types = (
    ("Global", "Global", "During scene translation, all Meshes with this type collapse into one common Mesh. This "
                         "increases the rendering speed, but the translation time is much slower and GPU memory usage "
                         "is much higher. Use this mode if you render a heavy interior scene as a still image. If you "
                         "have enough GPU memory to fit the entire scene as one common Mesh, it does not matter that "
                         "the translation time takes much longer because rendering the image may case take hours. You "
                         "an save time by using Global meshes in heavy still images, as the rendering speed is much "
                         "faster if the scene is used as one common Mesh. The Viewport refreshes slower if you have a "
                         "lot of Global meshes in scene", 0),
    ("Scatter", "Scatter", "Octane reloads Geometry objects with the Scatter type. This increases the scene "
                           "translation speed and decreases GPU memory usage", 1),
    ("Movable proxy", "Movable proxy", "Similar to Scatter, but only the geometry types with Movable Proxy are "
                                       "re-translated and reloaded into OctaneServer for every frame when you render "
                                       "an animation sequence", 2),
    ("Reshapable proxy", "Reshapable proxy", "Octane reloads the full Mesh and evaluates every frame. This is useful "
                                             "for deforming mesh types like fluids", 3),
    ("Auto", "Scatter/Movable", "Previously named Auto (Experimental), this option can manage both Scatter or Movable "
                                "(animated on transformations only, not deformed) meshes. This option will "
                                "re-translate objects with this type specified for every frame when rendering an "
                                "animation sequence", 4),
)

intermediate_color_space_types = (
    ('Linear sRGB', 'Linear sRGB', "Linear sRGB", 2),
    ('ACES2065-1', 'ACES2065-1', "ACES2065-1", 3),
)

imager_panel_modes = (
    ("Global", "Global", "Use a 'Global Imager Panel' for all cases. We recommend using this one unless you need "
                         "multiple different imagers in the scenes", 0),
    ("Multiple", "Multiple", "Enable multiple Imager panels for viewport and cameras. For backward compatibility, "
                             "it's the default option", 1),
)

postprocess_panel_modes = (
    ("Global", "Global", "Use a 'Global PostProcess Panel' for all cases. We recommend using this one unless you need "
                         "multiple different postprocesses in the scenes", 0),
    ("Multiple", "Multiple", "Enable multiple PostProcess panels for viewport and cameras. For backward "
                             "compatibility, it's the default option", 1),
)


def update_octane_localdb_path():
    if utility.is_exclusive_addon_mode():
        return
    try:
        preferences = utility.get_preferences()
        octane_localdb_path = utility.resolve_octane_format_path(str(preferences.octane_localdb_path))
    except Exception as e:
        octane_localdb_path = ""
        logger.exception(e)
    import _octane
    _octane.update_octane_localdb(octane_localdb_path)


def update_octane_texture_cache_path():
    if utility.is_exclusive_addon_mode():
        return
    try:
        preferences = utility.get_preferences()
        octane_texture_cache_path = utility.resolve_octane_format_path(str(preferences.octane_texture_cache_path))
    except Exception as e:
        octane_texture_cache_path = ""
        logger.exception(e)
    import _octane
    _octane.update_octane_texture_cache(octane_texture_cache_path)


def update_octane_server_address():
    if utility.is_exclusive_addon_mode():
        return
    try:
        preferences = utility.get_preferences()
        octane_server_address = str(preferences.octane_server_address)
        enable_release_octane_license_when_exiting = bool(preferences.enable_relese_octane_license_when_exiting)
    except Exception as e:
        octane_server_address = ""
        enable_release_octane_license_when_exiting = False
        logger.exception(e)
    import _octane
    _octane.update_octane_server_address(octane_server_address, enable_release_octane_license_when_exiting)


def update_octane_params():
    if utility.is_exclusive_addon_mode():
        return
    try:
        preferences = utility.get_preferences()
        default_material_id = int(preferences.default_material_id)
    except Exception as e:
        default_material_id = 0
        logger.exception(e)
    import _octane
    _octane.set_octane_params(default_material_id)


def update_octane_preferences():
    update_octane_localdb_path()
    update_octane_texture_cache_path()
    update_octane_server_address()
    update_octane_params()


class OctaneOCIOConfigName(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Octane OCIO Config Name")


class OctanePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    use_new_addon_nodes: BoolProperty(
        name="Experience the New Image and Ramp Nodes",
        description="Use the new addon style image and ramp nodes(reboot blender to take effect)",
        default=True,
    )
    copy_node_value_for_materials: BoolProperty(
        name="Material",
        description="When changing to a new type of node, try to copy the values from the previous node",
        default=True,
    )
    copy_node_value_for_worlds: BoolProperty(
        name="World",
        description="When changing to a new type of node, try to copy the values from the previous node",
        default=True,
    )
    copy_node_value_for_kernels: BoolProperty(
        name="Kernel",
        description="When changing to a new type of node, try to copy the values from the previous node",
        default=False,
    )
    copy_node_value_for_render_aov: BoolProperty(
        name="Render AOV",
        description="When changing to a new type of node, try to copy the values from the previous node",
        default=True,
    )
    copy_node_value_for_compositor: BoolProperty(
        name="Compositor",
        description="When changing to a new type of node, try to copy the values from the previous node",
        default=True,
    )
    default_object_mesh_type: EnumProperty(
        name="Default Object Mesh Type",
        description="Object mesh type to use for default (Used for rendering speed optimization. See the manual.)("
                    "reboot Blender to take effect)",
        items=object_mesh_types,
        default="Auto",
    )
    default_material_id: EnumProperty(
        name="Default Material Type",
        description="Material to use for default (rendering with Octane)(reboot blender to take effect)",
        items=default_material_orders,
        default="7",  # Universal
    )
    default_use_blender_builtin_render_layer: BoolProperty(
        name="Use Blender Built-in Render Layer",
        description="Whether to use blender built-in render layer system for default(reboot blender to take effect)",
        default=False,
    )
    imager_panel_mode: EnumProperty(
        name="Imager Property Panel Style",
        description="The style of Imager Property Panel. We recommend 'Global' unless you want to use multiple imager "
                    "configurations for viewport and cameras(reboot Blender to take effect)",
        items=imager_panel_modes,
        default="Multiple",
    )
    postprocess_panel_mode: EnumProperty(
        name="PostProcess Property Panel Style",
        description="The style of PostProcess Property Panel. We recommend 'Global' unless you want to use multiple "
                    "postprocess configurations for viewport and cameras(reboot Blender to take effect)",
        items=postprocess_panel_modes,
        default="Multiple",
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
        description="Do not regenerate & upload meshes(except reshapable ones) which are already cached",
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
    # noinspection SpellCheckingInspection
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

    use_factor_subtype_for_property: BoolProperty(
        name="Use 'Factor' subtype for properties",
        description="Use 'Factor' subtype for properties if possible(like Cycles). Or, do not use subtype for "
                    "properties(reboot blender to take effect)",
        default=True,
    )

    use_octane_default_color_management: BoolProperty(
        name="Use Octane default color management",
        description="For newly-created scenes, OctaneBlender will overwrite the Blender's built-in color management "
                    "to no-op(don't do anything, by setting 'Display Device' to 'sRGB' and 'View Transform' to 'Raw')",
        default=False,
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
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the "
                    "same color space as the 'OCIO' box",
        items=intermediate_color_space_types,
        default='Linear sRGB',
        update=ocio.update_ocio_info,
    )
    ocio_intermediate_color_space_ocio: StringProperty(
        name="Manual(OCIO)",
        description="Choose intermediate color space to allow conversions with OCIO. This should correspond to the"
                    "same color space as the 'Octane' box",
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
        description="On Windows, Octane can now send back shared surface handles for render passes instead of just "
                    "buffers, which makes viewport rendering faster.\nFor multiple-GPUs platforms, Octane may"
                    "change the 'Imaging' device during the viewport rendering. These changes are temporary and they "
                    "will be reverted back after the viewport rendering",
        default=True,
    )
    min_viewport_update_interval: FloatProperty(
        name="Min Viewport Update Interval(seconds)",
        description="The minimum interval for the viewport update. Basically, smaller update interval produces a "
                    "smoother Viewport rendering unless the performance hits the bottleneck",
        default=0.04,
        min=0.01, max=10.0,
    )

    def draw(self, _context):
        if utility.is_addon_mode():
            layout = self.layout
            box = layout.box()
            box.label(text="General")
            box.row().prop(self, "default_object_mesh_type", expand=False)
            box = layout.box()
            box.label(text="Viewport Rendering")
            row = box.row()
            row.prop(self, "min_viewport_update_interval")
            row = box.row()
            row.active = OctaneBlender().is_shared_surface_supported()
            row.prop(self, "use_shared_surface")
            if not row.active:
                box.row().label(text="Shared surface is not supported")
        else:
            layout = self.layout
            layout.row().prop(self, "octane_server_address", expand=False)
            # noinspection SpellCheckingInspection
            layout.row().prop(self, "enable_relese_octane_license_when_exiting", expand=False)
            layout.row().prop(self, "octane_localdb_path", expand=False)
            layout.row().prop(self, "default_object_mesh_type", expand=False)
            layout.row().prop(self, "octane_texture_cache_path", expand=False)
            layout.row().prop(self, "default_material_id", expand=False)
            box = layout.box()
            box.label(text="Viewport Rendering")
            row = box.row()
            row.active = OctaneBlender().is_shared_surface_supported()
            row.prop(self, "use_shared_surface")
            if not row.active:
                box.row().label(text="Shared surface is not supported")
        box = layout.box()
        box.label(text="User Interface")
        box.row().prop(self, "use_factor_subtype_for_property")
        box.row().prop(self, "imager_panel_mode")
        box.row().prop(self, "postprocess_panel_mode")
        box = layout.box()
        box.label(text="Node Graph")
        row = box.row()
        split = row.split(factor=0.35)
        split.use_property_split = False
        split.label(text="Copy Properties When Changing Node Type")
        row = split.row(align=True)
        row.prop(self, "copy_node_value_for_materials", text="Material", toggle=True)
        row.prop(self, "copy_node_value_for_worlds", text="World", toggle=True)
        row.prop(self, "copy_node_value_for_kernels", text="Kernel", toggle=True)
        row.prop(self, "copy_node_value_for_render_aov", text="RenderAOV", toggle=True)
        row.prop(self, "copy_node_value_for_compositor", text="Compositor", toggle=True)
        box = layout.box()
        box.label(text="Color Management")
        box.row().prop(self, "use_octane_default_color_management")
        box.row().prop(self, "ocio_use_other_config_file")
        box.row().prop(self, "ocio_config_file_path")
        box.row().prop(self, "ocio_use_automatic")
        row = box.row()
        row.active = not self.ocio_use_automatic
        row.prop(self, "ocio_intermediate_color_space_octane")
        row = box.row()
        row.active = not self.ocio_use_automatic
        row.prop_search(self, "ocio_intermediate_color_space_ocio", self, "ocio_intermediate_color_space_configs")
        update_octane_preferences()


classes = (
    OctaneOCIOConfigName,
    OctanePreferences,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    preferences = utility.get_preferences()
    runtime_globals.update_from_preferences(preferences)
    update_octane_preferences()


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
