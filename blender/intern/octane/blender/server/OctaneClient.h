//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OTOY Inc.
// The inline client-side code to access the OctaneEngine over network.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef __OCTANECLIENT_H__
#define __OCTANECLIENT_H__

#ifndef OCTANE_SERVER_MAJOR_VERSION
#   define OCTANE_SERVER_MAJOR_VERSION 11
#endif
#ifndef OCTANE_SERVER_MINOR_VERSION
#   define OCTANE_SERVER_MINOR_VERSION 24
#endif
#define OCTANE_SERVER_VERSION_NUMBER (((OCTANE_SERVER_MAJOR_VERSION & 0x0000FFFF) << 16) | (OCTANE_SERVER_MINOR_VERSION & 0x0000FFFF))

#define SEND_CHUNK_SIZE 67108864


#if !defined(__APPLE__)
#  undef htonl
#  undef ntohl
#else
#   include <errno.h>
#endif

#ifndef _WIN32
#  include <unistd.h>
#  include <sys/types.h>
#  include <sys/stat.h>
#  include <sys/socket.h>
#  include <netinet/ip.h>
#  include <netdb.h>
#  if defined(__APPLE__)
#    include <arpa/inet.h>
#  endif
#  include <pthread.h>
#  include <math.h>
#  include <string.h>

#  include <stdio.h>
#  include <fcntl.h>
#  include <stdlib.h>
#else
#  undef _WINSOCKAPI_ //Needs to be difined project-wide to prevent the inclusion of winsock.h from windows.h
#  include <winsock2.h>
#  include <windows.h>
#  include <ws2tcpip.h>

#  include <wchar.h>
#  include <io.h>
#endif

#ifdef __GNUC__
    #include <stdint.h>
#endif

#undef max
#undef min

#pragma push_macro("htonl")
#define htonl 1
#pragma push_macro("ntohl")
#define ntohl 1

#include <sys/stat.h>

#include <stdlib.h>
#include <string>
#include <vector>

#pragma pop_macro("htonl")
#pragma pop_macro("ntohl")

#ifndef MAX_PATH
#   define MAX_PATH 512
#endif


namespace Octane {

#define PIN_TYPE(_name, _enum)   _name = _enum,
enum NodePinType {
    PIN_TYPE(PT_UNKNOWN           , 0)

    PIN_TYPE(PT_ANIMATION_SETTINGS, 27)
    PIN_TYPE(PT_BOOL              , 1)
    PIN_TYPE(PT_CAMERA            , 8)
    PIN_TYPE(PT_DISPLACEMENT      , 22)
    PIN_TYPE(PT_EMISSION          , 6)
    PIN_TYPE(PT_ENUM              , 16)
    PIN_TYPE(PT_ENVIRONMENT       , 9)
    PIN_TYPE(PT_FILM_SETTINGS     , 15)
    PIN_TYPE(PT_FLOAT             , 2)
    PIN_TYPE(PT_GEOMETRY          , 12)
    PIN_TYPE(PT_IMAGER            , 10)
    PIN_TYPE(PT_INT               , 3)
    PIN_TYPE(PT_KERNEL            , 11)
    PIN_TYPE(PT_MATERIAL          , 7)
    PIN_TYPE(PT_MEDIUM            , 13)
    PIN_TYPE(PT_OBJECTLAYER       , 17)
    PIN_TYPE(PT_PHASEFUNCTION     , 14)
    PIN_TYPE(PT_POSTPROCESSING    , 18)
    PIN_TYPE(PT_PROJECTION        , 21)
    PIN_TYPE(PT_RENDER_LAYER      , 25)
    PIN_TYPE(PT_RENDER_PASSES     , 24)
    PIN_TYPE(PT_RENDERTARGET      , 19)
    PIN_TYPE(PT_STRING            , 23)
    PIN_TYPE(PT_TEXTURE           , 5)
    PIN_TYPE(PT_TRANSFORM         , 4)
    PIN_TYPE(PT_VOLUME_RAMP       , 26)
    PIN_TYPE(PT_WORK_PANE         , 20)
};

#define NODE_TYPE(_name, _enum)   _name = _enum,
enum NodeType {
    NODE_TYPE(NT_UNKNOWN                    ,   0)

    NODE_TYPE(NT_ANIMATION_SETTINGS         ,  99)
    NODE_TYPE(NT_ANNOTATION                 ,  68)
    NODE_TYPE(NT_BOOL                       ,  11)
    NODE_TYPE(NT_CAM_BAKING                 ,  94)
    NODE_TYPE(NT_CAM_CUSTOM                 ,  97)
    NODE_TYPE(NT_CAM_PANORAMIC              ,  62)
    NODE_TYPE(NT_CAM_THINLENS               ,  13)
    NODE_TYPE(NT_DIRECTORY                  , 101)
    NODE_TYPE(NT_DISPLACEMENT               ,  80)
    NODE_TYPE(NT_EMIS_BLACKBODY             ,  53)
    NODE_TYPE(NT_EMIS_TEXTURE               ,  54)
    NODE_TYPE(NT_ENUM                       ,  57)
    NODE_TYPE(NT_ENV_DAYLIGHT               ,  14)
    NODE_TYPE(NT_ENV_TEXTURE                ,  37)
    NODE_TYPE(NT_FILE                       ,  88)
    NODE_TYPE(NT_FILM_SETTINGS              , 100)
    NODE_TYPE(NT_FLOAT                      ,   6)
    NODE_TYPE(NT_GEO_GROUP                  ,   3)
    NODE_TYPE(NT_GEO_MESH                   ,   1)
    NODE_TYPE(NT_GEO_VOLUME                 ,  91)
    NODE_TYPE(NT_GEO_PLACEMENT              ,   4)
    NODE_TYPE(NT_GEO_SCATTER                ,   5)
    NODE_TYPE(NT_IMAGER_CAMERA              ,  15)
    NODE_TYPE(NT_IMPORT_ALEMBIC_PREFS       ,  82)
    NODE_TYPE(NT_IMPORT_OBJ_PREFS           ,  83)
    NODE_TYPE(NT_IMPORT_VDB_PREFS           ,  93)
    NODE_TYPE(NT_IMAGE_RESOLUTION           ,  12)
    NODE_TYPE(NT_INT                        ,   9)
    NODE_TYPE(NT_KERN_DIRECTLIGHTING        ,  24)
    NODE_TYPE(NT_KERN_INFO                  ,  26)
    NODE_TYPE(NT_KERN_MATPREVIEW            ,  69)
    NODE_TYPE(NT_KERN_PATHTRACING           ,  25)
    NODE_TYPE(NT_KERN_PMC                   ,  23)
    NODE_TYPE(NT_LOCAL_APP_PREFS            ,  55)
    NODE_TYPE(NT_MAT_DIFFUSE                ,  17)
    NODE_TYPE(NT_MAT_GLOSSY                 ,  16)
    NODE_TYPE(NT_MAT_MAP                    ,   2)
    NODE_TYPE(NT_MAT_MIX                    ,  19)
    NODE_TYPE(NT_MAT_PORTAL                 ,  20)
    NODE_TYPE(NT_MAT_SPECULAR               ,  18)
    NODE_TYPE(NT_MED_ABSORPTION             ,  58)
    NODE_TYPE(NT_MED_SCATTERING             ,  59)
    NODE_TYPE(NT_MED_VOLUME                 ,  98)
    NODE_TYPE(NT_OBJECTLAYER                ,  65)
    NODE_TYPE(NT_OBJECTLAYER_MAP            ,  64)
    NODE_TYPE(NT_ORC_VERSION                ,  92)
    NODE_TYPE(NT_PHASE_SCHLICK              ,  60)
    NODE_TYPE(NT_POSTPROCESSING             ,  61)
    NODE_TYPE(NT_PROJ_BOX                   ,  79)
    NODE_TYPE(NT_PROJ_CYLINDRICAL           ,  74)
    NODE_TYPE(NT_PROJ_LINEAR                ,  75)
    NODE_TYPE(NT_PROJ_PERSPECTIVE           ,  76)
    NODE_TYPE(NT_PROJ_SPHERICAL             ,  77)
    NODE_TYPE(NT_PROJ_UVW                   ,  78)
    NODE_TYPE(NT_PROJECT_SETTINGS           ,  70)
    NODE_TYPE(NT_RENDER_LAYER               ,  90)
    NODE_TYPE(NT_RENDER_PASSES              ,  86)
    NODE_TYPE(NT_RENDERTARGET               ,  56)
    NODE_TYPE(NT_SCRIPT_INPUT               ,  85)
    NODE_TYPE(NT_SPLIT_PANE                 ,  72)
    NODE_TYPE(NT_STRING                     ,  84)
    NODE_TYPE(NT_SUN_DIRECTION              ,  30)
    NODE_TYPE(NT_TEX_ALPHAIMAGE             ,  35)
    NODE_TYPE(NT_TEX_CHECKS                 ,  45)
    NODE_TYPE(NT_TEX_CLAMP                  ,  41)
    NODE_TYPE(NT_TEX_COLORCORRECTION        ,  51)
    NODE_TYPE(NT_TEX_COSINEMIX              ,  40)
    NODE_TYPE(NT_TEX_DIRT                   ,  63)
    NODE_TYPE(NT_TEX_FALLOFF                ,  50)
    NODE_TYPE(NT_TEX_FLOAT                  ,  31)
    NODE_TYPE(NT_TEX_FLOATIMAGE             ,  36)
    NODE_TYPE(NT_TEX_GAUSSIANSPECTRUM       ,  32)
    NODE_TYPE(NT_TEX_GRADIENT               ,  49)
    NODE_TYPE(NT_TEX_IMAGE                  ,  34)
    NODE_TYPE(NT_TEX_INVERT                 ,  46)
    NODE_TYPE(NT_TEX_MARBLE                 ,  47)
    NODE_TYPE(NT_TEX_MIX                    ,  38)
    NODE_TYPE(NT_TEX_MULTIPLY               ,  39)
    NODE_TYPE(NT_TEX_NOISE                  ,  87)
    NODE_TYPE(NT_TEX_RANDOMCOLOR            ,  81)
    NODE_TYPE(NT_TEX_RGB                    ,  33)
    NODE_TYPE(NT_TEX_RGFRACTAL              ,  48)
    NODE_TYPE(NT_TEX_SAWWAVE                ,  42)
    NODE_TYPE(NT_TEX_SINEWAVE               ,  44)
    NODE_TYPE(NT_TEX_SIDE                   ,  89)
    NODE_TYPE(NT_TEX_TRIANGLEWAVE           ,  43)
    NODE_TYPE(NT_TEX_TURBULENCE             ,  22)
    NODE_TYPE(NT_TEX_W                      , 104)
    NODE_TYPE(NT_TRANSFORM_2D               ,  66)
    NODE_TYPE(NT_TRANSFORM_3D               ,  27)
    NODE_TYPE(NT_TRANSFORM_ROTATION         ,  29)
    NODE_TYPE(NT_TRANSFORM_SCALE            ,  28)
    NODE_TYPE(NT_TRANSFORM_VALUE            ,  67)
    NODE_TYPE(NT_VOLUME_RAMP                ,  95)
    NODE_TYPE(NT_WORK_PANE                  ,  73)

    // The input linker node types.
    NODE_TYPE(NT_IN_OFFSET                  , 20000)
    NODE_TYPE(NT_IN_ANIMATION_SETTINGS      , NT_IN_OFFSET + PT_ANIMATION_SETTINGS)
    NODE_TYPE(NT_IN_BOOL                    , NT_IN_OFFSET + PT_BOOL)
    NODE_TYPE(NT_IN_CAMERA                  , NT_IN_OFFSET + PT_CAMERA)
    NODE_TYPE(NT_IN_DISPLACEMENT            , NT_IN_OFFSET + PT_DISPLACEMENT)
    NODE_TYPE(NT_IN_EMISSION                , NT_IN_OFFSET + PT_EMISSION)
    NODE_TYPE(NT_IN_ENUM                    , NT_IN_OFFSET + PT_ENUM)
    NODE_TYPE(NT_IN_ENVIRONMENT             , NT_IN_OFFSET + PT_ENVIRONMENT)
    NODE_TYPE(NT_IN_FILM_SETTINGS           , NT_IN_OFFSET + PT_FILM_SETTINGS)
    NODE_TYPE(NT_IN_FLOAT                   , NT_IN_OFFSET + PT_FLOAT)
    NODE_TYPE(NT_IN_GEOMETRY                , NT_IN_OFFSET + PT_GEOMETRY)
    NODE_TYPE(NT_IN_IMAGER                  , NT_IN_OFFSET + PT_IMAGER)
    NODE_TYPE(NT_IN_INT                     , NT_IN_OFFSET + PT_INT)
    NODE_TYPE(NT_IN_KERNEL                  , NT_IN_OFFSET + PT_KERNEL)
    NODE_TYPE(NT_IN_MATERIAL                , NT_IN_OFFSET + PT_MATERIAL)
    NODE_TYPE(NT_IN_MEDIUM                  , NT_IN_OFFSET + PT_MEDIUM)
    NODE_TYPE(NT_IN_OBJECTLAYER             , NT_IN_OFFSET + PT_OBJECTLAYER)
    NODE_TYPE(NT_IN_PHASEFUNCTION           , NT_IN_OFFSET + PT_PHASEFUNCTION)
    NODE_TYPE(NT_IN_POSTPROCESSING          , NT_IN_OFFSET + PT_POSTPROCESSING)
    NODE_TYPE(NT_IN_PROJECTION              , NT_IN_OFFSET + PT_PROJECTION)
    NODE_TYPE(NT_IN_RENDER_LAYER            , NT_IN_OFFSET + PT_RENDER_LAYER)
    NODE_TYPE(NT_IN_RENDER_PASSES           , NT_IN_OFFSET + PT_RENDER_PASSES)
    NODE_TYPE(NT_IN_RENDERTARGET            , NT_IN_OFFSET + PT_RENDERTARGET)
    NODE_TYPE(NT_IN_STRING                  , NT_IN_OFFSET + PT_STRING)
    NODE_TYPE(NT_IN_TEXTURE                 , NT_IN_OFFSET + PT_TEXTURE)
    NODE_TYPE(NT_IN_TRANSFORM               , NT_IN_OFFSET + PT_TRANSFORM)
    NODE_TYPE(NT_IN_VOLUME_RAMP             , NT_IN_OFFSET + PT_VOLUME_RAMP)

    // The output linker node types.
    NODE_TYPE(NT_OUT_OFFSET                 , 30000)
    NODE_TYPE(NT_OUT_ANIMATION_SETTINGS     , NT_OUT_OFFSET + PT_ANIMATION_SETTINGS)
    NODE_TYPE(NT_OUT_BOOL                   , NT_OUT_OFFSET + PT_BOOL)
    NODE_TYPE(NT_OUT_CAMERA                 , NT_OUT_OFFSET + PT_CAMERA)
    NODE_TYPE(NT_OUT_DISPLACEMENT           , NT_OUT_OFFSET + PT_DISPLACEMENT)
    NODE_TYPE(NT_OUT_EMISSION               , NT_OUT_OFFSET + PT_EMISSION)
    NODE_TYPE(NT_OUT_ENUM                   , NT_OUT_OFFSET + PT_ENUM)
    NODE_TYPE(NT_OUT_ENVIRONMENT            , NT_OUT_OFFSET + PT_ENVIRONMENT)
    NODE_TYPE(NT_OUT_FILM_SETTINGS          , NT_OUT_OFFSET + PT_FILM_SETTINGS)
    NODE_TYPE(NT_OUT_FLOAT                  , NT_OUT_OFFSET + PT_FLOAT)
    NODE_TYPE(NT_OUT_GEOMETRY               , NT_OUT_OFFSET + PT_GEOMETRY)
    NODE_TYPE(NT_OUT_IMAGER                 , NT_OUT_OFFSET + PT_IMAGER)
    NODE_TYPE(NT_OUT_INT                    , NT_OUT_OFFSET + PT_INT)
    NODE_TYPE(NT_OUT_KERNEL                 , NT_OUT_OFFSET + PT_KERNEL)
    NODE_TYPE(NT_OUT_MATERIAL               , NT_OUT_OFFSET + PT_MATERIAL)
    NODE_TYPE(NT_OUT_MEDIUM                 , NT_OUT_OFFSET + PT_MEDIUM)
    NODE_TYPE(NT_OUT_OBJECTLAYER            , NT_OUT_OFFSET + PT_OBJECTLAYER)
    NODE_TYPE(NT_OUT_PHASEFUNCTION          , NT_OUT_OFFSET + PT_PHASEFUNCTION)
    NODE_TYPE(NT_OUT_POSTPROCESSING         , NT_OUT_OFFSET + PT_POSTPROCESSING)
    NODE_TYPE(NT_OUT_PROJECTION             , NT_OUT_OFFSET + PT_PROJECTION)
    NODE_TYPE(NT_OUT_RENDER_LAYER           , NT_OUT_OFFSET + PT_RENDER_LAYER)
    NODE_TYPE(NT_OUT_RENDER_PASSES          , NT_OUT_OFFSET + PT_RENDER_PASSES)
    NODE_TYPE(NT_OUT_RENDERTARGET           , NT_OUT_OFFSET + PT_RENDERTARGET)
    NODE_TYPE(NT_OUT_STRING                 , NT_OUT_OFFSET + PT_STRING)
    NODE_TYPE(NT_OUT_TEXTURE                , NT_OUT_OFFSET + PT_TEXTURE)
    NODE_TYPE(NT_OUT_TRANSFORM              , NT_OUT_OFFSET + PT_TRANSFORM)
    NODE_TYPE(NT_OUT_VOLUME_RAMP            , NT_OUT_OFFSET + PT_VOLUME_RAMP)

    
    //--- deprecated ---

    NODE_TYPE(_NT_FLOAT2                    , 7)      // replaced by NT_FLOAT
    NODE_TYPE(_NT_FLOAT3                    , 8)      // replaced by NT_FLOAT
    NODE_TYPE(_NT_INT2                      , 10)     // replaced by NT_INT
    NODE_TYPE(_NT_CAMERARESPONSE            , 21)     // replaced by NT_ENUM
    NODE_TYPE(_NT_REMOTE_APP_PREFS          , 71)     // not used anymore
};

enum PanoramicCameraMode {
    SPHERICAL_CAMERA      = 0,
    CYLINDRICAL_CAMERA    = 1,
    CUBE_MAPPED_CAMERA    = 2,
    CUBE_MAPPED_CAMERA_PX = 3,
    CUBE_MAPPED_CAMERA_MX = 4,
    CUBE_MAPPED_CAMERA_PY = 5,
    CUBE_MAPPED_CAMERA_MY = 6,
    CUBE_MAPPED_CAMERA_PZ = 7,
    CUBE_MAPPED_CAMERA_MZ = 8,
};

enum StereoMode {
    /// The view of the left and right eye are shifted to keep the target position in center.
    STEREO_MODE_OFF_AXIS = 1,
    /// The left and right eyes have the same orientation.
    STEREO_MODE_PARALLEL = 2,
};

enum StereoOutput {
    /// Stereo output is disabled.
    STEREO_OUTPUT_DISABLED     = 0,
    /// Stereo rendering for the left eye.
    STEREO_OUTPUT_LEFT_EYE     = 1,
    /// Stereo rendering for the right eye.
    STEREO_OUTPUT_RIGHT_EYE    = 2,
    /// Stereo rendering for both eyes (side-by-side, half horizontal resolution for each eye).
    STEREO_OUTPUT_SIDE_BY_SIDE = 3,
    /// Anaglyphic stereo rendering.
    STEREO_OUTPUT_ANAGLYPHIC   = 4,
    /// Stereo rendering for both eyes (top-bottom, half vertical resolution for each eye).
    STEREO_OUTPUT_OVER_UNDER   = 5,
};

enum ResponseCurveId {
    // Agfa
    CURVE_AGFACOLOR_FUTURA_100CD      = 99,
    CURVE_AGFACOLOR_FUTURA_200CD      = 100,
    CURVE_AGFACOLOR_FUTURA_400CD      = 101,
    CURVE_AGFACOLOR_FUTURA_II_100CD   = 102,
    CURVE_AGFACOLOR_FUTURA_II_200CD   = 103,
    CURVE_AGFACOLOR_FUTURA_II_400CD   = 104,
    CURVE_AGFACOLOR_HDC_100_PLUSCD    = 105,
    CURVE_AGFACOLOR_HDC_200_PLUSCD    = 106,
    CURVE_AGFACOLOR_HDC_400_PLUSCD    = 107,
    CURVE_AGFACOLOR_OPTIMA_II_100CD   = 108,
    CURVE_AGFACOLOR_OPTIMA_II_200CD   = 109,
    CURVE_AGFACOLOR_ULTRA_050CD       = 110,
    CURVE_AGFACOLOR_VISTA_100CD       = 111,
    CURVE_AGFACOLOR_VISTA_200CD       = 112,
    CURVE_AGFACOLOR_VISTA_400CD       = 113,
    CURVE_AGFACOLOR_VISTA_800CD       = 114,
    CURVE_AGFACHROME_CT_PRECISA_100CD = 115,
    CURVE_AGFACHROME_CT_PRECISA_200CD = 116,
    CURVE_AGFACHROME_RSX2_050CD       = 117,
    CURVE_AGFACHROME_RSX2_100CD       = 118,
    CURVE_AGFACHROME_RSX2_200CD       = 119,
    // Eastman-Kodak group
    CURVE_ADVANTIX_100CD              = 201,
    CURVE_ADVANTIX_200CD              = 202,
    CURVE_ADVANTIX_400CD              = 203,
    CURVE_GOLD_100CD                  = 204,
    CURVE_GOLD_200CD                  = 205,
    CURVE_MAX_ZOOM_800CD              = 206,
    CURVE_PORTRA_100TCD               = 207,
    CURVE_PORTRA_160NCCD              = 208,
    CURVE_PORTRA_160VCCD              = 209,
    CURVE_PORTRA_800CD                = 210,
    CURVE_PORTRA_400VCCD              = 211,
    CURVE_PORTRA_400NCCD              = 212,
    CURVE_EKTACHROME_100_PLUSCD       = 213,
    CURVE_EKTACHROME_320TCD           = 214,
    CURVE_EKTACHROME_400XCD           = 215,
    CURVE_EKTACHROME_64CD             = 216,
    CURVE_EKTACHROME_64TCD            = 217,
    CURVE_EKTACHROME_E100SCD          = 218,
    CURVE_EKTACHROME_100CD            = 219,
    CURVE_KODACHROME_200CD            = 220,
    CURVE_KODACHROME_25               = 221,
    CURVE_KODACHROME_64CD             = 222,
    // Misc group
    CURVE_F125CD                      = 301,
    CURVE_F250CD                      = 302,
    CURVE_F400CD                      = 303,
    CURVE_FCICD                       = 304,
    CURVE_DSCS315_1                   = 305,
    CURVE_DSCS315_2                   = 306,
    CURVE_DSCS315_3                   = 307,
    CURVE_DSCS315_4                   = 308,
    CURVE_DSCS315_5                   = 309,
    CURVE_DSCS315_6                   = 310,
    CURVE_FP2900Z                     = 311,
    // Linear/off
    CURVE_LINEAR                      = 400
};

enum InfoChannelType {
    /// Geometric normals
    IC_TYPE_GEOMETRIC_NORMAL    = 0,
    /// Shading normals used after interpolation and correction for too grazing angles
    IC_TYPE_SHADING_NORMAL      = 1,
    /// The position of the first intersection point
    IC_TYPE_POSITION            = 2,
    /// Z-depth of the first intersection point
    IC_TYPE_Z_DEPTH             = 3,
    /// Material node ID
    IC_TYPE_MATERIAL_ID         = 4,
    /// Texture coordinates
    IC_TYPE_UV_COORD            = 5,
    /// First tangent vector
    IC_TYPE_TANGENT_U           = 6,
    /// Wireframe display
    IC_TYPE_WIREFRAME           = 7,
    /// Interpolated vertex normals
    IC_TYPE_VERTEX_NORMAL       = 8,
    /// Object layer node ID
    IC_TYPE_OBJECT_ID           = 9,
    /// Ambient occlussion 
    IC_TYPE_AMBIENT_OCCLUSION   = 10,
    /// 2D Motion vector 
    IC_TYPE_MOTION_VECTOR       = 11,
    /// Render layer ID
    IC_TYPE_RENDER_LAYER_ID     = 12,
    /// Render layer mask
    IC_TYPE_RENDER_LAYER_MASK   = 13,
    /// Light pass ID
    IC_TYPE_LIGHT_PASS_ID       = 14,
    /// Local normal in tangent space
    IC_TYPE_TANGENT_NORMAL      = 15,
    /// Opacity
    IC_TYPE_OPACITY             = 16,
    /// Baking group ID
    IC_TYPE_BAKING_GROUP_ID     = 17,
    /// Roughness
    IC_TYPE_ROUGHNESS           = 18,
    /// Index of Refraction
    IC_TYPE_IOR                 = 19,
    /// Diffuse filter color
    IC_TYPE_DIFFUSE_FILTER      = 20,
    /// Reflection filter color
    IC_TYPE_REFLECTION_FILTER   = 21,
    /// Refraction filter color
    IC_TYPE_REFRACTION_FILTER   = 22,
    /// Transmission filter color
    IC_TYPE_TRANSMISSION_FILTER = 23,
    /// Object layer color
    IC_TYPE_OBJECT_LAYER_COLOR  = 24,
};

enum RenderPassId {
    /// normal render passes
    RENDER_PASS_BEAUTY              = 0,
    RENDER_PASS_EMIT                = 1,
    RENDER_PASS_ENVIRONMENT         = 2,
    RENDER_PASS_DIFFUSE             = 3,
    RENDER_PASS_DIFFUSE_DIRECT      = 4,
    RENDER_PASS_DIFFUSE_INDIRECT    = 5,
    RENDER_PASS_DIFFUSE_FILTER      = 6,
    RENDER_PASS_REFLECTION          = 7,
    RENDER_PASS_REFLECTION_DIRECT   = 8,
    RENDER_PASS_REFLECTION_INDIRECT = 9,
    RENDER_PASS_REFLECTION_FILTER   = 10,
    RENDER_PASS_REFRACTION          = 11,
    RENDER_PASS_REFRACTION_FILTER   = 12,
    RENDER_PASS_TRANSMISSION        = 13,
    RENDER_PASS_TRANSMISSION_FILTER = 14,
    RENDER_PASS_SSS                 = 15,
    RENDER_PASS_POST_PROC           = 16,
    RENDER_PASS_LAYER_SHADOWS       = 17,
    RENDER_PASS_LAYER_BLACK_SHADOWS = 18,
    RENDER_PASS_LAYER_COLOR_SHADOWS = 19,
    RENDER_PASS_LAYER_REFLECTIONS   = 20,
    RENDER_PASS_AMBIENT_LIGHT       = 21,
    RENDER_PASS_SUNLIGHT            = 22,
    RENDER_PASS_LIGHT_1             = 23,
    RENDER_PASS_LIGHT_2             = 24,
    RENDER_PASS_LIGHT_3             = 25,
    RENDER_PASS_LIGHT_4             = 26,
    RENDER_PASS_LIGHT_5             = 27,
    RENDER_PASS_LIGHT_6             = 28,
    RENDER_PASS_LIGHT_7             = 29,
    RENDER_PASS_LIGHT_8             = 30,

    /// offset used for the info channels enum vals (don't use this)
    RENDER_PASS_INFO_OFFSET = 1000,

    /// info channel passes (identical to the info channels)
    RENDER_PASS_GEOMETRIC_NORMAL         = RENDER_PASS_INFO_OFFSET + IC_TYPE_GEOMETRIC_NORMAL,
    RENDER_PASS_SHADING_NORMAL           = RENDER_PASS_INFO_OFFSET + IC_TYPE_SHADING_NORMAL,
    RENDER_PASS_POSITION                 = RENDER_PASS_INFO_OFFSET + IC_TYPE_POSITION,
    RENDER_PASS_Z_DEPTH                  = RENDER_PASS_INFO_OFFSET + IC_TYPE_Z_DEPTH,
    RENDER_PASS_MATERIAL_ID              = RENDER_PASS_INFO_OFFSET + IC_TYPE_MATERIAL_ID,
    RENDER_PASS_UV_COORD                 = RENDER_PASS_INFO_OFFSET + IC_TYPE_UV_COORD,
    RENDER_PASS_TANGENT_U                = RENDER_PASS_INFO_OFFSET + IC_TYPE_TANGENT_U,
    RENDER_PASS_WIREFRAME                = RENDER_PASS_INFO_OFFSET + IC_TYPE_WIREFRAME,
    RENDER_PASS_VERTEX_NORMAL            = RENDER_PASS_INFO_OFFSET + IC_TYPE_VERTEX_NORMAL,
    RENDER_PASS_OBJECT_ID                = RENDER_PASS_INFO_OFFSET + IC_TYPE_OBJECT_ID,
    RENDER_PASS_BAKING_GROUP_ID          = RENDER_PASS_INFO_OFFSET + IC_TYPE_BAKING_GROUP_ID,
    RENDER_PASS_AMBIENT_OCCLUSION        = RENDER_PASS_INFO_OFFSET + IC_TYPE_AMBIENT_OCCLUSION,
    RENDER_PASS_MOTION_VECTOR            = RENDER_PASS_INFO_OFFSET + IC_TYPE_MOTION_VECTOR,
    RENDER_PASS_RENDER_LAYER_ID          = RENDER_PASS_INFO_OFFSET + IC_TYPE_RENDER_LAYER_ID,
    RENDER_PASS_RENDER_LAYER_MASK        = RENDER_PASS_INFO_OFFSET + IC_TYPE_RENDER_LAYER_MASK,
    RENDER_PASS_LIGHT_PASS_ID            = RENDER_PASS_INFO_OFFSET + IC_TYPE_LIGHT_PASS_ID,
    RENDER_PASS_TANGENT_NORMAL           = RENDER_PASS_INFO_OFFSET + IC_TYPE_TANGENT_NORMAL,
    RENDER_PASS_OPACITY                  = RENDER_PASS_INFO_OFFSET + IC_TYPE_OPACITY,
    RENDER_PASS_ROUGHNESS                = RENDER_PASS_INFO_OFFSET + IC_TYPE_ROUGHNESS,
    RENDER_PASS_IOR                      = RENDER_PASS_INFO_OFFSET + IC_TYPE_IOR,
    RENDER_PASS_DIFFUSE_FILTER_INFO      = RENDER_PASS_INFO_OFFSET + IC_TYPE_DIFFUSE_FILTER,
    RENDER_PASS_REFLECTION_FILTER_INFO   = RENDER_PASS_INFO_OFFSET + IC_TYPE_REFLECTION_FILTER,
    RENDER_PASS_REFRACTION_FILTER_INFO   = RENDER_PASS_INFO_OFFSET + IC_TYPE_REFRACTION_FILTER,
    RENDER_PASS_TRANSMISSION_FILTER_INFO = RENDER_PASS_INFO_OFFSET + IC_TYPE_TRANSMISSION_FILTER,
    RENDER_PASS_OBJECT_LAYER_COLOR       = RENDER_PASS_INFO_OFFSET + IC_TYPE_OBJECT_LAYER_COLOR,

    PASS_NONE = -1
};

enum FalloffTextureMode {
    FALLOFF_NORMAL_VS_EYE_RAY,
    FALLOFF_NORMAL_VS_VECTOR_90DEG,
    FALLOFF_NORMAL_VS_VECTOR_180DEG,
};

enum HairInterpolationType {
    /// W is calculated using the relative vertex position in the hair they belong to
    HAIR_INTERP_LENGTH   = 0,
    /// W is calculated using the index of the vertex in the hair they belong to
    HAIR_INTERP_SEGMENTS = 1,
    HAIR_INTERP_NONE,

    /// default hair interpolation type
    HAIR_INTERP_DEFAULT  = HAIR_INTERP_LENGTH,
};

} //namespace Octane


namespace OctaneEngine {

using namespace Octane;
using std::string;
using std::vector;

static const int SERVER_PORT = 5130;

#ifdef _WIN32
#   define LOCK_MUTEX(x) ::EnterCriticalSection(&(x));
#else
#   define LOCK_MUTEX(x) pthread_mutex_lock(&(x));
#endif //#ifdef _WIN32

#ifdef _WIN32
#   define UNLOCK_MUTEX(x) ::LeaveCriticalSection(&(x));
#else
#   define UNLOCK_MUTEX(x) pthread_mutex_unlock(&(x));
#endif //#ifdef _WIN32


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DATA TYPES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#pragma pack(push, 4)
template <typename T> struct Vec2 {
    T x;
    T y;
    inline bool operator==(const Vec2<T> &r) { return x == r.x && y == r.y; }
    inline bool operator!=(const Vec2<T> &r) { return x != r.x || y != r.y; }
};
#pragma pack(pop)

#pragma pack(push, 4)
template <typename T> struct Vec3 {
    T x;
    T y;
    T z;
    inline bool operator==(const Vec3<T> &r) { return x == r.x && y == r.y && z == r.z; }
    inline bool operator!=(const Vec3<T> &r) { return x != r.x || y != r.y || z != r.z; }
};
#pragma pack(pop)

#pragma pack(push, 4)
template <typename T> struct Vec4 {
    T x;
    T y;
    T z;
    T w;
    inline bool operator==(const Vec4<T> &r) { return x == r.x && y == r.y && z == r.z && w == r.w; }
    inline bool operator!=(const Vec4<T> &r) { return x != r.x || y != r.y || z != r.z || w != r.w; }
};
#pragma pack(pop)

#pragma pack(push, 4)
struct MatrixF {
    /// every Vec4 is one row
    Vec4<float> m[3];
};
#pragma pack(pop)

#ifdef __GNUC__
	typedef int8_t                int8_t;
	typedef int32_t               int32_t;
	typedef int64_t               int64_t;
	typedef uint8_t               uint8_t;
	typedef uint32_t              uint32_t;
	typedef uint64_t              uint64_t;

    typedef Vec2<int8_t>            int8_2;
    typedef Vec2<uint8_t>           uint8_2;
    typedef Vec3<int8_t>            int8_3;
    typedef Vec3<uint8_t>           uint8_3;
    typedef Vec4<int8_t>            int8_4;
    typedef Vec4<uint8_t>           uint8_4;

    typedef Vec2<int32_t>           int32_2;
    typedef Vec2<uint32_t>          uint32_2;
    typedef Vec3<int32_t>           int32_3;
    typedef Vec3<uint32_t>          uint32_3;
    typedef Vec4<int32_t>           int32_4;
    typedef Vec4<uint32_t>          uint32_4;

    typedef Vec2<int64_t>           int64_2;
    typedef Vec2<uint64_t>          uint64_2;
    typedef Vec3<int64_t>           int64_3;
    typedef Vec3<uint64_t>          uint64_3;
    typedef Vec4<int64_t>           int64_4;
    typedef Vec4<uint64_t>          uint64_4;
#elif defined(_MSC_VER)
	typedef __int8                  int8_t;
	typedef __int32                 int32_t;
	typedef __int64                 int64_t;
	typedef unsigned __int8         uint8_t;
	typedef unsigned __int32        uint32_t;
	typedef unsigned __int64        uint64_t;

    typedef Vec2<__int8>            int8_2;
    typedef Vec2<unsigned __int8>   uint8_2;
    typedef Vec3<__int8>            int8_3;
    typedef Vec3<unsigned __int8>   uint8_3;
    typedef Vec4<__int8>            int8_4;
    typedef Vec4<unsigned __int8>   uint8_4;

    typedef Vec2<__int32>           int32_2;
    typedef Vec2<unsigned __int32>  uint32_2;
    typedef Vec3<__int32>           int32_3;
    typedef Vec3<unsigned __int32>  uint32_3;
    typedef Vec4<__int32>           int32_4;
    typedef Vec4<unsigned __int32>  uint32_4;

    typedef Vec2<__int64>           int64_2;
    typedef Vec2<unsigned __int64>  uint64_2;
    typedef Vec3<__int64>           int64_3;
    typedef Vec3<unsigned __int64>  uint64_3;
    typedef Vec4<__int64>           int64_4;
    typedef Vec4<unsigned __int64>  uint64_4;
#else
	typedef char                    int8_t;
	typedef int                     int32_t;
	typedef long long int           int64_t;
	typedef unsigned char           uint8_t;
	typedef unsigned int            uint32_t;
	typedef unsigned long long int  uint64_t;

    typedef Vec2<char>              int8_2;
    typedef Vec2<unsigned char>     uint8_2;
    typedef Vec3<char>              int8_3;
    typedef Vec3<unsigned char>     uint8_3;
    typedef Vec4<char>              int8_4;
    typedef Vec4<unsigned char>     uint8_4;

    typedef Vec2<int>               int32_2;
    typedef Vec2<unsigned int>      uint32_2;
    typedef Vec3<int>               int32_3;
    typedef Vec3<unsigned int>      uint32_3;
    typedef Vec4<int>               int32_4;
    typedef Vec4<unsigned int>      uint32_4;

    typedef Vec2<long long int>           int64_2;
    typedef Vec2<unsigned long long int>  uint64_2;
    typedef Vec3<long long int>           int64_3;
    typedef Vec3<unsigned long long int>  uint64_3;
    typedef Vec4<long long int>           int64_4;
    typedef Vec4<unsigned long long int>  uint64_4;
#endif

typedef Vec2<float> float_2;
typedef Vec3<float> float_3;
typedef Vec4<float> float_4;


#ifdef _WIN32


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// UTF-8 TO UTF-16 CONVERSION HELPERS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#define UTF_ERROR_NULL_IN 1 << 0 /* Error occures when requered parameter is missing*/
#define UTF_ERROR_ILLCHAR 1 << 1 /* Error if character is in illigal UTF rage*/
#define UTF_ERROR_SMALL   1 << 2 /* Passed size is to small. It gives legal string with character missing at the end*/
#define UTF_ERROR_ILLSEQ  1 << 3 /* Error if sequence is broken and doesn't finish*/

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the nuber of Utf-16 characters representing the given Utf-8 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
#   pragma warning (push)
#   pragma warning (disable : 4706)
#endif
inline size_t utf16_len_of_utf8(const char *szU8) {
    size_t          stCharCnt   = 0;
    char            cCurType    = 0;
    uint32_t        u32         = 0;
    char            u;

    if(!szU8) return 0;

    for(; (u = *szU8); ++szU8) {
#ifdef _WIN32
#   pragma warning (pop)
#endif
        if(cCurType == 0) {
            if((u & 0x01 << 7) == 0)     { ++stCharCnt; u32 = 0; continue; }         //1 utf-8 char
            if((u & 0x07 << 5) == 0xC0)  { cCurType = 1; u32 = u & 0x1F; continue; } //2 utf-8 char
            if((u & 0x0F << 4) == 0xE0)  { cCurType = 2; u32 = u & 0x0F; continue; } //3 utf-8 char
            if((u & 0x1F << 3) == 0xF0)  { cCurType = 3; u32 = u & 0x07; continue; } //4 utf-8 char
            continue;
        }
        else {
            if((u & 0xC0) == 0x80) {
                u32 = (u32 << 6) | (u & 0x3F);
                --cCurType;
            }
            else {
                u32      = 0;
                cCurType = 0;
            }
        }

        if(cCurType == 0) {
            if((0 < u32 && u32 < 0xD800) || (0xE000 <= u32 && u32 < 0x10000)) ++stCharCnt;
            else if(0x10000 <= u32 && u32 < 0x110000) stCharCnt += 2;
            u32 = 0;
        }
    }

    return ++stCharCnt;
} //utf16_len_of_utf8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-8 string to Utf-16 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
#   pragma warning (push)
#   pragma warning (disable : 4706)
#endif
inline int utf8_to_utf16(const char *szU8, wchar_t *wszU16, size_t stSizeU16) {
    char        cCurType    = 0;
    uint32_t    u32         = 0;
    int         err         = 0;
    wchar_t     *wszU16end  = wszU16 + stSizeU16 - 1;
    char        u;

    if(!stSizeU16 || !szU8 || !wszU16) return UTF_ERROR_NULL_IN;
    //wszU16end--;

    for(; wszU16 < wszU16end && (u = *szU8); ++szU8) {
#ifdef _WIN32
#   pragma warning (pop)
#endif
        if(cCurType == 0) {
            if((u & 0x01 << 7) == 0)     { *wszU16 = u; ++wszU16; u32 = 0; continue; }  //1 utf-8 char
            if((u & 0x07 << 5) == 0xC0)  { cCurType = 1; u32 = u & 0x1F; continue; }    //2 utf-8 char
            if((u & 0x0F << 4) == 0xE0)  { cCurType = 2; u32 = u & 0x0F; continue; }    //3 utf-8 char
            if((u & 0x1F << 3) == 0xF0)  { cCurType = 3; u32 = u & 0x07; continue; }    //4 utf-8 char
            err |= UTF_ERROR_ILLCHAR;
            continue;
        }
        else {
            if((u & 0xC0) == 0x80) {
                u32 = (u32 << 6) | (u & 0x3F);
                --cCurType;
            }
            else {
                u32 = 0; cCurType = 0; err |= UTF_ERROR_ILLSEQ;
            }
        }
        if(cCurType == 0) {
            if((0 < u32 && u32 < 0xD800) || (0xE000 <= u32 && u32 < 0x10000)) {
                *wszU16 = static_cast<wchar_t>(u32);
                ++wszU16;
            }
            else if(0x10000 <= u32 && u32 < 0x110000) {
                if(wszU16 + 1 >= wszU16end) break;
                u32 -= 0x10000;
                *wszU16 = static_cast<wchar_t>(0xD800 + (u32 >> 10));
                ++wszU16;
                *wszU16 = 0xDC00 + (u32 & 0x3FF);
                ++wszU16;
            }
            u32 = 0;
        }

    }

    *wszU16 = *wszU16end = 0;

    if(*szU8) err |= UTF_ERROR_SMALL;

    return err;
} //utf8_to_utf16()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the nuber of Utf-8 characters representing the given Utf-16 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline size_t utf8_len_of_utf16(const wchar_t *szU16) {
    size_t      stCharCnt   = 0;
    wchar_t     u           = 0;

    if(!szU16) return 0;

    for(int i = 0; (u = szU16[i]); ++i) {
        if(u < 0x0080) stCharCnt += 1;
        else {
            if(u < 0x0800) stCharCnt += 2;
            else {
                if(u < 0xD800) stCharCnt += 3;
                else {
                    if(u < 0xDC00) {
                        ++i;
                        if((u = szU16[i]) == 0) break;
                        if(u >= 0xDC00 && u < 0xE000) stCharCnt += 4;
                    }
                    else {
                        if(u < 0xE000) {
                            /*illigal*/;
                        }
                        else stCharCnt += 3;
                    }
                }
            }
        }
    }

    return ++stCharCnt;
} //utf8_len_of_utf16()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-16 string to Utf-8 string
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int utf16_to_utf8(const wchar_t *szU16, char *szU8, size_t stSizeU8) {
    wchar_t u           = 0;
    int     err         = 0;
    char    *wszU8end   = szU8 + stSizeU8 - 1;

    if(!stSizeU8 || !szU16 || !szU8) return UTF_ERROR_NULL_IN;
    //wszU8end--;

    for(; szU8 < wszU8end && (u = *szU16); ++szU16, ++szU8) {
        if(u < 0x0080) *szU8 = static_cast<char>(u);
        else if(u < 0x0800) {
            if(szU8 + 1 >= wszU8end) break;
            *szU8++ = (0x3 << 6) | (0x1F & (u >> 6));
            *szU8   = (0x1 << 7) | (0x3F & (u));
        }
        else if(u < 0xD800 || u >= 0xE000) {
            if(szU8 + 2 >= wszU8end) break;
            *szU8++ = (0x7 << 5) | (0xF & (u >> 12));
            *szU8++ = (0x1 << 7) | (0x3F & (u >> 6));
            *szU8   = (0x1 << 7) | (0x3F & (u));
        }
        else if(u < 0xDC00) {
            wchar_t u2 = *++szU16;

            if(!u2) break;
            if(u2 >= 0xDC00 && u2 < 0xE000) {
                if(szU8 + 3 >= wszU8end) break;
                else {
                    uint32_t uc = 0x10000 + (u2 - 0xDC00) + ((u - 0xD800) << 10);

                    *szU8++ = (0xF << 4) | (0x7 & (uc >> 18));
                    *szU8++ = (0x1 << 7) | (0x3F & (uc >> 12));
                    *szU8++ = (0x1 << 7) | (0x3F & (uc >> 6));
                    *szU8   = (0x1 << 7) | (0x3F & (uc));
                }
            }
            else {
                --szU8; err |= UTF_ERROR_ILLCHAR;
            }
        }
        else if(u < 0xE000) {
            --szU8; err |= UTF_ERROR_ILLCHAR;
        }
    }

    *szU8 = *wszU8end = 0;

    if(*szU16) err |= UTF_ERROR_SMALL;

    return err;
} //utf16_to_utf8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-8 string to Utf-16 string, allocating the Utf-16 buffer (must be freed by caller)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline wchar_t *utf8_to_utf16_alloc(const char *szU8) {
    size_t stU16len = utf16_len_of_utf8(szU8);
    if(!stU16len) return 0;

    wchar_t *wszU16 = (wchar_t*) malloc(sizeof(wchar_t) * stU16len);
    utf8_to_utf16(szU8, wszU16, stU16len);
    return wszU16;
} //alloc_utf16_from_8()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Convert the Utf-16 string to Utf-8 string, allocating the Utf-8 buffer (must be freed by caller)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *utf16_to_utf8_alloc(const wchar_t *szU16) {
    size_t stU8len = utf8_len_of_utf16(szU16);
    if (!stU8len) return 0;

    char *szU8 = (char*) malloc(sizeof(char) * stU8len);
    utf16_to_utf8(szU16, szU8, stU8len);
    return szU8;
} //utf16_to_utf8_alloc()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Easy allocation and conversion to the new Utf-16 string. New string has _16 suffix. Must be deallocated with UTF16_ENCODE_FINISH in right order.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define UTF16_ENCODE(u8string) { \
    wchar_t *u8string ## _16 = utf8_to_utf16_alloc((char*)u8string)

#define UTF16_ENCODE_FINISH(u8string) \
    free(u8string ## _16); } (void)0

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// FILE FUNCTIONS WORKING WITH UTF-8 NAMES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *filename, const char *mode) {
	FILE *f = 0;

	UTF16_ENCODE(filename);
	UTF16_ENCODE(mode);

	if(filename_16 && mode_16)
		f = _wfopen(filename_16, mode_16);
	
	UTF16_ENCODE_FINISH(mode);
	UTF16_ENCODE_FINISH(filename);

	if(!f) {
		if((f = fopen(filename, mode))) {
			//printf("%s is not Utf-8 file name.\n", filename);
		}
	}
	return f;
} //ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const wchar_t *wszU16part, const char *szU8part, const char *szU8mode) {
    FILE *f = 0;

    UTF16_ENCODE(szU8part);
    UTF16_ENCODE(szU8mode);

    if(szU8part_16 && szU8mode_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, wszU16part);
        wcscat_s(wszFullPath, szU8part_16);
        f = _wfopen(wszFullPath, szU8mode_16);
    }

    UTF16_ENCODE_FINISH(szU8mode);
    UTF16_ENCODE_FINISH(szU8part);

    return f;
} //ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *szU8part, const wchar_t *wszU16part, const char *szU8mode) {
    FILE *f = 0;

    UTF16_ENCODE(szU8part);
    UTF16_ENCODE(szU8mode);

    if(szU8part_16 && szU8mode_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, szU8part_16);
        wcscat_s(wszFullPath, wszU16part);
        f = _wfopen(wszFullPath, szU8mode_16);
    }

    UTF16_ENCODE_FINISH(szU8mode);
    UTF16_ENCODE_FINISH(szU8part);

    return f;
} //ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *filename, struct _stat64i32 *attrib) {
    int ret = -1;

    UTF16_ENCODE(filename);

    if(filename_16) {
        ret = _wstat(filename_16, attrib);
    }

    UTF16_ENCODE_FINISH(filename);

    return ret;
} //ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const wchar_t *wszU16part, const char *szU8part, struct _stat64i32 *attrib) {
    int ret = -1;

    UTF16_ENCODE(szU8part);

    if(szU8part_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, wszU16part);
        wcscat_s(wszFullPath, szU8part_16);
        ret = _wstat(wszFullPath, attrib);
    }

    UTF16_ENCODE_FINISH(szU8part);

    return ret;
} //ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *szU8part, const wchar_t *wszU16part, struct _stat64i32 *attrib) {
    int ret = -1;

    UTF16_ENCODE(szU8part);

    if(szU8part_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, szU8part_16);
        wcscat_s(wszFullPath, wszU16part);
        ret = _wstat(wszFullPath, attrib);
    }

    UTF16_ENCODE_FINISH(szU8part);

    return ret;
} //ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const wchar_t *wszU16part, const char *szU8part) {
    int ret = -1;

    UTF16_ENCODE(szU8part);

    if(szU8part_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, wszU16part);
        wcscat_s(wszFullPath, szU8part_16);
        ret = _wremove(wszFullPath);
    }

    UTF16_ENCODE_FINISH(szU8part);

    return ret;
} //uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const char *szU8part, const wchar_t *wszU16part) {
    int ret = -1;

    UTF16_ENCODE(szU8part);

    if(szU8part_16) {
        wchar_t wszFullPath[MAX_PATH];
        wcscpy_s(wszFullPath, szU8part_16);
        wcscat_s(wszFullPath, wszU16part);
        ret = _wremove(wszFullPath);
    }

    UTF16_ENCODE_FINISH(szU8part);

    return ret;
} //uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uopen(const char *filename, int oflag, int pmode) {
	int f = -1;

	UTF16_ENCODE(filename);
	
	if(filename_16)
		f = _wopen(filename_16, oflag, pmode);

	UTF16_ENCODE_FINISH(filename);

	if(f == -1) {
		if((f = _open(filename, oflag, pmode)) != -1) {
			//printf("%s is not Utf-8 file name.\n", filename);
		}
	}
	return f;
} //uopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uaccess(const char *filename, int mode) {
	int r = -1;

	UTF16_ENCODE(filename);

	if(filename_16)
		r = _waccess(filename_16, mode);

	UTF16_ENCODE_FINISH(filename);

	return r;
} //uaccess()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int urename(const char *oldname, const char *newname) {
	int r = -1;

	UTF16_ENCODE(oldname);
	UTF16_ENCODE(newname);

	if(oldname_16 && newname_16)
		r = _wrename(oldname_16, newname_16);
	
	UTF16_ENCODE_FINISH(newname);
	UTF16_ENCODE_FINISH(oldname);

	return r;
} //urename()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int umkdir(const char *pathname) {
	bool ret = false;

	UTF16_ENCODE(pathname);
	
	if(pathname_16)
		ret = CreateDirectoryW(pathname_16, 0) ? true : false;

	UTF16_ENCODE_FINISH(pathname);

	return ret ? 0 : -1;
} //umkdir()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *ugetenv_alloc(const char *varname) {
	char    *ret = 0;
	wchar_t *wszValue;

	UTF16_ENCODE(varname);

	if(varname_16) {
		wszValue = _wgetenv(varname_16);
		ret      = utf16_to_utf8_alloc(wszValue);
	}
	UTF16_ENCODE_FINISH(varname);

	return ret;
} //ugetenv_alloc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void  ugetenv_free(char *val) {
	free(val);
} //ugetenv_free()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ugetenv_put(const char *varname, char *szU8, size_t buffsize) {
	int     ret = 0;
	wchar_t *wszValue;

	if(!buffsize) return ret;

	UTF16_ENCODE(varname);

	if(varname_16) {
		wszValue = _wgetenv(varname_16);
		utf16_to_utf8(wszValue, szU8, buffsize);
		ret = 1;
	}

	UTF16_ENCODE_FINISH(varname);

	if(!ret) szU8[0] = 0;

	return ret;
} //ugetenv_put()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uputenv(const char *szU8name, const char *szU8value) {
	int ret = -1;

	UTF16_ENCODE(szU8name);

	if(szU8value) {
		// Set the env variable
		UTF16_ENCODE(szU8value);

		if(szU8name_16 && szU8value_16)
			ret = (SetEnvironmentVariableW(szU8name_16, szU8value_16) != 0) ? 0 : -1;

		UTF16_ENCODE_FINISH(szU8value);
	}
	else {
        // Clear the env variable
		if(szU8name_16)
			ret = (SetEnvironmentVariableW(szU8name_16, 0) != 0) ? 0 : -1;
	}

	UTF16_ENCODE_FINISH(szU8name);

	return ret;
} //uputenv()

#else //#ifdef _WIN32

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *filename, const char *mode) {
    return fopen(filename, mode);
} //ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline FILE *ufopen(const char *szFirstPart, const char *szSecondPart, const char *szU8mode) {
    FILE *f = 0;

    if(szFirstPart && szSecondPart && szU8mode) {
        char szFullPath[MAX_PATH];
        strcpy(szFullPath, szFirstPart);
        strcat(szFullPath, szSecondPart);
        f = fopen(szFullPath, szU8mode);
    }

    return f;
} //ufopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *filename, struct stat *attrib) {
    int ret = -1;

    if(filename && attrib) {
        ret = stat(filename, attrib);
    }

    return ret;
} //ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ustat(const char *szFirstPart, const char *szSecondPart, struct stat *attrib) {
    int ret = -1;

    if(szFirstPart && szSecondPart && attrib) {
        char szFullPath[MAX_PATH];
        strcpy(szFullPath, szFirstPart);
        strcat(szFullPath, szSecondPart);
        ret = stat(szFullPath, attrib);
    }

    return ret;
} //ustat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uremove(const char *szFirstPart, const char *szSecondPart) {
    int ret = -1;

    if(szFirstPart && szSecondPart) {
        char szFullPath[MAX_PATH];
        strcpy(szFullPath, szFirstPart);
        strcat(szFullPath, szSecondPart);
        ret = remove(szFullPath);
    }

    return ret;
} //uremove()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uopen(const char *filename, int oflag, int pmode) {
    return open(filename,oflag, pmode);
} //uopen()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uaccess(const char *filename, int mode) {
    return access(filename, mode);
} //uaccess()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int urename(const char *oldname, const char *newname) {
    return rename(oldname, newname);
} //urename()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int umkdir(const char *pathname) {
    return mkdir(pathname, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
} //umkdir()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline char *ugetenv_alloc(const char *varname) {
    return getenv(varname);
} //ugetenv_alloc()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void  ugetenv_free(char *val) {
    return;
} //ugetenv_free()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int ugetenv_put(const char *varname, char *szU8, size_t buffsize) {
    int     ret = 0;

    if(!buffsize) return ret;

    char *szValue = getenv(varname);
    strncpy(szU8, szValue, buffsize);
    ret = 1;

    return ret;
} //ugetenv_put()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline int uputenv(const char *szU8name, const char *szU8value) {
    int ret = -1;

    if(szU8name && szU8value) {
        // Set the env variable
        ret = (setenv(szU8name, szU8value, 1) != 0) ? 0 : -1;
    }
    else {
        // Clear the env variable
        ret = (unsetenv(szU8name) != 0) ? 0 : -1;
    }

    return ret;
} //uputenv()

#endif //#ifdef _WIN32


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OCTANE SERVER
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PARAMETER TYPES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#pragma pack(push, 4)
/// Complex value structure for passing default greyscale or color values of textures.
struct ComplexValue {
	/// Type of the value.
    /// 0 - No value.
    /// 1 - Float value.
    /// 2 - Float-2 value (RESERVED for now).
    /// 3 - Float-3 value.
    int32_t     iType;
    float_3     f3Value;
}; //struct ComplexValue
#pragma pack(pop)

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Camera
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a camera data that is going to be uploaded to the Octane server.
struct Camera {
    enum CameraType {
        CAMERA_PERSPECTIVE,
        CAMERA_PANORAMA,
        CAMERA_BAKING,
        NONE
    };
    
    CameraType  type;

    bool        bUseRegion;
    uint32_4    ui4Region;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Camera
    float_3             f3EyePoint;
    float_3             f3LookAt;
    float_3             f3UpVector;
    float               fFOV; // Holds ortho scale in the case of orthographic camera
    float               fFOVx;
    float               fFOVy;
    bool                bUseFstopValue;
    float               fAperture;
    float               fApertureEdge;
    float               fDistortion;
    bool                bAutofocus;
    float               fFocalDepth;
    float               fNearClipDepth;
    float               fFarClipDepth;
    float_2             f2LensShift;
    bool                bPerspCorr;
    float               fStereoDist;
    float               fStereoDistFalloff;
    float               fTolerance;
    bool                bOrtho;
    PanoramicCameraMode panCamMode;
    StereoMode          stereoMode;
    StereoOutput        stereoOutput;
    int32_t             iBakingGroupId;
    int32_t             iPadding;
    int32_t             iUvSet;
    bool                bBakeOutwards;
    bool                bUseBakingPosition;
    bool                bBackfaceCulling;
    float_3             f3LeftFilter, f3RightFilter;
    float               fPixelAspect, fApertureAspect, fBlackoutLat;
    bool                bKeepUpright;
    float_2             f2UVboxMin;
    float_2             f2UVboxSize;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Imager
    float_3         f3WhiteBalance;
    ResponseCurveId responseCurve;
    float           fExposure;
    float           fGamma;
    float           fVignetting;
    float           fSaturation;
    float           fHotPixelFilter;
    bool            bPremultipliedAlpha;
    int32_t         iMinDisplaySamples;
    bool            bDithering;
    float           fWhiteSaturation;
    float           fHighlightCompression;
    int32_t         iMaxTonemapInterval;
    bool            bNeutralResponse;
    bool            bDisablePartialAlpha;
    bool            bSwapEyes;

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Postprocessor
    bool    bUsePostprocess;
    float   fBloomPower;
    float   fGlarePower;
    int32_t iGlareRayCount;
    float   fGlareAngle;
    float   fGlareBlur;
    float   fSpectralIntencity;
    float   fSpectralShift;

    inline Camera() : type(NONE) {}
    inline bool operator!=(const Camera& otherCam) {
        return (type != otherCam.type

                || bUseRegion != otherCam.bUseRegion
                || ui4Region != otherCam.ui4Region

                || f3EyePoint != otherCam.f3EyePoint
                || f3LookAt != otherCam.f3LookAt
                || f3UpVector != otherCam.f3UpVector
                || fFOV != otherCam.fFOV
                || fFOVx != otherCam.fFOVx
                || fFOVy != otherCam.fFOVy
                || bUseFstopValue != otherCam.bUseFstopValue
                || fAperture != otherCam.fAperture
                || fApertureEdge != otherCam.fApertureEdge
                || fDistortion != otherCam.fDistortion
                || bAutofocus != otherCam.bAutofocus
                || fFocalDepth != otherCam.fFocalDepth
                || fNearClipDepth != otherCam.fNearClipDepth
                || fFarClipDepth != otherCam.fFarClipDepth
                || f2LensShift != otherCam.f2LensShift
                || bPerspCorr != otherCam.bPerspCorr
                || fStereoDist != otherCam.fStereoDist
                || fStereoDistFalloff != otherCam.fStereoDistFalloff
                || fTolerance != otherCam.fTolerance
                || bOrtho != otherCam.bOrtho
                || panCamMode != otherCam.panCamMode
                || stereoMode != otherCam.stereoMode
                || stereoOutput != otherCam.stereoOutput
                || iBakingGroupId != otherCam.iBakingGroupId
                || iPadding != otherCam.iPadding
                || iUvSet != otherCam.iUvSet
                || bBakeOutwards != otherCam.bBakeOutwards
                || bUseBakingPosition != otherCam.bUseBakingPosition
                || f2UVboxMin != otherCam.f2UVboxMin
                || f2UVboxSize != otherCam.f2UVboxSize
                || bBackfaceCulling != otherCam.bBackfaceCulling
                || f3LeftFilter != otherCam.f3LeftFilter
                || f3RightFilter != otherCam.f3RightFilter
                || fPixelAspect != otherCam.fPixelAspect
                || fApertureAspect != otherCam.fApertureAspect
                || fBlackoutLat != otherCam.fBlackoutLat
                || bKeepUpright != otherCam.bKeepUpright

                || f3WhiteBalance != otherCam.f3WhiteBalance
                || responseCurve != otherCam.responseCurve
                || fExposure != otherCam.fExposure
                || fGamma != otherCam.fGamma
                || fVignetting != otherCam.fVignetting
                || fSaturation != otherCam.fSaturation
                || fHotPixelFilter != otherCam.fHotPixelFilter
                || bPremultipliedAlpha != otherCam.bPremultipliedAlpha
                || iMinDisplaySamples != otherCam.iMinDisplaySamples
                || bDithering != otherCam.bDithering
                || fWhiteSaturation != otherCam.fWhiteSaturation
                || fHighlightCompression != otherCam.fHighlightCompression
                || iMaxTonemapInterval != otherCam.iMaxTonemapInterval
                || bNeutralResponse != otherCam.bNeutralResponse
                || bDisablePartialAlpha != otherCam.bDisablePartialAlpha
                || bSwapEyes != otherCam.bSwapEyes

                || bUsePostprocess != otherCam.bUsePostprocess
                || fBloomPower != otherCam.fBloomPower
                || fGlarePower != otherCam.fGlarePower
                || iGlareRayCount != otherCam.iGlareRayCount
                || fGlareAngle != otherCam.fGlareAngle
                || fGlareBlur != otherCam.fGlareBlur
                || fSpectralIntencity != otherCam.fSpectralIntencity
                || fSpectralShift != otherCam.fSpectralShift);
    }
    inline bool operator==(const Camera& otherCam) {
        return (type == otherCam.type

                && bUseRegion == otherCam.bUseRegion
                && ui4Region == otherCam.ui4Region

                && f3EyePoint == otherCam.f3EyePoint
                && f3LookAt == otherCam.f3LookAt
                && f3UpVector == otherCam.f3UpVector
                && fFOV == otherCam.fFOV
                && fFOVx == otherCam.fFOVx
                && fFOVy == otherCam.fFOVy
                && bUseFstopValue == otherCam.bUseFstopValue
                && fAperture == otherCam.fAperture
                && fApertureEdge == otherCam.fApertureEdge
                && fDistortion == otherCam.fDistortion
                && bAutofocus == otherCam.bAutofocus
                && fFocalDepth == otherCam.fFocalDepth
                && fNearClipDepth == otherCam.fNearClipDepth
                && fFarClipDepth == otherCam.fFarClipDepth
                && f2LensShift == otherCam.f2LensShift
                && bPerspCorr == otherCam.bPerspCorr
                && fStereoDist == otherCam.fStereoDist
                && fStereoDistFalloff == otherCam.fStereoDistFalloff
                && fTolerance == otherCam.fTolerance
                && bOrtho == otherCam.bOrtho
                && panCamMode == otherCam.panCamMode
                && stereoMode == otherCam.stereoMode
                && stereoOutput == otherCam.stereoOutput
                && iBakingGroupId == otherCam.iBakingGroupId
                && iPadding == otherCam.iPadding
                && iUvSet == otherCam.iUvSet
                && bBakeOutwards == otherCam.bBakeOutwards
                && bUseBakingPosition == otherCam.bUseBakingPosition
                && f2UVboxMin == otherCam.f2UVboxMin
                && f2UVboxSize == otherCam.f2UVboxSize
                && bBackfaceCulling == otherCam.bBackfaceCulling
                && f3LeftFilter == otherCam.f3LeftFilter
                && f3RightFilter == otherCam.f3RightFilter
                && fPixelAspect == otherCam.fPixelAspect
                && fApertureAspect == otherCam.fApertureAspect
                && fBlackoutLat == otherCam.fBlackoutLat
                && bKeepUpright == otherCam.bKeepUpright

                && f3WhiteBalance == otherCam.f3WhiteBalance
                && responseCurve == otherCam.responseCurve
                && fExposure == otherCam.fExposure
                && fGamma == otherCam.fGamma
                && fVignetting == otherCam.fVignetting
                && fSaturation == otherCam.fSaturation
                && fHotPixelFilter == otherCam.fHotPixelFilter
                && bPremultipliedAlpha == otherCam.bPremultipliedAlpha
                && iMinDisplaySamples == otherCam.iMinDisplaySamples
                && bDithering == otherCam.bDithering
                && fWhiteSaturation == otherCam.fWhiteSaturation
                && fHighlightCompression == otherCam.fHighlightCompression
                && iMaxTonemapInterval == otherCam.iMaxTonemapInterval
                && bNeutralResponse == otherCam.bNeutralResponse
                && bDisablePartialAlpha == otherCam.bDisablePartialAlpha
                && bSwapEyes == otherCam.bSwapEyes

                && bUsePostprocess == otherCam.bUsePostprocess
                && fBloomPower == otherCam.fBloomPower
                && fGlarePower == otherCam.fGlarePower
                && iGlareRayCount == otherCam.iGlareRayCount
                && fGlareAngle == otherCam.fGlareAngle
                && fGlareBlur == otherCam.fGlareBlur
                && fSpectralIntencity == otherCam.fSpectralIntencity
                && fSpectralShift == otherCam.fSpectralShift);
    }
    inline Camera& operator=(const Camera& otherCam) {
        if(type != otherCam.type) type = otherCam.type;

        if(bUseRegion != otherCam.bUseRegion)   bUseRegion = otherCam.bUseRegion;
        if(ui4Region != otherCam.ui4Region)     ui4Region = otherCam.ui4Region;

        if(f3EyePoint != otherCam.f3EyePoint)                   f3EyePoint = otherCam.f3EyePoint;
        if(f3LookAt != otherCam.f3LookAt)                       f3LookAt = otherCam.f3LookAt;
        if(f3UpVector != otherCam.f3UpVector)                   f3UpVector = otherCam.f3UpVector;
        if(fFOV != otherCam.fFOV)                               fFOV = otherCam.fFOV;
        if(fFOVx != otherCam.fFOVx)                             fFOVx = otherCam.fFOVx;
        if(fFOVy != otherCam.fFOVy)                             fFOVy = otherCam.fFOVy;
        if(bUseFstopValue != otherCam.bUseFstopValue)           bUseFstopValue = otherCam.bUseFstopValue;
        if(fAperture != otherCam.fAperture)                     fAperture = otherCam.fAperture;
        if(fApertureEdge != otherCam.fApertureEdge)             fApertureEdge = otherCam.fApertureEdge;
        if(fDistortion != otherCam.fDistortion)                 fDistortion = otherCam.fDistortion;
        if(bAutofocus != otherCam.bAutofocus)                   bAutofocus = otherCam.bAutofocus;
        if(fFocalDepth != otherCam.fFocalDepth)                 fFocalDepth = otherCam.fFocalDepth;
        if(fNearClipDepth != otherCam.fNearClipDepth)           fNearClipDepth = otherCam.fNearClipDepth;
        if(fFarClipDepth != otherCam.fFarClipDepth)             fFarClipDepth = otherCam.fFarClipDepth;
        if(f2LensShift != otherCam.f2LensShift)                 f2LensShift = otherCam.f2LensShift;
        if(bPerspCorr != otherCam.bPerspCorr)                   bPerspCorr = otherCam.bPerspCorr;
        if(fStereoDist != otherCam.fStereoDist)                 fStereoDist = otherCam.fStereoDist;
        if(fStereoDistFalloff != otherCam.fStereoDistFalloff)   fStereoDistFalloff = otherCam.fStereoDistFalloff;
        if(fTolerance != otherCam.fTolerance)                   fTolerance = otherCam.fTolerance;
        if(bOrtho != otherCam.bOrtho)                           bOrtho = otherCam.bOrtho;
        if(panCamMode != otherCam.panCamMode)                   panCamMode = otherCam.panCamMode;
        if(stereoMode != otherCam.stereoMode)                   stereoMode = otherCam.stereoMode;
        if(stereoOutput != otherCam.stereoOutput)               stereoOutput = otherCam.stereoOutput;
        if(iBakingGroupId != otherCam.iBakingGroupId)           iBakingGroupId = otherCam.iBakingGroupId;
        if(iPadding != otherCam.iPadding)                       iPadding = otherCam.iPadding;
        if(iUvSet != otherCam.iUvSet)                           iUvSet = otherCam.iUvSet;
        if(bBakeOutwards != otherCam.bBakeOutwards)             bBakeOutwards = otherCam.bBakeOutwards;
        if(bUseBakingPosition != otherCam.bUseBakingPosition)   bUseBakingPosition = otherCam.bUseBakingPosition;
        if(f2UVboxMin != otherCam.f2UVboxMin)                   f2UVboxMin = otherCam.f2UVboxMin;
        if(f2UVboxSize != otherCam.f2UVboxSize)                 f2UVboxSize = otherCam.f2UVboxSize;
        if(bBackfaceCulling != otherCam.bBackfaceCulling)       bBackfaceCulling = otherCam.bBackfaceCulling;
        if(f3LeftFilter != otherCam.f3LeftFilter)               f3LeftFilter = otherCam.f3LeftFilter;
        if(f3RightFilter != otherCam.f3RightFilter)             f3RightFilter = otherCam.f3RightFilter;
        if(fPixelAspect != otherCam.fPixelAspect)               fPixelAspect = otherCam.fPixelAspect;
        if(fApertureAspect != otherCam.fApertureAspect)         fApertureAspect = otherCam.fApertureAspect;
        if(fBlackoutLat != otherCam.fBlackoutLat)               fBlackoutLat = otherCam.fBlackoutLat;
        if(bKeepUpright != otherCam.bKeepUpright)               bKeepUpright = otherCam.bKeepUpright;

        if(f3WhiteBalance != otherCam.f3WhiteBalance)                   f3WhiteBalance = otherCam.f3WhiteBalance;
        if(responseCurve != otherCam.responseCurve)                     responseCurve = otherCam.responseCurve;
        if(fExposure != otherCam.fExposure)                             fExposure = otherCam.fExposure;
        if(fGamma != otherCam.fGamma)                                   fGamma = otherCam.fGamma;
        if(fVignetting != otherCam.fVignetting)                         fVignetting = otherCam.fVignetting;
        if(fSaturation != otherCam.fSaturation)                         fSaturation = otherCam.fSaturation;
        if(fHotPixelFilter != otherCam.fHotPixelFilter)                 fHotPixelFilter = otherCam.fHotPixelFilter;
        if(bPremultipliedAlpha != otherCam.bPremultipliedAlpha)         bPremultipliedAlpha = otherCam.bPremultipliedAlpha;
        if(iMinDisplaySamples != otherCam.iMinDisplaySamples)           iMinDisplaySamples = otherCam.iMinDisplaySamples;
        if(bDithering != otherCam.bDithering)                           bDithering = otherCam.bDithering;
        if(fWhiteSaturation != otherCam.fWhiteSaturation)               fWhiteSaturation = otherCam.fWhiteSaturation;
        if(fHighlightCompression != otherCam.fHighlightCompression)     fHighlightCompression = otherCam.fHighlightCompression;
        if(iMaxTonemapInterval != otherCam.iMaxTonemapInterval)         iMaxTonemapInterval = otherCam.iMaxTonemapInterval;
        if(bNeutralResponse != otherCam.bNeutralResponse)               bNeutralResponse = otherCam.bNeutralResponse;
        if(bDisablePartialAlpha != otherCam.bDisablePartialAlpha)       bDisablePartialAlpha = otherCam.bDisablePartialAlpha;
        if(bSwapEyes != otherCam.bSwapEyes)                             bSwapEyes = otherCam.bSwapEyes;

        if(bUsePostprocess != otherCam.bUsePostprocess)         bUsePostprocess = otherCam.bUsePostprocess;
        if(fBloomPower != otherCam.fBloomPower)                 fBloomPower = otherCam.fBloomPower;
        if(fGlarePower != otherCam.fGlarePower)                 fGlarePower = otherCam.fGlarePower;
        if(iGlareRayCount != otherCam.iGlareRayCount)           iGlareRayCount = otherCam.iGlareRayCount;
        if(fGlareAngle != otherCam.fGlareAngle)                 fGlareAngle = otherCam.fGlareAngle;
        if(fGlareBlur != otherCam.fGlareBlur)                   fGlareBlur = otherCam.fGlareBlur;
        if(fSpectralIntencity != otherCam.fSpectralIntencity)   fSpectralIntencity = otherCam.fSpectralIntencity;
        if(fSpectralShift != otherCam.fSpectralShift)           fSpectralShift = otherCam.fSpectralShift;

        return *this;
    }
}; //struct Camera

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a passes data that is going to be uploaded to the Octane server.
struct Passes {
    bool            bUsePasses;
    RenderPassId    curPassType;

    bool    bBeautyPass;

    bool    bEmittersPass;
    bool    bEnvironmentPass;
    bool    bDiffusePass;
    bool    bDiffuseDirectPass;
    bool    bDiffuseIndirectPass;
    bool    bDiffuseFilterPass;
    bool    bReflectionPass;
    bool    bReflectionDirectPass;
    bool    bReflectionIndirectPass;
    bool    bReflectionFilterPass;
    bool    bRefractionPass;
    bool    bRefractionFilterPass;
    bool    bTransmissionPass;
    bool    bTransmissionFilterPass;
    bool    bSubsurfScatteringPass;
    bool    bPostProcessingPass;

    bool    bLayerShadowsPass;
    bool    bLayerBlackShadowsPass;
    bool    bLayerColorShadowsPass;
    bool    bLayerReflectionsPass;

    bool    bAmbientLightPass;
    bool    bSunlightPass;
    bool    bLight1Pass;
    bool    bLight2Pass;
    bool    bLight3Pass;
    bool    bLight4Pass;
    bool    bLight5Pass;
    bool    bLight6Pass;
    bool    bLight7Pass;
    bool    bLight8Pass;

    bool    bBackinGroupIdPass;
    bool    bOpacityPass;
    bool    bRoughnessPass;
    bool    bIorPass;
    bool    bDiffuseFilterInfoPass;
    bool    bReflectionFilterInfoPass;
    bool    bRefractionFilterInfoPass;
    bool    bTransmissionFilterInfoPass;

    bool    bGeomNormalsPass;
    bool    bShadingNormalsPass;
    bool    bVertexNormalsPass;
    bool    bTangentNormalsPass;
    bool    bPositionPass;
    bool    bZdepthPass;
    bool    bMaterialIdPass;
    bool    bUVCoordinatesPass;
    bool    bTangentsPass;
    bool    bWireframePass;
    bool    bMotionVectorPass;
    bool    bObjectIdPass;
    bool    bLayerIdPass;
    bool    bLayerMaskPass;
    bool    bLightPassIdPass;

    bool    bAOPass;

    int32_t iMaxSamples;
    bool    iSamplingMode;
    bool    bPassesRaw;
    bool    bPostProcEnvironment;
    bool    bBump;
    bool    bAoAlphaShadows;
    float   fZdepthMax;
    float   fUVMax;
    float   fMaxSpeed;
    float   fAODistance;
    float   fOpacityThreshold;

    inline Passes() : bUsePasses(false), curPassType((RenderPassId)-1) {}
    inline bool operator==(const Passes& otherPasses) {
        return (curPassType == otherPasses.curPassType
                && bUsePasses == otherPasses.bUsePasses

                && bBeautyPass == otherPasses.bBeautyPass

                && bEmittersPass == otherPasses.bEmittersPass
                && bEnvironmentPass == otherPasses.bEnvironmentPass
                && bDiffusePass == otherPasses.bDiffusePass
                && bDiffuseDirectPass == otherPasses.bDiffuseDirectPass
                && bDiffuseIndirectPass == otherPasses.bDiffuseIndirectPass
                && bDiffuseFilterPass == otherPasses.bDiffuseFilterPass
                && bReflectionPass == otherPasses.bReflectionPass
                && bReflectionDirectPass == otherPasses.bReflectionDirectPass
                && bReflectionIndirectPass == otherPasses.bReflectionIndirectPass
                && bReflectionFilterPass == otherPasses.bReflectionFilterPass
                && bRefractionPass == otherPasses.bRefractionPass
                && bRefractionFilterPass == otherPasses.bRefractionFilterPass
                && bTransmissionPass == otherPasses.bTransmissionPass
                && bTransmissionFilterPass == otherPasses.bTransmissionFilterPass
                && bSubsurfScatteringPass == otherPasses.bSubsurfScatteringPass
                && bPostProcessingPass == otherPasses.bPostProcessingPass

                && bLayerShadowsPass == otherPasses.bLayerShadowsPass
                && bLayerBlackShadowsPass == otherPasses.bLayerBlackShadowsPass
                && bLayerColorShadowsPass == otherPasses.bLayerColorShadowsPass
                && bLayerReflectionsPass == otherPasses.bLayerReflectionsPass

                && bAmbientLightPass == otherPasses.bAmbientLightPass
                && bSunlightPass == otherPasses.bSunlightPass
                && bLight1Pass == otherPasses.bLight1Pass
                && bLight2Pass == otherPasses.bLight2Pass
                && bLight3Pass == otherPasses.bLight3Pass
                && bLight4Pass == otherPasses.bLight4Pass
                && bLight5Pass == otherPasses.bLight5Pass
                && bLight6Pass == otherPasses.bLight6Pass
                && bLight7Pass == otherPasses.bLight7Pass
                && bLight8Pass == otherPasses.bLight8Pass

                && bBackinGroupIdPass == otherPasses.bBackinGroupIdPass
                && bOpacityPass == otherPasses.bOpacityPass
                && bRoughnessPass == otherPasses.bRoughnessPass
                && bIorPass == otherPasses.bIorPass
                && bDiffuseFilterInfoPass == otherPasses.bDiffuseFilterInfoPass
                && bReflectionFilterInfoPass == otherPasses.bReflectionFilterInfoPass
                && bRefractionFilterInfoPass == otherPasses.bRefractionFilterInfoPass
                && bTransmissionFilterInfoPass == otherPasses.bTransmissionFilterInfoPass

                && bGeomNormalsPass == otherPasses.bGeomNormalsPass
                && bShadingNormalsPass == otherPasses.bShadingNormalsPass
                && bVertexNormalsPass == otherPasses.bVertexNormalsPass
                && bTangentNormalsPass == otherPasses.bTangentNormalsPass
                && bPositionPass == otherPasses.bPositionPass
                && bZdepthPass == otherPasses.bZdepthPass
                && bMaterialIdPass == otherPasses.bMaterialIdPass
                && bUVCoordinatesPass == otherPasses.bUVCoordinatesPass
                && bTangentsPass == otherPasses.bTangentsPass
                && bWireframePass == otherPasses.bWireframePass
                && bMotionVectorPass == otherPasses.bMotionVectorPass
                && bObjectIdPass == otherPasses.bObjectIdPass
                && bLayerIdPass == otherPasses.bLayerIdPass
                && bLayerMaskPass == otherPasses.bLayerMaskPass
                && bLightPassIdPass == otherPasses.bLightPassIdPass

                && bAOPass == otherPasses.bAOPass

                && iMaxSamples == otherPasses.iMaxSamples
                && iSamplingMode == otherPasses.iSamplingMode
                && bPassesRaw == otherPasses.bPassesRaw
                && bPostProcEnvironment == otherPasses.bPostProcEnvironment
                && bBump == otherPasses.bBump
                && bAoAlphaShadows == otherPasses.bAoAlphaShadows
                && fZdepthMax == otherPasses.fZdepthMax
                && fUVMax == otherPasses.fUVMax
                && fMaxSpeed == otherPasses.fMaxSpeed
                && fAODistance == otherPasses.fAODistance
                && fOpacityThreshold == otherPasses.fOpacityThreshold);
    }
    inline Passes& operator=(const Passes& otherPasses) {
        if(curPassType != otherPasses.curPassType)                                  curPassType = otherPasses.curPassType;
        if(bUsePasses != otherPasses.bUsePasses)                                    bUsePasses = otherPasses.bUsePasses;

        if(bBeautyPass != otherPasses.bBeautyPass)                                  bBeautyPass = otherPasses.bBeautyPass;

        if(bEmittersPass != otherPasses.bEmittersPass)                              bEmittersPass = otherPasses.bEmittersPass;
        if(bEnvironmentPass != otherPasses.bEnvironmentPass)                        bEnvironmentPass = otherPasses.bEnvironmentPass;
        if(bDiffusePass != otherPasses.bDiffusePass)                                bDiffusePass = otherPasses.bDiffusePass;
        if(bDiffuseDirectPass != otherPasses.bDiffuseDirectPass)                    bDiffuseDirectPass = otherPasses.bDiffuseDirectPass;
        if(bDiffuseIndirectPass != otherPasses.bDiffuseIndirectPass)                bDiffuseIndirectPass = otherPasses.bDiffuseIndirectPass;
        if(bDiffuseFilterPass != otherPasses.bDiffuseFilterPass)                    bDiffuseFilterPass = otherPasses.bDiffuseFilterPass;
        if(bReflectionPass != otherPasses.bReflectionPass)                          bReflectionPass = otherPasses.bReflectionPass;
        if(bReflectionDirectPass != otherPasses.bReflectionDirectPass)              bReflectionDirectPass = otherPasses.bReflectionDirectPass;
        if(bReflectionIndirectPass != otherPasses.bReflectionIndirectPass)          bReflectionIndirectPass = otherPasses.bReflectionIndirectPass;
        if(bReflectionFilterPass != otherPasses.bReflectionFilterPass)              bReflectionFilterPass = otherPasses.bReflectionFilterPass;
        if(bRefractionPass != otherPasses.bRefractionPass)                          bRefractionPass = otherPasses.bRefractionPass;
        if(bRefractionFilterPass != otherPasses.bRefractionFilterPass)              bRefractionFilterPass = otherPasses.bRefractionFilterPass;
        if(bTransmissionPass != otherPasses.bTransmissionPass)                      bTransmissionPass = otherPasses.bTransmissionPass;
        if(bTransmissionFilterPass != otherPasses.bTransmissionFilterPass)          bTransmissionFilterPass = otherPasses.bTransmissionFilterPass;
        if(bSubsurfScatteringPass != otherPasses.bSubsurfScatteringPass)            bSubsurfScatteringPass = otherPasses.bSubsurfScatteringPass;
        if(bPostProcessingPass != otherPasses.bPostProcessingPass)                  bPostProcessingPass = otherPasses.bPostProcessingPass;

        if(bLayerShadowsPass != otherPasses.bLayerShadowsPass)                      bLayerShadowsPass = otherPasses.bLayerShadowsPass;
        if(bLayerBlackShadowsPass != otherPasses.bLayerBlackShadowsPass)            bLayerBlackShadowsPass = otherPasses.bLayerBlackShadowsPass;
        if(bLayerColorShadowsPass != otherPasses.bLayerColorShadowsPass)            bLayerColorShadowsPass = otherPasses.bLayerColorShadowsPass;
        if(bLayerReflectionsPass != otherPasses.bLayerReflectionsPass)              bLayerReflectionsPass = otherPasses.bLayerReflectionsPass;

        if(bAmbientLightPass != otherPasses.bAmbientLightPass)                      bAmbientLightPass = otherPasses.bAmbientLightPass;
        if(bSunlightPass != otherPasses.bSunlightPass)                              bSunlightPass = otherPasses.bSunlightPass;
        if(bLight1Pass != otherPasses.bLight1Pass)                                  bLight1Pass = otherPasses.bLight1Pass;
        if(bLight2Pass != otherPasses.bLight2Pass)                                  bLight2Pass = otherPasses.bLight2Pass;
        if(bLight3Pass != otherPasses.bLight3Pass)                                  bLight3Pass = otherPasses.bLight3Pass;
        if(bLight4Pass != otherPasses.bLight4Pass)                                  bLight4Pass = otherPasses.bLight4Pass;
        if(bLight5Pass != otherPasses.bLight5Pass)                                  bLight5Pass = otherPasses.bLight5Pass;
        if(bLight6Pass != otherPasses.bLight6Pass)                                  bLight6Pass = otherPasses.bLight6Pass;
        if(bLight7Pass != otherPasses.bLight7Pass)                                  bLight7Pass = otherPasses.bLight7Pass;
        if(bLight8Pass != otherPasses.bLight8Pass)                                  bLight8Pass = otherPasses.bLight8Pass;

        if(bBackinGroupIdPass != otherPasses.bBackinGroupIdPass)                    bBackinGroupIdPass = otherPasses.bBackinGroupIdPass;
        if(bOpacityPass != otherPasses.bOpacityPass)                                bOpacityPass = otherPasses.bOpacityPass;
        if(bRoughnessPass != otherPasses.bRoughnessPass)                            bRoughnessPass = otherPasses.bRoughnessPass;
        if(bIorPass != otherPasses.bIorPass)                                        bIorPass = otherPasses.bIorPass;
        if(bDiffuseFilterInfoPass != otherPasses.bDiffuseFilterInfoPass)            bDiffuseFilterInfoPass = otherPasses.bDiffuseFilterInfoPass;
        if(bReflectionFilterInfoPass != otherPasses.bReflectionFilterInfoPass)      bReflectionFilterInfoPass = otherPasses.bReflectionFilterInfoPass;
        if(bRefractionFilterInfoPass != otherPasses.bRefractionFilterInfoPass)      bRefractionFilterInfoPass = otherPasses.bRefractionFilterInfoPass;
        if(bTransmissionFilterInfoPass != otherPasses.bTransmissionFilterInfoPass)  bTransmissionFilterInfoPass = otherPasses.bTransmissionFilterInfoPass;

        if(bGeomNormalsPass != otherPasses.bGeomNormalsPass)                        bGeomNormalsPass = otherPasses.bGeomNormalsPass;
        if(bShadingNormalsPass != otherPasses.bShadingNormalsPass)                  bShadingNormalsPass = otherPasses.bShadingNormalsPass;
        if(bVertexNormalsPass != otherPasses.bVertexNormalsPass)                    bVertexNormalsPass = otherPasses.bVertexNormalsPass;
        if(bTangentNormalsPass != otherPasses.bTangentNormalsPass)                  bTangentNormalsPass = otherPasses.bTangentNormalsPass;
        if(bPositionPass != otherPasses.bPositionPass)                              bPositionPass = otherPasses.bPositionPass;
        if(bZdepthPass != otherPasses.bZdepthPass)                                  bZdepthPass = otherPasses.bZdepthPass;
        if(bMaterialIdPass != otherPasses.bMaterialIdPass)                          bMaterialIdPass = otherPasses.bMaterialIdPass;
        if(bUVCoordinatesPass != otherPasses.bUVCoordinatesPass)                    bUVCoordinatesPass = otherPasses.bUVCoordinatesPass;
        if(bTangentsPass != otherPasses.bTangentsPass)                              bTangentsPass = otherPasses.bTangentsPass;
        if(bWireframePass != otherPasses.bWireframePass)                            bWireframePass = otherPasses.bWireframePass;
        if(bMotionVectorPass != otherPasses.bMotionVectorPass)                      bMotionVectorPass = otherPasses.bMotionVectorPass;
        if(bObjectIdPass != otherPasses.bObjectIdPass)                              bObjectIdPass = otherPasses.bObjectIdPass;
        if(bLayerIdPass != otherPasses.bLayerIdPass)                                bLayerIdPass = otherPasses.bLayerIdPass;
        if(bLayerMaskPass != otherPasses.bLayerMaskPass)                            bLayerMaskPass = otherPasses.bLayerMaskPass;
        if(bLightPassIdPass != otherPasses.bLightPassIdPass)                        bLightPassIdPass = otherPasses.bLightPassIdPass;

        if(bAOPass != otherPasses.bAOPass)                                          bAOPass = otherPasses.bAOPass;

        if(iMaxSamples != otherPasses.iMaxSamples)                                  iMaxSamples = otherPasses.iMaxSamples;
        if(iSamplingMode != otherPasses.iSamplingMode)                  iSamplingMode = otherPasses.iSamplingMode;
        if(bPassesRaw != otherPasses.bPassesRaw)                                    bPassesRaw = otherPasses.bPassesRaw;
        if(bPostProcEnvironment != otherPasses.bPostProcEnvironment)                bPostProcEnvironment = otherPasses.bPostProcEnvironment;
        if(bBump != otherPasses.bBump)                                              bBump = otherPasses.bBump;
        if(bAoAlphaShadows != otherPasses.bAoAlphaShadows)                              bAoAlphaShadows = otherPasses.bAoAlphaShadows;
        if(fZdepthMax != otherPasses.fZdepthMax)                                    fZdepthMax = otherPasses.fZdepthMax;
        if(fUVMax != otherPasses.fUVMax)                                            fUVMax = otherPasses.fUVMax;
        if(fMaxSpeed != otherPasses.fMaxSpeed)                                      fMaxSpeed = otherPasses.fMaxSpeed;
        if(fAODistance != otherPasses.fAODistance)                                  fAODistance = otherPasses.fAODistance;
        if(fOpacityThreshold != otherPasses.fOpacityThreshold)                                        fOpacityThreshold = otherPasses.fOpacityThreshold;

        return *this;
    }
}; //struct Passes

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Kernel and some global settings
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a kernel data that is going to be uploaded to the Octane server.
struct Kernel {
    enum KernelType {
        DEFAULT = 0,
        DIRECT_LIGHT,
        PATH_TRACE,
        PMC,
        INFO_CHANNEL,
        NONE
    };
    enum DirectLightMode {
        GI_NONE,
        GI_AMBIENT,
        GI_SAMPLE_AMBIENT,
        GI_AMBIENT_OCCLUSION,
        GI_DIFFUSE
    };
    enum MBAlignmentType {
        BEFORE = 1,
        SYMMETRIC,
        AFTER
    };
    enum LayersMode {
        NORMAL = 0,
        HIDE_INACTIVE,
        ONLY_SIDE_EFFECTS
    };

    KernelType      type;

    float           fShutterTime;
    MBAlignmentType mbAlignment;

    //COMMON
    int32_t         iMaxSamples;
    float           fFilterSize;
    float           fRayEpsilon;
    bool            bAlphaChannel;
    float           fPathTermPower;

    //PATH_TRACE + PMC + DIRECT_LIGHT
    bool            bAlphaShadows;
    bool            bKeepEnvironment;

    //PATH_TRACE + PMC
    float           fCausticBlur;
    int32_t         iMaxDiffuseDepth, iMaxGlossyDepth;
    float           fGIClamp;

    //DIRECT_LIGHT + INFO_CHANNEL
    float           fAODist;

    //PATH_TRACE + DIRECT_LIGHT
    float           fCoherentRatio;
    bool            bStaticNoise;
    bool            bDeepImageEnable;
    int             iMaxDepthSamples;
    float           fDepthTolerance;

    //PATH_TRACE + DIRECT_LIGHT + INFO_CHANNEL
    int             iParallelSamples;
    int             iMaxTileSamples;
    bool            bMinimizeNetTraffic;

    //DIRECT_LIGHT
    int32_t         iDiffuseDepth;
    int32_t         iGlossyDepth;
    int32_t         iSpecularDepth;
    DirectLightMode GIMode;
    std::string     sAoTexture;

    //PATH_TRACE

    //PMC
    float           fExploration;
    float           fDLImportance;
    int32_t         iMaxRejects;
    int32_t         iParallelism;
    int             iWorkChunkSize;

    //INFO_CHANNEL
    InfoChannelType infoChannelType;
    float           fZdepthMax;
    float           fUVMax;
    bool            iSamplingMode;
    float           fMaxSpeed;
    bool            bAoAlphaShadows;
    float           fOpacityThreshold;
    bool            bBumpNormalMapping;
    bool            bBkFaceHighlight;

    // Object layers
    bool            bLayersEnable;
    int32_t         iLayersCurrent;
    bool            bLayersInvert;
    LayersMode      layersMode;

    inline Kernel() : type(NONE) {}
    inline bool operator==(const Kernel& otherKernel) {
        return (type == otherKernel.type

                && iMaxSamples == otherKernel.iMaxSamples
                && fFilterSize == otherKernel.fFilterSize
                && fRayEpsilon == otherKernel.fRayEpsilon
                && bAlphaChannel == otherKernel.bAlphaChannel
                && fPathTermPower == otherKernel.fPathTermPower

                && bAlphaShadows == otherKernel.bAlphaShadows
                && bKeepEnvironment == otherKernel.bKeepEnvironment

                && fCausticBlur == otherKernel.fCausticBlur
                && iMaxDiffuseDepth == otherKernel.iMaxDiffuseDepth
                && iMaxGlossyDepth == otherKernel.iMaxGlossyDepth
                && fGIClamp == otherKernel.fGIClamp

                && fAODist == otherKernel.fAODist

                && fCoherentRatio == otherKernel.fCoherentRatio
                && bStaticNoise == otherKernel.bStaticNoise
                && bDeepImageEnable == otherKernel.bDeepImageEnable
                && iMaxDepthSamples == otherKernel.iMaxDepthSamples
                && fDepthTolerance == otherKernel.fDepthTolerance

                && iParallelSamples == otherKernel.iParallelSamples
                && iMaxTileSamples == otherKernel.iMaxTileSamples
                && bMinimizeNetTraffic == otherKernel.bMinimizeNetTraffic

                && iDiffuseDepth == otherKernel.iDiffuseDepth
                && iGlossyDepth == otherKernel.iGlossyDepth
                && iSpecularDepth == otherKernel.iSpecularDepth
                && GIMode == otherKernel.GIMode
                && sAoTexture == otherKernel.sAoTexture

                && fExploration == otherKernel.fExploration
                && fDLImportance == otherKernel.fDLImportance
                && iMaxRejects == otherKernel.iMaxRejects
                && iParallelism == otherKernel.iParallelism
                && iWorkChunkSize == otherKernel.iWorkChunkSize

                && infoChannelType == otherKernel.infoChannelType
                && fZdepthMax == otherKernel.fZdepthMax
                && fUVMax == otherKernel.fUVMax
                && iSamplingMode == otherKernel.iSamplingMode
                && fMaxSpeed == otherKernel.fMaxSpeed
                && bAoAlphaShadows == otherKernel.bAoAlphaShadows
                && fOpacityThreshold == otherKernel.fOpacityThreshold
                && bBumpNormalMapping == otherKernel.bBumpNormalMapping
                && bBkFaceHighlight == otherKernel.bBkFaceHighlight

                && bLayersEnable == otherKernel.bLayersEnable
                && iLayersCurrent == otherKernel.iLayersCurrent
                && bLayersInvert == otherKernel.bLayersInvert
                && layersMode == otherKernel.layersMode

                && fShutterTime == otherKernel.fShutterTime
                && mbAlignment == otherKernel.mbAlignment);
    }
    inline Kernel& operator=(const Kernel& otherKernel) {
        if(type != otherKernel.type)                                type = otherKernel.type;

        if(iMaxSamples != otherKernel.iMaxSamples)                  iMaxSamples = otherKernel.iMaxSamples;
        if(fFilterSize != otherKernel.fFilterSize)                  fFilterSize = otherKernel.fFilterSize;
        if(fRayEpsilon != otherKernel.fRayEpsilon)                  fRayEpsilon = otherKernel.fRayEpsilon;
        if(bAlphaChannel != otherKernel.bAlphaChannel)              bAlphaChannel = otherKernel.bAlphaChannel;
        if(fPathTermPower != otherKernel.fPathTermPower)            fPathTermPower = otherKernel.fPathTermPower;

        if(bAlphaShadows != otherKernel.bAlphaShadows)              bAlphaShadows = otherKernel.bAlphaShadows;
        if(bKeepEnvironment != otherKernel.bKeepEnvironment)        bKeepEnvironment = otherKernel.bKeepEnvironment;

        if(fCausticBlur != otherKernel.fCausticBlur)                fCausticBlur = otherKernel.fCausticBlur;
        if(iMaxDiffuseDepth != otherKernel.iMaxDiffuseDepth)        iMaxDiffuseDepth = otherKernel.iMaxDiffuseDepth;
        if(iMaxGlossyDepth != otherKernel.iMaxGlossyDepth)          iMaxGlossyDepth = otherKernel.iMaxGlossyDepth;
        if(fGIClamp != otherKernel.fGIClamp)                        fGIClamp = otherKernel.fGIClamp;

        if(fAODist != otherKernel.fAODist)                          fAODist = otherKernel.fAODist;

        if(fCoherentRatio != otherKernel.fCoherentRatio)            fCoherentRatio = otherKernel.fCoherentRatio;
        if(bStaticNoise != otherKernel.bStaticNoise)                bStaticNoise = otherKernel.bStaticNoise;
        if(bDeepImageEnable != otherKernel.bDeepImageEnable)        bDeepImageEnable = otherKernel.bDeepImageEnable;
        if(iMaxDepthSamples != otherKernel.iMaxDepthSamples)        iMaxDepthSamples = otherKernel.iMaxDepthSamples;
        if(fDepthTolerance != otherKernel.fDepthTolerance)          fDepthTolerance = otherKernel.fDepthTolerance;

        if(iParallelSamples != otherKernel.iParallelSamples)        iParallelSamples = otherKernel.iParallelSamples;
        if(iMaxTileSamples != otherKernel.iMaxTileSamples)          iMaxTileSamples = otherKernel.iMaxTileSamples;
        if(bMinimizeNetTraffic != otherKernel.bMinimizeNetTraffic)  bMinimizeNetTraffic = otherKernel.bMinimizeNetTraffic;

        if(iDiffuseDepth != otherKernel.iDiffuseDepth)              iDiffuseDepth = otherKernel.iDiffuseDepth;
        if(iGlossyDepth != otherKernel.iGlossyDepth)                iGlossyDepth = otherKernel.iGlossyDepth;
        if(iSpecularDepth != otherKernel.iSpecularDepth)            iSpecularDepth = otherKernel.iSpecularDepth;
        if(GIMode != otherKernel.GIMode)                            GIMode = otherKernel.GIMode;
        if(sAoTexture != otherKernel.sAoTexture)                    sAoTexture = otherKernel.sAoTexture;

        if(fExploration != otherKernel.fExploration)                fExploration = otherKernel.fExploration;
        if(fDLImportance != otherKernel.fDLImportance)              fDLImportance = otherKernel.fDLImportance;
        if(iMaxRejects != otherKernel.iMaxRejects)                  iMaxRejects = otherKernel.iMaxRejects;
        if(iParallelism != otherKernel.iParallelism)                iParallelism = otherKernel.iParallelism;
        if(iWorkChunkSize != otherKernel.iWorkChunkSize)            iWorkChunkSize = otherKernel.iWorkChunkSize;

        if(infoChannelType != otherKernel.infoChannelType)          infoChannelType = otherKernel.infoChannelType;
        if(fZdepthMax != otherKernel.fZdepthMax)                    fZdepthMax = otherKernel.fZdepthMax;
        if(fUVMax != otherKernel.fUVMax)                            fUVMax = otherKernel.fUVMax;
        if(iSamplingMode != otherKernel.iSamplingMode)              iSamplingMode = otherKernel.iSamplingMode;
        if(fMaxSpeed != otherKernel.fMaxSpeed)                      fMaxSpeed = otherKernel.fMaxSpeed;
        if(bAoAlphaShadows != otherKernel.bAoAlphaShadows)          bAoAlphaShadows = otherKernel.bAoAlphaShadows;
        if(fOpacityThreshold != otherKernel.fOpacityThreshold)                        fOpacityThreshold = otherKernel.fOpacityThreshold;
        if(bBumpNormalMapping != otherKernel.bBumpNormalMapping)    bBumpNormalMapping = otherKernel.bBumpNormalMapping;
        if(bBkFaceHighlight != otherKernel.bBkFaceHighlight)        bBkFaceHighlight = otherKernel.bBkFaceHighlight;

        if(bLayersEnable != otherKernel.bLayersEnable)              bLayersEnable = otherKernel.bLayersEnable;
        if(iLayersCurrent != otherKernel.iLayersCurrent)            iLayersCurrent = otherKernel.iLayersCurrent;
        if(bLayersInvert != otherKernel.bLayersInvert)              bLayersInvert = otherKernel.bLayersInvert;
        if(layersMode != otherKernel.layersMode)            layersMode = otherKernel.layersMode;

        if(fShutterTime != otherKernel.fShutterTime)                fShutterTime = otherKernel.fShutterTime;
        if(mbAlignment != otherKernel.mbAlignment)                  mbAlignment = otherKernel.mbAlignment;

        return *this;
    }
}; //struct Kernel

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Environment
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a environment data that is going to be uploaded to the Octane server.
struct Environment {
    enum EnvType {
        TEXTURE,
        DAYLIGHT,
        NONE
    };
    enum DaylightType {
        DIRECTION,
        DAYLIGHT_SYSTEM
    };
    enum DaylightModel {
        OLD,
        NEW
    };

    EnvType         type;
                                            
    string          sTexture;
    string          sMedium;
    float           fMediumRadius;
    bool            bImportanceSampling;
    bool            bVisibleBackplate;
    bool            bVisibleReflections;
    bool            bVisibleRefractions;
    DaylightType    daylightType;
    float_3         f3SunVector;
    float           fPower;
    float           fLongitude;
    float           fLatitude;
    float           fHour;
    int32_t         iMonth;
    int32_t         iDay;
    int32_t         iGMTOffset;
    float           fTurbidity;
    float           fNorthOffset;
    DaylightModel   model;
    float           fSunSize;
                                            
    float_3         f3SkyColor;
    float_3         f3SunsetColor;
    float_3         f3GroundColor;

    float           fGroundStartAngle;
    float           fGroundBlendAngle;

    inline Environment() :  type                    (NONE),
                            sTexture                (""),
                            sMedium                 (""),
                            fMediumRadius           (1.0f),
                            bImportanceSampling     (true),
                            bVisibleBackplate       (false),
                            bVisibleReflections     (false),
                            bVisibleRefractions     (false),
                            daylightType            (DIRECTION),
                            fPower                  (1.0f),
                            fLongitude              (4.4667f),
                            fLatitude               (50.7667f),
                            fHour                   (14),
                            iMonth                  (3),
                            iDay                    (1),
                            iGMTOffset              (0),
                            fTurbidity              (2.2f),
                            fNorthOffset            (0),
                            model                   (NEW),
                            fSunSize                (1.0f)  {
        f3SunVector.x = 0.0f;
        f3SunVector.y = 1.0f;
        f3SunVector.z = 0.0f;

        f3SkyColor.x = 0.05f;
        f3SkyColor.y = 0.3f;
        f3SkyColor.z = 1.0f;

        f3SunsetColor.x = 0.6f;
        f3SunsetColor.y = 0.12f;
        f3SunsetColor.z = 0.02;

        f3GroundColor.x = 0.0f;
        f3GroundColor.y = 0.0f;
        f3GroundColor.z = 0.0f;

        fGroundStartAngle = 90.0f;
		fGroundStartAngle = 5.0f;
    }

    inline bool operator==(const Environment& otherEnv) {
        return (type == otherEnv.type

                && sTexture == otherEnv.sTexture
                && sMedium == otherEnv.sMedium
                && fMediumRadius == otherEnv.fMediumRadius
                && bImportanceSampling == otherEnv.bImportanceSampling
                && bVisibleBackplate == otherEnv.bVisibleBackplate
                && bVisibleReflections == otherEnv.bVisibleReflections
                && bVisibleRefractions == otherEnv.bVisibleRefractions
                && daylightType == otherEnv.daylightType
                && f3SunVector == otherEnv.f3SunVector
                && fPower == otherEnv.fPower
                && fLongitude == otherEnv.fLongitude
                && fLatitude == otherEnv.fLatitude
                && fHour == otherEnv.fHour
                && iMonth == otherEnv.iMonth
                && iDay == otherEnv.iDay
                && iGMTOffset == otherEnv.iGMTOffset
                && fTurbidity == otherEnv.fTurbidity
                && fNorthOffset == otherEnv.fNorthOffset
                && fSunSize == otherEnv.fSunSize

                && fGroundStartAngle == otherEnv.fGroundStartAngle
                && fGroundBlendAngle == otherEnv.fGroundBlendAngle

                && f3SkyColor == otherEnv.f3SkyColor
                && f3SunsetColor == otherEnv.f3SunsetColor
                && f3GroundColor == otherEnv.f3GroundColor);
    }
    inline Environment& operator=(const Environment& otherEnv) {
        if(type != otherEnv.type)                                type = otherEnv.type;

        if(sTexture != otherEnv.sTexture)                       sTexture = otherEnv.sTexture;
        if(sMedium != otherEnv.sMedium)                         sMedium = otherEnv.sMedium;
        if(fMediumRadius != otherEnv.fMediumRadius)             fMediumRadius = otherEnv.fMediumRadius;
        if(bImportanceSampling != otherEnv.bImportanceSampling) bImportanceSampling = otherEnv.bImportanceSampling;
        if(bVisibleBackplate != otherEnv.bVisibleBackplate)     bVisibleBackplate = otherEnv.bVisibleBackplate;
        if(bVisibleReflections != otherEnv.bVisibleReflections) bVisibleReflections = otherEnv.bVisibleReflections;
        if(bVisibleRefractions != otherEnv.bVisibleRefractions) bVisibleRefractions = otherEnv.bVisibleRefractions;
        if(daylightType != otherEnv.daylightType)               daylightType = otherEnv.daylightType;
        if(f3SunVector != otherEnv.f3SunVector)                 f3SunVector = otherEnv.f3SunVector;
        if(fPower != otherEnv.fPower)                           fPower = otherEnv.fPower;
        if(fLongitude != otherEnv.fLongitude)                   fLongitude = otherEnv.fLongitude;
        if(fLatitude != otherEnv.fLatitude)                     fLatitude = otherEnv.fLatitude;
        if(fHour != otherEnv.fHour)                             fHour = otherEnv.fHour;
        if(iMonth != otherEnv.iMonth)                           iMonth = otherEnv.iMonth;
        if(iDay != otherEnv.iDay)                               iDay = otherEnv.iDay;
        if(iGMTOffset != otherEnv.iGMTOffset)                   iGMTOffset = otherEnv.iGMTOffset;
        if(fTurbidity != otherEnv.fTurbidity)                   fTurbidity = otherEnv.fTurbidity;
        if(fNorthOffset != otherEnv.fNorthOffset)               fNorthOffset = otherEnv.fNorthOffset;
        if(fSunSize != otherEnv.fSunSize)                       fSunSize = otherEnv.fSunSize;
        if(fGroundStartAngle != otherEnv.fGroundStartAngle)     fGroundStartAngle = otherEnv.fGroundStartAngle;
        if(fGroundBlendAngle != otherEnv.fGroundBlendAngle)     fGroundBlendAngle = otherEnv.fGroundBlendAngle;
        if(f3SkyColor != otherEnv.f3SkyColor)                   f3SkyColor = otherEnv.f3SkyColor;
        if(f3SunsetColor != otherEnv.f3SunsetColor)             f3SunsetColor = otherEnv.f3SunsetColor;
        if(f3GroundColor != otherEnv.f3GroundColor)             f3GroundColor = otherEnv.f3GroundColor;

        return *this;
    }
}; //struct Environment


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// NODE BASE
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
struct OctaneNodeBase {
    string sName;
    Octane::NodeType nodeType;

    OctaneNodeBase(Octane::NodeType _nodeType) : nodeType(_nodeType) {}
    virtual ~OctaneNodeBase() {}
}; //struct OctaneNodeBase


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a diffuse material data that is going to be uploaded to the Octane server.
struct OctaneDiffuseMaterial : public OctaneNodeBase {
    string          sDiffuse;
    ComplexValue    diffuseDefaultVal;
    string          sTransmission;
    ComplexValue    transmissionDefaultVal;
    string          sBump;
    ComplexValue    bumpDefaultVal;
    string          sNormal;
    ComplexValue    normalDefaultVal;
    string          sOpacity;
    ComplexValue    opacityDefaultVal;
    string          sRounding;
    float           fRoundingDefaultVal;
    string          sRoughness;
    ComplexValue    roughnessDefaultVal;
    bool            bSmooth;
    string          sEmission;
    string          sMedium;
    string          sDisplacement;
    bool            bMatte;

    OctaneDiffuseMaterial() : OctaneNodeBase(Octane::NT_MAT_DIFFUSE) {}
}; //struct OctaneDiffuseMaterial

/// The structure holding a glossy material data that is going to be uploaded to the Octane server.
struct OctaneGlossyMaterial : public OctaneNodeBase {
    string          sDiffuse;
    ComplexValue    diffuseDefaultVal;
    string          sSpecular;
    ComplexValue    specularDefaultVal;
    string          sRoughness;
    ComplexValue    roughnessDefaultVal;
    string          sFilmwidth;
    ComplexValue    filmwidthDefaultVal;
    string          sFilmindex;
    float           fFilmindexDefaultVal;
    string          sBump;
    ComplexValue    bumpDefaultVal;
    string          sNormal;
    ComplexValue    normalDefaultVal;
    string          sOpacity;
    ComplexValue    opacityDefaultVal;
    bool            bSmooth;
    string          sIndex;
    float           fIndexDefaultVal;
    string          sRounding;
    float           fRoundingDefaultVal;
    string          sDisplacement;

    OctaneGlossyMaterial() : OctaneNodeBase(Octane::NT_MAT_GLOSSY) {}
}; //struct OctaneGlossyMaterial

/// The structure holding a specular material data that is going to be uploaded to the Octane server.
struct OctaneSpecularMaterial : public OctaneNodeBase {
    string          sReflection;
    ComplexValue    reflectionDefaultVal;
    string          sTransmission;
    ComplexValue    transmissionDefaultVal;
    string          sIndex;
    float           fIndexDefaultVal;
    string          sFilmwidth;
    ComplexValue    filmwidthDefaultVal;
    string          sFilmindex;
    float           fFilmindexDefaultVal;
    string          sBump;
    ComplexValue    bumpDefaultVal;
    string          sNormal;
    ComplexValue    normalDefaultVal;
    string          sOpacity;
    ComplexValue    opacityDefaultVal;
    bool            bSmooth;
    bool            bRefractionAlpha;
    string          sRoughness;
    ComplexValue    roughnessDefaultVal;
    string          sDispersionCoefB;
    float           fDispersionCoefBDefaultVal;
    string          sMedium;
    bool            bFakeShadows;
    string          sRounding;
    float           fRoundingDefaultVal;
    string          sDisplacement;

    OctaneSpecularMaterial() : OctaneNodeBase(Octane::NT_MAT_SPECULAR) {}
}; //struct OctaneSpecularMaterial

/// The structure holding a mix material data that is going to be uploaded to the Octane server.
struct OctaneMixMaterial : public OctaneNodeBase {
    string          sAmount;
    ComplexValue    amountDefaultVal;
    string          sMaterial1;
    string          sMaterial2;
    string          sDisplacement;

    OctaneMixMaterial() : OctaneNodeBase(Octane::NT_MAT_MIX) {}
}; //struct OctaneMixMaterial

/// The structure holding a portal material data that is going to be uploaded to the Octane server.
struct OctanePortalMaterial : public OctaneNodeBase {
    bool    bEnabled;

    OctanePortalMaterial() : OctaneNodeBase(Octane::NT_MAT_PORTAL) {}
}; //struct OctanePortalMaterial


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a greycolor texture data that is going to be uploaded to the Octane server.
struct OctaneFloatTexture : public OctaneNodeBase {
    float fValue;

    OctaneFloatTexture() : OctaneNodeBase(Octane::NT_TEX_FLOAT) {}
}; //struct OctaneFloatTexture

/// The structure holding a RGB spectrum texture data that is going to be uploaded to the Octane server.
struct OctaneRGBSpectrumTexture : public OctaneNodeBase {
    float_3 f3Value;

    OctaneRGBSpectrumTexture() : OctaneNodeBase(Octane::NT_TEX_RGB) {}
}; //struct OctaneRGBSpectrumTexture

/// The structure holding a gaussian spectrum texture data that is going to be uploaded to the Octane server.
struct OctaneGaussianSpectrumTexture : public OctaneNodeBase {
    string          sWaveLength;
    ComplexValue    waveLengthDefaultVal;
    string          sWidth;
    ComplexValue    widthDefaultVal;
    string          sPower;
    ComplexValue    powerDefaultVal;

    OctaneGaussianSpectrumTexture() : OctaneNodeBase(Octane::NT_TEX_GAUSSIANSPECTRUM) {}
}; //struct OctaneGaussianSpectrumTexture

/// The structure holding a checks texture data that is going to be uploaded to the Octane server.
struct OctaneChecksTexture : public OctaneNodeBase {
    string          sTransform;
    ComplexValue    transformDefaultVal;
    string          sProjection;

    OctaneChecksTexture() : OctaneNodeBase(Octane::NT_TEX_CHECKS) {}
}; //struct OctaneChecksTexture

/// The structure holding a marble texture data that is going to be uploaded to the Octane server.
struct OctaneMarbleTexture : public OctaneNodeBase {
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sOctaves;
    int32_t         iOctavesDefaultVal;
    string          sOmega;
    ComplexValue    omegaDefaultVal;
    string          sVariance;
    ComplexValue    varianceDefaultVal;
    string          sTransform;
    string          sProjection;

    OctaneMarbleTexture() : OctaneNodeBase(Octane::NT_TEX_MARBLE) {}
}; //struct OctaneMarbleTexture

/// The structure holding a ridged fractal texture data that is going to be uploaded to the Octane server.
struct OctaneRidgedFractalTexture : public OctaneNodeBase {
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sOctaves;
    int32_t         iOctavesDefaultVal;
    string          sLacunarity;
    ComplexValue    lacunarityDefaultVal;
    string          sTransform;
    string          sProjection;

    OctaneRidgedFractalTexture() : OctaneNodeBase(Octane::NT_TEX_RGFRACTAL) {}
}; //struct OctaneRidgedFractalTexture

/// The structure holding a saw wave texture data that is going to be uploaded to the Octane server.
struct OctaneSawWaveTexture : public OctaneNodeBase {
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sTransform;
    string          sProjection;

    OctaneSawWaveTexture() : OctaneNodeBase(Octane::NT_TEX_SAWWAVE) {}
}; //struct OctaneSawWaveTexture

/// The structure holding a sine wave texture data that is going to be uploaded to the Octane server.
struct OctaneSineWaveTexture : public OctaneNodeBase {
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sTransform;
    string          sProjection;

    OctaneSineWaveTexture() : OctaneNodeBase(Octane::NT_TEX_SINEWAVE) {}
}; //struct OctaneSineWaveTexture

/// The structure holding a triangle wave texture data that is going to be uploaded to the Octane server.
struct OctaneTriangleWaveTexture : public OctaneNodeBase {
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sTransform;
    string          sProjection;

    OctaneTriangleWaveTexture() : OctaneNodeBase(Octane::NT_TEX_TRIANGLEWAVE) {}
}; //struct OctaneTriangleWaveTexture

/// The structure holding a turbulence texture data that is going to be uploaded to the Octane server.
struct OctaneTurbulenceTexture : public OctaneNodeBase {
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sOffset;
    ComplexValue    offsetDefaultVal;
    string          sOctaves;
    int32_t         iOctavesDefaultVal;
    string          sOmega;
    ComplexValue    omegaDefaultVal;
    string          sGamma;
    float           fGammaDefaultVal;
    bool            bTurbulence;
    bool            bInvert;
    string          sTransform;
    string          sProjection;

    OctaneTurbulenceTexture() : OctaneNodeBase(Octane::NT_TEX_TURBULENCE) {}
}; //struct OctaneTurbulenceTexture

/// The structure holding a clamp texture data that is going to be uploaded to the Octane server.
struct OctaneClampTexture : public OctaneNodeBase {
    string          sInput;
    ComplexValue    inputDefaultVal;
    string          sMin;
    ComplexValue    minDefaultVal;
    string          sMax;
    ComplexValue    maxDefaultVal;

    OctaneClampTexture() : OctaneNodeBase(Octane::NT_TEX_CLAMP) {}
}; //struct OctaneClampTexture

/// The structure holding a cosine mix texture data that is going to be uploaded to the Octane server.
struct OctaneCosineMixTexture : public OctaneNodeBase {
    string          sAmount;
    ComplexValue    amountDefaultVal;
    string          sTexture1;
    string          sTexture2;

    OctaneCosineMixTexture() : OctaneNodeBase(Octane::NT_TEX_COSINEMIX) {}
}; //struct OctaneCosineMixTexture

/// The structure holding an invert texture data that is going to be uploaded to the Octane server.
struct OctaneInvertTexture : public OctaneNodeBase {
    string  sTexture;

    OctaneInvertTexture() : OctaneNodeBase(Octane::NT_TEX_INVERT) {}
}; //struct OctaneInvertTexture

/// The structure holding a mix texture data that is going to be uploaded to the Octane server.
struct OctaneMixTexture : public OctaneNodeBase {
    string          sAmount;
    ComplexValue    amountDefaultVal;
    string          sTexture1;
    ComplexValue    tex1DefaultVal;
    string          sTexture2;
    ComplexValue    tex2DefaultVal;

    OctaneMixTexture() : OctaneNodeBase(Octane::NT_TEX_MIX) {}
}; //struct OctaneMixTexture

/// The structure holding a multiply texture data that is going to be uploaded to the Octane server.
struct OctaneMultiplyTexture : public OctaneNodeBase {
    string  sTexture1;
    string  sTexture2;

    OctaneMultiplyTexture() : OctaneNodeBase(Octane::NT_TEX_MULTIPLY) {}
}; //struct OctaneMultiplyTexture

/// The structure holding a falloff texture data that is going to be uploaded to the Octane server.
struct OctaneFalloffTexture : public OctaneNodeBase {
    string              sMode;
    FalloffTextureMode  modeDefaultVal;
    string              sNormal;
    float               fNormalDefaultVal;
    string              sGrazing;
    float               fGrazingDefaultVal;
    string              sIndex;
    float               fIndexDefaultVal;
    float_3             f3Direction;

    OctaneFalloffTexture() : OctaneNodeBase(Octane::NT_TEX_FALLOFF) {}
}; //struct OctaneFalloffTexture

/// The structure holding a color correct texture data that is going to be uploaded to the Octane server.
struct OctaneColorCorrectTexture : public OctaneNodeBase {
    string          sTexture;
    bool            bInvert;
    string          sBrightness;
    ComplexValue    brightnessDefaultVal;
    string          sGamma;
    float           fGammaDefaultVal;
    string          sHue;
    float           fHueDefaultVal;
    string          sSaturation;
    float           fSaturationDefaultVal;
    string          sContrast;
    float           fContrastDefaultVal;

    OctaneColorCorrectTexture() : OctaneNodeBase(Octane::NT_TEX_COLORCORRECTION) {}
}; //struct OctaneColorCorrectTexture

/// The structure holding image texture databuffer.
struct OctaneImageTextureBuffer {
    OctaneImageTextureBuffer() : pvBufImgData(0) {}
    virtual ~OctaneImageTextureBuffer() {
        clear();
    }
    inline void clear() {
        if(pvBufImgData) {
            if(bBufIsFloat) delete[] (float*)pvBufImgData;
            else delete[] (unsigned char*)pvBufImgData;
            pvBufImgData = nullptr;
        }
    }

    void*           pvBufImgData;
    bool            bBufIsFloat;
    int32_t         iBufWidth;
    int32_t         iBufHeight;
    int32_t         iBufComponents;
}; //struct OctaneImageTextureBuffer

/// The structure holding an image texture data that is going to be uploaded to the Octane server.
struct OctaneImageTexture : public OctaneNodeBase {
    string          sFileName;
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sGamma;
    float           fGammaDefaultVal;
    string          sTransform;
    bool            bInvert;
    string          sProjection;
    string          sBorderMode;
    int32_t         iBorderModeDefaultVal;

    OctaneImageTextureBuffer dataBuffer;

    OctaneImageTexture() : OctaneNodeBase(Octane::NT_TEX_IMAGE) {}
}; //struct OctaneImageTexture

/// The structure holding a float image texture data that is going to be uploaded to the Octane server.
struct OctaneFloatImageTexture : public OctaneNodeBase {
    string          sFileName;
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sGamma;
    float           fGammaDefaultVal;
    string          sTransform;
    bool            bInvert;
    string          sProjection;
    string          sBorderMode;
    int32_t         iBorderModeDefaultVal;

    OctaneImageTextureBuffer dataBuffer;

    OctaneFloatImageTexture() : OctaneNodeBase(Octane::NT_TEX_FLOATIMAGE) {}
}; //struct OctaneFloatImageTexture

/// The structure holding an alpha image texture data that is going to be uploaded to the Octane server.
struct OctaneAlphaImageTexture : public OctaneNodeBase {
    string          sFileName;
    string          sPower;
    ComplexValue    powerDefaultVal;
    string          sGamma;
    float           fGammaDefaultVal;
    string          sTransform;
    bool            bInvert;
    string          sProjection;
    string          sBorderMode;
    int32_t         iBorderModeDefaultVal;

    OctaneImageTextureBuffer dataBuffer;

    OctaneAlphaImageTexture() : OctaneNodeBase(Octane::NT_TEX_ALPHAIMAGE) {}
}; //struct OctaneAlphaImageTexture

/// The structure holding a dirt texture data that is going to be uploaded to the Octane server.
struct OctaneDirtTexture : public OctaneNodeBase {
    string  sStrength;
    float   fStrengthDefaultVal;
    string  sDetails;
    float   fDetailsDefaultVal;
    string  sRadius;
    float   fRadiusDefaultVal;
    string  sTolerance;
    float   fToleranceDefaultVal;
    bool    bInvertNormal;

    OctaneDirtTexture() : OctaneNodeBase(Octane::NT_TEX_DIRT) {}
}; //struct OctaneDirtTexture

/// The structure holding a gradient texture data that is going to be uploaded to the Octane server.
struct OctaneGradientTexture : public OctaneNodeBase {
    string  sTexture;
    string  sInterpolationType;
    int32_t iInterpolationTypeDefaultVal;

    vector<float>  aPosData;
    vector<float>  aColorData;

    OctaneGradientTexture() : OctaneNodeBase(Octane::NT_TEX_GRADIENT) {}
}; //struct OctaneGradientTexture

/// The structure holding a volume ramp texture data that is going to be uploaded to the Octane server.
struct OctaneVolumeRampTexture : public OctaneNodeBase {
    string  sInterpolationType;
    int32_t iInterpolationTypeDefaultVal;
    string  sMaxGridValue;
    float   fMaxGridValueDefaultVal;

    vector<float>  aPosData;
    vector<float>  aColorData;

    OctaneVolumeRampTexture() : OctaneNodeBase(Octane::NT_VOLUME_RAMP) {}
}; //struct OctaneVolumeRampTexture

/// The structure holding a random color texture data that is going to be uploaded to the Octane server.
struct OctaneRandomColorTexture : public OctaneNodeBase {
    string  sSeed;
    int32_t iSeedDefaultVal;

    OctaneRandomColorTexture() : OctaneNodeBase(Octane::NT_TEX_RANDOMCOLOR) {}
}; //struct OctaneRandomColorTexture

/// The structure holding a polygon side texture data that is going to be uploaded to the Octane server.
struct OctanePolygonSideTexture : public OctaneNodeBase {
    bool bInvert;

    OctanePolygonSideTexture() : OctaneNodeBase(Octane::NT_TEX_SIDE) {}
}; //struct OctanePolygonSideTexture

/// The structure holding a noise texture data that is going to be uploaded to the Octane server.
struct OctaneNoiseTexture : public OctaneNodeBase {
    string  sNoiseType;
    int32_t iNoiseTypeDefaultVal;
    string  sOctaves;
    int32_t iOctavesDefaultVal;
    string  sOmega;
    float   fOmegaDefaultVal;
    string  sTransform;
    string  sProjection;
    bool    bInvert;
    string  sGamma;
    float   fGammaDefaultVal;
    string  sContrast;
    float   fContrastDefaultVal;

    OctaneNoiseTexture() : OctaneNodeBase(Octane::NT_TEX_NOISE) {}
}; //struct OctaneNoiseTexture

/// The structure holding a displacement data that is going to be uploaded to the Octane server.
struct OctaneDisplacementTexture : public OctaneNodeBase {
    string  sTexture;
    int32_t iDetailsLevel;
    string  sHeight;
    float   fHeightDefaultVal;
    string  sOffset;
    float   fOffsetDefaultVal;

    OctaneDisplacementTexture() : OctaneNodeBase(Octane::NT_DISPLACEMENT) {}
}; //struct OctaneDisplacementTexture

/// The structure holding a displacement data that is going to be uploaded to the Octane server.
struct OctaneWTexture : public OctaneNodeBase {
    OctaneWTexture() : OctaneNodeBase(Octane::NT_TEX_W) {}
}; //struct OctaneWTexture


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a black body emission data that is going to be uploaded to the Octane server.
struct OctaneBlackBodyEmission : public OctaneNodeBase {
    string          sTextureOrEff;
    ComplexValue    textureOrEffDefaultVal;
    string          sPower;
    float           fPowerDefaultVal;
    bool            bSurfaceBrightness;
    string          sTemperature;
    float           fTemperatureDefaultVal;
    bool            bNormalize;
    string          sDistribution;
    ComplexValue    distributionDefaultVal;
    string          sSamplingRate;
    float           fSamplingRateDefaultVal;
    bool            bCastIllumination;
    string          sLightPassId;
    int32_t         iLightPassIdDefaultVal;

    OctaneBlackBodyEmission() : OctaneNodeBase(Octane::NT_EMIS_BLACKBODY) {}
}; //struct OctaneBlackBodyEmission

/// The structure holding a texture emission data that is going to be uploaded to the Octane server.
struct OctaneTextureEmission : public OctaneNodeBase {
    string          sTextureOrEff;
    ComplexValue    textureOrEffDefaultVal;
    string          sPower;
    float           fPowerDefaultVal;
    bool            bSurfaceBrightness;
    string          sDistribution;
    ComplexValue    distributionDefaultVal;
    string          sSamplingRate;
    float           fSamplingRateDefaultVal;
    bool            bCastIllumination;
    string          sLightPassId;
    int32_t         iLightPassIdDefaultVal;

    OctaneTextureEmission() : OctaneNodeBase(Octane::NT_EMIS_TEXTURE) {}
}; //struct OctaneTextureEmission


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MEDIUMS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding an absorption medium data that is going to be uploaded to the Octane server.
struct OctaneAbsorptionMedium : public OctaneNodeBase {
    string          sAbsorption;
    ComplexValue    absorptionDefaultVal;
    string          sScale;
    float           fScaleDefaultVal;
    bool            bInvertAbsorption;

    OctaneAbsorptionMedium() : OctaneNodeBase(Octane::NT_MED_ABSORPTION) {}
}; //struct OctaneAbsorptionMedium

/// The structure holding a scattering medium data that is going to be uploaded to the Octane server.
struct OctaneScatteringMedium : public OctaneNodeBase {
    string          sAbsorption;
    ComplexValue    absorptionDefaultVal;
    string          sScattering;
    ComplexValue    scatteringDefaultVal;
    string          sPhase;
    float           fPhaseDefaultVal;
    string          sEmission;
    string          sScale;
    float           fScaleDefaultVal;
    bool            bInvertAbsorption;

    OctaneScatteringMedium() : OctaneNodeBase(Octane::NT_MED_SCATTERING) {}
}; //struct OctaneScatteringMedium

/// The structure holding a volume medium data that is going to be uploaded to the Octane server.
struct OctaneVolumeMedium : public OctaneNodeBase {
    string          sScale;
    float           fScaleDefaultVal;
    string          sAbsorption;
    ComplexValue    absorptionDefaultVal;
    string          sAbsorptionRamp;
    bool            bInvertAbsorption;
    string          sScattering;
    ComplexValue    scatteringDefaultVal;
    string          sScatteringRamp;
    string          sPhase;
    float           fPhaseDefaultVal;
    string          sEmission;
    string          sEmissionRamp;
    string          sStepLength;
    float           fStepLengthDefaultVal;

    OctaneVolumeMedium() : OctaneNodeBase(Octane::NT_MED_VOLUME) {}
}; //struct OctaneVolumeMedium


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TRANSFORM
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a rotation transform data that is going to be uploaded to the Octane server.
struct OctaneRotationTransform : public OctaneNodeBase {
    string  sRotation;
    float_3 f3RotationDefaultVal;
    string  sRotationOrder;
    int32_t iRotationOrderDefaultVal;

    OctaneRotationTransform() : OctaneNodeBase(Octane::NT_TRANSFORM_ROTATION) {}
}; //struct OctaneRotationTransform

/// The structure holding a scale transform data that is going to be uploaded to the Octane server.
struct OctaneScaleTransform : public OctaneNodeBase {
    string  sScale;
    float_3 f3ScaleDefaultVal;

    OctaneScaleTransform() : OctaneNodeBase(Octane::NT_TRANSFORM_SCALE) {}
}; //struct OctaneScaleTransform

/// The structure holding a full transform data that is going to be uploaded to the Octane server.
struct OctaneFullTransform : public OctaneNodeBase {
    bool    bIsValue;
    float_3 f3Rotation;
    float_3 f3Scale;
    float_3 f3Translation;
    int32_t iRotationOrderDefaultVal;
    MatrixF matrix;

    OctaneFullTransform() : OctaneNodeBase(Octane::NT_TRANSFORM_VALUE) {}
}; //struct OctaneFullTransform

/// The structure holding a 2D transform data that is going to be uploaded to the Octane server.
struct Octane2DTransform : public OctaneNodeBase {
    string  sRotation;
    float_2 f2RotationDefaultVal;
    string  sScale;
    float_2 f2ScaleDefaultVal;
    string  sTranslation;
    float_2 f2TranslationDefaultVal;

    Octane2DTransform() : OctaneNodeBase(Octane::NT_TRANSFORM_2D) {}
}; //struct Octane2DTransform

/// The structure holding a 3D transform data that is going to be uploaded to the Octane server.
struct Octane3DTransform : public OctaneNodeBase {
    string  sRotation;
    float_3 f3RotationDefaultVal;
    string  sScale;
    float_3 f3ScaleDefaultVal;
    string  sTranslation;
    float_3 f3TranslationDefaultVal;
    string  sRotationOrder;
    int32_t iRotationOrderDefaultVal;

    Octane3DTransform() : OctaneNodeBase(Octane::NT_TRANSFORM_3D) {}
}; //struct Octane3DTransform


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a XYZ projection data that is going to be uploaded to the Octane server.
struct OctaneXYZProjection : public OctaneNodeBase {
    string  sTransform;
    string  sCoordinateSpace;
    int32_t iCoordinateSpaceDefaultVal;

    OctaneXYZProjection() : OctaneNodeBase(Octane::NT_PROJ_LINEAR) {}
}; //struct OctaneXYZProjection

/// The structure holding a box projection data that is going to be uploaded to the Octane server.
struct OctaneBoxProjection : public OctaneNodeBase {
    string  sTransform;
    string  sCoordinateSpace;
    int32_t iCoordinateSpaceDefaultVal;

    OctaneBoxProjection() : OctaneNodeBase(Octane::NT_PROJ_BOX) {}
}; //struct OctaneBoxProjection

/// The structure holding a cylindrical projection data that is going to be uploaded to the Octane server.
struct OctaneCylProjection : public OctaneNodeBase {
    string  sTransform;
    string  sCoordinateSpace;
    int32_t iCoordinateSpaceDefaultVal;

    OctaneCylProjection() : OctaneNodeBase(Octane::NT_PROJ_CYLINDRICAL) {}
}; //struct OctaneCylProjection

/// The structure holding a perspective projection data that is going to be uploaded to the Octane server.
struct OctanePerspProjection : public OctaneNodeBase {
    string  sTransform;
    string  sCoordinateSpace;
    /// 0 - Global
    /// 1 - Object
    /// 2 - Normal
    int32_t iCoordinateSpaceDefaultVal;

    OctanePerspProjection() : OctaneNodeBase(Octane::NT_PROJ_PERSPECTIVE) {}
}; //struct OctanePerspProjection

/// The structure holding a spherical projection data that is going to be uploaded to the Octane server.
struct OctaneSphericalProjection : public OctaneNodeBase {
    string  sTransform;
    string  sCoordinateSpace;
    int32_t iCoordinateSpaceDefaultVal;

    OctaneSphericalProjection() : OctaneNodeBase(Octane::NT_PROJ_SPHERICAL) {}
}; //struct OctaneSphericalProjection

struct OctaneUVWProjection : public OctaneNodeBase {

    OctaneUVWProjection() : OctaneNodeBase(Octane::NT_PROJ_UVW) {}
}; //struct OctaneUVWProjection



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VOLUME
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding an OpenVDB volume data that is going to be uploaded to the Octane server.
struct OctaneVolume : public OctaneNodeBase {
    string  sFileName;
    float   *pfRegularGrid;
    int32_t iGridSize;
    MatrixF gridMatrix;
    float_3 f3Resolution;
    float   fISO;
    string  sMedium;
    int32_t iAbsorptionOffset;
    float   fAbsorptionScale;
    int32_t iEmissionOffset;
    float   fEmissionScale;
    int32_t iScatterOffset;
    float   fScatterScale;
    int32_t iVelocityOffsetX;
    int32_t iVelocityOffsetY;
    int32_t iVelocityOffsetZ;
    float   fVelocityScale;
    string  sAbsorptionId;
    string  sEmissionId;
    string  sScatterId;
    string  sVelocityId;
    string  sVelocityIdX;
    string  sVelocityIdY;
    string  sVelocityIdZ;

    float   fGenVisibility;
    bool    bCamVisibility;
    bool    bShadowVisibility;
    int32_t iRandomColorSeed;
    int32_t iLayerNumber;
    int32_t iBakingGroupId;

    OctaneVolume() : OctaneNodeBase(Octane::NT_GEO_VOLUME) {}
}; //struct OctaneVolume


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a float value data that is going to be uploaded to the Octane server.
struct OctaneFloatValue : public OctaneNodeBase {
    float_3 f3Value;

    OctaneFloatValue() : OctaneNodeBase(Octane::NT_FLOAT) {}
}; //struct OctaneFloatValue

/// The structure holding a integer value data that is going to be uploaded to the Octane server.
struct OctaneIntValue : public OctaneNodeBase {
    int32_t iValue;

    OctaneIntValue() : OctaneNodeBase(Octane::NT_INT) {}
}; //struct OctaneIntValue


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OctaneEngine packet type
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
enum PacketType {
    NONE = 0,
    TEST_PACKET,

    GET_LDB_CAT,
    GET_LDB_MAT_PREVIEW,
    GET_LDB_MAT,

    ERROR_PACKET,
    DESCRIPTION,
    SET_LIC_DATA,
    RESET,
    CLEAR,
    START,
    STOP,
    START_FRAME_LOAD,
    FINISH_FRAME_LOAD,
    UPDATE,
    PAUSE,
    GET_IMAGE,
    GET_SAMPLES,

    LOAD_GPU,
    LOAD_PASSES,
    LOAD_KERNEL,
    LOAD_RENDER_REGION,
    LOAD_THIN_LENS_CAMERA,
    LOAD_PANORAMIC_CAMERA,
    LOAD_BAKING_CAMERA,
    //LOAD_IMAGER,
    //LOAD_POSTPROCESSOR,
    LOAD_SUNSKY,
    LOAD_VISIBLE_SUNSKY,
    LOAD_FILE,

    FIRST_NAMED_PACKET,
    LOAD_GLOBAL_MESH = FIRST_NAMED_PACKET,
    DEL_GLOBAL_MESH,
    LOAD_LOCAL_MESH,
    DEL_LOCAL_MESH,
    LOAD_VOLUME,
    LOAD_VOLUME_DATA,
    DEL_VOLUME,
    LOAD_GEO_MAT,
    DEL_GEO_MAT,
    LOAD_GEO_LAYERMAP,
    DEL_GEO_LAYERMAP,
    LOAD_GEO_SCATTER,
    DEL_GEO_SCATTER,
    LOAD_IMAGE_FILE,
    GET_PREVIEW,

    LOAD_MATERIAL_FIRST,
    LOAD_DIFFUSE_MATERIAL = LOAD_MATERIAL_FIRST,
    LOAD_GLOSSY_MATERIAL,
    LOAD_SPECULAR_MATERIAL,
    LOAD_MIX_MATERIAL,
    LOAD_PORTAL_MATERIAL,
    LOAD_MATERIAL_LAST = LOAD_PORTAL_MATERIAL,
    DEL_MATERIAL,

    LOAD_TEXTURE_FIRST,
    LOAD_FLOAT_TEXTURE = LOAD_TEXTURE_FIRST,
    LOAD_RGB_SPECTRUM_TEXTURE,
    LOAD_GAUSSIAN_SPECTRUM_TEXTURE,
    LOAD_CHECKS_TEXTURE,
    LOAD_MARBLE_TEXTURE,
    LOAD_RIDGED_FRACTAL_TEXTURE,
    LOAD_SAW_WAVE_TEXTURE,
    LOAD_SINE_WAVE_TEXTURE,
    LOAD_TRIANGLE_WAVE_TEXTURE,
    LOAD_TURBULENCE_TEXTURE,
    LOAD_CLAMP_TEXTURE,
    LOAD_COSINE_MIX_TEXTURE,
    LOAD_INVERT_TEXTURE,
    LOAD_MIX_TEXTURE,
    LOAD_W_TEXTURE,
    LOAD_MULTIPLY_TEXTURE,
    LOAD_IMAGE_TEXTURE,
    LOAD_IMAGE_TEXTURE_DATA,
    LOAD_ALPHA_IMAGE_TEXTURE,
    LOAD_ALPHA_IMAGE_TEXTURE_DATA,
    LOAD_FLOAT_IMAGE_TEXTURE,
    LOAD_FLOAT_IMAGE_TEXTURE_DATA,
    LOAD_FALLOFF_TEXTURE,
    LOAD_COLOR_CORRECT_TEXTURE,
    LOAD_DIRT_TEXTURE,
    LOAD_GRADIENT_TEXTURE,
    LOAD_VOLUMERAMP_TEXTURE,
    LOAD_DISPLACEMENT_TEXTURE,
    LOAD_RANDOM_COLOR_TEXTURE,
    LOAD_POLYGON_SIDE_TEXTURE,
    LOAD_NOISE_TEXTURE,
    LOAD_TEXTURE_LAST = LOAD_NOISE_TEXTURE,
    DEL_TEXTURE,

    LOAD_EMISSION_FIRST,
    LOAD_BLACKBODY_EMISSION = LOAD_EMISSION_FIRST,
    LOAD_TEXTURE_EMISSION,
    LOAD_EMISSION_LAST = LOAD_TEXTURE_EMISSION,
    DEL_EMISSION,

    LOAD_TRANSFORM_FIRST,
    LOAD_SCALE_TRANSFORM = LOAD_TRANSFORM_FIRST,
    LOAD_ROTATION_TRANSFORM,
    LOAD_FULL_TRANSFORM,
    LOAD_VALUE_TRANSFORM,
    LOAD_2D_TRANSFORM,
    LOAD_3D_TRANSFORM,
    LOAD_TRANSFORM_LAST = LOAD_3D_TRANSFORM,
    DEL_TRANSFORM,

    LOAD_MEDIUM_FIRST,
    LOAD_ABSORPTION_MEDIUM = LOAD_MEDIUM_FIRST,
    LOAD_SCATTERING_MEDIUM,
    LOAD_VOLUME_MEDIUM,
    LOAD_MEDIUM_LAST = LOAD_VOLUME_MEDIUM,
    DEL_MEDIUM,

    LOAD_PROJECTION_FIRST,
    LOAD_PROJECTION_XYZ = LOAD_PROJECTION_FIRST,
    LOAD_PROJECTION_BOX,
    LOAD_PROJECTION_CYL,
    LOAD_PROJECTION_PERSP,
    LOAD_PROJECTION_SPHERICAL,
    LOAD_PROJECTION_UVW,
    LOAD_PROJECTION_LAST = LOAD_PROJECTION_UVW,
    DEL_PROJECTION,

    LOAD_VALUE_FIRST,
    LOAD_VALUE_FLOAT = LOAD_VALUE_FIRST,
    LOAD_VALUE_INT,
    LOAD_VALUE_LAST = LOAD_VALUE_INT,
    DEL_VALUE,

    LAST_NAMED_PACKET = DEL_VALUE,

    LAST_PACKET_TYPE = LAST_NAMED_PACKET
}; //enum PacketType


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render Server
/// OctaneClient class is used to communicate with OctaneEngine.
/// Create the instance of OctaneClient class and connect it to the server using connectToServer().
/// You need to check that the server has the proper version using checkServerVersion().
/// To start the rendering of the scene, first call the reset() method to prepare the scene for rendering.
/// Then upload the scene data using all the upload methods. End the scene uploading by startRender() method.
/// Refresh the image buffer cache by the currently rendered image from the server by downloadImageBuffer() method.
/// Get the image by getImgBuffer8bit(), getCopyImgBuffer8bit(), getImgBufferFloat() or getCopyImgBufferFloat().
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneClient {
public:
    ////////////////////////////////////////////////////////////////////////////////////////////////
    // Render Server structures

    /// The information about the server we are currently connected to.
    struct RenderServerInfo {
        string              sNetAddress;    ///< The network address of the server.
	    string              sDescription;   ///< Server description (currently not used).
        std::vector<string> gpuNames;       ///< Names of active GPUs on a server.
    }; //struct RenderServerInfo

    /// The type of the rendered image.
    enum ImageType {
        IMAGE_8BIT = 0,         ///< RGBA 8 bit per channel image.
        IMAGE_FLOAT,            ///< RGBA 32 bit per channel image.
        IMAGE_FLOAT_TONEMAPPED  ///< RGBA 32 bit per channel tonemapped image.
    }; //enum ImageType

    /// The render statistics returned by the **GET_IMAGE** packet.
    struct RenderStatistics {
        uint32_t    uiCurSamples,   ///< Amount of samples per pixel currently rendered.
                    uiMaxSamples;   ///< Max. samples to render.
        uint64_t    ulVramUsed,     ///< Amount of VRAM used.
                    ulVramFree,     ///< Amount of free VRAM.
                    ulVramTotal;    ///< Total amount of VRAM.
        float       fSPS,           ///< The current rendering speed (in samples per second).
                    fRenderTime,    ///< Render time.
                    fGamma;         ///< Image gamma.
        uint32_t    uiTrianglesCnt, ///< The total amount of triangles in currently rendered scene.
                    uiMeshesCnt,    ///< The total amount of meshes in currently rendered scene.
                    uiSpheresCnt,   ///< The total amount of sphere primitives in currently rendered scene.
                    uiVoxelsCnt,    ///< The total amount of voxels in currently rendered scene.
                    uiDisplCnt,     ///< The total amount of displacement polygons.
                    uiHairsCnt;     ///< The total amount of hairs.
        uint32_t    uiRgb32Cnt,     ///< The total amount of RGB-32 textures in currently rendered scene.
                    uiRgb64Cnt,     ///< The total amount of RGB-64 textures in currently rendered scene.
                    uiGrey8Cnt,     ///< The total amount of Grey-8 textures in currently rendered scene.
                    uiGrey16Cnt;    ///< The total amount of Grey-16 textures in currently rendered scene.
        uint32_t    uiNetGPUs,      ///< The amount of available network GPUs.
                    uiNetGPUsUsed;  ///< The amount of network GPUs used by current rendering session.
        int32_t     iExpiryTime;    ///< Expiry time (in seconds) for the subscription version.
        int32_t     iComponentsCnt; ///< Number of color components in image.
        uint32_t    uiW,            ///< Render width.
                    uiH,            ///< Render height.
                    uiRegW,         ///< Render region width.
                    uiRegH;         ///< Render region height.
    }; //struct RenderStatistics

    /// Wrapper structure for the enum of the fail reasons returned by getFailReason().
    struct FailReasons {
        /// The fail reasons returned by getFailReason().
        enum FailReasonsEnum {
            NONE = -1,      ///< No failure.
            UNKNOWN,        ///< Unknown fail reason.
            WRONG_VERSION,  ///< The OctaneEngine version differs from that of the current client library.
            NO_CONNECTION,  ///< No network connection to the server.
            NOT_ACTIVATED,  ///< The Octane license is not activated on the server. Use the activate() method to activate the license on the server.
            NO_GPUS         ///< No CUDA GPUs available on a server.
        }; //enum FailReasonsEnum
    };

    /// Wrapper structure for the enum of the types of scene export.
    struct SceneExportTypes {
        /// Type of scene export.
        enum SceneExportTypesEnum {
            NONE = 0,   ///< No export, just render.
            ALEMBIC,    ///< Export alembic file.
            ORBX        ///< Export ORBX file.
        }; //enum SceneExportTypesEnum
    };

    inline OctaneClient();
    inline ~OctaneClient();

    /// Sets the output path for alembic or ORBX export file, or for deep image file.
    /// Should be a full path containing file name without extension.
    /// @param [in] szOutPath - path for the assets.
    inline void setOutputPath(const char *szOutPath);

    /// Sets the type of export (no export, alembic or ORBX).
    /// @param [in] exportSceneType - type of scene export.
    inline void setExportType(const SceneExportTypes::SceneExportTypesEnum exportSceneType);

    /// Connects to the given Octane server.
    /// @param [in] szAddr - server address
    /// @return **true** if connection has been successful, **false** otherwise.
    inline bool     connectToServer(const char *szAddr);
    /// Disconnects from the currently connected Octane server. Safe to call when not connected.
    /// @return **true** if disconnection has been successful, **false** otherwise.
    inline bool     disconnectFromServer();
    /// Check if connected to server.
    /// @return **true** if connected, **false** otherwise.
    inline bool     checkServerConnection();
    /// Block any server updates (all data upload functions will do nothing).
    /// @param [in] bBlocked - current "blocked" status.
    inline void     setUpdatesBlocked(bool bBlocked);

    /// Get the current error message returned by Octane server.
    /// @return A reference to **std::string** value containing the message.
	inline const string&        getServerErrorMessage();
    /// Clear the current error message returned by Octane server.
	inline void                 clearServerErrorMessage();
    /// Get the info about the currently connected Octane server.
    /// @return RenderServerInfo structure containing information about the server.
    inline RenderServerInfo&    getServerInfo(void);
    /// Get the current fail reason.
    /// @return Enum value of FailReasons type.
    inline FailReasons::FailReasonsEnum getFailReason(void);

    
    /// Check the connected OctaneEngine version.
    /// @return **true** if the server has the corresponding version, **false** otherwise. Disconnets from the server if wrong version.
    inline bool     checkServerVersion();                                                               
    /// Activate the Octane license on server.
    /// @param [in] sStandLogin - The login of standalone license.
    /// @param [in] sStandPass - The password of standalone license.
    /// @param [in] sLogin - The login of a plugin license.
    /// @param [in] sPass - The password of a plugin license.
    /// @return **true** if successfully activated, **false** otherwise.
    inline bool     activate(string const &sStandLogin, string const &sStandPass, string const &sLogin, string const &sPass);   

    /// Reset the project on the server.
    /// @param [in] exportSceneType - Type of the scene export (NONE if just rendering).
    /// @param [in] uiGPUs - The GPUs that should be used by server, as a bit-map.
    /// @param [in] fFrameTimeSampling - Time sampling of the frames (for the animation and motion blur).
    /// @param [in] fFps - Frames per second value.
    inline void reset(SceneExportTypes::SceneExportTypesEnum exportSceneType, uint32_t uiGPUs, float fFrameTimeSampling, float fFps, bool bDeepImage);

    /// Delete all the nodes int the project currently loaded on the server. Does nothing if a file export session is active.
    inline void clear();

    /// Update current render project on the server.
    /// @return **true** if successfully updated, **false** otherwise.
    inline bool update();

    /// Start the rendering process on the server.
    /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
    /// @param [in] iWidth - The width of the the rendered image.
    /// @param [in] iHeigth - The heigth of the the rendered image.
    /// @param [in] imgType - The type of the rendered image.
    /// @param [in] bOutOfCoreEnabled - Enable "out of core" mode.
    /// @param [in] iOutOfCoreMemLimit - Memory limit for "out of core" mode.
    /// @param [in] iOutOfCoreGPUHeadroom - GPU headroom for "out of core" mode.
    inline void startRender(bool bInteractive, int32_t iWidth, int32_t iHeigth, ImageType imgType, bool bOutOfCoreEnabled, int32_t iOutOfCoreMemLimit, int32_t iOutOfCoreGPUHeadroom);
    /// Stop the render process on the server.
    /// Mostly needed to close the animation export sequence on the server.
    /// @param [in] fFPS - Frames per second value.
    inline void stopRender(float fFPS);
    /// Check if the scene has already been loaded onto the server and startRender() has been called.
    inline bool isRenderStarted();
    /// Pause the current rendering.
    inline void pauseRender(int32_t bPause);
    /// Start the frame uploading.
    /// Mostly needed to upload the animation export sequence to the server or for motion blur.
    inline void startFrameUpload();
    /// Indicate to the server that the frame uploading has been finished.
    /// Mostly needed to upload the animation export sequence to the server.
    /// @param [in] bUpdate - Do the update of the loaded scene on the server or for motion blur.
    inline void finishFrameUpload(bool bUpdate);

    /// Upload GPUs configuration to render server.
    /// @param [in] uiGPUs - The GPUs that should be used by server, as a bit-map.
    inline void uploadGPUs(uint32_t uiGPUs);

    /// Upload camera to render server.
    /// @param [in] pCamera - Camera data structure.
    /// @param [in] uiFrameIdx - The index of the frame the camera is loaded for.
    /// @param [in] uiTotalFrames - First time the animated frames of camera are uploaded (starting from 0) - this value contains the total amount of frames this camera node is going to be uploaded for.
    inline void uploadCamera(Camera *pCamera, uint32_t uiFrameIdx, uint32_t uiTotalFrames);

    /// Upoad passes configuration to render server.
    /// @param [in] pPasses - Passes data structure.
    void uploadPasses(Passes *pPasses);

    /// Upload kernel configuration to render server.
    /// @param [in] pKernel - Kernel data structure.
    void uploadKernel(Kernel *pKernel);

    /// Upload the configuration of region of image to render.
    /// @param [in] pCamera - Camera data structure.
    /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
    void uploadRenderRegion(Camera *pCamera, bool bInteractive);

    /// Upload environment configuration to render server.
    /// @param [in] pEnv - Environment data structure.
    void uploadEnvironment(Environment *pEnv);

    /// Upload visible environment configuration to render server.
    /// @param [in] pEnv - Environment data structure.
    void uploadVisibleEnvironment(Environment *pEnv);

    /// Upload the node to server.
    /// @param [in] pNodeData - Pointer to node's data structure.
    void uploadNode(OctaneNodeBase *pNodeData);

    /// Delete the node on the server.
    /// @param [in] pNodeData - Pointer to node data structure holding node's type and name.
    void deleteNode(OctaneNodeBase *pNodeData);

    /// Upload scatter node to server. Only one matrix upload is supported for "movable" mode at the time.
    /// @param [in] sScatterName - Statter's unique name.
    /// @param [in] sMeshName - Unique name of geometry node being scattered.
    /// @param [in] pfMatrices - Array of 4x3 matrices. Only one matrix upload is supported for "movable" mode at the time.
    /// @param [in] ulMatrCnt - Count of matrices. Only one matrix upload is supported for "movable" mode at the time, so this must always be 1 if **bMovable** is set to **true**.
    /// @param [in] bMovable - Load the scatter as movable. That means the animated sequence of matrices will be loaded for every frame on the server. See **uiFrameIdx** and **uiTotalFrames**.
    /// @param [in] asShaderNames - Array of names of shaders assigned to scatters.
    /// @param [in] uiFrameIdx - The index of the frame the scatter is loaded for. Makes sense only if **bMovable** is set to **true**, otherwise must be 0.
    /// @param [in] uiTotalFrames - First time the animated frames of scatter are uploaded (starting from 0) - this value contains the total amount of frames this scatter node is going to be uploaded for.
    /// To re-upload the scatter node for some already loaded frames - set this parameter to 0 and **uiFrameIdx** to needed frame index.
    inline void uploadScatter(string &sScatterName, string &sMeshName, float *pfMatrices, uint64_t ulMatrCnt, bool bMovable, vector<string> &asShaderNames, uint32_t uiFrameIdx, uint32_t uiTotalFrames);
    /// Delete the scatter node on the server.
    /// @param [in] sName - Unique name of the scatter node that is going to be deleted on the server.
    inline void deleteScatter(string const &sName);

    /// Upload a bunch of mesh nodes to render server. If the global world-space mesh is going to be loaded - this bunch must contain all the meshes the global mesh consists of.
    /// @param [in] bGlobal - If **true**, the global mesh is going to be loaded. All the given meshes will be merged by the server into one world-space mesh.
    /// @param [in] uiFrameIdx - The index of the frame the meshes are loaded for. Used only for the meshes who's corresponding **pbReshapable** array element is set to **true**.
    /// @param [in] uiTotalFrames - First time the animated frames of mesehs are uploaded (starting from 0) - this value contains the total amount of frames these mesh nodes are going to be uploaded for.
    /// To re-upload the **reshapable** mesh nodes for some already loaded frames - set this parameter to 0 and **uiFrameIdx** to needed frame index.
    /// @param [in] uiMeshCnt - Number of meshes in this bunch.
    /// @param [in] ppcNames - Array of unique mesh names.
    /// @param [in] puiShadersCnt - Array with number of shaders for each mesh.
    /// @param [in] puiObjectsCnt - Array with number of objects for each mesh.
    /// @param [in] pasShaderNames - Array of string arrays holding the shader names for each mesh.
    /// @param [in] pasObjectNames - Array of string arrays holding the object names for each mesh.
    /// @param [in] ppf3Points - Array with arrays of points coordinates for each mesh.
    /// @param [in] pulPointsSize - Array with number of points for each mesh.
    /// @param [in] ppf3Normals - Array with arrays of normals vectors for each mesh.
    /// @param [in] pulNormalsSize - Array with number of normals for each mesh.
    /// @param [in] ppiPointsIndices - Array with arrays of points indices for each mesh.
    /// @param [in] ppiNormalsIndices - Array with arrays of normals indices for each mesh.
    /// @param [in] plPointsIndicesSize - Array with number of points indices for each mesh.
    /// @param [in] plNormalsIndicesSize - Array with number of normals indices for each mesh.
    /// @param [in] ppiVertPerPoly - Array with arrays of numbers of vertices per polygon for aach mesh.
    /// @param [in] plVertPerPolySize - Array with number of polygons for each mesh.
    /// @param [in] ppiPolyMatIndex - Array with arrays of material indices of each polygon for each mesh.
    /// @param [in] ppiPolyObjIndex - Array with arrays of object indices of each polygon for each mesh.
    /// @param [in] ppf3UVs - Array with arrays of UV coordinates for each mesh.
    /// @param [in] plUVsSize - Array with number of UVs for each mesh.
    /// @param [in] ppiUVIndices - Array with arrays of UVs indices for each mesh.
    /// @param [in] plUVIndicesSize - Array with number of UVs for each mesh.
    /// @param [in] ppf3HairPoints - Array with arrays of hair points coordinates for each mesh.
    /// @param [in] plHairPointsSize - Array with number of hair points for each mesh.
    /// @param [in] plHairWsSize - Array with number of hair Ws for each mesh.
    /// @param [in] ppiVertPerHair - Array with arrays of number of vertices per hair for each mesh.
    /// @param [in] plVertPerHairSize - Array with number of hairs for each mesh.
    /// @param [in] ppfHairThickness - Array with arrays of hair thicknesses for each mesh.
    /// @param [in] ppiHairMatIndices - Array with arrays of material indices for hairs of each mesh.
    /// @param [in] ppf2HairUVs - Array with arrays of UVs for hairs of each mesh.
    /// @param [in] ppf2HairWs - Array with arrays of Ws for hairs of each mesh.
    /// @param [in] aiHairInterpolations - Array with W interpolation types for hairs of each mesh.
    /// @param [in] pbOpenSubdEnable - Array with "OpenSubDiv enable" switches for each mesh.
    /// @param [in] piOpenSubdScheme - Array with "OpenSubDiv scheme" value for each mesh.
    /// @param [in] piOpenSubdLevel - Array with "OpenSubDiv level" value for each mesh.
    /// @param [in] pfOpenSubdSharpness - Array with "OpenSubDiv sharpness" value for each mesh.
    /// @param [in] piOpenSubdBoundInterp - Array with "OpenSubDiv boundary interpolation" value for each mesh.
    /// @param [in] piOpenSubdCreasesCnt - Array with creases count for each mesh.
    /// @param [in] ppiOpenSubdCreasesIndices - Array with creases indices for each mesh.
    /// @param [in] ppfOpenSubdCreasesSharpnesses - Array with creases sharpnesses for each mesh.
    /// @param [in] piLayerNumber - Array with layer number for each mesh.
    /// @param [in] piBakingGroupId - Array with baking group id for each mesh.
    /// @param [in] pfGeneralVis - Array with "General visibility" value for each mesh.
    /// @param [in] pbCamVis - Array with "Camera visibility" value for each mesh.
    /// @param [in] pbShadowVis - Array with "Shadow visibility" value for each mesh.
    /// @param [in] piRandColorSeed - Array with "Random color seed" value for each mesh.
    /// @param [in] pbReshapable - Array with "Reshapable mesh" switch for each mesh. Only reshapable meshes are deform-animated and can have deform-motionblur.
    /// @param [in] pfMaxSmoothAngle - Array with "Max. smooth angle" value for each mesh. If negative - normals data is used, otherwise - normals data is ignored.
    inline void uploadMesh(         bool            bGlobal, uint32_t uiFrameIdx, uint32_t uiTotalFrames,
                                    uint64_t        uiMeshCnt,
                                    char            **ppcNames,
                                    uint64_t        *puiShadersCnt,
                                    uint64_t        *puiObjectsCnt,
                                    vector<string>  *pasShaderNames,
                                    vector<string>  *pasObjectNames,
                                    float_3         **ppf3Points,
                                    uint64_t        *pulPointsSize,
                                    float_3         **ppf3Normals,
                                    uint64_t        *pulNormalsSize,
                                    int32_t         **ppiPointsIndices,
                                    int32_t         **ppiNormalsIndices,
                                    uint64_t        *plPointsIndicesSize,
                                    uint64_t        *plNormalsIndicesSize,
                                    int32_t         **ppiVertPerPoly,
                                    uint64_t        *plVertPerPolySize,
                                    int32_t         **ppiPolyMatIndex,
                                    int32_t         **ppiPolyObjIndex,
                                    float_3         **ppf3UVs,
                                    uint64_t        *plUVsSize,
                                    int32_t         **ppiUVIndices,
                                    uint64_t        *plUVIndicesSize,
                                    float_3         **ppf3HairPoints,
                                    uint64_t        *plHairPointsSize,
                                    uint64_t        *plHairWsSize,
                                    int32_t         **ppiVertPerHair,
                                    uint64_t        *plVertPerHairSize,
                                    float           **ppfHairThickness,
                                    int32_t         **ppiHairMatIndices,
                                    float_2         **ppf2HairUVs,
                                    float_2         **ppf2HairWs,
                                    int32_t         *aiHairInterpolations,
                                    bool            *pbOpenSubdEnable,
                                    int32_t         *piOpenSubdScheme,
                                    int32_t         *piOpenSubdLevel,
                                    float           *pfOpenSubdSharpness,
                                    int32_t         *piOpenSubdBoundInterp,
                                    uint64_t        *piOpenSubdCreasesCnt,
                                    int32_t         **ppiOpenSubdCreasesIndices,
                                    float           **ppfOpenSubdCreasesSharpnesses,
                                    int32_t         *piLayerNumber,
                                    int32_t         *piBakingGroupId,
                                    float           *pfGeneralVis,
                                    bool            *pbCamVis,
                                    bool            *pbShadowVis,
                                    int32_t         *piRandColorSeed,
                                    bool            *pbReshapable,
                                    float           *pfMaxSmoothAngle);
    /// Delete the mesh node on the server.
    /// @param [in] bGlobal - Set to **true** if the global world-space mesh needs to be deleted.
    /// @param [in] sName - Unique name of the mesh node that is going to be deleted on the server. Does not make sense if **bGloabl** is true.
    inline void deleteMesh(bool bGlobal, string const &sName);
    /// Upload layer map node to the server.
    /// @param [in] bGlobal - If **true**, the layer map of global mesh is going to be loaded.
    /// @param [in] sName - Unique name of the layer map node.
    /// @param [in] sMeshName - Unique name of geometry node being layered.
    /// @param [in] iLayersCnt - Number of layers in this map.
    /// @param [in] piLayerId - Array with layer number for each layer node.
    /// @param [in] piBakingGroupId - Array with baking group number for each layer node.
    /// @param [in] pfGeneralVis - Array with "General visibility" value for each layer node.
    /// @param [in] pbCamVis - Array with "Camera visibility" value for each layer node.
    /// @param [in] pbShadowVis - Array with "Shadow visibility" value for each layer node.
    /// @param [in] piRandColorSeed - Array with "Random color seed" value for each layer node.
    inline void uploadLayerMap( bool bGlobal,
                                string const    &sLayerMapName, string const &sMeshName,
                                int32_t         iLayersCnt,
                                int32_t         *piLayerId,
                                int32_t         *piBakingGroupId,
                                float           *pfGeneralVis,
                                bool            *pbCamVis,
                                bool            *pbShadowVis,
                                int32_t         *piRandColorSeed);
    /// Delete the layer node on the server.
    /// @param [in] sName - Unique name of the layer node that is going to be deleted on the server.
    inline void deleteLayerMap(string const &sName);
    /// Upload the OpenVDB volume node to the server.
    /// @param [in] pNode - Volume data structure.
    inline void uploadVolume(OctaneVolume *pNode);
    /// Delete the volume node on the server.
    /// @param [in] sName - Unique name of the volume node that is going to be deleted on the server.
    inline void deleteVolume(string const &sName);

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // MATERIALS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the diffuse material node to the server.
    /// @param [in] pNode - Material data structure.
    inline void uploadDiffuseMat(OctaneDiffuseMaterial *pNode);
    /// Upload the glossy material node to the server.
    /// @param [in] pNode - Material data structure.
    inline void uploadGlossyMat(OctaneGlossyMaterial *pNode);
    /// Upload the specular material node to the server.
    /// @param [in] pNode - Material data structure.
    inline void uploadSpecularMat(OctaneSpecularMaterial *pNode);
    /// Upload the mix material node to the server.
    /// @param [in] pNode - Material data structure.
    inline void uploadMixMat(OctaneMixMaterial *pNode);
    /// Upload the portal material node to the server.
    /// @param [in] pNode - Material data structure.
    inline void uploadPortalMat(OctanePortalMaterial *pNode);
    /// Delete the material node on the server.
    /// @param [in] sName - Unique name of the material.
    inline void deleteMaterial(string const &sName);



    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // TEXTURES
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the greycolor texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadFloatTex(OctaneFloatTexture *pNode);
    /// Upload the RGB-color texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadRgbSpectrumTex(OctaneRGBSpectrumTexture *pNode);
    /// Upload the gaussian spectrum texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadGaussianSpectrumTex(OctaneGaussianSpectrumTexture *pNode);
    /// Upload the checks texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadChecksTex(OctaneChecksTexture *pNode);
    /// Upload the marble texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadMarbleTex(OctaneMarbleTexture *pNode);
    /// Upload the ridged fractal texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadRidgedFractalTex(OctaneRidgedFractalTexture *pNode);
    /// Upload the saw wave texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadSawWaveTex(OctaneSawWaveTexture *pNode);
    /// Upload the sine wave texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadSineWaveTex(OctaneSineWaveTexture *pNode);
    /// Upload the triangle wave texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadTriangleWaveTex(OctaneTriangleWaveTexture *pNode);
    /// Upload the turbulence texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadTurbulenceTex(OctaneTurbulenceTexture *pNode);
    /// Upload the clamp  texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadClampTex(OctaneClampTexture *pNode);
    /// Upload the cosine mix texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadCosineMixTex(OctaneCosineMixTexture *pNode);
    /// Upload the invert texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadInvertTex(OctaneInvertTexture *pNode);
    /// Upload the mix texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadMixTex(OctaneMixTexture *pNode);
    /// Upload the multiply texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadMultiplyTex(OctaneMultiplyTexture *pNode);
    /// Upload the falloff texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadFalloffTex(OctaneFalloffTexture *pNode);
    /// Upload the color correct texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadColorcorrectTex(OctaneColorCorrectTexture *pNode);

    /// Upload the image texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadImageTex(OctaneImageTexture *pNode);
    /// Upload the float image texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadFloatImageTex(OctaneFloatImageTexture *pNode);
    /// Upload the alpha image texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadAlphaImageTex(OctaneAlphaImageTexture *pNode);

    /// Upload the dirt texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadDirtTex(OctaneDirtTexture *pNode);
    /// Upload the gradient texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadGradientTex(OctaneGradientTexture *pNode);
    /// Upload the volume ramp texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadVolumeRampTex(OctaneVolumeRampTexture *pNode);
    /// Upload the random color texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadRandomColorTex(OctaneRandomColorTexture *pNode);
    /// Upload the polygon side texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadPolygonSideTex(OctanePolygonSideTexture *pNode);
    /// Upload the noise texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadNoiseTex(OctaneNoiseTexture *pNode);
    /// Upload the displacement node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadDisplacementTex(OctaneDisplacementTexture *pNode);
    /// Upload the W texture node to the server.
    /// @param [in] pNode - Texture data structure.
    inline void uploadWTex(OctaneWTexture *pNode);

    /// Delete the texture node on the server.
    /// @param [in] sName - Unique name of the texture.
    inline void deleteTexture(string const &sName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // EMISSIONS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline void uploadBbodyEmission(OctaneBlackBodyEmission *pNode);
    inline void uploadTextureEmission(OctaneTextureEmission *pNode);
    /// Delete the emission node on the server.
    /// @param [in] sName - Unique name of the emission.
    inline void deleteEmission(string const &sName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // MEDIUMS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the absorption medium node to the server.
    /// @param [in] pNode - Medium data structure.
    inline void uploadAbsorptionMedium(OctaneAbsorptionMedium *pNode);
    /// Upload the scattering medium node to the server.
    /// @param [in] pNode - Medium data structure.
    inline void uploadScatteringMedium(OctaneScatteringMedium *pNode);
    /// Upload the volume medium node to the server.
    /// @param [in] pNode - Medium data structure.
    inline void uploadVolumeMedium(OctaneVolumeMedium *pNode);
    /// Delete the medium node on the server.
    /// @param [in] sName - Unique name of the medium.
    inline void deleteMedium(string const &sName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // TRANSFORMS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the rotation transform node to the server.
    /// @param [in] pNode - Transform data structure.
    inline void uploadRotationTransform(OctaneRotationTransform *pNode);
    /// Upload the scale transform node to the server.
    /// @param [in] pNode - Transform data structure.
    inline void uploadScaleTransform(OctaneScaleTransform *pNode);
    /// Upload the full transform node to the server.
    /// @param [in] pNode - Transform data structure.
    inline void uploadFullTransform(OctaneFullTransform *pNode);
    /// Upload the 3D transform node to the server.
    /// @param [in] pNode - Transform data structure.
    inline void upload3dTransform(Octane3DTransform *pNode);
    /// Upload the 2D transform node to the server.
    /// @param [in] pNode - Transform data structure.
    inline void upload2dTransform(Octane2DTransform *pNode);
    /// Delete the transform node on the server.
    /// @param [in] sName - Unique name of the transform.
    inline void deleteTransform(string const &sName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // PROJECTIONS
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the XYZ projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadXyzProjection(OctaneXYZProjection *pNode);
    /// Upload the box projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadBoxProjection(OctaneBoxProjection *pNode);
    /// Upload the cylindrical projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadCylProjection(OctaneCylProjection *pNode);
    /// Upload the perspective projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadPerspProjection(OctanePerspProjection *pNode);
    /// Upload the spherical projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadSphericalProjection(OctaneSphericalProjection *pNode);
    /// Upload the UVW projection node to the server.
    /// @param [in] pNode - Projection data structure.
    inline void uploadUvwProjection(OctaneUVWProjection *pNode);
    /// Delete the projection node on the server.
    /// @param [in] sName - Unique name of the projection.
    inline void deleteProjection(string const &sName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // VALUES
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Upload the float value node to the server.
    /// @param [in] pNode - Value data structure.
    inline void uploadFloatValue(OctaneFloatValue *pNode);
    /// Upload the integer value node to the server.
    /// @param [in] pNode - Value data structure.
    inline void uploadIntValue(OctaneIntValue *pNode);
    /// Delete the value node on the server.
    /// @param [in] sName - Unique name of the value.
    inline void deleteValue(string const &sName);


    /// Get current render-buffer pass type.
    inline Octane::RenderPassId currentPassType();

    /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the image buffer from Octane server.
    /// This method is made a way it **always** returns the image buffer of requested size, even if it has not been downloaded from the server so far (just empty image in this case).
    /// You can change the size of currently cached image by this method: requesting the different size in parameters. In this case you'll get the empty image buffer of requested size
    /// if the cache contains the image of different size of does not contain an image so far, but the next call to downloadImageBuffer() will refresh the size of rendered image on
    /// the server according to size requested here.
    /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
    /// @param [out] pucBuf - Pointer to cached image buffer.
    /// @param [in] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in] iRegionWidth - Requested width of the region. Must be equal to iWidth if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @return **true** if image cache contains image of requested size, **false** otherwise (empty image buffer having requested size is returned in this case).
    inline bool getImgBuffer8bit(int &iComponentsCnt, uint8_t *&pucBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight);
    /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the image buffer from Octane server.
    /// This method is made a way it **always** returns the image buffer of requested size, even if it has not been downloaded from the server so far (just empty image in this case).
    /// You can change the size of currently rendered image by this method: requesting the different size in parameters. In this case you'll get the empty image buffer of requested size
    /// if the cache contains the image of different size of does not contain an image so far, but the next call to downloadImageBuffer() will refresh the size of rendered image on
    /// the server according to size requested here.
    /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
    /// @param [out] pucBuf - Pointer to the buffer holding the copy of cached image buffer. It is caller's responsibility to **delete[]** this buffer.
    /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @return **true** if image cache contains image of requested size, **false** otherwise (empty image buffer having requested size is returned in this case).
    inline bool getCopyImgBuffer8bit(int iComponentsCnt, uint8_t *&pucBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight);

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Get Image-buffer of given pass
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the image buffer from Octane server.
    /// This method is made a way it **always** returns the image buffer of requested size, even if it has not been downloaded from the server so far (just empty image in this case).
    /// You can change the size of currently rendered image by this method: requesting the different image and region size in parameters. In this case you'll get the empty image buffer of requested size
    /// if the cache contains the image of different size of does not contain an image so far, but the next call to downloadImageBuffer() will refresh the size of rendered image on
    /// the server according to size requested here.
    /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
    /// @param [out] pfBuf - Pointer to cached image buffer.
    /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @return **true** if image cache contains image of requested size, **false** otherwise (empty image buffer having requested size is returned in this case).
    inline bool getImgBufferFloat(int &iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight);
    /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the image buffer from Octane server.
    /// This method is made a way it **always** returns the image buffer of requested size, even if it has not been downloaded from the server so far (just empty image in this case).
    /// You can change the size of currently rendered image by this method: requesting the different size in parameters. In this case you'll get the empty image buffer of requested size
    /// if the cache contains the image of different size of does not contain an image so far, but the next call to downloadImageBuffer() will refresh the size of rendered image on
    /// the server according to size requested here.
    /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
    /// @param [out] pfBuf - Pointer to the buffer holding the copy of cached image buffer. It is caller's responsibility to **delete[]** this buffer.
    /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
    /// @return **true** if image cache contains image of requested size, **false** otherwise (empty image buffer having requested size is returned in this case).
    inline bool getCopyImgBufferFloat(int iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight);

    /// Downloads and caches the currently rendered image buffer from the server. Gets the rendering statistics in addition to that.
    /// @param [out] renderStat - RenderStatistics structure.
    /// @param [in] imgType - The type of rendered image.
    /// @param [in] passType - The pass type.
    /// @param [in] bForce - Force to download a buffer even if no buffer refresh has been made on a server.
    inline bool downloadImageBuffer(RenderStatistics &renderStat, ImageType const imgType, RenderPassId &passType, bool const bForce = false);

    /// Get a preiview for material or texture by node Id. The node must be already uploaded to the server.
    /// @param [out] renderStat - RenderStatistics structure.
    /// @param [in] sName - The Id of a node.
    /// @param [in] uiWidth - Preview width in pixels.
    /// @param [in] uiHeight - Preview height in pixels.
    /// @return - A pointer to the downloaded image buffer or NULL if error. The caller is responsible for freeing a buffer.
    inline unsigned char* getPreview(std::string sName, uint32_t &uiWidth, uint32_t &uiHeight);

    inline bool checkImgBuffer8bit(uint8_4 *&puc4Buf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight, bool bCopyToBuf = false);
    inline bool checkImgBufferFloat(int iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight, bool bCopyToBuf = false);

private:
#ifdef _WIN32
    CRITICAL_SECTION    m_SocketMutex;
    CRITICAL_SECTION    m_ImgBufMutex;
#else
    pthread_mutex_t     m_SocketMutex;
    pthread_mutex_t     m_ImgBufMutex;
#endif

    uint8_t     *m_pucImageBuf;
    float       *m_pfImageBuf;
    int32_t     m_iComponentCnt;
    size_t      m_stImgBufLen;

    SceneExportTypes::SceneExportTypesEnum  m_ExportSceneType;
    bool                                    m_bDeepImage;
    FailReasons::FailReasonsEnum            m_FailReason;
    char                                    m_cBlockUpdates;

    int32_t             m_iCurImgBufWidth, m_iCurImgBufHeight, m_iCurRegionWidth, m_iCurRegionHeight;
    bool                m_bUnpackedTexturesMsgShown;
	string              m_sErrorMsg;

    RenderPassId        m_CurPassType;
    string              m_sAddress;
    string              m_sOutPath;
	RenderServerInfo    m_ServerInfo;
    int                 m_Socket;

    std::vector<Camera>         m_CameraCache;
    std::vector<Kernel>         m_KernelCache;
    std::vector<Passes>         m_PassesCache;
    std::vector<Environment>    m_EnvironmentCache, m_VisibleEnvironmentCache;

    bool                m_bRenderStarted;

    inline bool checkResponsePacket(PacketType packetType, const char *szErrorMsg = 0);

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // 
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    inline string   getFileName(string &sFullPath);
    inline uint64_t getFileTime(string &sFullPath);
    inline bool     uploadFile(string &sFilePath, string &sFileName);


    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Send data class
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    class RPCSend {
    public:
        RPCSend(int socket, uint64_t ulBufSize, PacketType packetType, const char* szName = 0) : m_PacketType(packetType), m_Socket(socket) {
            m_ulBufSize = ulBufSize + sizeof(uint64_t)*2;
            size_t stNameLen, stNameBufLen;

            if(szName) {
                stNameLen = strlen(szName);
                if(stNameLen > 245) stNameLen = 245;
                stNameBufLen = stNameLen + 1 + 1;
                stNameBufLen += sizeof(uint64_t) - stNameBufLen%sizeof(uint64_t);
                m_ulBufSize += stNameBufLen;
            }
            else {
                stNameLen = 0;
                stNameBufLen = 0;
            }
            m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];

            *reinterpret_cast<uint64_t*>(m_pucCurBuffer) = static_cast<uint64_t>(packetType);
            m_pucCurBuffer += sizeof(uint64_t);
            *reinterpret_cast<uint64_t*>(m_pucCurBuffer) = m_ulBufSize - sizeof(uint64_t) * 2;
            m_pucCurBuffer += sizeof(uint64_t);
            if(szName) {
                *reinterpret_cast<uint8_t*>(m_pucCurBuffer) = static_cast<uint8_t>(stNameBufLen);
#ifndef WIN32
                strncpy(reinterpret_cast<char*>(m_pucCurBuffer + 1), szName, stNameLen + 1);
#else
                strncpy_s(reinterpret_cast<char*>(m_pucCurBuffer + 1), stNameLen + 1, szName, stNameLen);
#endif
                m_pucCurBuffer += stNameBufLen;
            }
        }
        ~RPCSend() {
            if(m_pucBuffer) delete[] m_pucBuffer;
        }

        inline RPCSend& operator<<(OctaneEngine::Camera::CameraType const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(PanoramicCameraMode const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(ResponseCurveId const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(StereoOutput const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(StereoMode const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(RenderPassId const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(HairInterpolationType const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(OctaneClient::ImageType const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(Kernel::KernelType const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(InfoChannelType const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(Kernel::LayersMode const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(Kernel::DirectLightMode const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(Kernel::MBAlignmentType const &enumVal) {
            int32_t iVal = static_cast<int32_t>(enumVal);
            return this->operator<<(iVal);
        }

        inline RPCSend& operator<<(Environment::EnvType const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(Environment::DaylightType const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(Environment::DaylightModel const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(SceneExportTypes::SceneExportTypesEnum const &enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            return this->operator<<(uiVal);
        }

        inline RPCSend& operator<<(ComplexValue const &val) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(ComplexValue) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<ComplexValue*>(m_pucCurBuffer) = val;
                m_pucCurBuffer += sizeof(ComplexValue);
            }
            return *this;
        }

        inline RPCSend& operator<<(float const &fVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(float) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<float*>(m_pucCurBuffer) = fVal;
                m_pucCurBuffer += sizeof(float);
            }
            return *this;
        }

        inline RPCSend& operator<<(float_3 const &f3Val) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
                reinterpret_cast<float*>(m_pucCurBuffer)[0] = f3Val.x;
                reinterpret_cast<float*>(m_pucCurBuffer)[1] = f3Val.y;
                reinterpret_cast<float*>(m_pucCurBuffer)[2] = f3Val.z;
                m_pucCurBuffer += sizeof(float) * 3;
            }
            return *this;
        }

        inline RPCSend& operator<<(float_2 const &f2Val) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
                reinterpret_cast<float*>(m_pucCurBuffer)[0] = f2Val.x;
                reinterpret_cast<float*>(m_pucCurBuffer)[1] = f2Val.y;
                m_pucCurBuffer += sizeof(float) * 2;
            }
            return *this;
        }

        inline RPCSend& operator<<(double const &dVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(double) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<double*>(m_pucCurBuffer) = dVal;
                m_pucCurBuffer += sizeof(double);
            }
            return *this;
        }

        inline RPCSend& operator<<(int64_t const &lVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(int64_t) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<int64_t*>(m_pucCurBuffer) = lVal;
                m_pucCurBuffer += sizeof(int64_t);
            }
            return *this;
        }

        inline RPCSend& operator<<(uint64_t const &ulVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(uint64_t) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<uint64_t*>(m_pucCurBuffer) = ulVal;
                m_pucCurBuffer += sizeof(uint64_t);
            }
            return *this;
        }

        inline RPCSend& operator<<(uint32_t const &uiVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(uint32_t) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<uint32_t*>(m_pucCurBuffer) = uiVal;
                m_pucCurBuffer += sizeof(uint32_t);
            }
            return *this;
        }

        inline RPCSend& operator<<(int32_t const &iVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(int32_t) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<int32_t*>(m_pucCurBuffer) = iVal;
                m_pucCurBuffer += sizeof(int32_t);
            }
            return *this;
        }

        inline RPCSend& operator<<(bool const &bVal) {
            if(m_pucBuffer && (m_pucCurBuffer+sizeof(int32_t) <= m_pucBuffer+m_ulBufSize)) {
                *reinterpret_cast<uint32_t*>(m_pucCurBuffer) = bVal;
                m_pucCurBuffer += sizeof(uint32_t);
            }
            return *this;
        }

        inline RPCSend& operator<<(char const *szVal) {
            if(!szVal) return this->writeChar("");
            else return this->writeChar(szVal);
        }

        inline RPCSend& operator<<(string const &sVal) {
            return this->writeChar(sVal.c_str());
        }

        bool writeBuffer(void* pvBuf, uint64_t ulLen) {
            if(m_pucBuffer && (m_pucCurBuffer+ulLen <= m_pucBuffer+m_ulBufSize)) {
                memcpy(m_pucCurBuffer, pvBuf, static_cast<size_t>(ulLen));
                m_pucCurBuffer += ulLen;
                return true;
            }
            else return false;
        } //writeBuffer()

        inline bool writeFloat3Buffer(float_3* pf3Buf, uint64_t ulLen) {
            if(m_pucBuffer && (m_pucCurBuffer + ulLen * sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
                register float* pfPtr = (float*)m_pucCurBuffer;
                for(register uint64_t i = 0; i < ulLen; ++i) {
                    *(pfPtr++) = pf3Buf[i].x;
                    *(pfPtr++) = pf3Buf[i].y;
                    *(pfPtr++) = pf3Buf[i].z;
                }
                m_pucCurBuffer = (uint8_t*)pfPtr;
                return true;
            }
            else return false;
        } //writeFloat3Buffer()

        inline bool writeFloat2Buffer(float_2* pf2Buf, uint64_t ulLen) {
            if(m_pucBuffer && (m_pucCurBuffer + ulLen * sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
                register float* pfPtr = (float*)m_pucCurBuffer;
                for(register uint64_t i = 0; i < ulLen; ++i) {
                    *(pfPtr++) = pf2Buf[i].x;
                    *(pfPtr++) = pf2Buf[i].y;
                }
                m_pucCurBuffer = (uint8_t*)pfPtr;
                return true;
            }
            else return false;
        } //writeFloat2Buffer()

        inline bool write() {
            if(!m_pucBuffer) return false;

            unsigned int uiHeaderSize = sizeof(uint64_t) * 2;
            if(::send(m_Socket, (const char*)m_pucBuffer, uiHeaderSize, 0) < 0)
                return false;

            uint64_t ulDataBufSize          = m_ulBufSize - uiHeaderSize;
            unsigned int uiChunksCnt        = static_cast<unsigned int>(ulDataBufSize / SEND_CHUNK_SIZE);
            unsigned int uiLastChunkSize    = ulDataBufSize % SEND_CHUNK_SIZE;
            for(unsigned int i = 0; i < uiChunksCnt; ++i) {
                if(::send(m_Socket, (const char*)m_pucBuffer + uiHeaderSize + i * SEND_CHUNK_SIZE, SEND_CHUNK_SIZE, 0) < 0)
                    return false;
            }
            if(uiLastChunkSize && ::send(m_Socket, (const char*)m_pucBuffer + uiHeaderSize + uiChunksCnt * SEND_CHUNK_SIZE, uiLastChunkSize, 0) < 0)
                return false;

            delete[] m_pucBuffer;
            m_pucBuffer    = 0;
            m_ulBufSize    = 0;
            m_pucCurBuffer = 0;

            return true;
        } //write()

        inline bool writeFile(string const &path) {
            if(!m_pucBuffer || !m_ulBufSize || !path.length()) return false;
            bool bRet = false;
            uint8_t *pucBuf = 0;
            int64_t lFileSize = 0;

            FILE *hFile = ufopen(path.c_str(), "rb");
            if(!hFile) goto exit3;

#ifndef WIN32
    	    fseek(hFile, 0, SEEK_END);
    	    lFileSize = ftell(hFile);
#else
    	    _fseeki64(hFile, 0, SEEK_END);
    	    lFileSize = _ftelli64(hFile);
#endif
            rewind(hFile);

            reinterpret_cast<uint64_t*>(m_pucBuffer)[1] = lFileSize;
            if(::send(m_Socket, (const char*)m_pucBuffer, sizeof(uint64_t) * 2, 0) < 0)
                goto exit2;

            pucBuf = new uint8_t[lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize];
            while(pucBuf && lFileSize) {
                unsigned int uiSizeToRead = (lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize);

                if(!fread(pucBuf, uiSizeToRead, 1, hFile))
                    goto exit1;

                if(::send(m_Socket, (const char*)pucBuf, uiSizeToRead, 0) < 0)
                    goto exit1;

                lFileSize -= uiSizeToRead;
            }
            bRet = true;
exit1:
            if(pucBuf) delete[] pucBuf;
exit2:
            fclose(hFile);
exit3:
            delete[] m_pucBuffer;
            m_pucCurBuffer  = m_pucBuffer = 0;
            m_PacketType    = OctaneEngine::NONE;
            m_ulBufSize     = 0;

            return bRet;
        } //writeFile()

    private:
        RPCSend() {}

        inline RPCSend& writeChar(char const *szVal) {
            if(m_pucBuffer) {
                size_t stLen = strlen(szVal);
                if(m_pucCurBuffer + stLen + 2 > m_pucBuffer + m_ulBufSize) return *this;
                if(stLen > 4096) stLen = 4096;
                *reinterpret_cast<uint8_t*>(m_pucCurBuffer) = static_cast<uint8_t>(stLen);
                m_pucCurBuffer += sizeof(uint8_t);
#ifndef WIN32
                strncpy(reinterpret_cast<char*>(m_pucCurBuffer), szVal, stLen + 1);
#else
                strncpy_s(reinterpret_cast<char*>(m_pucCurBuffer), stLen+1, szVal, stLen);
#endif
                m_pucCurBuffer += stLen+1;
            }
            return *this;
        }

        PacketType  m_PacketType;
        int         m_Socket;
        uint64_t    m_ulBufSize;
        uint8_t     *m_pucBuffer;
        uint8_t     *m_pucCurBuffer;
    }; //class RPCSend

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Receive data class
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    class RPCReceive {
    public:
        RPCReceive(int socket) : m_Socket(socket), m_pucBuffer(0), m_pucCurBuffer(0) {
            uint64_t ulTmp[2];
            if(::recv(socket, (char*)ulTmp, sizeof(uint64_t) * 2, MSG_WAITALL) != sizeof(uint64_t) * 2) {
                m_PacketType = OctaneEngine::NONE;
                m_ulBufSize  = 0;
                return;
            }
            else {
                m_PacketType = static_cast<PacketType>(ulTmp[0]);
                m_ulBufSize  = ulTmp[1];
            }

            if(m_ulBufSize > 0) {
                unsigned int uiChunksCnt = static_cast<unsigned int>(m_ulBufSize / SEND_CHUNK_SIZE);
                int iLastChunkSize = static_cast<int>(m_ulBufSize % SEND_CHUNK_SIZE);

                if(m_PacketType == LOAD_FILE) {
                    m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : m_ulBufSize];
                    if(!m_pucBuffer) {
                        delete[] m_pucBuffer;
                        m_pucCurBuffer  = m_pucBuffer = 0;
                        m_PacketType    = OctaneEngine::NONE;
                        m_ulBufSize     = 0;
                        return;
                    }
                }
                else {
                    m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];
                    for(unsigned int i = 0; i < uiChunksCnt; ++i) {
                        if(::recv(socket, (char*)m_pucBuffer + i * SEND_CHUNK_SIZE, SEND_CHUNK_SIZE, MSG_WAITALL) != SEND_CHUNK_SIZE) {
                            delete[] m_pucBuffer;
                            m_pucCurBuffer  = m_pucBuffer = 0;
                            m_PacketType    = OctaneEngine::NONE;
                            m_ulBufSize     = 0;
                            return;
                        }
                    }
                    if(iLastChunkSize && ::recv(socket, (char*)m_pucBuffer + uiChunksCnt * SEND_CHUNK_SIZE, iLastChunkSize, MSG_WAITALL) != iLastChunkSize) {
                        delete[] m_pucBuffer;
                        m_pucCurBuffer  = m_pucBuffer = 0;
                        m_PacketType    = OctaneEngine::NONE;
                        m_ulBufSize     = 0;
                        return;
                    }
                }
            }
            if(m_pucBuffer && m_PacketType >= FIRST_NAMED_PACKET && m_PacketType <= LAST_NAMED_PACKET) {
                uint8_t ucLen = *reinterpret_cast<uint8_t*>(m_pucCurBuffer);
                //m_pucCurBuffer += sizeof(uint8_t);

                m_szName = reinterpret_cast<char*>(m_pucCurBuffer + 1);
                m_pucCurBuffer += ucLen;
            }
        } //RPCReceive()

        ~RPCReceive() {
            if(m_pucBuffer) delete[] m_pucBuffer;
        } //~RPCReceive()

        inline bool readFile(string &sPath, int *piErr) {
            *piErr = 0;
            if(!m_pucBuffer || !m_ulBufSize || !sPath.length()) return false;

            if(sPath[sPath.length() - 1] == '/' || sPath[sPath.length() - 1] == '\\')
                sPath.operator+=(m_szName);

            FILE *hFile = ufopen(sPath.c_str(), "wb");
            if(!hFile) {
                *piErr = errno;
                return false;
            }

            uint64_t ulCurSize = m_ulBufSize;
            while(ulCurSize) {
                int iSizeToRead = (ulCurSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : static_cast<int>(ulCurSize));
                if(::recv(m_Socket, (char*)m_pucBuffer, iSizeToRead, MSG_WAITALL) != iSizeToRead) {
                    *piErr = errno;
                    fclose(hFile);
                    delete[] m_pucBuffer;
                    m_pucCurBuffer  = m_pucBuffer = 0;
                    m_PacketType    = OctaneEngine::NONE;
                    m_ulBufSize     = 0;
                    return false;
                }
                fwrite(m_pucBuffer, iSizeToRead, 1, hFile);
                ulCurSize -= iSizeToRead;
            }
            delete[] m_pucBuffer;
            m_pucCurBuffer  = m_pucBuffer = 0;
            m_PacketType    = OctaneEngine::NONE;
            m_ulBufSize     = 0;
            fclose(hFile);

            return true;
        } //readFile()

        inline RPCReceive& operator>>(float& fVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(float) <= m_pucBuffer + m_ulBufSize)) {
                fVal = *reinterpret_cast<float*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(float);
            }
            else fVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(ComplexValue& val) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(ComplexValue) <= m_pucBuffer + m_ulBufSize)) {
                val = *reinterpret_cast<ComplexValue*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(ComplexValue);
            }
            else {
                val.iType     = 0;
                val.f3Value.x = 0;
                val.f3Value.y = 0;
                val.f3Value.z = 0;
            }
            return *this;
        }

        inline RPCReceive& operator>>(float_3& f3Val) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
                f3Val.x = reinterpret_cast<float*>(m_pucCurBuffer)[0];
                f3Val.y = reinterpret_cast<float*>(m_pucCurBuffer)[1];
                f3Val.z = reinterpret_cast<float*>(m_pucCurBuffer)[2];
                m_pucCurBuffer += sizeof(float) * 3;
            }
            else {
                f3Val.x = 0;
                f3Val.y = 0;
                f3Val.z = 0;
            }
            return *this;
        }

        inline RPCReceive& operator>>(double& dVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(double) <= m_pucBuffer + m_ulBufSize)) {
                dVal = *reinterpret_cast<double*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(double);
            }
            else dVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(bool& bVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
                bVal = (*reinterpret_cast<uint32_t*>(m_pucCurBuffer) != 0);
                m_pucCurBuffer += sizeof(uint32_t);
            }
            else bVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(int64_t& lVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(int64_t) <= m_pucBuffer + m_ulBufSize)) {
                lVal = *reinterpret_cast<int64_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(int64_t);
            }
            else lVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(uint64_t& ulVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(uint64_t) <= m_pucBuffer + m_ulBufSize)) {
                ulVal = *reinterpret_cast<uint64_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(uint64_t);
            }
            else ulVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(uint32_t& uiVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
                uiVal = *reinterpret_cast<uint32_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(uint32_t);
            }
            else uiVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(RenderPassId& enumVal) {
            uint32_t uiVal = static_cast<uint32_t>(enumVal);
            this->operator>>(uiVal);
            enumVal = static_cast<RenderPassId>(uiVal);
            return *this;
        }

        inline RPCReceive& operator>>(int32_t& iVal) {
            if(m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
                iVal = *reinterpret_cast<int32_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(int32_t);
            }
            else iVal = 0;
            return *this;
        }

        inline RPCReceive& operator>>(char*& szVal) {
            if(m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
                uint8_t ucLen = *reinterpret_cast<uint8_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(uint8_t);
                if(m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
                    szVal = "";
                    return *this;
                }
                szVal = reinterpret_cast<char*>(m_pucCurBuffer);
                m_pucCurBuffer += ucLen + 1;
            }
            else szVal = "";
            return *this;
        }

        inline RPCReceive& operator>>(string& sVal) {
            if(m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
                uint8_t ucLen = *reinterpret_cast<uint8_t*>(m_pucCurBuffer);
                m_pucCurBuffer += sizeof(uint8_t);
                if(m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
                    sVal = "";
                    return *this;
                }
                sVal = reinterpret_cast<char*>(m_pucCurBuffer);
                m_pucCurBuffer += ucLen + 1;
            }
            else sVal = "";
            return *this;
        }

        inline void* readBuffer(uint64_t ulLen) {
            if(m_pucBuffer && (m_pucCurBuffer + ulLen <= m_pucBuffer + m_ulBufSize)) {
                void* pvRet = reinterpret_cast<void*>(m_pucCurBuffer);
                m_pucCurBuffer += ulLen;
                return pvRet;
            }
            else return 0;
        }

        PacketType  m_PacketType;

    private:
        RPCReceive() {}

        int      m_Socket;
        char*    m_szName;

        uint64_t m_ulBufSize;
        uint8_t  *m_pucBuffer;
        uint8_t  *m_pucCurBuffer;
    }; //class RPCReceive
}; //class OctaneClient


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inline methods
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::OctaneClient() : m_bRenderStarted(false), m_cBlockUpdates(0), m_iComponentCnt(0), m_stImgBufLen(0), m_pucImageBuf(0), m_pfImageBuf(0), m_iCurImgBufWidth(0), m_iCurImgBufHeight(0), m_iCurRegionWidth(0),
                               m_iCurRegionHeight(0), m_Socket(-1), m_ExportSceneType(SceneExportTypes::NONE), m_bDeepImage(false), m_FailReason(FailReasons::NONE), m_CurPassType(Octane::RenderPassId::PASS_NONE) {
        
#ifdef _WIN32
    ::InitializeCriticalSection(&m_SocketMutex);
    ::InitializeCriticalSection(&m_ImgBufMutex);
#else
    pthread_mutex_init(&m_SocketMutex, 0);
    pthread_mutex_init(&m_ImgBufMutex, 0);
#endif
    m_sOutPath = "";
} //OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::~OctaneClient() {
    if(m_Socket >= 0)
#ifndef WIN32
        close(m_Socket);
#else
        closesocket(m_Socket);
#endif
    if(m_pucImageBuf) delete[] m_pucImageBuf;
    if(m_pfImageBuf) delete[] m_pfImageBuf;

#ifdef _WIN32
    ::DeleteCriticalSection(&m_SocketMutex);
    ::DeleteCriticalSection(&m_ImgBufMutex);
#else
    pthread_mutex_destroy(&m_SocketMutex);
    pthread_mutex_destroy(&m_ImgBufMutex);
#endif
} //~OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setOutputPath(const char *szOutPath) {
    m_sOutPath = szOutPath;
} //setOutputPath()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setExportType(const SceneExportTypes::SceneExportTypesEnum exportSceneType) {
    m_ExportSceneType = exportSceneType;
} //setExportType()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::connectToServer(const char *szAddr) {
    LOCK_MUTEX(m_SocketMutex);

    struct  hostent *host;
    struct  sockaddr_in sa;

    m_ServerInfo.sNetAddress  = szAddr;

    m_sAddress = szAddr;
    host = gethostbyname(szAddr);
    if(!host || host->h_length != sizeof(struct in_addr)) {
        m_FailReason = FailReasons::UNKNOWN;

        UNLOCK_MUTEX(m_SocketMutex);
        return false;
    }

    memset(&sa, 0, sizeof(sa));
    sa.sin_family = AF_INET;

    if(m_Socket < 0) {
#ifdef __APPLE__
        m_Socket = ::socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
#else
        m_Socket = ::socket(AF_INET, SOCK_STREAM, 0);
#endif
        if(m_Socket < 0) {
            m_FailReason = FailReasons::UNKNOWN;

            UNLOCK_MUTEX(m_SocketMutex);
            return false;
        }
#ifdef __APPLE__
        int value = 1;
        ::setsockopt(m_Socket, SOL_SOCKET, SO_NOSIGPIPE, &value, sizeof(value));
#endif

        sa.sin_family = AF_INET;
        sa.sin_port = htons(0);
        sa.sin_addr.s_addr = htonl(INADDR_ANY);
        if(::bind(m_Socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
            close(m_Socket);
#else
            closesocket(m_Socket);
#endif
            m_FailReason = FailReasons::UNKNOWN;
            m_Socket = -1;

            UNLOCK_MUTEX(m_SocketMutex);
            return false;
        }
    }

    sa.sin_port = htons(SERVER_PORT);
    sa.sin_addr = *(struct in_addr*) host->h_addr;
    if(::connect(m_Socket, (struct sockaddr*) &sa, sizeof(sa)) < 0) {
#ifndef WIN32
        close(m_Socket);
#else
        closesocket(m_Socket);
#endif
        m_FailReason = FailReasons::NO_CONNECTION;
        m_Socket = -1;

        UNLOCK_MUTEX(m_SocketMutex);
        return false;
    }

    UNLOCK_MUTEX(m_SocketMutex);
    if(!checkServerVersion()) return false;

    LOCK_MUTEX(m_SocketMutex);
    m_FailReason = FailReasons::NONE;

    //m_ServerInfo.sNetAddress  = szAddr;
    m_ServerInfo.sDescription = "";

    UNLOCK_MUTEX(m_SocketMutex);
    return true;
} //connectToServer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::disconnectFromServer() {
    LOCK_MUTEX(m_SocketMutex);

    if(m_Socket >= 0) {
#ifndef WIN32
        close(m_Socket);
#else
        closesocket(m_Socket);
#endif
        m_Socket = -1;
    }
        
    m_ServerInfo.sNetAddress  = "";
    m_ServerInfo.sDescription = "";
    m_ServerInfo.gpuNames.clear();

    UNLOCK_MUTEX(m_SocketMutex);
    return true;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkServerConnection() {
    bool bRet;
    LOCK_MUTEX(m_SocketMutex);

    if(m_Socket < 0) bRet = false;
    else {
        int iError = 0;
        socklen_t iLen = sizeof(iError);
        int iRet = ::getsockopt(m_Socket, SOL_SOCKET, SO_ERROR, (char*)(&iError), &iLen);

        if(iRet != 0)
            bRet = false;
        else if(iError != 0) {
            //fprintf(stderr, "socket error: %s\n", strerror(error));
            bRet = false;
        }
        else {
            RPCSend snd(m_Socket, 0, TEST_PACKET);
            if(snd.write()) bRet = true;
            else bRet = false;
        }
    }

    if(!bRet) {
        if(m_Socket >= 0) {
#ifndef WIN32
            close(m_Socket);
#else
            closesocket(m_Socket);
#endif
            m_Socket = -1;
        }
        
        //m_ServerInfo.sNetAddress  = "";
        m_ServerInfo.sDescription = "";
        m_ServerInfo.gpuNames.clear();
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return bRet;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline const string& OctaneClient::getServerErrorMessage() {
    return m_sErrorMsg;
} //getServerErrorMessage()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::clearServerErrorMessage() {
    m_sErrorMsg.clear();
} //clearServerErrorMessage()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkServerVersion() {
    if(m_Socket < 0) return false;

    LOCK_MUTEX(m_SocketMutex);

    m_ServerInfo.gpuNames.clear();
    RPCSend snd(m_Socket, 0, DESCRIPTION);
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != DESCRIPTION) {
        m_FailReason = FailReasons::UNKNOWN;

        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR getting render-server description.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");

        UNLOCK_MUTEX(m_SocketMutex);
        return false;
    }
    else {
        m_FailReason = FailReasons::NONE;

        uint32_t maj_num, min_num, num_gpus;
        bool active;
        rcv >> maj_num >> min_num >> num_gpus >> active;

        if(maj_num != OCTANE_SERVER_MAJOR_VERSION || min_num != OCTANE_SERVER_MINOR_VERSION) {
            m_FailReason = FailReasons::WRONG_VERSION;
            fprintf(stderr, "Octane: ERROR: Wrong version of render-server (%d.%d), %d.%d is needed\n",
                    maj_num, min_num, OCTANE_SERVER_MAJOR_VERSION, OCTANE_SERVER_MINOR_VERSION);

            if(m_Socket >= 0)
#ifndef WIN32
                close(m_Socket);
#else
                closesocket(m_Socket);
#endif
            m_Socket = -1;
            UNLOCK_MUTEX(m_SocketMutex);
            return false;
        }
        
        if(num_gpus) {
            m_ServerInfo.gpuNames.resize(num_gpus);
            string *str = &m_ServerInfo.gpuNames[0];
            for(uint32_t i = 0; i < num_gpus; ++i) rcv >> str[i];
        }
        else {
			m_FailReason = FailReasons::NO_GPUS;
            fprintf(stderr, "Octane: ERROR: no available CUDA GPUs on a server\n");
		}

        if(!active) {
			m_FailReason = FailReasons::NOT_ACTIVATED;
            fprintf(stderr, "Octane: ERROR: server is not activated\n");
		}

        UNLOCK_MUTEX(m_SocketMutex);
        return m_FailReason == FailReasons::NONE;
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
} //checkServerVersion()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::activate(string const &sStandLogin, string const &sStandPass, string const &sLogin, string const &sPass) {
    if(m_Socket < 0) return false;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, sStandLogin.length()+2 + sStandPass.length()+2 + sLogin.length()+2 + sPass.length()+2, SET_LIC_DATA);
    snd << sStandLogin << sStandPass << sLogin << sPass;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != SET_LIC_DATA) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR of the license activation on render-server.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");

        UNLOCK_MUTEX(m_SocketMutex);
        return false;
    }
    else {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
} //activate()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::reset(SceneExportTypes::SceneExportTypesEnum exportSceneType, uint32_t uiGPUs, float fFrameTimeSampling, float fFps, bool bDeepImage) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    m_bUnpackedTexturesMsgShown = false;

    LOCK_MUTEX(m_SocketMutex);

    m_ExportSceneType = exportSceneType;
    m_bDeepImage      = bDeepImage;

    RPCSend snd(m_Socket, sizeof(float) * 2 + sizeof(uint32_t) * 2, RESET);
    snd << fFrameTimeSampling << fFps << m_ExportSceneType << bDeepImage;

    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != RESET) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR resetting render server.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_CameraCache.clear();
        m_KernelCache.clear();
        m_PassesCache.clear();
        m_EnvironmentCache.clear();
        m_VisibleEnvironmentCache.clear();
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::clear() {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    m_bUnpackedTexturesMsgShown = false;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, 0, CLEAR);
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != CLEAR) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR clearing render server.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_CameraCache.clear();
        m_KernelCache.clear();
        m_PassesCache.clear();
        m_EnvironmentCache.clear();
        m_VisibleEnvironmentCache.clear();
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //clear()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::update() {
    if(m_Socket < 0 || m_cBlockUpdates) return false;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, 0, UPDATE);
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != UPDATE) {
        UNLOCK_MUTEX(m_SocketMutex);
        return false;
    }
    else {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
} //update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::startRender(bool bInteractive, int32_t iWidth, int32_t iHeigth, ImageType imgType, bool bOutOfCoreEnabled, int32_t iOutOfCoreMemLimit, int32_t iOutOfCoreGPUHeadroom) {
    if(m_bRenderStarted) m_bRenderStarted = false;

    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, sizeof(int32_t) * 5 + sizeof(uint32_t) * 2, START);
    snd << bInteractive << bOutOfCoreEnabled << iOutOfCoreMemLimit << iOutOfCoreGPUHeadroom << iWidth << iHeigth << imgType;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != START) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR starting render.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else m_bRenderStarted = true;

    UNLOCK_MUTEX(m_SocketMutex);
} //startRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
#   pragma warning (push)
#   pragma warning (disable : 4706)
#endif
inline void OctaneClient::stopRender(float fFPS) {
    if(m_Socket < 0) return;
    if(m_cBlockUpdates) m_cBlockUpdates = 0;

    LOCK_MUTEX(m_SocketMutex);

    bool is_alembic = (m_ExportSceneType == SceneExportTypes::ALEMBIC ? true : false);
    RPCSend snd(m_Socket, m_ExportSceneType != SceneExportTypes::NONE ? sizeof(float) + sizeof(uint32_t) : 0, STOP);
    if(m_ExportSceneType != SceneExportTypes::NONE) snd << fFPS << is_alembic;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != STOP) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR stopping render.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else if(m_ExportSceneType != SceneExportTypes::NONE && m_sOutPath.length()) {
        int err;
        RPCReceive rcv(m_Socket);
        string s_out_path(m_sOutPath);
        if(m_ExportSceneType == SceneExportTypes::ALEMBIC) s_out_path += ".abc";
        else s_out_path += ".orbx";
            
        if(rcv.m_PacketType != LOAD_FILE) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR downloading scene file from server.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
        else if(!rcv.readFile(s_out_path, &err)) {
            char *err_str;
            fprintf(stderr, "Octane: ERROR downloading scene file from server.");
            if(err && (err_str = strerror(err)) && err_str[0]) fprintf(stderr, " Description: %s\n", err_str);
            else fprintf(stderr, "\n");
        }
#ifdef _WIN32
#   pragma warning (pop)
#endif
    }
    else if(m_bDeepImage && m_sOutPath.length()) {
        int err;
        RPCReceive rcv(m_Socket);
        string s_out_path(m_sOutPath);
        s_out_path += "_deep.exr";
            
        if(rcv.m_PacketType != LOAD_FILE) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
        else if(!rcv.readFile(s_out_path, &err)) {
            char *err_str;
            fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
            if(err && (err_str = strerror(err)) && err_str[0]) fprintf(stderr, " Description: %s\n", err_str);
            else fprintf(stderr, "\n");
        }
    }

    m_CameraCache.clear();
    m_KernelCache.clear();
    m_PassesCache.clear();
    m_EnvironmentCache.clear();
    m_VisibleEnvironmentCache.clear();

    UNLOCK_MUTEX(m_SocketMutex);

    m_bRenderStarted = false;
} //stopRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::isRenderStarted() {
    return m_bRenderStarted;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::pauseRender(int32_t bPause) {
    if(m_Socket < 0) return;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, sizeof(int32_t), PAUSE);
    snd << bPause;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != PAUSE) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR pause render.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //pauseRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::startFrameUpload() {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, 0, START_FRAME_LOAD);
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != START_FRAME_LOAD) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR starting frame load.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //startFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::finishFrameUpload(bool bUpdate) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, sizeof(int32_t), FINISH_FRAME_LOAD);
    snd << bUpdate;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != FINISH_FRAME_LOAD) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR finishing frame load.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //finishFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadGPUs(uint32_t uiGPUs) {
    if(m_Socket < 0) return;

    LOCK_MUTEX(m_SocketMutex);

    RPCSend snd(m_Socket, sizeof(uint32_t), LOAD_GPU);
    snd << uiGPUs;
    snd.write();

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_GPU) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR setting GPUs on render server.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadGPUs()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadCamera(Camera *pCamera, uint32_t uiFrameIdx, uint32_t uiTotalFrames) {
    if(m_Socket < 0 || m_cBlockUpdates || !pCamera) return;

    size_t stCacheSize = m_CameraCache.size();
    if(uiTotalFrames && stCacheSize != uiTotalFrames) {
        std::vector<Camera>().swap(m_CameraCache);
        m_CameraCache.resize(uiTotalFrames);
    }
    else if(stCacheSize > uiFrameIdx && *pCamera == m_CameraCache[uiFrameIdx]) return;

    LOCK_MUTEX(m_SocketMutex);

    if(pCamera->type == Camera::CAMERA_PANORAMA) {
        {
            RPCSend snd(m_Socket, sizeof(float_3) * 6 + sizeof(float) * 19 + sizeof(int32_t) * 13, LOAD_PANORAMIC_CAMERA);
            snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance 

                << pCamera->fFOVx << pCamera->fFOVy << pCamera->fNearClipDepth << pCamera->fFarClipDepth << pCamera->fExposure
                << pCamera->fGamma << pCamera->fVignetting << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
                << pCamera->fBloomPower << pCamera->fGlarePower << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity << pCamera->fHighlightCompression
                << pCamera->fBlackoutLat << pCamera->fStereoDist << pCamera->fStereoDistFalloff

                << pCamera->panCamMode << pCamera->responseCurve << pCamera->iMinDisplaySamples << pCamera->iGlareRayCount << pCamera->stereoOutput << pCamera->iMaxTonemapInterval
                    
                << pCamera->bPremultipliedAlpha << pCamera->bDithering << pCamera->bUsePostprocess << pCamera->bKeepUpright << pCamera->bNeutralResponse << pCamera->bDisablePartialAlpha;
            snd.write();
        }

        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != LOAD_PANORAMIC_CAMERA) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR loading camera.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
        else {
            m_CameraCache[uiFrameIdx] = *pCamera;
        }
    }
    else if(pCamera->type == Camera::CAMERA_BAKING) {
        {
            RPCSend snd(m_Socket, sizeof(float_3) * 2 + sizeof(float_2) * 2 + sizeof(float) * 9 + sizeof(int32_t) * 15, LOAD_BAKING_CAMERA);
            snd << pCamera->f3EyePoint << pCamera->f3WhiteBalance << pCamera->f2UVboxMin << pCamera->f2UVboxSize

                << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting
                << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
                << pCamera->fBloomPower << pCamera->fGlarePower << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity << pCamera->fHighlightCompression << pCamera->fTolerance

                << pCamera->responseCurve << pCamera->iMinDisplaySamples << pCamera->iGlareRayCount << pCamera->iMaxTonemapInterval << pCamera->iBakingGroupId << pCamera->iPadding << pCamera->iUvSet

                << pCamera->bPremultipliedAlpha << pCamera->bDithering
                << pCamera->bUsePostprocess << pCamera->bNeutralResponse << pCamera->bBakeOutwards << pCamera->bUseBakingPosition << pCamera->bBackfaceCulling << pCamera->bDisablePartialAlpha;
            snd.write();
        }

        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != LOAD_BAKING_CAMERA) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR loading camera.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
        else {
            m_CameraCache[uiFrameIdx] = *pCamera;
        }
    }
    else {
        {
            RPCSend snd(m_Socket, sizeof(float_3)*6 + sizeof(float)*26 + sizeof(int32_t) * 17 + sizeof(uint32_t) * 2, LOAD_THIN_LENS_CAMERA);
            snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance 

                << pCamera->fAperture << pCamera->fApertureEdge << pCamera->fDistortion << pCamera->fFocalDepth << pCamera->fNearClipDepth << pCamera->fFarClipDepth << pCamera->f2LensShift.x << pCamera->f2LensShift.y
                << pCamera->fStereoDist << pCamera->fFOV << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting
                << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
                << pCamera->fBloomPower << pCamera->fGlarePower << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity << pCamera->fHighlightCompression
                << pCamera->fPixelAspect << pCamera->fApertureAspect

                << pCamera->responseCurve << pCamera->iMinDisplaySamples << pCamera->iGlareRayCount << pCamera->stereoMode << pCamera->stereoOutput << pCamera->iMaxTonemapInterval << uiFrameIdx << uiTotalFrames

                << pCamera->bOrtho << pCamera->bAutofocus
                << pCamera->bPremultipliedAlpha << pCamera->bDithering
                << pCamera->bUsePostprocess << pCamera->bPerspCorr << pCamera->bNeutralResponse << pCamera->bUseFstopValue << pCamera->bDisablePartialAlpha << pCamera->bSwapEyes;
            snd.write();
        }

        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != LOAD_THIN_LENS_CAMERA) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR loading camera.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
        else {
            m_CameraCache[uiFrameIdx] = *pCamera;
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadCamera()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadPasses(Passes *pPasses) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint32_t uiTotalFrames = 1, uiFrameIdx = 0;//Temp

    size_t stCacheSize = m_PassesCache.size();
    if(uiTotalFrames && stCacheSize != uiTotalFrames) {
        std::vector<Passes>().swap(m_PassesCache);
        m_PassesCache.resize(uiTotalFrames);
    }
    else if(stCacheSize > uiFrameIdx && *pPasses == m_PassesCache[uiFrameIdx]) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, sizeof(float) * 5 + sizeof(int32_t) * 63, LOAD_PASSES);
        snd << pPasses->fZdepthMax << pPasses->fUVMax << pPasses->fMaxSpeed << pPasses->fAODistance << pPasses->fOpacityThreshold
            << pPasses->bUsePasses << pPasses->curPassType << pPasses->iMaxSamples << pPasses->iSamplingMode << pPasses->bPassesRaw << pPasses->bPostProcEnvironment << pPasses->bBump << pPasses->bAoAlphaShadows

            << pPasses->bBeautyPass << pPasses->bEmittersPass << pPasses->bEnvironmentPass << pPasses->bDiffusePass << pPasses->bDiffuseDirectPass << pPasses->bDiffuseIndirectPass << pPasses->bDiffuseFilterPass << pPasses->bReflectionPass << pPasses->bReflectionDirectPass << pPasses->bReflectionIndirectPass << pPasses->bReflectionFilterPass
            << pPasses->bRefractionPass << pPasses->bRefractionFilterPass << pPasses->bTransmissionPass << pPasses->bTransmissionFilterPass << pPasses->bSubsurfScatteringPass << pPasses->bPostProcessingPass

            << pPasses->bGeomNormalsPass << pPasses->bShadingNormalsPass << pPasses->bVertexNormalsPass << pPasses->bTangentNormalsPass << pPasses->bPositionPass << pPasses->bZdepthPass << pPasses->bMaterialIdPass << pPasses->bUVCoordinatesPass
            << pPasses->bTangentsPass << pPasses->bWireframePass << pPasses->bObjectIdPass << pPasses->bAOPass << pPasses->bMotionVectorPass
            << pPasses->bLayerShadowsPass << pPasses->bLayerBlackShadowsPass << pPasses->bLayerColorShadowsPass << pPasses->bLayerReflectionsPass
            << pPasses->bLayerIdPass << pPasses->bLayerMaskPass
            << pPasses->bLightPassIdPass
            << pPasses->bAmbientLightPass << pPasses->bSunlightPass << pPasses->bLight1Pass << pPasses->bLight2Pass << pPasses->bLight3Pass
            << pPasses->bLight4Pass << pPasses->bLight5Pass << pPasses->bLight6Pass << pPasses->bLight7Pass << pPasses->bLight8Pass
            << pPasses->bBackinGroupIdPass << pPasses->bOpacityPass << pPasses->bRoughnessPass << pPasses->bIorPass << pPasses->bDiffuseFilterInfoPass << pPasses->bReflectionFilterInfoPass << pPasses->bRefractionFilterInfoPass << pPasses->bTransmissionFilterInfoPass;
        snd.write();
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_PASSES) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading render passes.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_PassesCache[uiFrameIdx] = *pPasses;
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadPasses()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadKernel(Kernel *pKernel) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint32_t uiTotalFrames = 1, uiFrameIdx = 0; //Temp

    size_t stCacheSize = m_KernelCache.size();
    if(uiTotalFrames && stCacheSize != uiTotalFrames) {
        std::vector<Kernel>().swap(m_KernelCache);
        m_KernelCache.resize(uiTotalFrames);
    }
    else if(stCacheSize > uiFrameIdx && *pKernel == m_KernelCache[uiFrameIdx]) return;

    LOCK_MUTEX(m_SocketMutex);

    switch(pKernel->type) {
        case Kernel::DIRECT_LIGHT:
        {
            RPCSend snd(m_Socket, sizeof(float) * 7 + sizeof(int32_t) * 20 + pKernel->sAoTexture.length() + 2, LOAD_KERNEL);
            snd << pKernel->type << pKernel->iMaxSamples << pKernel->fShutterTime << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fCoherentRatio << pKernel->fAODist << pKernel->fDepthTolerance
                << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bStaticNoise << pKernel->bKeepEnvironment << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
                << pKernel->iSpecularDepth << pKernel->iGlossyDepth << pKernel->GIMode << pKernel->iDiffuseDepth << pKernel->iParallelSamples << pKernel->iMaxTileSamples << pKernel->iMaxDepthSamples << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
                << pKernel->sAoTexture;
            snd.write();
        }
            break;
        case Kernel::PATH_TRACE:
        {
            RPCSend snd(m_Socket, sizeof(float) * 8 + sizeof(int32_t) * 18, LOAD_KERNEL);
            snd << pKernel->type << pKernel->iMaxSamples << pKernel->fShutterTime << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fCoherentRatio << pKernel->fCausticBlur << pKernel->fGIClamp << pKernel->fDepthTolerance
                << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bStaticNoise << pKernel->bKeepEnvironment << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
                << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth << pKernel->iParallelSamples << pKernel->iMaxTileSamples << pKernel->iMaxDepthSamples << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode;
            snd.write();
        }
            break;
        case Kernel::PMC:
        {
            RPCSend snd(m_Socket, sizeof(float) * 8 + sizeof(int32_t) * 15, LOAD_KERNEL);
            snd << pKernel->type << pKernel->iMaxSamples << pKernel->fShutterTime << pKernel->fFilterSize << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fExploration << pKernel->fDLImportance << pKernel->fCausticBlur << pKernel->fGIClamp
                << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bKeepEnvironment
                << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth << pKernel->iMaxRejects << pKernel->iParallelism << pKernel->iWorkChunkSize << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode;
            snd.write();
        }
            break;
        case Kernel::INFO_CHANNEL:
        {
            RPCSend snd(m_Socket, sizeof(float) * 8 + sizeof(int32_t) * 16, LOAD_KERNEL);
            snd << pKernel->type << pKernel->infoChannelType << pKernel->fShutterTime << pKernel->fFilterSize << pKernel->fZdepthMax << pKernel->fUVMax << pKernel->fRayEpsilon << pKernel->fAODist << pKernel->fMaxSpeed << pKernel->fOpacityThreshold
                << pKernel->bAlphaChannel << pKernel->bBumpNormalMapping << pKernel->bBkFaceHighlight << pKernel->bAoAlphaShadows << pKernel->bMinimizeNetTraffic
                << pKernel->iSamplingMode << pKernel->iMaxSamples << pKernel->iParallelSamples << pKernel->iMaxTileSamples << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode;
            snd.write();
        }
            break;
        default:
        {
            RPCSend snd(m_Socket, sizeof(int32_t) * 6 + sizeof(float), LOAD_KERNEL);
            OctaneEngine::Kernel::KernelType defType = OctaneEngine::Kernel::DEFAULT;
            snd << defType << pKernel->mbAlignment << pKernel->fShutterTime << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode;
            snd.write();
        }
            break;
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_KERNEL) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading kernel.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_KernelCache[uiFrameIdx] = *pKernel;
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadKernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRenderRegion(Camera *pCamera, bool bInteractive) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, sizeof(uint32_t) * 5, LOAD_RENDER_REGION);
        if(pCamera->bUseRegion)
            snd << pCamera->ui4Region.x << pCamera->ui4Region.y << pCamera->ui4Region.z << pCamera->ui4Region.w << bInteractive;
        else {
            uint32_t tmp = 0;
            snd << tmp << tmp << tmp << tmp;
        }
        snd.write();
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_RENDER_REGION) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR setting render region.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadRenderRegion()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadEnvironment(Environment *pEnv) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint32_t uiTotalFrames = 1, uiFrameIdx = 0; //Temp

    size_t stCacheSize = m_EnvironmentCache.size();
    if(uiTotalFrames && stCacheSize != uiTotalFrames) {
        std::vector<Environment>().swap(m_EnvironmentCache);
        m_EnvironmentCache.resize(uiTotalFrames);
    }
    else if(stCacheSize > uiFrameIdx && *pEnv == m_EnvironmentCache[uiFrameIdx]) return;

    LOCK_MUTEX(m_SocketMutex);

    if(pEnv->type == 0) {
        RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 2 + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_SUNSKY);
        snd << pEnv->type << pEnv->type << pEnv->fPower << pEnv->fMediumRadius << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
        snd.write();
    }
    else {
        if(pEnv->daylightType == Environment::DIRECTION) {
            RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 19 + sizeof(int32_t) + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_SUNSKY);
            snd << pEnv->type << pEnv->daylightType << pEnv->f3SunVector.x << pEnv->f3SunVector.y << pEnv->f3SunVector.z << pEnv->fPower << pEnv->fTurbidity << pEnv->fNorthOffset
                << pEnv->fSunSize << pEnv->fMediumRadius << pEnv->fGroundStartAngle << pEnv->fGroundBlendAngle
                << pEnv->f3SkyColor.x << pEnv->f3SkyColor.y << pEnv->f3SkyColor.z << pEnv->f3SunsetColor.x << pEnv->f3SunsetColor.y << pEnv->f3SunsetColor.z
                << pEnv->f3GroundColor.x << pEnv->f3GroundColor.y << pEnv->f3GroundColor.z
                << pEnv->model << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
            snd.write();
        }
        else {
            RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 19 + sizeof(int32_t) * 4 + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_SUNSKY);
            snd << pEnv->type << pEnv->daylightType << pEnv->fLongitude << pEnv->fLatitude << pEnv->fHour << pEnv->fPower << pEnv->fTurbidity << pEnv->fNorthOffset
                << pEnv->fSunSize << pEnv->fMediumRadius << pEnv->fGroundStartAngle << pEnv->fGroundBlendAngle
                << pEnv->f3SkyColor.x << pEnv->f3SkyColor.y << pEnv->f3SkyColor.z << pEnv->f3SunsetColor.x << pEnv->f3SunsetColor.y << pEnv->f3SunsetColor.z
                << pEnv->f3GroundColor.x << pEnv->f3GroundColor.y << pEnv->f3GroundColor.z
                << pEnv->model << pEnv->iMonth << pEnv->iDay << pEnv->iGMTOffset << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
            snd.write();
        }
    }
    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_SUNSKY) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading environment.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_EnvironmentCache[uiFrameIdx] = *pEnv;
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadEnvironment()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadVisibleEnvironment(Environment *pEnv) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint32_t uiTotalFrames = 1, uiFrameIdx = 0; //Temp

    size_t stCacheSize = m_VisibleEnvironmentCache.size();
    if(uiTotalFrames && stCacheSize != uiTotalFrames) {
        std::vector<Environment>().swap(m_VisibleEnvironmentCache);
        m_VisibleEnvironmentCache.resize(uiTotalFrames);
    }
    else if(stCacheSize > uiFrameIdx && *pEnv == m_VisibleEnvironmentCache[uiFrameIdx]) return;

    LOCK_MUTEX(m_SocketMutex);

    if(pEnv->type == 0) {
        RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 2 + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_VISIBLE_SUNSKY);
        snd << pEnv->type << pEnv->type << pEnv->fPower << pEnv->fMediumRadius << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
        snd.write();
    }
    else {
        if(pEnv->daylightType == Environment::DIRECTION) {
            RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 19 + sizeof(int32_t) + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_VISIBLE_SUNSKY);
            snd << pEnv->type << pEnv->daylightType << pEnv->f3SunVector.x << pEnv->f3SunVector.y << pEnv->f3SunVector.z << pEnv->fPower << pEnv->fTurbidity << pEnv->fNorthOffset
                << pEnv->fSunSize << pEnv->fMediumRadius << pEnv->fGroundStartAngle << pEnv->fGroundBlendAngle
                << pEnv->f3SkyColor.x << pEnv->f3SkyColor.y << pEnv->f3SkyColor.z << pEnv->f3SunsetColor.x << pEnv->f3SunsetColor.y << pEnv->f3SunsetColor.z
                << pEnv->f3GroundColor.x << pEnv->f3GroundColor.y << pEnv->f3GroundColor.z
                << pEnv->model << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
            snd.write();
        }
        else {
            RPCSend snd(m_Socket, sizeof(uint32_t) * 6 + sizeof(float) * 19 + sizeof(int32_t) * 4 + pEnv->sTexture.length() + 2 + pEnv->sMedium.length() + 2, LOAD_VISIBLE_SUNSKY);
            snd << pEnv->type << pEnv->daylightType << pEnv->fLongitude << pEnv->fLatitude << pEnv->fHour << pEnv->fPower << pEnv->fTurbidity << pEnv->fNorthOffset
                << pEnv->fSunSize << pEnv->fMediumRadius << pEnv->fGroundStartAngle << pEnv->fGroundBlendAngle
                << pEnv->f3SkyColor.x << pEnv->f3SkyColor.y << pEnv->f3SkyColor.z << pEnv->f3SunsetColor.x << pEnv->f3SunsetColor.y << pEnv->f3SunsetColor.z
                << pEnv->f3GroundColor.x << pEnv->f3GroundColor.y << pEnv->f3GroundColor.z
                << pEnv->model << pEnv->iMonth << pEnv->iDay << pEnv->iGMTOffset << pEnv->bImportanceSampling << pEnv->bVisibleBackplate << pEnv->bVisibleReflections << pEnv->bVisibleRefractions << pEnv->sTexture.c_str() << pEnv->sMedium.c_str();
            snd.write();
        }
    }
    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_VISIBLE_SUNSKY) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading visible environment.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }
    else {
        m_VisibleEnvironmentCache[uiFrameIdx] = *pEnv;
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadVisibleEnvironment()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadNode(OctaneNodeBase *pNodeData) {
    switch(pNodeData->nodeType) {
        //case Octane::NT_BOOL:
        //case Octane::NT_STRING:
        //case Octane::NT_ENUM:
        case Octane::NT_FLOAT:
            uploadFloatValue((OctaneEngine::OctaneFloatValue*)pNodeData);
            break;
        case Octane::NT_INT:
            uploadIntValue((OctaneEngine::OctaneIntValue*)pNodeData);
            break;

        case Octane::NT_EMIS_BLACKBODY:
            uploadBbodyEmission((OctaneEngine::OctaneBlackBodyEmission*)pNodeData);
            break;
        case Octane::NT_EMIS_TEXTURE:
            uploadTextureEmission((OctaneEngine::OctaneTextureEmission*)pNodeData);
            break;
        case Octane::NT_MAT_DIFFUSE:
            uploadDiffuseMat((OctaneEngine::OctaneDiffuseMaterial*)pNodeData);
            break;
        case Octane::NT_MAT_GLOSSY:
            uploadGlossyMat((OctaneEngine::OctaneGlossyMaterial*)pNodeData);
            break;
        case Octane::NT_MAT_MIX:
            uploadMixMat((OctaneEngine::OctaneMixMaterial*)pNodeData);
            break;
        case Octane::NT_MAT_PORTAL:
            uploadPortalMat((OctaneEngine::OctanePortalMaterial*)pNodeData);
            break;
        case Octane::NT_MAT_SPECULAR:
            uploadSpecularMat((OctaneEngine::OctaneSpecularMaterial*)pNodeData);
            break;
        case Octane::NT_MED_ABSORPTION:
            uploadAbsorptionMedium((OctaneEngine::OctaneAbsorptionMedium*)pNodeData);
            break;
        case Octane::NT_MED_SCATTERING:
            uploadScatteringMedium((OctaneEngine::OctaneScatteringMedium*)pNodeData);
            break;
        case Octane::NT_MED_VOLUME:
            uploadVolumeMedium((OctaneEngine::OctaneVolumeMedium*)pNodeData);
            break;
        //case Octane::NT_PHASE_SCHLICK:
        //    break;
        case Octane::NT_PROJ_BOX:
            uploadBoxProjection((OctaneEngine::OctaneBoxProjection*)pNodeData);
            break;
        case Octane::NT_PROJ_CYLINDRICAL:
            uploadCylProjection((OctaneEngine::OctaneCylProjection*)pNodeData);
            break;
        case Octane::NT_PROJ_LINEAR:
            uploadXyzProjection((OctaneEngine::OctaneXYZProjection*)pNodeData);
            break;
        case Octane::NT_PROJ_PERSPECTIVE:
            uploadPerspProjection((OctaneEngine::OctanePerspProjection*)pNodeData);
            break;
        case Octane::NT_PROJ_SPHERICAL:
            uploadSphericalProjection((OctaneEngine::OctaneSphericalProjection*)pNodeData);
            break;
        case Octane::NT_PROJ_UVW:
            uploadUvwProjection((OctaneEngine::OctaneUVWProjection*)pNodeData);
            break;
        case Octane::NT_DISPLACEMENT:
            uploadDisplacementTex((OctaneEngine::OctaneDisplacementTexture*)pNodeData);
            break;
        case Octane::NT_TEX_ALPHAIMAGE:
            uploadAlphaImageTex((OctaneEngine::OctaneAlphaImageTexture*)pNodeData);
            break;
        case Octane::NT_TEX_CHECKS:
            uploadChecksTex((OctaneEngine::OctaneChecksTexture*)pNodeData);
            break;
        case Octane::NT_TEX_CLAMP:
            uploadClampTex((OctaneEngine::OctaneClampTexture*)pNodeData);
            break;
        case Octane::NT_TEX_COLORCORRECTION:
            uploadColorcorrectTex((OctaneEngine::OctaneColorCorrectTexture*)pNodeData);
            break;
        case Octane::NT_TEX_COSINEMIX:
            uploadCosineMixTex((OctaneEngine::OctaneCosineMixTexture*)pNodeData);
            break;
        case Octane::NT_TEX_DIRT:
            uploadDirtTex((OctaneEngine::OctaneDirtTexture*)pNodeData);
            break;
        case Octane::NT_TEX_FALLOFF:
            uploadFalloffTex((OctaneEngine::OctaneFalloffTexture*)pNodeData);
            break;
        case Octane::NT_TEX_FLOAT:
            uploadFloatTex((OctaneEngine::OctaneFloatTexture*)pNodeData);
            break;
        case Octane::NT_TEX_FLOATIMAGE:
            uploadFloatImageTex((OctaneEngine::OctaneFloatImageTexture*)pNodeData);
            break;
        case Octane::NT_TEX_GAUSSIANSPECTRUM:
            uploadGaussianSpectrumTex((OctaneEngine::OctaneGaussianSpectrumTexture*)pNodeData);
            break;
        case Octane::NT_TEX_GRADIENT:
            uploadGradientTex((OctaneEngine::OctaneGradientTexture*)pNodeData);
            break;
        case Octane::NT_VOLUME_RAMP:
            uploadVolumeRampTex((OctaneEngine::OctaneVolumeRampTexture*)pNodeData);
            break;
        case Octane::NT_TEX_IMAGE:
            uploadImageTex((OctaneEngine::OctaneImageTexture*)pNodeData);
            break;
        case Octane::NT_TEX_INVERT:
            uploadInvertTex((OctaneEngine::OctaneInvertTexture*)pNodeData);
            break;
        case Octane::NT_TEX_MARBLE:
            uploadMarbleTex((OctaneEngine::OctaneMarbleTexture*)pNodeData);
            break;
        case Octane::NT_TEX_MIX:
            uploadMixTex((OctaneEngine::OctaneMixTexture*)pNodeData);
            break;
        case Octane::NT_TEX_MULTIPLY:
            uploadMultiplyTex((OctaneEngine::OctaneMultiplyTexture*)pNodeData);
            break;
        case Octane::NT_TEX_NOISE:
            uploadNoiseTex((OctaneEngine::OctaneNoiseTexture*)pNodeData);
            break;
        case Octane::NT_TEX_RANDOMCOLOR:
            uploadRandomColorTex((OctaneEngine::OctaneRandomColorTexture*)pNodeData);
            break;
        case Octane::NT_TEX_RGB:
            uploadRgbSpectrumTex((OctaneEngine::OctaneRGBSpectrumTexture*)pNodeData);
            break;
        case Octane::NT_TEX_RGFRACTAL:
            uploadRidgedFractalTex((OctaneEngine::OctaneRidgedFractalTexture*)pNodeData);
            break;
        case Octane::NT_TEX_SAWWAVE:
            uploadSawWaveTex((OctaneEngine::OctaneSawWaveTexture*)pNodeData);
            break;
        case Octane::NT_TEX_SINEWAVE:
            uploadSineWaveTex((OctaneEngine::OctaneSineWaveTexture*)pNodeData);
            break;
        case Octane::NT_TEX_SIDE:
            uploadPolygonSideTex((OctaneEngine::OctanePolygonSideTexture*)pNodeData);
            break;
        case Octane::NT_TEX_TRIANGLEWAVE:
            uploadTriangleWaveTex((OctaneEngine::OctaneTriangleWaveTexture*)pNodeData);
            break;
        case Octane::NT_TEX_TURBULENCE:
            uploadTurbulenceTex((OctaneEngine::OctaneTurbulenceTexture*)pNodeData);
            break;
        case Octane::NT_TRANSFORM_2D:
            upload2dTransform((OctaneEngine::Octane2DTransform*)pNodeData);
            break;
        case Octane::NT_TRANSFORM_3D:
            upload3dTransform((OctaneEngine::Octane3DTransform*)pNodeData);
            break;
        case Octane::NT_TRANSFORM_ROTATION:
            uploadRotationTransform((OctaneEngine::OctaneRotationTransform*)pNodeData);
            break;
        case Octane::NT_TRANSFORM_SCALE:
            uploadScaleTransform((OctaneEngine::OctaneScaleTransform*)pNodeData);
            break;
        case Octane::NT_TRANSFORM_VALUE:
            uploadFullTransform((OctaneEngine::OctaneFullTransform*)pNodeData);
            break;
        case Octane::NT_TEX_W:
            uploadWTex((OctaneEngine::OctaneWTexture*)pNodeData);
            break;
        default:
            break;
    }
} //uploadNode()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteNode(OctaneNodeBase *pNodeData) {
    switch(pNodeData->nodeType) {
        //case Octane::NT_BOOL:
        //case Octane::NT_STRING:
        //case Octane::NT_ENUM:
        case Octane::NT_FLOAT:
        case Octane::NT_INT:
            deleteValue(pNodeData->sName);
            break;
        case Octane::NT_EMIS_BLACKBODY:
        case Octane::NT_EMIS_TEXTURE:
            deleteEmission(pNodeData->sName);
            break;
        case Octane::NT_MAT_DIFFUSE:
        case Octane::NT_MAT_GLOSSY:
        case Octane::NT_MAT_MIX:
        case Octane::NT_MAT_PORTAL:
        case Octane::NT_MAT_SPECULAR:
            deleteMaterial(pNodeData->sName);
            break;
        case Octane::NT_MED_ABSORPTION:
        case Octane::NT_MED_SCATTERING:
            deleteMedium(pNodeData->sName);
            break;
        //case Octane::NT_PHASE_SCHLICK:
        //    break;
        case Octane::NT_PROJ_BOX:
        case Octane::NT_PROJ_CYLINDRICAL:
        case Octane::NT_PROJ_LINEAR:
        case Octane::NT_PROJ_PERSPECTIVE:
        case Octane::NT_PROJ_SPHERICAL:
        case Octane::NT_PROJ_UVW:
            deleteProjection(pNodeData->sName);
            break;
        case Octane::NT_DISPLACEMENT:
        case Octane::NT_TEX_ALPHAIMAGE:
        case Octane::NT_TEX_CHECKS:
        case Octane::NT_TEX_CLAMP:
        case Octane::NT_TEX_COLORCORRECTION:
        case Octane::NT_TEX_COSINEMIX:
        case Octane::NT_TEX_DIRT:
        case Octane::NT_TEX_FALLOFF:
        case Octane::NT_TEX_FLOAT:
        case Octane::NT_TEX_FLOATIMAGE:
        case Octane::NT_TEX_GAUSSIANSPECTRUM:
        case Octane::NT_TEX_GRADIENT:
        case Octane::NT_TEX_IMAGE:
        case Octane::NT_TEX_INVERT:
        case Octane::NT_TEX_MARBLE:
        case Octane::NT_TEX_MIX:
        case Octane::NT_TEX_MULTIPLY:
        case Octane::NT_TEX_NOISE:
        case Octane::NT_TEX_RANDOMCOLOR:
        case Octane::NT_TEX_RGB:
        case Octane::NT_TEX_RGFRACTAL:
        case Octane::NT_TEX_SAWWAVE:
        case Octane::NT_TEX_SINEWAVE:
        case Octane::NT_TEX_SIDE:
        case Octane::NT_TEX_TRIANGLEWAVE:
        case Octane::NT_TEX_TURBULENCE:
            deleteTexture(pNodeData->sName);
            break;
        case Octane::NT_TRANSFORM_2D:
        case Octane::NT_TRANSFORM_3D:
        case Octane::NT_TRANSFORM_ROTATION:
        case Octane::NT_TRANSFORM_SCALE:
        case Octane::NT_TRANSFORM_VALUE:
            deleteTransform(pNodeData->sName);
            break;
        default:
            break;
    }
} //deleteNode()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadScatter(string &sScatterName, string &sMeshName, float *pfMatrices, uint64_t ulMatrCnt, bool bMovable, vector<string>& asShaderNames, uint32_t uiFrameIdx, uint32_t uiTotalFrames) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    uint64_t shaders_cnt = asShaderNames.size();
        
    {
        uint64_t size = sizeof(uint64_t) + sMeshName.length() + 2;
        for(uint64_t n=0; n<shaders_cnt; ++n)
            size += asShaderNames[n].length()+2;

        RPCSend snd(m_Socket, size, LOAD_GEO_MAT, (sScatterName+"_m__").c_str());
        snd << shaders_cnt << sMeshName;
        for(uint64_t n=0; n<shaders_cnt; ++n)
            snd << asShaderNames[n];
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != LOAD_GEO_MAT) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR loading materials of transform.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    {
        uint64_t size = sizeof(uint64_t)
            + sizeof(int32_t) //Movable
            + sizeof(uint32_t) * 2 //Frame index
            + sScatterName.length() + 4 + 2 + sizeof(float) * 12 * ulMatrCnt;

        RPCSend snd(m_Socket, size, LOAD_GEO_SCATTER, (sScatterName+"_s__").c_str());
        string tmp = sScatterName+"_m__";
        snd << ulMatrCnt;
        if(ulMatrCnt) snd.writeBuffer(pfMatrices, sizeof(float)*12*ulMatrCnt);
        snd << bMovable << uiFrameIdx << uiTotalFrames << tmp;
        snd.write();
    }
    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_GEO_SCATTER) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading transform.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadScatter()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteScatter(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        std::string sGeoScatterName = sName + "_s__";
        RPCSend snd(m_Socket, 0, DEL_GEO_SCATTER, sGeoScatterName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_GEO_SCATTER) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting transform.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    {
        std::string sGeoMatName = sName + "_m__";
        RPCSend snd(m_Socket, 0, DEL_GEO_MAT, sGeoMatName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_GEO_MAT) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting transform materials.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteScatter()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadMesh(  bool            bGlobal, uint32_t uiFrameIdx, uint32_t uiTotalFrames,
                                uint64_t        uiMeshCnt,
                                char            **ppcNames,
                                uint64_t        *puiShadersCnt,
                                uint64_t        *puiObjectsCnt,
                                vector<string>  *pasShaderNames,
                                vector<string>  *pasObjectNames,
                                float_3         **ppf3Points,
                                uint64_t        *pulPointsSize,
                                float_3         **ppf3Normals,
                                uint64_t        *pulNormalsSize,
                                int32_t         **ppiPointsIndices,
                                int32_t         **ppiNormalsIndices,
                                uint64_t        *plPointsIndicesSize,
                                uint64_t        *plNormalsIndicesSize,
                                int32_t         **ppiVertPerPoly,
                                uint64_t        *plVertPerPolySize,
                                int32_t         **ppiPolyMatIndex,
                                int32_t         **ppiPolyObjIndex,
                                float_3         **ppf3UVs,
                                uint64_t        *plUVsSize,
                                int32_t         **ppiUVIndices,
                                uint64_t        *plUVIndicesSize,
                                float_3         **ppf3HairPoints,
                                uint64_t        *plHairPointsSize,
                                uint64_t        *plHairWsSize,
                                int32_t         **ppiVertPerHair,
                                uint64_t        *plVertPerHairSize,
                                float           **ppfHairThickness,
                                int32_t         **ppiHairMatIndices,
                                float_2         **ppf2HairUVs,
                                float_2         **ppf2HairWs,
                                int32_t         *aiHairInterpolations,
                                bool            *pbOpenSubdEnable,
                                int32_t         *piOpenSubdScheme,
                                int32_t         *piOpenSubdLevel,
                                float           *pfOpenSubdSharpness,
                                int32_t         *piOpenSubdBoundInterp,
                                uint64_t        *piOpenSubdCreasesCnt,
                                int32_t         **ppiOpenSubdCreasesIndices,
                                float           **ppfOpenSubdCreasesSharpnesses,
                                int32_t         *piLayerNumber,
                                int32_t         *piBakingGroupId,
                                float           *pfGeneralVis,
                                bool            *pbCamVis,
                                bool            *pbShadowVis,
                                int32_t         *piRandColorSeed,
                                bool            *pbReshapable,
                                float           *pfMaxSmoothAngle) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        uint64_t size = sizeof(uint64_t) //Meshes count;
            + sizeof(uint32_t) * 2 //Frame index
            + sizeof(uint64_t) * 1 * uiMeshCnt + sizeof(int32_t) * 4 * uiMeshCnt + sizeof(float) * 1 * uiMeshCnt //Subdivision addributes
            + sizeof(int32_t) * 7 * uiMeshCnt + sizeof(float) * 1 * uiMeshCnt //Visibility and reshapable addributes
            + sizeof(uint64_t) * 12 * uiMeshCnt + sizeof(float) * 1 * uiMeshCnt; //Array lentghs and smooth angles

        for(unsigned long i=0; i<uiMeshCnt; ++i) {
            size +=
            + pulPointsSize[i]*sizeof(float)*3
            + pulNormalsSize[i]*sizeof(float)*3
            + plPointsIndicesSize[i]*sizeof(int32_t)
            + plNormalsIndicesSize[i]*sizeof(int32_t)
            + 3 * plVertPerPolySize[i]*sizeof(int32_t)
            + plUVsSize[i]*sizeof(float)*3
            + plUVIndicesSize[i] * sizeof(int32_t)
            + plHairPointsSize[i] * sizeof(float) * 3
            + (plHairWsSize && ppf2HairWs ? plHairWsSize[i] * sizeof(float) * 2 : 0)
            + plVertPerHairSize[i] * sizeof(int32_t)
            + plHairPointsSize[i] * sizeof(float)
            + plVertPerHairSize[i] * sizeof(int32_t)
            + plVertPerHairSize[i] * sizeof(float) * 2
            + piOpenSubdCreasesCnt[i] * sizeof(int32_t) * 2
            + piOpenSubdCreasesCnt[i] * sizeof(float);

            if(!bGlobal) size += strlen(ppcNames[i])+2;
            for(unsigned int n=0; n < puiShadersCnt[i]; ++n)
                size += pasShaderNames[i][n].length()+2;

            for(unsigned int n=0; n < puiObjectsCnt[i]; ++n)
                size += pasObjectNames[i][n].length()+2;
        }

        RPCSend snd(m_Socket, size, bGlobal ? LOAD_GLOBAL_MESH : LOAD_LOCAL_MESH, ppcNames[0]);

        snd << uiMeshCnt << uiFrameIdx << uiTotalFrames;

        for(unsigned long i=0; i<uiMeshCnt; ++i) {
            if(!plHairPointsSize[i] && (!pulPointsSize[i] || !pulNormalsSize[i] || !plPointsIndicesSize[i] || !plVertPerPolySize[i] || !plUVsSize[i] || !plUVIndicesSize[i])) {
                UNLOCK_MUTEX(m_SocketMutex);
                return;
            }

            snd << pulPointsSize[i]
                << pulNormalsSize[i]
                << plPointsIndicesSize[i]
                << plNormalsIndicesSize[i]
                << plVertPerPolySize[i]
                << plUVsSize[i]
                << plUVIndicesSize[i]
                << puiShadersCnt[i]
                << puiObjectsCnt[i]
                << plHairPointsSize[i]
                << plVertPerHairSize[i]
                << (plHairWsSize ? plHairWsSize[i] : (uint64_t)0)
                << piOpenSubdCreasesCnt[i]
                << pfMaxSmoothAngle[i];
        }

        for(unsigned long i=0; i<uiMeshCnt; ++i) {
            snd.writeFloat3Buffer(ppf3Points[i], pulPointsSize[i]);
            if(pulNormalsSize[i]) snd.writeFloat3Buffer(ppf3Normals[i], pulNormalsSize[i]);
            if(plUVsSize[i]) snd.writeFloat3Buffer(ppf3UVs[i], plUVsSize[i]);
            if(plHairPointsSize[i]) snd.writeFloat3Buffer(ppf3HairPoints[i], plHairPointsSize[i]);
            if(plVertPerHairSize[i]) snd.writeFloat2Buffer(ppf2HairUVs[i], plVertPerHairSize[i]);
            if(plHairPointsSize[i]) snd.writeBuffer(ppfHairThickness[i], plHairPointsSize[i] * sizeof(float));
            if(plHairWsSize && plHairWsSize[i] && ppf2HairWs) snd.writeFloat2Buffer(ppf2HairWs[i], plHairWsSize[i]);
            if(piOpenSubdCreasesCnt[i]) snd.writeBuffer(ppfOpenSubdCreasesSharpnesses[i], piOpenSubdCreasesCnt[i] * sizeof(float));
            snd << pfOpenSubdSharpness[i] << pfGeneralVis[i];
        }

        for(unsigned long i=0; i<uiMeshCnt; ++i) {
            snd.writeBuffer(ppiPointsIndices[i], plPointsIndicesSize[i] * sizeof(int32_t));
            snd.writeBuffer(ppiVertPerPoly[i], plVertPerPolySize[i] * sizeof(int32_t));
            snd.writeBuffer(ppiPolyMatIndex[i], plVertPerPolySize[i] * sizeof(int32_t));
            snd.writeBuffer(ppiPolyObjIndex[i], plVertPerPolySize[i] * sizeof(int32_t));
            if(plNormalsIndicesSize[i]) snd.writeBuffer(ppiNormalsIndices[i], plNormalsIndicesSize[i] * sizeof(int32_t));
            if(plUVIndicesSize[i]) snd.writeBuffer(ppiUVIndices[i], plUVIndicesSize[i] * sizeof(int32_t));
            if(plVertPerHairSize[i]) snd.writeBuffer(ppiVertPerHair[i], plVertPerHairSize[i] * sizeof(int32_t));
            if(plVertPerHairSize[i]) snd.writeBuffer(ppiHairMatIndices[i], plVertPerHairSize[i] * sizeof(int32_t));
            if(piOpenSubdCreasesCnt[i]) snd.writeBuffer(ppiOpenSubdCreasesIndices[i], piOpenSubdCreasesCnt[i] * sizeof(int32_t) * 2);
            snd << pbOpenSubdEnable[i] << piOpenSubdScheme[i] << piOpenSubdLevel[i] << piOpenSubdBoundInterp[i] << piLayerNumber[i] << piBakingGroupId[i] << piRandColorSeed[i]
                << (aiHairInterpolations ? aiHairInterpolations[i] : ::Octane::HairInterpolationType::HAIR_INTERP_DEFAULT) << pbCamVis[i] << pbShadowVis[i] << pbReshapable[i];
        }
        for(unsigned long i=0; i<uiMeshCnt; ++i) {
            if(!bGlobal) snd << ppcNames[i];
            for(unsigned int n=0; n < puiShadersCnt[i]; ++n)
                snd << pasShaderNames[i][n];

            for(unsigned int n=0; n < puiObjectsCnt[i]; ++n)
                snd << pasObjectNames[i][n];
        }

        snd.write();
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != (bGlobal ? LOAD_GLOBAL_MESH : LOAD_LOCAL_MESH)) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading mesh.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMesh(bool bGlobal, string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, (bGlobal ? DEL_GLOBAL_MESH : DEL_LOCAL_MESH), sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != (bGlobal ? DEL_GLOBAL_MESH : DEL_LOCAL_MESH)) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting mesh.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteMesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadLayerMap(bool bGlobal,
                                        string const    &sLayerMapName, string const &sMeshName,
                                        int32_t         iLayersCnt,
                                        int32_t         *piLayerId,
                                        int32_t         *piBakingGroupId,
                                        float           *pfGeneralVis,
                                        bool            *pbCamVis,
                                        bool            *pbShadowVis,
                                        int32_t         *piRandColorSeed) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        uint64_t size = sizeof(int32_t) + sMeshName.length() + 2
            + sizeof(int32_t) //Layers count;
            + sizeof(int32_t) * iLayersCnt * 2 //Layer and Baking group IDs
            + sizeof(int32_t) * iLayersCnt //Color seeds
            + sizeof(float) * iLayersCnt //Gen visibilities
            + sizeof(int32_t) * iLayersCnt * 2; //Cam and shadow visibilities

        RPCSend snd(m_Socket, size, LOAD_GEO_LAYERMAP, sLayerMapName.c_str());

        snd << bGlobal << iLayersCnt;

        for(long i=0; i<iLayersCnt; ++i)
            snd << pfGeneralVis[i] << piLayerId[i] << piBakingGroupId[i] << pbCamVis[i] << pbShadowVis[i] << piRandColorSeed[i];

        snd << sMeshName;

        snd.write();
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != LOAD_GEO_LAYERMAP) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading layer map.");
        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteLayerMap(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_GEO_LAYERMAP, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_GEO_LAYERMAP) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting layer map.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteLayerMap()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadVolume(OctaneVolume *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    if(pNode->pfRegularGrid) {
        uint64_t size = sizeof(int32_t) * 12 + sizeof(float) * 9 + sizeof(float) * pNode->iGridSize + sizeof(float) * 12
            + pNode->sMedium.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_VOLUME_DATA, pNode->sName.c_str());
            snd << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
                << pNode->iGridSize << pNode->iAbsorptionOffset << pNode->iEmissionOffset << pNode->iScatterOffset << pNode->iVelocityOffsetX << pNode->iVelocityOffsetY << pNode->iVelocityOffsetZ
                << pNode->f3Resolution << pNode->fISO << pNode->fAbsorptionScale << pNode->fEmissionScale << pNode->fScatterScale << pNode->fVelocityScale;
            snd.writeBuffer(pNode->pfRegularGrid, pNode->iGridSize * sizeof(float));
            snd.writeBuffer(&pNode->gridMatrix, 12 * sizeof(float));
            snd << pNode->sMedium.c_str();
            snd.write();
        }

        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != LOAD_VOLUME_DATA) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR loading volume.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }

        UNLOCK_MUTEX(m_SocketMutex);
    }
    else {
        uint64_t mod_time = getFileTime(pNode->sFileName);
        string file_name  = getFileName(pNode->sFileName);

        uint64_t size = sizeof(uint64_t) + sizeof(float) * 5 + sizeof(int32_t) * 5
            + file_name.length() + 2
            + pNode->sMedium.length() + 2
            + pNode->sAbsorptionId.length() + 2
            + pNode->sEmissionId.length() + 2
            + pNode->sScatterId.length() + 2
            + pNode->sVelocityId.length() + 2
            + pNode->sVelocityIdX.length() + 2
            + pNode->sVelocityIdY.length() + 2
            + pNode->sVelocityIdZ.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_VOLUME, pNode->sName.c_str());
            snd << mod_time
                << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
                << pNode->fAbsorptionScale << pNode->fEmissionScale << pNode->fScatterScale << pNode->fVelocityScale
                << file_name.c_str() << pNode->sMedium.c_str() << pNode->sAbsorptionId.c_str() << pNode->sEmissionId.c_str() << pNode->sScatterId.c_str()
                << pNode->sVelocityId.c_str() << pNode->sVelocityIdX.c_str() << pNode->sVelocityIdY.c_str() << pNode->sVelocityIdZ.c_str();
            snd.write();
        }

        bool file_is_needed;
        {
            RPCReceive rcv(m_Socket);
            if(rcv.m_PacketType != LOAD_VOLUME)
                file_is_needed = true;
            else
                file_is_needed = false;
        }

        if(file_is_needed && uploadFile(pNode->sFileName, file_name)) {
            {
                RPCSend snd(m_Socket, size, LOAD_VOLUME, pNode->sName.c_str());
                snd << mod_time
                    << pNode->fGenVisibility << pNode->iLayerNumber << pNode->iBakingGroupId << pNode->iRandomColorSeed << pNode->bShadowVisibility << pNode->bCamVisibility
                    << pNode->fAbsorptionScale << pNode->fEmissionScale << pNode->fScatterScale << pNode->fVelocityScale
                    << file_name.c_str() << pNode->sMedium.c_str() << pNode->sAbsorptionId.c_str() << pNode->sEmissionId.c_str() << pNode->sScatterId.c_str()
                    << pNode->sVelocityId.c_str() << pNode->sVelocityIdX.c_str() << pNode->sVelocityIdY.c_str() << pNode->sVelocityIdZ.c_str();
                snd.write();
            }
            {
                RPCReceive rcv(m_Socket);
                if(rcv.m_PacketType != LOAD_VOLUME) {
                    rcv >> m_sErrorMsg;
                    fprintf(stderr, "Octane: ERROR loading volume.");
                    if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
                    else fprintf(stderr, "\n");
                }
            }
        }

        UNLOCK_MUTEX(m_SocketMutex);
    }
} //uploadVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteVolume(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_VOLUME, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_VOLUME) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting volume.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkResponsePacket(PacketType packetType, const char *szErrorMsg) {
    if(m_Socket < 0) return false;

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType != packetType) {
        rcv >> m_sErrorMsg;

        if(szErrorMsg && szErrorMsg[0])
            fprintf(stderr, "Octane: uploading ERROR: %s.", szErrorMsg);
        else
            fprintf(stderr, "Octane: uploading ERROR.");

        if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else fprintf(stderr, "\n");
        return false;
    }
    else return true;
} //checkResponsePacket()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadDiffuseMat(OctaneDiffuseMaterial *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 1 + sizeof(int32_t) * 2 + sizeof(ComplexValue) * 6
        + pNode->sDiffuse.length() + 2
        + pNode->sTransmission.length() + 2
        + pNode->sBump.length() + 2
        + pNode->sNormal.length() + 2
        + pNode->sOpacity.length() + 2
        + pNode->sRounding.length() + 2
        + pNode->sEmission.length() + 2
        + pNode->sMedium.length() + 2
        + pNode->sDisplacement.length() + 2
        + pNode->sRoughness.length() + 2;

    const char* mat_name = pNode->sName.c_str();

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_DIFFUSE_MATERIAL, mat_name);
        snd << pNode->diffuseDefaultVal << pNode->transmissionDefaultVal << pNode->bumpDefaultVal << pNode->normalDefaultVal << pNode->opacityDefaultVal << pNode->roughnessDefaultVal
            << pNode->fRoundingDefaultVal
            << pNode->bSmooth << pNode->bMatte << pNode->sDiffuse.c_str() << pNode->sTransmission.c_str() << pNode->sBump.c_str()
            << pNode->sNormal.c_str() << pNode->sOpacity.c_str() << pNode->sRounding.c_str() << pNode->sEmission.c_str() << pNode->sMedium.c_str() << pNode->sDisplacement.c_str() << pNode->sRoughness.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_DIFFUSE_MATERIAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadDiffuseMat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadGlossyMat(OctaneGlossyMaterial *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3 + sizeof(int32_t) * 1 + sizeof(ComplexValue) * 7
        + pNode->sDiffuse.length() + 2
        + pNode->sSpecular.length() + 2
        + pNode->sRoughness.length() + 2
        + pNode->sFilmwidth.length() + 2
        + pNode->sBump.length() + 2
        + pNode->sNormal.length() + 2
        + pNode->sOpacity.length() + 2
        + pNode->sFilmindex.length() + 2
        + pNode->sIndex.length() + 2
        + pNode->sRounding.length() + 2
        + pNode->sDisplacement.length() + 2;

    const char* mat_name = pNode->sName.c_str();

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_GLOSSY_MATERIAL, mat_name);
        snd << pNode->diffuseDefaultVal << pNode->specularDefaultVal << pNode->roughnessDefaultVal << pNode->filmwidthDefaultVal << pNode->bumpDefaultVal
            << pNode->normalDefaultVal << pNode->opacityDefaultVal
            << pNode->fFilmindexDefaultVal << pNode->fIndexDefaultVal << pNode->fRoundingDefaultVal
            << pNode->bSmooth
            << pNode->sFilmindex.c_str() << pNode->sIndex.c_str() << pNode->sRounding.c_str()
            << pNode->sDiffuse.c_str() << pNode->sSpecular.c_str() << pNode->sRoughness.c_str()
            << pNode->sFilmwidth.c_str() << pNode->sBump.c_str() << pNode->sNormal.c_str() << pNode->sOpacity.c_str() << pNode->sDisplacement.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_GLOSSY_MATERIAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadGlossyMat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadSpecularMat(OctaneSpecularMaterial *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 4 + sizeof(int32_t) * 3 + sizeof(ComplexValue) * 7
        + pNode->sReflection.length() + 2
        + pNode->sTransmission.length() + 2
        + pNode->sFilmwidth.length() + 2
        + pNode->sBump.length() + 2
        + pNode->sNormal.length() + 2
        + pNode->sOpacity.length() + 2
        + pNode->sRoughness.length() + 2
        + pNode->sMedium.length() + 2
        + pNode->sFilmindex.length() + 2
        + pNode->sIndex.length() + 2
        + pNode->sDispersionCoefB.length() + 2
        + pNode->sRounding.length() + 2
        + pNode->sDisplacement.length() + 2;

    const char* mat_name = pNode->sName.c_str();

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_SPECULAR_MATERIAL, mat_name);
        snd << pNode->reflectionDefaultVal << pNode->transmissionDefaultVal << pNode->filmwidthDefaultVal << pNode->bumpDefaultVal << pNode->normalDefaultVal
            << pNode->opacityDefaultVal << pNode->roughnessDefaultVal
            << pNode->fFilmindexDefaultVal << pNode->fIndexDefaultVal << pNode->fDispersionCoefBDefaultVal << pNode->fRoundingDefaultVal
            << pNode->bSmooth << pNode->bRefractionAlpha << pNode->bFakeShadows
            << pNode->sFilmindex.c_str() << pNode->sIndex.c_str() << pNode->sDispersionCoefB.c_str() << pNode->sRounding.c_str()
            << pNode->sReflection.c_str() << pNode->sTransmission.c_str() << pNode->sFilmwidth.c_str() << pNode->sBump.c_str()
            << pNode->sNormal.c_str() << pNode->sOpacity.c_str() << pNode->sRoughness.c_str() << pNode->sMedium.c_str() << pNode->sDisplacement.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_SPECULAR_MATERIAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadSpecularMat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadMixMat(OctaneMixMaterial *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue)
        + pNode->sAmount.length() + 2
        + pNode->sMaterial1.length() + 2
        + pNode->sMaterial2.length() + 2
        + pNode->sDisplacement.length() + 2;

    const char* mat_name = pNode->sName.c_str();

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_MIX_MATERIAL, mat_name);
        snd << pNode->amountDefaultVal << pNode->sAmount.c_str() << pNode->sMaterial2.c_str() << pNode->sMaterial1.c_str() << pNode->sDisplacement.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_MIX_MATERIAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMixMat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadPortalMat(OctanePortalMaterial *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t);

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PORTAL_MATERIAL, pNode->sName.c_str());
        snd << pNode->bEnabled;
        snd.write();
    }
    checkResponsePacket(LOAD_PORTAL_MATERIAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadPortalMat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMaterial(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_MATERIAL, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_MATERIAL) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting material.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteMaterial()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadFloatTex(OctaneFloatTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float);

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_FLOAT_TEXTURE, pNode->sName.c_str());
        snd << pNode->fValue;
        snd.write();
    }
    checkResponsePacket(LOAD_FLOAT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadFloatTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRgbSpectrumTex(OctaneRGBSpectrumTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_RGB_SPECTRUM_TEXTURE, pNode->sName.c_str());
        snd << pNode->f3Value.x << pNode->f3Value.y << pNode->f3Value.z;
        snd.write();
    }
    checkResponsePacket(LOAD_RGB_SPECTRUM_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadRgbSpectrumTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadGaussianSpectrumTex(OctaneGaussianSpectrumTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) * 3
        + pNode->sWaveLength.length() + 2
        + pNode->sWidth.length() + 2
        + pNode->sPower.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_GAUSSIAN_SPECTRUM_TEXTURE, pNode->sName.c_str());
        snd << pNode->waveLengthDefaultVal << pNode->widthDefaultVal << pNode->powerDefaultVal
            << pNode->sWaveLength.c_str() << pNode->sWidth.c_str() << pNode->sPower.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_GAUSSIAN_SPECTRUM_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadGaussianSpectrumTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadChecksTex(OctaneChecksTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) + pNode->sTransform.length() + 2 + pNode->sProjection.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_CHECKS_TEXTURE, pNode->sName.c_str());
        snd << pNode->transformDefaultVal << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_CHECKS_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadChecksTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadMarbleTex(OctaneMarbleTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) * 4 + sizeof(int32_t)
        + pNode->sPower.length() + 2
        + pNode->sOffset.length() + 2
        + pNode->sOmega.length() + 2
        + pNode->sVariance.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2
        + pNode->sOctaves.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_MARBLE_TEXTURE, pNode->sName.c_str());
        snd << pNode->powerDefaultVal << pNode->offsetDefaultVal << pNode->omegaDefaultVal << pNode->varianceDefaultVal
            << pNode->iOctavesDefaultVal << pNode->sOctaves.c_str()
            << pNode->sPower.c_str() << pNode->sOffset.c_str() << pNode->sOmega.c_str() << pNode->sVariance.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_MARBLE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMarbleTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRidgedFractalTex(OctaneRidgedFractalTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) * 3 + sizeof(int32_t)
        + pNode->sPower.length() + 2
        + pNode->sOffset.length() + 2
        + pNode->sLacunarity.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2
        + pNode->sOctaves.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_RIDGED_FRACTAL_TEXTURE, pNode->sName.c_str());
        snd << pNode->powerDefaultVal << pNode->offsetDefaultVal << pNode->lacunarityDefaultVal
            << pNode->iOctavesDefaultVal << pNode->sOctaves.c_str()
            << pNode->sPower.c_str() << pNode->sOffset.c_str() << pNode->sLacunarity.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_RIDGED_FRACTAL_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadRidgedFractalTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadSawWaveTex(OctaneSawWaveTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue)
        + pNode->sOffset.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_SAW_WAVE_TEXTURE, pNode->sName.c_str());
        snd << pNode->offsetDefaultVal
            << pNode->sOffset.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_SAW_WAVE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadSawWaveTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadSineWaveTex(OctaneSineWaveTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue)
        + pNode->sOffset.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_SINE_WAVE_TEXTURE, pNode->sName.c_str());
        snd << pNode->offsetDefaultVal
            << pNode->sOffset.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_SINE_WAVE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadSineWaveTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadTriangleWaveTex(OctaneTriangleWaveTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue)
        + pNode->sOffset.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_TRIANGLE_WAVE_TEXTURE, pNode->sName.c_str());
        snd << pNode->offsetDefaultVal
            << pNode->sOffset.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_TRIANGLE_WAVE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadTriangleWaveTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadTurbulenceTex(OctaneTurbulenceTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 1 + sizeof(int32_t) * 3 + sizeof(ComplexValue) * 3
        + pNode->sPower.length() + 2
        + pNode->sOffset.length() + 2
        + pNode->sOmega.length() + 2
        + pNode->sGamma.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2
        + pNode->sOctaves.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_TURBULENCE_TEXTURE, pNode->sName.c_str());
        snd << pNode->powerDefaultVal << pNode->offsetDefaultVal << pNode->omegaDefaultVal
            << pNode->fGammaDefaultVal << pNode->iOctavesDefaultVal
            << pNode->bTurbulence << pNode->bInvert
            << pNode->sOctaves.c_str() << pNode->sPower.c_str() << pNode->sOffset.c_str() << pNode->sOmega.c_str() << pNode->sGamma.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_TURBULENCE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadTurbulenceTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadClampTex(OctaneClampTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) * 3
        + pNode->sInput.length() + 2
        + pNode->sMin.length() + 2
        + pNode->sMax.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_CLAMP_TEXTURE, pNode->sName.c_str());
        snd << pNode->inputDefaultVal << pNode->minDefaultVal << pNode->maxDefaultVal
            << pNode->sInput.c_str() << pNode->sMin.c_str() << pNode->sMax.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_CLAMP_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadClampTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadCosineMixTex(OctaneCosineMixTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue)
        + pNode->sAmount.length() + 2
        + pNode->sTexture1.length() + 2
        + pNode->sTexture2.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_COSINE_MIX_TEXTURE, pNode->sName.c_str());
        snd << pNode->amountDefaultVal
            << pNode->sAmount.c_str() << pNode->sTexture1.c_str() << pNode->sTexture2.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_COSINE_MIX_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadCosineMixTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadInvertTex(OctaneInvertTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = pNode->sTexture.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_INVERT_TEXTURE, pNode->sName.c_str());
        snd << pNode->sTexture.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_INVERT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadInvertTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadMixTex(OctaneMixTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(ComplexValue) * 3
        + pNode->sAmount.length() + 2
        + pNode->sTexture1.length() + 2
        + pNode->sTexture2.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_MIX_TEXTURE, pNode->sName.c_str());
        snd << pNode->amountDefaultVal << pNode->tex1DefaultVal << pNode->tex2DefaultVal
            << pNode->sAmount.c_str() << pNode->sTexture1.c_str() << pNode->sTexture2.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_MIX_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMixTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadMultiplyTex(OctaneMultiplyTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = pNode->sTexture1.length() + 2
        + pNode->sTexture2.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_MULTIPLY_TEXTURE, pNode->sName.c_str());
        snd << pNode->sTexture1.c_str() << pNode->sTexture2.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_MULTIPLY_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadMultiplyTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadFalloffTex(OctaneFalloffTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 6 + sizeof(int32_t) * 1
        + pNode->sNormal.length() + 2
        + pNode->sGrazing.length() + 2
        + pNode->sIndex.length() + 2
        + pNode->sMode.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_FALLOFF_TEXTURE, pNode->sName.c_str());
        snd << pNode->fNormalDefaultVal << pNode->fGrazingDefaultVal << pNode->fIndexDefaultVal << pNode->f3Direction
            << pNode->modeDefaultVal
            << pNode->sNormal.c_str() << pNode->sGrazing.c_str() << pNode->sIndex.c_str() << pNode->sMode.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_FALLOFF_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadFalloffTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadColorcorrectTex(OctaneColorCorrectTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 4 + sizeof(int32_t) + sizeof(ComplexValue)
        + pNode->sTexture.length() + 2
        + pNode->sBrightness.length() + 2
        + pNode->sGamma.length() + 2
        + pNode->sHue.length() + 2
        + pNode->sSaturation.length() + 2
        + pNode->sContrast.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_COLOR_CORRECT_TEXTURE, pNode->sName.c_str());
        snd << pNode->brightnessDefaultVal
            << pNode->fGammaDefaultVal << pNode->fHueDefaultVal << pNode->fSaturationDefaultVal << pNode->fContrastDefaultVal
            << pNode->bInvert
            << pNode->sGamma.c_str() << pNode->sHue.c_str() << pNode->sSaturation.c_str() << pNode->sContrast.c_str()
            << pNode->sTexture.c_str() << pNode->sBrightness.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_COLOR_CORRECT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadColorcorrectTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline string OctaneClient::getFileName(string &sFullPath) {
    size_t sl1 = sFullPath.rfind('/');
    size_t sl2 = sFullPath.rfind('\\');
    string file_name;
    if(sl1 == string::npos && sl2 == string::npos) {
        file_name = sFullPath;
    }
    else {
        if(sl1 == string::npos)
            sl1 = sl2;
        else if(sl2 != string::npos)
            sl1 = sl1 > sl2 ? sl1 : sl2;
        file_name = sFullPath.substr(sl1 + 1);
    }
    return file_name;
} //getFileName()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline uint64_t OctaneClient::getFileTime(string &sFullPath) {
    if(!sFullPath.length()) return 0;

#ifdef _WIN32
    struct _stat64i32 attrib;
#else
    struct stat attrib;
#endif
    ustat(sFullPath.c_str(), &attrib);

    return static_cast<uint64_t>(attrib.st_mtime);
} //getFileTime()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::uploadFile(string &sFilePath, string &sFileName) {
    FILE *hFile = ufopen(sFilePath.c_str(), "rb");
    if(hFile) {
        fseek(hFile, 0, SEEK_END);
        uint32_t ulFileSize = ftell(hFile);
        rewind(hFile);

        char* pCurPtr = new char[ulFileSize];

        if(!fread(pCurPtr, ulFileSize, 1, hFile)) {
            fclose(hFile);
            delete[] pCurPtr;
            return false;
        }
        fclose(hFile);

        RPCSend snd(m_Socket, sizeof(uint32_t) + ulFileSize, LOAD_IMAGE_FILE, sFileName.c_str());
        snd << ulFileSize;
        snd.writeBuffer(pCurPtr, ulFileSize);
        snd.write();
        delete[] pCurPtr;

        {
            RPCReceive rcv(m_Socket);
            if(rcv.m_PacketType != LOAD_IMAGE_FILE) {
                rcv >> m_sErrorMsg;
                fprintf(stderr, "Octane: ERROR loading image file.");
                if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
                else fprintf(stderr, "\n");
                return false;
            }
        }
        return true;
    }
    else return false;
} //uploadFile()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadImageTex(OctaneImageTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    if(pNode->dataBuffer.pvBufImgData) {
        int iImgSize = pNode->dataBuffer.iBufWidth * pNode->dataBuffer.iBufHeight * pNode->dataBuffer.iBufComponents;
        uint64_t size = sizeof(ComplexValue) + sizeof(float) * 1 + sizeof(int32_t) * 6 + iImgSize * (pNode->dataBuffer.bBufIsFloat ? sizeof(float) : 1)
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_IMAGE_TEXTURE_DATA, pNode->sName.c_str());
            snd << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->dataBuffer.iBufWidth << pNode->dataBuffer.iBufHeight << pNode->dataBuffer.iBufComponents << pNode->dataBuffer.bBufIsFloat << pNode->bInvert;
            if(pNode->dataBuffer.bBufIsFloat)
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize * sizeof(float));
            else
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize);
            snd << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        checkResponsePacket(LOAD_IMAGE_TEXTURE_DATA);
        UNLOCK_MUTEX(m_SocketMutex);
    }
    else {
        string sFileName  = getFileName(pNode->sFileName);
        uint64_t mod_time = getFileTime(pNode->sFileName);

        uint64_t size = sizeof(uint64_t) + sizeof(float) * 1 + sizeof(int32_t) * 2 + sizeof(ComplexValue)
            + sFileName.length() + 2
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_IMAGE_TEXTURE, pNode->sName.c_str());
            snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->bInvert
                << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << sFileName.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        bool file_is_needed;
        {
            RPCReceive rcv(m_Socket);
            if(rcv.m_PacketType != LOAD_IMAGE_TEXTURE)
                file_is_needed = true;
            else
                file_is_needed = false;
        }

        if(file_is_needed && uploadFile(pNode->sFileName, sFileName)) {
            {
                RPCSend snd(m_Socket, size, LOAD_IMAGE_TEXTURE, pNode->sName.c_str());
                snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                    << pNode->iBorderModeDefaultVal << pNode->bInvert
                    << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << sFileName.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
                snd.write();
            }
            {
                RPCReceive rcv(m_Socket);
                if(rcv.m_PacketType != LOAD_IMAGE_TEXTURE) {
                    rcv >> m_sErrorMsg;
                    fprintf(stderr, "Octane: ERROR loading image texture.");
                    if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
                    else fprintf(stderr, "\n");
                }
            }
        }
        UNLOCK_MUTEX(m_SocketMutex);
    }
} //uploadImageTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadFloatImageTex(OctaneFloatImageTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    if(pNode->dataBuffer.pvBufImgData) {
        int iImgSize = pNode->dataBuffer.iBufWidth * pNode->dataBuffer.iBufHeight * pNode->dataBuffer.iBufComponents;
        uint64_t size = sizeof(ComplexValue) + sizeof(float) * 1 + sizeof(int32_t) * 6 + iImgSize * (pNode->dataBuffer.bBufIsFloat ? sizeof(float) : 1)
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_FLOAT_IMAGE_TEXTURE_DATA, pNode->sName.c_str());
            snd << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->dataBuffer.iBufWidth << pNode->dataBuffer.iBufHeight << pNode->dataBuffer.iBufComponents << pNode->dataBuffer.bBufIsFloat << pNode->bInvert;
            if(pNode->dataBuffer.bBufIsFloat)
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize * sizeof(float));
            else
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize);
            snd << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        checkResponsePacket(LOAD_FLOAT_IMAGE_TEXTURE_DATA);
        UNLOCK_MUTEX(m_SocketMutex);
    }
    else {
        uint64_t mod_time = getFileTime(pNode->sFileName);
        string file_name  = getFileName(pNode->sFileName);

        uint64_t size = sizeof(uint64_t) + sizeof(float) * 1 + sizeof(int32_t) * 2 + sizeof(ComplexValue)
            + file_name.length() + 2
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_FLOAT_IMAGE_TEXTURE, pNode->sName.c_str());
            snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->bInvert
                << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << file_name.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        bool file_is_needed;
        {
            RPCReceive rcv(m_Socket);
            if(rcv.m_PacketType != LOAD_FLOAT_IMAGE_TEXTURE)
                file_is_needed = true;
            else
                file_is_needed = false;
        }

        if(file_is_needed && uploadFile(pNode->sFileName, file_name)) {
            {
                RPCSend snd(m_Socket, size, LOAD_FLOAT_IMAGE_TEXTURE, pNode->sName.c_str());
                snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                    << pNode->iBorderModeDefaultVal << pNode->bInvert
                    << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << file_name.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
                snd.write();
            }
            {
                RPCReceive rcv(m_Socket);
                if(rcv.m_PacketType != LOAD_FLOAT_IMAGE_TEXTURE) {
                    rcv >> m_sErrorMsg;
                    fprintf(stderr, "Octane: ERROR loading float image texture.");
                    if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
                    else fprintf(stderr, "\n");
                }
            }
        }
        UNLOCK_MUTEX(m_SocketMutex);
    }
} //uploadFloatImageTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadAlphaImageTex(OctaneAlphaImageTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    if(pNode->dataBuffer.pvBufImgData) {
        int iImgSize = pNode->dataBuffer.iBufWidth * pNode->dataBuffer.iBufHeight * pNode->dataBuffer.iBufComponents;
        uint64_t size = sizeof(ComplexValue) + sizeof(float) * 1 + sizeof(int32_t) * 6 + iImgSize * (pNode->dataBuffer.bBufIsFloat ? sizeof(float) : 1)
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_ALPHA_IMAGE_TEXTURE_DATA, pNode->sName.c_str());
            snd << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->dataBuffer.iBufWidth << pNode->dataBuffer.iBufHeight << pNode->dataBuffer.iBufComponents << pNode->dataBuffer.bBufIsFloat << pNode->bInvert;
            if(pNode->dataBuffer.bBufIsFloat)
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize * sizeof(float));
            else
                snd.writeBuffer(pNode->dataBuffer.pvBufImgData, iImgSize);
            snd << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        checkResponsePacket(LOAD_ALPHA_IMAGE_TEXTURE_DATA);
        UNLOCK_MUTEX(m_SocketMutex);
    }
    else {
        uint64_t mod_time = getFileTime(pNode->sFileName);
        string file_name  = getFileName(pNode->sFileName);

        uint64_t size = sizeof(uint64_t) + sizeof(float) * 1 + sizeof(int32_t) * 2 + sizeof(ComplexValue)
            + file_name.length() + 2
            + pNode->sPower.length() + 2
            + pNode->sProjection.length() + 2
            + pNode->sTransform.length() + 2
            + pNode->sGamma.length() + 2
            + pNode->sBorderMode.length() + 2;

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_ALPHA_IMAGE_TEXTURE, pNode->sName.c_str());
            snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                << pNode->iBorderModeDefaultVal << pNode->bInvert
                << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << file_name.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
            snd.write();
        }

        bool file_is_needed;
        {
            RPCReceive rcv(m_Socket);
            if(rcv.m_PacketType != LOAD_ALPHA_IMAGE_TEXTURE)
                file_is_needed = true;
            else
                file_is_needed = false;
        }

        if(file_is_needed && uploadFile(pNode->sFileName, file_name)) {
            {
                RPCSend snd(m_Socket, size, LOAD_ALPHA_IMAGE_TEXTURE, pNode->sName.c_str());
                snd << mod_time << pNode->powerDefaultVal << pNode->fGammaDefaultVal
                    << pNode->iBorderModeDefaultVal << pNode->bInvert
                    << pNode->sGamma.c_str() << pNode->sBorderMode.c_str() << file_name.c_str() << pNode->sPower.c_str() << pNode->sTransform.c_str() << pNode->sProjection.c_str();
                snd.write();
            }
            {
                RPCReceive rcv(m_Socket);
                if(rcv.m_PacketType != LOAD_ALPHA_IMAGE_TEXTURE) {
                    rcv >> m_sErrorMsg;
                    fprintf(stderr, "Octane: ERROR loading alpha image texture.");
                    if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
                    else fprintf(stderr, "\n");
                }
            }
        }
        UNLOCK_MUTEX(m_SocketMutex);
    }
} //uploadAlphaImageTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadDirtTex(OctaneDirtTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 4 + sizeof(int32_t)
        + pNode->sStrength.length() + 2
        + pNode->sDetails.length() + 2
        + pNode->sRadius.length() + 2
        + pNode->sTolerance.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_DIRT_TEXTURE, pNode->sName.c_str());
        snd << pNode->fStrengthDefaultVal << pNode->fDetailsDefaultVal << pNode->fRadiusDefaultVal << pNode->fToleranceDefaultVal
            << pNode->bInvertNormal
            << pNode->sStrength.c_str() << pNode->sDetails.c_str() << pNode->sRadius.c_str() << pNode->sTolerance.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_DIRT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadDirtTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadGradientTex(OctaneGradientTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t) * 2
        + pNode->aPosData.size() * sizeof(float)
        + pNode->aColorData.size() * sizeof(float)
        + pNode->sTexture.length() + 2
        + pNode->sInterpolationType.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        int32_t grad_cnt = static_cast<int32_t>(pNode->aPosData.size());

        RPCSend snd(m_Socket, size, LOAD_GRADIENT_TEXTURE, pNode->sName.c_str());
        snd << grad_cnt << pNode->iInterpolationTypeDefaultVal;
        snd.writeBuffer(&pNode->aPosData[0], sizeof(float) * pNode->aPosData.size());
        snd.writeBuffer(&pNode->aColorData[0], sizeof(float) * pNode->aColorData.size());
        snd << pNode->sTexture.c_str() << pNode->sInterpolationType.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_GRADIENT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadGradientTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadVolumeRampTex(OctaneVolumeRampTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t) * 2 + sizeof(float)
        + pNode->aPosData.size() * sizeof(float)
        + pNode->aColorData.size() * sizeof(float)
        + pNode->sInterpolationType.length() + 2
        + pNode->sMaxGridValue.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        int32_t grad_cnt = static_cast<int32_t>(pNode->aPosData.size());

        RPCSend snd(m_Socket, size, LOAD_VOLUMERAMP_TEXTURE, pNode->sName.c_str());
        snd << grad_cnt << pNode->iInterpolationTypeDefaultVal << pNode->fMaxGridValueDefaultVal;
        snd.writeBuffer(&pNode->aPosData[0], sizeof(float) * pNode->aPosData.size());
        snd.writeBuffer(&pNode->aColorData[0], sizeof(float) * pNode->aColorData.size());
        snd << pNode->sInterpolationType.c_str() << pNode->sMaxGridValue.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_VOLUMERAMP_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadVolumeRampTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRandomColorTex(OctaneRandomColorTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sSeed.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_RANDOM_COLOR_TEXTURE, pNode->sName.c_str());
        snd << pNode->iSeedDefaultVal
            << pNode->sSeed.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_RANDOM_COLOR_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadRandomColorTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadPolygonSideTex(OctanePolygonSideTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t);

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_POLYGON_SIDE_TEXTURE, pNode->sName.c_str());
        snd << pNode->bInvert;
        snd.write();
    }
    checkResponsePacket(LOAD_POLYGON_SIDE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadPolygonSideTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadNoiseTex(OctaneNoiseTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3 + sizeof(int32_t) * 3
        + pNode->sNoiseType.length() + 2
        + pNode->sOctaves.length() + 2
        + pNode->sOmega.length() + 2
        + pNode->sTransform.length() + 2
        + pNode->sProjection.length() + 2
        + pNode->sGamma.length() + 2
        + pNode->sContrast.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_NOISE_TEXTURE, pNode->sName.c_str());
        snd << pNode->fOmegaDefaultVal << pNode->fGammaDefaultVal << pNode->fContrastDefaultVal
            << pNode->iNoiseTypeDefaultVal << pNode->iOctavesDefaultVal << pNode->bInvert
            << pNode->sNoiseType.c_str() << pNode->sOctaves.c_str() << pNode->sOmega.c_str() << pNode->sTransform.c_str()
            << pNode->sProjection.c_str() << pNode->sGamma.c_str() << pNode->sContrast.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_NOISE_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadNoiseTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadDisplacementTex(OctaneDisplacementTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 2 + sizeof(int32_t)
        + pNode->sTexture.length() + 2
        + pNode->sHeight.length() + 2
        + pNode->sOffset.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_DISPLACEMENT_TEXTURE, pNode->sName.c_str());
        snd << pNode->fHeightDefaultVal << pNode->fOffsetDefaultVal
            << pNode->iDetailsLevel
            << pNode->sTexture.c_str() << pNode->sHeight.c_str() << pNode->sOffset.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_DISPLACEMENT_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadDisplacementTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadWTex(OctaneWTexture *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, LOAD_W_TEXTURE, pNode->sName.c_str());
        snd.write();
    }
    checkResponsePacket(LOAD_W_TEXTURE);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadWTex()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteTexture(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_TEXTURE, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_TEXTURE) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting texture.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteTexture()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadBbodyEmission(OctaneBlackBodyEmission *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3 + sizeof(int32_t) * 4 + sizeof(ComplexValue) * 2
        + pNode->sTextureOrEff.length() + 2
        + pNode->sPower.length() + 2
        + pNode->sTemperature.length() + 2
        + pNode->sDistribution.length() + 2
        + pNode->sSamplingRate.length() + 2
        + pNode->sLightPassId.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_BLACKBODY_EMISSION, pNode->sName.c_str());
        snd << pNode->textureOrEffDefaultVal << pNode->distributionDefaultVal
            << pNode->fPowerDefaultVal << pNode->fTemperatureDefaultVal << pNode->fSamplingRateDefaultVal
            << pNode->iLightPassIdDefaultVal << pNode->bSurfaceBrightness << pNode->bNormalize << pNode->bCastIllumination
            << pNode->sTextureOrEff.c_str() << pNode->sPower.c_str() << pNode->sTemperature.c_str() << pNode->sDistribution.c_str() << pNode->sSamplingRate.c_str() << pNode->sLightPassId.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_BLACKBODY_EMISSION);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadBbodyEmission()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadTextureEmission(OctaneTextureEmission *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 2 + sizeof(int32_t) * 3 + sizeof(ComplexValue) * 2
        + pNode->sTextureOrEff.length() + 2
        + pNode->sPower.length() + 2
        + pNode->sDistribution.length() + 2
        + pNode->sSamplingRate.length() + 2
        + pNode->sLightPassId.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_TEXTURE_EMISSION, pNode->sName.c_str());
        snd << pNode->textureOrEffDefaultVal << pNode->distributionDefaultVal
            << pNode->fPowerDefaultVal << pNode->fSamplingRateDefaultVal
            << pNode->iLightPassIdDefaultVal << pNode->bSurfaceBrightness << pNode->bCastIllumination
            << pNode->sTextureOrEff.c_str() << pNode->sPower.c_str() << pNode->sDistribution.c_str() << pNode->sSamplingRate.c_str() << pNode->sLightPassId.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_TEXTURE_EMISSION);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadTextureEmission()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteEmission(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_EMISSION, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_EMISSION) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting emission.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteEmission()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MEDIUMS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadAbsorptionMedium(OctaneAbsorptionMedium *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t) + sizeof(float) + sizeof(ComplexValue)
        + pNode->sAbsorption.length() + 2
        + pNode->sScale.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_ABSORPTION_MEDIUM, pNode->sName.c_str());
        snd << pNode->absorptionDefaultVal
            << pNode->fScaleDefaultVal
            << pNode->bInvertAbsorption 
            << pNode->sAbsorption.c_str() << pNode->sScale.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_ABSORPTION_MEDIUM);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadAbsorptionMedium()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadScatteringMedium(OctaneScatteringMedium *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t) + sizeof(float) * 2 +  + sizeof(ComplexValue) * 2
        + pNode->sAbsorption.length() + 2
        + pNode->sScattering.length() + 2
        + pNode->sPhase.length() + 2
        + pNode->sEmission.length() + 2
        + pNode->sScale.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_SCATTERING_MEDIUM, pNode->sName.c_str());
        snd << pNode->absorptionDefaultVal << pNode->scatteringDefaultVal
            << pNode->fPhaseDefaultVal << pNode->fScaleDefaultVal
            << pNode->bInvertAbsorption 
            << pNode->sAbsorption.c_str() << pNode->sScattering.c_str() << pNode->sPhase.c_str() << pNode->sEmission.c_str() << pNode->sScale.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_SCATTERING_MEDIUM);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadScatteringMedium()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadVolumeMedium(OctaneVolumeMedium *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t) + sizeof(float) * 3 +  + sizeof(ComplexValue) * 2
        + pNode->sScale.length() + 2
        + pNode->sAbsorption.length() + 2
        + pNode->sAbsorptionRamp.length() + 2
        + pNode->sScattering.length() + 2
        + pNode->sScatteringRamp.length() + 2
        + pNode->sPhase.length() + 2
        + pNode->sEmission.length() + 2
        + pNode->sEmissionRamp.length() + 2
        + pNode->sStepLength.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_VOLUME_MEDIUM, pNode->sName.c_str());
        snd << pNode->absorptionDefaultVal << pNode->scatteringDefaultVal
            << pNode->fPhaseDefaultVal << pNode->fScaleDefaultVal << pNode->fStepLengthDefaultVal
            << pNode->bInvertAbsorption 
            << pNode->sScale.c_str() << pNode->sAbsorption.c_str() << pNode->sAbsorptionRamp.c_str() << pNode->sScattering.c_str()
            << pNode->sScatteringRamp.c_str() << pNode->sPhase.c_str() << pNode->sEmission.c_str() << pNode->sEmissionRamp.c_str()
            << pNode->sStepLength.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_VOLUME_MEDIUM);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadVolumeMedium()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteMedium(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_MEDIUM, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_MEDIUM) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting medium.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteMedium()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TRANSFORMS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadRotationTransform(OctaneRotationTransform *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3 + sizeof(int32_t)
        + pNode->sRotation.length() + 2
        + pNode->sRotationOrder.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_ROTATION_TRANSFORM, pNode->sName.c_str());
        snd << pNode->f3RotationDefaultVal.x << pNode->f3RotationDefaultVal.y << pNode->f3RotationDefaultVal.z << pNode->iRotationOrderDefaultVal << pNode->sRotation << pNode->sRotationOrder;
        snd.write();
    }
    checkResponsePacket(LOAD_ROTATION_TRANSFORM);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadRotationTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadScaleTransform(OctaneScaleTransform *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3
        + pNode->sScale.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_SCALE_TRANSFORM, pNode->sName.c_str());
        snd << pNode->f3ScaleDefaultVal.x << pNode->f3ScaleDefaultVal.y << pNode->f3ScaleDefaultVal.z << pNode->sScale;
        snd.write();
    }
    checkResponsePacket(LOAD_SCALE_TRANSFORM);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadScaleTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadFullTransform(OctaneFullTransform *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    if(pNode->bIsValue) {
        uint64_t size = sizeof(float) * 12 + sizeof(int32_t);

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_VALUE_TRANSFORM, pNode->sName.c_str());
            snd << pNode->iRotationOrderDefaultVal;
            snd.writeBuffer(&pNode->matrix, sizeof(float) * 12);
            snd.write();
        }
        checkResponsePacket(LOAD_VALUE_TRANSFORM);

        UNLOCK_MUTEX(m_SocketMutex);
    }
    else {
        uint64_t size = sizeof(float) * 9 + sizeof(int32_t);

        LOCK_MUTEX(m_SocketMutex);

        {
            RPCSend snd(m_Socket, size, LOAD_FULL_TRANSFORM, pNode->sName.c_str());
            snd << pNode->f3Rotation.x << pNode->f3Rotation.y << pNode->f3Rotation.z
                << pNode->f3Scale.x << pNode->f3Scale.y << pNode->f3Scale.z
                << pNode->f3Translation.x << pNode->f3Translation.y << pNode->f3Translation.z
                << pNode->iRotationOrderDefaultVal;
            snd.write();
        }
        checkResponsePacket(LOAD_FULL_TRANSFORM);

        UNLOCK_MUTEX(m_SocketMutex);
    }
} //uploadFullTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::upload3dTransform(Octane3DTransform *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 9 + sizeof(int32_t)
        + pNode->sRotation.length() + 2
        + pNode->sScale.length() + 2
        + pNode->sTranslation.length() + 2
        + pNode->sRotationOrder.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_3D_TRANSFORM, pNode->sName.c_str());
        snd << pNode->f3RotationDefaultVal.x << pNode->f3RotationDefaultVal.y << pNode->f3RotationDefaultVal.z
            << pNode->f3ScaleDefaultVal.x << pNode->f3ScaleDefaultVal.y << pNode->f3ScaleDefaultVal.z
            << pNode->f3TranslationDefaultVal.x << pNode->f3TranslationDefaultVal.y << pNode->f3TranslationDefaultVal.z
            << pNode->iRotationOrderDefaultVal
            << pNode->sRotation << pNode->sScale << pNode->sTranslation << pNode->sRotationOrder;
        snd.write();
    }
    checkResponsePacket(LOAD_3D_TRANSFORM);

    UNLOCK_MUTEX(m_SocketMutex);
} //upload3dTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::upload2dTransform(Octane2DTransform *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 6
        + pNode->sRotation.length() + 2
        + pNode->sScale.length() + 2
        + pNode->sTranslation.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_2D_TRANSFORM, pNode->sName.c_str());
        snd << pNode->f2RotationDefaultVal.x << pNode->f2RotationDefaultVal.y
            << pNode->f2ScaleDefaultVal.x << pNode->f2ScaleDefaultVal.y
            << pNode->f2TranslationDefaultVal.x << pNode->f2TranslationDefaultVal.y
            << pNode->sRotation << pNode->sScale << pNode->sTranslation;
        snd.write();
    }
    checkResponsePacket(LOAD_2D_TRANSFORM);

    UNLOCK_MUTEX(m_SocketMutex);
} //upload2dTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteTransform(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_TRANSFORM, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_TRANSFORM) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting transform.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteTransform()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadXyzProjection(OctaneXYZProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sTransform.length() + 2
        + pNode->sCoordinateSpace.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_XYZ, pNode->sName.c_str());
        snd << pNode->iCoordinateSpaceDefaultVal
            << pNode->sCoordinateSpace.c_str() << pNode->sTransform.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_XYZ);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadXyzProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadBoxProjection(OctaneBoxProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sTransform.length() + 2
        + pNode->sCoordinateSpace.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_BOX, pNode->sName.c_str());
        snd << pNode->iCoordinateSpaceDefaultVal
            << pNode->sCoordinateSpace.c_str() << pNode->sTransform.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_BOX);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadBoxProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadCylProjection(OctaneCylProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sTransform.length() + 2
        + pNode->sCoordinateSpace.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_CYL, pNode->sName.c_str());
        snd << pNode->iCoordinateSpaceDefaultVal
            << pNode->sCoordinateSpace.c_str() << pNode->sTransform.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_CYL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadCylProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadPerspProjection(OctanePerspProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sTransform.length() + 2
        + pNode->sCoordinateSpace.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_PERSP, pNode->sName.c_str());
        snd << pNode->iCoordinateSpaceDefaultVal
            << pNode->sCoordinateSpace.c_str() << pNode->sTransform.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_PERSP);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadPerspProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadSphericalProjection(OctaneSphericalProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t)
        + pNode->sTransform.length() + 2
        + pNode->sCoordinateSpace.length() + 2;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_SPHERICAL, pNode->sName.c_str());
        snd << pNode->iCoordinateSpaceDefaultVal
            << pNode->sCoordinateSpace.c_str() << pNode->sTransform.c_str();
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_SPHERICAL);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadSphericalProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadUvwProjection(OctaneUVWProjection *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = 0;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_PROJECTION_UVW, pNode->sName.c_str());
        snd.write();
    }
    checkResponsePacket(LOAD_PROJECTION_UVW);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadUvwProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteProjection(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_PROJECTION, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_PROJECTION) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting projection.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteProjection()


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadFloatValue(OctaneFloatValue *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(float) * 3;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_VALUE_FLOAT, pNode->sName.c_str());
        snd << pNode->f3Value.x << pNode->f3Value.y << pNode->f3Value.z;
        snd.write();
    }
    checkResponsePacket(LOAD_VALUE_FLOAT);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadFloatValue()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::uploadIntValue(OctaneIntValue *pNode) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    uint64_t size = sizeof(int32_t);

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, size, LOAD_VALUE_INT, pNode->sName.c_str());
        snd << pNode->iValue;
        snd.write();
    }
    checkResponsePacket(LOAD_VALUE_INT);

    UNLOCK_MUTEX(m_SocketMutex);
} //uploadIntValue()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::deleteValue(string const &sName) {
    if(m_Socket < 0 || m_cBlockUpdates) return;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, 0, DEL_VALUE, sName.c_str());
        snd.write();
    }
    {
        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType != DEL_VALUE) {
            rcv >> m_sErrorMsg;
            fprintf(stderr, "Octane: ERROR deleting value node.");
            if(m_sErrorMsg.length() > 0) fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
            else fprintf(stderr, "\n");
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
} //deleteValue()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// IMAGE BUFFER METHODS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline Octane::RenderPassId OctaneClient::currentPassType() {
    return m_CurPassType;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkImgBuffer8bit(uint8_4 *&puc4Buf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight, bool bCopyToBuf) {
    if((!m_pucImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight || m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) && iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0) {
        if(iWidth < 4) iWidth = 4;
        if(iHeight < 4) iHeight = 4;
        if(iRegionWidth < 4) iRegionWidth = 4;
        if(iRegionHeight < 4) iRegionHeight = 4;

        if(m_pucImageBuf) delete[] m_pucImageBuf;
        size_t stLen  = iRegionWidth * iRegionHeight * 4;
        m_pucImageBuf   = new unsigned char[stLen];

        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        memset(m_pucImageBuf, 1, stLen);
        if(bCopyToBuf) {
            //if(puc4Buf) delete[] puc4Buf;
            puc4Buf = new uint8_4[iRegionWidth * iRegionHeight];
            memcpy(puc4Buf, m_pucImageBuf, iRegionWidth * iRegionHeight * 4);
        }

        return false;
    }
    else if(iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
        if(!m_pucImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 || m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4) {
            iWidth  = m_iCurImgBufWidth = -1;
            iHeight = m_iCurImgBufHeight = -1;
            iRegionWidth    = m_iCurRegionWidth = -1;
            iRegionHeight   = m_iCurRegionHeight = -1;

            return false;
        }
        else {
            iWidth  = m_iCurImgBufWidth;
            iHeight = m_iCurImgBufHeight;
            iRegionWidth    = m_iCurRegionWidth;
            iRegionHeight   = m_iCurRegionHeight;

            m_iCurImgBufWidth = -1;
            m_iCurImgBufHeight = -1;
            m_iCurRegionWidth = -1;
            m_iCurRegionHeight = -1;
        }
    }
    return true;
} //checkImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
inline bool OctaneClient::getImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int &iRegionWidth, int &iRegionHeight) {
    LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, false)) {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
    }
    else {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getImgBuffer8bit()
*/
inline bool OctaneClient::getImgBuffer8bit(int &iComponentsCnt, uint8_t *&pucBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight) {
    LOCK_MUTEX(m_ImgBufMutex);

    if(iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight || iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        if(m_pucImageBuf) {
            delete[] m_pucImageBuf;
            m_pucImageBuf = 0;
            m_stImgBufLen = 0;
        }

        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    if(!m_pucImageBuf || !m_stImgBufLen) {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    iComponentsCnt  = m_iComponentCnt;
    pucBuf          = m_pucImageBuf;
    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
inline bool OctaneClient::getCopyImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int &iRegionWidth, int &iRegionHeight) {
    LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, true)) {
        if(!puc4Buf) puc4Buf = new uint8_4[iWidth * iHeight];

        memcpy(puc4Buf, m_pucImageBuf, iWidth * iHeight * 4);
    }
    else {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }
    
    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getCopyImgBuffer8bit()
*/
inline bool OctaneClient::getCopyImgBuffer8bit(int iComponentsCnt, uint8_t *&pucBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight) {
    //FIXME: Make it respect 8-bit buffer alignment
    return false;

    LOCK_MUTEX(m_ImgBufMutex);

    if(iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight || iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        if(m_pucImageBuf) {
            delete[] m_pucImageBuf;
            m_pucImageBuf = 0;
            m_stImgBufLen = 0;
        }

        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    if(!m_pucImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    size_t stPixelSize = iRegionWidth * iRegionHeight;
    uint8_t* in = m_pucImageBuf;

    switch(iComponentsCnt) {
        case 1: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
                        *pOut = *in;
                    break;
                }
                case 2: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
                        *pOut = *in;
                    break;
                }
                case 3: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
                        *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
                    break;
                }
                case 4: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
                        *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 1
        case 2: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
                        pOut[0] = in[0];
                        pOut[1] = 255;
                    }
                    break;
                }
                case 2: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                    }
                    break;
                }
                case 3: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
                        pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
                        pOut[1] = 255;
                    }
                    break;
                }
                case 4: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
                        pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
                        pOut[1] = in[1];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 2
        case 3: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                    }
                    break;
                }
                case 2: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                    }
                    break;
                }
                case 3: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                    }
                    break;
                }
                case 4: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 3
        case 4: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                        pOut[3] = 255;
                    }
                    break;
                }
                case 2: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                        pOut[3] = in[1];
                    }
                    break;
                }
                case 3: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                        pOut[3] = 255;
                    }
                    break;
                }
                case 4: {
                    if(!pucBuf) pucBuf = new uint8_t[stPixelSize];
                    uint8_t *pOut = pucBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                        pOut[3] = in[3];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 4
        default: {
            UNLOCK_MUTEX(m_ImgBufMutex);
            return false;
            break;
        } //default
    }
    
    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getCopyImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::checkImgBufferFloat(int iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight, bool bCopyToBuf) {
    if((!m_pfImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight || m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) && iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0) {
        if(iWidth < 4) iWidth = 4;
        if(iHeight < 4) iHeight = 4;
        if(iRegionWidth < 4) iRegionWidth = 4;
        if(iRegionHeight < 4) iRegionHeight = 4;

        if(m_pfImageBuf) delete[] m_pfImageBuf;
        size_t stLen = iRegionWidth * iRegionHeight * 4;
        m_pfImageBuf = new float[stLen];

        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        memset(m_pfImageBuf, 0, stLen * sizeof(float));
        if(bCopyToBuf) {
            pfBuf = new float[iRegionWidth * iRegionHeight * iComponentsCnt];
        	memset(pfBuf, 0, iRegionWidth * iRegionHeight * iComponentsCnt * sizeof(float));
        }

        return false;
    }
    else if(iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
        if(!m_pfImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 || m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4) {
            iWidth  = m_iCurImgBufWidth = -1;
            iHeight = m_iCurImgBufHeight = -1;
            iRegionWidth    = m_iCurRegionWidth = -1;
            iRegionHeight   = m_iCurRegionHeight = -1;

            return false;
        }
        else {
            iWidth  = m_iCurImgBufWidth;
            iHeight = m_iCurImgBufHeight;
            iRegionWidth    = m_iCurRegionWidth;
            iRegionHeight   = m_iCurRegionHeight;

            m_iCurImgBufWidth = -1;
            m_iCurImgBufHeight = -1;
            m_iCurRegionWidth = -1;
            m_iCurRegionHeight = -1;
        }
    }
    return true;
} //checkImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::getImgBufferFloat(int &iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight) {
    LOCK_MUTEX(m_ImgBufMutex);

    if(iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight || iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        if(m_pfImageBuf) {
            delete[] m_pfImageBuf;
            m_pfImageBuf = 0;
            m_stImgBufLen = 0;
        }

        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    if(!m_pfImageBuf || !m_stImgBufLen) {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    iComponentsCnt  = m_iComponentCnt;
    pfBuf           = m_pfImageBuf;
    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::getCopyImgBufferFloat(int iComponentsCnt, float *&pfBuf, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight) {
    LOCK_MUTEX(m_ImgBufMutex);

    if(iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight || iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight) {
        m_iCurImgBufWidth   = iWidth;
        m_iCurImgBufHeight  = iHeight;
        m_iCurRegionWidth   = iRegionWidth;
        m_iCurRegionHeight  = iRegionHeight;

        if(m_pfImageBuf) {
            delete[] m_pfImageBuf;
            m_pfImageBuf = 0;
            m_stImgBufLen = 0;
        }

        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    if(!m_pfImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    size_t stPixelSize = iRegionWidth * iRegionHeight;
    float* in = m_pfImageBuf;

    switch(iComponentsCnt) {
        case 1: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
                        *pOut = *in;
                    break;
                }
                case 2: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
                        *pOut = *in;
                    break;
                }
                case 3: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
                        *pOut = (in[0] + in[1] + in[2]) / 3.0f;
                    break;
                }
                case 4: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
                        *pOut = (in[0] + in[1] + in[2]) / 3.0f;
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 1
        case -1: { //Usable for MaterialId pass in host-applications requiring just one ID number instead of color
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
                        *pOut = *in;
                    break;
                }
                case 2: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
                        *pOut = *in;
                    break;
                }
                case 3: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
                        *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) | ((uint32_t)(in[2] * 255));
                    break;
                }
                case 4: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
                        *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) | ((uint32_t)(in[2] * 255));
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case -1
        case 2: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
                        pOut[0] = in[0];
                        pOut[1] = 1.0f;
                    }
                    break;
                }
                case 2: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                    }
                    break;
                }
                case 3: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
                        pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
                        pOut[1] = 1.0f;
                    }
                    break;
                }
                case 4: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
                        pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
                        pOut[1] = in[1];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 2
        case 3: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                    }
                    break;
                }
                case 2: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                    }
                    break;
                }
                case 3: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                    }
                    break;
                }
                case 4: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 3
        case 4: {
            switch(m_iComponentCnt) {
                case 1: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                        pOut[3] = 1.0f;
                    }
                    break;
                }
                case 2: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[0];
                        pOut[2] = in[0];
                        pOut[3] = in[1];
                    }
                    break;
                }
                case 3: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                        pOut[3] = 1.0f;
                    }
                    break;
                }
                case 4: {
                    if(!pfBuf) pfBuf = new float[stPixelSize];
                    float *pOut = pfBuf;
                    for(int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
                        pOut[0] = in[0];
                        pOut[1] = in[1];
                        pOut[2] = in[2];
                        pOut[3] = in[3];
                    }
                    break;
                }
                default: {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    return false;
                    break;
                }
            }
            break;
        } //case 4
        default: {
            UNLOCK_MUTEX(m_ImgBufMutex);
            return false;
            break;
        } //default
    }
    
    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getCopyImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline bool OctaneClient::downloadImageBuffer(RenderStatistics &renderStat, ImageType const imgType, RenderPassId &passType, bool const bForce) {
    if(m_Socket < 0) return false;

    LOCK_MUTEX(m_SocketMutex);

    while(true) {
        {
            RPCSend snd(m_Socket, sizeof(int32_t) * 4 + sizeof(uint32_t), GET_IMAGE);
            snd << bForce << imgType << m_iCurImgBufWidth << m_iCurImgBufHeight << passType;
            snd.write();
        }

        RPCReceive rcv(m_Socket);
        if(rcv.m_PacketType == GET_IMAGE) {
            uint32_t uiW, uiH, uiRegW, uiRegH, uiSamples;
            rcv >> renderStat.ulVramUsed >> renderStat.ulVramFree >> renderStat.ulVramTotal >> renderStat.fSPS >> renderStat.fRenderTime >> renderStat.fGamma >> passType >> renderStat.iExpiryTime >> renderStat.iComponentsCnt >> renderStat.uiTrianglesCnt >> renderStat.uiMeshesCnt >> renderStat.uiSpheresCnt >> renderStat.uiVoxelsCnt >> renderStat.uiDisplCnt >> renderStat.uiHairsCnt >> renderStat.uiRgb32Cnt
                >> renderStat.uiRgb64Cnt >> renderStat.uiGrey8Cnt >> renderStat.uiGrey16Cnt >> uiSamples >> renderStat.uiMaxSamples >> uiW >> uiH >> uiRegW >> uiRegH >> renderStat.uiNetGPUs >> renderStat.uiNetGPUsUsed;

            renderStat.uiW = uiW;
            renderStat.uiH = uiH;
            renderStat.uiRegW = uiRegW;
            renderStat.uiRegH = uiRegH;

            if(m_iComponentCnt != renderStat.iComponentsCnt) m_iComponentCnt = renderStat.iComponentsCnt;

            if(uiSamples && renderStat.uiCurSamples != uiSamples) renderStat.uiCurSamples = uiSamples;

            if(m_iCurImgBufWidth < 0 || m_iCurImgBufHeight < 0 || m_iCurRegionWidth < 0 || m_iCurRegionHeight < 0) {
                m_iCurImgBufWidth   = static_cast<int>(uiW);
                m_iCurImgBufHeight  = static_cast<int>(uiH);
                m_iCurRegionWidth   = static_cast<int>(uiRegW);
                m_iCurRegionHeight  = static_cast<int>(uiRegH);
            }

            LOCK_MUTEX(m_ImgBufMutex);

            size_t stLen = uiRegW * uiRegH * renderStat.iComponentsCnt;

            if(m_CurPassType != passType) m_CurPassType = passType;

            if(imgType == IMAGE_8BIT) {
                size_t stSrcStringSize = uiRegW * renderStat.iComponentsCnt;
                size_t stDstStringSize = ((uiRegW * renderStat.iComponentsCnt) / 4 + ((uiRegW * renderStat.iComponentsCnt) % 4 ? 1 : 0)) * 4;
                size_t stDstLen = stDstStringSize * uiRegH;

                if(!m_pucImageBuf || m_stImgBufLen != stDstLen) {
                    m_stImgBufLen = stDstLen;

                    if(m_pucImageBuf) delete[] m_pucImageBuf;
                    if(stLen) m_pucImageBuf = new unsigned char[stDstLen];
                    else m_pucImageBuf = 0;

                    if(m_pfImageBuf) delete[] m_pfImageBuf;
                    if(stLen) m_pfImageBuf = new float[stLen];
                    else m_pfImageBuf = 0;
                }

                if(!m_pucImageBuf) {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    UNLOCK_MUTEX(m_SocketMutex);
                    return false;
                }

                uint8_t *ucBuf  = (uint8_t*)rcv.readBuffer(stLen);

                //if(ucBuf) memcpy(m_pucImageBuf, ucBuf, stLen);
                uint8_t *p = m_pucImageBuf;
                uint8_t *s = ucBuf;
                for(int y = 0; y < uiRegH; ++y) {
                    memcpy(p, s, stSrcStringSize);
                    p += stDstStringSize;
                    s += stSrcStringSize;
                }
            }
            else {
                if(!m_pfImageBuf || m_stImgBufLen != stLen) {
                    m_stImgBufLen = stLen;

                    if(m_pfImageBuf) delete[] m_pfImageBuf;
                    if(stLen) m_pfImageBuf = new float[stLen];
                    else m_pfImageBuf = 0;

                    if(m_pucImageBuf) delete[] m_pucImageBuf;
                    if(stLen) m_pucImageBuf = new unsigned char[stLen];
                    else m_pucImageBuf = 0;
                }

                if(!m_pfImageBuf) {
                    UNLOCK_MUTEX(m_ImgBufMutex);
                    UNLOCK_MUTEX(m_SocketMutex);
                    return false;
                }

                float* pfBuf = (float*)rcv.readBuffer(stLen * sizeof(float));

                if(pfBuf) memcpy(m_pfImageBuf, pfBuf, stLen * sizeof(float));
            }

            UNLOCK_MUTEX(m_ImgBufMutex);
            break;
        }
        else if(!bForce) {
            std::string sError;
            rcv >> sError;
            if(sError.length() > 0) {
                fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
                m_sErrorMsg += sError;
            }

            if(imgType == IMAGE_8BIT && m_pucImageBuf && m_stImgBufLen) {
                UNLOCK_MUTEX(m_SocketMutex);
                return true;
            }
            else if(imgType != IMAGE_8BIT && m_pfImageBuf && m_stImgBufLen) {
                UNLOCK_MUTEX(m_SocketMutex);
                return true;
            }
            else {
                UNLOCK_MUTEX(m_SocketMutex);
                return false;
            }
        }
        else {
            std::string sError;
            rcv >> sError;
            if(sError.length() > 0) {
                fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
                m_sErrorMsg += sError;
            }

            UNLOCK_MUTEX(m_SocketMutex);
            return false;
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return true;
} //downloadImageBuffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline unsigned char* OctaneClient::getPreview(std::string sName, uint32_t &uiWidth, uint32_t &uiHeight) {
    if(m_Socket < 0) return nullptr;
    unsigned char *pucImageBuf = 0;

    LOCK_MUTEX(m_SocketMutex);

    {
        RPCSend snd(m_Socket, sizeof(uint32_t) * 2, GET_PREVIEW, sName.c_str());
        snd << uiWidth << uiHeight;
        snd.write();
    }

    RPCReceive rcv(m_Socket);
    if(rcv.m_PacketType == GET_PREVIEW) {
        uint32_t uiW, uiH;
        rcv >> uiW >> uiH;

        size_t stLen = uiW * uiH * 4;

        if(stLen) {
            uiWidth = uiW;
            uiHeight = uiH;

            uint8_t *ucBuf  = (uint8_t*)rcv.readBuffer(stLen);

            if(ucBuf) {
                pucImageBuf = new unsigned char[stLen];
                memcpy(pucImageBuf, ucBuf, stLen);
            }
        }
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return pucImageBuf;
} //getPreview()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline void OctaneClient::setUpdatesBlocked(bool bBlocked) {
    m_cBlockUpdates = bBlocked ? 1 : 0;
    return;
} //getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline OctaneClient::RenderServerInfo& OctaneClient::getServerInfo(void) {
    return m_ServerInfo;
} //getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inline OctaneClient::FailReasons::FailReasonsEnum OctaneClient::getFailReason(void) {
    return m_FailReason;
} //getFailReason()

} //namespace OctaneEngine

#endif /* __OCTANECLIENT_H__ */
