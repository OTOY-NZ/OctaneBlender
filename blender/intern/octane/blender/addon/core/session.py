import bpy
import collections
from octane.utils import consts, utility
from octane.core.caches import OctaneNodeCache, ObjectCache, ImageCache, MaterialCache, WorldCache, CompositeCache, RenderAOVCache, KernelCache, OctaneRenderTargetCache
from octane.core.client import OctaneClient
from octane.core.octane_node import OctaneNode, OctaneNodeType
from octane.nodes.base_node import OctaneBaseNode


class RenderSession(object):

    def __init__(self):
        self.session_type = consts.SessionType.UNKNOWN
        self.octane_node_cache = OctaneNodeCache(self)
        self.object_cache = ObjectCache(self)
        self.image_cache = ImageCache(self)
        self.material_cache = MaterialCache(self)
        self.world_cache = WorldCache(self)
        self.composite_cache = CompositeCache(self)
        self.render_aov_cache = RenderAOVCache(self)
        self.kernel_cache = KernelCache(self)
        self.rendertarget_cache = OctaneRenderTargetCache(self)

    def __del__(self):
        self.clear()

    def clear(self):
        self.octane_node_cache = None
        self.object_cache = None
        self.image_cache = None        
        self.material_cache = None
        self.world_cache = None
        self.composite_cache = None
        self.kernel_cache = None
        self.rendertarget_cache = None

    def is_viewport(self):
        return self.session_type == consts.SessionType.VIEWPORT

    def is_final(self):
        return self.session_type == consts.SessionType.FINAL_RENDER

    def is_preview(self):
        return self.session_type == consts.SessionType.PREVIEW

    def is_export(self):
        return self.session_type == consts.SessionType.EXPORT

    def view_update(self, context, depsgraph):
        # check diff        
        self.object_cache.diff(context, depsgraph)                
        self.image_cache.diff(context, depsgraph)        
        self.material_cache.diff(context, depsgraph)
        self.world_cache.diff(context, depsgraph)
        self.composite_cache.diff(context, depsgraph)
        self.render_aov_cache.diff(context, depsgraph)
        self.kernel_cache.diff(context, depsgraph)
        # update
        if self.object_cache.need_update:
            self.object_cache.update(context, depsgraph)        
        if self.image_cache.need_update:
            self.image_cache.update(context, depsgraph)        
        if self.material_cache.need_update:
            self.material_cache.update(context, depsgraph)
        if self.world_cache.need_update:
            self.world_cache.update(context, depsgraph)
        if self.composite_cache.need_update:
            self.composite_cache.update(context, depsgraph)
        if self.render_aov_cache.need_update:
            self.render_aov_cache.update(context, depsgraph)
        if self.kernel_cache.need_update:
            self.kernel_cache.update(context, depsgraph)            
        # update render target
        if self.rendertarget_cache.diff(context, depsgraph):
            self.rendertarget_cache.update(context, depsgraph)            

    def _update_node_tree(self, context, node_tree, owner_type, active_output_node, active_input_name, root_name, node_tree_attributes):
        ancestor_list = [utility.OctaneGraphNodeDummy(root_name), ]
        # nodes to process [OctaneGraphNode...]
        queue = collections.deque()
        queue.append(utility.OctaneGraphNode(active_output_node, None, ancestor_list, False))
        # node name => OctaneGraphNode
        processed_octane_nodes = {}
        # the final node list to update [OctaneGraphNode...]
        final_node_list = []        
        # traverse node graph recursively and generate linked node maps
        while len(queue):
            octane_graph_node = queue.popleft()            
            if octane_graph_node.node is active_output_node:
                # Root node
                root_octane_node = octane_graph_node.add_socket(active_output_node.inputs[active_input_name])
                if root_octane_node is None:
                    continue
                root_octane_node.octane_name = root_name
                root_octane_node.is_root = True                
                if active_input_name in ("Geometry", "Octane Geometry"):
                    if len(active_output_node.inputs[active_input_name].links):
                        root_octane_node.octane_name = root_name + "_" + active_output_node.inputs[active_input_name].links[0].from_node.name
                    root_octane_node.is_root = False
                queue.append(root_octane_node)
            else:
                # Avoid cyclic link and redundant process
                if octane_graph_node.octane_name in processed_octane_nodes:
                    continue
                processed_octane_nodes[octane_graph_node.octane_name] = octane_graph_node
                for _input in octane_graph_node.node.inputs:                
                    linked_octane_node = octane_graph_node.add_socket(_input)
                    if linked_octane_node:
                        queue.append(linked_octane_node)
                final_node_list.append(octane_graph_node)
                if isinstance(octane_graph_node.node, OctaneBaseNode):
                    # Set auto refresh attribute
                    if octane_graph_node.node.auto_refresh():
                        node_tree_attributes.auto_refresh = True
                    # Set image attribute
                    if octane_graph_node.node.is_octane_image_node() and octane_graph_node.node.image is not None:                    
                        node_tree_attributes.image_names.append(octane_graph_node.node.image.name)
                    # Set object attribute
                    if octane_graph_node.node.bl_idname == "OctaneObjectData":
                        node_tree_attributes.object_names.append(octane_graph_node.node.get_target_object_name())                
        # update node to the server
        is_updated = False
        for octane_graph_node_data in final_node_list:
            octane_name = octane_graph_node_data.octane_name
            node = octane_graph_node_data.node
            otane_node_id = str(node.as_pointer())
            if self.octane_node_cache.has_data(otane_node_id):
                octane_node = self.octane_node_cache.get(octane_name, otane_node_id)
            else:
                octane_node = self.octane_node_cache.add(octane_name, otane_node_id)
            if isinstance(octane_graph_node.node, OctaneBaseNode):
                octane_node.set_node_type(node.octane_node_type)
                octane_node.set_name(octane_name)
                node.sync_data(octane_node, octane_graph_node_data, owner_type, context.scene, self.is_viewport())
                # print(octane_node)
                if octane_node.need_update:
                    OctaneClient().process_octane_node(octane_node)
                    octane_node.need_update = False
                    is_updated = True
        return is_updated

    def update_node_tree(self, context, node_tree, owner_id, node_tree_attributes):
        owner_type = utility.get_node_tree_owner_type(owner_id)
        active_output_node = utility.find_active_output_node(node_tree, owner_type)
        if active_output_node:
            for _input in active_output_node.inputs:
                if not _input.enabled:
                    continue
                root_node = _input.links[0].from_node if len(_input.links) else None
                root_name = utility.get_octane_name_for_root_node(active_output_node, _input.name, owner_id)
                self.rendertarget_cache.update_links(owner_type, _input.name, root_node, root_name)
                if not root_node:
                    continue                
                is_updated = self._update_node_tree(context, node_tree, owner_type, active_output_node, _input.name, root_name, node_tree_attributes)