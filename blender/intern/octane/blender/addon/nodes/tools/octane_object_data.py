# <pep8 compliant>

import math

import mathutils
from bpy.props import EnumProperty, StringProperty, IntProperty

import bpy
import octane
from octane.nodes.base_node import OctaneBaseNode
from octane.utils import utility, consts, octane_name


class OctaneObjectData(bpy.types.Node, OctaneBaseNode):
    TRANSFORM_OUT = "Transform out"
    ROTATION_OUT = "Rotation out"
    GEOMETRY_OUT = "Geometry out"
    TRANSFORMED_GEO_OUT = "Transformed Geo out"

    bl_idname = "OctaneObjectData"
    bl_label = "Object Data"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_BLENDER_NODE_OBJECT_DATA
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    def update_source_type(self, context):
        is_collection_mode = self.source_type == "Collection"
        self.outputs[self.TRANSFORM_OUT].hide = is_collection_mode
        self.outputs[self.ROTATION_OUT].hide = is_collection_mode
        self.update_node_tree(context)

    items = [
        ("Object", "Object", "Use an individual object as data source", 0),
        ("Collection", "Collection", "Use an entire collection as data source", 1),
    ]
    source_type: EnumProperty(name="Source type", default="Object", update=update_source_type,
                              description="Determines the data source type(object or collection)", items=items)
    primitive_coordinate_modes = [
        ("Blender", "Blender", "", 0),
        ("Octane", "Octane", "", 1),
    ]
    target_primitive_coordinate_mode: EnumProperty(name="Target coordinate", default="Blender",
                                                   update=OctaneBaseNode.update_node_tree,
                                                   description="Determines the coordinate mode of the target's primitive data",
                                                   items=primitive_coordinate_modes)
    object_ptr: bpy.props.PointerProperty(type=bpy.types.Object, name="Object", update=OctaneBaseNode.update_node_tree)
    collection_ptr: bpy.props.PointerProperty(type=bpy.types.Collection, name="Collection",
                                              update=OctaneBaseNode.update_node_tree)
    # Replaced by the above Pointer properties since 27.9
    object_name: StringProperty(name="Object name")
    collection_name: StringProperty(name="Collection name")

    def use_multiple_outputs(self):
        return True

    def init(self, _context):
        self.outputs.new("OctaneTransformOutSocket", self.TRANSFORM_OUT).init()
        self.outputs.new("OctaneFloatOutSocket", self.ROTATION_OUT).init()
        self.outputs.new("OctaneGeometryOutSocket", self.GEOMETRY_OUT).init()
        self.outputs.new("OctaneGeometryOutSocket", self.TRANSFORMED_GEO_OUT).init()

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "target_primitive_coordinate_mode", expand=True)
        row = layout.row()
        row.prop(self, "source_type", expand=True)
        row = layout.row()
        if self.source_type == "Object":
            row.prop(self, "object_ptr")
        else:
            row.prop(self, "collection_ptr")
        # if self.source_type == "Object":            
        #     row.prop_search(self, "object_name", bpy.data, "objects")            
        # else:
        #     row.prop_search(self, "collection_name", bpy.data, "collections")

    def get_blender_attribute_name(self, node_name, attribute_name):
        return node_name + consts.DERIVED_NODE_SEPARATOR + attribute_name

    def get_blender_pin_symbol(self, node_name, pin_symbol):
        return node_name + consts.DERIVED_NODE_SEPARATOR + pin_symbol

    def get_octane_matrix(self, matrix, octane_graph_node_data, is_rotation_out=False):
        matrix = utility.OctaneMatrixConvertor.get_octane_matrix(matrix)
        is_light_nodetree = (getattr(octane_graph_node_data, "owner_type",
                                     consts.OctaneNodeTreeIDName.MATERIAL) == consts.OctaneNodeTreeIDName.LIGHT)
        if is_light_nodetree and not is_rotation_out:
            matrix = matrix @ mathutils.Matrix.Rotation(math.radians(-90), 4, "Y")
        else:
            if self.target_primitive_coordinate_mode == "Octane":
                matrix = matrix @ mathutils.Matrix.Rotation(math.radians(90), 4, "X")
        return matrix

    def sync_geometry_data(self, object_eval, name, octane_node, octane_graph_node_data, depsgraph, need_transform):
        # Placement node
        placement_node_name = name
        placement_subnode = octane_node.get_subnode(placement_node_name, consts.NodeType.NT_GEO_PLACEMENT)
        transform_node_name = ""
        octane_geometry_name = ""
        if object_eval is not None:
            scene_eval = depsgraph.scene_eval
            is_viewport = depsgraph.mode == "VIEWPORT"
            active_engine = octane.get_active_render_engine()
            if getattr(active_engine, "session", None) is not None:
                session = active_engine.session
                if object_eval.name in session.object_cache.object_name_to_scatter_node_name_map:
                    octane_geometry_name = session.object_cache.object_name_to_scatter_node_name_map[object_eval.name]
                    octane_geometry_name = octane_name.resolve_objectlayer_map_octane_name(octane_geometry_name)
            if need_transform:
                # Transform node
                transform_node_name = placement_node_name + "_Transform"
                transform_subnode = octane_node.get_subnode(transform_node_name, consts.NodeType.NT_TRANSFORM_VALUE)
                matrix = self.get_octane_matrix(object_eval.matrix_world, octane_graph_node_data)
                transform_subnode.set_attribute_id(consts.AttributeID.A_TRANSFORM, matrix)
        placement_subnode.set_pin_id(consts.PinID.P_GEOMETRY, True, octane_geometry_name, "")
        placement_subnode.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, "")

    def sync_collection_data(self, collection, name, octane_node, depsgraph, octane_graph_node_data, need_transform):
        # Geometry Group node
        geometry_group_node_name = name
        geometry_group_subnode = octane_node.get_subnode(geometry_group_node_name, consts.NodeType.NT_GEO_GROUP)
        geometry_count = 0
        if collection is not None:
            for obj in collection.all_objects:
                if obj.type != "MESH":
                    continue
                mesh_name = geometry_group_node_name + "_" + str(geometry_count)
                pin_name = "Input " + str(geometry_count + 1)
                geometry_group_subnode.set_pin_index(geometry_count, pin_name, consts.SocketType.ST_LINK,
                                                     consts.PinType.PT_GEOMETRY, 0, True, mesh_name, "")
                self.sync_geometry_data(obj, mesh_name, octane_node, depsgraph, octane_graph_node_data, need_transform)
                geometry_count += 1
        geometry_group_subnode.set_attribute_id(consts.AttributeID.A_PIN_COUNT, geometry_count)

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        octane_node_name = octane_node.name
        _object = self.object_ptr
        object_eval = _object.evaluated_get(depsgraph) if _object is not None else None
        collection = self.collection_ptr
        if octane_node_name.endswith(self.TRANSFORM_OUT):
            if object_eval is not None:
                subnode_name = octane_node_name
                matrix = self.get_octane_matrix(object_eval.matrix_world, octane_graph_node_data)
                subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_TRANSFORM_VALUE)
                subnode.set_attribute_id(consts.AttributeID.A_TRANSFORM, matrix)
        elif octane_node_name.endswith(self.ROTATION_OUT):
            if object_eval is not None:
                subnode_name = octane_node_name
                matrix = self.get_octane_matrix(object_eval.matrix_world, octane_graph_node_data, True)
                direction = utility.OctaneMatrixConvertor.get_octane_direction(matrix)
                subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_FLOAT)
                subnode.set_attribute_id(consts.AttributeID.A_VALUE, direction)
        elif octane_node_name.endswith(self.GEOMETRY_OUT):
            if self.source_type == "Object":
                self.sync_geometry_data(object_eval, octane_node.name, octane_node, octane_graph_node_data, depsgraph,
                                        False)
            else:
                self.sync_collection_data(collection, octane_node.name, octane_node, octane_graph_node_data, depsgraph,
                                          False)
        elif octane_node_name.endswith(self.TRANSFORMED_GEO_OUT):
            if self.source_type == "Object":
                self.sync_geometry_data(object_eval, octane_node.name, octane_node, octane_graph_node_data, depsgraph,
                                        True)
            else:
                self.sync_collection_data(collection, octane_node.name, octane_node, octane_graph_node_data, depsgraph,
                                          True)

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        if legacy_node.source_type == "OBJECT":
            self.source_type = "Object"
        else:
            self.source_type = "Collection"
        if legacy_node.inputs["Object"].default_value is not None:
            object_name = legacy_node.inputs["Object"].default_value.name
            self.object_ptr = bpy.data.objects.get(object_name, None)
        else:
            self.object_ptr = None
        if legacy_node.inputs["Collection"].default_value is not None:
            collection_name = legacy_node.inputs["Collection"].default_value.name
            self.collection_ptr = bpy.data.collections.get(collection_name, None)
        else:
            self.collection_ptr = None
        outputs_mapping = {
            "OutTransform": "Transform out",
            "OutRotation": "Rotation out",
            "OutGeo": "Geometry out",
            "OutTransformedGeo": "Transformed Geo out",
        }
        for legacy_output_name, current_output_name in outputs_mapping.items():
            for link in legacy_node.outputs[legacy_output_name].links:
                node_tree.links.new(self.outputs[current_output_name], link.to_socket)

    def get_target_object_name(self):
        if self.source_type == "Object":
            return self.object_ptr.name if self.object_ptr is not None else ""
        return ""

    def get_target_object_id(self):
        if self.source_type == "Object":
            return self.object_ptr
        return None


_CLASSES = [
    OctaneObjectData,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))
