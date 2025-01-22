# <pep8 compliant>

from octane.utils.octaneid import *

ENGINE_NAME = "octane"
ADDON_NAME = "octane"

DERIVED_NODE_NAMES = "DERIVED_NODE_NAMES"
DERIVED_NODE_TYPES = "DERIVED_NODE_TYPES"
DERIVED_NODE_SEPARATOR = "###DERIVED_NODE_SEPARATOR###"
OBJECT_INDEX_SEPARATOR = "###OBJECT_INDEX###"
OCTANE_EXPORT_VIEW_LAYER_TAG = "$VIEW_LAYER$"
OCTANE_EXPORT_OCTANE_PASS_TAG = "$OCTANE_PASS$"

OCTANE_BLENDER_STATIC_FRONT_PROJECTION = "OCTANE_BLENDER_STATIC_FRONT_PROJECTION"
OCTANE_BLENDER_STATIC_FRONT_PROJECTION_TRANSFORM = "OCTANE_BLENDER_STATIC_FRONT_PROJECTION_TRANSFORM"
OCTANE_BLENDER_CAMERA_MODE = "OCTANE_BLENDER_CAMERA_MODE"
OCTANE_BLENDER_CAMERA_CENTER_X = "OCTANE_BLENDER_CAMERA_CENTER_X"
OCTANE_BLENDER_CAMERA_CENTER_Y = "OCTANE_BLENDER_CAMERA_CENTER_Y"
OCTANE_BLENDER_CAMERA_REGION_WIDTH = "OCTANE_BLENDER_CAMERA_REGION_WIDTH"
OCTANE_BLENDER_CAMERA_REGION_HEIGHT = "OCTANE_BLENDER_CAMERA_REGION_HEIGHT"
OCTANE_BLENDER_CAMERA_IMAGER_LUT = "OCTANE_BLENDER_CAMERA_IMAGER_LUT"
OCTANE_BLENDER_CAMERA_IMAGER_OCIO_VIEW = "OCTANE_BLENDER_CAMERA_IMAGER_OCIO_VIEW"
OCTANE_BLENDER_CAMERA_IMAGER_OCIO_LOOK = "OCTANE_BLENDER_CAMERA_IMAGER_OCIO_LOOK"

LEGACY_OCTANE_HELPER_NODE_GROUP = "[OCTANE_HELPER_NODE_GROUP]"
OCTANE_HELPER_NODE_GROUP = ".[OCTANE_HELPER_NODE_GROUP]"

DEPRECATED_PREFIX = "[Deprecated]"

# Add Blender Pin Type
PinType.PT_BLENDER_OUTPUT = -10000
PinType.PT_BLENDER_INPUT = -10001
PinType.PT_BLENDER_VALUES = -10002
PinType.PT_BLENDER_UTILITY = -20000
# Add Octane Legacy Pin Type
PinType.PT_COMPOSITE_AOV_LAYER = PinType.PT_OUTPUT_AOV_LAYER

# Add Blender Node Type
NodeType.NT_BLENDER_NODE_OFFSET = -100000
NodeType.NT_BLENDER_NODE_OCTANE_PROXY = -100001
NodeType.NT_BLENDER_NODE_OBJECT_DATA = -100002
NodeType.NT_BLENDER_NODE_CAMERA_DATA = -100003
NodeType.NT_BLENDER_NODE_IMAGE_INFO = -100004
NodeType.NT_BLENDER_NODE_GET_RENDER_RESULT = -100005
NodeType.NT_BLENDER_NODE_START_RENDER = -100006
NodeType.NT_BLENDER_NODE_STOP_RENDER = -100007
NodeType.NT_BLENDER_NODE_RESET_RENDER = -100008
NodeType.NT_BLENDER_NODE_SCATTER = -100009
NodeType.NT_BLENDER_NODE_MESH = -100010
NodeType.NT_BLENDER_NODE_VOLUME = -100011
NodeType.NT_BLENDER_NODE_GRAPH_NODE = -100012
# Add Octane Legacy Node Type
NodeType.NT_OUT_COMPOSITE_AOV_LAYER = NodeType.NT_OUT_OUTPUT_AOV_LAYER


# Octane Version Type
class VersionType:
    UNKNOWN = -1
    STUDIO = 0
    PRIME = 1
    DEMO = 2


# Scene State
class SceneState:
    UNINIT = 0
    INITIALIZED = 1


# Batch State
class BatchState:
    DISABLED = 0
    START_BATCH = 1
    END_BATCH = 2


# Render Frame Data Type
class RenderFrameDataType:
    RENDER_FRAME_SIGNED_BYTE_RGBA = 0  # -127~128
    RENDER_FRAME_FLOAT_RGBA = 1
    RENDER_FRAME_FLOAT_MONO = 2


class ExportRenderPassMode:
    EXPORT_RENDER_PASS_MODE_SEPARATE = 0
    EXPORT_RENDER_PASS_MODE_MULTILAYER = 1
    EXPORT_RENDER_PASS_MODE_DEEP_EXR = 2


class ImageSaveFormat:
    IMAGE_SAVE_FORMAT_PNG_8 = 0
    IMAGE_SAVE_FORMAT_PNG_16 = 1
    IMAGE_SAVE_FORMAT_EXR_16 = 2
    IMAGE_SAVE_FORMAT_EXR_32 = 3
    IMAGE_SAVE_FORMAT_TIFF_8 = 4
    IMAGE_SAVE_FORMAT_TIFF_16 = 5
    IMAGE_SAVE_FORMAT_JPEG = 6


# The different tonemap result buffer formats we support.
class TonemapBufferType:
    # LDR tonemapping resulting in uint8_t per channel (should only be used when outputting in a non-linear color
    # space).
    TONEMAP_BUFFER_TYPE_LDR = 0
    # HDR tonemapping resulting in float per channel.
    TONEMAP_BUFFER_TYPE_HDR_FLOAT = 1
    # Same as TONEMAP_BUFFER_TYPE_HDR_FLOAT but the results are converted to half (16-bit) floating point.
    # This is only supported on macOS/iOS.
    TONEMAP_BUFFER_TYPE_HDR_HALF = 2


# Specific color spaces that Octane knows about.
class NamedColorSpace:
    # A custom color space that this enum can't identify.
    NAMED_COLOR_SPACE_OTHER = 0
    # The sRGB color space.
    NAMED_COLOR_SPACE_SRGB = 1
    # The sRGB color space with a linear transfer function.
    NAMED_COLOR_SPACE_LINEAR_SRGB = 2
    # The ACES2065-1 color space, which is a linear color space using the ACES AP0 primaries and a white point very
    # close to "D60".
    NAMED_COLOR_SPACE_ACES2065_1 = 3
    # The ACEScg color space, which is a linear color space using the ACES AP1 primaries and a white point very close
    # to "D60".
    NAMED_COLOR_SPACE_ACESCG = 4
    # The XYZ color space (with E white point).
    NAMED_COLOR_SPACE_XYZ_E = 5
    # A placeholder value to represent some OCIO color space. We don't have any further details about these color
    # spaces.
    NAMED_COLOR_SPACE_OCIO = 1000


# Render Session type
class SessionType:
    UNKNOWN = 0
    VIEWPORT = 1
    FINAL_RENDER = 2
    PREVIEW = 3
    EXPORT = 4


# Node Resource type
class NodeResourceType:
    LIGHT = 0
    HEAVY = 1
    TEXTURE = 1
    GEOMETRY = 2


# Resource cache type
class ResourceCacheType:
    NONE = 0
    TEXTURE_ONLY = 1
    GEOMETRY_ONLY = 2
    ALL = 127


# Blender Scene Data type
class SceneDataType:
    MESH = 0
    SUBDIVISION_MESH = 1
    OBJECT = 2


# Octane Data Block Symbol Type
class OctaneDataBlockSymbolType:
    ATTRIBUTE_ID = 0
    ATTRIBUTE_NAME = 1
    ATTRIBUTE_CUSTOM = 2
    PIN_OFFSET = 10
    PIN_ID = 10
    PIN_NAME = 11
    PIN_INDEX = 12
    PIN_DYNAMIC = 13
    PIN_CUSTOM = 14


# Legacy OctaneDataTransferObject Type
class LegacyDTOType:
    DTO_NONE = 0
    DTO_BOOL = 1
    DTO_FLOAT = 2
    DTO_FLOAT_2 = 3
    DTO_FLOAT_3 = 4
    DTO_RGB = 5
    DTO_ENUM = 6
    DTO_INT = 7
    DTO_INT_2 = 8
    DTO_INT_3 = 9
    DTO_STR = 10
    DTO_SHADER = 11


# Socket type
class SocketType:
    ST_UNKNOWN = 0
    ST_BOOL = 1
    ST_ENUM = 2
    ST_INT = 3
    ST_INT2 = 4
    ST_INT3 = 5
    ST_FLOAT = 6
    ST_FLOAT2 = 7
    ST_FLOAT3 = 8
    ST_RGBA = 9
    ST_STRING = 10
    ST_LINK = 11
    ST_INT4 = 12
    ST_FLOAT4 = 13
    ST_OUTPUT = 100
    ST_GROUP_TITLE = 1000


# Auto Refresh Strategy
class AutoRefreshStrategy:
    DISABLE = 0
    FRAME_CHANGE = 1
    ALWAYS = 2


# Pin color
class OctanePinColor:
    Default = (1, 1, 1, 1)
    GroupTitle = (0, 0, 0, 0)
    BlenderEditor = (0.7, 0.7, 0.7, 0.7)
    Bool = (0.87, 0.66, 0.83, 0.70)
    Float = (0.50, 0.70, 0.90, 0.70)
    Int = (1.00, 0.84, 0.17, 0.70)
    Transform = (0.75, 0.87, 1.00, 0.70)
    Texture = (0.75, 1.00, 0.87, 0.70)
    Emission = (1.00, 1.00, 1.00, 0.70)
    Material = (1.00, 0.95, 0.74, 0.70)
    Camera = (0.50, 1.00, 1.00, 0.70)
    Environment = (0.50, 0.50, 1.00, 0.70)
    Imager = (0.50, 1.00, 0.50, 0.70)
    Kernel = (1.00, 0.80, 0.50, 0.70)
    Geometry = (1.00, 0.74, 0.95, 0.70)
    Medium = (1.00, 0.95, 0.74, 0.70)
    PhaseFunction = (1.00, 1.00, 1.00, 0.70)
    FilmSettings = (1.00, 1.00, 1.00, 0.70)
    Enum = (1.00, 1.00, 1.00, 0.70)
    ObjectLayer = (1.00, 1.00, 1.00, 0.70)
    PostProcessing = (1.00, 0.30, 1.00, 0.70)
    RenderTarget = (0.90, 0.90, 0.90, 0.70)
    WorkPane = (1.00, 1.00, 1.00, 0.70)
    Projection = (1.00, 1.00, 1.00, 0.70)
    Displacement = (1.00, 1.00, 1.00, 0.70)
    String = (1.00, 1.00, 1.00, 0.70)
    RenderAOV = (1.00, 1.00, 1.00, 0.70)
    RenderLayer = (0.90, 0.50, 0.00, 0.70)
    VolumeRamp = (1.00, 1.00, 1.00, 0.70)
    AnimationSettings = (1.00, 1.00, 1.00, 0.70)
    LUT = (1.00, 1.00, 1.00, 0.70)
    RenderJob = (1.00, 1.00, 1.00, 0.70)
    ToonRamp = (1.00, 1.00, 1.00, 0.70)
    BitMask = (1.00, 1.00, 1.00, 0.70)
    RoundEdges = (1.00, 1.00, 1.00, 0.70)
    MaterialLayer = (1.00, 1.00, 1.00, 0.70)
    OCIOView = (1.00, 1.00, 1.00, 0.70)
    OCIOLook = (1.00, 1.00, 1.00, 0.70)
    OCIOColorSpace = (1.00, 1.00, 1.00, 0.70)
    OutputAOVGroup = (1.00, 1.00, 1.00, 0.70)
    OutputAOV = (1.00, 1.00, 1.00, 0.70)
    TextureLayer = (1.00, 1.00, 1.00, 0.70)
    OutputAOVLayer = (1.00, 1.00, 1.00, 0.70)
    BlendingSettings = (1.00, 1.00, 1.00, 0.70)
    PostVolume = (0.80, 0.24, 0.80, 0.70)
    # Legacy values
    AOVOutputGroup = OutputAOVGroup
    AOVOutput = OutputAOV
    CompositeAOVOutputLayer = OutputAOVLayer
    CompositeTextureLayer = TextureLayer


class ArrayIdentifier:
    ARRAY_INFO_POINT_DATA = "POINT"
    ARRAY_INFO_NORMAL_DATA = "NORMAL"
    ARRAY_INFO_POINT_INDEX_DATA = "POINT_INDEX"
    ARRAY_INFO_NORMAL_INDEX_DATA = "NORMAL_INDEX"
    ARRAY_INFO_VERTEX_PER_POLY_DATA = "VERTEX_PER_POLY"
    ARRAY_INFO_MAT_ID_POLY_DATA = "MATERIAL_ID_PER_POLY"
    ARRAY_INFO_OBJ_ID_POLY_DATA = "OBJECT_ID_PER_POLY"
    ARRAY_INFO_UV_DATA = "UV"
    ARRAY_INFO_UV_INDEX_DATA = "UV_INDEX"
    ARRAY_INFO_CANDIDATE_UV_DATA = "CANDIDATE_UV"
    ARRAY_INFO_CANDIDATE_UV_INDEX_DATA = "CANDIDATE_UV_INDEX"
    ARRAY_INFO_VERTEX_COLOR_DATA = "VERTEX_COLOR"
    ARRAY_INFO_VERTEX_FLOAT_DATA = "VERTEX_FLOAT"
    ARRAY_INFO_VELOCITY_DATA = "VERTEX_VELOCITY"
    ARRAY_INFO_HAIR_POINT_DATA = "HAIR_POINT"
    ARRAY_INFO_HAIR_VERTEX_PER_HAIR_DATA = "HAIR_VERTEX_PER_HAIR"
    ARRAY_INFO_HAIR_THICKNESS_DATA = "HAIR_THICKNESS"
    ARRAY_INFO_HAIR_MAT_INDEX_DATA = "HAIR_MAT_INDEX"
    ARRAY_INFO_HAIR_UV_DATA = "HAIR_UV"
    ARRAY_INFO_HAIR_W_DATA = "HAIR_W"
    ARRAY_INFO_OPENSUBDIVISION_CREASE_INDEX = "OPENSUBDIVISION_CREASE_INDEX"
    ARRAY_INFO_OPENSUBDIVISION_CREASE_SHARPNESS = "OPENSUBDIVISION_CREASE_SHARPNESS"
    ARRAY_INFO_MATRIX_DATA = "MATRIX"
    ARRAY_INFO_INSTANCE_ID_DATA = "INSTANCE_ID"
    ARRAY_INFO_SPHERE_CENTER_DATA = "SPHERE_CENTER"
    ARRAY_INFO_SPHERE_RADIUS_DATA = "SPHERE_RADIUS"
    ARRAY_INFO_SPHERE_SPEED_DATA = "SPHERE_SPEED"
    ARRAY_INFO_SPHERE_UV_DATA = "SPHERE_UV"
    ARRAY_INFO_SPHERE_VERTEX_COLOR_DATA = "SPHERE_VERTEX_COLOR"
    ARRAY_INFO_SPHERE_VERTEX_FLOAT_DATA = "SPHERE_VERTEX_FLOAT"
    ARRAY_INFO_SPHERE_MATERIAL_INDEX_DATA = "SPHERE_MATERIAL_INDEX"


# Octane NodeTree
class OctaneNodeTree:
    GENERAL = "OCTANE_TREE"
    CAMERA_IMAGER = "OCTANE_CAMERA_IMAGER_TREE"
    COMPOSITE = "OCTANE_COMPOSITE_TREE"
    KERNEL = "OCTANE_KERNEL_TREE"
    RENDER_AOV = "OCTANE_RENDER_AOV_TREE"
    BLENDER_SHADER = "OCTANE_SHADER_TREE"
    BLENDER_TEXTURE = "OCTANE_TEXTURE_TREE"


# Node Tree ID Names
class OctaneNodeTreeIDName:
    GENERAL = "octane_general_nodes"
    MATERIAL = "octane_material_nodes"
    TEXTURE = "octane_texture_nodes"
    WORLD = "octane_world_nodes"
    LIGHT = "octane_light_nodes"
    CAMERA_IMAGER = "octane_camera_imager_nodes"
    COMPOSITE = "octane_composite_nodes"
    KERNEL = "octane_kernel_nodes"
    RENDER_AOV = "octane_render_aov_nodes"
    BLENDER_SHADER = "ShaderNodeTree"
    BLENDER_TEXTURE = "TextureNodeTree"


# Octane Preset Node Tree Names
class OctanePresetNodeTreeNames:
    COMPOSITE = "Octane Compositor"
    KERNEL = "Octane Kernel"
    RENDER_AOV = "Octane AOVs"


# Octane Preset Node Names
class OctanePresetNodeNames:
    ENVIRONMENT = "OCTANE_BLENDER_ENVIRONMENT"
    VISIBLE_ENVIRONMENT = "OCTANE_BLENDER_VISIBLE_ENVIRONMENT"
    COMPOSITE = "OCTANE_BLENDER_RENDER_AOV_NODE"
    RENDER_AOV = "OCTANE_BLENDER_RENDER_AOV_NODE"
    CAMERA = "OCTANE_CAMERA"
    IMAGER = "OCTANE_IMAGER"
    POST_PROCESSING = "OCTANE_POST_PROCESSING"
    POST_VOLUME = "OCTANE_POST_VOLUME"
    ANIMATION_SETTINGS = "OCTANE_ANIMATION_SETTINGS"
    RENDER_LAYER = "OCTANE_RENDER_LAYER"
    RENDER_PASSES = "OCTANE_RENDER_PASSES"
    OCTANE_BLENDER_RENDER_PASSES = "OCTANE_BLENDER_RENDER_PASSES"
    CAMERA_POSITION = "OCTANE_CAMERA_POSITION"
    CAMERA_TARGET = "OCTANE_CAMERA_TARGET"
    CAMERA_UP = "OCTANE_CAMERA_UP"
    GEOMETRY_GROUP = "OCTANE_GEOMETRY_GROUP"


# Octane OutputNode Socket Names
class OctaneOutputNodeSocketNames:
    KERNEL = "Kernel"
    TEXTURE = "Texture"
    SURFACE = "Surface"
    VOLUME = "Volume"
    GEOMETRY = "Geometry"
    LIGHT = "Light"
    ENVIRONMENT = "Environment"
    VISIBLE_ENVIRONMENT = "Visible Environment"
    LEGACY_GEOMETRY = "Octane Geometry"
    LEGACY_ENVIRONMENT = "Octane Environment"
    LEGACY_VISIBLE_ENVIRONMENT = "Octane VisibleEnvironment"
    COMPOSITE = "AOVOutputGroup"
    RENDER_AOV = "RenderAOVs"


class ObjectLayerMode:
    NO_OBJECTLAYER = 0
    WITH_OBJECTLAYER = 1
    WITH_OBJECTLAYER_FOR_ORBX_PROXY = 2


class UtilsFunctionType:
    TEST = 0
    SHOW_NODEGRAPH = 1
    SHOW_NETWORK_PREFERENCE = 2
    STOP_RENDERING = 3
    SHOW_LOG = 4
    SHOW_DEVICE_SETTINGS = 5
    FETCH_LIVEDB = 6
    SHOW_ACTIVATION = 7
    SAVE_LIVEDB = 8
    SHOW_VIEWPORT = 9
    UPDATE_RENDER_SETTINGS = 10
    UPDATE_OCIO_SETTINGS = 11
    EXPORT_RENDER_PASS = 12
    CRYPTOMATTE_PICKER = 13
    FETCH_IMAGE_INFO = 100
    FETCH_VDB_INFO = 101
    FETCH_OSL_INFO = 102
    FETCH_STATISTICS = 103
    FETCH_NODE_INFO = 104
    FETCH_VERSION_INFO = 105
    EXPORT_OFFSET = 200
    EXPORT_ALEMBIC_START = 201
    EXPORT_ALEMBIC_END = 202
    EXPORT_ALEMBIC_WRITE_FRAME = 203
    EXPORT_ORBX_START = 204
    EXPORT_ORBX_END = 205
    EXPORT_ORBX_WRITE_FRAME = 206
    RENDER_START = 300
    RENDER_STOP = 301
    RENDER_PAUSE = 302
    OCTANE_ORBX_PROXY = 400
    OCTANE_NODE_PROXY = 401
    OCTANE_MATERIALX_FETCHER = 500
    OCTANE_RESOURCE_CACHE_RESET = 600
    UTILS_FUNC_GIZMOS_PICK_WHITEBALANCE = 1000
    TOGGLE_RECORD = 10000
    PLAY_RECORD = 10001


# Pin Id
P_INVALID = -1
P_UNKNOWN = 0

# Attribute ID
A_UNKNOWN = 0

# OSL Compilation Results
COMPILE_NONE = 0
COMPILE_SUCCESS = 1
COMPILE_FAILED = 2
COMPILE_FORCE = 3

# Socket colors
SOCKET_COLOR_OCIO_COLOR_SPACE = (1, 0, 1, 1)

# Render pass ID
RENDER_PASS_INVALID = -1

# Link Utility Menu
LINK_UTILITY_REMOVE = "LINK_UTILITY_REMOVE_OPERATOR"
LINK_UTILITY_DISCONNECT = "LINK_UTILITY_DISCONNECT_OPERATOR"
LINK_UTILITY_DEFAULT = "LINK_UTILITY_DEFAULT_OPERATOR"
LINK_UTILITY_REMOVE_INDEX = 10002
LINK_UTILITY_DISCONNECT_INDEX = 10001
LINK_UTILITY_DEFAULT_INDEX = 10000
LINK_UTILITY_MENU = (
    ("", "Link", ""),
    (LINK_UTILITY_REMOVE, "Remove", "Remove nodes connected to the input", LINK_UTILITY_REMOVE_INDEX),
    (LINK_UTILITY_DISCONNECT, "Disconnect", "Disconnect nodes connected to the input", LINK_UTILITY_DISCONNECT_INDEX),
    (LINK_UTILITY_DEFAULT, "Default", "Same effect as the 'Disconnect'", LINK_UTILITY_DEFAULT_INDEX),
)
