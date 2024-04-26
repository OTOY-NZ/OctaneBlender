# <pep8 compliant>

from bpy.props import IntProperty, BoolProperty

import bpy
from bpy.utils import register_class, unregister_class
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket
from octane.utils import utility, consts


class OctaneBaseKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctaneBaseKernelMaxsamples"
    bl_label = "Max. samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_SAMPLES
    octane_pin_name = "maxsamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_INT
    octane_used_for_preview: BoolProperty(name="", default=False)

    def update_max_sample(self, context):
        if self.octane_used_for_preview:
            context.scene.octane.max_preview_samples = self.default_value
        else:
            context.scene.octane.max_samples = self.default_value

    default_value: IntProperty(default=500, update=update_max_sample,
                               description="The maximum samples per pixel that will be calculated until rendering is "
                                           "stopped",
                               min=1, max=1000000, soft_min=1, soft_max=100000, step=1)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneBaseKernelNode(OctaneBaseNode):
    MAX_SAMPLE_SOCKET_NAME = "Max. samples"
    MAX_PREVIEW_SAMPLE_SOCKET_NAME = "Max. preview samples"
    LIGHT_ID_NAME = "Light IDs"
    LIGHT_LINKING_INVERT_NAME = "Light linking invert"
    NODE_PIN_ID_TO_PROPERTY_INFO_MAP = {
        consts.PinID.P_MAX_SAMPLES: "max_samples",
        consts.PinID.P_GI_MODE: "gi_mode",
        consts.PinID.P_SPECULAR_DEPTH: "specular_depth",
        consts.PinID.P_GLOSSY_DEPTH: "glossy_depth",
        consts.PinID.P_DIFFUSE_DEPTH: "diffuse_depth",
        consts.PinID.P_MAX_OVERLAPPING_VOLUMES: "",
        consts.PinID.P_RAY_EPSILON: "ray_epsilon",
        consts.PinID.P_FILTERSIZE: "filter_size",
        consts.PinID.P_AO_DISTANCE: "ao_dist",
        consts.PinID.P_ALPHA_SHADOWS: "alpha_shadows",
        consts.PinID.P_NESTED_DIELECTRICS: "nested_dielectrics",
        consts.PinID.P_IRRADIANCE: "irradiance_mode",
        consts.PinID.P_MAX_SUBD_LEVEL: "max_subdivision_level",
        consts.PinID.P_ALPHA_CHANNEL: "alpha_channel",
        consts.PinID.P_KEEP_ENVIRONMENT: "keep_environment",
        consts.PinID.P_AI_LIGHT: "ai_light_enable",
        consts.PinID.P_AI_LIGHT_UPDATE: "ai_light_update",
        consts.PinID.P_GLOBAL_LIGHT_ID_MASK_ACTION: "light_ids_action",
        consts.PinID.P_PATH_TERM_POWER: "path_term_power",
        consts.PinID.P_COHERENT_RATIO: "coherent_ratio",
        consts.PinID.P_STATIC_NOISE: "static_noise",
        consts.PinID.P_PARALLEL_SAMPLES: "parallel_samples",
        consts.PinID.P_MAX_TILE_SAMPLES: "max_tile_samples",
        consts.PinID.P_MINIMIZE_NET_TRAFFIC: "minimize_net_traffic",
        consts.PinID.P_ADAPTIVE_SAMPLING: "adaptive_sampling",
        consts.PinID.P_NOISE_THRESHOLD: "adaptive_noise_threshold",
        consts.PinID.P_MIN_ADAPTIVE_SAMPLES: "adaptive_min_samples",
        consts.PinID.P_ADAPTIVE_SAMPLING_PIXEL_GROUP: "adaptive_group_pixels1",
        consts.PinID.P_ADAPTIVE_SAMPLING_EXPOSURE: "adaptive_expected_exposure",
        consts.PinID.P_DEEP_ENABLE: "deep_image",
        consts.PinID.P_DEEP_ENABLE_PASSES: "deep_render_passes",
        consts.PinID.P_MAX_DEPTH_SAMPLES: "max_depth_samples",
        consts.PinID.P_DEPTH_TOLERANCE: "depth_tolerance",
        consts.PinID.P_WHITE_LIGHT_SPECTRUM: "white_light_spectrum",
        consts.PinID.P_TOON_SHADOW_AMBIENT: "toon_shadow_ambient",
        consts.PinID.P_MAX_DIFFUSEDEPTH: "max_diffuse_depth",
        consts.PinID.P_MAX_GLOSSYDEPTH: "max_glossy_depth",
        consts.PinID.P_MAX_SCATTER_DEPTH: "max_scatter_depth",
        consts.PinID.P_CAUSTIC_BLUR: "caustic_blur",
        consts.PinID.P_GI_CLAMP: "gi_clamp",
        consts.PinID.P_EXPLORATION_STRENGTH: "exploration",
        consts.PinID.P_DIRECT_LIGHT_IMPORTANCE: "direct_light_importance",
        consts.PinID.P_MAX_REJECTS: "max_rejects",
        consts.PinID.P_PARALLELISM: "parallelism",
        consts.PinID.P_WORK_CHUNK_SIZE: "work_chunk_size",
        consts.PinID.P_INFOCHANNELS_TYPE: "info_channel_type",
        consts.PinID.P_OPACITY: "opacity_threshold",
        consts.PinID.P_Z_DEPTH_MAX: "zdepth_max",
        consts.PinID.P_UV_MAX: "uv_max",
        consts.PinID.P_UV_SET: "info_pass_uv_coordinate_selection",
        consts.PinID.P_MAX_SPEED: "max_speed",
        consts.PinID.P_INFOCHANNEL_SAMPLING_MODE: "sampling_mode",
        consts.PinID.P_BUMP: "bump_normal_mapping",
        consts.PinID.P_HIGHLIGHT_BACKFACES: "wf_bkface_hl",
        consts.PinID.P_MAX_PHOTONDEPTH: "photon_depth",
        consts.PinID.P_ACCURATE_COLOR: "accurate_colors",
        consts.PinID.P_GATHER_RADIUS: "photon_gather_radius",
        consts.PinID.P_PHOTON_COUNT_MULTIPLIER: "photon_gather_multiplier",
        consts.PinID.P_PHOTON_GATHER_SAMPLES: "photon_gather_samples",
        consts.PinID.P_PHOTON_EXPLORATION_STRENGTH: "exploration_strength",
    }

    @classmethod
    def update_node_definition(cls):
        utility.remove_socket_list(cls, [cls.MAX_SAMPLE_SOCKET_NAME, cls.MAX_PREVIEW_SAMPLE_SOCKET_NAME])

    def init_octane_kernel(self, context, create_light_id_config=False):
        utility.remove_socket_inputs(self, [self.MAX_SAMPLE_SOCKET_NAME, self.MAX_PREVIEW_SAMPLE_SOCKET_NAME])
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_SAMPLE_SOCKET_NAME).init()
        self.inputs.new("OctaneBaseKernelMaxsamples", self.MAX_PREVIEW_SAMPLE_SOCKET_NAME).init()
        self.inputs[self.MAX_SAMPLE_SOCKET_NAME].octane_used_for_preview = False
        self.inputs[self.MAX_PREVIEW_SAMPLE_SOCKET_NAME].octane_used_for_preview = True
        for idx, _input in enumerate(self.inputs):
            if isinstance(_input, OctaneGroupTitleSocket):
                if _input.is_group_socket(self.MAX_SAMPLE_SOCKET_NAME):
                    _input.add_group_socket(self.MAX_PREVIEW_SAMPLE_SOCKET_NAME)
        self.inputs.move(len(self.inputs) - 1, 1)
        self.inputs.move(len(self.inputs) - 1, 1)
        if create_light_id_config:
            self.create_light_id_config(context)

    def create_light_id_config(self, _context):
        node_tree = self.id_data
        if self.LIGHT_ID_NAME in node_tree.nodes:
            light_id_node = node_tree.nodes[self.LIGHT_ID_NAME]
        else:
            light_id_node = node_tree.nodes.new("OctaneLightIDBitValue")
            light_id_node.name = self.LIGHT_ID_NAME
        if self.LIGHT_LINKING_INVERT_NAME in node_tree.nodes:
            light_linking_invert_node = node_tree.nodes[self.LIGHT_LINKING_INVERT_NAME]
        else:
            light_linking_invert_node = node_tree.nodes.new("OctaneLightIDBitValue")
            light_linking_invert_node.name = self.LIGHT_LINKING_INVERT_NAME
        light_id_node.location = (self.location.x - 600, self.location.y - 200)
        light_linking_invert_node.location = (self.location.x - 600, self.location.y - 400)
        node_tree.links.new(light_id_node.outputs[0], self.inputs["Light IDs"])
        node_tree.links.new(light_linking_invert_node.outputs[0], self.inputs["Light linking invert"])

    def sync_sample_data(self, octane_node, octane_graph_node_data, sample_socket_name):
        socket = self.inputs[sample_socket_name]
        link_node_name = ""
        if octane_graph_node_data:
            link_node_name = octane_graph_node_data.get_link_node_name(sample_socket_name)
            data_socket = octane_graph_node_data.get_link_data_socket(sample_socket_name)
        else:
            data_socket = None
        if data_socket is None:
            data_socket = socket
        default_value = getattr(data_socket, "default_value", "")
        octane_node.set_pin(consts.OctaneDataBlockSymbolType.PIN_NAME, socket.octane_pin_index, socket.octane_pin_name,
                            socket.octane_socket_type, socket.octane_pin_type, socket.octane_default_node_type,
                            data_socket.is_linked, link_node_name, default_value)

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        if depsgraph and depsgraph.mode == "VIEWPORT":
            self.sync_sample_data(octane_node, octane_graph_node_data, self.MAX_PREVIEW_SAMPLE_SOCKET_NAME)
        else:
            self.sync_sample_data(octane_node, octane_graph_node_data, self.MAX_SAMPLE_SOCKET_NAME)

    @classmethod
    def generate_from_legacy_octane_property(cls, octane_scene, node_tree):
        nodes = node_tree.nodes
        kernel_type = octane_scene.kernel_type
        kernel_node = None
        if kernel_type in ("0", "1",):
            kernel_node = nodes.new("OctaneDirectLightingKernel")
        elif kernel_type in ("2",):
            kernel_node = nodes.new("OctanePathTracingKernel")
        elif kernel_type in ("3",):
            kernel_node = nodes.new("OctanePMCKernel")
        elif kernel_type in ("4",):
            kernel_node = nodes.new("OctaneInfoChannelsKernel")
        elif kernel_type in ("5",):
            kernel_node = nodes.new("OctanePhotonTracingKernel")
        kernel_node.inputs["Max. preview samples"].default_value = octane_scene.max_preview_samples
        for _input in kernel_node.inputs:
            pin_id = getattr(_input, "octane_pin_id", consts.PinID.P_UNKNOWN)
            if pin_id in cls.NODE_PIN_ID_TO_PROPERTY_INFO_MAP:
                property_info = cls.NODE_PIN_ID_TO_PROPERTY_INFO_MAP[pin_id]
                if property_info is dict:
                    property_name = property_info[kernel_node.octane_node_type]
                else:
                    property_name = property_info
                if len(property_name) and hasattr(octane_scene, property_name):
                    property_type = octane_scene.rna_type.properties[property_name].type
                    if property_type == "ENUM":
                        enum_int_value = utility.get_enum_int_value(octane_scene, property_name, 0)
                        utility.set_enum_int_value(_input, "default_value", enum_int_value)
                    else:
                        _input.default_value = getattr(octane_scene, property_name, None)
        # AO ambient texture
        if kernel_node.octane_node_type == consts.NodeType.NT_KERN_DIRECTLIGHTING:
            if octane_scene.ao_texture in bpy.data.textures:
                ao_texture = bpy.data.textures[octane_scene.ao_texture]
                if ao_texture and ao_texture.use_nodes:
                    output = utility.find_active_output_node(ao_texture.node_tree, consts.OctaneNodeTreeIDName.TEXTURE)
                    if output and output.inputs[0].is_linked:
                        root_node = output.inputs[0].links[0].from_node
                        new_root_node = utility.copy_nodes(node_tree, ao_texture.node_tree, root_node)
                        node_tree.links.new(kernel_node.inputs["AO ambient texture"], new_root_node.outputs[0])
                        # Light linking
        if cls.LIGHT_ID_NAME in kernel_node.inputs:
            light_id_socket = kernel_node.inputs[cls.LIGHT_ID_NAME]
            if light_id_socket.is_linked:
                light_id_node = light_id_socket.links[0].from_node
                light_id_node.sunlight = octane_scene.light_id_sunlight
                light_id_node.environment = octane_scene.light_id_env
                light_id_node.light_pass_id_1 = octane_scene.light_id_pass_1
                light_id_node.light_pass_id_2 = octane_scene.light_id_pass_2
                light_id_node.light_pass_id_3 = octane_scene.light_id_pass_3
                light_id_node.light_pass_id_4 = octane_scene.light_id_pass_4
                light_id_node.light_pass_id_5 = octane_scene.light_id_pass_5
                light_id_node.light_pass_id_6 = octane_scene.light_id_pass_6
                light_id_node.light_pass_id_7 = octane_scene.light_id_pass_7
                light_id_node.light_pass_id_8 = octane_scene.light_id_pass_8
        if cls.LIGHT_LINKING_INVERT_NAME in kernel_node.inputs:
            light_id_socket = kernel_node.inputs[cls.LIGHT_LINKING_INVERT_NAME]
            if light_id_socket.is_linked:
                light_id_node = light_id_socket.links[0].from_node
                light_id_node.sunlight = octane_scene.light_id_sunlight_invert
                light_id_node.environment = octane_scene.light_id_env_invert
                light_id_node.light_pass_id_1 = octane_scene.light_id_pass_1_invert
                light_id_node.light_pass_id_2 = octane_scene.light_id_pass_2_invert
                light_id_node.light_pass_id_3 = octane_scene.light_id_pass_3_invert
                light_id_node.light_pass_id_4 = octane_scene.light_id_pass_4_invert
                light_id_node.light_pass_id_5 = octane_scene.light_id_pass_5_invert
                light_id_node.light_pass_id_6 = octane_scene.light_id_pass_6_invert
                light_id_node.light_pass_id_7 = octane_scene.light_id_pass_7_invert
                light_id_node.light_pass_id_8 = octane_scene.light_id_pass_8_invert
        return kernel_node


_CLASSES = [
    OctaneBaseKernelMaxsamples,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
