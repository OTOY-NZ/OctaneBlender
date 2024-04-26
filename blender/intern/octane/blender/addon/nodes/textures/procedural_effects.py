# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneProceduralEffectsOperationType(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsOperationType"
    bl_label = "Type"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_OPERATION_TYPE
    octane_pin_name = "operationType"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Blaschke product", "Blaschke product", "", 11),
        ("Candle flame", "Candle flame", "", 20),
        ("Combustible Voronoi", "Combustible Voronoi", "", 0),
        ("Fire emitter", "Fire emitter", "", 8),
        ("Fractal 1", "Fractal 1", "", 1),
        ("Fractal 2", "Fractal 2", "", 18),
        ("Fractal 3", "Fractal 3", "", 12),
        ("Kaleidoscope", "Kaleidoscope", "", 2),
        ("Mist", "Mist", "", 9),
        ("Neon stripes", "Neon stripes", "", 3),
        ("Noise smoke flow", "Noise smoke flow", "", 17),
        ("Paint colors 1", "Paint colors 1", "", 4),
        ("Particles", "Particles", "", 5),
        ("Portal", "Portal", "", 19),
        ("Skinner", "Skinner", "", 13),
        ("Star scroller", "Star scroller", "", 6),
        ("Sun surface", "Sun surface", "", 14),
        ("Tunnel", "Tunnel", "", 10),
        ("Wavey colors", "Wavey colors", "", 7),
        ("Volumetric|Paint colors 2", "Volumetric|Paint colors 2", "", 15),
        ("Volumetric|Spiral", "Volumetric|Spiral", "", 16),
    ]
    default_value: EnumProperty(default="Combustible Voronoi", update=OctaneBaseSocket.update_node_tree, description="The effect to generate", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneProceduralEffectsTime(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsTime"
    bl_label = "Time"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TIME
    octane_pin_name = "time"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The animation timestamp", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneProceduralEffectsTransform(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsTransform"
    bl_label = "UVW transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneProceduralEffectsProjection(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_UVW
    octane_default_node_name = "OctaneMeshUVProjection"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneProceduralEffects(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneProceduralEffects"
    bl_label = "Procedural effects"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneProceduralEffectsOperationType, OctaneProceduralEffectsTime, OctaneProceduralEffectsTransform, OctaneProceduralEffectsProjection, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_TEX_PROCEDURAL_EFFECTS
    octane_socket_list = ["Type", "Time", "UVW transform", "Projection", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 4

    def init(self, context):  # noqa
        self.inputs.new("OctaneProceduralEffectsOperationType", OctaneProceduralEffectsOperationType.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsTime", OctaneProceduralEffectsTime.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsTransform", OctaneProceduralEffectsTransform.bl_label).init()
        self.inputs.new("OctaneProceduralEffectsProjection", OctaneProceduralEffectsProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneProceduralEffectsOperationType,
    OctaneProceduralEffectsTime,
    OctaneProceduralEffectsTransform,
    OctaneProceduralEffectsProjection,
    OctaneProceduralEffects,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
