# <pep8 compliant>

from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, \
    FloatVectorProperty

import bpy
from bpy.utils import register_class, unregister_class
from octane.preferences import object_mesh_types
from octane.properties_.common import OctanePropertyGroup


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


class OctaneObjectPropertyGroup(OctanePropertyGroup):
    render_layer_id: IntProperty(
        name="Render layer ID",
        description="Render layer number for current object. Will use the layer number from blender built-in render "
                    "layer system if the value is 0",
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
    round_edge_visibility: BoolProperty(
        name="Round Edges Visibility",
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
    light_id_pass_9: BoolProperty(
        name="Pass 9",
        description="Pass 9",
        default=True,
    )
    light_id_pass_10: BoolProperty(
        name="Pass 10",
        description="Pass 10",
        default=True,
    )
    light_id_pass_11: BoolProperty(
        name="Pass 11",
        description="Pass 11",
        default=True,
    )
    light_id_pass_12: BoolProperty(
        name="Pass 12",
        description="Pass 12",
        default=True,
    )
    light_id_pass_13: BoolProperty(
        name="Pass 13",
        description="Pass 13",
        default=True,
    )
    light_id_pass_14: BoolProperty(
        name="Pass 14",
        description="Pass 14",
        default=True,
    )
    light_id_pass_15: BoolProperty(
        name="Pass 15",
        description="Pass 15",
        default=True,
    )
    light_id_pass_16: BoolProperty(
        name="Pass 16",
        description="Pass 16",
        default=True,
    )
    light_id_pass_17: BoolProperty(
        name="Pass 17",
        description="Pass 17",
        default=True,
    )
    light_id_pass_18: BoolProperty(
        name="Pass 18",
        description="Pass 18",
        default=True,
    )
    light_id_pass_19: BoolProperty(
        name="Pass 19",
        description="Pass 19",
        default=True,
    )
    light_id_pass_20: BoolProperty(
        name="Pass 20",
        description="Pass 20",
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
        description="Use deformation motion blur for this object\nWarning: \nAutosmooth or an object modifier that "
                    "changes mesh topology over time may not render deformation motion blur correctly",
        default=False,
    )
    motion_steps: IntProperty(
        name="Motion Steps",
        description="Control accuracy of motion blur, more steps gives more memory usage (actual number of steps is "
                    "2^(steps - 1))",
        min=1, soft_max=8,
        default=1,
    )
    object_mesh_type: EnumProperty(
        name="Object Type",
        description="Used for rendering speed optimization. See the manual",
        items=object_mesh_types,
        # default="Auto",
        default=bpy.context.preferences.addons["octane"].preferences.default_object_mesh_type,
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
    scatter_id_source_types = (
        ("Built-in", "Built-in", "Blender Built-in Instance ID(e.g. particle ID)", 0),
        ("Attribute", "GeoNode Attribute", "Instance Attribute defined in the GeoNodes", 1),
        ("Sequence", "Sequence", "An auto-generated list of sequential numbers", 2),
    )
    scatter_id_source_type: EnumProperty(
        name="Scatter ID source",
        description="Scatter ID source",
        items=scatter_id_source_types,
        default="Built-in"
    )
    scatter_id_source_instance_attribute: StringProperty(
        name="Instance Attribute Name",
        description="The name of the instance attribute defined in the GeoNodes",
        default="",
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


class OctaneLightPropertyGroup(bpy.types.PropertyGroup):
    octane_point_light_types = (
        ("Toon Point", "Toon Point", "Toon Point", 0),
        ("Sphere", "Sphere", "Sphere", 1),
        ("Analytical", "Analytical", "Analytical", 2),
    )
    octane_directional_light_types = (
        ("Toon Directional", "Toon Directional", "Toon Directional", 0),
        ("Directional", "Directional", "Directional", 1),
        ("Analytical", "Analytical", "Analytical", 2),
    )
    octane_analytical_light_types = (
        ("Quad", "Quad", "Quad", 0),
        ("Disk", "Disk", "Disk", 1),
        # ("Directional", "Directional", "Directional", 2),
        ("Sphere", "Sphere", "Sphere", 3),
        ("Tube", "Tube", "Tube", 4),
    )

    octane_point_light_type: EnumProperty(
        name="Used as Octane Point Light",
        description="Use this Light as Octane Toon Point Light or Sphere Light",
        items=octane_point_light_types,
        default="Toon Point",
    )
    octane_directional_light_type: EnumProperty(
        name="Used as Octane Directional Light",
        description="Use this Light as Octane Toon Directional Light or Directional Light",
        items=octane_directional_light_types,
        default="Toon Directional",
    )
    octane_analytical_light_type: EnumProperty(
        name="Octane Analytical Light",
        description="Use this Light as Octane Analytical Light",
        items=octane_analytical_light_types,
        default="Quad",
    )
    used_as_octane_mesh_light: BoolProperty(
        name="Used as Octane Mesh Light",
        description="Use this Light as Octane Mesh Light",
        default=False,
    )
    light_mesh_object: PointerProperty(
        name="Light Object",
        description="Use this object's mesh with octane emission",
        type=bpy.types.Object,
        poll=lambda self, obj: obj.type == "MESH",
    )
    light_mesh: PointerProperty(
        name="Light Mesh",
        description="Use this mesh with octane emission",
        type=bpy.types.Mesh,
    )
    use_external_mesh: BoolProperty(
        name="Use External Mesh",
        description="",
        default=False,
    )
    external_mesh_file: StringProperty(
        name="External Obj File",
        description="Use external mesh with octane emission",
        default='',
        subtype='FILE_PATH',
    )

    @classmethod
    def register(cls):
        bpy.types.Light.octane = PointerProperty(
            name="Octane Light Settings",
            description="Octane Light settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Light.octane


_CLASSES = [
    OctaneObjectPropertyGroup,
    OctaneLightPropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
