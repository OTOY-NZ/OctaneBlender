ENGINE_NAME = "octane"
ADDON_NAME = "octane"

DERIVED_NODE_NAMES = "DERIVED_NODE_NAMES"
DERIVED_NODE_TYPES = "DERIVED_NODE_TYPES"
DERIVED_NODE_SEPARATOR = "###DERIVED_NODE_SEPARATOR###"
OBJECT_INDEX_SEPARATOR = "###OBJECT_INDEX###"

OCTANE_HELPER_NODE_GROUP = "[OCTANE_HELPER_NODE_GROUP]"


# Render Session type
class SessionType:
    UNKNOWN = 0
    VIEWPORT = 1
    FINAL_RENDER = 2
    PREVIEW = 3
    EXPORT = 4


# Blender Scene Data type
class SceneDataType:
    MESH = 0
    SUBDIVISION_MESH = 1
    OBJECT = 2


# Socket type
class SocketType:
    ST_UNKNOWN = 0
    ST_BOOL    = 1
    ST_ENUM    = 2
    ST_INT     = 3
    ST_INT2    = 4
    ST_INT3    = 5
    ST_FLOAT   = 6
    ST_FLOAT2  = 7
    ST_FLOAT3  = 8
    ST_RGBA    = 9
    ST_STRING  = 10
    ST_LINK    = 11
    ST_OUTPUT  = 100
    ST_GROUP_TITLE = 1000


# Pin type
class PinType:
    PT_UNKNOWN             = 0
    PT_ANIMATION_SETTINGS  = 27
    PT_BIT_MASK            = 31
    PT_BOOL                = 1
    PT_CAMERA              = 8
    PT_COMPOSITE_AOV_LAYER = 40
    PT_DISPLACEMENT        = 22
    PT_EMISSION            = 6
    PT_ENUM                = 16
    PT_ENVIRONMENT         = 9
    PT_FILM_SETTINGS       = 15
    PT_FLOAT               = 2
    PT_GEOMETRY            = 12
    PT_IMAGER              = 10
    PT_INT                 = 3
    PT_KERNEL              = 11
    PT_LUT                 = 28
    PT_MATERIAL            = 7
    PT_MATERIAL_LAYER      = 33
    PT_MEDIUM              = 13
    PT_OBJECTLAYER         = 17
    PT_OCIO_COLOR_SPACE    = 36
    PT_OCIO_LOOK           = 35
    PT_OCIO_VIEW           = 34
    PT_OUTPUT_AOV          = 38
    PT_OUTPUT_AOV_GROUP    = 37
    PT_PHASEFUNCTION       = 14
    PT_POSTPROCESSING      = 18
    PT_PROJECTION          = 21
    PT_RENDER_JOB          = 29
    PT_RENDER_LAYER        = 25
    PT_RENDER_PASSES       = 24
    PT_RENDERTARGET        = 19
    PT_ROUND_EDGES         = 32
    PT_STRING              = 23
    PT_TEX_COMPOSITE_LAYER = 39
    PT_TEXTURE             = 5
    PT_TOON_RAMP           = 30
    PT_TRANSFORM           = 4
    PT_VOLUME_RAMP         = 26
    PT_WORK_PANE           = 20
    PT_BLENDER_OUTPUT      = -10000
    PT_BLENDER_INPUT       = -10001
    PT_BLENDER_VALUES      = -10002
    PT_BLENDER_UTILITY     = -20000


# Attribute type
class AttributeType:
    AT_UNKNOWN   = 0
    AT_BOOL      = 1
    AT_INT       = 2
    AT_INT2      = 3
    AT_INT3      = 4
    AT_INT4      = 5
    AT_LONG      = 14
    AT_LONG2     = 15
    AT_FLOAT     = 6
    AT_FLOAT2    = 7
    AT_FLOAT3    = 8
    AT_FLOAT4    = 9
    AT_STRING    = 10
    AT_FILENAME  = 11
    AT_BYTE      = 12
    AT_MATRIX    = 13   


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
    RenderAOVs = (1.00, 1.00, 1.00, 0.70)
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
    AOVOutputGroup = (1.00, 1.00, 1.00, 0.70)
    AOVOutput = (1.00, 1.00, 1.00, 0.70)
    CompositeTextureLayer = (1.00, 1.00, 1.00, 0.70)
    CompositeAOVLayer = (1.00, 1.00, 1.00, 0.70)


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
    KERNEL = "OCTANE_KERNEL"
    CAMERA = "OCTANE_CAMERA"
    IMAGER = "OCTANE_IMAGER"
    POST_PROCESSING = "OCTANE_POST_PROCESSING"


# Octane Preset Node Names
class OctanePresetNodeNames:
    ENVIRONMENT = "OCTANE_BLENDER_ENVIRONMENT"
    VISIBLE_ENVIRONMENT = "OCTANE_BLENDER_VISIBLE_ENVIRONMENT"
    COMPOSITE = "OCTANE_BLENDER_RENDER_AOV_NODE"
    RENDER_AOV = "OCTANE_BLENDER_RENDER_AOV_NODE"


# Octane OutputNode Socket Names
class OctaneOutputNodeSocketNames:
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


# Node type
class NodeType:
    NT_UNKNOWN = 0
    NT_CAM_THINLENS = 13
    NT_IMAGER_CAMERA = 15
    NT_RENDERTARGET = 56    
    NT_POSTPROCESSING = 61
    NT_CAM_PANORAMIC = 62
    NT_CAM_BAKING = 94
    NT_CAM_OSL = 126
    NT_CAM_OSL_BAKING = 128
    NT_CAM_UNIVERSAL = 157
    NT_BLENDER_NODE_OFFSET = -100000
    NT_BLENDER_NODE_OCTANE_PROXY = -100001
    NT_BLENDER_NODE_OBJECT_DATA = -100002
    NT_BLENDER_NODE_CAMERA_DATA = -100003
    NT_BLENDER_NODE_IMAGE_INFO = -100004
    NT_BLENDER_NODE_GET_RENDER_RESULT = -100005
    NT_BLENDER_NODE_START_RENDER = -100006
    NT_BLENDER_NODE_STOP_RENDER = -100007
    NT_BLENDER_NODE_RESET_RENDER = -100008
    NT_BLENDER_NODE_SCATTER = -100009
    NT_BLENDER_NODE_MESH = -100010

# Pin Id
P_INVALID = -1
P_UNKNOWN = 0

# Attribute Id
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