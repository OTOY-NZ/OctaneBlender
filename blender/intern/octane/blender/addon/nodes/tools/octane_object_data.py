import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneObjectData(bpy.types.Node, OctaneBaseNode):
    TRANSFORM_OUT = "Transform out"
    ROTATION_OUT = "Rotation out"
    GEOMETRY_OUT = "Geometry out"
    TRANSFORMED_GEO_OUT = "Transformed Geo out"
    # Transform
    NT_TRANSFORM_VALUE = "67"
    A_TRANSFORM = "a_transform"
    # Rotation
    NT_FLOAT = "6"
    A_VALUE = "a_value"
    # Geometry
    NT_GEO_PLACEMENT = "4"
    P_GEOMETRY = "59"
    P_TRANSFORM = "243"
    # Collection
    NT_GEO_GROUP = "3"
    A_PIN_COUNT = "a_pin_count"

    bl_idname="OctaneObjectData"
    bl_label="Object Data"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NodeType.NT_BLENDER_NODE_OBJECT_DATA)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)

    def update_source_type(self, context):
        is_collection_mode = self.source_type == "Collection"
        self.outputs[self.TRANSFORM_OUT].hide = is_collection_mode
        self.outputs[self.ROTATION_OUT].hide = is_collection_mode           

    items = [
        ("Object", "Object", "Use an individual object as data source", 0),
        ("Collection", "Collection", "Use an entire collection as data source", 1),
    ]
    source_type: EnumProperty(name="Source type", default="Object", update=update_source_type, description="Determines the data source type(object or collection)", items=items) 
    object_name: StringProperty(name="Object name")
    collection_name: StringProperty(name="Collection name")    

    def use_mulitple_outputs(self):
        return True

    def init(self, context):
        self.outputs.new("OctaneTransformOutSocket", self.TRANSFORM_OUT).init()
        self.outputs.new("OctaneFloatOutSocket", self.ROTATION_OUT).init()
        self.outputs.new("OctaneGeometryOutSocket", self.GEOMETRY_OUT).init()
        self.outputs.new("OctaneGeometryOutSocket", self.TRANSFORMED_GEO_OUT).init()

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "source_type", expand=True)
        row = layout.row()
        if self.source_type == "Object":            
            row.prop_search(self, "object_name", bpy.data, "objects")
        else:
            row.prop_search(self, "collection_name", bpy.data, "collections")

    def get_target_object_name(self):
        if self.source_type == "Object":
            return self.object_name
        return ""

    def get_target_collection_name(self):
        if self.source_type == "Collection":
            return self.collection_name
        return ""        

    def get_blender_attribute_name(self, node_name, attribute_name):
        return node_name + consts.DERIVED_NODE_SEPARATOR + attribute_name

    def get_blender_pin_symbol(self, node_name, pin_symbol):
        return node_name + consts.DERIVED_NODE_SEPARATOR + pin_symbol

    def sync_geometry_data(self, obj, name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, need_transform):
        if obj is None:
            return
        # Placement node
        placement_node_name = name
        derived_node_names.append(placement_node_name)
        derived_node_types.append(self.NT_GEO_PLACEMENT)                    
        octane_mesh_name = utility.resolve_mesh_octane_name(obj, scene, is_viewport)
        pin_symbol = self.get_blender_pin_symbol(placement_node_name, self.P_GEOMETRY)
        octane_node.set_blender_pin(pin_symbol, "Geometry", consts.SocketType.ST_LINK, "", True, octane_mesh_name)
        if not need_transform:
            return
        # Placement node, transform node link
        transform_node_name = placement_node_name + "_Transform"
        pin_symbol = self.get_blender_pin_symbol(placement_node_name, self.P_TRANSFORM)
        octane_node.set_blender_pin(pin_symbol, "Transform", consts.SocketType.ST_LINK, "", True, transform_node_name)
        # Transform node
        derived_node_names.append(transform_node_name)
        derived_node_types.append(self.NT_TRANSFORM_VALUE)
        matrix = utility.OctaneMatrixConvertor.get_octane_matrix(obj.matrix_world)
        blender_attribute_name = self.get_blender_attribute_name(transform_node_name, self.A_TRANSFORM)
        octane_node.set_blender_attribute(blender_attribute_name, consts.AttributeType.AT_MATRIX, matrix)
        
    def sync_collection_data(self, collection, name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, need_transform):
        if collection is None:
            return
        # Geometry Group node
        geometry_group_node_name = name
        derived_node_names.append(geometry_group_node_name)
        derived_node_types.append(self.NT_GEO_GROUP)
        geometry_count = 0
        for obj in collection.all_objects:
            if obj.type != "MESH":
                continue
            mesh_name = geometry_group_node_name + "_" + str(geometry_count)
            pin_symbol = self.get_blender_pin_symbol(geometry_group_node_name, OctaneBaseSocket.DYNAMIC_PIN_INDEX + str(geometry_count))
            octane_node.set_blender_pin(pin_symbol, "Geometry", consts.SocketType.ST_LINK, "", True, mesh_name)
            self.sync_geometry_data(obj, mesh_name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, need_transform)
            geometry_count += 1
        blender_attribute_name = self.get_blender_attribute_name(geometry_group_node_name, self.A_PIN_COUNT)
        octane_node.set_blender_attribute(blender_attribute_name, consts.AttributeType.AT_INT, geometry_count)

    def sync_custom_data(self, octane_node, octane_graph_node_data, owner_type, scene, is_viewport):
        super().sync_custom_data(octane_node, octane_graph_node_data, owner_type, scene, is_viewport)
        octane_name = octane_node.name
        derived_node_names = []
        derived_node_types = []
        obj = bpy.data.objects.get(self.get_target_object_name(), None)
        collection = bpy.data.collections.get(self.get_target_collection_name(), None)
        if octane_name.endswith(self.TRANSFORM_OUT):
            if obj is not None:
                matrix = utility.OctaneMatrixConvertor.get_octane_matrix(obj.matrix_world)
                derived_node_names.append(octane_name)
                derived_node_types.append(self.NT_TRANSFORM_VALUE)
                blender_attribute_name = self.get_blender_attribute_name(octane_name, self.A_TRANSFORM)
                octane_node.set_blender_attribute(blender_attribute_name, consts.AttributeType.AT_MATRIX, matrix)
        elif octane_name.endswith(self.ROTATION_OUT):
            if obj is not None:
                direction = utility.OctaneMatrixConvertor.get_octane_direction(obj.matrix_world)
                derived_node_names.append(octane_name)
                derived_node_types.append(self.NT_FLOAT)
                blender_attribute_name = self.get_blender_attribute_name(octane_name, self.A_VALUE)
                octane_node.set_blender_attribute(blender_attribute_name, consts.AttributeType.AT_FLOAT3, direction)
        elif octane_name.endswith(self.GEOMETRY_OUT):
            if self.source_type == "Object":
                self.sync_geometry_data(obj, octane_node.name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, False)
            else:
                self.sync_collection_data(collection, octane_node.name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, False)
        elif octane_name.endswith(self.TRANSFORMED_GEO_OUT):
            if self.source_type == "Object":
                self.sync_geometry_data(obj, octane_node.name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, True)
            else:
                self.sync_collection_data(collection, octane_node.name, octane_node, scene, is_viewport, derived_node_names, derived_node_types, True)
        if len(derived_node_names):
            octane_node.set_blender_attribute(consts.DERIVED_NODE_NAMES, consts.AttributeType.AT_STRING, ";".join(derived_node_names))
            octane_node.set_blender_attribute(consts.DERIVED_NODE_TYPES, consts.AttributeType.AT_STRING, ";".join(derived_node_types))


_CLASSES=[
    OctaneObjectData,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))