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


class OctanePhotonTracingKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxsamples"
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


class OctanePhotonTracingKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxDiffuseDepth"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxGlossyDepth"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxScatterDepth"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxOverlappingVolumes"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelRayepsilon"
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


class OctanePhotonTracingKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelFiltersize"
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


class OctanePhotonTracingKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAlphashadows"
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


class OctanePhotonTracingKernelCausticBlur(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelCausticBlur"
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


class OctanePhotonTracingKernelGiClamp(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelGiClamp"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelNestedDielectrics"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelIrradiance"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxsubdLevel"
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
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxPhotonDepth(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxPhotonDepth"
    bl_label = "Photon depth"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_PHOTONDEPTH
    octane_pin_name = "maxPhotonDepth"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 13
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for photons", min=2, max=256, soft_min=2, soft_max=16, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAccurateColor(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAccurateColor"
    bl_label = "Accurate colors"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ACCURATE_COLOR
    octane_pin_name = "accurateColor"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 14
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled colors will be more accurate but noise will converge more slowly")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelGatherRadius(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelGatherRadius"
    bl_label = "Photon gathering radius"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_GATHER_RADIUS
    octane_pin_name = "gatherRadius"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 15
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="The maximum radius where photons can contribute", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelPhotonCountMultiplier(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelPhotonCountMultiplier"
    bl_label = "Photon count multiplier"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PHOTON_COUNT_MULTIPLIER
    octane_pin_name = "photonCountMultiplier"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 16
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Approximate ratio between photons and camera rays", min=0.250000, max=8.000000, soft_min=0.250000, soft_max=8.000000, step=25.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelPhotonGatherSamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelPhotonGatherSamples"
    bl_label = "Photon gather samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PHOTON_GATHER_SAMPLES
    octane_pin_name = "photonGatherSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 17
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=2, update=OctaneBaseSocket.update_node_tree, description="Maximal amount of photon gather samples per pixel between photon tracing passes. This is similar to max. tile samples, but it also affects the quality of caustics rendered. Higher values give more samples per second at the expense of caustic quality", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelPhotonExplorationStrength(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelPhotonExplorationStrength"
    bl_label = "Exploration strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PHOTON_EXPLORATION_STRENGTH
    octane_pin_name = "photonExplorationStrength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 18
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="The higher this value, the more the photon sampling is influenced by which photons are actually gathered", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 12000005
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAlphachannel"
    bl_label = "Alpha channel"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ALPHA_CHANNEL
    octane_pin_name = "alphachannel"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 19
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables a compositing alpha channel")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelKeepEnvironment"
    bl_label = "Keep environment"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_KEEP_ENVIRONMENT
    octane_pin_name = "keep_environment"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 20
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keeps environment with enabled alpha channel")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAiLight"
    bl_label = "AI light"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT
    octane_pin_name = "aiLight"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 21
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables AI light")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAiLightUpdate"
    bl_label = "AI light update"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_AI_LIGHT_UPDATE
    octane_pin_name = "aiLightUpdate"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 22
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables dynamic AI light update")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelGlobalLightIdMaskAction"
    bl_label = "Light IDs action"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_GLOBAL_LIGHT_ID_MASK_ACTION
    octane_pin_name = "globalLightIdMaskAction"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 23
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("Disable", "Disable", "", 1),
        ("Enable", "Enable", "", 0),
    ]
    default_value: EnumProperty(default="Disable", update=OctaneBaseSocket.update_node_tree, description="The action to be taken on selected lights IDs", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelGlobalLightIdMask"
    bl_label = "Light IDs"
    color = consts.OctanePinColor.BitMask
    octane_default_node_type = consts.NodeType.NT_BIT_MASK
    octane_default_node_name = "OctaneBitValue"
    octane_pin_id = consts.PinID.P_GLOBAL_LIGHT_ID_MASK
    octane_pin_name = "globalLightIdMask"
    octane_pin_type = consts.PinType.PT_BIT_MASK
    octane_pin_index = 24
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelLightPassMask"
    bl_label = "Light linking invert"
    color = consts.OctanePinColor.BitMask
    octane_default_node_type = consts.NodeType.NT_BIT_MASK
    octane_default_node_name = "OctaneBitValue"
    octane_pin_id = consts.PinID.P_LIGHT_PASS_MASK
    octane_pin_name = "lightPassMask"
    octane_pin_type = consts.PinType.PT_BIT_MASK
    octane_pin_index = 25
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelPathTermPower"
    bl_label = "Path term. power"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_PATH_TERM_POWER
    octane_pin_name = "pathTermPower"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 26
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Path may get terminated when ray power is less than this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelDirectLightRayCount(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelDirectLightRayCount"
    bl_label = "Direct light rays"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_DIRECT_LIGHT_RAY_COUNT
    octane_pin_name = "directLightRayCount"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 27
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of direct light rays traced for every sample. This amount is used after camera rays, and after very smooth specular reflections or transmission", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 14000000
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelCoherentRatio(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelCoherentRatio"
    bl_label = "Coherent ratio"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_COHERENT_RATIO
    octane_pin_name = "coherentRatio"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 28
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelStaticNoise(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelStaticNoise"
    bl_label = "Static noise"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_STATIC_NOISE
    octane_pin_name = "staticNoise"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 29
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the noise patterns are kept stable between frames")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelParallelSamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelParallelSamples"
    bl_label = "Parallel samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PARALLEL_SAMPLES
    octane_pin_name = "parallelSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 30
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxTileSamples"
    bl_label = "Max. tile samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_TILE_SAMPLES
    octane_pin_name = "maxTileSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 31
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=32, update=OctaneBaseSocket.update_node_tree, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 12000008
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMinimizeNetTraffic"
    bl_label = "Minimize net traffic"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_MINIMIZE_NET_TRAFFIC
    octane_pin_name = "minimizeNetTraffic"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 32
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAdaptiveSampling(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAdaptiveSampling"
    bl_label = "Adaptive sampling"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING
    octane_pin_name = "adaptiveSampling"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 33
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Stops rendering clean parts of the image and focuses on noisy parts")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelNoiseThreshold(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelNoiseThreshold"
    bl_label = "Noise threshold"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_NOISE_THRESHOLD
    octane_pin_name = "noiseThreshold"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 34
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.020000, update=OctaneBaseSocket.update_node_tree, description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMinAdaptiveSamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMinAdaptiveSamples"
    bl_label = "Min. adaptive samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MIN_ADAPTIVE_SAMPLES
    octane_pin_name = "minAdaptiveSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 35
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=512, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples per pixel until adaptive sampling kicks in. Set it to a higher value if you notice that the error estimate is incorrect and stops sampling pixels too early resulting in artifacts.\nOnly valid if adaptive sampling is enabled", min=2, max=1000000, soft_min=2, soft_max=100000, step=1, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAdaptiveSamplingPixelGroup(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAdaptiveSamplingPixelGroup"
    bl_label = "Pixel grouping"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING_PIXEL_GROUP
    octane_pin_name = "adaptiveSamplingPixelGroup"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 36
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("None", "None", "", 1),
        ("2 x 2", "2 x 2", "", 2),
        ("4 x 4", "4 x 4", "", 4),
    ]
    default_value: EnumProperty(default="2 x 2", update=OctaneBaseSocket.update_node_tree, description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelAdaptiveSamplingExposure(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelAdaptiveSamplingExposure"
    bl_label = "Expected exposure"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_ADAPTIVE_SAMPLING_EXPOSURE
    octane_pin_name = "adaptiveSamplingExposure"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 37
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The expected exposure should be approximately the same value as the exposure in the imager or 0 to ignore this settings.\nIt's used by adaptive sampling to determine which pixels are bright and which are dark, which obviously depends on the exposure setting in the imaging settings. Adaptive sampling tweaks/reduces the noise estimate of very dark areas of the image. It also increases the min. adaptive samples limit for very dark areas which tend to find paths to light sources only very irregularly and thus have a too optimistic noise estimate", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=4096.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelWhiteLightSpectrum"
    bl_label = "White light spectrum"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_ENUM
    octane_default_node_name = "OctaneEnumValue"
    octane_pin_id = consts.PinID.P_WHITE_LIGHT_SPECTRUM
    octane_pin_name = "whiteLightSpectrum"
    octane_pin_type = consts.PinType.PT_ENUM
    octane_pin_index = 38
    octane_socket_type = consts.SocketType.ST_ENUM
    items = [
        ("D65", "D65", "", 1),
        ("Legacy/flat", "Legacy/flat", "", 0),
    ]
    default_value: EnumProperty(default="D65", update=OctaneBaseSocket.update_node_tree, description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, black body emitters). This determines the spectrum that will produce white (before white balance) in the final image. Use D65 to adapt to a reasonable daylight \"white\" color. Use Legacy/flat to preserve the appearance of old projects (spectral emitters will appear rather blue)", items=items)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelDeepEnable(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelDeepEnable"
    bl_label = "Deep image"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DEEP_ENABLE
    octane_pin_name = "deepEnable"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 39
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render a deep image")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelDeepEnablePasses"
    bl_label = "Deep render AOVs"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_DEEP_ENABLE_PASSES
    octane_pin_name = "deepEnablePasses"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 40
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Include render AOVs in deep pixels")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelMaxDepthSamples"
    bl_label = "Max. depth samples"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_MAX_DEPTH_SAMPLES
    octane_pin_name = "maxDepthSamples"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 41
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelDepthTolerance(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelDepthTolerance"
    bl_label = "Depth tolerance"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_DEPTH_TOLERANCE
    octane_pin_name = "depthTolerance"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 42
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.050000, update=OctaneBaseSocket.update_node_tree, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_TOON_SHADOW_AMBIENT
    octane_pin_name = "toonShadowAmbient"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 43
    octane_socket_type = consts.SocketType.ST_RGBA
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The ambient modifier of toon shadowing", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, subtype="COLOR", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctanePhotonTracingKernelOldVolumeBehavior(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelOldVolumeBehavior"
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
    octane_min_version = 0
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePhotonTracingKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelUseOldColorPipeline"
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
    octane_min_version = 0
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePhotonTracingKernelExplorationStrength(OctaneBaseSocket):
    bl_idname = "OctanePhotonTracingKernelExplorationStrength"
    bl_label = "[Deprecated]Exploration strength"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_EXPLORATION_STRENGTH
    octane_pin_name = "exploration_strength"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 46
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="deprecated", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 12000005
    octane_deprecated = True


class OctanePhotonTracingKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupQuality"
    bl_label = "[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;")


class OctanePhotonTracingKernelGroupPhotons(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupPhotons"
    bl_label = "[OctaneGroupTitle]Photons"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Photon depth;Accurate colors;Photon gathering radius;Photon count multiplier;Photon gather samples;Exploration strength;Exploration strength;")


class OctanePhotonTracingKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupAlphaChannel"
    bl_label = "[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;Keep environment;")


class OctanePhotonTracingKernelGroupLight(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupLight"
    bl_label = "[OctaneGroupTitle]Light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="AI light;AI light update;Light IDs action;Light IDs;Light linking invert;")


class OctanePhotonTracingKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupSampling"
    bl_label = "[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Path term. power;Direct light rays;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;")


class OctanePhotonTracingKernelGroupAdaptiveSampling(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupAdaptiveSampling"
    bl_label = "[OctaneGroupTitle]Adaptive sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;")


class OctanePhotonTracingKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupColor"
    bl_label = "[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")


class OctanePhotonTracingKernelGroupDeepImage(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupDeepImage"
    bl_label = "[OctaneGroupTitle]Deep image"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;")


class OctanePhotonTracingKernelGroupToonShading(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupToonShading"
    bl_label = "[OctaneGroupTitle]Toon Shading"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Toon shadow ambient;")


class OctanePhotonTracingKernelGroupCompatibilitySettings(OctaneGroupTitleSocket):
    bl_idname = "OctanePhotonTracingKernelGroupCompatibilitySettings"
    bl_label = "[OctaneGroupTitle]Compatibility settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emulate old volume behavior;")


class OctanePhotonTracingKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname = "OctanePhotonTracingKernel"
    bl_label = "Photon tracing kernel"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctanePhotonTracingKernelGroupQuality, OctanePhotonTracingKernelMaxsamples, OctanePhotonTracingKernelMaxDiffuseDepth, OctanePhotonTracingKernelMaxGlossyDepth, OctanePhotonTracingKernelMaxScatterDepth, OctanePhotonTracingKernelMaxOverlappingVolumes, OctanePhotonTracingKernelRayepsilon, OctanePhotonTracingKernelFiltersize, OctanePhotonTracingKernelAlphashadows, OctanePhotonTracingKernelCausticBlur, OctanePhotonTracingKernelGiClamp, OctanePhotonTracingKernelNestedDielectrics, OctanePhotonTracingKernelIrradiance, OctanePhotonTracingKernelMaxsubdLevel, OctanePhotonTracingKernelGroupPhotons, OctanePhotonTracingKernelMaxPhotonDepth, OctanePhotonTracingKernelAccurateColor, OctanePhotonTracingKernelGatherRadius, OctanePhotonTracingKernelPhotonCountMultiplier, OctanePhotonTracingKernelPhotonGatherSamples, OctanePhotonTracingKernelPhotonExplorationStrength, OctanePhotonTracingKernelExplorationStrength, OctanePhotonTracingKernelGroupAlphaChannel, OctanePhotonTracingKernelAlphachannel, OctanePhotonTracingKernelKeepEnvironment, OctanePhotonTracingKernelGroupLight, OctanePhotonTracingKernelAiLight, OctanePhotonTracingKernelAiLightUpdate, OctanePhotonTracingKernelGlobalLightIdMaskAction, OctanePhotonTracingKernelGlobalLightIdMask, OctanePhotonTracingKernelLightPassMask, OctanePhotonTracingKernelGroupSampling, OctanePhotonTracingKernelPathTermPower, OctanePhotonTracingKernelDirectLightRayCount, OctanePhotonTracingKernelCoherentRatio, OctanePhotonTracingKernelStaticNoise, OctanePhotonTracingKernelParallelSamples, OctanePhotonTracingKernelMaxTileSamples, OctanePhotonTracingKernelMinimizeNetTraffic, OctanePhotonTracingKernelGroupAdaptiveSampling, OctanePhotonTracingKernelAdaptiveSampling, OctanePhotonTracingKernelNoiseThreshold, OctanePhotonTracingKernelMinAdaptiveSamples, OctanePhotonTracingKernelAdaptiveSamplingPixelGroup, OctanePhotonTracingKernelAdaptiveSamplingExposure, OctanePhotonTracingKernelGroupColor, OctanePhotonTracingKernelWhiteLightSpectrum, OctanePhotonTracingKernelUseOldColorPipeline, OctanePhotonTracingKernelGroupDeepImage, OctanePhotonTracingKernelDeepEnable, OctanePhotonTracingKernelDeepEnablePasses, OctanePhotonTracingKernelMaxDepthSamples, OctanePhotonTracingKernelDepthTolerance, OctanePhotonTracingKernelGroupToonShading, OctanePhotonTracingKernelToonShadowAmbient, OctanePhotonTracingKernelGroupCompatibilitySettings, OctanePhotonTracingKernelOldVolumeBehavior, ]
    octane_min_version = 12000000
    octane_node_type = consts.NodeType.NT_KERN_PHOTONTRACING
    octane_socket_list = ["Max. samples", "Diffuse depth", "Specular depth", "Scatter depth", "Maximal overlapping volumes", "Ray epsilon", "Filter size", "Alpha shadows", "Caustic blur", "GI clamp", "Nested dielectrics", "Irradiance mode", "Max subdivision level", "Photon depth", "Accurate colors", "Photon gathering radius", "Photon count multiplier", "Photon gather samples", "Exploration strength", "Alpha channel", "Keep environment", "AI light", "AI light update", "Light IDs action", "Light IDs", "Light linking invert", "Path term. power", "Direct light rays", "Coherent ratio", "Static noise", "Parallel samples", "Max. tile samples", "Minimize net traffic", "Adaptive sampling", "Noise threshold", "Min. adaptive samples", "Pixel grouping", "Expected exposure", "White light spectrum", "Deep image", "Deep render AOVs", "Max. depth samples", "Depth tolerance", "Toon shadow ambient", "[Deprecated]Emulate old volume behavior", "[Deprecated]Use old color pipeline", "[Deprecated]Exploration strength", ]
    octane_attribute_list = ["a_compatibility_version", ]
    octane_attribute_config = {"a_compatibility_version": [consts.AttributeID.A_COMPATIBILITY_VERSION, "compatibilityVersion", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 44

    compatibility_mode_infos = [
        ("Latest (2023.1.1)", "Latest (2023.1.1)", """(null)""", 13000100),
        ("2022.1 compatibility mode", "2022.1 compatibility mode", """Enable legacy behavior for light visibility flags on medium (visibility on scattering for environment and null material is controlled by the diffuse flag).""", 12000005),
        ("2021.1 compatibility mode", "2021.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000099),
        ("2021.1 compatibility mode (with 4.0 volumes)", "2021.1 compatibility mode (with 4.0 volumes)", """Volume tracing behavior from version 4.0 and earlier is used. This applies in addition to 2022.1 compatibility mode behavior.""", 11000098),
        ("2018.1 compatibility mode", "2018.1 compatibility mode", """Volume tracing behavior from versions 2018.1 to 2021.1 is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 5000000),
        ("4.0 compatibility mode", "4.0 compatibility mode", """Volume tracing behavior from version 4.0 and earlier is used. Original pipeline for converting colors to and from spectra and for applying white balance is used (textures with colors outside the sRGB gamut will be rendered inaccurately). This applies in addition to 2022.1 compatibility mode behavior.""", 0),
    ]
    a_compatibility_version_enum: EnumProperty(name="Compatibility version", default="Latest (2023.1.1)", update=OctaneBaseNode.update_compatibility_mode, description="The Octane version that the behavior of this node should match", items=compatibility_mode_infos)

    a_compatibility_version: IntProperty(name="Compatibility version", default=14000005, update=OctaneBaseNode.update_node_tree, description="The Octane version that the behavior of this node should match")

    def init(self, context):  # noqa
        self.inputs.new("OctanePhotonTracingKernelGroupQuality", OctanePhotonTracingKernelGroupQuality.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxsamples", OctanePhotonTracingKernelMaxsamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxDiffuseDepth", OctanePhotonTracingKernelMaxDiffuseDepth.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxGlossyDepth", OctanePhotonTracingKernelMaxGlossyDepth.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxScatterDepth", OctanePhotonTracingKernelMaxScatterDepth.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxOverlappingVolumes", OctanePhotonTracingKernelMaxOverlappingVolumes.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelRayepsilon", OctanePhotonTracingKernelRayepsilon.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelFiltersize", OctanePhotonTracingKernelFiltersize.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAlphashadows", OctanePhotonTracingKernelAlphashadows.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelCausticBlur", OctanePhotonTracingKernelCausticBlur.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGiClamp", OctanePhotonTracingKernelGiClamp.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelNestedDielectrics", OctanePhotonTracingKernelNestedDielectrics.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelIrradiance", OctanePhotonTracingKernelIrradiance.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxsubdLevel", OctanePhotonTracingKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupPhotons", OctanePhotonTracingKernelGroupPhotons.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxPhotonDepth", OctanePhotonTracingKernelMaxPhotonDepth.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAccurateColor", OctanePhotonTracingKernelAccurateColor.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGatherRadius", OctanePhotonTracingKernelGatherRadius.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelPhotonCountMultiplier", OctanePhotonTracingKernelPhotonCountMultiplier.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelPhotonGatherSamples", OctanePhotonTracingKernelPhotonGatherSamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelPhotonExplorationStrength", OctanePhotonTracingKernelPhotonExplorationStrength.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelExplorationStrength", OctanePhotonTracingKernelExplorationStrength.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupAlphaChannel", OctanePhotonTracingKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAlphachannel", OctanePhotonTracingKernelAlphachannel.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelKeepEnvironment", OctanePhotonTracingKernelKeepEnvironment.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupLight", OctanePhotonTracingKernelGroupLight.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAiLight", OctanePhotonTracingKernelAiLight.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAiLightUpdate", OctanePhotonTracingKernelAiLightUpdate.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGlobalLightIdMaskAction", OctanePhotonTracingKernelGlobalLightIdMaskAction.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGlobalLightIdMask", OctanePhotonTracingKernelGlobalLightIdMask.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelLightPassMask", OctanePhotonTracingKernelLightPassMask.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupSampling", OctanePhotonTracingKernelGroupSampling.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelPathTermPower", OctanePhotonTracingKernelPathTermPower.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelDirectLightRayCount", OctanePhotonTracingKernelDirectLightRayCount.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelCoherentRatio", OctanePhotonTracingKernelCoherentRatio.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelStaticNoise", OctanePhotonTracingKernelStaticNoise.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelParallelSamples", OctanePhotonTracingKernelParallelSamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxTileSamples", OctanePhotonTracingKernelMaxTileSamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMinimizeNetTraffic", OctanePhotonTracingKernelMinimizeNetTraffic.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupAdaptiveSampling", OctanePhotonTracingKernelGroupAdaptiveSampling.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAdaptiveSampling", OctanePhotonTracingKernelAdaptiveSampling.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelNoiseThreshold", OctanePhotonTracingKernelNoiseThreshold.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMinAdaptiveSamples", OctanePhotonTracingKernelMinAdaptiveSamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAdaptiveSamplingPixelGroup", OctanePhotonTracingKernelAdaptiveSamplingPixelGroup.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelAdaptiveSamplingExposure", OctanePhotonTracingKernelAdaptiveSamplingExposure.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupColor", OctanePhotonTracingKernelGroupColor.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelWhiteLightSpectrum", OctanePhotonTracingKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelUseOldColorPipeline", OctanePhotonTracingKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupDeepImage", OctanePhotonTracingKernelGroupDeepImage.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelDeepEnable", OctanePhotonTracingKernelDeepEnable.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelDeepEnablePasses", OctanePhotonTracingKernelDeepEnablePasses.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelMaxDepthSamples", OctanePhotonTracingKernelMaxDepthSamples.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelDepthTolerance", OctanePhotonTracingKernelDepthTolerance.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupToonShading", OctanePhotonTracingKernelGroupToonShading.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelToonShadowAmbient", OctanePhotonTracingKernelToonShadowAmbient.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelGroupCompatibilitySettings", OctanePhotonTracingKernelGroupCompatibilitySettings.bl_label).init()
        self.inputs.new("OctanePhotonTracingKernelOldVolumeBehavior", OctanePhotonTracingKernelOldVolumeBehavior.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.row().prop(self, "a_compatibility_version_enum")


_CLASSES = [
    OctanePhotonTracingKernelMaxsamples,
    OctanePhotonTracingKernelMaxDiffuseDepth,
    OctanePhotonTracingKernelMaxGlossyDepth,
    OctanePhotonTracingKernelMaxScatterDepth,
    OctanePhotonTracingKernelMaxOverlappingVolumes,
    OctanePhotonTracingKernelRayepsilon,
    OctanePhotonTracingKernelFiltersize,
    OctanePhotonTracingKernelAlphashadows,
    OctanePhotonTracingKernelCausticBlur,
    OctanePhotonTracingKernelGiClamp,
    OctanePhotonTracingKernelNestedDielectrics,
    OctanePhotonTracingKernelIrradiance,
    OctanePhotonTracingKernelMaxsubdLevel,
    OctanePhotonTracingKernelMaxPhotonDepth,
    OctanePhotonTracingKernelAccurateColor,
    OctanePhotonTracingKernelGatherRadius,
    OctanePhotonTracingKernelPhotonCountMultiplier,
    OctanePhotonTracingKernelPhotonGatherSamples,
    OctanePhotonTracingKernelPhotonExplorationStrength,
    OctanePhotonTracingKernelAlphachannel,
    OctanePhotonTracingKernelKeepEnvironment,
    OctanePhotonTracingKernelAiLight,
    OctanePhotonTracingKernelAiLightUpdate,
    OctanePhotonTracingKernelGlobalLightIdMaskAction,
    OctanePhotonTracingKernelGlobalLightIdMask,
    OctanePhotonTracingKernelLightPassMask,
    OctanePhotonTracingKernelPathTermPower,
    OctanePhotonTracingKernelDirectLightRayCount,
    OctanePhotonTracingKernelCoherentRatio,
    OctanePhotonTracingKernelStaticNoise,
    OctanePhotonTracingKernelParallelSamples,
    OctanePhotonTracingKernelMaxTileSamples,
    OctanePhotonTracingKernelMinimizeNetTraffic,
    OctanePhotonTracingKernelAdaptiveSampling,
    OctanePhotonTracingKernelNoiseThreshold,
    OctanePhotonTracingKernelMinAdaptiveSamples,
    OctanePhotonTracingKernelAdaptiveSamplingPixelGroup,
    OctanePhotonTracingKernelAdaptiveSamplingExposure,
    OctanePhotonTracingKernelWhiteLightSpectrum,
    OctanePhotonTracingKernelDeepEnable,
    OctanePhotonTracingKernelDeepEnablePasses,
    OctanePhotonTracingKernelMaxDepthSamples,
    OctanePhotonTracingKernelDepthTolerance,
    OctanePhotonTracingKernelToonShadowAmbient,
    OctanePhotonTracingKernelOldVolumeBehavior,
    OctanePhotonTracingKernelUseOldColorPipeline,
    OctanePhotonTracingKernelExplorationStrength,
    OctanePhotonTracingKernelGroupQuality,
    OctanePhotonTracingKernelGroupPhotons,
    OctanePhotonTracingKernelGroupAlphaChannel,
    OctanePhotonTracingKernelGroupLight,
    OctanePhotonTracingKernelGroupSampling,
    OctanePhotonTracingKernelGroupAdaptiveSampling,
    OctanePhotonTracingKernelGroupColor,
    OctanePhotonTracingKernelGroupDeepImage,
    OctanePhotonTracingKernelGroupToonShading,
    OctanePhotonTracingKernelGroupCompatibilitySettings,
    OctanePhotonTracingKernel,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #


OctanePhotonTracingKernelGlobalLightIdMask.octane_default_node_name = "OctaneLightIDBitValue"
OctanePhotonTracingKernelLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"


class OctanePhotonTracingKernel_Override(OctanePhotonTracingKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, True)

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "a_compatibility_version_enum")


OctanePhotonTracingKernelGroupCompatibilitySettings.octane_deprecated = True
OctanePhotonTracingKernel_Override.update_node_definition()
utility.override_class(_CLASSES, OctanePhotonTracingKernel, OctanePhotonTracingKernel_Override)
