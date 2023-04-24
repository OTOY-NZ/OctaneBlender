import bpy
from collections import defaultdict
from octane.utils import consts, utility
from octane.core.client import OctaneClient
from octane.core.octane_node import OctaneNode, OctaneNodeType


class NodeTreeAttributes(object):
    def __init__(self):
        self.auto_refresh = False
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
        self.auto_refresh_data_names = set()
        self.need_update_all = True
        self.need_update = False

    def reset(self, session):
        self.session = session
        self.last_update_frame = 0
        self.cached_data.clear()
        self.changed_data_names.clear()
        self.data_to_dependent.clear()
        self.dependent_to_data.clear()
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
            self.auto_refresh_data_names.remove(name)

    def add_all(self, context, depsgraph):
        for _id in getattr(bpy.data, self.type_collection_name):
            self.changed_data_names.add(_id.name)
            self.need_update = True
        self.need_update_all = False

    def dependency_diff(self, context, depsgraph):
        pass

    def custom_diff(self, context, depsgraph):
        pass

    def diff(self, context, depsgraph):
        self.changed_data_names.clear()
        if self.need_update_all:
            self.add_all(context, depsgraph)
        else:
            if depsgraph.id_type_updated(self.type_name):
                for dg_update in depsgraph.updates:
                    if isinstance(dg_update.id, self.type_class):
                        self.changed_data_names.add(dg_update.id.name)
                        self.need_update = True          
            # Process auto refresh
            if self.last_update_frame != context.scene.frame_current:
                if len(self.auto_refresh_data_names):
                    self.changed_data_names.update(self.auto_refresh_data_names)
                    self.need_update = True
            # Process dependency
            self.dependency_diff(context, depsgraph)
            self.custom_diff(context, depsgraph)
        self.last_update_frame = context.scene.frame_current
        return self.need_update

    def update(self, context, depsgraph):
        pass


class OctaneNodeCache(BaseDataCache):

    @staticmethod
    def generate_octane_node_id(node_name, node_id):
        return "%s[%s]" % (node_name, node_id)

    def add(self, node_name, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_name, node_id)
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        self.cached_data[_id] = octane_node
        return octane_node

    def get(self, node_name, node_id):
        _id = OctaneNodeCache.generate_octane_node_id(node_name, node_id)
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

    def __init__(self, session):
        super().__init__(session)
        self.rendertarget_node = self.add(self.DEFAULT_RENDERTARGET_NAME)
        self.links = {}

    def get_rendertarget_node(self):
        return self.rendertarget_node

    def add(self, name):
        octane_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        octane_node.set_name(name)
        octane_node.set_node_type(consts.NodeType.NT_RENDERTARGET)
        self.cached_data[name] = octane_node
        return octane_node

    def diff(self, context, depsgraph):
        return self.rendertarget_node.need_update

    def update(self, context, depsgraph):        
        if self.rendertarget_node.need_update:
            OctaneClient().process_octane_node(self.rendertarget_node)
            self.rendertarget_node.need_update = False

    def update_link(self, pin_name, node_name, link_name):
        self.rendertarget_node.set_blender_attribute(pin_name, consts.AttributeType.AT_STRING, link_name)
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

class ObjectCache(BaseDataCache):
    TYPE_NAME = "OBJECT"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Object
        self.type_collection_name = "objects"


class ImageCache(BaseDataCache):
    TYPE_NAME = "IMAGE"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Image
        self.type_collection_name = "images"


class NodeTreeCache(BaseDataCache):

    def _dependency_diff(self, context, depsgraph, cache_depend_on):
        if cache_depend_on and len(cache_depend_on.changed_data_names):
            for dependent_name in cache_depend_on.changed_data_names:
                for data_name in self.dependent_to_data[cache_depend_on.type_name][dependent_name]:
                    self.changed_data_names.add(data_name)
                    self.need_update = True

    def dependency_diff(self, context, depsgraph):
        # Process image
        self._dependency_diff(context, depsgraph, self.session.image_cache)
        # Process object
        self._dependency_diff(context, depsgraph, self.session.object_cache)

    def use_node_tree(self, context, _id):
        return _id is not None and _id.use_nodes

    def get_node_tree(self, _id):
        return _id.node_tree

    def update(self, context, depsgraph):
        self.custom_update(context, depsgraph)
        for name in self.changed_data_names:            
            _id = getattr(bpy.data, self.type_collection_name).get(name, None)
            if self.use_node_tree(context, _id):
                data_name = _id.name
                node_tree_attributes = NodeTreeAttributes()
                self.session.update_node_tree(context, self.get_node_tree(_id), _id, node_tree_attributes)
                self.add(data_name)
                # Update auto refresh attribute
                if node_tree_attributes.auto_refresh:
                    self.auto_refresh_data_names.add(data_name)
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

    def custom_update(self, context, depsgraph):
        pass


class MaterialCache(NodeTreeCache):
    TYPE_NAME = "MATERIAL"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.Material
        self.type_collection_name = "materials"


class WorldCache(NodeTreeCache):
    TYPE_NAME = "WORLD"

    def __init__(self, session):
        super().__init__(session)
        self.type_name = self.TYPE_NAME
        self.type_class = bpy.types.World
        self.type_collection_name = "worlds"
        self.last_name = ""

    def use_node_tree(self, context, _id):
        return super().use_node_tree(context, _id) and context.scene.world is _id

    def custom_diff(self, context, depsgraph):
        current_name = getattr(context.scene.world, "name", "")
        if current_name != self.last_name:
            self.last_name = current_name
            self.need_update = True

    def custom_update(self, context, depsgraph):        
        if context.scene.world is None:            
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.ENVIRONMENT, None, "")
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.WORLD, consts.OctaneOutputNodeSocketNames.VISIBLE_ENVIRONMENT, None, "")


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

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_composite_node_tree(context) is _id

    def find_active_composite_node_tree(self, context):
        node_tree = utility.find_active_composite_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_composite_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_composite_node_tree(context) is None:
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

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_render_aov_node_tree(context) is _id

    def find_active_render_aov_node_tree(self, context):
        node_tree = utility.find_active_render_aov_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_render_aov_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_render_aov_node_tree(context) is None:
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

    def use_node_tree(self, context, _id):
        return _id is not None and self.find_active_kernel_node_tree(context) is _id

    def find_active_kernel_node_tree(self, context):
        node_tree = utility.find_active_kernel_node_tree(context)
        if node_tree and node_tree.active_output_node:
            return node_tree
        return None

    def custom_diff(self, context, depsgraph):
        current_name = getattr(self.find_active_kernel_node_tree(context), "name", "")
        if depsgraph.id_type_updated(self.type_name) or current_name != self.last_name:            
            self.changed_data_names.add(current_name)
            self.need_update = True
        self.last_name = current_name

    def custom_update(self, context, depsgraph):
        if self.find_active_kernel_node_tree(context) is None:
            self.session.rendertarget_cache.update_links(consts.OctaneNodeTreeIDName.KERNEL, consts.OctaneOutputNodeSocketNames.KERNEL, None, "")
