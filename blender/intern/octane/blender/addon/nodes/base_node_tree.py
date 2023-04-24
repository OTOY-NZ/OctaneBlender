import bpy
from bpy.app.handlers import persistent
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class
from bl_ui.space_node import NODE_HT_header, NODE_MT_editor_menus
from octane.utils import consts
from octane import core


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

    @staticmethod
    def update_active_output_name(node_tree, context, name, active):
        from octane.nodes.base_node import OctaneBaseOutputNode
        if "active_output_name" not in node_tree:
            node_tree["active_output_name"] = name if active else ""
        if active:
            for node in node_tree.nodes:
                if node.name != name and isinstance(node, OctaneBaseOutputNode):
                    if node.active:
                        node.set_active(context, False)
            node_tree["active_output_name"] = name
        else:
            if name == node_tree["active_output_name"]:
                node_tree["active_output_name"] = ""    

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


_NODE_HT_header_draw = None

def NODE_HT_header_octane_draw(self, context):
    layout = self.layout

    scene = context.scene
    snode = context.space_data
    snode_id = snode.id
    id_from = snode.id_from
    tool_settings = context.tool_settings
    is_compositor = snode.tree_type == 'CompositorNodeTree'

    if snode.tree_type not in (consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneNodeTreeIDName.RENDER_AOV, consts.OctaneNodeTreeIDName.KERNEL,consts.OctaneNodeTreeIDName.CAMERA_IMAGER,):
        _NODE_HT_header_draw(self, context)
        return

    layout.template_header()

    # Now expanded via the 'ui_type'
    # layout.prop(snode, "tree_type", text="")

    if snode.tree_type == 'ShaderNodeTree':
        layout.prop(snode, "shader_type", text="")

        ob = context.object
        if snode.shader_type == 'OBJECT' and ob:
            ob_type = ob.type

            NODE_MT_editor_menus.draw_collapsible(context, layout)

            # No shader nodes for Eevee lights
            if snode_id and not (context.engine == 'BLENDER_EEVEE' and ob_type == 'LIGHT'):
                row = layout.row()
                row.prop(snode_id, "use_nodes")

            layout.separator_spacer()

            types_that_support_material = {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META',
                                           'GPENCIL', 'VOLUME', 'HAIR', 'POINTCLOUD'}
            # disable material slot buttons when pinned, cannot find correct slot within id_from (T36589)
            # disable also when the selected object does not support materials
            has_material_slots = not snode.pin and ob_type in types_that_support_material

            if ob_type != 'LIGHT':
                row = layout.row()
                row.enabled = has_material_slots
                row.ui_units_x = 4
                row.popover(panel="NODE_PT_material_slots")

            row = layout.row()
            row.enabled = has_material_slots

            # Show material.new when no active ID/slot exists
            if not id_from and ob_type in types_that_support_material:
                row.template_ID(ob, "active_material", new="material.new")
            # Material ID, but not for Lights
            if id_from and ob_type != 'LIGHT':
                row.template_ID(id_from, "active_material", new="material.new")

        if snode.shader_type == 'WORLD':
            NODE_MT_editor_menus.draw_collapsible(context, layout)

            if snode_id:
                row = layout.row()
                row.prop(snode_id, "use_nodes")

            layout.separator_spacer()

            row = layout.row()
            row.enabled = not snode.pin
            row.template_ID(scene, "world", new="world.new")

        if snode.shader_type == 'LINESTYLE':
            view_layer = context.view_layer
            lineset = view_layer.freestyle_settings.linesets.active

            if lineset is not None:
                NODE_MT_editor_menus.draw_collapsible(context, layout)

                if snode_id:
                    row = layout.row()
                    row.prop(snode_id, "use_nodes")

                layout.separator_spacer()

                row = layout.row()
                row.enabled = not snode.pin
                row.template_ID(lineset, "linestyle", new="scene.freestyle_linestyle_new")

    elif snode.tree_type == 'TextureNodeTree':
        layout.prop(snode, "texture_type", text="")

        NODE_MT_editor_menus.draw_collapsible(context, layout)

        if snode_id:
            layout.prop(snode_id, "use_nodes")

        layout.separator_spacer()

        if id_from:
            if snode.texture_type == 'BRUSH':
                layout.template_ID(id_from, "texture", new="texture.new")
            else:
                layout.template_ID(id_from, "active_texture", new="texture.new")

    elif snode.tree_type == 'CompositorNodeTree':

        NODE_MT_editor_menus.draw_collapsible(context, layout)

        if snode_id:
            layout.prop(snode_id, "use_nodes")

    elif snode.tree_type == 'GeometryNodeTree':
        NODE_MT_editor_menus.draw_collapsible(context, layout)
        layout.separator_spacer()

        ob = context.object

        row = layout.row()
        if snode.pin:
            row.enabled = False
            row.template_ID(snode, "node_tree", new="node.new_geometry_node_group_assign")
        elif ob:
            active_modifier = ob.modifiers.active
            if active_modifier and active_modifier.type == 'NODES':
                if active_modifier.node_group:
                    row.template_ID(active_modifier, "node_group", new="node.copy_geometry_node_group_assign")
                else:
                    row.template_ID(active_modifier, "node_group", new="node.new_geometry_node_group_assign")
            else:
                row.template_ID(snode, "node_tree", new="node.new_geometry_nodes_modifier")

    else:
        # Custom node tree is edited as independent ID block
        NODE_MT_editor_menus.draw_collapsible(context, layout)

        layout.separator_spacer()

        layout.template_ID(snode, "node_tree", new="node.new_node_tree")

        if snode.tree_type == consts.OctaneNodeTreeIDName.COMPOSITE:
            layout.separator()
            layout.operator("octane.quick_add_composite_nodetree", icon="NODETREE", text="Quick-Add NodeTree")
        elif snode.tree_type == consts.OctaneNodeTreeIDName.RENDER_AOV:
            layout.separator()
            layout.operator("octane.quick_add_render_aov_nodetree", icon="NODETREE", text="Quick-Add NodeTree")
        elif snode.tree_type == consts.OctaneNodeTreeIDName.KERNEL:
            layout.separator()
            layout.operator("octane.quick_add_kernel_nodetree", icon="NODETREE", text="Quick-Add NodeTree")

    # Put pin next to ID block
    if not is_compositor:
        layout.prop(snode, "pin", text="", emboss=False)

    layout.separator_spacer()

    # Put pin on the right for Compositing
    if is_compositor:
        layout.prop(snode, "pin", text="", emboss=False)

    layout.operator("node.tree_path_parent", text="", icon='FILE_PARENT')

    # Backdrop
    if is_compositor:
        row = layout.row(align=True)
        row.prop(snode, "show_backdrop", toggle=True)
        sub = row.row(align=True)
        sub.active = snode.show_backdrop
        sub.prop(snode, "backdrop_channels", icon_only=True, text="", expand=True)

    # Snap
    row = layout.row(align=True)
    row.prop(tool_settings, "use_snap", text="")
    row.prop(tool_settings, "snap_node_element", icon_only=True)
    if tool_settings.snap_node_element != 'GRID':
        row.prop(tool_settings, "snap_target", text="")


class OCTANE_quick_add_composite_nodetree(bpy.types.Operator):
    """Add an Octane Composite node tree with the default node configuration"""
    
    bl_idname = "octane.quick_add_composite_nodetree"
    bl_label = "Quick-Add Composite NodeTree"
    bl_description = "Add an Octane Composite node tree with the default node configuration"

    def execute(self, context):
        from octane.utils import utility
        name = "Comp"
        node_tree = bpy.data.node_groups.new(name=name, type=consts.OctaneNodeTreeIDName.COMPOSITE)
        node_tree.use_fake_user = True
        nodes = node_tree.nodes
        output = nodes.new("OctaneAOVOutputGroupOutputNode")
        output.location = (0, 0)
        aov_output_group = nodes.new("OctaneAOVOutputGroup")
        aov_output_group.location = (-300, 0)
        node_tree.links.new(aov_output_group.outputs[0], output.inputs[0])        
        utility.show_nodetree(context, node_tree)
        return {"FINISHED"}


class OCTANE_quick_add_render_aov_nodetree(bpy.types.Operator):
    """Add an Octane Render AOV node tree with the default node configuration"""
    
    bl_idname = "octane.quick_add_render_aov_nodetree"
    bl_label = "Quick-Add Render AOV NodeTree"
    bl_description = "Add an Octane Render AOV node tree with the default node configuration"

    def execute(self, context):
        from octane.utils import utility
        name = "AOVs"
        node_tree = bpy.data.node_groups.new(name=name, type=consts.OctaneNodeTreeIDName.RENDER_AOV)
        node_tree.use_fake_user = True
        nodes = node_tree.nodes
        output = nodes.new("OctaneRenderAOVsOutputNode")
        output.location = (0, 0)
        render_aov_group = nodes.new("OctaneRenderAOVGroup")
        render_aov_group.location = (-300, 0)
        node_tree.links.new(render_aov_group.outputs[0], output.inputs[0])
        utility.show_nodetree(context, node_tree)        
        return {"FINISHED"}


class OCTANE_quick_add_kernel_nodetree(bpy.types.Operator):
    """Add an Octane Kernel node tree with the default node configuration"""
    
    bl_idname = "octane.quick_add_kernel_nodetree"
    bl_label = "Quick-Add Kernel NodeTree"
    bl_description = "Add an Octane Kernel node tree with the default node configuration"

    def execute(self, context):
        from octane.utils import utility
        node_tree = utility.quick_add_octane_kernel_node_tree()
        utility.show_nodetree(context, node_tree)        
        return {"FINISHED"}


class NodeTreeHandler:    
    material_node_tree_count = 0
    world_node_tree_count = 0
    light_node_tree_count = 0
    MATERIAL_OUTPUT_NODE_NAME = "Material Output"
    WORLD_OUTPUT_NODE_NAME = "World Output"
    LIGHT_OUTPUT_NODE_NAME = "Light Output"
    SURFACE_INPUT_NAME = "Surface"
    VOLUME_INPUT_NAME = "Volume"
    WORLD_INPUT_NAME = "Surface"
    OCTANE_WORLD_INPUT_NAME = "Environment"

    @staticmethod
    def init_helper_color_ramp_watcher():
        def _init_helper_color_ramp_watcher(node_tree):
            from octane.nodes.base_color_ramp import OctaneBaseRampNode
            for node in node_tree.nodes:
                if isinstance(node, OctaneBaseRampNode):
                    node.init_helper_color_ramp_watcher()
        for material in bpy.data.materials:
            if material.use_nodes and material.node_tree:
                _init_helper_color_ramp_watcher(material.node_tree)

    @staticmethod
    def init_octane_kernel():        
        if consts.OctanePresetNodeTreeNames.KERNEL not in bpy.data.node_groups:
            from octane.utils import utility
            utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True)

    @staticmethod
    def on_file_load(scene):
        from octane.utils import utility
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)
        NodeTreeHandler.light_node_tree_count = NodeTreeHandler.get_light_node_tree_count(scene)
        utility.update_active_render_aov_node_tree(bpy.context)
        # Init color ramp watchers
        NodeTreeHandler.init_helper_color_ramp_watcher()
        # Init kernel and camera imager
        NodeTreeHandler.init_octane_kernel()

    @staticmethod
    def convert_to_octane_new_addon_node(node_tree, output_node, new_output_node, socket_name, new_socket_name, octane_node_type, octane_node_output_name=None):
        _input = output_node.inputs[socket_name]
        if len(_input.links):            
            from_node = _input.links[0].from_node
            # Do not convert new add-on style nodes and old octane nodes
            if hasattr(from_node, "octane_node_type") or from_node.bl_idname.startswith("ShaderNodeOct"):
                return
            octane_node = node_tree.nodes.new(octane_node_type)
            octane_node.location = from_node.location
            octane_output_socket = None
            if octane_node_output_name is None:
                octane_output_socket = octane_node.outputs[0]
            else:
                octane_output_socket = octane_node.outputs[octane_node_output_name]
            final_output_node = new_output_node if new_output_node is not None else output_node
            node_tree.links.new(octane_output_socket, final_output_node.inputs[new_socket_name])
            node_tree.nodes.remove(from_node)

    @staticmethod
    def on_material_new(scene):
        from octane.nodes import base_output_node
        if len(bpy.data.materials) > NodeTreeHandler.material_node_tree_count:            
            active_object = bpy.context.active_object
            active_material = None
            node_tree = None
            if active_object:
                active_material = active_object.active_material
            if active_material and active_material.use_nodes:
                node_tree = active_material.node_tree
            if node_tree and NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME in node_tree.nodes:
                blender_output = node_tree.nodes[NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME]
                if core.ENABLE_OCTANE_ADDON_CLIENT:                    
                    output = node_tree.nodes.new("OctaneEditorMaterialOutputNode")
                    output.location = blender_output.location
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, output, NodeTreeHandler.SURFACE_INPUT_NAME, NodeTreeHandler.SURFACE_INPUT_NAME, "OctaneUniversalMaterial")
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, output, NodeTreeHandler.VOLUME_INPUT_NAME, NodeTreeHandler.VOLUME_INPUT_NAME, "OctaneVolumeMedium")
                    node_tree.nodes.remove(blender_output)
                else:
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, blender_output, NodeTreeHandler.SURFACE_INPUT_NAME, NodeTreeHandler.SURFACE_INPUT_NAME, "OctaneUniversalMaterial")
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, blender_output, NodeTreeHandler.VOLUME_INPUT_NAME, NodeTreeHandler.VOLUME_INPUT_NAME, "OctaneVolumeMedium")                    

        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        
    @staticmethod
    def on_world_new(scene):
        from octane.nodes import base_output_node
        if len(bpy.data.worlds) > NodeTreeHandler.world_node_tree_count:
            active_world = scene.world
            node_tree = None
            if active_world and active_world.use_nodes:
                node_tree = active_world.node_tree
            if node_tree and NodeTreeHandler.WORLD_OUTPUT_NODE_NAME in node_tree.nodes:
                blender_output = node_tree.nodes[NodeTreeHandler.WORLD_OUTPUT_NODE_NAME]
                if core.ENABLE_OCTANE_ADDON_CLIENT:
                    output = node_tree.nodes.new("OctaneEditorWorldOutputNode")
                    output.location = blender_output.location
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, output, NodeTreeHandler.WORLD_INPUT_NAME, NodeTreeHandler.OCTANE_WORLD_INPUT_NAME, "OctaneTextureEnvironment")
                    node_tree.nodes.remove(blender_output)
                else:
                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, blender_output, NodeTreeHandler.WORLD_INPUT_NAME, "Octane Environment", "OctaneTextureEnvironment")
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)

    @staticmethod
    def get_light_node_tree_count(scene):
        return len([light.node_tree for light in bpy.data.lights if light.node_tree is not None])

    @staticmethod
    def on_light_new(scene):
        from octane.nodes import base_output_node
        current_light_node_tree_count = NodeTreeHandler.get_light_node_tree_count(scene)
        if current_light_node_tree_count > NodeTreeHandler.light_node_tree_count:
            active_object = bpy.context.active_object
            if active_object.type == "LIGHT":
                light_data = active_object.data
                node_tree = None
                if light_data:
                    node_tree = light_data.node_tree
                if node_tree and NodeTreeHandler.LIGHT_OUTPUT_NODE_NAME in node_tree.nodes:
                    output = node_tree.nodes[NodeTreeHandler.LIGHT_OUTPUT_NODE_NAME]
                    if light_data.type == "POINT":
                        NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output, NodeTreeHandler.SURFACE_INPUT_NAME, NodeTreeHandler.SURFACE_INPUT_NAME, "ShaderNodeOctToonPointLight")
                    elif light_data.type == "SUN":
                        NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output, NodeTreeHandler.SURFACE_INPUT_NAME, NodeTreeHandler.SURFACE_INPUT_NAME, "ShaderNodeOctToonDirectionLight")
                    elif light_data.type in ("AREA", "MESH", "SPHERE"):
                        NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output, NodeTreeHandler.SURFACE_INPUT_NAME, NodeTreeHandler.SURFACE_INPUT_NAME, "OctaneDiffuseMaterial")
                        material_node = node_tree.nodes["Diffuse material"]
                        emission_node = node_tree.nodes.new("OctaneTextureEmission")
                        emission_node.location = (material_node.location.x - 300, material_node.location.y)
                        node_tree.links.new(emission_node.outputs[0], material_node.inputs["Emission"])
        NodeTreeHandler.light_node_tree_count = current_light_node_tree_count

    @staticmethod
    def blender_internal_node_tree_update_handler(scene, depsgraph=None):
        NodeTreeHandler.on_material_new(scene)
        NodeTreeHandler.on_world_new(scene)
        NodeTreeHandler.on_light_new(scene)
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


_CLASSES = [
    OCTANE_quick_add_composite_nodetree,
    OCTANE_quick_add_render_aov_nodetree,
    OCTANE_quick_add_kernel_nodetree,
]


def register():
    global _NODE_HT_header_draw
    _NODE_HT_header_draw = NODE_HT_header.draw
    NODE_HT_header.draw = NODE_HT_header_octane_draw
    bpy.app.handlers.load_post.append(node_tree_initialization_handler)
    bpy.app.handlers.depsgraph_update_post.append(node_tree_update_handler)
    for cls in _CLASSES:
        register_class(cls)
    

def unregister():
    global _NODE_HT_header_draw
    NODE_HT_header.draw = _NODE_HT_header_draw
    bpy.app.handlers.load_post.remove(node_tree_initialization_handler)
    bpy.app.handlers.depsgraph_update_post.remove(node_tree_update_handler)
    for cls in _CLASSES:
        unregister_class(cls)    
