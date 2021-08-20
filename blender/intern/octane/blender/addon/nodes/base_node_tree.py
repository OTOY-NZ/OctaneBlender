import bpy
from bpy.app.handlers import persistent
from bpy.props import StringProperty
from ..utils import consts


class OctaneBaseNodeTree(object):
    USE_LEGACY_NODE=True
    LEGACY_OUTPUT_SOCKET_CONVERSION_MAP={
        "OutGeo": consts.PinType.PT_GEOMETRY,
        "OutTex": consts.PinType.PT_UNKNOWN, # (consts.PinType.PT_TEXTURE, consts.PinType.PT_TOON_RAMP),
        "OutMat": consts.PinType.PT_MATERIAL,
        "OutMatLayer": consts.PinType.PT_MATERIAL_LAYER,
        "OutMedium": consts.PinType.PT_MEDIUM,
        "OutRotation": consts.PinType.PT_UNKNOWN, # (consts.PinType.PT_TRANSFORM, consts.PinType.PT_FLOAT),
        "OutTransform": consts.PinType.PT_TRANSFORM,
        "OutProjection": consts.PinType.PT_PROJECTION,
        "OutAOV": consts.PinType.PT_OUTPUT_AOV,
        "OutLayer": consts.PinType.PT_COMPOSITE_AOV_LAYER,
    }

    active_output_name: StringProperty(name="Active Output Name", default="")

    @property
    def active_output_node(self):
        if len(self.active_output_name):
            return self.nodes.get(self.active_output_name)
        return None

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == consts.ENGINE_NAME

    def update_active_output_name(self, context, name, active):
        from .base_node import OctaneBaseOutputNode
        if active:
            for node in self.nodes:
                if node.name != name and isinstance(node, OctaneBaseOutputNode):
                    if node.active:
                        node.set_active(context, False)
            self.active_output_name = name
        else:
            if name == self.active_output_name:
                self.active_output_name = ""    

    def update(self):
        # This is a workaround to solve the link validation issue
        # https://blender.stackexchange.com/questions/153489/custom-nodes-how-to-validate-a-link        
        bpy.app.timers.register(self.update_post)

    def update_post(self):
        self.update_link_validity(self)   
    
    # Ensure the viewport update
    def update_viewport(self):
        self.update_tag()        

    @staticmethod
    def resovle_socket_octane_pin_type(node_tree, socket):
        socket_pin_type = getattr(socket, "octane_pin_type", consts.PinType.PT_UNKNOWN)
        if getattr(node_tree, "USE_LEGACY_NODE", True):
            if socket_pin_type == consts.PinType.PT_UNKNOWN:
                socket_name = getattr(socket, "name", "")
                if socket_name in OctaneBaseNodeTree.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP:
                    socket_pin_type = OctaneBaseNodeTree.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP[socket_name]
        return socket_pin_type

    @staticmethod
    def update_link_validity(node_tree):
        for link in node_tree.links:
            from_socket = link.from_socket
            to_socket = link.to_socket
            if from_socket and to_socket:
                from_socket_pin_type = OctaneBaseNodeTree.resovle_socket_octane_pin_type(node_tree, from_socket)
                to_socket_pin_type = OctaneBaseNodeTree.resovle_socket_octane_pin_type(node_tree, to_socket)
                if from_socket_pin_type == consts.PinType.PT_UNKNOWN:
                    continue
                if to_socket_pin_type == consts.PinType.PT_UNKNOWN:
                    continue                
                if from_socket_pin_type != to_socket_pin_type:
                    link.is_valid = False


class NodeTreeHandler:
    material_node_tree_count = 0
    world_node_tree_count = 0
    MATERIAL_OUTPUT_NODE_NAME = "Material Output"
    WORLD_OUTPUT_NODE_NAME = "World Output"
    SURFACE_INPUT_NAME = "Surface"
    VOLUME_INPUT_NAME = "Volume"
    WORLD_INPUT_NAME = "Surface"
    OCTANE_WORLD_INPUT_NAME = "Octane Environment"

    @staticmethod
    def on_file_load(scene):
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)

    @staticmethod
    def convert_to_octane_node(node_tree, output_node, socket_name, octane_node_type, octane_node_output_name=None):
        _input = output_node.inputs[socket_name]
        if len(_input.links):            
            from_node = _input.links[0].from_node
            octane_node = node_tree.nodes.new(octane_node_type)
            octane_node.location = from_node.location
            octane_output_socket = None
            if octane_node_output_name is None:
                octane_output_socket = octane_node.outputs[0]
            else:
                octane_output_socket = octane_node.outputs[octane_node_output_name]
            node_tree.links.new(octane_output_socket, _input)
            node_tree.nodes.remove(from_node)

    @staticmethod
    def on_material_new(scene):
        if len(bpy.data.materials) > NodeTreeHandler.material_node_tree_count:            
            active_object = bpy.context.active_object
            active_material = None
            node_tree = None
            if active_object:
                active_material = active_object.active_material
            if active_material and active_material.use_nodes:
                node_tree = active_material.node_tree
            if node_tree and NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME in node_tree.nodes:
                output = node_tree.nodes[NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME]
                NodeTreeHandler.convert_to_octane_node(node_tree, output, NodeTreeHandler.SURFACE_INPUT_NAME, "OctaneUniversalMaterial")
                NodeTreeHandler.convert_to_octane_node(node_tree, output, NodeTreeHandler.VOLUME_INPUT_NAME, "OctaneAbsorption")                    
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        
    @staticmethod
    def on_world_new(scene):
        if len(bpy.data.worlds) > NodeTreeHandler.world_node_tree_count:
            active_world = scene.world
            node_tree = None
            if active_world and active_world.use_nodes:
                node_tree = active_world.node_tree
            if node_tree and NodeTreeHandler.WORLD_OUTPUT_NODE_NAME in node_tree.nodes:
                output = node_tree.nodes[NodeTreeHandler.WORLD_OUTPUT_NODE_NAME]
                NodeTreeHandler.convert_to_octane_node(node_tree, output, NodeTreeHandler.WORLD_INPUT_NAME, "OctaneDaylightEnvironment")
                NodeTreeHandler.convert_to_octane_node(node_tree, output, NodeTreeHandler.OCTANE_WORLD_INPUT_NAME, "OctaneDaylightEnvironment")
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)

    @staticmethod
    def blender_internal_node_tree_update_handler(scene, depsgraph=None):
        NodeTreeHandler.on_material_new(scene)
        NodeTreeHandler.on_world_new(scene)
        if depsgraph is None:
            depsgraph = bpy.context.evaluated_depsgraph_get()
        for update in depsgraph.updates:
            if not update.is_updated_shading:
                continue
            if bpy.context.active_object and \
                bpy.context.active_object.active_material and \
                bpy.context.active_object.active_material.use_nodes:            
                OctaneBaseNodeTree.update_link_validity(bpy.context.active_object.active_material.node_tree)
            if scene.world and scene.world.use_nodes:
                OctaneBaseNodeTree.update_link_validity(scene.world.node_tree)


@persistent
def node_tree_initialization_handler(scene):
    if scene is None:
        scene = bpy.context.scene
    if scene.render.engine != consts.ENGINE_NAME:
        return
    NodeTreeHandler.on_file_load(scene)

@persistent
def node_tree_update_handler(scene):
    if scene is None:
        scene = bpy.context.scene
    if scene.render.engine != consts.ENGINE_NAME:
        return
    NodeTreeHandler.blender_internal_node_tree_update_handler(scene)


def register():
    bpy.app.handlers.load_post.append(node_tree_initialization_handler)
    bpy.app.handlers.depsgraph_update_post.append(node_tree_update_handler)
    

def unregister():
    bpy.app.handlers.load_post.remove(node_tree_initialization_handler)
    bpy.app.handlers.depsgraph_update_post.remove(node_tree_update_handler)
