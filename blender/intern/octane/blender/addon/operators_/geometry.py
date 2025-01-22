# <pep8 compliant>

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from octane.utils import consts, utility


class OCTANE_OT_quick_add_octane_geometry(Operator):
    geometry_node_bl_idname = ""
    default_object_name = ""
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, _context):
        return True

    def execute(self, context):
        from octane.nodes.base_node_tree import NodeTreeHandler
        bpy.ops.mesh.primitive_cube_add()
        proxy_object = context.active_object
        proxy_object.name = "OctaneGeometry[%s]" % self.default_object_name
        proxy_object.display_type = "WIRE"
        material = bpy.data.materials.new(proxy_object.name + "_Material")
        material.use_nodes = True
        # noinspection PyProtectedMember
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


class OCTANE_OT_quick_add_octane_vectron(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Vectron® to the scene"""
    bl_idname = "octane.quick_add_octane_vectron"
    bl_label = "Vectron®"
    geometry_node_bl_idname = "OctaneVectron"
    default_object_name = "Vectron"


class OCTANE_OT_quick_add_octane_box(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Box to the scene"""
    bl_idname = "octane.quick_add_octane_box"
    bl_label = "Box"
    geometry_node_bl_idname = "OctaneSDFBox"
    default_object_name = "Box"


class OCTANE_OT_quick_add_octane_capsule(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Capsule to the scene"""
    bl_idname = "octane.quick_add_octane_capsule"
    bl_label = "Capsule"
    geometry_node_bl_idname = "OctaneSDFCapsule"
    default_object_name = "Capsule"


class OCTANE_OT_quick_add_octane_cylinder(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Cylinder to the scene"""
    bl_idname = "octane.quick_add_octane_cylinder"
    bl_label = "Cylinder"
    geometry_node_bl_idname = "OctaneSDFCylinder"
    default_object_name = "Cylinder"


class OCTANE_OT_quick_add_octane_prism(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Prism to the scene"""
    bl_idname = "octane.quick_add_octane_prism"
    bl_label = "Prism"
    geometry_node_bl_idname = "OctaneSDFPrism"
    default_object_name = "Prism"


class OCTANE_OT_quick_add_octane_sphere(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Sphere to the scene"""
    bl_idname = "octane.quick_add_octane_sphere"
    bl_label = "Sphere"
    geometry_node_bl_idname = "OctaneSDFSphere"
    default_object_name = "Sphere"


class OCTANE_OT_quick_add_octane_torus(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Torus to the scene"""
    bl_idname = "octane.quick_add_octane_torus"
    bl_label = "Torus"
    geometry_node_bl_idname = "OctaneSDFTorus"
    default_object_name = "Torus"


class OCTANE_OT_quick_add_octane_tube(OCTANE_OT_quick_add_octane_geometry):
    """Add an Octane Tube to the scene"""
    bl_idname = "octane.quick_add_octane_tube"
    bl_label = "Tube"
    geometry_node_bl_idname = "OctaneSDFTube"
    default_object_name = "Tube"


class OCTANE_OT_quick_add_octane_light(Operator):
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
        # Create a new object with our light datablock.
        light_object = bpy.data.objects.new(name=self.bl_label, object_data=light_data)
        # Link light object to the active collection of current viewlayer
        # so that it'll appear in the current scene.
        view_layer = context.view_layer
        view_layer.active_layer_collection.collection.objects.link(light_object)
        # Place light to a specified location.
        light_object.location = context.scene.cursor.location
        # And finally, select it and make it active.
        bpy.ops.object.select_all(action="DESELECT")
        light_object.select_set(True)
        view_layer.objects.active = light_object
        self.update_octane_light(light_data)
        return {"FINISHED"}


class OCTANE_OT_quick_add_octane_toon_point_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_toon_directional_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_directional_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_spot_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_area_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_sphere_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_mesh_light(OCTANE_OT_quick_add_octane_light):
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


class OCTANE_OT_quick_add_octane_analytical_light(OCTANE_OT_quick_add_octane_light):
    """Add an Octane Analytical Light to the scene"""
    bl_idname = "octane.quick_add_octane_analytical_light"
    bl_label = "Octane Analytical Light"
    light_typename = "SUN"
    bl_register = True
    bl_undo = False

    @classmethod
    def poll(cls, context):
        return True

    def update_octane_light(self, light_data):
        octane_light_data = light_data.octane
        octane_light_data.octane_directional_light_type = "Analytical"
        light_data.use_nodes = True


_CLASSES = [
    OCTANE_OT_quick_add_octane_vectron,
    OCTANE_OT_quick_add_octane_box,
    OCTANE_OT_quick_add_octane_capsule,
    OCTANE_OT_quick_add_octane_cylinder,
    OCTANE_OT_quick_add_octane_prism,
    OCTANE_OT_quick_add_octane_sphere,
    OCTANE_OT_quick_add_octane_torus,
    OCTANE_OT_quick_add_octane_tube,

    OCTANE_OT_quick_add_octane_toon_point_light,
    OCTANE_OT_quick_add_octane_toon_directional_light,
    OCTANE_OT_quick_add_octane_directional_light,
    OCTANE_OT_quick_add_octane_spot_light,
    OCTANE_OT_quick_add_octane_area_light,
    OCTANE_OT_quick_add_octane_sphere_light,
    OCTANE_OT_quick_add_octane_mesh_light,
    OCTANE_OT_quick_add_octane_analytical_light,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
