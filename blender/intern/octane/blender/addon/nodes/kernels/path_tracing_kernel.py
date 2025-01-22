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


class OctanePathTracingKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxsamples"
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


class OctanePathTracingKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxDiffuseDepth"
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


class OctanePathTracingKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxGlossyDepth"
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


class OctanePathTracingKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxScatterDepth"
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


class OctanePathTracingKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxOverlappingVolumes"
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


class OctanePathTracingKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelRayepsilon"
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


class OctanePathTracingKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelFiltersize"
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


class OctanePathTracingKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAlphashadows"
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


class OctanePathTracingKernelCausticBlur(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelCausticBlur"
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


class OctanePathTracingKernelGiClamp(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGiClamp"
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


class OctanePathTracingKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelNestedDielectrics"
    bl_label = "Nested dielectrics"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_NESTED_DIELECTRICS
    octane_pin_name = "nestedDielectrics"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 10
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")
    octane_hide_value = False
    octane_min_version = 10020100
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelIrradiance"
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


class OctanePathTracingKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxsubdLevel"
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


class OctanePathTracingKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAlphachannel"
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


class OctanePathTracingKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelKeepEnvironment"
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


class OctanePathTracingKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAiLight"
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


class OctanePathTracingKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAiLightUpdate"
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


class OctanePathTracingKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGlobalLightIdMaskAction"
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


class OctanePathTracingKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGlobalLightIdMask"
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


class OctanePathTracingKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelLightPassMask"
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


class OctanePathTracingKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelPathTermPower"
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


class OctanePathTracingKernelDirectLightRayCount(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDirectLightRayCount"
    bl_label = "Direct light rays"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_DIRECT_LIGHT_RAY_COUNT
    octane_pin_name = "directLightRayCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of direct light rays traced for every sample. This amount is used after camera rays, and after very smooth specular reflections or transmission", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 14000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelCoherentRatio(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelCoherentRatio"
    bl_label = "Coherent ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_COHERENT_RATIO
    octane_pin_name = "coherentRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 2140000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelStaticNoise(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelStaticNoise"
    bl_label = "Static noise"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STATIC_NOISE
    octane_pin_name = "staticNoise"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the noise patterns are kept stable between frames")
    octane_hide_value = False
    octane_min_version = 2110002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelParallelSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelParallelSamples"
    bl_label = "Parallel samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PARALLEL_SAMPLES
    octane_pin_name = "parallelSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxTileSamples"
    bl_label = "Max. tile samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_TILE_SAMPLES
    octane_pin_name = "maxTileSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=32, update=OctaneBaseSocket.update_node_tree, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMinimizeNetTraffic"
    bl_label = "Minimize net traffic"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_MINIMIZE_NET_TRAFFIC
    octane_pin_name = "minimizeNetTraffic"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelAdaptiveSampling(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSampling"
    bl_label = "Adaptive sampling"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING
    octane_pin_name = "adaptiveSampling"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Stops rendering clean parts of the image and focuses on noisy parts")
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelNoiseThreshold(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelNoiseThreshold"
    bl_label = "Noise threshold"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NOISE_THRESHOLD
    octane_pin_name = "noiseThreshold"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.020000, update=OctaneBaseSocket.update_node_tree, description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelMinAdaptiveSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMinAdaptiveSamples"
    bl_label = "Min. adaptive samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MIN_ADAPTIVE_SAMPLES
    octane_pin_name = "minAdaptiveSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=512, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples per pixel until adaptive sampling kicks in. Set it to a higher value if you notice that the error estimate is incorrect and stops sampling pixels too early resulting in artifacts.\nOnly valid if adaptive sampling is enabled", min=2, max=1000000, soft_min=2, soft_max=100000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelAdaptiveSamplingPixelGroup(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSamplingPixelGroup"
    bl_label = "Pixel grouping"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING_PIXEL_GROUP
    octane_pin_name = "adaptiveSamplingPixelGroup"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("None", "None", "", 1),
        ("2 x 2", "2 x 2", "", 2),
        ("4 x 4", "4 x 4", "", 4),
    ]
    default_value: EnumProperty(default="2 x 2", update=OctaneBaseSocket.update_node_tree, description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not", items=items)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelAdaptiveSamplingExposure(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSamplingExposure"
    bl_label = "Expected exposure"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING_EXPOSURE
    octane_pin_name = "adaptiveSamplingExposure"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The expected exposure should be approximately the same value as the exposure in the imager or 0 to ignore this settings.\nIt's used by adaptive sampling to determine which pixels are bright and which are dark, which obviously depends on the exposure setting in the imaging settings. Adaptive sampling tweaks/reduces the noise estimate of very dark areas of the image. It also increases the min. adaptive samples limit for very dark areas which tend to find paths to light sources only very irregularly and thus have a too optimistic noise estimate", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=4096.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3060002
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelWhiteLightSpectrum"
    bl_label = "White light spectrum"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_WHITE_LIGHT_SPECTRUM
    octane_pin_name = "whiteLightSpectrum"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 32
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


class OctanePathTracingKernelDeepEnable(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDeepEnable"
    bl_label = "Deep image"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DEEP_ENABLE
    octane_pin_name = "deepEnable"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 33
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render a deep image")
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDeepEnablePasses"
    bl_label = "Deep render AOVs"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DEEP_ENABLE_PASSES
    octane_pin_name = "deepEnablePasses"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 34
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Include render AOVs in deep pixels")
    octane_hide_value = False
    octane_min_version = 5000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxDepthSamples"
    bl_label = "Max. depth samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DEPTH_SAMPLES
    octane_pin_name = "maxDepthSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 35
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelDepthTolerance(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDepthTolerance"
    bl_label = "Depth tolerance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DEPTH_TOLERANCE
    octane_pin_name = "depthTolerance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 36
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.050000, update=OctaneBaseSocket.update_node_tree, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 3000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TOON_SHADOW_AMBIENT
    octane_pin_name = "toonShadowAmbient"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 37
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The ambient modifier of toon shadowing", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 3080000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePathTracingKernelAffectRoughness(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAffectRoughness"
    bl_label = "[Deprecated]Affect roughness"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AFFECT_ROUGHNESS
    octane_pin_name = "affectRoughness"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 38
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 6000000
    octane_end_version = 6000006
    octane_deprecated = True


class OctanePathTracingKernelAiLightUpdateStrength(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAiLightUpdateStrength"
    bl_label = "[Deprecated]AI light strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT_STRENGTH
    octane_pin_name = "aiLightUpdateStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 39
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="The strength for dynamic AI light update", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 4000000
    octane_end_version = 4000009
    octane_deprecated = True


class OctanePathTracingKernelCoherentMode(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelCoherentMode"
    bl_label = "[Deprecated]Coherent mode"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_COHERENT_MODE
    octane_pin_name = "coherentMode"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 40
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts")
    octane_hide_value = False
    octane_min_version = 2100000
    octane_end_version = 2140000
    octane_deprecated = True


class OctanePathTracingKernelMaxdepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxdepth"
    bl_label = "[Deprecated]Path depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DEPTH
    octane_pin_name = "maxdepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 41
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Maximum path depth", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2000002
    octane_deprecated = True


class OctanePathTracingKernelRrprob(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelRrprob"
    bl_label = "[Deprecated]RR probability"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RR_PROB
    octane_pin_name = "rrprob"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 42
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Russian Roulette Termination Probability (0=auto)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 2100000
    octane_deprecated = True


class OctanePathTracingKernelAdaptiveStrength(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveStrength"
    bl_label = "[Deprecated]Adaptive strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_STRENGTH
    octane_pin_name = "adaptiveStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 43
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The strength with which the adaptive sampling is applied. Lower the values will increase render time. Only valid if adaptive sampling is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 3060000
    octane_end_version = 3060001
    octane_deprecated = True


class OctanePathTracingKernelOldVolumeBehavior(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelOldVolumeBehavior"
    bl_label = "[Deprecated]Emulate old volume behavior"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_OLD_VOLUME_BEHAVIOR
    octane_pin_name = "oldVolumeBehavior"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 44
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Emulate the behavior of emission and scattering of version 4.0 and earlier")
    octane_hide_value = False
    octane_min_version = 5000000
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePathTracingKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelUseOldColorPipeline"
    bl_label = "[Deprecated]Use old color pipeline"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_USE_OLD_COLOR_PIPELINE
    octane_pin_name = "useOldColorPipeline"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 45
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")
    octane_hide_value = False
    octane_min_version = 11000005
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePathTracingKernelAnalyticLight(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAnalyticLight"
    bl_label = "[Deprecated]Analytic light"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ANALYTIC_LIGHT
    octane_pin_name = "analyticLight"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 46
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Enables analytic light feature")
    octane_hide_value = False
    octane_min_version = 13000001
    octane_end_version = 13000005
    octane_deprecated = True


class OctanePathTracingKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupQuality"
    bl_label = "[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Affect roughness;")


class OctanePathTracingKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupAlphaChannel"
    bl_label = "[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;Keep environment;")


class OctanePathTracingKernelGroupLight(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupLight"
    bl_label = "[OctaneGroupTitle]Light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="AI light;AI light update;Light IDs action;Light IDs;Light linking invert;AI light strength;Analytic light;")


class OctanePathTracingKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupSampling"
    bl_label = "[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Path term. power;Direct light rays;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;")


class OctanePathTracingKernelGroupAdaptiveSampling(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupAdaptiveSampling"
    bl_label = "[OctaneGroupTitle]Adaptive sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;Adaptive strength;")


class OctanePathTracingKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupColor"
    bl_label = "[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")


class OctanePathTracingKernelGroupDeepImage(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupDeepImage"
    bl_label = "[OctaneGroupTitle]Deep image"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;")


class OctanePathTracingKernelGroupToonShading(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupToonShading"
    bl_label = "[OctaneGroupTitle]Toon Shading"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Toon shadow ambient;")


class OctanePathTracingKernelGroupCompatibilitySettings(OctaneGroupTitleSocket):
    bl_idname = "OctanePathTracingKernelGroupCompatibilitySettings"
    bl_label = "[OctaneGroupTitle]Compatibility settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emulate old volume behavior;")


class OctanePathTracingKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname = "OctanePathTracingKernel"
    bl_label = "Path tracing kernel"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctanePathTracingKernelGroupQuality, OctanePathTracingKernelMaxsamples, OctanePathTracingKernelMaxDiffuseDepth, OctanePathTracingKernelMaxGlossyDepth, OctanePathTracingKernelMaxScatterDepth, OctanePathTracingKernelMaxOverlappingVolumes, OctanePathTracingKernelRayepsilon, OctanePathTracingKernelFiltersize, OctanePathTracingKernelAlphashadows, OctanePathTracingKernelCausticBlur, OctanePathTracingKernelGiClamp, OctanePathTracingKernelNestedDielectrics, OctanePathTracingKernelIrradiance, OctanePathTracingKernelMaxsubdLevel, OctanePathTracingKernelAffectRoughness, OctanePathTracingKernelGroupAlphaChannel, OctanePathTracingKernelAlphachannel, OctanePathTracingKernelKeepEnvironment, OctanePathTracingKernelGroupLight, OctanePathTracingKernelAiLight, OctanePathTracingKernelAiLightUpdate, OctanePathTracingKernelGlobalLightIdMaskAction, OctanePathTracingKernelGlobalLightIdMask, OctanePathTracingKernelLightPassMask, OctanePathTracingKernelAiLightUpdateStrength, OctanePathTracingKernelAnalyticLight, OctanePathTracingKernelGroupSampling, OctanePathTracingKernelPathTermPower, OctanePathTracingKernelDirectLightRayCount, OctanePathTracingKernelCoherentRatio, OctanePathTracingKernelStaticNoise, OctanePathTracingKernelParallelSamples, OctanePathTracingKernelMaxTileSamples, OctanePathTracingKernelMinimizeNetTraffic, OctanePathTracingKernelGroupAdaptiveSampling, OctanePathTracingKernelAdaptiveSampling, OctanePathTracingKernelNoiseThreshold, OctanePathTracingKernelMinAdaptiveSamples, OctanePathTracingKernelAdaptiveSamplingPixelGroup, OctanePathTracingKernelAdaptiveSamplingExposure, OctanePathTracingKernelAdaptiveStrength, OctanePathTracingKernelGroupColor, OctanePathTracingKernelWhiteLightSpectrum, OctanePathTracingKernelUseOldColorPipeline, OctanePathTracingKernelGroupDeepImage, OctanePathTracingKernelDeepEnable, OctanePathTracingKernelDeepEnablePasses, OctanePathTracingKernelMaxDepthSamples, OctanePathTracingKernelDepthTolerance, OctanePathTracingKernelGroupToonShading, OctanePathTracingKernelToonShadowAmbient, OctanePathTracingKernelCoherentMode, OctanePathTracingKernelMaxdepth, OctanePathTracingKernelRrprob, OctanePathTracingKernelGroupCompatibilitySettings, OctanePathTracingKernelOldVolumeBehavior, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_KERN_PATHTRACING
    octane_socket_list = ["Max. samples", "Diffuse depth", "Specular depth", "Scatter depth", "Maximal overlapping volumes", "Ray epsilon", "Filter size", "Alpha shadows", "Caustic blur", "GI clamp", "Nested dielectrics", "Irradiance mode", "Max subdivision level", "Alpha channel", "Keep environment", "AI light", "AI light update", "Light IDs action", "Light IDs", "Light linking invert", "Path term. power", "Direct light rays", "Coherent ratio", "Static noise", "Parallel samples", "Max. tile samples", "Minimize net traffic", "Adaptive sampling", "Noise threshold", "Min. adaptive samples", "Pixel grouping", "Expected exposure", "White light spectrum", "Deep image", "Deep render AOVs", "Max. depth samples", "Depth tolerance", "Toon shadow ambient", "[Deprecated]Affect roughness", "[Deprecated]AI light strength", "[Deprecated]Coherent mode", "[Deprecated]Path depth", "[Deprecated]RR probability", "[Deprecated]Adaptive strength", "[Deprecated]Emulate old volume behavior", "[Deprecated]Use old color pipeline", "[Deprecated]Analytic light", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 38

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Enable legacy behavior for light visibility flags on medium (visibility on scattering for environment and null material is controlled by the diffuse flag).""", 12000005),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000099),
        ("2021.1 compatibility mode (with 4.0 volumes)", "2021.1 compatibility mode (with 4.0 volumes)", """Volume tracing behavior from version 4.0 and earlier is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000098),
        ("2018.1 compatibility mode", "2018.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 5000000),
        ("4.0 compatibility mode", "4.0 compatibility mode", """Volume tracing behavior from version 4.0 and earlier is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode_to_int, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000011, update=OctaneBaseNode.update_compatibility_mode_to_enum, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctanePathTracingKernelGroupQuality", OctanePathTracingKernelGroupQuality.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxsamples", OctanePathTracingKernelMaxsamples.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxDiffuseDepth", OctanePathTracingKernelMaxDiffuseDepth.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxGlossyDepth", OctanePathTracingKernelMaxGlossyDepth.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxScatterDepth", OctanePathTracingKernelMaxScatterDepth.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxOverlappingVolumes", OctanePathTracingKernelMaxOverlappingVolumes.bl_label).init()
        self.inputs.new("OctanePathTracingKernelRayepsilon", OctanePathTracingKernelRayepsilon.bl_label).init()
        self.inputs.new("OctanePathTracingKernelFiltersize", OctanePathTracingKernelFiltersize.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAlphashadows", OctanePathTracingKernelAlphashadows.bl_label).init()
        self.inputs.new("OctanePathTracingKernelCausticBlur", OctanePathTracingKernelCausticBlur.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGiClamp", OctanePathTracingKernelGiClamp.bl_label).init()
        self.inputs.new("OctanePathTracingKernelNestedDielectrics", OctanePathTracingKernelNestedDielectrics.bl_label).init()
        self.inputs.new("OctanePathTracingKernelIrradiance", OctanePathTracingKernelIrradiance.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxsubdLevel", OctanePathTracingKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAffectRoughness", OctanePathTracingKernelAffectRoughness.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupAlphaChannel", OctanePathTracingKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAlphachannel", OctanePathTracingKernelAlphachannel.bl_label).init()
        self.inputs.new("OctanePathTracingKernelKeepEnvironment", OctanePathTracingKernelKeepEnvironment.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupLight", OctanePathTracingKernelGroupLight.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAiLight", OctanePathTracingKernelAiLight.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAiLightUpdate", OctanePathTracingKernelAiLightUpdate.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGlobalLightIdMaskAction", OctanePathTracingKernelGlobalLightIdMaskAction.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGlobalLightIdMask", OctanePathTracingKernelGlobalLightIdMask.bl_label).init()
        self.inputs.new("OctanePathTracingKernelLightPassMask", OctanePathTracingKernelLightPassMask.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAiLightUpdateStrength", OctanePathTracingKernelAiLightUpdateStrength.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAnalyticLight", OctanePathTracingKernelAnalyticLight.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupSampling", OctanePathTracingKernelGroupSampling.bl_label).init()
        self.inputs.new("OctanePathTracingKernelPathTermPower", OctanePathTracingKernelPathTermPower.bl_label).init()
        self.inputs.new("OctanePathTracingKernelDirectLightRayCount", OctanePathTracingKernelDirectLightRayCount.bl_label).init()
        self.inputs.new("OctanePathTracingKernelCoherentRatio", OctanePathTracingKernelCoherentRatio.bl_label).init()
        self.inputs.new("OctanePathTracingKernelStaticNoise", OctanePathTracingKernelStaticNoise.bl_label).init()
        self.inputs.new("OctanePathTracingKernelParallelSamples", OctanePathTracingKernelParallelSamples.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxTileSamples", OctanePathTracingKernelMaxTileSamples.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMinimizeNetTraffic", OctanePathTracingKernelMinimizeNetTraffic.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupAdaptiveSampling", OctanePathTracingKernelGroupAdaptiveSampling.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAdaptiveSampling", OctanePathTracingKernelAdaptiveSampling.bl_label).init()
        self.inputs.new("OctanePathTracingKernelNoiseThreshold", OctanePathTracingKernelNoiseThreshold.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMinAdaptiveSamples", OctanePathTracingKernelMinAdaptiveSamples.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAdaptiveSamplingPixelGroup", OctanePathTracingKernelAdaptiveSamplingPixelGroup.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAdaptiveSamplingExposure", OctanePathTracingKernelAdaptiveSamplingExposure.bl_label).init()
        self.inputs.new("OctanePathTracingKernelAdaptiveStrength", OctanePathTracingKernelAdaptiveStrength.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupColor", OctanePathTracingKernelGroupColor.bl_label).init()
        self.inputs.new("OctanePathTracingKernelWhiteLightSpectrum", OctanePathTracingKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctanePathTracingKernelUseOldColorPipeline", OctanePathTracingKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupDeepImage", OctanePathTracingKernelGroupDeepImage.bl_label).init()
        self.inputs.new("OctanePathTracingKernelDeepEnable", OctanePathTracingKernelDeepEnable.bl_label).init()
        self.inputs.new("OctanePathTracingKernelDeepEnablePasses", OctanePathTracingKernelDeepEnablePasses.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxDepthSamples", OctanePathTracingKernelMaxDepthSamples.bl_label).init()
        self.inputs.new("OctanePathTracingKernelDepthTolerance", OctanePathTracingKernelDepthTolerance.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupToonShading", OctanePathTracingKernelGroupToonShading.bl_label).init()
        self.inputs.new("OctanePathTracingKernelToonShadowAmbient", OctanePathTracingKernelToonShadowAmbient.bl_label).init()
        self.inputs.new("OctanePathTracingKernelCoherentMode", OctanePathTracingKernelCoherentMode.bl_label).init()
        self.inputs.new("OctanePathTracingKernelMaxdepth", OctanePathTracingKernelMaxdepth.bl_label).init()
        self.inputs.new("OctanePathTracingKernelRrprob", OctanePathTracingKernelRrprob.bl_label).init()
        self.inputs.new("OctanePathTracingKernelGroupCompatibilitySettings", OctanePathTracingKernelGroupCompatibilitySettings.bl_label).init()
        self.inputs.new("OctanePathTracingKernelOldVolumeBehavior", OctanePathTracingKernelOldVolumeBehavior.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctanePathTracingKernelMaxsamples,
    OctanePathTracingKernelMaxDiffuseDepth,
    OctanePathTracingKernelMaxGlossyDepth,
    OctanePathTracingKernelMaxScatterDepth,
    OctanePathTracingKernelMaxOverlappingVolumes,
    OctanePathTracingKernelRayepsilon,
    OctanePathTracingKernelFiltersize,
    OctanePathTracingKernelAlphashadows,
    OctanePathTracingKernelCausticBlur,
    OctanePathTracingKernelGiClamp,
    OctanePathTracingKernelNestedDielectrics,
    OctanePathTracingKernelIrradiance,
    OctanePathTracingKernelMaxsubdLevel,
    OctanePathTracingKernelAlphachannel,
    OctanePathTracingKernelKeepEnvironment,
    OctanePathTracingKernelAiLight,
    OctanePathTracingKernelAiLightUpdate,
    OctanePathTracingKernelGlobalLightIdMaskAction,
    OctanePathTracingKernelGlobalLightIdMask,
    OctanePathTracingKernelLightPassMask,
    OctanePathTracingKernelPathTermPower,
    OctanePathTracingKernelDirectLightRayCount,
    OctanePathTracingKernelCoherentRatio,
    OctanePathTracingKernelStaticNoise,
    OctanePathTracingKernelParallelSamples,
    OctanePathTracingKernelMaxTileSamples,
    OctanePathTracingKernelMinimizeNetTraffic,
    OctanePathTracingKernelAdaptiveSampling,
    OctanePathTracingKernelNoiseThreshold,
    OctanePathTracingKernelMinAdaptiveSamples,
    OctanePathTracingKernelAdaptiveSamplingPixelGroup,
    OctanePathTracingKernelAdaptiveSamplingExposure,
    OctanePathTracingKernelWhiteLightSpectrum,
    OctanePathTracingKernelDeepEnable,
    OctanePathTracingKernelDeepEnablePasses,
    OctanePathTracingKernelMaxDepthSamples,
    OctanePathTracingKernelDepthTolerance,
    OctanePathTracingKernelToonShadowAmbient,
    OctanePathTracingKernelAffectRoughness,
    OctanePathTracingKernelAiLightUpdateStrength,
    OctanePathTracingKernelCoherentMode,
    OctanePathTracingKernelMaxdepth,
    OctanePathTracingKernelRrprob,
    OctanePathTracingKernelAdaptiveStrength,
    OctanePathTracingKernelOldVolumeBehavior,
    OctanePathTracingKernelUseOldColorPipeline,
    OctanePathTracingKernelAnalyticLight,
    OctanePathTracingKernelGroupQuality,
    OctanePathTracingKernelGroupAlphaChannel,
    OctanePathTracingKernelGroupLight,
    OctanePathTracingKernelGroupSampling,
    OctanePathTracingKernelGroupAdaptiveSampling,
    OctanePathTracingKernelGroupColor,
    OctanePathTracingKernelGroupDeepImage,
    OctanePathTracingKernelGroupToonShading,
    OctanePathTracingKernelGroupCompatibilitySettings,
    OctanePathTracingKernel,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


OctanePathTracingKernelGlobalLightIdMask.octane_default_node_name = "OctaneLightIDBitValue"
OctanePathTracingKernelLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"


class OctanePathTracingKernel_Override(OctanePathTracingKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, True)
        
    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")


OctanePathTracingKernelGroupCompatibilitySettings.octane_deprecated = True
OctanePathTracingKernel_Override.update_node_definition()
utility.override_class(_CLASSES, OctanePathTracingKernel, OctanePathTracingKernel_Override)
