ENGINE_NAME = "octane"
ADDON_NAME = "octane"

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


# Octane NodeTree
class OctaneNodeTree:
    COMPOSITE = "OCTANE_COMPOSITE_TREE"
    RENDER_AOV = "OCTANE_RENDER_AOV_TREE"


# Node Tree ID Names
class OctaneNodeTreeIDName:
    MATERIAL = "octane_material_nodes"
    TEXTURE = "octane_texture_nodes"
    COMPOSITE = "octane_composite_nodes"
    RENDER_AOV = "octane_render_aov_nodes"


# Node type
NT_UNKNOWN = 0

# Pin Id
P_UNKNOWN = 0

# Attribute Id
A_UNKNOWN = 0


# Socket colors
SOCKET_COLOR_DEFAULT = (1, 1, 1, 1)
SOCKET_COLOR_OCIO_COLOR_SPACE = (1, 0, 1, 1)
