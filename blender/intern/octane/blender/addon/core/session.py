import bpy
import numpy as np
import time
import collections
import _thread
import threading
import queue
from octane.utils import consts, utility
from octane.core.caches import OctaneNodeCache, ObjectCache, ImageCache, MaterialCache, WorldCache, CompositeCache, RenderAOVCache, KernelCache, OctaneRenderTargetCache, SceneCache
from octane.core.client import OctaneClient
from octane.core.octane_node import OctaneNode, OctaneNodeType, CArray
from octane.nodes.base_node import OctaneBaseNode


class RenderResult(object):
    DEFAULT_RESOLUTION = (1024, 1024)
    MIN_UPDATE_INTERVAL = 0.03
    RENDER_RESULT = "RENDER_RESULT"
    BLENDER_ATTRIBUTE_RESOLUTION = "RESOLUTION"
    BLENDER_ATTRIBUTE_RENDER_PASS_ID = "RENDER_PASS_ID"
    BLENDER_ATTRIBUTE_CHANGE_LEVEL = "CHANGE_LEVEL"

    def __init__(self):
        self.resolution = [self.DEFAULT_RESOLUTION[0], self.DEFAULT_RESOLUTION[1]]
        self.render_pass_id = 0
        self.last_update_time = 0
        self.render_result_node = OctaneNode(OctaneNodeType.SYNC_NODE)
        self.render_result_node.set_name(self.RENDER_RESULT)
        self.render_result_node.set_node_type(consts.NodeType.NT_BLENDER_NODE_GET_RENDER_RESULT)
        self.viewport_float_pixel_array = None
        self.mutex = threading.Lock()
        self.index = 0

    def clear(self):
        self.render_result_node = None

    def setup(self, width, height, render_pass_id):
        self.resolution = [width, height]
        self.render_pass_id = render_pass_id
        self.render_result_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_RESOLUTION, consts.AttributeType.AT_INT2, self.resolution)
        self.render_result_node.set_blender_attribute(self.BLENDER_ATTRIBUTE_RENDER_PASS_ID, consts.AttributeType.AT_INT, render_pass_id)                

    def lock_render_result(self):
        self.mutex.acquire()

    def unlock_render_result(self):
        self.mutex.release()

    def update_pixel_array(self, width=None, height=None, render_pass_id=None):
        self.lock_render_result()
        current_time = time.time()
        if current_time - self.last_update_time < self.MIN_UPDATE_INTERVAL:
            self.unlock_render_result()
            return
        if width is not None and height is not None and render_pass_id is not None:
            self.setup(width, height, render_pass_id)
        reply_body = OctaneClient().process_octane_node(self.render_result_node)
        uint8_pixel_array = self.render_result_node.get_reply_c_array(CArray.UINT8)
        if len(uint8_pixel_array):
            pixel_array = uint8_pixel_array.astype(np.float32, copy=True) / 255.0
            self.viewport_float_pixel_array = pixel_array            
        self.last_update_time = current_time
        self.unlock_render_result()


def start_session(session, engine):
    while True:
        if _current_render_session is not None:            
            _current_render_session.update_node_to_server()
        try:
            if engine:
                session.grab_render_result(engine)
        except:
            pass
        time.sleep(0.03)


_current_render_session = None

def update_node_to_server():
    if _current_render_session is None:
        return
    _current_render_session.update_node_to_server()
    return 0.05


class RenderSession(object):
    def __init__(self):
        print("RenderSession Init")
        self.session_type = consts.SessionType.UNKNOWN
        self.render_result = RenderResult()
        self.octane_node_cache = OctaneNodeCache(self)
        self.object_cache = ObjectCache(self)
        self.image_cache = ImageCache(self)
        self.material_cache = MaterialCache(self)
        self.world_cache = WorldCache(self)
        self.composite_cache = CompositeCache(self)
        self.render_aov_cache = RenderAOVCache(self)
        self.kernel_cache = KernelCache(self)
        self.scene_cache = SceneCache(self)
        self.rendertarget_cache = OctaneRenderTargetCache(self)
        self.need_update_node_queue = queue.Queue()
        global _current_render_session
        _current_render_session = self
        # bpy.app.timers.register(update_node_to_server)

    def __del__(self):
        self.clear()

    def clear(self):
        self.render_result = None
        self.octane_node_cache = None
        self.object_cache = None
        self.image_cache = None        
        self.material_cache = None
        self.world_cache = None
        self.composite_cache = None
        self.kernel_cache = None
        self.scene_cache = None
        self.rendertarget_cache = None
        self.need_update_node_queue.queue.clear()        
        self.need_update_node_queue = None
        # bpy.app.timers.unregister(update_node_to_server)
        global _current_render_session
        _current_render_session = None

    def update_node_to_server(self):
        while not self.need_update_node_queue.empty():
            node = self.need_update_node_queue.get()
            if node.need_update:
                OctaneClient().process_octane_node(node)
                node.need_update = False

    def add_to_update_node_queue(self, node):
        # with self.need_update_node_queue.mutex:
        self.need_update_node_queue.put(node)

    def is_viewport(self):
        return self.session_type == consts.SessionType.VIEWPORT

    def is_final(self):
        return self.session_type == consts.SessionType.FINAL_RENDER

    def is_preview(self):
        return self.session_type == consts.SessionType.PREVIEW

    def is_export(self):
        return self.session_type == consts.SessionType.EXPORT

    def start_render(self, engine, context, depsgraph, is_viewport=True):
        node = OctaneNode(OctaneNodeType.SYNC_NODE)
        node.set_name("START_RENDER")
        node.set_node_type(consts.NodeType.NT_BLENDER_NODE_START_RENDER)
        region = context.region
        scene = depsgraph.scene
        node.set_blender_attribute("VIEWPORT_RENDER", consts.AttributeType.AT_BOOL, is_viewport)
        node.set_blender_attribute("ENABLE_OUT_OF_CORE", consts.AttributeType.AT_BOOL, False)
        node.set_blender_attribute("RENDER_PRIORITY", consts.AttributeType.AT_INT, 2)
        node.set_blender_attribute("RESOURCE_CACHE_TYPE", consts.AttributeType.AT_INT, 0)
        node.set_blender_attribute("OUTPUT_PATH", consts.AttributeType.AT_STRING, "")
        node.set_blender_attribute("CACHE_PATH", consts.AttributeType.AT_STRING, "")
        node.set_blender_attribute("RESOLUTION", consts.AttributeType.AT_INT2, (region.width, region.height))
        node.set_blender_attribute("IMAGE_TYPE", consts.AttributeType.AT_INT, 0)
        OctaneClient().process_octane_node(node)
        _thread.start_new_thread(start_session, (self, engine))

    def stop_render(self, engine, context, depsgraph):
        node = OctaneNode(OctaneNodeType.SYNC_NODE)
        node.set_name("STOP_RENDER")
        node.set_node_type(consts.NodeType.NT_BLENDER_NODE_STOP_RENDER)
        node.set_blender_attribute("FPS", consts.AttributeType.AT_FLOAT, 24)
        node.set_blender_attribute("IS_ALEMBIC", consts.AttributeType.AT_BOOL, False)
        OctaneClient().process_octane_node(node)

    def reset_render(self, engine, context, depsgraph, is_viewport=True):
        node = OctaneNode(OctaneNodeType.SYNC_NODE)
        node.set_name("RESET_RENDER")
        node.set_node_type(consts.NodeType.NT_BLENDER_NODE_RESET_RENDER)
        node.set_blender_attribute("VIEWPORT_RENDER", consts.AttributeType.AT_BOOL, is_viewport)
        node.set_blender_attribute("FPS", consts.AttributeType.AT_FLOAT, 24)
        node.set_blender_attribute("FRAME_TIME_SAMPLING", consts.AttributeType.AT_FLOAT, 100.0)
        node.set_blender_attribute("DEEP_IMAGE", consts.AttributeType.AT_BOOL, False)
        node.set_blender_attribute("WITH_OBJECT_LAYER", consts.AttributeType.AT_BOOL, False)
        node.set_blender_attribute("EXPORT_TYPE", consts.AttributeType.AT_INT, 0)
        node.set_blender_attribute("OUTPUT_PATH", consts.AttributeType.AT_STRING, "")
        node.set_blender_attribute("CACHE_PATH", consts.AttributeType.AT_STRING, "")
        OctaneClient().process_octane_node(node)

    def view_update(self, engine, context, depsgraph):
        # check diff        
        self.object_cache.diff(engine, context, depsgraph)                
        self.image_cache.diff(engine, context, depsgraph)        
        self.material_cache.diff(engine, context, depsgraph)
        self.world_cache.diff(engine, context, depsgraph)
        self.composite_cache.diff(engine, context, depsgraph)
        self.render_aov_cache.diff(engine, context, depsgraph)
        self.kernel_cache.diff(engine, context, depsgraph)
        self.scene_cache.diff(engine, context, depsgraph)
        # update
        if self.object_cache.need_update:
            self.object_cache.update(engine, context, depsgraph)        
        if self.image_cache.need_update:
            self.image_cache.update(engine, context, depsgraph)        
        if self.material_cache.need_update:
            self.material_cache.update(engine, context, depsgraph)
        if self.world_cache.need_update:
            self.world_cache.update(engine, context, depsgraph)
        if self.composite_cache.need_update:
            self.composite_cache.update(engine, context, depsgraph)
        if self.render_aov_cache.need_update:
            self.render_aov_cache.update(engine, context, depsgraph)
        if self.kernel_cache.need_update:
            self.kernel_cache.update(engine, context, depsgraph)
        if self.scene_cache.need_update:
            self.scene_cache.update(engine, context, depsgraph)
        self.scene_cache.update_camera(engine, context, depsgraph)
        # update render target
        if self.rendertarget_cache.diff(engine, context, depsgraph):
            self.rendertarget_cache.update(engine, context, depsgraph)

    def view_draw(self, engine, context, depsgraph):
        region = context.region
        scene = depsgraph.scene
        self.scene_cache.update_camera(engine, context, depsgraph)
        self.render_result.update_pixel_array(region.width, region.height, 0)

    def grab_render_result(self, engine):
        if self.render_result:
            self.render_result.update_pixel_array()
            engine.tag_redraw()
            # engine.draw_render_result(self.render_result)

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
                    self.add_to_update_node_queue(octane_node)
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