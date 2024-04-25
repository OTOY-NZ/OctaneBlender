# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctanePMCKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxsamples"
    bl_label = "Max. samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_SAMPLES
    octane_pin_name = "maxsamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=5000, update=OctaneBaseSocket.update_node_tree, description="The number of samples per pixel that will be calculated before rendering is stopped", min=1, max=1000000, soft_min=1, soft_max=100000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxDiffuseDepth"
    bl_label = "Diffuse depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DIFFUSEDEPTH
    octane_pin_name = "maxDiffuseDepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxGlossyDepth"
    bl_label = "Specular depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_GLOSSYDEPTH
    octane_pin_name = "maxGlossyDepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=24, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2000002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxScatterDepth"
    bl_label = "Scatter depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_SCATTER_DEPTH
    octane_pin_name = "maxScatterDepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which scattering is allowed", min=1, max=256, soft_min=1, soft_max=256, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 5000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxOverlappingVolumes"
    bl_label = "Maximal overlapping volumes"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_OVERLAPPING_VOLUMES
    octane_pin_name = "maxOverlappingVolumes"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000004
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelRayepsilon"
    bl_label = "Ray epsilon"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RAY_EPSILON
    octane_pin_name = "rayepsilon"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Shadow ray offset distance", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=0.000100, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelFiltersize"
    bl_label = "Filter size"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_FILTERSIZE
    octane_pin_name = "filtersize"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 6
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.200000, update=OctaneBaseSocket.update_node_tree, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAlphashadows"
    bl_label = "Alpha shadows"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ALPHA_SHADOWS
    octane_pin_name = "alphashadows"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 7
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelCausticBlur(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelCausticBlur"
    bl_label = "Caustic blur"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_CAUSTIC_BLUR
    octane_pin_name = "caustic_blur"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 8
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="Caustic blur for noise reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelGiClamp(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGiClamp"
    bl_label = "GI clamp"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GI_CLAMP
    octane_pin_name = "giClamp"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 9
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1000000.000000, update=OctaneBaseSocket.update_node_tree, description="GI clamp reducing fireflies", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=1000000.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 2040000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelNestedDielectrics"
    bl_label = "Nested dielectrics"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NESTED_DIELECTRICS
    octane_pin_name = "nestedDielectrics"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables nested dielectrics. If disabled, the surface IOR is not tracked and surface priorities are ignored")
    octane_hide_value = False
    octane_min_version = 10020100
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelIrradiance"
    bl_label = "Irradiance mode"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_IRRADIANCE
    octane_pin_name = "irradiance"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 11
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render the first surface as a white diffuse material")
    octane_hide_value = False
    octane_min_version = 3080009
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxsubdLevel"
    bl_label = "Max subdivision level"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_SUBD_LEVEL
    octane_pin_name = "MaxsubdLevel"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 12
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAlphachannel"
    bl_label = "Alpha channel"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ALPHA_CHANNEL
    octane_pin_name = "alphachannel"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables a compositing alpha channel")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelKeepEnvironment"
    bl_label = "Keep environment"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_KEEP_ENVIRONMENT
    octane_pin_name = "keep_environment"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keeps environment with enabled alpha channel")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAiLight"
    bl_label = "AI light"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT
    octane_pin_name = "aiLight"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables AI light")
    octane_hide_value = False
    octane_min_version = 4000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAiLightUpdate"
    bl_label = "AI light update"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT_UPDATE
    octane_pin_name = "aiLightUpdate"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables dynamic AI light update")
    octane_hide_value = False
    octane_min_version = 4000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGlobalLightIdMaskAction"
    bl_label = "Light IDs action"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_GLOBAL_LIGHT_ID_MASK_ACTION
    octane_pin_name = "globalLightIdMaskAction"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Disable", "Disable", "", 1),
        ("Enable", "Enable", "", 0),
    ]
    default_value: EnumProperty(default="Disable", update=OctaneBaseSocket.update_node_tree, description="The action to be taken on selected lights IDs", items=items)
    octane_hide_value = False
    octane_min_version = 4000009
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGlobalLightIdMask"
    bl_label = "Light IDs"
    color = consts.OctanePinColor.BitMask
    octane_default_node_type = consts.NodeType.NT_BIT_MASK
    octane_default_node_name = "OctaneBitValue"
    octane_pin_id = consts.PinID.P_GLOBAL_LIGHT_ID_MASK
    octane_pin_name = "globalLightIdMask"
    octane_pin_type = consts.PinType.PT_BIT_MASK
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 4000009
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelLightPassMask"
    bl_label = "Light linking invert"
    color = consts.OctanePinColor.BitMask
    octane_default_node_type = consts.NodeType.NT_BIT_MASK
    octane_default_node_name = "OctaneBitValue"
    octane_pin_id = consts.PinID.P_LIGHT_PASS_MASK
    octane_pin_name = "lightPassMask"
    octane_pin_type = consts.PinType.PT_BIT_MASK
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 4000013
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelPathTermPower"
    bl_label = "Path term. power"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PATH_TERM_POWER
    octane_pin_name = "pathTermPower"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Path may get terminated when ray power is less than this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2100000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelExplorationStrength(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelExplorationStrength"
    bl_label = "Exploration strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EXPLORATION_STRENGTH
    octane_pin_name = "exploration_strength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.700000, update=OctaneBaseSocket.update_node_tree, description="Effort on investigating good paths", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelDirectLightImportance(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelDirectLightImportance"
    bl_label = "Direct light importance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DIRECT_LIGHT_IMPORTANCE
    octane_pin_name = "direct_light_importance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Computational effort on direct lighting", min=0.010000, max=1.000000, soft_min=0.010000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelMaxrejects(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxrejects"
    bl_label = "Max. rejects"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_REJECTS
    octane_pin_name = "maxrejects"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=500, update=OctaneBaseSocket.update_node_tree, description="Maximum number of consecutive rejects", min=100, max=10000, soft_min=100, soft_max=10000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelParallelism(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelParallelism"
    bl_label = "Parallel samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PARALLELISM
    octane_pin_name = "parallelism"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed.\n\nNOTE: Changing this value restarts rendering", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelWorkChunkSize(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelWorkChunkSize"
    bl_label = "Work chunk size"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_WORK_CHUNK_SIZE
    octane_pin_name = "workChunkSize"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value may increase render speed but it will increase system memory usage", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelWhiteLightSpectrum"
    bl_label = "White light spectrum"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_WHITE_LIGHT_SPECTRUM
    octane_pin_name = "whiteLightSpectrum"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("D65", "D65", "", 1),
        ("Legacy/flat", "Legacy/flat", "", 0),
    ]
    default_value: EnumProperty(default="D65", update=OctaneBaseSocket.update_node_tree, description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, black body emitters). This determines the spectrum that will produce white (before white balance) in the final image. Use D65 to adapt to a reasonable daylight \"white\" color. Use Legacy/flat to preserve the appearance of old projects (spectral emitters will appear rather blue)", items=items)
    octane_hide_value = False
    octane_min_version = 11000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TOON_SHADOW_AMBIENT
    octane_pin_name = "toonShadowAmbient"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The ambient modifier of toon shadowing", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePMCKernelAffectRoughness(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAffectRoughness"
    bl_label = "[Deprecated]Affect roughness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AFFECT_ROUGHNESS
    octane_pin_name = "affectRoughness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000000
    octane_end_version = 6000006
    octane_deprecated = True


class OctanePMCKernelAiLightUpdateStrength(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAiLightUpdateStrength"
    bl_label = "[Deprecated]AI light strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT_STRENGTH
    octane_pin_name = "aiLightUpdateStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="The strength for dynamic AI light update", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 4000000
    octane_end_version = 4000009
    octane_deprecated = True


class OctanePMCKernelMaxdepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxdepth"
    bl_label = "[Deprecated]Path depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DEPTH
    octane_pin_name = "maxdepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Maximum path depth", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2000002
    octane_deprecated = True


class OctanePMCKernelRrprob(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelRrprob"
    bl_label = "[Deprecated]RR probability"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RR_PROB
    octane_pin_name = "rrprob"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Russian Roulette Termination Probability (0=auto)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2100000
    octane_deprecated = True


class OctanePMCKernelOldVolumeBehavior(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelOldVolumeBehavior"
    bl_label = "[Deprecated]Emulate old volume behavior"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_OLD_VOLUME_BEHAVIOR
    octane_pin_name = "oldVolumeBehavior"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 32
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Emulate the behavior of emission and scattering of version 4.0 and earlier")
    octane_hide_value = False
    octane_min_version = 5000000
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePMCKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelUseOldColorPipeline"
    bl_label = "[Deprecated]Use old color pipeline"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_OLD_COLOR_PIPELINE
    octane_pin_name = "useOldColorPipeline"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 33
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")
    octane_hide_value = False
    octane_min_version = 11000005
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePMCKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupQuality"
    bl_label = "[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Affect roughness;")


class OctanePMCKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupAlphaChannel"
    bl_label = "[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;Keep environment;")


class OctanePMCKernelGroupLight(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupLight"
    bl_label = "[OctaneGroupTitle]Light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="AI light;AI light update;Light IDs action;Light IDs;Light linking invert;AI light strength;")


class OctanePMCKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupSampling"
    bl_label = "[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Path term. power;Exploration strength;Direct light importance;Max. rejects;Parallel samples;Work chunk size;")


class OctanePMCKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupColor"
    bl_label = "[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")


class OctanePMCKernelGroupToonShading(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupToonShading"
    bl_label = "[OctaneGroupTitle]Toon Shading"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Toon shadow ambient;")


class OctanePMCKernelGroupCompatibilitySettings(OctaneGroupTitleSocket):
    bl_idname = "OctanePMCKernelGroupCompatibilitySettings"
    bl_label = "[OctaneGroupTitle]Compatibility settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emulate old volume behavior;")


class OctanePMCKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname = "OctanePMCKernel"
    bl_label = "PMC kernel"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctanePMCKernelGroupQuality, OctanePMCKernelMaxsamples, OctanePMCKernelMaxDiffuseDepth, OctanePMCKernelMaxGlossyDepth, OctanePMCKernelMaxScatterDepth, OctanePMCKernelMaxOverlappingVolumes, OctanePMCKernelRayepsilon, OctanePMCKernelFiltersize, OctanePMCKernelAlphashadows, OctanePMCKernelCausticBlur, OctanePMCKernelGiClamp, OctanePMCKernelNestedDielectrics, OctanePMCKernelIrradiance, OctanePMCKernelMaxsubdLevel, OctanePMCKernelAffectRoughness, OctanePMCKernelGroupAlphaChannel, OctanePMCKernelAlphachannel, OctanePMCKernelKeepEnvironment, OctanePMCKernelGroupLight, OctanePMCKernelAiLight, OctanePMCKernelAiLightUpdate, OctanePMCKernelGlobalLightIdMaskAction, OctanePMCKernelGlobalLightIdMask, OctanePMCKernelLightPassMask, OctanePMCKernelAiLightUpdateStrength, OctanePMCKernelGroupSampling, OctanePMCKernelPathTermPower, OctanePMCKernelExplorationStrength, OctanePMCKernelDirectLightImportance, OctanePMCKernelMaxrejects, OctanePMCKernelParallelism, OctanePMCKernelWorkChunkSize, OctanePMCKernelGroupColor, OctanePMCKernelWhiteLightSpectrum, OctanePMCKernelUseOldColorPipeline, OctanePMCKernelGroupToonShading, OctanePMCKernelToonShadowAmbient, OctanePMCKernelMaxdepth, OctanePMCKernelRrprob, OctanePMCKernelGroupCompatibilitySettings, OctanePMCKernelOldVolumeBehavior, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_KERN_PMC
    octane_socket_list = ["Max. samples", "Diffuse depth", "Specular depth", "Scatter depth", "Maximal overlapping volumes", "Ray epsilon", "Filter size", "Alpha shadows", "Caustic blur", "GI clamp", "Nested dielectrics", "Irradiance mode", "Max subdivision level", "Alpha channel", "Keep environment", "AI light", "AI light update", "Light IDs action", "Light IDs", "Light linking invert", "Path term. power", "Exploration strength", "Direct light importance", "Max. rejects", "Parallel samples", "Work chunk size", "White light spectrum", "Toon shadow ambient", "[Deprecated]Affect roughness", "[Deprecated]AI light strength", "[Deprecated]Path depth", "[Deprecated]RR probability", "[Deprecated]Emulate old volume behavior", "[Deprecated]Use old color pipeline", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 28

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Enable legacy behavior for light visibility flags on medium (visibility on scattering for environment and null material is controlled by the diffuse flag).""", 12000005),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000099),
        ("2021.1 compatibility mode (with 4.0 volumes)", "2021.1 compatibility mode (with 4.0 volumes)", """Volume tracing behavior from version 4.0 and earlier is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000098),
        ("2018.1 compatibility mode", "2018.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 5000000),
        ("4.0 compatibility mode", "4.0 compatibility mode", """Volume tracing behavior from version 4.0 and earlier is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=13000200, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctanePMCKernelGroupQuality", OctanePMCKernelGroupQuality.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxsamples", OctanePMCKernelMaxsamples.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxDiffuseDepth", OctanePMCKernelMaxDiffuseDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxGlossyDepth", OctanePMCKernelMaxGlossyDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxScatterDepth", OctanePMCKernelMaxScatterDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxOverlappingVolumes", OctanePMCKernelMaxOverlappingVolumes.bl_label).init()
        self.inputs.new("OctanePMCKernelRayepsilon", OctanePMCKernelRayepsilon.bl_label).init()
        self.inputs.new("OctanePMCKernelFiltersize", OctanePMCKernelFiltersize.bl_label).init()
        self.inputs.new("OctanePMCKernelAlphashadows", OctanePMCKernelAlphashadows.bl_label).init()
        self.inputs.new("OctanePMCKernelCausticBlur", OctanePMCKernelCausticBlur.bl_label).init()
        self.inputs.new("OctanePMCKernelGiClamp", OctanePMCKernelGiClamp.bl_label).init()
        self.inputs.new("OctanePMCKernelNestedDielectrics", OctanePMCKernelNestedDielectrics.bl_label).init()
        self.inputs.new("OctanePMCKernelIrradiance", OctanePMCKernelIrradiance.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxsubdLevel", OctanePMCKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctanePMCKernelAffectRoughness", OctanePMCKernelAffectRoughness.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupAlphaChannel", OctanePMCKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctanePMCKernelAlphachannel", OctanePMCKernelAlphachannel.bl_label).init()
        self.inputs.new("OctanePMCKernelKeepEnvironment", OctanePMCKernelKeepEnvironment.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupLight", OctanePMCKernelGroupLight.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLight", OctanePMCKernelAiLight.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLightUpdate", OctanePMCKernelAiLightUpdate.bl_label).init()
        self.inputs.new("OctanePMCKernelGlobalLightIdMaskAction", OctanePMCKernelGlobalLightIdMaskAction.bl_label).init()
        self.inputs.new("OctanePMCKernelGlobalLightIdMask", OctanePMCKernelGlobalLightIdMask.bl_label).init()
        self.inputs.new("OctanePMCKernelLightPassMask", OctanePMCKernelLightPassMask.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLightUpdateStrength", OctanePMCKernelAiLightUpdateStrength.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupSampling", OctanePMCKernelGroupSampling.bl_label).init()
        self.inputs.new("OctanePMCKernelPathTermPower", OctanePMCKernelPathTermPower.bl_label).init()
        self.inputs.new("OctanePMCKernelExplorationStrength", OctanePMCKernelExplorationStrength.bl_label).init()
        self.inputs.new("OctanePMCKernelDirectLightImportance", OctanePMCKernelDirectLightImportance.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxrejects", OctanePMCKernelMaxrejects.bl_label).init()
        self.inputs.new("OctanePMCKernelParallelism", OctanePMCKernelParallelism.bl_label).init()
        self.inputs.new("OctanePMCKernelWorkChunkSize", OctanePMCKernelWorkChunkSize.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupColor", OctanePMCKernelGroupColor.bl_label).init()
        self.inputs.new("OctanePMCKernelWhiteLightSpectrum", OctanePMCKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctanePMCKernelUseOldColorPipeline", OctanePMCKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupToonShading", OctanePMCKernelGroupToonShading.bl_label).init()
        self.inputs.new("OctanePMCKernelToonShadowAmbient", OctanePMCKernelToonShadowAmbient.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxdepth", OctanePMCKernelMaxdepth.bl_label).init()
        self.inputs.new("OctanePMCKernelRrprob", OctanePMCKernelRrprob.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupCompatibilitySettings", OctanePMCKernelGroupCompatibilitySettings.bl_label).init()
        self.inputs.new("OctanePMCKernelOldVolumeBehavior", OctanePMCKernelOldVolumeBehavior.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctanePMCKernelMaxsamples,
    OctanePMCKernelMaxDiffuseDepth,
    OctanePMCKernelMaxGlossyDepth,
    OctanePMCKernelMaxScatterDepth,
    OctanePMCKernelMaxOverlappingVolumes,
    OctanePMCKernelRayepsilon,
    OctanePMCKernelFiltersize,
    OctanePMCKernelAlphashadows,
    OctanePMCKernelCausticBlur,
    OctanePMCKernelGiClamp,
    OctanePMCKernelNestedDielectrics,
    OctanePMCKernelIrradiance,
    OctanePMCKernelMaxsubdLevel,
    OctanePMCKernelAlphachannel,
    OctanePMCKernelKeepEnvironment,
    OctanePMCKernelAiLight,
    OctanePMCKernelAiLightUpdate,
    OctanePMCKernelGlobalLightIdMaskAction,
    OctanePMCKernelGlobalLightIdMask,
    OctanePMCKernelLightPassMask,
    OctanePMCKernelPathTermPower,
    OctanePMCKernelExplorationStrength,
    OctanePMCKernelDirectLightImportance,
    OctanePMCKernelMaxrejects,
    OctanePMCKernelParallelism,
    OctanePMCKernelWorkChunkSize,
    OctanePMCKernelWhiteLightSpectrum,
    OctanePMCKernelToonShadowAmbient,
    OctanePMCKernelAffectRoughness,
    OctanePMCKernelAiLightUpdateStrength,
    OctanePMCKernelMaxdepth,
    OctanePMCKernelRrprob,
    OctanePMCKernelOldVolumeBehavior,
    OctanePMCKernelUseOldColorPipeline,
    OctanePMCKernelGroupQuality,
    OctanePMCKernelGroupAlphaChannel,
    OctanePMCKernelGroupLight,
    OctanePMCKernelGroupSampling,
    OctanePMCKernelGroupColor,
    OctanePMCKernelGroupToonShading,
    OctanePMCKernelGroupCompatibilitySettings,
    OctanePMCKernel,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


OctanePMCKernelGlobalLightIdMask.octane_default_node_name = "OctaneLightIDBitValue"
OctanePMCKernelLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"


class OctanePMCKernel_Override(OctanePMCKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, True)

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")


OctanePMCKernelGroupCompatibilitySettings.octane_deprecated = True
OctanePMCKernel_Override.update_node_definition()
utility.override_class(_CLASSES, OctanePMCKernel, OctanePMCKernel_Override)
