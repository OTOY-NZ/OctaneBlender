import bpy
import xml.etree.ElementTree as ET
from collections import deque, defaultdict
from octane.utils import consts, utility
from octane.core.octane_node import OctaneNode, CArray
from octane.nodes.base_node import OctaneBaseNode


class NodeTreeAttributes(object):
    def __init__(self):
        self.auto_refresh = consts.AutoRereshStrategy.DISABLE
        self.image_names = []
        self.object_names = []


class BaseDataCache(object):
    def __init__(self, session):
        self.session = session        
        self.type_name = ""
        self.type_class = None
        self.type_collection_name = ""        
        self.last_update_frame = 0
        self.cached_data = {}
        self.changed_data_names = set()
        # {type_name => {data => a set of dependent names}}
        self.data_to_dependent = defaultdict(lambda: defaultdict(set))
        # {type_name => {dependent => a set of data names}
        self.dependent_to_data = defaultdict(lambda: defaultdict(set))
        # {data name => refresh strategy type}
        self.auto_refresh_data_names = defaultdict(int)
        self.need_update_all = True
        self.need_update = False

    def reset(self):
        self.last_update_frame = 0
        self.cached_data.clear()
        self.changed_data_names.clear()
        self.data_to_dependent.clear()
        self.dependent_to_data.clear()
        self.auto_refresh_data_names.clear()
        self.need_update_all = True
        self.need_update = False

    def need_update(self):
        return self.need_update

    def has_data(self, name):
        return name in self.cached_data

    def get(self, name):
        if name in self.cached_data:
            return self.cached_data[name]
        return None

    def add(self, name):
        self.cached_data[name] = name

    def remove(self, name):
        if name in self.cached_data:
            del self.cached_data[name]
        if name in self.auto_refresh_data_names:
            del self.auto_refresh_data_names[name]

    def add_all(self, depsgraph):
        # Add non-evaluated data
        for _id in getattr(bpy.data, self.type_collection_name):
            self.changed_data_names.add(_id.name)
            self.need_update = True
        # Add evaluated data
        for _id in [item for item in depsgraph.ids if isinstance(item, self.type_class)]:
            self.changed_data_names.add(_id.name)
            self.need_update = True            
        self.need_update_all = False

    def dependency_diff(self, depsgraph, scene, view_layer, context=None):
        pass

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        pass

    def diff(self, depsgraph, scene, view_layer, context=None):
        self.changed_data_names.clear()
        if self.need_update_all or self.session.session_type == consts.SessionType.EXPORT:
            self.add_all(depsgraph)
        else:
            if depsgraph.id_type_updated(self.type_name):
                for dg_update in depsgraph.updates:
                    if isinstance(dg_update.id, self.type_class):
                        self.changed_data_names.add(dg_update.id.name)
                        self.need_update = True          
            # Process auto refresh
            frame_changed = (self.last_update_frame != scene.frame_current)
            for auto_refresh_data_name, strategy in self.auto_refresh_data_names.items():
                if strategy == consts.AutoRereshStrategy.ALWAYS or (frame_changed and strategy == consts.AutoRereshStrategy.FRAME_CHANGE):
                    self.changed_data_names.add(auto_refresh_data_name)
                    self.need_update = True
            # Process dependency
            self.dependency_diff(depsgraph, scene, view_layer, context)
            self.custom_diff(depsgraph, scene, view_layer, context)
        self.last_update_frame = scene.frame_current
        return self.need_update

    def create_octane_node(self, name, node_type=None):
        octane_node = OctaneNode(name)
        if node_type is not None:
            octane_node.node_type = node_type
        return octane_node

    def update(self, depsgraph, scene, view_layer, context=None):
        pass


class OctaneNodeCache(BaseDataCache):

    @staticmethod
    def generate_octane_node_id(node_id):
        return node_id

    def add(self, node_name, node_type, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_id)
        octane_node = OctaneNode(node_name, node_type)
        self.cached_data[_id] = octane_node
        return octane_node

    def get(self, node_name, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_id)
        if _id in self.cached_data:
            return self.cached_data[_id]
        return None


class OctaneRenderTargetCache(BaseDataCache):
    DEFAULT_RENDERTARGET_NAME = "RenderTarget"
    P_CAMERA_NAME = "camera"
    P_IMAGER_NAME = "imager"
    P_KERNEL_NAME = "kernel"
    P_ENVIRONMENT_NAME = "environment"
    P_VISIBLE_ENVIRONMENT_NAME = "cameraEnvironment"
    P_RENDER_PASSES_NAME = "renderPasses"
    P_OUTPUT_AOVS_NAME = "compositeAovs"
    P_POST_PROCESSING_NAME = "postproc"
    P_ANIMATION_SETTINGS_NAME = "animation"
    P_RENDER_LAYER_NAME = "renderLayer"    

    def __init__(self, session):
        super().__init__(session)
        self.rendertarget_node = self.create_octane_node(self.DEFAULT_RENDERTARGET_NAME, consts.NodeType.NT_RENDERTARGET)
        self.links = {}

    def __del__(self):
        self.rendertarget_node = None

    def get_rendertarget_node(self):
        return self.rendertarget_node

    def diff(self, depsgraph, scene, view_layer, context=None):
        return self.rendertarget_node.need_update

    def update(self, depsgraph, scene, view_layer, context=None):        
        if self.rendertarget_node.need_update:
            self.rendertarget_node.update_to_engine(True)

    def update_link(self, pin_name, node_name, link_name):
        self.rendertarget_node.set_attribute_blender_name(pin_name, consts.AttributeType.AT_STRING, link_name)
        # If the linked blender node is changed, force to update it
        if self.links.get(pin_name, None) != node_name:
            self.links[pin_name] = node_name
            self.rendertarget_node.need_update = True

    def update_links(self, owner_type, input_socket_name, root_node, root_name):
        node_name = root_node.name if root_node else ""
        link_name = root_name if root_node else ""
        if owner_type == consts.OctaneNodeTreeIDName.MATERIAL:
            pass
        elif owner_type == consts.OctaneNodeTreeIDName.WORLD:
            if input_socket_name in (consts.OctaneOutputNodeSocketNames.ENVIRONMENT, consts.OctaneOutputNodeSocketNames.LEGACY_ENVIRONMENT):                
                self.update_link(self.P_ENVIRONMENT_NAME, node_name, link_name)
            elif input_socket_name in (consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT, consts.OctaneOutputNodeSocketNames.LEGACY_VISIBLE_ENVIRONMENT):                
                self.update_link(self.P_VISIBLE_ENVIRONMENT_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.COMPOSITE:
            self.update_link(self.P_OUTPUT_AOVS_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.RENDER_AOV:
            self.update_link(self.P_RENDER_PASSES_NAME, node_name, link_name)
        elif owner_type == consts.OctaneNodeTreeIDName.KERNEL:
            self.update_link(self.P_KERNEL_NAME, node_name, link_name)


class ImageCache(BaseDataCache):
    TYPE_NAME = "IMAGE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Image
        self.type_collection_name = "images"


class NodeTreeCache(OctaneNodeCache):

    def _dependency_diff(self, depsgraph, cache_depend_on):
        if cache_depend_on and len(cache_depend_on.changed_data_names):
            for dependent_name in cache_depend_on.changed_data_names:
                for data_name in self.dependent_to_data[cache_depend_on.type_name][dependent_name]:
                    self.changed_data_names.add(data_name)
                    self.need_update = True

    def dependency_diff(self, depsgraph, scene, view_layer, context=None):
        # Process image
        self._dependency_diff(depsgraph, self.session.image_cache)
        # Process object
        self._dependency_diff(depsgraph, self.session.object_cache)

    def use_node_tree(self, scene, view_layer, _id):
        return _id is not None and _id.use_nodes

    def get_node_tree(self, _id):
        return _id.node_tree

    def get_octane_node(self, node_name, node):
        node_id = node_name
        node_type = node.octane_node_type
        if self.has_data(node_id):
            octane_node = self.get(node_name, node_id)
            if octane_node.node_type != node_type:
                self.remove(node_id)
                octane_node = self.add(node_name, node_type, node_id)
        else:
            octane_node = self.add(node_name, node_type, node_id)
        return octane_node

    def _update_node_tree(self, depsgraph, view_layer, node_tree, owner_id, owner_type, active_output_node, active_input_name, root_name, node_tree_attributes):
        ancestor_list = [utility.OctaneGraphNodeDummy(root_name), ]
        # nodes to process [OctaneGraphNode...]
        queue = deque()
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
                    node_tree_attributes.auto_refresh = max(node_tree_attributes.auto_refresh, octane_graph_node.node.auto_refresh())
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
            octane_node = self.get_octane_node(octane_name, node)
            if isinstance(node, OctaneBaseNode):
                octane_node.node_type = node.octane_node_type
                octane_node.name = octane_name
                node.sync_data(octane_node, octane_graph_node_data, depsgraph)
                if octane_node.need_update:
                    octane_node.update_to_engine(True)
                    is_updated = True
        return is_updated

    def update_node_tree(self, depsgraph, view_layer, node_tree, owner_id, node_tree_attributes):
        owner_type = utility.get_node_tree_owner_type(owner_id)
        active_output_node = utility.find_active_output_node(node_tree, owner_type)
        if active_output_node:
            for _input in active_output_node.inputs:
                if not _input.enabled:
                    continue
                root_node = _input.links[0].from_node if len(_input.links) else None
                root_name = utility.get_octane_name_for_root_node(active_output_node, _input.name, owner_id)
                self.session.rendertarget_cache.update_links(owner_type, _input.name, root_node, root_name)
                if not root_node:
                    continue                
                is_updated = self._update_node_tree(depsgraph, view_layer, node_tree, owner_id, owner_type, active_output_node, _input.name, root_name, node_tree_attributes)

    def update(self, depsgraph, scene, view_layer, context=None):
        from octane.core.object_cache import ObjectCache
        self.custom_update(depsgraph, scene, view_layer, context)
        for name in self.changed_data_names:
            if len(name) == 0:
                continue
            _id = None
            for depsgraph_id in depsgraph.ids:
                if depsgraph_id.name == name and isinstance(depsgraph_id.original, self.type_class):
                    _id = depsgraph_id
                    break
            if _id is None:
                _id = getattr(bpy.data, self.type_collection_name).get(name, None)
                if _id is not None:
                    _id = _id.evaluated_get(depsgraph)
            if self.use_node_tree(scene, view_layer, _id):
                data_name = _id.name
                node_tree_attributes = NodeTreeAttributes()
                self.update_node_tree(depsgraph, view_layer, self.get_node_tree(_id), _id, node_tree_attributes)
                # Update auto refresh attribute
                if node_tree_attributes.auto_refresh != consts.AutoRereshStrategy.DISABLE:
                    self.auto_refresh_data_names[data_name] = node_tree_attributes.auto_refresh
                else:
                    if data_name in self.auto_refresh_data_names:
                        self.auto_refresh_data_names.remove(data_name)
                # Update image attribute
                self.data_to_dependent[ImageCache.TYPE_NAME][data_name] = set(node_tree_attributes.image_names)
                # Update object attribute
                self.data_to_dependent[ObjectCache.TYPE_NAME][data_name] = set(node_tree_attributes.object_names)
        # Update image attribute
        self.dependent_to_data[ImageCache.TYPE_NAME].clear()
        for data_name, dependent_set in self.data_to_dependent[ImageCache.TYPE_NAME].items():
            for dependent_name in dependent_set:
                self.dependent_to_data[ImageCache.TYPE_NAME][dependent_name].add(data_name)
        # Update object attribute
        self.dependent_to_data[ObjectCache.TYPE_NAME].clear()
        for data_name, dependent_set in self.data_to_dependent[ObjectCache.TYPE_NAME].items():
            for dependent_name in dependent_set:
                self.dependent_to_data[ObjectCache.TYPE_NAME][dependent_name].add(data_name)
        self.changed_data_names.clear()
        self.need_update = False

    def custom_update(self, depsgraph, scene, view_layer, context=None):
        pass


class MaterialCache(NodeTreeCache):
    TYPE_NAME = "MATERIAL"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Material
        self.type_collection_name = "materials"


class LightCache(NodeTreeCache):
    TYPE_NAME = "LIGHT"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Light
        self.type_collection_name = "lights"


class WorldCache(NodeTreeCache):
    TYPE_NAME = "WORLD"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.World
        self.type_collection_name = "worlds"
        self.last_name = ""
        self.last_links_set = set()

    def use_node_tree(self, scene, view_layer, _id):        
        return super().use_node_tree(scene, view_layer, _id) and getattr(scene.world, "name", "") == getattr(_id, "name", "")

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        current_name = getattr(scene.world, "name", "")
        if current_name != self.last_name:
            self.last_name = current_name
            self.need_update = True
        if self.is_node_tree_link_changed(scene):
            self.need_update = True
        if self.need_update:
            self.changed_data_names.add(current_name)

    def custom_update(self, depsgraph, scene, view_layer, context=None):
        if scene.world is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.ENVIRONMENT, None, "")
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT, None, "")

    def is_node_tree_link_changed(self, scene):
        # The customized World Output cannot trigger the update signal automatically
        # So we need an additional check here
        is_changed = False
        links_set = set()
        if scene.world and scene.world.use_nodes:
            for link in scene.world.node_tree.links:
                link_info = "%s->%s" % (link.from_node.name, link.to_node.name)
                links_set.add(link_info)
                # links_set.add(link.as_pointer())
        if links_set != self.last_links_set:
            self.last_links_set = links_set
            is_changed = True
        return is_changed

class CompositeCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, scene, view_layer, _id):
        active_composite_node_tree = self.find_active_composite_node_tree(view_layer)
        return _id is not None and getattr(active_composite_node_tree, "name", "") == getattr(_id, "name", "")

    def find_active_composite_node_tree(self, view_layer):
        node_tree = utility.find_active_composite_node_tree(view_layer)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        current_name = getattr(self.find_active_composite_node_tree(view_layer), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, depsgraph, scene, view_layer, context=None):
        if self.find_active_composite_node_tree(view_layer) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneOutputNodeSocketNames.COMPOSITE, None, "")


class RenderAOVCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, scene, view_layer, _id):
        render_aov_node_tree = self.find_active_render_aov_node_tree(view_layer)
        return _id is not None and getattr(render_aov_node_tree, "name", "") == getattr(_id, "name", "")

    def find_active_render_aov_node_tree(self, view_layer):
        node_tree = utility.find_active_render_aov_node_tree(view_layer)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def get_current_preview_render_pass_id(self, view_layer):
        node_tree = self.find_active_render_aov_node_tree(view_layer)
        if node_tree is None:
            return consts.RenderPassId.BEAUTY
        return node_tree.get_current_preview_render_pass_id(view_layer)

    def get_enabled_render_pass_ids(self, view_layer):
        node_tree = self.find_active_render_aov_node_tree(view_layer)
        if node_tree is None:
            return [consts.RenderPassId.BEAUTY, ]
        return node_tree.get_enabled_render_pass_ids(view_layer)

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        current_name = getattr(self.find_active_render_aov_node_tree(view_layer), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, depsgraph, scene, view_layer, context=None):
        if self.find_active_render_aov_node_tree(view_layer) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.RENDER_AOV, consts.OctaneOutputNodeSocketNames.RENDER_AOV, None, "")            


class KernelCache(NodeTreeCache):
    TYPE_NAME = "NODETREE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.NodeGroup
        self.type_collection_name = "node_groups"
        self.last_name = ""

    def get_node_tree(self, _id):
        return _id

    def use_node_tree(self, scene, view_layer, _id):
        kernel_node_tree = self.find_active_kernel_node_tree(scene)
        return _id is not None and getattr(kernel_node_tree, "name", "") == getattr(_id, "name", "")

    def find_active_kernel_node_tree(self, scene):
        node_tree = utility.find_active_kernel_node_tree(scene)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, depsgraph, scene, view_layer, context=None):
        current_name = getattr(self.find_active_kernel_node_tree(scene), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, depsgraph, scene, view_layer, context=None):
        if self.find_active_kernel_node_tree(scene) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.KERNEL, consts.OctaneOutputNodeSocketNames.KERNEL, None, "")


class RenderSettings(object):
    def __init__(self):
        # Priority Level
        self.priority_level = 0
        # Out of Core
        self.enable_out_of_core = False
        self.out_of_core_limit = 0
        self.out_of_core_gpu_headroom = 0
        # Sub-sampling Mode
        self.subsampling_mode = 0
        # Clay Mode
        self.clay_mode = 0


class SceneCache(BaseDataCache):
    CAMERA_MOTION_DATA_SAMPLE_NUM = "CAMERA_MOTION_DATA_SAMPLE_NUM"
    CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER = "CAMERA_POSITION"
    CAMERA_TARGET_DATA_C_ARRAY_IDENTIFIER = "CAMERA_TARGET"
    CAMERA_UP_DATA_C_ARRAY_IDENTIFIER = "CAMERA_UP"

    def __init__(self, session):
        super().__init__(session)
        self.render_settings = RenderSettings()
        self.camera_node = self.create_octane_node(consts.OctanePresetNodeNames.CAMERA)
        self.imager_node = self.create_octane_node(consts.OctanePresetNodeNames.IMAGER, consts.NodeType.NT_IMAGER_CAMERA)
        self.post_processing_node = self.create_octane_node(consts.OctanePresetNodeNames.POST_PROCESSING, consts.NodeType.NT_POSTPROCESSING)
        self.animation_setting_node = self.create_octane_node(consts.OctanePresetNodeNames.ANIMATION_SETTINGS, consts.NodeType.NT_ANIMATION_SETTINGS)
        self.render_layer_node = self.create_octane_node(consts.OctanePresetNodeNames.RENDER_LAYER, consts.NodeType.NT_RENDER_LAYER)
        self.last_camera_name = ""
        self.last_imager_name = ""
        self.last_post_processing_name = ""        

    def diff(self, depsgraph, scene, view_layer, context=None):
        if self.need_update_all or depsgraph.id_type_updated("SCENE") or depsgraph.id_type_updated("CAMERA"):
            self.need_update_all = False            
            self.need_update = True
        else:
            _, post_processing_name = utility.find_active_post_process_data(scene, context)            
            if post_processing_name != self.last_post_processing_name:
                self.last_post_processing_name = post_processing_name
                self.need_update = True
            _, imager_name = utility.find_active_imager_data(scene, context)
            if imager_name != self.last_imager_name:
                self.last_imager_name = imager_name
                self.need_update = True            
        return self.need_update

    def update(self, depsgraph, scene, view_layer, context=None):
        if self.need_update:
            self.update_post_processing(depsgraph, scene, view_layer, context)
            self.update_imager(depsgraph, scene, view_layer, context)
            self.update_animation_settings(depsgraph, scene, view_layer, context)
            self.update_render_layer(depsgraph, scene, view_layer, context)
            self.update_render_settings(depsgraph, scene, view_layer, context)
        self.need_update = False

    def update_camera(self, depsgraph, scene, view_layer, context=None):        
        camera_data, camera_name = utility.find_active_camera_data(scene, context)
        is_viewport = self.session.is_viewport()
        motion_time_offsets = None
        if self.session.need_motion_blur:
            motion_time_offsets = utility.object_motion_time_offsets(bpy.data.objects[camera_name], self.session.motion_blur_start_frame_offset, self.session.motion_blur_end_frame_offset)
            if motion_time_offsets is not None:
                self.camera_node.need_motion_blur = True
                for offset in motion_time_offsets:
                    self.session.motion_blur_time_offsets.add(offset)
        if is_viewport:
            if context is None:
                context = bpy.context
            camera_data.sync_data(self.camera_node, scene=scene, region=context.region, v3d=context.space_data, rv3d=context.region_data, is_viewport=True)
        else:
            camera_data.sync_data(self.camera_node, scene=scene, is_viewport=False)        
        if self.camera_node.need_update:
            self.camera_node.update_to_engine(True)            
        current_active_camera_name = getattr(self.camera_node, "current_active_camera_name", "")
        active_camera_node = self.camera_node.find_subnode(current_active_camera_name)
        if active_camera_node is not None:
            active_camera_node.motion_time_offsets = motion_time_offsets
        self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_CAMERA_NAME, current_active_camera_name, current_active_camera_name)

    def update_camera_motion_blur_sample(self, motion_time_offset, depsgraph, scene, view_layer, context=None):        
        camera_data, camera_name = utility.find_active_camera_data(scene, context)
        current_active_camera_name = getattr(self.camera_node, "current_active_camera_name", "")
        active_camera_node = self.camera_node.find_subnode(current_active_camera_name)
        if active_camera_node.motion_time_offsets and motion_time_offset in active_camera_node.motion_time_offsets:
            camera_eval = scene.camera.evaluated_get(depsgraph)
            camera_data.sync_camera_motion_blur(active_camera_node, motion_time_offset, camera_eval)

    def update_camera_motion_array_data(self, node, identifier, sample_num, current_sample_index, current_data):
        float_data_num = sample_num * 3
        array_data = node.get_array_data(identifier)
        if array_data is None or len(array_data) != float_data_num:
            node.delete_array_data(identifier)
            if node.new_array_data(identifier, CArray.FLOAT, float_data_num, 3):
                array_data = node.get_array_data(identifier)
        offset = current_sample_index * 3
        array_data[offset] = current_data[0]
        array_data[offset + 1] = current_data[1]
        array_data[offset + 2] = current_data[2]

    def update_camera_motion_blur(self, depsgraph, scene, view_layer, context=None):
        camera_data, camera_name = utility.find_active_camera_data(scene, context)
        current_active_camera_name = getattr(self.camera_node, "current_active_camera_name", "")
        active_camera_node = self.camera_node.find_subnode(current_active_camera_name)
        # camera_position_node = self.camera_node.get_subnode(consts.OctanePresetNodeNames.CAMERA_POSITION, consts.NodeType.NT_FLOAT)
        # camera_target_node = self.camera_node.get_subnode(consts.OctanePresetNodeNames.CAMERA_TARGET, consts.NodeType.NT_FLOAT)
        # camera_up_node = self.camera_node.get_subnode(consts.OctanePresetNodeNames.CAMERA_UP, consts.NodeType.NT_FLOAT)
        if active_camera_node.motion_time_offsets and len(active_camera_node.motion_time_offsets) > 0:
            sample_num = len(active_camera_node.motion_time_offsets)
            for idx, time_offset in enumerate(sorted(list(active_camera_node.motion_time_offsets))):
                self.update_camera_motion_array_data(active_camera_node, self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER, sample_num, idx, active_camera_node.positions[time_offset])
                self.update_camera_motion_array_data(active_camera_node, self.CAMERA_TARGET_DATA_C_ARRAY_IDENTIFIER, sample_num, idx, active_camera_node.targets[time_offset])
                self.update_camera_motion_array_data(active_camera_node, self.CAMERA_UP_DATA_C_ARRAY_IDENTIFIER, sample_num, idx, active_camera_node.ups[time_offset])
            # camera_position_node.set_attribute_id(consts.AttributeID.A_VALUE, self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER, sample_num)
            # camera_target_node.set_attribute_id(consts.AttributeID.A_VALUE, self.CAMERA_TARGET_DATA_C_ARRAY_IDENTIFIER, sample_num)
            # camera_up_node.set_attribute_id(consts.AttributeID.A_VALUE, self.CAMERA_UP_DATA_C_ARRAY_IDENTIFIER, sample_num)
            # camera_position_node.update_to_engine(True)
            # camera_target_node.update_to_engine(True)
            # camera_up_node.update_to_engine(True)
            active_camera_node.set_attribute_blender_name(self.CAMERA_MOTION_DATA_SAMPLE_NUM, consts.AttributeType.AT_INT, sample_num)
            active_camera_node.set_attribute_blender_name(self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER, consts.AttributeType.AT_STRING, self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER)
            active_camera_node.set_attribute_blender_name(self.CAMERA_TARGET_DATA_C_ARRAY_IDENTIFIER, consts.AttributeType.AT_STRING, self.CAMERA_TARGET_DATA_C_ARRAY_IDENTIFIER)
            active_camera_node.set_attribute_blender_name(self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER, consts.AttributeType.AT_STRING, self.CAMERA_POSITION_DATA_C_ARRAY_IDENTIFIER)
            active_camera_node.update_to_engine(True)            

    def update_post_processing(self, depsgraph, scene, view_layer, context=None):
        camera_data, camera_name = utility.find_active_post_process_data(scene, context)
        if camera_data is None:
            self.post_processing_node.set_pin_id(consts.PinID.P_ON_OFF, False, "", False)
        else:
            self.post_processing_node.set_pin_id(consts.PinID.P_ON_OFF, False, "", getattr(camera_data, "postprocess", False))
            camera_data.post_processing.sync_data(self.post_processing_node, scene=scene, is_viewport=self.session.is_viewport())
        if self.post_processing_node.need_update:
            self.post_processing_node.update_to_engine(True)
        self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_POST_PROCESSING_NAME, self.post_processing_node.name, self.post_processing_node.name)

    def update_imager(self, depsgraph, scene, view_layer, context=None):
        camera_data, camera_name = utility.find_active_imager_data(scene, context)
        enable_imager = utility.is_active_imager_enabled(scene, context)
        if not enable_imager or camera_data is None:
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_IMAGER_NAME, "", "")
        else:
            camera_data.imager.sync_data(self.imager_node, scene=scene, is_viewport=self.session.is_viewport())
            if self.imager_node.need_update:
                self.imager_node.update_to_engine(True)
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_IMAGER_NAME, self.imager_node.name, self.imager_node.name)

    def update_animation_settings(self, depsgraph, scene, view_layer, context=None):
        enable_animation_settings = scene.render.use_motion_blur
        if enable_animation_settings:
            scene.octane.animation_settings.sync_data(self.animation_setting_node, scene=scene, is_viewport=self.session.is_viewport())
            if self.animation_setting_node.need_update:
                self.animation_setting_node.update_to_engine(True)
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_ANIMATION_SETTINGS_NAME, self.animation_setting_node.name, self.animation_setting_node.name)
        else:
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_ANIMATION_SETTINGS_NAME, "", "")

    def update_render_layer(self, depsgraph, scene, view_layer, context=None):
        enable_global_render_layer = scene.octane.render_layer.layers_enable
        enable_viewlayer_render_layer = view_layer.octane.layers_enable
        if enable_global_render_layer or enable_viewlayer_render_layer:
            if enable_global_render_layer:
                scene.octane.render_layer.sync_data(self.render_layer_node, scene=scene, is_viewport=self.session.is_viewport())
            elif enable_viewlayer_render_layer:
                view_layer.octane.sync_data(self.render_layer_node, scene=scene, is_viewport=self.session.is_viewport())
            if self.render_layer_node.need_update:
                self.render_layer_node.update_to_engine(True)
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_RENDER_LAYER_NAME, self.render_layer_node.name, self.render_layer_node.name)
        else:
            self.session.rendertarget_cache.update_link(OctaneRenderTargetCache.P_RENDER_LAYER_NAME, "", "")

    def update_render_settings(self, depsgraph, scene, view_layer, context=None):
        need_update = False
        scene_octane = scene.octane
        request_et = ET.Element('updateRenderSettings')
        # Priority Level
        priority_mode = utility.get_enum_int_value(scene_octane, "priority_mode", 0)
        if self.render_settings.priority_level != priority_mode:
            self.render_settings.priority_level = priority_mode
            request_et.set("priorityLevel", str(self.render_settings.priority_level))
            need_update = True
        # Out of Core
        if self.render_settings.enable_out_of_core != scene_octane.out_of_core_enable or \
            self.render_settings.out_of_core_limit != scene_octane.out_of_core_limit or \
            self.render_settings.out_of_core_gpu_headroom != scene_octane.out_of_core_gpu_headroom:
            self.render_settings.enable_out_of_core = scene_octane.out_of_core_enable
            self.render_settings.out_of_core_limit = scene_octane.out_of_core_limit
            self.render_settings.out_of_core_gpu_headroom = scene_octane.out_of_core_gpu_headroom
            request_et.set("enableOutOfCore", str(1 if self.render_settings.enable_out_of_core else 0))
            request_et.set("outOfCoreLimit", str(self.render_settings.out_of_core_limit))
            request_et.set("outOfCoreGPUheadroom", str(self.render_settings.out_of_core_gpu_headroom))
            need_update = True
        # Subsample Mode
        subsample_mode = utility.get_enum_int_value(scene_octane, "subsample_mode", 0)
        if self.render_settings.subsampling_mode != subsample_mode:
            self.render_settings.subsampling_mode = subsample_mode
            request_et.set("subsamplingMode", str(self.render_settings.subsampling_mode))
            need_update = True
        # Clay Mode
        clay_mode = utility.get_enum_int_value(scene_octane, "clay_mode", 0)
        if self.render_settings.clay_mode != clay_mode:
            self.render_settings.clay_mode = clay_mode
            request_et.set("clayMode", str(self.render_settings.clay_mode))
            need_update = True                        
        if need_update:
            xml_data = ET.tostring(request_et, encoding="unicode")
            from octane.core.client import OctaneBlender
            response = OctaneBlender().utils_function(consts.UtilsFunctionType.UPDATE_RENDER_SETTINGS, xml_data)