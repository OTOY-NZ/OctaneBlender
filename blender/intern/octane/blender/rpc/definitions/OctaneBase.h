// clang-format off
#ifndef __OCTANE_BASE_H__
#define __OCTANE_BASE_H__
#include "msgpack.hpp"
#include <vector>

#ifndef OCTANE_SERVER_MAJOR_VERSION
#  define OCTANE_SERVER_MAJOR_VERSION "20"
#endif
#ifndef OCTANE_SERVER_MINOR_VERSION
#  define OCTANE_SERVER_MINOR_VERSION "4"
#endif

#ifdef OCTANE_SERVER
#include "octaneapi.h"
#else
namespace Octane {
#define PIN_TYPE(_name, _enum)   _name = _enum,
	enum NodePinType {
		PIN_TYPE(PT_UNKNOWN           , 0)

		PIN_TYPE(PT_ANIMATION_SETTINGS, 27)
		PIN_TYPE(PT_BIT_MASK          , 31)
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
		PIN_TYPE(PT_LUT               , 28)
		PIN_TYPE(PT_MATERIAL          , 7)
		PIN_TYPE(PT_MATERIAL_LAYER    , 33)
		PIN_TYPE(PT_MEDIUM            , 13)
		PIN_TYPE(PT_OBJECTLAYER       , 17)
		PIN_TYPE(PT_PHASEFUNCTION     , 14)
		PIN_TYPE(PT_POSTPROCESSING    , 18)
		PIN_TYPE(PT_PROJECTION        , 21)
		PIN_TYPE(PT_RENDER_JOB        , 29)
		PIN_TYPE(PT_RENDER_LAYER      , 25)
		PIN_TYPE(PT_RENDER_PASSES     , 24)
		PIN_TYPE(PT_RENDERTARGET      , 19)
		PIN_TYPE(PT_ROUND_EDGES       , 32)
		PIN_TYPE(PT_STRING            , 23)
		PIN_TYPE(PT_TEXTURE           , 5)
		PIN_TYPE(PT_TOON_RAMP         , 30)
		PIN_TYPE(PT_TRANSFORM         , 4)
		PIN_TYPE(PT_VOLUME_RAMP       , 26)
		PIN_TYPE(PT_WORK_PANE         , 20)
	};
#undef PIN_TYPE

#define NODE_TYPE(_name, _enum)   _name = _enum,
	enum NodeType {
		NODE_TYPE(NT_UNKNOWN                    ,   0)

		NODE_TYPE(NT_ANIMATION_SETTINGS         ,  99)
		NODE_TYPE(NT_ANNOTATION                 ,  68)
		NODE_TYPE(NT_BIT_MASK                   , 132)
		NODE_TYPE(NT_BOOL                       ,  11)
		NODE_TYPE(NT_CAM_BAKING                 ,  94)
		NODE_TYPE(NT_CAM_OSL                    , 126)
		NODE_TYPE(NT_CAM_OSL_BAKING             , 128)
		NODE_TYPE(NT_CAM_PANORAMIC              ,  62)
		NODE_TYPE(NT_CAM_THINLENS               ,  13)
		NODE_TYPE(NT_DIRECTORY                  , 101)
		NODE_TYPE(NT_DISPLACEMENT               ,  80)
		NODE_TYPE(NT_EMIS_BLACKBODY             ,  53)
		NODE_TYPE(NT_EMIS_TEXTURE               ,  54)
		NODE_TYPE(NT_ENUM                       ,  57)
		NODE_TYPE(NT_ENV_DAYLIGHT               ,  14)
		NODE_TYPE(NT_ENV_PLANETARY              , 129)
		NODE_TYPE(NT_ENV_TEXTURE                ,  37)
		NODE_TYPE(NT_FILE                       ,  88)
		NODE_TYPE(NT_FILM_SETTINGS              , 100)
		NODE_TYPE(NT_FLOAT                      ,   6)
		NODE_TYPE(NT_GEO_GROUP                  ,   3)
		NODE_TYPE(NT_GEO_PLANE                  , 110)
		NODE_TYPE(NT_GEO_JOINT                  , 102)
		NODE_TYPE(NT_GEO_MESH                   ,   1)
		NODE_TYPE(NT_GEO_VOLUME                 ,  91)
		NODE_TYPE(NT_GEO_VOLUME_SDF             , 134)
		NODE_TYPE(NT_GEO_PLACEMENT              ,   4)
		NODE_TYPE(NT_GEO_SCATTER                ,   5)
		NODE_TYPE(NT_GEO_OSL                    , 133)
		NODE_TYPE(NT_IMAGER_CAMERA              ,  15)
		NODE_TYPE(NT_IMPORT_ALEMBIC_PREFS       ,  82)
		NODE_TYPE(NT_IMPORT_FBX_PREFS           , 119)
		NODE_TYPE(NT_IMPORT_IMAGE_PREFS         , 112)
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
		NODE_TYPE(NT_LUT_CUSTOM                 , 103)
		NODE_TYPE(NT_MAT_COMPOSITE              , 138)
		NODE_TYPE(NT_MAT_DIFFUSE                ,  17)
		NODE_TYPE(NT_MAT_DIFFUSE_LAYER          , 140)
		NODE_TYPE(NT_MAT_GLOSSY                 ,  16)
		NODE_TYPE(NT_MAT_LAYER                  , 143)
		NODE_TYPE(NT_MAT_LAYER_GROUP            , 144)
		NODE_TYPE(NT_MAT_SHADOW_CATCHER         , 145)
		NODE_TYPE(NT_MAT_SHEEN_LAYER            , 142)
		NODE_TYPE(NT_MAT_SPECULAR_LAYER         , 139)
		NODE_TYPE(NT_MAT_MAP                    ,   2)
		NODE_TYPE(NT_MAT_METAL                  , 120)
		NODE_TYPE(NT_MAT_METALLIC_LAYER         , 141)
		NODE_TYPE(NT_MAT_MIX                    ,  19)
		NODE_TYPE(NT_MAT_OSL                    , 116)
		NODE_TYPE(NT_MAT_PORTAL                 ,  20)
		NODE_TYPE(NT_MAT_SPECULAR               ,  18)
		NODE_TYPE(NT_MAT_TOON                   , 121)
		NODE_TYPE(NT_MAT_UNIVERSAL              , 130)
		NODE_TYPE(NT_MED_ABSORPTION             ,  58)
		NODE_TYPE(NT_MED_SCATTERING             ,  59)
		NODE_TYPE(NT_MED_VOLUME                 ,  98)
		NODE_TYPE(NT_OBJECTLAYER                ,  65)
		NODE_TYPE(NT_OBJECTLAYER_MAP            ,  64)
		NODE_TYPE(NT_ORC_VERSION                ,  92)
		NODE_TYPE(NT_PHASE_SCHLICK              ,  60)
		NODE_TYPE(NT_POSTPROCESSING             ,  61)
		NODE_TYPE(NT_PROGRAMMABLE_GRAPH_INPUT   ,  85)
		NODE_TYPE(NT_PROJ_BOX                   ,  79)
		NODE_TYPE(NT_PROJ_CYLINDRICAL           ,  74)
		NODE_TYPE(NT_PROJ_LINEAR                ,  75)
		NODE_TYPE(NT_PROJ_OSL                   , 125)
		NODE_TYPE(NT_PROJ_OSL_UV                , 127)
		NODE_TYPE(NT_PROJ_PERSPECTIVE           ,  76)
		NODE_TYPE(NT_PROJ_SPHERICAL             ,  77)
		NODE_TYPE(NT_PROJ_TRIPLANAR             , 111)
		NODE_TYPE(NT_PROJ_UVW                   ,  78)
		NODE_TYPE(NT_PROJECT_SETTINGS           ,  70)
		NODE_TYPE(NT_RENDER_JOB_GROUP           , 105)
		NODE_TYPE(NT_RENDER_LAYER               ,  90)
		NODE_TYPE(NT_RENDER_PASSES              ,  86)
		NODE_TYPE(NT_RENDERTARGET               ,  56)
		NODE_TYPE(NT_ROUND_EDGES                , 137)
		NODE_TYPE(NT_SPLIT_PANE                 ,  72)
		NODE_TYPE(NT_STRING                     ,  84)
		NODE_TYPE(NT_SUN_DIRECTION              ,  30)
		NODE_TYPE(NT_TEX_ALPHAIMAGE             ,  35)
		NODE_TYPE(NT_TEX_ADD                    , 106)
		NODE_TYPE(NT_TEX_BAKED_IMAGE            , 115)
		NODE_TYPE(NT_TEX_CHECKS                 ,  45)
		NODE_TYPE(NT_TEX_CLAMP                  ,  41)
		NODE_TYPE(NT_TEX_COLOUR_VERTEXATTRIBUTE , 135)
		NODE_TYPE(NT_TEX_COLORCORRECTION        ,  51)
		NODE_TYPE(NT_TEX_COMPARE                , 107)
		NODE_TYPE(NT_TEX_COSINEMIX              ,  40)
		NODE_TYPE(NT_TEX_DIRT                   ,  63)
		NODE_TYPE(NT_TEX_FALLOFF                ,  50)
		NODE_TYPE(NT_TEX_FLOAT                  ,  31)
		NODE_TYPE(NT_TEX_FLOAT_VERTEXATTRIBUTE  , 136)
		NODE_TYPE(NT_TEX_FLOATIMAGE             ,  36)
		NODE_TYPE(NT_TEX_GAUSSIANSPECTRUM       ,  32)
		NODE_TYPE(NT_TEX_GRADIENT               ,  49)
		NODE_TYPE(NT_TEX_IMAGE                  ,  34)
		NODE_TYPE(NT_TEX_IMAGE_TILES            , 131)
		NODE_TYPE(NT_TEX_INSTANCE_COLOR         , 113)
		NODE_TYPE(NT_TEX_INSTANCE_RANGE         , 114)
		NODE_TYPE(NT_TEX_INVERT                 ,  46)
		NODE_TYPE(NT_TEX_MARBLE                 ,  47)
		NODE_TYPE(NT_TEX_MIX                    ,  38)
		NODE_TYPE(NT_TEX_MULTIPLY               ,  39)
		NODE_TYPE(NT_TEX_NOISE                  ,  87)
		NODE_TYPE(NT_TEX_OSL                    , 117)
		NODE_TYPE(NT_TEX_RANDOMCOLOR            ,  81)
		NODE_TYPE(NT_TEX_RGB                    ,  33)
		NODE_TYPE(NT_TEX_RGFRACTAL              ,  48)
		NODE_TYPE(NT_TEX_SAWWAVE                ,  42)
		NODE_TYPE(NT_TEX_SINEWAVE               ,  44)
		NODE_TYPE(NT_TEX_SIDE                   ,  89)
		NODE_TYPE(NT_TEX_SUBTRACT               , 108)
		NODE_TYPE(NT_TEX_TRIANGLEWAVE           ,  43)
		NODE_TYPE(NT_TEX_TRIPLANAR              , 109)
		NODE_TYPE(NT_TEX_TURBULENCE             ,  22)
		NODE_TYPE(NT_TEX_UVW_TRANSFORM          , 118)
		NODE_TYPE(NT_TEX_W                      , 104)
		NODE_TYPE(NT_TOON_DIRECTIONAL_LIGHT     , 124)
		NODE_TYPE(NT_TOON_POINT_LIGHT           , 123)
		NODE_TYPE(NT_TOON_RAMP                  , 122)
		NODE_TYPE(NT_TRANSFORM_2D               ,  66)
		NODE_TYPE(NT_TRANSFORM_3D               ,  27)
		NODE_TYPE(NT_TRANSFORM_ROTATION         ,  29)
		NODE_TYPE(NT_TRANSFORM_SCALE            ,  28)
		NODE_TYPE(NT_TRANSFORM_VALUE            ,  67)
		NODE_TYPE(NT_VERTEX_DISPLACEMENT        ,  97)
		NODE_TYPE(NT_VERTEX_DISPLACEMENT_MIXER  , 151)
		NODE_TYPE(NT_VOLUME_RAMP                ,  95)
		NODE_TYPE(NT_WORK_PANE                  ,  73)

		// The input linker node types.
		NODE_TYPE(NT_IN_OFFSET                  , 20000)
		NODE_TYPE(NT_IN_ANIMATION_SETTINGS      , NT_IN_OFFSET + PT_ANIMATION_SETTINGS)
		NODE_TYPE(NT_IN_BIT_MASK                , NT_IN_OFFSET + PT_BIT_MASK)
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
		NODE_TYPE(NT_IN_LUT                     , NT_IN_OFFSET + PT_LUT)
		NODE_TYPE(NT_IN_MATERIAL                , NT_IN_OFFSET + PT_MATERIAL)
		NODE_TYPE(NT_IN_MEDIUM                  , NT_IN_OFFSET + PT_MEDIUM)
		NODE_TYPE(NT_IN_OBJECTLAYER             , NT_IN_OFFSET + PT_OBJECTLAYER)
		NODE_TYPE(NT_IN_PHASEFUNCTION           , NT_IN_OFFSET + PT_PHASEFUNCTION)
		NODE_TYPE(NT_IN_POSTPROCESSING          , NT_IN_OFFSET + PT_POSTPROCESSING)
		NODE_TYPE(NT_IN_PROJECTION              , NT_IN_OFFSET + PT_PROJECTION)
		NODE_TYPE(NT_IN_RENDER_JOB              , NT_IN_OFFSET + PT_RENDER_JOB)
		NODE_TYPE(NT_IN_RENDER_LAYER            , NT_IN_OFFSET + PT_RENDER_LAYER)
		NODE_TYPE(NT_IN_RENDER_PASSES           , NT_IN_OFFSET + PT_RENDER_PASSES)
		NODE_TYPE(NT_IN_RENDERTARGET            , NT_IN_OFFSET + PT_RENDERTARGET)
		NODE_TYPE(NT_IN_ROUND_EDGES             , NT_IN_OFFSET + PT_ROUND_EDGES)
		NODE_TYPE(NT_IN_STRING                  , NT_IN_OFFSET + PT_STRING)
		NODE_TYPE(NT_IN_TEXTURE                 , NT_IN_OFFSET + PT_TEXTURE)
		NODE_TYPE(NT_IN_TOON_RAMP               , NT_IN_OFFSET + PT_TOON_RAMP)
		NODE_TYPE(NT_IN_TRANSFORM               , NT_IN_OFFSET + PT_TRANSFORM)
		NODE_TYPE(NT_IN_VOLUME_RAMP             , NT_IN_OFFSET + PT_VOLUME_RAMP)

		// The output linker node types.
		NODE_TYPE(NT_OUT_OFFSET                 , 30000)
		NODE_TYPE(NT_OUT_ANIMATION_SETTINGS     , NT_OUT_OFFSET + PT_ANIMATION_SETTINGS)
		NODE_TYPE(NT_OUT_BIT_MASK               , NT_OUT_OFFSET + PT_BIT_MASK)
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
		NODE_TYPE(NT_OUT_LUT                    , NT_OUT_OFFSET + PT_LUT)
		NODE_TYPE(NT_OUT_MATERIAL               , NT_OUT_OFFSET + PT_MATERIAL)
		NODE_TYPE(NT_OUT_MEDIUM                 , NT_OUT_OFFSET + PT_MEDIUM)
		NODE_TYPE(NT_OUT_OBJECTLAYER            , NT_OUT_OFFSET + PT_OBJECTLAYER)
		NODE_TYPE(NT_OUT_PHASEFUNCTION          , NT_OUT_OFFSET + PT_PHASEFUNCTION)
		NODE_TYPE(NT_OUT_POSTPROCESSING         , NT_OUT_OFFSET + PT_POSTPROCESSING)
		NODE_TYPE(NT_OUT_PROJECTION             , NT_OUT_OFFSET + PT_PROJECTION)
		NODE_TYPE(NT_OUT_RENDER_JOB             , NT_OUT_OFFSET + PT_RENDER_JOB)
		NODE_TYPE(NT_OUT_RENDER_LAYER           , NT_OUT_OFFSET + PT_RENDER_LAYER)
		NODE_TYPE(NT_OUT_RENDER_PASSES          , NT_OUT_OFFSET + PT_RENDER_PASSES)
		NODE_TYPE(NT_OUT_RENDERTARGET           , NT_OUT_OFFSET + PT_RENDERTARGET)
		NODE_TYPE(NT_OUT_ROUND_EDGES            , NT_OUT_OFFSET + PT_ROUND_EDGES)
		NODE_TYPE(NT_OUT_STRING                 , NT_OUT_OFFSET + PT_STRING)
		NODE_TYPE(NT_OUT_TEXTURE                , NT_OUT_OFFSET + PT_TEXTURE)
		NODE_TYPE(NT_OUT_TOON_RAMP              , NT_OUT_OFFSET + PT_TOON_RAMP)
		NODE_TYPE(NT_OUT_TRANSFORM              , NT_OUT_OFFSET + PT_TRANSFORM)
		NODE_TYPE(NT_OUT_VOLUME_RAMP            , NT_OUT_OFFSET + PT_VOLUME_RAMP)


		//--- deprecated ---

		NODE_TYPE(_NT_FLOAT2                    , 7)      // replaced by NT_FLOAT
		NODE_TYPE(_NT_FLOAT3                    , 8)      // replaced by NT_FLOAT
		NODE_TYPE(_NT_INT2                      , 10)     // replaced by NT_INT
		NODE_TYPE(_NT_CAMERARESPONSE            , 21)     // replaced by NT_ENUM
		NODE_TYPE(_NT_REMOTE_APP_PREFS          , 71)     // not used anymore
		NODE_TYPE(_NT_COATING_LAYER             ,150)     // not used anymore
	};
#undef NODE_TYPE

	enum FalloffTextureMode {
		FALLOFF_NORMAL_VS_EYE_RAY,
		FALLOFF_NORMAL_VS_VECTOR_90DEG,
		FALLOFF_NORMAL_VS_VECTOR_180DEG,
	};
}
#endif

MSGPACK_ADD_ENUM(Octane::NodeType);
MSGPACK_ADD_ENUM(Octane::NodePinType);

namespace OctaneDataTransferObject {

#ifdef __GNUC__
	typedef int8_t                int8_t;
	typedef int32_t               int32_t;
	typedef int64_t               int64_t;
	typedef uint8_t               uint8_t;
	typedef uint32_t              uint32_t;
	typedef uint64_t              uint64_t;
#elif defined(_MSC_VER)
	typedef __int8                  int8_t;
	typedef __int32                 int32_t;
	typedef __int64                 int64_t;
	typedef unsigned __int8         uint8_t;
	typedef unsigned __int32        uint32_t;
	typedef unsigned __int64        uint64_t;
#else
	typedef char                    int8_t;
	typedef int                     int32_t;
	typedef long long int           int64_t;
	typedef unsigned char           uint8_t;
	typedef unsigned int            uint32_t;
	typedef unsigned long long int  uint64_t;
#endif

#pragma pack(push, 4)
	template <class ST>
	struct Vec2
	{
		static const uint32_t DIM_COUNT = 2;

		ST x;
		ST y;

		Vec2(const ST x = 0, const ST y = 0) : x(x), y(y){}
		void set(const ST _x, const ST _y, const ST _z) { x = _x; y = _y; }
		Vec2& operator=(const Vec2<ST>& other) { if (&other != this) { x = other.x; y = other.y; } return *this; }
		inline bool operator==(const Vec2<ST> &r) { return x == r.x && y == r.y; }
		inline bool operator!=(const Vec2<ST> &r) { return x != r.x || y != r.y; }
#ifdef OCTANE_SERVER
		Vec2& operator=(const Octane::Vec2<ST>& other) { x = other.x; y = other.y; return *this; }
#endif
		MSGPACK_DEFINE(x, y);
	};
#pragma pack(pop)
	typedef Vec2<float>    float_2;
	typedef Vec2<int32_t>  int32_2;

#pragma pack(push, 4)
	template <class ST>
	struct Vec3
	{
		static const uint32_t DIM_COUNT = 3;

		ST x;
		ST y;
		ST z;

		Vec3(const ST x = 0, const ST y = 0, const ST z = 0) : x(x), y(y), z(z){}
		void set(const ST _x, const ST _y, const ST _z) { x = _x; y = _y; z = _z; }
		Vec3& operator=(const Vec3<ST>& other) { if (&other != this) { x = other.x; y = other.y; z = other.z; } return *this; }
		inline bool operator==(const Vec3<ST> &r) { return x == r.x && y == r.y && z == r.z; }
		inline bool operator!=(const Vec3<ST> &r) { return x != r.x || y != r.y || z != r.z; }
#ifdef OCTANE_SERVER
		Vec3& operator=(const Octane::Vec3<ST>& other) { x = other.x; y = other.y; z = other.z; return *this; }
#endif
		MSGPACK_DEFINE(x, y, z);
	};
#pragma pack(pop)
	typedef Vec3<float>    float_3;
	typedef Vec3<int32_t>  int32_3;

#pragma pack(push, 4)
	template <class ST>
	struct Vec4
	{
		static const uint32_t DIM_COUNT = 4;

		ST x;
		ST y;
		ST z;
		ST w;

		Vec4(const ST x = 0, const ST y = 0, const ST z = 0, const ST w = 0) : x(x), y(y), z(z), w(w){}
		void set(const ST _x, const ST _y, const ST _z, const ST _w) { x = _x; y = _y; z = _z; w = _w; }
		Vec4& operator=(const Vec4<ST>& other) { if (&other != this) { x = other.x; y = other.y; z = other.z; w = other.w; } return *this; }
		inline bool operator==(const Vec4<ST> &r) { return x == r.x && y == r.y && z == r.z && w == r.w; }
		inline bool operator!=(const Vec4<ST> &r) { return x != r.x || y != r.y || z != r.z || w != r.w; }
#ifdef OCTANE_SERVER
		Vec4& operator=(const Octane::Vec4<ST>& other) { x = other.x; y = other.y; z = other.z; w = other.w; return *this; }
#endif
		MSGPACK_DEFINE(x, y, z, w);
	};
#pragma pack(pop)
	typedef Vec4<float>    float_4;

#pragma pack(push, 4)
	template <class ST>
	struct Matrix
	{
		/// every Vec4 is one row
		Vec4<ST> m[3];
		Matrix<ST>& operator=(const Matrix<ST>& other) { if (&other != this) { m[0] = other.m[0]; m[1] = other.m[1]; m[2] = other.m[2]; } return *this; }
#ifdef OCTANE_SERVER
		Matrix<ST>& operator=(const Octane::Matrix<ST>& other) { m[0] = other.m[0]; m[1] = other.m[1]; m[2] = other.m[2]; return *this; }
#endif
		MSGPACK_DEFINE(m);
	};
#pragma pack(pop)
	typedef Matrix<float>  MatrixF;

#ifdef __GNUC__
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
}

namespace OctaneDataTransferObject {
	enum OctaneDTOType {
		DTO_NONE = 0,
		DTO_BOOL,
		DTO_FLOAT,
		DTO_FLOAT_2,
		DTO_FLOAT_3,
		DTO_RGB,
		DTO_ENUM,
		DTO_INT,
		DTO_INT_2,
		DTO_INT_3,
		DTO_STR,
		DTO_SHADER
	};

	struct OctaneDTOBase {
		OctaneDTOType type;
		std::string sName;
		bool bUseSocket;
		bool bUseLinked;
		std::string sLinkNodeName;
		OctaneDTOBase(const std::string &name, OctaneDTOType type = DTO_NONE, bool bUseSocket = true) : 
			type(type), sName(name), bUseSocket(bUseSocket), bUseLinked(false), sLinkNodeName("") {}
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOBase& obj);
		MSGPACK_DEFINE(bUseLinked, sLinkNodeName)
	};

	struct OctaneDTOBool : OctaneDTOBase {		
		bool bVal;
		OctaneDTOBool() : OctaneDTOBase("", DTO_BOOL), bVal(false) {}
		OctaneDTOBool(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_BOOL, bUseSocket), bVal(false) {}
		inline operator bool() { return bVal; }
		inline bool operator==(const bool& val) { return bVal == val; }
		inline bool operator!=(const bool& val) { return bVal != val; }
		inline OctaneDTOBool& operator=(const bool& val) { bVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOBool& obj);
		MSGPACK_DEFINE(bVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOFloat : OctaneDTOBase {		
		float fVal;
		OctaneDTOFloat() : OctaneDTOBase("", DTO_FLOAT), fVal(0) {}
		OctaneDTOFloat(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_FLOAT, bUseSocket), fVal(0) {}
		inline bool operator==(const float& val) { return fVal == val; }
		inline bool operator!=(const float& val) { return fVal != val; }
		inline OctaneDTOFloat& operator=(const float& val) { fVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat& obj);
		MSGPACK_DEFINE(fVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOFloat2 : OctaneDTOBase {		
		float_2 fVal;
		OctaneDTOFloat2() : OctaneDTOBase("", DTO_FLOAT_2) { fVal.x = fVal.y = 0; }
		OctaneDTOFloat2(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_FLOAT_2, bUseSocket) { fVal.x = fVal.y = 0; }
		inline bool operator==(const float_2& val) { return fVal == val; }
		inline bool operator!=(const float_2& val) { return fVal != val; }
		inline OctaneDTOFloat2& operator=(const float_2& val) { fVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat2& obj);
		MSGPACK_DEFINE(fVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOFloat3 : OctaneDTOBase {		
		float_3 fVal;
		OctaneDTOFloat3() : OctaneDTOBase("", DTO_FLOAT_3) { fVal.x = fVal.y = fVal.z = 0; }
		OctaneDTOFloat3(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_FLOAT_3, bUseSocket) { fVal.x = fVal.y = fVal.z = 0; }
		inline bool operator==(const float_3& val) { return fVal == val; }
		inline bool operator!=(const float_3& val) { return fVal != val; }
		inline OctaneDTOFloat3& operator=(const float_3& val) { fVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat3& obj);
		MSGPACK_DEFINE(fVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTORGB : OctaneDTOBase {
		float_3 fVal;
		OctaneDTORGB() : OctaneDTOBase("", DTO_RGB) { fVal.x = fVal.y = fVal.z = 0; }
		OctaneDTORGB(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_RGB, bUseSocket) { fVal.x = fVal.y = fVal.z = 0; }
		inline bool operator==(const float_3& val) { return fVal == val; }
		inline bool operator!=(const float_3& val) { return fVal != val; }
		inline OctaneDTORGB& operator=(const float_3& val) { fVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTORGB& obj);
		MSGPACK_DEFINE(fVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOEnum : OctaneDTOBase {
		int32_t iVal;
		OctaneDTOEnum() : OctaneDTOBase("", DTO_ENUM), iVal(0) {}
		OctaneDTOEnum(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_ENUM, bUseSocket), iVal(0) {}
		inline bool operator==(const int32_t& val) { return iVal == val; }
		inline bool operator!=(const int32_t& val) { return iVal != val; }
		inline OctaneDTOEnum& operator=(const int32_t& val) { iVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOEnum& obj);
		MSGPACK_DEFINE(iVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOInt : OctaneDTOBase {
		int32_t iVal;
		OctaneDTOInt() : OctaneDTOBase("", DTO_INT), iVal(0) {}
		OctaneDTOInt(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_INT, bUseSocket), iVal(0) {}
		inline operator int() { return iVal; }
		inline bool operator==(const int32_t& val) { return iVal == val; }
		inline bool operator!=(const int32_t& val) { return iVal != val; }
		inline OctaneDTOInt& operator=(const int32_t& val) { iVal = val;  return *this; }		
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOInt& obj);
		MSGPACK_DEFINE(iVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOInt2 : OctaneDTOBase {
		int32_2 iVal;
		OctaneDTOInt2() : OctaneDTOBase("", DTO_INT_2) { iVal.x = iVal.y = 0; }
		OctaneDTOInt2(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_INT_2, bUseSocket) { iVal.x = iVal.y = 0; }
		inline bool operator==(const int32_2& val) { return iVal == val; }
		inline bool operator!=(const int32_2& val) { return iVal != val; }
		inline OctaneDTOInt2& operator=(const int32_2& val) { iVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOInt2& obj);
		MSGPACK_DEFINE(iVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOInt3 : OctaneDTOBase {
		int32_3 iVal;
		OctaneDTOInt3() : OctaneDTOBase("", DTO_INT_3) { iVal.x = iVal.y = iVal.z = 0; }
		OctaneDTOInt3(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_INT_3, bUseSocket) { iVal.x = iVal.y = iVal.z = 0; }
		inline bool operator==(const int32_3& val) { return iVal == val; }
		inline bool operator!=(const int32_3& val) { return iVal != val; }
		inline OctaneDTOInt3& operator=(const int32_3& val) { iVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOInt3& obj);
		MSGPACK_DEFINE(iVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOString : OctaneDTOBase {
		std::string sVal;
		OctaneDTOString() : OctaneDTOBase("", DTO_STR) { sVal = ""; }
		OctaneDTOString(const std::string &name, bool bUseSocket = true) : OctaneDTOBase(name, DTO_STR, bUseSocket) { sVal = ""; }
		inline bool operator==(const std::string& val) { return sVal == val; }
		inline bool operator!=(const std::string& val) { return sVal != val; }
		inline OctaneDTOString& operator=(const std::string& val) { sVal = val;  return *this; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOString& obj);
		MSGPACK_DEFINE(sVal, MSGPACK_BASE(OctaneDTOBase));
	};

	struct OctaneDTOShader : OctaneDTOBase {		
		OctaneDTOShader() : OctaneDTOBase("", DTO_SHADER) { bUseLinked = true; }
		OctaneDTOShader(const std::string &name) : OctaneDTOBase(name, DTO_SHADER) { bUseLinked = true; }
		inline bool operator==(const std::string& val) { return sLinkNodeName == val; }
		inline bool operator!=(const std::string& val) { return sLinkNodeName != val; }
		inline OctaneDTOShader& operator=(const std::string& val) { sLinkNodeName = val;  return *this; }
		inline operator std::string() const { return sLinkNodeName; }
		friend std::ostream& operator<< (std::ostream& out, const OctaneDTOShader& obj);
		MSGPACK_DEFINE(MSGPACK_BASE(OctaneDTOBase));
	};
}

namespace OctaneDataTransferObject {
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// OctaneEngine packet type
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	enum PacketType {
		NONE = 0,
		TEST_PACKET,

		GET_OCTANEDB,
		GET_LDB_MAT_END,
		LAST_LDB_PACKET = GET_LDB_MAT_END,

		ERROR_PACKET,
		DESCRIPTION,
		SET_LIC_DATA,
    INIT_API,
		RELEASE_API,
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
		LOAD_MESH = FIRST_NAMED_PACKET,
		GET_GEO_NODES,
		DEL_GLOBAL_MESH,
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
		LOAD_TOON_MATERIAL,
		LOAD_MATEL_MATERIAL,
		LOAD_UNIVERSAL_MATERIAL,
		LOAD_SHADOW_CATCHER_MATERIAL,
		LOAD_LAYERED_MATERIAL,
		LOAD_COMPOSITE_MATERIAL,
		LOAD_GROUP_LAYER,
		LOAD_DIFFUSE_LAYER,
		LOAD_METALLIC_LAYER,
		LOAD_SHEEN_LAYER,
		LOAD_SPECULAR_LAYER,
		LOAD_MATERIAL_LAST = LOAD_SPECULAR_LAYER,
		DEL_MATERIAL,

		LOAD_TEXTURE_FIRST,
		LOAD_GRAYSCALE_COLOR_TEXTURE = LOAD_TEXTURE_FIRST,
		LOAD_RGB_SPECTRUM_TEXTURE,
		LOAD_GAUSSIAN_SPECTRUM_TEXTURE,
		LOAD_FLOAT_VERTEXATTRIBUTE_TEXTURE,
		LOAD_COLOUR_VERTEXATTRIBUTE_TEXTURE,
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
		LOAD_ADD_TEXTURE,
		LOAD_SUBTRACT_TEXTURE,
		LOAD_COMPARE_TEXTURE,
		LOAD_TRIPLANAR_TEXTURE,
		LOAD_IMAGE_TEXTURE,
		LOAD_ALPHA_IMAGE_TEXTURE,
		LOAD_FLOAT_IMAGE_TEXTURE,
		LOAD_FALLOFF_TEXTURE,
		LOAD_COLOR_CORRECT_TEXTURE,
		LOAD_DIRT_TEXTURE,
		LOAD_GRADIENT_TEXTURE,
		LOAD_VOLUMERAMP_TEXTURE,
		LOAD_DISPLACEMENT_TEXTURE,
		LOAD_VERTEX_DISPLACEMENT_TEXTURE,
		LOAD_VERTEX_DISPLACEMENT_MIXER_TEXTURE,
		LOAD_RANDOM_COLOR_TEXTURE,
		LOAD_POLYGON_SIDE_TEXTURE,
		LOAD_NOISE_TEXTURE,
		LOAD_BAKING_TEXTURE,
		LOAD_UVW_TRANSFORM_TEXTURE,
		LOAD_INSTANCE_RANGE_TEXTURE,
		LOAD_INSTANCE_COLOR_TEXTURE,
		LOAD_OSL_TEXTURE,
		LOAD_OSL_CAMERA,
		LOAD_OSL_BAKING_CAMERA,
		LOAD_OSL_GEO,
		GET_OSL_PIN_INFO,
		LOAD_TOON_RAMP_TEXTURE,
		LOAD_IMAGE_TILE_TEXTURE,
		LOAD_TEXTURE_LAST = LOAD_IMAGE_TILE_TEXTURE,
		
		DEL_TEXTURE,

		LOAD_EMISSION_FIRST,
		LOAD_BLACKBODY_EMISSION = LOAD_EMISSION_FIRST,
		LOAD_TEXTURE_EMISSION,
		LOAD_TOON_POINT_LIGHT,
		LOAD_TOON_DIRECTIONAL_LIGHT,
		LOAD_EMISSION_LAST = LOAD_TOON_DIRECTIONAL_LIGHT,
		DEL_EMISSION,

		LOAD_TRANSFORM_FIRST,
		LOAD_SCALE_TRANSFORM = LOAD_TRANSFORM_FIRST,
		LOAD_ROTATION_TRANSFORM,
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
		LOAD_PROJECTION_TRIPLANAR,
		LOAD_PROJECTION_OSL_UV,
		LOAD_OSL_PROJECTION,
		LOAD_PROJECTION_LAST = LOAD_OSL_PROJECTION,
		DEL_PROJECTION,

		LOAD_VALUE_FIRST,
		LOAD_VALUE_FLOAT = LOAD_VALUE_FIRST,
		LOAD_VALUE_INT,
		LOAD_VALUE_SUN_DIRECTION,
		LOAD_SCHLICK,
		LOAD_ROUND_EDGES,
		LOAD_VALUE_LAST = LOAD_ROUND_EDGES,
		DEL_VALUE,
		
		LOAD_LIGHT,
		DEL_LIGHT,

		LOAD_OBJECT,

		LOAD_TEXTURE_ENVIRONMENT,
		LOAD_DAYLIGHT_ENVIRONMENT,
		LOAD_PLANETARY_ENVIRONMENT,

		COMMAND,
		LOAD_RENDER_PASSES,

		LAST_NAMED_PACKET = LOAD_RENDER_PASSES,

		LAST_PACKET_TYPE = LAST_NAMED_PACKET
	}; //enum PacketType
}
MSGPACK_ADD_ENUM(OctaneDataTransferObject::PacketType);

#ifdef OCTANE_SERVER
typedef enum OctaneScenePassType {
	OCT_SCE_PASS_INVALID = 0,
	/* Beauty Passes */
	OCT_SCE_PASS_BEAUTY = (1 << 0),
	OCT_SCE_PASS_EMITTERS = (1 << 1),
	OCT_SCE_PASS_ENVIRONMENT = (1 << 2),
	OCT_SCE_PASS_DIFFUSE = (1 << 3),
	OCT_SCE_PASS_DIFFUSE_DIRECT = (1 << 4),
	OCT_SCE_PASS_DIFFUSE_INDIRECT = (1 << 5),
	OCT_SCE_PASS_DIFFUSE_FILTER = (1 << 6),
	OCT_SCE_PASS_REFLECTION = (1 << 7),
	OCT_SCE_PASS_REFLECTION_DIRECT = (1 << 8),
	OCT_SCE_PASS_REFLECTION_INDIRECT = (1 << 9),
	OCT_SCE_PASS_REFLECTION_FILTER = (1 << 10),
	OCT_SCE_PASS_REFRACTION = (1 << 11),
	OCT_SCE_PASS_REFRACTION_FILTER = (1 << 12),
	OCT_SCE_PASS_TRANSMISSION = (1 << 13),
	OCT_SCE_PASS_TRANSMISSION_FILTER = (1 << 14),
	OCT_SCE_PASS_SSS = (1 << 15),
	OCT_SCE_PASS_SHADOW = (1 << 16),
	OCT_SCE_PASS_IRRADIANCE = (1 << 17),
	OCT_SCE_PASS_LIGHT_DIRECTION = (1 << 18),
	OCT_SCE_PASS_VOLUME = (1 << 19),
	OCT_SCE_PASS_VOLUME_MASK = (1 << 20),
	OCT_SCE_PASS_VOLUME_EMISSION = (1 << 21),
	OCT_SCE_PASS_VOLUME_Z_FRONT = (1 << 22),
	OCT_SCE_PASS_VOLUME_Z_BACK = (1 << 23),
	OCT_SCE_PASS_NOISE = (1 << 24),
	/* Denoise Passes */
	OCT_SCE_PASS_DENOISER_BEAUTY = (1 << 0),
	OCT_SCE_PASS_DENOISER_DIFF_DIR = (1 << 1),
	OCT_SCE_PASS_DENOISER_DIFF_INDIR = (1 << 2),
	OCT_SCE_PASS_DENOISER_REFLECTION_DIR = (1 << 3),
	OCT_SCE_PASS_DENOISER_REFLECTION_INDIR = (1 << 4),
	OCT_SCE_PASS_DENOISER_EMISSION = (1 << 5),
	OCT_SCE_PASS_DENOISER_REMAINDER = (1 << 6),
	OCT_SCE_PASS_DENOISER_VOLUME = (1 << 7),
	OCT_SCE_PASS_DENOISER_VOLUME_EMISSION = (1 << 8),
	/* Render Postprocess Passes */
	OCT_SCE_PASS_POSTPROCESS = (1 << 0),
	/* Render Layer Passes */
	OCT_SCE_PASS_LAYER_SHADOWS = (1 << 0),
	OCT_SCE_PASS_LAYER_BLACK_SHADOW = (1 << 1),
	OCT_SCE_PASS_LAYER_REFLECTIONS = (1 << 2),
	/* Render Lighting Passes */
	OCT_SCE_PASS_AMBIENT_LIGHT = (1 << 0),
	OCT_SCE_PASS_AMBIENT_LIGHT_DIRECT = (1 << 1),
	OCT_SCE_PASS_AMBIENT_LIGHT_INDIRECT = (1 << 2),
	OCT_SCE_PASS_SUNLIGHT = (1 << 3),
	OCT_SCE_PASS_SUNLIGHT_DIRECT = (1 << 4),
	OCT_SCE_PASS_SUNLIGHT_INDIRECT = (1 << 5),
	OCT_SCE_PASS_LIGHT_PASS_1 = (1 << 6),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_1 = (1 << 7),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_1 = (1 << 8),
	OCT_SCE_PASS_LIGHT_PASS_2 = (1 << 9),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_2 = (1 << 10),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_2 = (1 << 11),
	OCT_SCE_PASS_LIGHT_PASS_3 = (1 << 12),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_3 = (1 << 13),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_3 = (1 << 14),
	OCT_SCE_PASS_LIGHT_PASS_4 = (1 << 15),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_4 = (1 << 16),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_4 = (1 << 17),
	OCT_SCE_PASS_LIGHT_PASS_5 = (1 << 18),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_5 = (1 << 19),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_5 = (1 << 20),
	OCT_SCE_PASS_LIGHT_PASS_6 = (1 << 21),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_6 = (1 << 22),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_6 = (1 << 23),
	OCT_SCE_PASS_LIGHT_PASS_7 = (1 << 24),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_7 = (1 << 25),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_7 = (1 << 26),
	OCT_SCE_PASS_LIGHT_PASS_8 = (1 << 27),
	OCT_SCE_PASS_LIGHT_DIRECT_PASS_8 = (1 << 28),
	OCT_SCE_PASS_LIGHT_INDIRECT_PASS_8 = (1 << 29),
	/* Render Cryptomatte Passes */
	OCT_SCE_PASS_CRYPTOMATTE_INSTANCE_ID = (1 << 0),
	OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME = (1 << 1),
	OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_NODE = (1 << 2),
	OCT_SCE_PASS_CRYPTOMATTE_MATERIAL_PIN_NODE = (1 << 3),
	OCT_SCE_PASS_CRYPTOMATTE_OBJECT_NODE_NAME = (1 << 4),
	OCT_SCE_PASS_CRYPTOMATTE_OBJECT_NODE = (1 << 5),
	OCT_SCE_PASS_CRYPTOMATTE_OBJECT_PIN_NODE = (1 << 6),
	/* Render Info Passes */
	OCT_SCE_PASS_GEOMETRIC_NORMAL = (1 << 0),
	OCT_SCE_PASS_SMOOTH_NORMAL = (1 << 1),
	OCT_SCE_PASS_SHADING_NORMAL = (1 << 2),
	OCT_SCE_PASS_TANGENT_NORMAL = (1 << 3),
	OCT_SCE_PASS_Z_DEPTH = (1 << 4),
	OCT_SCE_PASS_POSITION = (1 << 5),
	OCT_SCE_PASS_UV_COORDINATES = (1 << 6),
	OCT_SCE_PASS_TEXTURE_TANGENT = (1 << 7),
	OCT_SCE_PASS_MOTION_VECTOR = (1 << 8),
	OCT_SCE_PASS_MATERIAL_ID = (1 << 9),
	OCT_SCE_PASS_OBJECT_ID = (1 << 10),
	OCT_SCE_PASS_OBJECT_LAYER_COLOR = (1 << 11),
	OCT_SCE_PASS_BAKING_GROUP_ID = (1 << 12),
	OCT_SCE_PASS_LIGHT_PASS_ID = (1 << 13),
	OCT_SCE_PASS_RENDER_LAYER_ID = (1 << 14),
	OCT_SCE_PASS_RENDER_LAYER_MASK = (1 << 15),
	OCT_SCE_PASS_WIREFRAME = (1 << 16),
	OCT_SCE_PASS_AMBIENT_OCCLUSION = (1 << 17),
	/* Render Material Passes */
	OCT_SCE_PASS_OPACITY = (1 << 0),
	OCT_SCE_PASS_ROUGHNESS = (1 << 1),
	OCT_SCE_PASS_INDEX_OF_REFRACTION = (1 << 2),
	OCT_SCE_PASS_DIFFUSE_FILTER_INFO = (1 << 3),
	OCT_SCE_PASS_REFLECTION_FILTER_INFO = (1 << 4),
	OCT_SCE_PASS_REFRACTION_FILTER_INFO = (1 << 5),
	OCT_SCE_PASS_TRANSMISSION_FILTER_INFO = (1 << 6),
} OctaneScenePassType;
#endif 

inline std::string version(std::string major, std::string minor) { return major + std::string(".") + minor; }

#endif
// clang-format on
