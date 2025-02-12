# <pep8 compliant>

import bpy
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class

from octane import core
from octane.utils import consts, logger, utility


class OctaneBaseNodeTree(object):
    USE_LEGACY_NODE = True
    LEGACY_OUTPUT_SOCKET_CONVERSION_MAP = {
        "OutGeo": consts.PinType.PT_GEOMETRY,
        "OutTex": consts.PinType.PT_UNKNOWN,  # (consts.PinType.PT_TEXTURE, consts.PinType.PT_TOON_RAMP),
        "OutMat": consts.PinType.PT_MATERIAL,
        "OutMatLayer": consts.PinType.PT_MATERIAL_LAYER,
        "OutMedium": consts.PinType.PT_MEDIUM,
        "OutRotation": consts.PinType.PT_UNKNOWN,  # (consts.PinType.PT_TRANSFORM, consts.PinType.PT_FLOAT),
        "OutTransform": consts.PinType.PT_TRANSFORM,
        "OutProjection": consts.PinType.PT_PROJECTION,
        "OutAOV": consts.PinType.PT_OUTPUT_AOV,
        "OutLayer": consts.PinType.PT_OUTPUT_AOV_LAYER,
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
        # noinspection PyTypeChecker
        self.update_link_validity(self, utility.find_node_tree_owner(self), None)

        # Ensure the viewport update

    def update_viewport(self):
        self.update_tag()

    @staticmethod
    def resolve_socket_octane_pin_type(node_tree, socket):
        socket_pin_type = getattr(socket, "octane_pin_type", consts.PinType.PT_UNKNOWN)
        if getattr(node_tree, "USE_LEGACY_NODE", True):
            if socket_pin_type == consts.PinType.PT_UNKNOWN:
                socket_name = getattr(socket, "name", "")
                if socket_name in OctaneBaseNodeTree.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP:
                    socket_pin_type = OctaneBaseNodeTree.LEGACY_OUTPUT_SOCKET_CONVERSION_MAP[socket_name]
        return socket_pin_type

    @staticmethod
    def update_link_validity_for_blender_insert_links(node_tree, last_op_bl_idname=None):
        try:
            is_node_op = last_op_bl_idname is None or last_op_bl_idname.startswith(
                "NODE_OT") or last_op_bl_idname.startswith("OCTANE_OT_node")
        except Exception as e:
            logger.exception(e)
            is_node_op = True
        if not is_node_op:
            return
        # Check the "Insert link" feature of the Blender
        if len(node_tree.links) > 2:
            selected_nodes = [node for node in node_tree.nodes if node.select]
            if len(selected_nodes) == 1:
                selected_node = selected_nodes[0]
                link1 = None
                link2 = None
                for _input in selected_node.inputs:
                    if _input.is_linked:
                        link1 = _input.links[0]
                        break
                if len(selected_node.outputs) >= 1 and selected_node.outputs[0].is_linked:
                    link2 = selected_node.outputs[0].links[0]
                # Detect the link status
                if link1 and link2:
                    insert_in_link = None
                    insert_out_link = None
                    if link1.from_node == selected_node and link2.to_node == selected_node:
                        insert_in_link = link2
                        insert_out_link = link1
                    elif link2.from_node == selected_node and link1.to_node == selected_node:
                        insert_in_link = link1
                        insert_out_link = link2
                    if insert_in_link and insert_out_link:
                        if not insert_in_link.is_valid:
                            # Find the compatible socket to link
                            from_socket_pin_type = (
                                OctaneBaseNodeTree.resolve_socket_octane_pin_type(node_tree,
                                                                                  insert_in_link.from_socket))
                            for to_socket in selected_node.inputs:
                                to_socket_pin_type = OctaneBaseNodeTree.resolve_socket_octane_pin_type(node_tree,
                                                                                                       to_socket)
                                if from_socket_pin_type == to_socket_pin_type:
                                    node_tree.links.new(insert_in_link.from_socket, to_socket)
                                    if insert_in_link in set(node_tree.links):
                                        node_tree.links.remove(insert_in_link)
                                    break

    @staticmethod
    def update_link_validity(node_tree, data_owner, last_op_bl_idname=None):
        for link in node_tree.links:
            from_socket = link.from_socket
            to_socket = link.to_socket
            if from_socket and to_socket:
                from_socket_pin_type = OctaneBaseNodeTree.resolve_socket_octane_pin_type(node_tree, from_socket)
                to_socket_pin_type = OctaneBaseNodeTree.resolve_socket_octane_pin_type(node_tree, to_socket)
                if from_socket_pin_type == consts.PinType.PT_UNKNOWN:
                    continue
                if to_socket_pin_type == consts.PinType.PT_UNKNOWN:
                    continue
                if from_socket_pin_type != to_socket_pin_type:
                    link.is_valid = False
        OctaneBaseNodeTree.update_link_validity_for_blender_insert_links(node_tree, last_op_bl_idname)
        OctaneBaseNodeTree.update_special_node_validity(node_tree, data_owner, last_op_bl_idname)

    @staticmethod
    def update_special_node_validity(node_tree, data_owner, last_op_bl_idname=None):
        # Ramp Node
        from octane.nodes.base_color_ramp import OctaneBaseRampNode
        # Curve Node
        from octane.nodes.base_curve import OctaneBaseCurveNode
        from octane.operators_.node_tree import OCTANE_OT_convert_to_octane_node
        original_node_tree = node_tree.original
        for node in original_node_tree.nodes:
            if isinstance(node, OctaneBaseRampNode):
                node.validate_color_ramp(data_owner)
            elif isinstance(node, OctaneBaseCurveNode):
                node.validate(data_owner)
        # If Adding Cycles Image Node?
        if last_op_bl_idname == "NODE_OT_add_file":
            if len(original_node_tree.nodes) and original_node_tree.nodes[-1].select \
                    and original_node_tree.nodes[-1].bl_idname == "ShaderNodeTexImage":
                OCTANE_OT_convert_to_octane_node.convert_tex_image_node(None, original_node_tree.nodes[-1])


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
    def init_node_helper():
        from octane.nodes.base_image import OctaneBaseImageNode
        OctaneBaseImageNode.get_octane_image_helper()

    @staticmethod
    def init_octane_node_helper():
        from octane.nodes.base_color_ramp import OctaneBaseRampNode
        from octane.nodes.base_curve import OctaneBaseCurveNode
        from octane.nodes.base_wrapper_node import OctaneScriptNodeWrapper

        def nest_init_octane_node_helper(node_tree, current_used_color_ramp_names, current_used_curve_names,
                                         data_owner):
            original_node_tree = node_tree.original
            for node in original_node_tree.nodes:
                if isinstance(node, OctaneBaseRampNode):
                    node.init_helper_color_ramp_watcher()
                    node.validate_color_ramp(data_owner, True)
                    current_used_color_ramp_names.add(node.color_ramp_name)
                elif isinstance(node, OctaneBaseCurveNode):
                    node.init_helper_curve_watcher()
                    node.validate(data_owner, True)
                    current_used_curve_names.add(node.curve_name)
                elif isinstance(node, OctaneScriptNodeWrapper):
                    node.update_shader_code()

        used_color_ramp_names = set()
        used_curve_names = set()
        for material in bpy.data.materials:
            if material.use_nodes and material.node_tree:
                nest_init_octane_node_helper(material.node_tree, used_color_ramp_names, used_curve_names, material)
        for world in bpy.data.worlds:
            if world.use_nodes and world.node_tree:
                nest_init_octane_node_helper(world.node_tree, used_color_ramp_names, used_curve_names, world)
        for light in bpy.data.lights:
            if light.use_nodes and light.node_tree:
                nest_init_octane_node_helper(light.node_tree, used_color_ramp_names, used_curve_names, light)
        for node_group in bpy.data.node_groups:
            nest_init_octane_node_helper(node_group, used_color_ramp_names, used_curve_names, node_group)
        OctaneBaseRampNode.clear_unused_color_ramp_helpers(used_color_ramp_names)
        OctaneBaseCurveNode.clear_unused_curve_helpers(used_curve_names)

    @staticmethod
    def init_octane_kernel():
        from octane.utils import utility
        octane_scene = bpy.context.scene.octane
        if octane_scene.kernel_data_mode == "PROPERTY_PANEL":
            from octane.utils import utility
            utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True,
                                                      generate_from_legacy_octane_property=True)
            octane_scene.kernel_data_mode = "NODETREE"
        else:
            if octane_scene.kernel_node_graph_property.node_tree is None:
                utility.quick_add_octane_kernel_node_tree(assign_to_kernel_node_graph=True)

    @staticmethod
    def convert_legacy_worlds(scene):
        if scene.world:
            world = scene.world
            node_tree = world.node_tree
            if not core.ENABLE_OCTANE_ADDON_CLIENT:
                utility.convert_to_addon_node_tree(world, node_tree, bpy.context, None)
            else:
                if node_tree and NodeTreeHandler.WORLD_OUTPUT_NODE_NAME in node_tree.nodes:
                    node_bl_idnames = [node.bl_idname for node in node_tree.nodes]
                    if "ShaderNodeOutputWorld" in node_bl_idnames and "NodeUndefined" in node_bl_idnames:
                        # Convert legacy environment node
                        original_env_node = None
                        addon_env_node = None
                        original_sun_direction_node = None
                        original_env_bl_idname = ""
                        addon_env_bl_idname = ""
                        original_sun_direction_bl_idname = ""
                        addon_sun_direction_bl_idname = ""
                        for node in world.node_tree.nodes:
                            if node.bl_idname == "NodeUndefined":
                                if len(node.outputs) and node.outputs[0].name == "OutEnv":
                                    if "Star field" in node.inputs:
                                        original_env_node = node
                                        original_env_bl_idname = "ShaderNodeOctPlanetaryEnvironment"
                                        addon_env_bl_idname = "OctanePlanetaryEnvironment"
                                    elif "Sky color" in node.inputs:
                                        original_env_node = node
                                        original_env_bl_idname = "ShaderNodeOctDaylightEnvironment"
                                        addon_env_bl_idname = "OctaneDaylightEnvironment"
                                    else:
                                        original_env_node = node
                                        original_env_bl_idname = "ShaderNodeOctTextureEnvironment"
                                        addon_env_bl_idname = "OctaneTextureEnvironment"
                                elif len(node.outputs) and node.outputs[0].name == "OutValue":
                                    if "Month" in node.inputs and "Day" in node.inputs and "GMT offset" in node.inputs:
                                        original_sun_direction_node = node
                                        original_sun_direction_bl_idname = "ShaderNodeOctSunDirectionValue"
                                        addon_sun_direction_bl_idname = "OctaneSunDirection"
                        # Create a new world
                        new_world = bpy.data.worlds.new(world.name)
                        new_world.use_nodes = True
                        NodeTreeHandler._on_world_new(new_world.node_tree, new_world, None, addon_env_bl_idname)
                        for node in new_world.node_tree.nodes:
                            if node.bl_idname == addon_env_bl_idname:
                                addon_env_node = node
                            elif node.bl_idname == addon_sun_direction_bl_idname:
                                pass
                        if original_env_node and addon_env_node:
                            addon_env_node.load_legacy_node(original_env_node, original_env_bl_idname, world.node_tree,
                                                            bpy.context, None)
                        if original_sun_direction_node and addon_env_node and "Sun direction" in addon_env_node.inputs:
                            addon_sun_direction_node = new_world.node_tree.nodes.new(addon_sun_direction_bl_idname)
                            addon_sun_direction_node.load_legacy_node(original_sun_direction_node,
                                                                      original_sun_direction_bl_idname, world.node_tree,
                                                                      bpy.context, None)
                            new_world.node_tree.links.new(addon_sun_direction_node.outputs[0],
                                                          addon_env_node.inputs["Sun direction"])
                        utility.beautifier_nodetree_layout_by_owner(new_world)
                        scene.world = new_world

    @staticmethod
    def on_file_load(scene):
        from octane.utils import utility
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)
        NodeTreeHandler.light_node_tree_count = NodeTreeHandler.get_light_node_tree_count(scene)
        if scene.render.engine != consts.ENGINE_NAME:
            return
        utility.update_active_render_aov_node_tree(bpy.context.view_layer)
        # Init node helper
        NodeTreeHandler.init_node_helper()
        # Init color ramp watchers
        NodeTreeHandler.init_octane_node_helper()
        # Init kernel
        NodeTreeHandler.init_octane_kernel()
        # Convert legacy worlds
        NodeTreeHandler.convert_legacy_worlds(scene)

    @staticmethod
    def convert_to_octane_new_addon_node(node_tree, output_node, new_output_node, socket_name, new_socket_name,
                                         octane_node_type, octane_node_output_name=None):
        _input = output_node.inputs[socket_name]
        if len(_input.links):
            from_node = _input.links[0].from_node
            # Do not convert new add-on style nodes
            if hasattr(from_node, "octane_node_type"):
                return False
            # Do not convert legacy octane nodes or group nodes
            if from_node.bl_idname.startswith("ShaderNodeOct") or from_node.bl_idname == "ShaderNodeGroup":
                return False
            octane_node = node_tree.nodes.new(octane_node_type)
            octane_node.location = from_node.location
            if octane_node_output_name is None:
                octane_output_socket = octane_node.outputs[0]
            else:
                octane_output_socket = octane_node.outputs[octane_node_output_name]
            final_output_node = new_output_node if new_output_node is not None else output_node
            node_tree.links.new(octane_output_socket, final_output_node.inputs[new_socket_name])
            node_tree.nodes.remove(from_node)
            return True
        return False

    @staticmethod
    def _is_blender_default_material(node_tree):
        if node_tree and len(node_tree.nodes) == 2:
            node_names = [node.name for node in node_tree.nodes]
            if "Material Output" in node_names and "Principled BSDF" in node_names:
                return True
        return False

    @staticmethod
    def _is_blender_default_volume(node_tree):
        if node_tree and len(node_tree.nodes) == 2:
            node_names = [node.name for node in node_tree.nodes]
            if "Material Output" in node_names and "Principled Volume" in node_names:
                return True
        return False

    @staticmethod
    def _on_material_new(node_tree, data_owner, last_op_bl_idname=None):
        if node_tree and NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME in node_tree.nodes:
            blender_output = node_tree.nodes[NodeTreeHandler.MATERIAL_OUTPUT_NODE_NAME]
            if NodeTreeHandler._is_blender_default_material(node_tree):
                material_node_bl_idname = utility.get_default_material_node_bl_idname()
                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, blender_output,
                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                 material_node_bl_idname)
            elif NodeTreeHandler._is_blender_default_volume(node_tree):
                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, blender_output,
                                                                 NodeTreeHandler.VOLUME_INPUT_NAME,
                                                                 NodeTreeHandler.VOLUME_INPUT_NAME,
                                                                 "OctaneVolumeMedium")
            if blender_output and getattr(blender_output, "target", None) == "":
                blender_output.target = "ALL"
        if node_tree:
            OctaneBaseNodeTree.update_link_validity(node_tree, data_owner, last_op_bl_idname)

    @staticmethod
    def on_material_new(_scene, last_op_bl_idname=None):
        if len(bpy.data.materials) > NodeTreeHandler.material_node_tree_count:
            active_object = bpy.context.active_object
            active_material = None
            node_tree = None
            if active_object:
                active_material = active_object.active_material
            if active_material and active_material.use_nodes:
                node_tree = active_material.node_tree
            NodeTreeHandler._on_material_new(node_tree, active_material, last_op_bl_idname)
            for idx in range(NodeTreeHandler.material_node_tree_count, len(bpy.data.materials)):
                current_material = bpy.data.materials[idx]
                if current_material.node_tree is not node_tree:
                    NodeTreeHandler._on_material_new(current_material.node_tree, current_material, last_op_bl_idname)
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)

    @staticmethod
    def _is_blender_default_world(node_tree):
        if node_tree and len(node_tree.nodes) == 2:
            node_names = [node.name for node in node_tree.nodes]
            if "World Output" in node_names and "Background" in node_names:
                return True
        return False

    @staticmethod
    def _on_world_new(node_tree, data_owner, last_op_bl_idname=None,
                      environment_bl_idname="OctaneTextureEnvironment"):
        if node_tree and NodeTreeHandler.WORLD_OUTPUT_NODE_NAME in node_tree.nodes:
            if NodeTreeHandler._is_blender_default_world(node_tree):
                blender_output = node_tree.nodes[NodeTreeHandler.WORLD_OUTPUT_NODE_NAME]
                output = node_tree.nodes.new("OctaneEditorWorldOutputNode")
                output.location = blender_output.location
                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, blender_output, output,
                                                                 NodeTreeHandler.WORLD_INPUT_NAME,
                                                                 NodeTreeHandler.OCTANE_WORLD_INPUT_NAME,
                                                                 environment_bl_idname)
                node_tree.nodes.remove(blender_output)
        if node_tree:
            OctaneBaseNodeTree.update_link_validity(node_tree, data_owner, last_op_bl_idname)

    @staticmethod
    def on_world_new(scene, last_op_bl_idname=None):
        if len(bpy.data.worlds) > NodeTreeHandler.world_node_tree_count:
            active_world = scene.world
            node_tree = None
            if active_world and active_world.use_nodes:
                node_tree = active_world.node_tree
            NodeTreeHandler._on_world_new(node_tree, active_world, last_op_bl_idname)
            for idx in range(NodeTreeHandler.world_node_tree_count, len(bpy.data.worlds)):
                current_world = bpy.data.worlds[idx]
                if current_world.node_tree is not node_tree:
                    NodeTreeHandler._on_world_new(current_world.node_tree, current_world, last_op_bl_idname)
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)

    @staticmethod
    def get_light_node_tree_count(_scene):
        return len([light.node_tree for light in bpy.data.lights if light.node_tree is not None])

    @staticmethod
    def _is_blender_default_light(node_tree):
        if node_tree and len(node_tree.nodes) == 2:
            node_names = [node.name for node in node_tree.nodes]
            if "Light Output" in node_names and "Emission" in node_names:
                return True
        return False

    @staticmethod
    def on_light_new(scene, _last_op_bl_idname=None):
        current_light_node_tree_count = NodeTreeHandler.get_light_node_tree_count(scene)
        if current_light_node_tree_count > NodeTreeHandler.light_node_tree_count:
            active_object = bpy.context.active_object
            if active_object.type == "LIGHT":
                light_data = active_object.data
                node_tree = None
                if light_data:
                    node_tree = light_data.node_tree
                if node_tree and NodeTreeHandler.LIGHT_OUTPUT_NODE_NAME in node_tree.nodes:
                    if NodeTreeHandler._is_blender_default_light(node_tree):
                        output = node_tree.nodes[NodeTreeHandler.LIGHT_OUTPUT_NODE_NAME]
                        if light_data.type in ("POINT", "AREA", "MESH", "SPHERE"):
                            if light_data.type == "POINT":
                                if light_data.octane.octane_point_light_type == "Toon Point":
                                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                     NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                     NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                     "OctaneToonPointLight")
                                else:
                                    NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                     NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                     NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                     "OctaneDiffuseMaterial")
                                    material_node = node_tree.nodes["Diffuse material"]
                                    emission_node = node_tree.nodes.new("OctaneTextureEmission")
                                    node_tree.links.new(emission_node.outputs[0], material_node.inputs["Emission"])
                            else:
                                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 "OctaneDiffuseMaterial")
                                material_node = node_tree.nodes["Diffuse material"]
                                emission_node = node_tree.nodes.new("OctaneTextureEmission")
                                node_tree.links.new(emission_node.outputs[0], material_node.inputs["Emission"])
                        elif light_data.type == "SUN":
                            if light_data.octane.octane_directional_light_type == "Toon Directional":
                                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 "OctaneToonDirectionalLight")
                                light_node = node_tree.nodes["Toon directional light"]
                                utility.setup_directional_light(node_tree, light_node, active_object)
                            elif light_data.octane.octane_directional_light_type == "Analytical":
                                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 "OctaneAnalyticLight")
                                light_node = node_tree.nodes["Analytic light"]
                                emission_node = node_tree.nodes.new("OctaneTextureEmission")
                                node_tree.links.new(emission_node.outputs[0], light_node.inputs["Emission"])
                            else:
                                NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                                 "OctaneDirectionalLight")
                                light_node = node_tree.nodes["Directional light"]
                                emission_node = node_tree.nodes.new("OctaneTextureEmission")
                                node_tree.links.new(emission_node.outputs[0], light_node.inputs["Emission"])
                                utility.setup_directional_light(node_tree, light_node, active_object)
                        elif light_data.type == "SPOT":
                            NodeTreeHandler.convert_to_octane_new_addon_node(node_tree, output, output,
                                                                             NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                             NodeTreeHandler.SURFACE_INPUT_NAME,
                                                                             "OctaneVolumetricSpotlight")
                            light_data.spot_blend = 0
                            light_data.shadow_soft_size = 0
                        utility.beautifier_nodetree_layout_by_owner(light_data)
        NodeTreeHandler.light_node_tree_count = current_light_node_tree_count

    @staticmethod
    def blender_internal_node_tree_update_handler(scene, depsgraph, last_op_bl_idname=None):
        NodeTreeHandler.on_material_new(scene, last_op_bl_idname)
        NodeTreeHandler.on_world_new(scene, last_op_bl_idname)
        NodeTreeHandler.on_light_new(scene, last_op_bl_idname)
        is_active_object_updated = False
        is_active_world_updated = False
        for update in depsgraph.updates:
            node_tree = None
            data_owner = update.id
            if isinstance(update.id, bpy.types.NodeTree):
                node_tree = update.id
                data_owner = utility.find_node_tree_owner(node_tree)
            elif isinstance(update.id, bpy.types.Light):
                node_tree = update.id.node_tree
            elif isinstance(update.id, bpy.types.World):
                node_tree = update.id.node_tree
            elif isinstance(update.id, bpy.types.Material):
                node_tree = update.id.node_tree
            if node_tree is not None:
                if update.id is scene.world:
                    is_active_world_updated = True
                if update.id is getattr(bpy.context, "active_object", None):
                    is_active_object_updated = True
                OctaneBaseNodeTree.update_link_validity(node_tree, data_owner, last_op_bl_idname)
        if getattr(bpy.context, "active_object", None) and not is_active_object_updated:
            active_object = bpy.context.active_object
            data_owner = None
            node_tree = None
            if active_object.active_material and active_object.active_material.use_nodes:
                data_owner = active_object.active_material
                node_tree = active_object.active_material.node_tree
            if active_object.type == "LIGHT" and active_object.data.use_nodes:
                data_owner = active_object.data
                node_tree = active_object.data.node_tree
            if node_tree is not None:
                if data_owner is None:
                    data_owner = utility.find_node_tree_owner(node_tree)
                OctaneBaseNodeTree.update_link_validity(node_tree, data_owner, last_op_bl_idname)
        if scene.world and scene.world.use_nodes and not is_active_world_updated:
            OctaneBaseNodeTree.update_link_validity(scene.world.node_tree, scene.world, last_op_bl_idname)

    @staticmethod
    def update_node_tree_count(scene):
        NodeTreeHandler.material_node_tree_count = len(bpy.data.materials)
        NodeTreeHandler.world_node_tree_count = len(bpy.data.worlds)
        NodeTreeHandler.light_node_tree_count = NodeTreeHandler.get_light_node_tree_count(scene)


def node_tree_update_handler(scene):
    # last_op_bl_idname = bpy.context.window_manager.operators[-1].bl_idname
    # if len(bpy.context.window_manager.operators) else None
    last_op_bl_idname = bpy.context.active_operator.bl_idname if getattr(bpy.context, "active_operator",
                                                                         None) is not None else None
    if scene is None:
        scene = bpy.context.scene
    if scene.render.engine != consts.ENGINE_NAME:
        NodeTreeHandler.update_node_tree_count(scene)
        return
    depsgraph = bpy.context.evaluated_depsgraph_get()
    NodeTreeHandler.blender_internal_node_tree_update_handler(scene, depsgraph, last_op_bl_idname)


_CLASSES = [
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
