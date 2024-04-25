// clang-format off
#ifndef __OCTANE_NODE_H__
#define __OCTANE_NODE_H__
#include "OctaneBase.h"
#include "OctanePinInfo.h"
#include "OctaneReflection.h"

#define ENVIRONMENT_NODE_NAME "Environment"
#define VISIBLE_ENVIRONMENT_NODE_NAME "VisibleEnvironment"
#define OCTANE_STATIC_FRONT_PROJECTION "OCTANE_STATIC_FRONT_PROJECTION"
#define OCTANE_BLENDER_CAMERA_MODE "OCTANE_BLENDER_CAMERA_MODE"
#define OCTANE_BLENDER_CAMERA_CENTER_X "OCTANE_BLENDER_CAMERA_CENTER_X"
#define OCTANE_BLENDER_CAMERA_CENTER_Y "OCTANE_BLENDER_CAMERA_CENTER_Y"
#define OCTANE_BLENDER_CAMERA_REGION_WIDTH "OCTANE_BLENDER_CAMERA_REGION_WIDTH"
#define OCTANE_BLENDER_CAMERA_REGION_HEIGHT "OCTANE_BLENDER_CAMERA_REGION_HEIGHT"
#define OCTANE_BLENDER_RENDER_PASS_NODE "OCTANE_BLENDER_RENDER_PASS_NODE"
#define OCTANE_BLENDER_RENDER_AOV_NODE "OCTANE_BLENDER_RENDER_AOV_NODE"
#define OCTANE_BLENDER_AOV_OUTPUT_NODE "OCTANE_BLENDER_AOV_OUTPUT_NODE"
#define OCTANE_BLENDER_KERNEL_NODE "OCTANE_BLENDER_KERNEL_NODE"
#define OCTANE_BLENDER_ANIMATION_SETTING_NODE "OCTANE_BLENDER_ANIMATION_SETTING_NODE"
#define OCTANE_BLENDER_RENDER_LAYER_NODE "OCTANE_BLENDER_RENDER_LAYER_NODE"
#define OCTANE_BLENDER_DYNAMIC_PIN_TAG "###DYNAMIC_PIN###"
#define OCTANE_BLENDER_OCTANE_PROXY_TAG "###OCTANE_PROXY###"
#define OCTANE_PASS_TAG "$OCTANE_PASS$"

namespace OctaneDataTransferObject {

	enum CommandType {
		SHOW_NODEGRAPH = 1,
		SHOW_NETWORK_PREFERENCE = 2,
		STOP_RENDERING = 3,
		SHOW_LOG = 4,
		SHOW_DEVICE_SETTINGS = 5,
		SHOW_LIVEDB = 6,
		SHOW_ACTIVATION = 7,
		SAVE_OCTANDB = 8,
		SHOW_OCTANE_VIEWPORT = 9,
		CLEAR_RESOURCE_CACHE_SYSTEM = 10,
		RESET_BLENDER_VIEWLAYER = 11,
		TOGGLE_RECORD = 10000,
		PLAY_RECORD = 10001,
	};

	enum EngineDataType {
		RESOURCE_CACHE_DATA = 0,
	};

	enum ResourceCacheSystemType {
		DISABLE_CACHE_SYSTEM = 0,
		TEXTURE_ONLY = 1,
		GEOMETRY_ONLY = 2,
		ALL_RESOURCE_APPLICABLE = 127
	};

	enum NodeResourceType {
		LIGHT = 0,
		HEAVY = 1,
		TEXTURE = 1,
		GEOMETRY = 2
	};

	enum ImageSaveMode {
		IMAGE_SAVE_MODE_SEPARATE = 0,
		IMAGE_SAVE_MODE_MULTILAYER = 1,
		IMAGE_SAVE_MODE_DEEP_EXR = 2
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// NODE BASE
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneNodeBase {
		std::string sName;
		int octaneType;
		std::string pluginType;
		static const PacketType packetType = NONE;
		void* arrayData;
		uint64_t arraySize;
		uint8_t responseNodeNum;

		OctaneNodeBase(int octaneType, std::string pluginType, uint64_t arraySize = 0, uint8_t responseNodeNum = 0) : octaneType(octaneType), pluginType(pluginType), arraySize(arraySize), responseNodeNum(responseNodeNum) {}
		virtual ~OctaneNodeBase() {}		
		virtual void PackAttributes() {}
		virtual void UnpackAttributes() {}
		virtual void VisitEach(BaseVisitor* pVisitor) {}
		virtual void UpdateOctaneDBNode(void* data) {}
#ifdef OCTANE_SERVER
		virtual bool PreUpdateNode(Octane::ApiNode* pApiNode) { return false; }
		virtual bool PostUpdateNode(Octane::ApiNode* pApiNode) { return false; }
		virtual void GenerateResponseNodes(Octane::ApiNode* pApiNode, std::vector<OctaneNodeBase*>& nodes) {}
#endif // !OCTANE_SERVER
		virtual void Serialize(msgpack::sbuffer& buf) {}
		virtual void Deserialize(msgpack::object& obj) {}
		MSGPACK_DEFINE(sName, arraySize);
	}; //struct OctaneNodeBase

	typedef std::vector<OctaneNodeBase *> OctaneNodeResponse;

#ifndef OCTANE_NODE_SERIALIZARION_FUNCTIONS
#define OCTANE_NODE_SERIALIZARION_FUNCTIONS \
	virtual void Serialize(msgpack::sbuffer& buf) { msgpack::pack(buf, *(this)); } \
	virtual void Deserialize(msgpack::object& obj) { obj.convert(*(this)); }
#endif // !OCTANE_NODE_SERIALIZARION_FUNCTIONS

#ifndef OCTANE_NODE_VISIT_FUNCTIONS
#define OCTANE_NODE_VISIT_FUNCTIONS \
	virtual void VisitEach(BaseVisitor* pVisitor) { visit_each_field_data(*(this), pVisitor); }
#endif // !OCTANE_NODE_VISIT_FUNCTIONS

#ifndef OCTANE_NODE_OCTANEDB_FUNCTIONS
#define OCTANE_NODE_OCTANEDB_FUNCTIONS \
	virtual void UpdateOctaneDBNode(void* data);
#endif // !OCTANE_NODE_OCTANEDB_FUNCTIONS

#ifndef OCTANE_NODE_PRE_UPDATE_FUNCTIONS
#ifdef OCTANE_SERVER
#define OCTANE_NODE_PRE_UPDATE_FUNCTIONS \
	virtual bool PreUpdateNode(Octane::ApiNode* pApiNode);
#else
#define OCTANE_NODE_PRE_UPDATE_FUNCTIONS
#endif
#endif

#ifndef OCTANE_NODE_POST_UPDATE_FUNCTIONS
#ifdef OCTANE_SERVER
#define OCTANE_NODE_POST_UPDATE_FUNCTIONS \
	virtual bool PostUpdateNode(Octane::ApiNode* pApiNode);
#else
#define OCTANE_NODE_POST_UPDATE_FUNCTIONS
#endif
#endif

#ifndef OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
#ifdef OCTANE_SERVER
#define OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS \
	virtual void GenerateResponseNodes(Octane::ApiNode* pApiNode, std::vector<OctaneNodeBase*>& nodes);
#else
#define OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
#endif
#endif
	struct OctaneEnvironment : public OctaneNodeBase {
		bool	bUsed;
		OctaneEnvironment(int octaneType, std::string pluginType) :
			bUsed(true), OctaneNodeBase(octaneType, pluginType)
		{
		}
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(bUsed, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneEnvironment

	struct OctaneTextureEnvironment : public OctaneEnvironment{
		REFLECTABLE
		(
		(OctaneDTORGB)		fTexture,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOBool)		bImportanceSampling,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fMediumRadius,
		(OctaneDTOBool)		bVisableEnvBackplate,
		(OctaneDTOBool)		bVisableReflections,
		(OctaneDTOBool)		bVisableRefractions
		)

		OctaneTextureEnvironment() :
			fTexture("Texture"),
			fPower("Power"),
			bImportanceSampling("Importance sampling"),
			tMedium("Medium"),
			fMediumRadius("Medium radius"),
			bVisableEnvBackplate("Visable env Backplate"),
			bVisableReflections("Visable env Reflections"),
			bVisableRefractions("Visable env Refractions"),
			OctaneEnvironment(Octane::NT_ENV_TEXTURE, "ShaderNodeOctTextureEnvironment")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, fPower, bImportanceSampling, tMedium, fMediumRadius, bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};

	struct OctaneDaylightEnvironment : public OctaneEnvironment{
		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3SunDirection,
		(OctaneDTOFloat)	fSkyTurbidity,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fNorthOffset,
		(OctaneDTOEnum)		iDaylightModel,
		(OctaneDTORGB)		fSkyColor,
		(OctaneDTORGB)		fSunsetColor,
		(OctaneDTOFloat)	fSunSize,
		(OctaneDTORGB)		fGroundColor,
		(OctaneDTOFloat)	fGroundStartAngle,
		(OctaneDTOFloat)	fGroundBlendAngle,
		(OctaneDTOShader)	tSkyTexture,
		(OctaneDTOBool)		bImportanceSampling,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fMediumRadius,
		(OctaneDTOBool)		bVisableEnvBackplate,
		(OctaneDTOBool)		bVisableReflections,
		(OctaneDTOBool)		bVisableRefractions
		)

		OctaneDaylightEnvironment() :
			f3SunDirection("Sun direction"),
			fSkyTurbidity("Sky turbidity"),
			fPower("Power"),
			fNorthOffset("North offset"),
			iDaylightModel("daylight_model_type", false),
			fSkyColor("Sky color"),
			fSunsetColor("Sunset color"),
			fSunSize("Sun size"),
			fGroundColor("Ground color"),
			fGroundStartAngle("Ground start angle"),
			fGroundBlendAngle("Ground blend angle"),
			tSkyTexture("Sky texture"),
			bImportanceSampling("Importance sampling"),
			tMedium("Medium"),
			fMediumRadius("Medium radius"),
			bVisableEnvBackplate("Visable env Backplate"),
			bVisableReflections("Visable env Reflections"),
			bVisableRefractions("Visable env Refractions"),
			OctaneEnvironment(Octane::NT_ENV_DAYLIGHT, "ShaderNodeOctDaylightEnvironment")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3SunDirection, fSkyTurbidity, fPower, fNorthOffset, iDaylightModel,
			fSkyColor, fSunsetColor, fSunSize, fGroundColor, fGroundStartAngle, fGroundBlendAngle, tSkyTexture,
			bImportanceSampling, tMedium, fMediumRadius, bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};

	struct OctanePlanetaryEnvironment : public OctaneEnvironment{
		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3SunDirection,
		(OctaneDTOFloat)	fSkyTurbidity,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fSunIntensity,
		(OctaneDTOFloat)	fNorthOffset,
		(OctaneDTOFloat)	fSunSize,
		(OctaneDTOFloat)	fAltitude,
		(OctaneDTOShader)	tStarField,
		(OctaneDTOBool)		bImportanceSampling,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fMediumRadius,
		(OctaneDTOFloat)	fLatitude,
		(OctaneDTOFloat)	fLongtitude,
		(OctaneDTORGB)		fGroundAlbedo,
		(OctaneDTOShader)	tGroundReflection,
		(OctaneDTOShader)	tGroundGlossiness,
		(OctaneDTORGB)		fGroundEmission,
		(OctaneDTOShader)	tGroundNormalMap,
		(OctaneDTOShader)	tGroundElevation,
		(OctaneDTOBool)		bVisableEnvBackplate,
		(OctaneDTOBool)		bVisableReflections,
		(OctaneDTOBool)		bVisableRefractions
		)

		OctanePlanetaryEnvironment() :
			f3SunDirection("Sun direction"),
			fSkyTurbidity("Sky turbidity"),
			fPower("Power"),
			fSunIntensity("Sun intensity"),
			fNorthOffset("North offset"),
			fSunSize("Sun size"),
			fAltitude("Altitude"),
			tStarField("Star field"),
			bImportanceSampling("Importance sampling"),
			tMedium("Medium"),
			fMediumRadius("Medium radius"),
			fLatitude("Latitude"),
			fLongtitude("Longtitude"),
			fGroundAlbedo("Ground albedo"),
			tGroundReflection("Ground reflection"),
			tGroundGlossiness("Ground glossiness"),
			fGroundEmission("Ground emission"),
			tGroundNormalMap("Ground normal map"),
			tGroundElevation("Ground elevation"),
			bVisableEnvBackplate("Visable env Backplate"),
			bVisableReflections("Visable env Reflections"),
			bVisableRefractions("Visable env Refractions"),
			OctaneEnvironment(Octane::NT_ENV_PLANETARY, "ShaderNodeOctPlanetaryEnvironment")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3SunDirection, fSkyTurbidity, fPower, fSunIntensity, fNorthOffset,
			fSunSize, fAltitude, fAltitude, tStarField,
			bImportanceSampling, tMedium, fMediumRadius,
			fLatitude, fLongtitude, fGroundAlbedo, tGroundReflection, tGroundGlossiness, fGroundEmission, tGroundNormalMap, tGroundElevation,
			bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};

	struct OctaneGeoNode : public OctaneNodeBase {
		std::string     sGeoName;

		OctaneGeoNode() : OctaneNodeBase(Octane::ENT_OCTANE_GEO_NODE, "OctaneGeoNode") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		MSGPACK_DEFINE(sGeoName, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolObjects : public OctaneNodeBase {
        REFLECTABLE
        (
		(OctaneDTOShader)	sScatteredObject1,
		(OctaneDTOShader)	sScatteredObject2,
		(OctaneDTOShader)	sScatteredObject3,
		(OctaneDTOShader)	sScatteredObject4,
		(OctaneDTOEnum)		iObjectSelectionMethod,
		(OctaneDTOInt)		iObjectSelectionSeed,
		(OctaneDTOShader)	sObjectSelectionMap
		)

		OctaneScatterToolObjects() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sScatteredObject1, sScatteredObject2, sScatteredObject3, sScatteredObject4,
			iObjectSelectionMethod, iObjectSelectionSeed, sObjectSelectionMap, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneScatterToolGrid : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOInt3)		i3Dimension,
		(OctaneDTOFloat3)	f3Offset
		)

		OctaneScatterToolGrid() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(i3Dimension, f3Offset, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolShape : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iShape,
		(OctaneDTOShader)	sCullingMap,
		(OctaneDTOFloat)	fCullingMin,
		(OctaneDTOFloat)	fCullingMax
		)

		OctaneScatterToolShape() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iShape, sCullingMap, fCullingMin, fCullingMax, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolDistribution : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iDistributionOnSurface,
		(OctaneDTOEnum)		iDistributionOnParticles,
		(OctaneDTOEnum)		iDistributionOnHairs,
		(OctaneDTOFloat)	fPositionOnEdge,
		(OctaneDTOFloat)	fSpacingOnEdges,
		(OctaneDTOBool)		bPoissonDiskSampling,
		(OctaneDTOFloat)	fPositionOnHair,
		(OctaneDTOFloat)	fSpacingOnHairs,
		(OctaneDTOShader)	sRelativeDensityMap,
		(OctaneDTOInt)		iSeed
		)

		OctaneScatterToolDistribution() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iDistributionOnSurface, iDistributionOnParticles, iDistributionOnHairs, 
			fPositionOnEdge, fSpacingOnEdges, bPoissonDiskSampling, fPositionOnHair, fSpacingOnHairs,
			sRelativeDensityMap, iSeed, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolDensity : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOInt)		iInstances,
		(OctaneDTOShader)	sCullingMap,
		(OctaneDTOFloat)	fCullingMin,
		(OctaneDTOFloat)	fCullingMax,
		(OctaneDTOFloat)	fCullingAngleLow,
		(OctaneDTOFloat)	fCullingAngleHigh
		)

		OctaneScatterToolDensity() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iInstances, sCullingMap, fCullingMin, fCullingMax, fCullingAngleLow, fCullingAngleHigh, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolInstanceOrientation : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOBool)		bSmoothNormals,
		(OctaneDTOFloat)	fNormalAlign,
		(OctaneDTOFloat)	fFrontAlign,
		(OctaneDTOEnum)		iOrientationPriority,
		(OctaneDTOEnum)		iUpDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceUpDirection,
		(OctaneDTOFloat3)	f3ReferenceUpPoint,
		(OctaneDTOEnum)		iFrontDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceFrontDirection,
		(OctaneDTOFloat3)	f3ReferenceFrontPoint
		)

		OctaneScatterToolInstanceOrientation() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bSmoothNormals, fNormalAlign, fFrontAlign, iOrientationPriority,
			iUpDirectionMode, f3ReferenceUpDirection, f3ReferenceUpPoint, 
			iFrontDirectionMode, f3ReferenceFrontDirection, f3ReferenceFrontPoint,
			MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolInstanceTransform : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iRotationMode,
		(OctaneDTOFloat3)	f3RotationMin,
		(OctaneDTOFloat3)	f3RotationMax,
		(OctaneDTOFloat)	fRotationStep,
		(OctaneDTOShader)	sRotationMap,
		(OctaneDTOEnum)		iScaleMode,
		(OctaneDTOFloat3)	f3ScaleMin,
		(OctaneDTOFloat3)	f3ScaleMax,
		(OctaneDTOFloat)	fScaleStep,
		(OctaneDTOShader)	sScaleMap,
		(OctaneDTOEnum)		iTranslationMode,
		(OctaneDTOFloat3)	f3TranslationMin,
		(OctaneDTOFloat3)	f3TranslationMax,
		(OctaneDTOFloat)	fTranslationStep,
		(OctaneDTOShader)	sTranslationMap
		)

		OctaneScatterToolInstanceTransform() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iRotationMode, f3RotationMin, f3RotationMax, fRotationStep, sRotationMap,
			iScaleMode, f3ScaleMin, f3ScaleMax, fScaleStep, sScaleMap,
			iTranslationMode, f3TranslationMin, f3TranslationMax, fTranslationStep, sTranslationMap,
			MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatterToolSurface : public OctaneNodeBase {
		REFLECTABLE
		(				
		// Geometry
		(OctaneDTOShader)	sSurface,
		// Objects
		(OctaneDTOShader)	sScatteredObject1,
		(OctaneDTOShader)	sScatteredObject2,
		(OctaneDTOShader)	sScatteredObject3,
		(OctaneDTOShader)	sScatteredObject4,
		(OctaneDTOEnum)		iObjectSelectionMethod,
		(OctaneDTOInt)		iObjectSelectionSeed,
		(OctaneDTOShader)	sObjectSelectionMap,
		// Distribution
		(OctaneDTOEnum)		iDistributionOnSurface,
		(OctaneDTOEnum)		iDistributionOnParticles,
		(OctaneDTOEnum)		iDistributionOnHairs,
		(OctaneDTOFloat)	fPositionOnEdge,
		(OctaneDTOFloat)	fSpacingOnEdges,
		(OctaneDTOBool)		bPoissonDiskSampling,
		(OctaneDTOFloat)	fPositionOnHair,
		(OctaneDTOFloat)	fSpacingOnHairs,
		(OctaneDTOShader)	sRelativeDensityMap,
		(OctaneDTOInt)		iSeed,
		// Density
		(OctaneDTOInt)		iInstances,
		(OctaneDTOShader)	sCullingMap,
		(OctaneDTOFloat)	fCullingMin,
		(OctaneDTOFloat)	fCullingMax,
		(OctaneDTOFloat)	fCullingAngleLow,
		(OctaneDTOFloat)	fCullingAngleHigh,
		// Instance orientation
		(OctaneDTOBool)		bSmoothNormals,
		(OctaneDTOFloat)	fNormalAlign,
		(OctaneDTOFloat)	fFrontAlign,
		(OctaneDTOEnum)		iOrientationPriority,
		(OctaneDTOEnum)		iUpDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceUpDirection,
		(OctaneDTOFloat3)	f3ReferenceUpPoint,
		(OctaneDTOEnum)		iFrontDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceFrontDirection,
		(OctaneDTOFloat3)	f3ReferenceFrontPoint,
		// Instance transform
		(OctaneDTOEnum)		iRotationMode,
		(OctaneDTOFloat3)	f3RotationMin,
		(OctaneDTOFloat3)	f3RotationMax,
		(OctaneDTOFloat)	fRotationStep,
		(OctaneDTOShader)	sRotationMap,
		(OctaneDTOEnum)		iScaleMode,
		(OctaneDTOFloat3)	f3ScaleMin,
		(OctaneDTOFloat3)	f3ScaleMax,
		(OctaneDTOFloat)	fScaleStep,
		(OctaneDTOShader)	sScaleMap,
		(OctaneDTOEnum)		iTranslationMode,
		(OctaneDTOFloat3)	f3TranslationMin,
		(OctaneDTOFloat3)	f3TranslationMax,
		(OctaneDTOFloat)	fTranslationStep,
		(OctaneDTOShader)	sTranslationMap
		)
		OctaneScatterToolObjects oOctaneScatterToolObjects;
		OctaneScatterToolDistribution oOctaneScatterToolDistribution;
		OctaneScatterToolDensity oOctaneScatterToolDensity;
		OctaneScatterToolInstanceOrientation oOctaneScatterToolInstanceOrientation;
		OctaneScatterToolInstanceTransform oOctaneScatterToolInstanceTransform;

		OctaneScatterToolSurface() :
			// Geometry
			sSurface("Surface"),
			// Objects
			sScatteredObject1("Scattered object 1"),
			sScatteredObject2("Scattered object 2"),
			sScatteredObject3("Scattered object 3"),
			sScatteredObject4("Scattered object 4"),
			iObjectSelectionMethod("object_selection_method", false),
			iObjectSelectionSeed("Object selection seed"),
			sObjectSelectionMap("Object selection map"),
			// Distribution
			iDistributionOnSurface("distribution_method", false),
			iDistributionOnParticles("distribution_on_particles_method", false),
			iDistributionOnHairs("distribution_on_hairs_method", false),
			fPositionOnEdge("Position on edge"),
			fSpacingOnEdges("Spacing on edges"),
			bPoissonDiskSampling("Poisson disk sampling"),
			fPositionOnHair("Position on hair"),
			fSpacingOnHairs("Spacing on hairs"),
			sRelativeDensityMap("Relative density map"),
			iSeed("Seed"),
			// Density
			iInstances("Instances"),
			sCullingMap("Culling map"),
			fCullingMin("Culling min"),
			fCullingMax("Culling max"),
			fCullingAngleLow("Culling angle low"),
			fCullingAngleHigh("Culling angle high"),
			// Instance orientation
			bSmoothNormals("Smooth normals"),
			fNormalAlign("Normal align"),
			fFrontAlign("Front align"),
			iOrientationPriority("orientation_priority", false),
			iUpDirectionMode("up_direction_mode", false),
			f3ReferenceUpDirection("Reference up direction"),
			f3ReferenceUpPoint("Reference up point"),
			iFrontDirectionMode("front_direction_mode", false),
			f3ReferenceFrontDirection("Reference front direction"),
			f3ReferenceFrontPoint("Reference front point"),
			// Instance transform
			iRotationMode("rotation_mode", false),
			f3RotationMin("Rotation min"),
			f3RotationMax("Rotation max"),
			fRotationStep("Rotation step"),
			sRotationMap("Rotation map"),
			iScaleMode("scale_mode", false),
			f3ScaleMin("Scale min"),
			f3ScaleMax("Scale max"),
			fScaleStep("Scale step"),
			sScaleMap("Scale map"),
			iTranslationMode("translation_mode", false),
			f3TranslationMin("Translation min"),
			f3TranslationMax("Translation max"),
			fTranslationStep("Translation step"),
			sTranslationMap("Translation map"),
			OctaneNodeBase(Octane::NT_SCATTER_SURFACE, "ShaderNodeOctScatterToolSurface")
		{
		}

		void PackAttributes() {
			oOctaneScatterToolObjects.sScatteredObject1 = sScatteredObject1;
			oOctaneScatterToolObjects.sScatteredObject2 = sScatteredObject2;
			oOctaneScatterToolObjects.sScatteredObject3 = sScatteredObject3;
			oOctaneScatterToolObjects.sScatteredObject4 = sScatteredObject4;
			oOctaneScatterToolObjects.iObjectSelectionMethod = iObjectSelectionMethod;
			oOctaneScatterToolObjects.iObjectSelectionSeed = iObjectSelectionSeed;
			oOctaneScatterToolObjects.sObjectSelectionMap = sObjectSelectionMap;

			oOctaneScatterToolDistribution.iDistributionOnSurface = iDistributionOnSurface;
			oOctaneScatterToolDistribution.iDistributionOnParticles = iDistributionOnParticles;
			oOctaneScatterToolDistribution.iDistributionOnHairs = iDistributionOnHairs;
			oOctaneScatterToolDistribution.fPositionOnEdge = fPositionOnEdge;
			oOctaneScatterToolDistribution.fSpacingOnEdges = fSpacingOnEdges;
			oOctaneScatterToolDistribution.bPoissonDiskSampling = bPoissonDiskSampling;
			oOctaneScatterToolDistribution.fPositionOnHair = fPositionOnHair;
			oOctaneScatterToolDistribution.fSpacingOnHairs = fSpacingOnHairs;
			oOctaneScatterToolDistribution.sRelativeDensityMap = sRelativeDensityMap;
			oOctaneScatterToolDistribution.iSeed = iSeed;

			oOctaneScatterToolDensity.iInstances = iInstances;
			oOctaneScatterToolDensity.sCullingMap = sCullingMap;
			oOctaneScatterToolDensity.fCullingMin = fCullingMin;
			oOctaneScatterToolDensity.fCullingMax = fCullingMax;
			oOctaneScatterToolDensity.fCullingAngleLow = fCullingAngleLow;
			oOctaneScatterToolDensity.fCullingAngleHigh = fCullingAngleHigh;

			oOctaneScatterToolInstanceOrientation.bSmoothNormals = bSmoothNormals;
			oOctaneScatterToolInstanceOrientation.fNormalAlign = fNormalAlign;
			oOctaneScatterToolInstanceOrientation.fFrontAlign = fFrontAlign;
			oOctaneScatterToolInstanceOrientation.iOrientationPriority = iOrientationPriority;
			oOctaneScatterToolInstanceOrientation.iUpDirectionMode = iUpDirectionMode;
			oOctaneScatterToolInstanceOrientation.f3ReferenceUpDirection = f3ReferenceUpDirection;
			oOctaneScatterToolInstanceOrientation.f3ReferenceUpPoint = f3ReferenceUpPoint;
			oOctaneScatterToolInstanceOrientation.iFrontDirectionMode = iFrontDirectionMode;
			oOctaneScatterToolInstanceOrientation.f3ReferenceFrontDirection = f3ReferenceFrontDirection;
			oOctaneScatterToolInstanceOrientation.f3ReferenceFrontPoint = f3ReferenceFrontPoint;

			oOctaneScatterToolInstanceTransform.iRotationMode = iRotationMode;
			oOctaneScatterToolInstanceTransform.f3RotationMin = f3RotationMin;
			oOctaneScatterToolInstanceTransform.f3RotationMax = f3RotationMax;
			oOctaneScatterToolInstanceTransform.fRotationStep = fRotationStep;
			oOctaneScatterToolInstanceTransform.sRotationMap = sRotationMap;
			oOctaneScatterToolInstanceTransform.iScaleMode = iScaleMode;
			oOctaneScatterToolInstanceTransform.f3ScaleMin = f3ScaleMin;
			oOctaneScatterToolInstanceTransform.f3ScaleMax = f3ScaleMax;
			oOctaneScatterToolInstanceTransform.fScaleStep = fScaleStep;
			oOctaneScatterToolInstanceTransform.sScaleMap = sScaleMap;
			oOctaneScatterToolInstanceTransform.iTranslationMode = iTranslationMode;
			oOctaneScatterToolInstanceTransform.f3TranslationMin = f3TranslationMin;
			oOctaneScatterToolInstanceTransform.f3TranslationMax = f3TranslationMax;
			oOctaneScatterToolInstanceTransform.fTranslationStep = fTranslationStep;
			oOctaneScatterToolInstanceTransform.sTranslationMap = sTranslationMap;
		}
		void UnpackAttributes() {
			sScatteredObject1 = oOctaneScatterToolObjects.sScatteredObject1;
			sScatteredObject2 = oOctaneScatterToolObjects.sScatteredObject2;
			sScatteredObject3 = oOctaneScatterToolObjects.sScatteredObject3;
			sScatteredObject4 = oOctaneScatterToolObjects.sScatteredObject4;
			iObjectSelectionMethod = oOctaneScatterToolObjects.iObjectSelectionMethod;
			iObjectSelectionSeed = oOctaneScatterToolObjects.iObjectSelectionSeed;
			sObjectSelectionMap = oOctaneScatterToolObjects.sObjectSelectionMap;

			iDistributionOnSurface = oOctaneScatterToolDistribution.iDistributionOnSurface;
			iDistributionOnParticles = oOctaneScatterToolDistribution.iDistributionOnParticles;
			iDistributionOnHairs = oOctaneScatterToolDistribution.iDistributionOnHairs;
			fPositionOnEdge = oOctaneScatterToolDistribution.fPositionOnEdge;
			fSpacingOnEdges = oOctaneScatterToolDistribution.fSpacingOnEdges;
			bPoissonDiskSampling = oOctaneScatterToolDistribution.bPoissonDiskSampling;
			fPositionOnHair = oOctaneScatterToolDistribution.fPositionOnHair;
			fSpacingOnHairs = oOctaneScatterToolDistribution.fSpacingOnHairs;
			sRelativeDensityMap = oOctaneScatterToolDistribution.sRelativeDensityMap;
			iSeed = oOctaneScatterToolDistribution.iSeed;

			iInstances = oOctaneScatterToolDensity.iInstances;
			sCullingMap = oOctaneScatterToolDensity.sCullingMap;
			fCullingMin = oOctaneScatterToolDensity.fCullingMin;
			fCullingMax = oOctaneScatterToolDensity.fCullingMax;
			fCullingAngleLow = oOctaneScatterToolDensity.fCullingAngleLow;
			fCullingAngleHigh = oOctaneScatterToolDensity.fCullingAngleHigh;

			bSmoothNormals = oOctaneScatterToolInstanceOrientation.bSmoothNormals;
			fNormalAlign = oOctaneScatterToolInstanceOrientation.fNormalAlign;
			fFrontAlign = oOctaneScatterToolInstanceOrientation.fFrontAlign;
			iOrientationPriority = oOctaneScatterToolInstanceOrientation.iOrientationPriority;
			iUpDirectionMode = oOctaneScatterToolInstanceOrientation.iUpDirectionMode;
			f3ReferenceUpDirection = oOctaneScatterToolInstanceOrientation.f3ReferenceUpDirection;
			f3ReferenceUpPoint = oOctaneScatterToolInstanceOrientation.f3ReferenceUpPoint;
			iFrontDirectionMode = oOctaneScatterToolInstanceOrientation.iFrontDirectionMode;
			f3ReferenceFrontDirection = oOctaneScatterToolInstanceOrientation.f3ReferenceFrontDirection;
			f3ReferenceFrontPoint = oOctaneScatterToolInstanceOrientation.f3ReferenceFrontPoint;

			iRotationMode = oOctaneScatterToolInstanceTransform.iRotationMode;
			f3RotationMin = oOctaneScatterToolInstanceTransform.f3RotationMin;
			f3RotationMax = oOctaneScatterToolInstanceTransform.f3RotationMax;
			fRotationStep = oOctaneScatterToolInstanceTransform.fRotationStep;
			sRotationMap = oOctaneScatterToolInstanceTransform.sRotationMap;
			iScaleMode = oOctaneScatterToolInstanceTransform.iScaleMode;
			f3ScaleMin = oOctaneScatterToolInstanceTransform.f3ScaleMin;
			f3ScaleMax = oOctaneScatterToolInstanceTransform.f3ScaleMax;
			fScaleStep = oOctaneScatterToolInstanceTransform.fScaleStep;
			sScaleMap = oOctaneScatterToolInstanceTransform.sScaleMap;
			iTranslationMode = oOctaneScatterToolInstanceTransform.iTranslationMode;
			f3TranslationMin = oOctaneScatterToolInstanceTransform.f3TranslationMin;
			f3TranslationMax = oOctaneScatterToolInstanceTransform.f3TranslationMax;
			fTranslationStep = oOctaneScatterToolInstanceTransform.fTranslationStep;
			sTranslationMap = oOctaneScatterToolInstanceTransform.sTranslationMap;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sSurface, 
			oOctaneScatterToolObjects,
			oOctaneScatterToolDistribution,
			oOctaneScatterToolDensity, 
			oOctaneScatterToolInstanceOrientation,
			oOctaneScatterToolInstanceTransform, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneScatterToolSurface

	struct OctaneScatterToolVolume : public OctaneNodeBase {
		REFLECTABLE
		(				
		// Objects
		(OctaneDTOShader)	sScatteredObject1,
		(OctaneDTOShader)	sScatteredObject2,
		(OctaneDTOShader)	sScatteredObject3,
		(OctaneDTOShader)	sScatteredObject4,
		(OctaneDTOEnum)		iObjectSelectionMethod,
		(OctaneDTOInt)		iObjectSelectionSeed,
		(OctaneDTOShader)	sObjectSelectionMap,
		// Grid
		(OctaneDTOInt3)		i3Dimension,
		(OctaneDTOInt)		iDimensionX,
		(OctaneDTOInt)		iDimensionY,
		(OctaneDTOInt)		iDimensionZ,
		(OctaneDTOFloat3)	f3Offset,
		// Shape
		(OctaneDTOEnum)		iShape,
		(OctaneDTOShader)	sCullingMap,
		(OctaneDTOFloat)	fCullingMin,
		(OctaneDTOFloat)	fCullingMax,
		// Instance orientation
		(OctaneDTOEnum)		iOrientationPriority,
		(OctaneDTOEnum)		iUpDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceUpDirection,
		(OctaneDTOFloat3)	f3ReferenceUpPoint,
		(OctaneDTOEnum)		iFrontDirectionMode,
		(OctaneDTOFloat3)	f3ReferenceFrontDirection,
		(OctaneDTOFloat3)	f3ReferenceFrontPoint,
		// Instance transform
		(OctaneDTOEnum)		iRotationMode,
		(OctaneDTOFloat3)	f3RotationMin,
		(OctaneDTOFloat3)	f3RotationMax,
		(OctaneDTOFloat)	fRotationStep,
		(OctaneDTOShader)	sRotationMap,
		(OctaneDTOEnum)		iScaleMode,
		(OctaneDTOFloat3)	f3ScaleMin,
		(OctaneDTOFloat3)	f3ScaleMax,
		(OctaneDTOFloat)	fScaleStep,
		(OctaneDTOShader)	sScaleMap,
		(OctaneDTOEnum)		iTranslationMode,
		(OctaneDTOFloat3)	f3TranslationMin,
		(OctaneDTOFloat3)	f3TranslationMax,
		(OctaneDTOFloat)	fTranslationStep,
		(OctaneDTOShader)	sTranslationMap
		)
		OctaneScatterToolObjects oOctaneScatterToolObjects;
		OctaneScatterToolGrid oOctaneScatterToolGrid;
		OctaneScatterToolShape oOctaneScatterToolShape;
		OctaneScatterToolInstanceOrientation oOctaneScatterToolInstanceOrientation;
		OctaneScatterToolInstanceTransform oOctaneScatterToolInstanceTransform;

		OctaneScatterToolVolume() :
			// Objects
			sScatteredObject1("Scattered object 1"),
			sScatteredObject2("Scattered object 2"),
			sScatteredObject3("Scattered object 3"),
			sScatteredObject4("Scattered object 4"),
			iObjectSelectionMethod("object_selection_method", false),
			iObjectSelectionSeed("Object selection seed"),
			sObjectSelectionMap("Object selection map"),
			// Grid
			i3Dimension("Dimension"),
			iDimensionX("DimensionX"),
			iDimensionY("DimensionY"),
			iDimensionZ("DimensionZ"),
			f3Offset("Offsets"),
			// Shape
			iShape("shape", false),
			sCullingMap("Culling map"),
			fCullingMin("Culling min"),
			fCullingMax("Culling max"),
			// Instance orientation
			iOrientationPriority("orientation_priority", false),
			iUpDirectionMode("up_direction_mode", false),
			f3ReferenceUpDirection("Reference up direction"),
			f3ReferenceUpPoint("Reference up point"),
			iFrontDirectionMode("front_direction_mode", false),
			f3ReferenceFrontDirection("Reference front direction"),
			f3ReferenceFrontPoint("Reference front point"),
			// Instance transform
			iRotationMode("rotation_mode", false),
			f3RotationMin("Rotation min"),
			f3RotationMax("Rotation max"),
			fRotationStep("Rotation step"),
			sRotationMap("Rotation map"),
			iScaleMode("scale_mode", false),
			f3ScaleMin("Scale min"),
			f3ScaleMax("Scale max"),
			fScaleStep("Scale step"),
			sScaleMap("Scale map"),
			iTranslationMode("translation_mode", false),
			f3TranslationMin("Translation min"),
			f3TranslationMax("Translation max"),
			fTranslationStep("Translation step"),
			sTranslationMap("Translation map"),
			OctaneNodeBase(Octane::NT_SCATTER_VOLUME, "ShaderNodeOctScatterToolVolume")
		{
		}

		void PackAttributes() {
			oOctaneScatterToolObjects.sScatteredObject1 = sScatteredObject1;
			oOctaneScatterToolObjects.sScatteredObject2 = sScatteredObject2;
			oOctaneScatterToolObjects.sScatteredObject3 = sScatteredObject3;
			oOctaneScatterToolObjects.sScatteredObject4 = sScatteredObject4;
			oOctaneScatterToolObjects.iObjectSelectionMethod = iObjectSelectionMethod;
			oOctaneScatterToolObjects.iObjectSelectionSeed = iObjectSelectionSeed;
			oOctaneScatterToolObjects.sObjectSelectionMap = sObjectSelectionMap;

			i3Dimension.iVal.x = iDimensionX.iVal;
			i3Dimension.iVal.y = iDimensionY.iVal;
			i3Dimension.iVal.z = iDimensionZ.iVal;
			oOctaneScatterToolGrid.i3Dimension = i3Dimension;
			oOctaneScatterToolGrid.f3Offset = f3Offset;

			oOctaneScatterToolShape.iShape = iShape;
			oOctaneScatterToolShape.sCullingMap = sCullingMap;
			oOctaneScatterToolShape.fCullingMin = fCullingMin;
			oOctaneScatterToolShape.fCullingMax = fCullingMax;

			oOctaneScatterToolInstanceOrientation.iOrientationPriority = iOrientationPriority;
			oOctaneScatterToolInstanceOrientation.iUpDirectionMode = iUpDirectionMode;
			oOctaneScatterToolInstanceOrientation.f3ReferenceUpDirection = f3ReferenceUpDirection;
			oOctaneScatterToolInstanceOrientation.f3ReferenceUpPoint = f3ReferenceUpPoint;
			oOctaneScatterToolInstanceOrientation.iFrontDirectionMode = iFrontDirectionMode;
			oOctaneScatterToolInstanceOrientation.f3ReferenceFrontDirection = f3ReferenceFrontDirection;
			oOctaneScatterToolInstanceOrientation.f3ReferenceFrontPoint = f3ReferenceFrontPoint;

			oOctaneScatterToolInstanceTransform.iRotationMode = iRotationMode;
			oOctaneScatterToolInstanceTransform.f3RotationMin = f3RotationMin;
			oOctaneScatterToolInstanceTransform.f3RotationMax = f3RotationMax;
			oOctaneScatterToolInstanceTransform.fRotationStep = fRotationStep;
			oOctaneScatterToolInstanceTransform.sRotationMap = sRotationMap;
			oOctaneScatterToolInstanceTransform.iScaleMode = iScaleMode;
			oOctaneScatterToolInstanceTransform.f3ScaleMin = f3ScaleMin;
			oOctaneScatterToolInstanceTransform.f3ScaleMax = f3ScaleMax;
			oOctaneScatterToolInstanceTransform.fScaleStep = fScaleStep;
			oOctaneScatterToolInstanceTransform.sScaleMap = sScaleMap;
			oOctaneScatterToolInstanceTransform.iTranslationMode = iTranslationMode;
			oOctaneScatterToolInstanceTransform.f3TranslationMin = f3TranslationMin;
			oOctaneScatterToolInstanceTransform.f3TranslationMax = f3TranslationMax;
			oOctaneScatterToolInstanceTransform.fTranslationStep = fTranslationStep;
			oOctaneScatterToolInstanceTransform.sTranslationMap = sTranslationMap;
		}
		void UnpackAttributes() {
			sScatteredObject1 = oOctaneScatterToolObjects.sScatteredObject1;
			sScatteredObject2 = oOctaneScatterToolObjects.sScatteredObject2;
			sScatteredObject3 = oOctaneScatterToolObjects.sScatteredObject3;
			sScatteredObject4 = oOctaneScatterToolObjects.sScatteredObject4;
			iObjectSelectionMethod = oOctaneScatterToolObjects.iObjectSelectionMethod;
			iObjectSelectionSeed = oOctaneScatterToolObjects.iObjectSelectionSeed;
			sObjectSelectionMap = oOctaneScatterToolObjects.sObjectSelectionMap;
			
			i3Dimension = oOctaneScatterToolGrid.i3Dimension;
			iDimensionX.iVal = i3Dimension.iVal.x;
			iDimensionY.iVal = i3Dimension.iVal.y;
			iDimensionZ.iVal = i3Dimension.iVal.z;
			f3Offset = oOctaneScatterToolGrid.f3Offset;

			iShape = oOctaneScatterToolShape.iShape;
			sCullingMap = oOctaneScatterToolShape.sCullingMap;
			fCullingMin = oOctaneScatterToolShape.fCullingMin;
			fCullingMax = oOctaneScatterToolShape.fCullingMax;

			iOrientationPriority = oOctaneScatterToolInstanceOrientation.iOrientationPriority;
			iUpDirectionMode = oOctaneScatterToolInstanceOrientation.iUpDirectionMode;
			f3ReferenceUpDirection = oOctaneScatterToolInstanceOrientation.f3ReferenceUpDirection;
			f3ReferenceUpPoint = oOctaneScatterToolInstanceOrientation.f3ReferenceUpPoint;
			iFrontDirectionMode = oOctaneScatterToolInstanceOrientation.iFrontDirectionMode;
			f3ReferenceFrontDirection = oOctaneScatterToolInstanceOrientation.f3ReferenceFrontDirection;
			f3ReferenceFrontPoint = oOctaneScatterToolInstanceOrientation.f3ReferenceFrontPoint;

			iRotationMode = oOctaneScatterToolInstanceTransform.iRotationMode;
			f3RotationMin = oOctaneScatterToolInstanceTransform.f3RotationMin;
			f3RotationMax = oOctaneScatterToolInstanceTransform.f3RotationMax;
			fRotationStep = oOctaneScatterToolInstanceTransform.fRotationStep;
			sRotationMap = oOctaneScatterToolInstanceTransform.sRotationMap;
			iScaleMode = oOctaneScatterToolInstanceTransform.iScaleMode;
			f3ScaleMin = oOctaneScatterToolInstanceTransform.f3ScaleMin;
			f3ScaleMax = oOctaneScatterToolInstanceTransform.f3ScaleMax;
			fScaleStep = oOctaneScatterToolInstanceTransform.fScaleStep;
			sScaleMap = oOctaneScatterToolInstanceTransform.sScaleMap;
			iTranslationMode = oOctaneScatterToolInstanceTransform.iTranslationMode;
			f3TranslationMin = oOctaneScatterToolInstanceTransform.f3TranslationMin;
			f3TranslationMax = oOctaneScatterToolInstanceTransform.f3TranslationMax;
			fTranslationStep = oOctaneScatterToolInstanceTransform.fTranslationStep;
			sTranslationMap = oOctaneScatterToolInstanceTransform.sTranslationMap;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(oOctaneScatterToolObjects,
			oOctaneScatterToolGrid,
			oOctaneScatterToolShape, 
			oOctaneScatterToolInstanceOrientation,
			oOctaneScatterToolInstanceTransform, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneScatterToolVolume

	struct OctaneCameraPosition : public OctaneNodeBase {
        REFLECTABLE
        (
		(OctaneDTOFloat3)	f3Position,
		(OctaneDTOFloat3)	f3Target,
		(OctaneDTOFloat3)	f3Up,
		(OctaneDTOBool)		bKeepUpright
        )
		std::vector<float>	 oMotionPositions;
		std::vector<float>	 oMotionTargets;
		std::vector<float>	 oMotionUps;
		std::vector<float>	 oMotionFOVs;

		OctaneCameraPosition() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3Position, f3Target, f3Up, bKeepUpright, 
			oMotionPositions, oMotionTargets, oMotionUps, oMotionFOVs, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneCameraDistortion : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOBool)		bUseDistortionTexture,
		(OctaneDTOShader)	sDistortionTexture,
		(OctaneDTOFloat)	fSphereDistortion,
		(OctaneDTOFloat)	fBarrelDistortion,
		(OctaneDTOFloat)	fBarrelDistortionCorners
		)

		OctaneCameraDistortion() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bUseDistortionTexture, sDistortionTexture, fSphereDistortion, fBarrelDistortion, fBarrelDistortionCorners, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCameraAberration : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fSphereAberration,
		(OctaneDTOFloat)	fComa,
		(OctaneDTOFloat)	fAstigmatism,
		(OctaneDTOFloat)	fFieldCurvature
		)

		OctaneCameraAberration() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fSphereAberration, fComa, fAstigmatism, fFieldCurvature, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCameraDepthOfField : public OctaneNodeBase {
        REFLECTABLE
        (
		(OctaneDTOBool)		bAutoFocus,
		(OctaneDTOFloat)	fFocalDepth,
		(OctaneDTOFloat)	fAperture,
		(OctaneDTOFloat)	fApertureAspectRatio,
		(OctaneDTOEnum)		iApertureShape,
		(OctaneDTOFloat)	fApertureEdge,
		(OctaneDTOInt)		iApertureBladeCount,
		(OctaneDTOFloat)	fApertureRotation,
		(OctaneDTOFloat)	fApertureRoundedness,
		(OctaneDTOFloat)	fCentralObstruction,
		(OctaneDTOFloat)	fNorchPosition,
		(OctaneDTOFloat)	fNorchScale,
		(OctaneDTOShader)	sCustomAperture
        )

		OctaneCameraDepthOfField() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bAutoFocus, fFocalDepth, fAperture, fApertureAspectRatio, iApertureShape, fApertureEdge, 
			iApertureBladeCount, fApertureRotation, fApertureRoundedness, fCentralObstruction,
			fNorchPosition, fNorchScale, sCustomAperture, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneCameraDiopter : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnableSplitFocusDiopter,
		(OctaneDTOFloat)	fDiopterFocalDepth,
		(OctaneDTOFloat)	fDiopterRotation,
		(OctaneDTOFloat2)	f2DiopterTranslation,
		(OctaneDTOFloat)	fDiopterBoundaryWidth,
		(OctaneDTOFloat)	fDiopterBoundaryFalloff,
		(OctaneDTOBool)		bShowDiopterGuide
		)

		OctaneCameraDiopter() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnableSplitFocusDiopter, fDiopterFocalDepth, fDiopterRotation, f2DiopterTranslation, 
			fDiopterBoundaryWidth, fDiopterBoundaryFalloff, bShowDiopterGuide, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneUniversalCamera : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCameraMode,
		//Physical Camera parameters
		(OctaneDTOFloat)	fSensorWidth,
		(OctaneDTOFloat)	fFocalLength,
		(OctaneDTOFloat)	fFstop,
    (OctaneDTOBool)		bUseFstop,
		//Viewing angle
		(OctaneDTOFloat)	fFieldOfView,
		(OctaneDTOFloat)	fScaleOfView,
		(OctaneDTOFloat2)	f2LensShift,
		(OctaneDTOFloat)	fPixelAspectRatio,
    (OctaneDTOBool)		bPerspectiveCorrection,
		//Fisheye
		(OctaneDTOFloat)	fFisheyeAngle,
		(OctaneDTOEnum)		iFisheyeType,
		(OctaneDTOBool)		bHardVignette,
		(OctaneDTOEnum)		iFisheyeProjection,
		//Panoramic
		(OctaneDTOFloat)	fHorizontalFiledOfView,
		(OctaneDTOFloat)	fVerticalFiledOfView,
		(OctaneDTOEnum)		iCubemapLayout,
		(OctaneDTOBool)		bEquiAngularCubemap,
		//Distortion
		(OctaneDTOBool)		bUseDistortionTexture,
		(OctaneDTOShader)	sDistortionTexture,
		(OctaneDTOFloat)	fSphereDistortion,
		(OctaneDTOFloat)	fBarrelDistortion,
		(OctaneDTOFloat)	fBarrelDistortionCorners,
		//Aberration
		(OctaneDTOFloat)	fSphereAberration,
		(OctaneDTOFloat)	fComa,
		(OctaneDTOFloat)	fAstigmatism,
		(OctaneDTOFloat)	fFieldCurvature,
		//Clipping
		(OctaneDTOFloat)	fNearClipDepth,
		(OctaneDTOFloat)	fFarClipDepth,
		//Depth of field
		(OctaneDTOBool)		bAutoFocus,
		(OctaneDTOFloat)	fFocalDepth,
		(OctaneDTOFloat)	fAperture,
		(OctaneDTOFloat)	fApertureAspectRatio,
		(OctaneDTOEnum)		iApertureShape,
		(OctaneDTOFloat)	fApertureEdge,
		(OctaneDTOInt)		iApertureBladeCount,
		(OctaneDTOFloat)	fApertureRotation,
		(OctaneDTOFloat)	fApertureRoundedness,
		(OctaneDTOFloat)	fCentralObstruction,
		(OctaneDTOFloat)	fNorchPosition,
		(OctaneDTOFloat)	fNorchScale,
		(OctaneDTOShader)	sCustomAperture,
		//Optical vignetting
		(OctaneDTOFloat)	fOpticalVignetteDistance,
		(OctaneDTOFloat)	fOpticalVignetteScale,
		//Split-focus diopter
		(OctaneDTOBool)		bEnableSplitFocusDiopter,
		(OctaneDTOFloat)	fDiopterFocalDepth,
		(OctaneDTOFloat)	fDiopterRotation,
		(OctaneDTOFloat2)	f2DiopterTranslation,
		(OctaneDTOFloat)	fDiopterBoundaryWidth,
		(OctaneDTOFloat)	fDiopterBoundaryFalloff,
		(OctaneDTOBool)		bShowDiopterGuide,
		//Position
		(OctaneDTOFloat3)	f3Position,
		(OctaneDTOFloat3)	f3Target,
		(OctaneDTOFloat3)	f3Up,
		(OctaneDTOBool)		bKeepUpright
		)
		OctaneCameraDistortion		oDistortion;
		OctaneCameraAberration		oAberration;
		OctaneCameraDepthOfField	oDepthOfField;
		OctaneCameraDiopter			oDiopter;
		OctaneCameraPosition		oPositoin;

		OctaneUniversalCamera() : 
			OctaneNodeBase(Octane::NT_CAM_UNIVERSAL, "OctUniversalCam")
		{
		}

		void PackAttributes() {
			oDistortion.bUseDistortionTexture = bUseDistortionTexture;
			oDistortion.sDistortionTexture = sDistortionTexture;
			oDistortion.fSphereDistortion = fSphereDistortion;
			oDistortion.fBarrelDistortion = fBarrelDistortion;
			oDistortion.fBarrelDistortionCorners = fBarrelDistortionCorners;

			oAberration.fSphereAberration = fSphereAberration;
			oAberration.fComa = fComa;
			oAberration.fAstigmatism = fAstigmatism;
			oAberration.fFieldCurvature = fFieldCurvature;

			oDepthOfField.bAutoFocus = bAutoFocus;
			oDepthOfField.fFocalDepth = fFocalDepth;
			oDepthOfField.fAperture = fAperture;
			oDepthOfField.fApertureAspectRatio = fApertureAspectRatio;
			oDepthOfField.iApertureShape = iApertureShape;
			oDepthOfField.fApertureEdge = fApertureEdge;
			oDepthOfField.iApertureBladeCount = iApertureBladeCount;
			oDepthOfField.fApertureRotation = fApertureRotation;
			oDepthOfField.fApertureRoundedness = fApertureRoundedness;
			oDepthOfField.fCentralObstruction = fCentralObstruction;
			oDepthOfField.fNorchPosition = fNorchPosition;
			oDepthOfField.fNorchScale = fNorchScale;
			oDepthOfField.sCustomAperture = sCustomAperture;

			oDiopter.bEnableSplitFocusDiopter = bEnableSplitFocusDiopter;
			oDiopter.fDiopterFocalDepth = fDiopterFocalDepth;
			oDiopter.fDiopterRotation = fDiopterRotation;
			oDiopter.f2DiopterTranslation = f2DiopterTranslation;
			oDiopter.fDiopterBoundaryWidth = fDiopterBoundaryWidth;
			oDiopter.fDiopterBoundaryFalloff = fDiopterBoundaryFalloff;
			oDiopter.bShowDiopterGuide = bShowDiopterGuide;

			oPositoin.f3Position = f3Position;
			oPositoin.f3Target = f3Target;
			oPositoin.f3Up = f3Up;
			oPositoin.bKeepUpright = bKeepUpright;
		}
		void UnpackAttributes() {
			bUseDistortionTexture = oDistortion.bUseDistortionTexture;
			sDistortionTexture = oDistortion.sDistortionTexture;
			fSphereDistortion = oDistortion.fSphereDistortion;
			fBarrelDistortion = oDistortion.fBarrelDistortion;
			fBarrelDistortionCorners = oDistortion.fBarrelDistortionCorners;

			fSphereAberration = oAberration.fSphereAberration;
			fComa = oAberration.fComa;
			fAstigmatism = oAberration.fAstigmatism;
			fFieldCurvature = oAberration.fFieldCurvature;

			bAutoFocus = oDepthOfField.bAutoFocus;
			fFocalDepth = oDepthOfField.fFocalDepth;
			fAperture = oDepthOfField.fAperture;
			fApertureAspectRatio = oDepthOfField.fApertureAspectRatio;
			iApertureShape = oDepthOfField.iApertureShape;
			fApertureEdge = oDepthOfField.fApertureEdge;
			iApertureBladeCount = oDepthOfField.iApertureBladeCount;
			fApertureRotation = oDepthOfField.fApertureRotation;
			fApertureRoundedness = oDepthOfField.fApertureRoundedness;
			fCentralObstruction = oDepthOfField.fCentralObstruction;
			fNorchPosition = oDepthOfField.fNorchPosition;
			fNorchScale = oDepthOfField.fNorchScale;
			sCustomAperture = oDepthOfField.sCustomAperture;

			bEnableSplitFocusDiopter = oDiopter.bEnableSplitFocusDiopter;
			fDiopterFocalDepth = oDiopter.fDiopterFocalDepth;
			fDiopterRotation = oDiopter.fDiopterRotation;
			f2DiopterTranslation = oDiopter.f2DiopterTranslation;
			fDiopterBoundaryWidth = oDiopter.fDiopterBoundaryWidth;
			fDiopterBoundaryFalloff = oDiopter.fDiopterBoundaryFalloff;
			bShowDiopterGuide = oDiopter.bShowDiopterGuide;

			f3Position = oPositoin.f3Position;
			f3Target = oPositoin.f3Target;
			f3Up = oPositoin.f3Up;
			bKeepUpright = oPositoin.bKeepUpright;
		}

		OCTANE_NODE_PRE_UPDATE_FUNCTIONS
    OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(
			iCameraMode, 
			fSensorWidth, fFocalLength, fFstop, bUseFstop,
			fFieldOfView, fScaleOfView, f2LensShift, fPixelAspectRatio, bPerspectiveCorrection,
			fFisheyeAngle, iFisheyeType, bHardVignette, iFisheyeProjection,
			fHorizontalFiledOfView, fVerticalFiledOfView, iCubemapLayout, bEquiAngularCubemap, 
			oDistortion,
			oAberration,
			fNearClipDepth, fFarClipDepth,
			oDepthOfField,
			fOpticalVignetteDistance, fOpticalVignetteScale, 
			oDiopter, 
			oPositoin,
			MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneUniversalCamera

	struct OctaneRenderPasses : public OctaneNodeBase {
		const static PacketType packetType = LOAD_RENDER_PASSES;

		REFLECTABLE
		(
		(OctaneDTOBool)		bUsePasses,
		(OctaneDTOInt)		iPreviewPass,
		(OctaneDTOBool)		bIncludeEnvironment,
		(OctaneDTOInt)		iCryptomatteBins,
		(OctaneDTOInt)		iCryptomatteSeedFactor,
		(OctaneDTOInt)		iMaxInfoSample,
		(OctaneDTOEnum)		iSamplingMode,
		(OctaneDTOBool)		bBumpAndNormalMapping,
		(OctaneDTOFloat)	fOpacityThreshold,
		(OctaneDTOFloat)	fZDepthMax,
		(OctaneDTOFloat)	fUVMax,
		(OctaneDTOInt)		iUVCoordinateSelection,
		(OctaneDTOFloat)	fMaxSpeed,
		(OctaneDTOFloat)	fAODistance,
		(OctaneDTOBool)		bAOAlphaShadows,
		(OctaneDTOFloat)	fInfoPassZDepthEnvironment,
		(OctaneDTOBool)		bShadingEnabled,
		(OctaneDTOBool)		bHighlightBackfaces
		)
		OctaneDTOInt		iBeautyPasses;
		OctaneDTOInt		iDenoiserPasses;
		OctaneDTOInt		iPostProcessingPasses;
		OctaneDTOInt		iRenderLayerPasses;
		OctaneDTOInt		iLightingPasses;
    OctaneDTOInt		iLightingDirectPasses;
    OctaneDTOInt		iLightingIndirectPasses;
		OctaneDTOInt		iCryptomattePasses;
		OctaneDTOInt		iInfoPasses;
		OctaneDTOInt		iMaterialPasses;
		OctaneDTOBool		bUseRenderAOV;
    OctaneDTOString		sRenderPassesLibraryOrbxPath;
		OctaneDTOString		sRenderAOVRootNode;

		OctaneRenderPasses() :
			bUsePasses("use_passes"),
			iPreviewPass("current_preview_pass_type"),
			bIncludeEnvironment("pass_pp_env"),
			iCryptomatteBins("cryptomatte_pass_channels"),
			iCryptomatteSeedFactor("cryptomatte_seed_factor"),
			iMaxInfoSample("info_pass_max_samples"),
			iSamplingMode("info_pass_sampling_mode"),
			bBumpAndNormalMapping("info_pass_bump"),
			fOpacityThreshold("info_pass_opacity_threshold"),
			fZDepthMax("info_pass_z_depth_max"),
			fUVMax("info_pass_uv_max"),
			iUVCoordinateSelection("info_pass_uv_coordinate_selection"),
			fMaxSpeed("info_pass_max_speed"),
			fAODistance("info_pass_ao_distance"),
			bAOAlphaShadows("info_pass_alpha_shadows"),
      fInfoPassZDepthEnvironment("info_pass_z_depth_environment"),
      bShadingEnabled("shading_enabled"),
      bHighlightBackfaces("highlight_backfaces"),
			OctaneNodeBase(Octane::NT_RENDER_PASSES, "OctaneRenderPasses")
		{
			sName = OCTANE_BLENDER_RENDER_PASS_NODE;
			bUseRenderAOV = false;
			sRenderAOVRootNode.sVal = "";
		}

		inline bool operator==(const OctaneRenderPasses& other) {
			return bUsePasses.bVal == other.bUsePasses.bVal
				&& iPreviewPass.iVal == other.iPreviewPass.iVal
				&& bIncludeEnvironment.bVal == other.bIncludeEnvironment.bVal
				&& iCryptomatteBins.iVal == other.iCryptomatteBins.iVal
				&& iCryptomatteSeedFactor.iVal == other.iCryptomatteSeedFactor.iVal
				&& iMaxInfoSample.iVal == other.iMaxInfoSample.iVal
				&& iSamplingMode.iVal == other.iSamplingMode.iVal
				&& bBumpAndNormalMapping.bVal == other.bBumpAndNormalMapping.bVal
				&& fOpacityThreshold.fVal == other.fOpacityThreshold.fVal
				&& fZDepthMax.fVal == other.fZDepthMax.fVal
				&& fUVMax.fVal == other.fUVMax.fVal
				&& iUVCoordinateSelection.iVal == other.iUVCoordinateSelection.iVal
				&& fMaxSpeed.fVal == other.fMaxSpeed.fVal
				&& fAODistance.fVal == other.fAODistance.fVal
				&& bAOAlphaShadows.bVal == other.bAOAlphaShadows.bVal
        && fInfoPassZDepthEnvironment.fVal == other.fInfoPassZDepthEnvironment.fVal
        && bShadingEnabled.bVal == other.bShadingEnabled.bVal
        && bHighlightBackfaces.bVal == other.bHighlightBackfaces.bVal
				&& iBeautyPasses.iVal == other.iBeautyPasses.iVal
				&& iDenoiserPasses.iVal == other.iDenoiserPasses.iVal
				&& iPostProcessingPasses.iVal == other.iPostProcessingPasses.iVal
				&& iRenderLayerPasses.iVal == other.iRenderLayerPasses.iVal
				&& iLightingPasses.iVal == other.iLightingPasses.iVal
        && iLightingDirectPasses.iVal == other.iLightingDirectPasses.iVal
        && iLightingIndirectPasses.iVal == other.iLightingIndirectPasses.iVal
				&& iCryptomattePasses.iVal == other.iCryptomattePasses.iVal
				&& iInfoPasses.iVal == other.iInfoPasses.iVal
				&& iMaterialPasses.iVal == other.iMaterialPasses.iVal
				&& bUseRenderAOV.bVal == other.bUseRenderAOV.bVal
        && sRenderPassesLibraryOrbxPath.sVal == other.sRenderPassesLibraryOrbxPath.sVal
				&& sRenderAOVRootNode.sVal == other.sRenderAOVRootNode.sVal;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(bUsePasses, iPreviewPass, bIncludeEnvironment, iCryptomatteBins, iCryptomatteSeedFactor,
			iMaxInfoSample, iSamplingMode, bBumpAndNormalMapping, fOpacityThreshold, fZDepthMax, fUVMax, iUVCoordinateSelection,
			fMaxSpeed, fAODistance, bAOAlphaShadows, fInfoPassZDepthEnvironment, bShadingEnabled, bHighlightBackfaces,
			iBeautyPasses, iDenoiserPasses, iPostProcessingPasses, iRenderLayerPasses, iLightingPasses, iLightingDirectPasses, iLightingIndirectPasses, iCryptomattePasses, iInfoPasses, iMaterialPasses,
			bUseRenderAOV, sRenderPassesLibraryOrbxPath, sRenderAOVRootNode,
			MSGPACK_BASE(OctaneNodeBase));
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// BASIC INFO NODE
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneCommand : public OctaneNodeBase {
		int							iCommandType;
		std::vector<int>			iParams;
		std::vector<float>			fParams;
		std::vector<std::string>	sParams;
		OctaneCommand() : iCommandType(iCommandType), OctaneNodeBase(Octane::ENT_COMMAND, "OctaneCommand") { sName = "OctaneCommand"; }
		OctaneCommand(int cmdType, const std::vector<int>& iParams, const std::vector<float>& fParams, const std::vector<std::string>& sParams) :
			iCommandType(cmdType), iParams(iParams), fParams(fParams), sParams(sParams), OctaneNodeBase(Octane::ENT_COMMAND, "OctaneCommand") {
			sName = "OctaneCommand";
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(iCommandType, iParams, fParams, sParams, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneDBNodes : public OctaneNodeBase {
		enum OctaneDBType {
		  MATERIAL = 0,
		  MEDIUM = 1,
		  TEXTURE = 2,
		};
		bool bClose;
		int iOctaneDBType;
		uint32_t iNodesNum;
		std::vector<OctaneNodeBase*> octaneDBNodes;
		OctaneDBNodes() : bClose(true), iOctaneDBType(0), iNodesNum(0), OctaneNodeBase(Octane::ENT_OCTANEDB_NODE, "OctaneDBNodes") {}
		OctaneDBNodes(bool bClose, uint32_t iNodesNum) : bClose(bClose), iOctaneDBType(0), iNodesNum(iNodesNum), OctaneNodeBase(Octane::ENT_OCTANEDB_NODE, "OctaneDBNodes") {}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		MSGPACK_DEFINE(bClose, iOctaneDBType, iNodesNum, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSaveImage : public OctaneNodeBase {
		std::string					sPath;
		std::string					sFileName;
		std::string					sOctaneTag;
		std::vector<std::string>	sPassNames;
		std::vector<int>			iPasses;
		std::string					sOCIOColorSpaceName;
		std::string					sOCIOLookName;
		bool						bForceToneMapping;
		bool						bPremultipleAlpha;
		int							iExportType;
		int							iImageType;
		int							iExrCompressionType;
		int							iDWACompressionLevel;
		int							iTiffCompressionType;
		int							iJpegQuality;
		OctaneSaveImage() : OctaneNodeBase(Octane::ENT_SAVE_IMAGES, "OctaneSaveImage") {}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(sPath, sFileName, sOctaneTag, sPassNames, iPasses, sOCIOColorSpaceName, sOCIOLookName, bForceToneMapping, bPremultipleAlpha, iExportType, iImageType, iExrCompressionType, iDWACompressionLevel, iTiffCompressionType, iJpegQuality, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCameraData : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOFloat)	fMaxZDepth,
		(OctaneDTOFloat)	fMaxDistance,
		(OctaneDTOBool)		bEnvironmentProjection,
		(OctaneDTOBool)		bKeepFrontProjection
		)

		std::string sViewVectorNodeName;
		std::string sViewZDepthName;
		std::string sViewDistanceName;
		std::string sFrontProjectionName;
		std::string sCameraDataOrbxPath;

		OctaneCameraData() :
			fMaxZDepth("Max Z-Depth"),
			fMaxDistance("Max Distance"),
			bKeepFrontProjection("Keep Front Projection"),
			OctaneNodeBase(Octane::ENT_CAMERA_DATA, "ShaderNodeCameraData")
		{
		  sViewVectorNodeName = "";
		  sViewZDepthName = "";
		  sViewDistanceName = "";
		  sFrontProjectionName = "";
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(fMaxZDepth, fMaxDistance, bEnvironmentProjection, bKeepFrontProjection, sViewVectorNodeName, sViewZDepthName, sViewDistanceName, sFrontProjectionName, sCameraDataOrbxPath, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneEngineData : public OctaneNodeBase {		
		int iType;	
		std::map<std::string, int> oResourceCacheData;
		OctaneEngineData() : OctaneNodeBase(Octane::ENT_ENGINE_DATA, "OctaneEngineData", 0, 1) { iType = RESOURCE_CACHE_DATA; }

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		MSGPACK_DEFINE(iType, oResourceCacheData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneOrbxPreview : public OctaneNodeBase {
		std::string sOrbxPath;
		std::string sAbcPath;
		float fFps;
		OctaneOrbxPreview() : OctaneNodeBase(Octane::ENT_ORBX_PREVIEW, "OctaneOrbxPreview", 0, 1) {}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		MSGPACK_DEFINE(sOrbxPath, sAbcPath, fFps, MSGPACK_BASE(OctaneNodeBase));
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// MATERIALS
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	/// The structure holding a diffuse material data that is going to be uploaded to the Octane server.
	struct OctaneDiffuseMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fDiffuse,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOInt)		iPriority,
		(OctaneDTOFloat)	fTransmission,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOShader)	tEmission,
		(OctaneDTOBool)		bShadowCatcher,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)	tMaterialLayer
		)

		OctaneDiffuseMaterial() :
			fDiffuse("Diffuse"),
			fRoughness("Roughness"),
			sBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			fRoundedEdgeRadius("Edges rounding"),
			iPriority("Priority"),
			fTransmission("Transmission"),
			tMedium("Medium"),
			tEmission("Emission"),
			bShadowCatcher("Shadow catcher"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_DIFFUSE, "ShaderNodeOctDiffuseMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDiffuse, fRoughness, sBump, tNormal, tDisplacement, fOpacity, bSmooth, bSmoothShadowTerminator,
			fRoundedEdgeRadius, iPriority, fTransmission, tMedium, tEmission, bShadowCatcher, 
			iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDiffuseMaterial

	struct OctaneMixMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fAmount,
		(OctaneDTOShader)	tMaterial1,
		(OctaneDTOShader)	tMaterial2,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)	tDisplacement
		)

		OctaneMixMaterial() :
			fAmount("Amount"),
			tMaterial1("Material1"),
			tMaterial2("Material2"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tDisplacement("Displacement"),
			OctaneNodeBase(Octane::NT_MAT_MIX, "ShaderNodeOctMixMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAmount, tMaterial1, tMaterial2, tDisplacement, iCustomAOV, iCustomAOVChannel, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMixMaterial

	struct OctanePortalMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnabled
		)

		OctanePortalMaterial() :
			bEnabled("Enabled"),
			OctaneNodeBase(Octane::NT_MAT_PORTAL, "ShaderNodeOctPortalMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnabled, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctanePortalMaterial

	struct OctaneGlossyMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fDiffuse,
		(OctaneDTOFloat)	fSpecular,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTORGB)		fSheen,
		(OctaneDTOFloat)	fSheenRoughness,
		(OctaneDTOFloat)	fIndexOfReflection,		
		(OctaneDTOBool)		bAllowCaustics,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOInt)		iPriority,
		(OctaneDTOFloat)	fRoundedEdgeRadius,		
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)	tMaterialLayer
		)

		OctaneGlossyMaterial() :
			fDiffuse("Diffuse"),
			fSpecular("Specular"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			fSheen("Sheen"),
			fSheenRoughness("Sheen Roughness"),
			fIndexOfReflection("Index"),
			bAllowCaustics("Allow caustics"),
			sBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			iPriority("Priority"),
			fRoundedEdgeRadius("Edges rounding"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_GLOSSY, "ShaderNodeOctGlossyMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDiffuse, fSpecular, iBRDFModel, fRoughness, 
			fAnisotropy, fRotation, fSheen, fSheenRoughness, fIndexOfReflection, bAllowCaustics,
			sBump, tNormal, tDisplacement, fOpacity, bSmooth, bSmoothShadowTerminator, iPriority, fRoundedEdgeRadius,
			fFilmWidth, fFilmIndex, iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneGlossyMaterial

	struct OctaneSpecularMaterial : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fReflection,
		(OctaneDTORGB)		fTransmission,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTOFloat)	fIndexOfReflection,
		(OctaneDTOBool)		bAllowCaustics,
		(OctaneDTOFloat)	fDispersionCoef,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOInt)		iPriority,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOBool)		bFakeShadows,
		(OctaneDTOBool)		bAffectAplha,
		(OctaneDTOBool)		bThinWall,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)	tMaterialLayer	
		)

		OctaneSpecularMaterial() : 
			fReflection("Reflection"),
			fTransmission("Transmission Color"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			fIndexOfReflection("Index"),
			bAllowCaustics("Allow caustics"),
			fDispersionCoef("Dispersion Coef."),
			sBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			iPriority("Priority"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			fRoundedEdgeRadius("Edges rounding"),
			tMedium("Medium"),
			bFakeShadows("Fake Shadows"),
			bAffectAplha("Affect alpha"),
			bThinWall("Thin wall"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_SPECULAR, "ShaderNodeOctSpecularMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fReflection, fTransmission, iBRDFModel, fRoughness, 
			fAnisotropy, fRotation, fIndexOfReflection, bAllowCaustics, fDispersionCoef,
			sBump, tNormal, tDisplacement, fOpacity, bSmooth, bSmoothShadowTerminator, iPriority,
			fRoundedEdgeRadius, tMedium, bFakeShadows, bAffectAplha, bThinWall,
			fFilmWidth, fFilmIndex, iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSpecularMaterial

	struct OctaneToonMaterial : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fDiffuse,
		(OctaneDTOFloat)	fSpecular,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOEnum)		iToonLightMode,
		(OctaneDTOShader)	tToonDiffuseRamp,
		(OctaneDTOShader)	tToonSpecularRamp,
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat3)	fOutlineColor,
		(OctaneDTOFloat)	fOutlineThickness,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel
		)

		OctaneToonMaterial() : 
			fDiffuse("Diffuse"), 
			fSpecular("Specular"),
			fRoughness("Roughness"),
			iToonLightMode("toon_light_mode", false),
			tToonDiffuseRamp("Toon Diffuse Ramp"),
			tToonSpecularRamp("Toon Specular Ramp"),
			tBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOutlineColor("Outline Color"),
			fOutlineThickness("Outline Thickness"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			fRoundedEdgeRadius("Rounded Edge Radius"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			OctaneNodeBase(Octane::NT_MAT_TOON, "ShaderNodeOctToonMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDiffuse, fSpecular, fRoughness, iToonLightMode, 
			tToonDiffuseRamp, tToonSpecularRamp, tBump, tNormal, tDisplacement, 
			fOutlineColor, fOutlineThickness, fOpacity, bSmooth, bSmoothShadowTerminator,
			fRoundedEdgeRadius, iCustomAOV, iCustomAOVChannel, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneToonMaterial

	struct OctaneMetalMaterial : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	tDiffuse,
		(OctaneDTOFloat)	fSpecular,
		(OctaneDTOShader)	tSpecularMap,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTORGB)		fSheen,
		(OctaneDTOFloat)	fSheenRoughness,
		(OctaneDTOEnum)		iIORModel,
		(OctaneDTOFloat2)	fIndexOfReflection,
		(OctaneDTOFloat2)	fIndexOfReflectionGreen,
		(OctaneDTOFloat2)	fIndexOfReflectionBlue,
		(OctaneDTOBool)		bAllowCaustics,
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOInt)		iPriority,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)   tMaterialLayer
		)

		OctaneMetalMaterial() :
			tDiffuse("Diffuse"),
			fSpecular("Specular"),
			tSpecularMap("Specular map"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			fSheen("Sheen"),
			fSheenRoughness("Sheen Roughness"),
			iIORModel("metallic_reflection_mode", false),
			fIndexOfReflection("IOR"),
			fIndexOfReflectionGreen("IOR(green)"),
			fIndexOfReflectionBlue("IOR(blue)"),
			bAllowCaustics("Allow caustics"),
			tBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			iPriority("Priority"),
			fRoundedEdgeRadius("Rounded Edge Radius"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_METAL, "ShaderNodeOctMetalMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(tDiffuse, fSpecular, tSpecularMap, iBRDFModel, fRoughness, 
			fAnisotropy, fRotation, fSheen, fSheenRoughness, iIORModel, fIndexOfReflection, 
			fIndexOfReflectionGreen, fIndexOfReflectionBlue, bAllowCaustics, tBump, tNormal,
			tDisplacement, fOpacity, bSmooth, bSmoothShadowTerminator, iPriority, fRoundedEdgeRadius,
			fFilmWidth, fFilmIndex, iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMetalMaterial

	struct OctaneUniversalIOR : public OctaneNodeBase {
        REFLECTABLE
        (
		(OctaneDTOFloat)	fBaseIOR,
		(OctaneDTOShader)	tBaseIORMap,
		(OctaneDTOEnum)		iIORModel,
		(OctaneDTOFloat2)	fIOR,
		(OctaneDTOFloat2)	fIORGreen,
		(OctaneDTOFloat2)	fIORBlue,
		(OctaneDTOBool)		bAllowCaustics
        )

		OctaneUniversalIOR() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fBaseIOR, tBaseIORMap, iIORModel, fIOR, fIORGreen, fIORBlue, bAllowCaustics, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneUniversalCoating : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fCoating,
		(OctaneDTOFloat)	fCoatingRoughness,
		(OctaneDTOFloat)	fCoatingIOR,
		(OctaneDTOShader)	tCoatingBump,
		(OctaneDTOShader)	tCoatingNormal
		)

		OctaneUniversalCoating() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fCoating, fCoatingRoughness, fCoatingIOR, tCoatingBump, tCoatingNormal, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneUniversalTransmission : public OctaneNodeBase {
        REFLECTABLE
        (
		(OctaneDTOFloat)	fDispersionCoef,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fOpacity,		
		(OctaneDTOBool)		bFakeShadows,
		(OctaneDTOBool)		bAffectAplha
        )

		OctaneUniversalTransmission() : OctaneNodeBase(Octane::NT_UNKNOWN, "") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDispersionCoef, tMedium, fOpacity, bFakeShadows, bAffectAplha, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneUniversalMaterial : public OctaneNodeBase {
		REFLECTABLE
		(				
		//Base Layer
		(OctaneDTORGB)		fTransmission,
		(OctaneDTOEnum)		iTransmissionType,
		(OctaneDTORGB)		fAlbedoColor,
		(OctaneDTOFloat)	fMetallic,
		(OctaneDTOEnum)		iBRDFModel,
		//Specular Layer
		(OctaneDTOFloat)	fSpecular,
		//Roughness
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		//IOR
		(OctaneDTOFloat)	fBaseIOR,
		(OctaneDTOShader)	tBaseIORMap,
		(OctaneDTOEnum)		iIORModel,
		(OctaneDTOFloat2)	fIndexOfReflection,
		(OctaneDTOFloat2)	fIndexOfReflectionGreen,
		(OctaneDTOFloat2)	fIndexOfReflectionBlue,
		(OctaneDTOBool)		bAllowCaustics,
		//Coating Layer
		(OctaneDTORGB)		fCoating,
		(OctaneDTOFloat)	fCoatingRoughness,
		(OctaneDTOFloat)	fCoatingIOR,
		(OctaneDTOShader)	tCoatingBump,
		(OctaneDTOShader)	tCoatingNormal,
		//Thin Film Layer
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		//Sheen Layer
		(OctaneDTORGB)		fSheen,
		(OctaneDTOFloat)	fSheenRoughness,
		(OctaneDTOShader)	tSheenBump,
		(OctaneDTOShader)	tSheenNormal,
		//Transmission Properties
		(OctaneDTOFloat)	fDispersionCoef,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fOpacity,		
		(OctaneDTOBool)		bFakeShadows,
		(OctaneDTOBool)		bAffectAplha,
		//Geometric Properties
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,		
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOInt)		iPriority,
		(OctaneDTOFloat)	fRoundedEdgeRadius,		
		(OctaneDTOShader)	tEmission,
		(OctaneDTOBool)		bShadowCatcher,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)   tMaterialLayer
		)
		OctaneUniversalIOR	oOctaneUniversalIOR;
		OctaneUniversalCoating oOctaneUniversalCoating;
		OctaneUniversalTransmission oOctaneUniversalTransmission;


		OctaneUniversalMaterial() :						
			//Base Layer
			fTransmission("Transmission"),
			iTransmissionType("transmission_type", false),
			fAlbedoColor("Albedo color"),
			fMetallic("Metallic"),
			iBRDFModel("brdf_model", false),
			//Specular Layer			
			fSpecular("Specular"),
			//Roughness
			fRoughness("Roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			//IOR
			fBaseIOR("Dielectric IOR"),
			tBaseIORMap("Dielectric 1|IOR map"),
			iIORModel("universal_reflection_mode", false),
			fIndexOfReflection("Metallic IOR"),
			fIndexOfReflectionGreen("Metallic IOR(green)"),
			fIndexOfReflectionBlue("Metallic IOR(blue)"),
			bAllowCaustics("Allow caustics"),
			//Coating Layer
			fCoating("Coating"),
			fCoatingRoughness("Coating Roughness"),
			fCoatingIOR("Coating IOR"),
			tCoatingBump("Coating Bump"),
			tCoatingNormal("Coating Normal"),
			//Thin Film Layer
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			//Sheen Layer
			fSheen("Sheen"),
			fSheenRoughness("Sheen Roughness"),
			tSheenBump("Sheen Bump"),
			tSheenNormal("Sheen Normal"),
			//Transmission Properties
			fDispersionCoef("Dispersion Coef."),
			tMedium("Medium"),
			fOpacity("Opacity"),
			bFakeShadows("Fake Shadows"),
			bAffectAplha("Affect alpha"),
			//Geometric Properties
			tBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			iPriority("Priority"),
			fRoundedEdgeRadius("Rounded Edge Radius"),
			tEmission("Emission"),
			bShadowCatcher("Shadow catcher"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_UNIVERSAL, "ShaderNodeOctUniversalMat")
		{
		}

		void PackAttributes() {
			oOctaneUniversalIOR.fBaseIOR = fBaseIOR;
			oOctaneUniversalIOR.tBaseIORMap = tBaseIORMap;
			oOctaneUniversalIOR.iIORModel = iIORModel;
			oOctaneUniversalIOR.fIOR = fIndexOfReflection;
			oOctaneUniversalIOR.fIORGreen = fIndexOfReflectionGreen;
			oOctaneUniversalIOR.fIORBlue = fIndexOfReflectionBlue;
			oOctaneUniversalIOR.bAllowCaustics = bAllowCaustics;

			oOctaneUniversalCoating.fCoating = fCoating;
			oOctaneUniversalCoating.fCoatingRoughness = fCoatingRoughness;
			oOctaneUniversalCoating.fCoatingIOR = fCoatingIOR;
			oOctaneUniversalCoating.tCoatingBump = tCoatingBump;
			oOctaneUniversalCoating.tCoatingNormal = tCoatingNormal;

			oOctaneUniversalTransmission.fDispersionCoef = fDispersionCoef;
			oOctaneUniversalTransmission.tMedium = tMedium;
			oOctaneUniversalTransmission.fOpacity = fOpacity;
			oOctaneUniversalTransmission.bFakeShadows = bFakeShadows;
			oOctaneUniversalTransmission.bAffectAplha = bAffectAplha;
		}
		void UnpackAttributes() {
			fBaseIOR = oOctaneUniversalIOR.fBaseIOR;
			tBaseIORMap = oOctaneUniversalIOR.tBaseIORMap;
			iIORModel = oOctaneUniversalIOR.iIORModel;
			fIndexOfReflection = oOctaneUniversalIOR.fIOR;
			fIndexOfReflectionGreen = oOctaneUniversalIOR.fIORGreen;
			fIndexOfReflectionBlue = oOctaneUniversalIOR.fIORBlue;
			bAllowCaustics = oOctaneUniversalIOR.bAllowCaustics;

			fCoating = oOctaneUniversalCoating.fCoating;
			fCoatingRoughness = oOctaneUniversalCoating.fCoatingRoughness;
			fCoatingIOR = oOctaneUniversalCoating.fCoatingIOR;
			tCoatingBump = oOctaneUniversalCoating.tCoatingBump;
			tCoatingNormal = oOctaneUniversalCoating.tCoatingNormal;

			fDispersionCoef = oOctaneUniversalTransmission.fDispersionCoef;
			tMedium = oOctaneUniversalTransmission.tMedium;
			fOpacity = oOctaneUniversalTransmission.fOpacity;
			bFakeShadows = oOctaneUniversalTransmission.bFakeShadows;
			bAffectAplha = oOctaneUniversalTransmission.bAffectAplha;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTransmission, iTransmissionType, fAlbedoColor, fMetallic, iBRDFModel, fSpecular, fRoughness, fAnisotropy, fRotation,
			oOctaneUniversalIOR, 
			oOctaneUniversalCoating,
			oOctaneUniversalTransmission,
			fFilmWidth, fFilmIndex, fSheen, fSheenRoughness, tSheenBump, tSheenNormal,
			tBump, tNormal, tDisplacement, bSmooth, bSmoothShadowTerminator, iPriority, fRoundedEdgeRadius, tEmission, bShadowCatcher,
			iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneUniversalMaterial

	struct OctaneShadowCatcherMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnabled,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel
		)

		OctaneShadowCatcherMaterial() :			
			bEnabled("Enabled"),
			fOpacity("Opacity"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			OctaneNodeBase(Octane::NT_MAT_SHADOW_CATCHER, "ShaderNodeOctShadowCatcherMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnabled, fOpacity, iCustomAOV, iCustomAOVChannel, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneShadowCatcherMaterial

	struct OctaneLayeredMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)		tBaseMaterial,
		(OctaneDTOEnum)			iCustomAOV,
		(OctaneDTOEnum)			iCustomAOVChannel
		)
		std::vector<std::string>	sLayers;

		OctaneLayeredMaterial() :
			tBaseMaterial("Base Material"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			OctaneNodeBase(Octane::NT_MAT_LAYER, "ShaderNodeOctLayeredMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(tBaseMaterial, iCustomAOV, iCustomAOVChannel, sLayers, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneLayeredMaterial

	struct OctaneCompositeMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)		tDisplacement,
		(OctaneDTOEnum)			iCustomAOV,
		(OctaneDTOEnum)			iCustomAOVChannel
		)
		std::vector<std::string>	sMaterials;
		std::vector<std::string>	sMasks;

		OctaneCompositeMaterial() :
			tDisplacement("Displacement"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			OctaneNodeBase(Octane::NT_MAT_COMPOSITE, "ShaderNodeOctCompositeMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(tDisplacement, iCustomAOV, iCustomAOVChannel, sMaterials, sMasks, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCompositeMaterial

	struct OctaneHairMaterial : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fAlbedo,
		(OctaneDTORGB)		fSpecular,
		(OctaneDTOFloat)	fMelanin,
		(OctaneDTOFloat)	fPheomelanin,
		(OctaneDTOEnum)		iMode,
		(OctaneDTOFloat)	fIndexOfRefraction,	
		(OctaneDTOFloat)	fLongitudinalRoughness,
		(OctaneDTOFloat)	fAzimuthalRoughness,
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOFloat)	fRandomnessFrequency,
		(OctaneDTOFloat2)	fRandomnessOffset,
		(OctaneDTOFloat)	fRandomnessIntensity,
		(OctaneDTORGB)		fRandomnessAlbedo,
		(OctaneDTOFloat)	fRandomRoughness,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOShader)	tEmission,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel,
		(OctaneDTOShader)	tMaterialLayer	
		)

		OctaneHairMaterial() :
			fAlbedo("Albedo"),
			fSpecular("Specular"),
			fMelanin("Melanin"),
			fPheomelanin("Pheomelanin"),
			iMode("mode", false),
			fIndexOfRefraction("Index of refraction"),
			fLongitudinalRoughness("Longitudinal Roughness"),
			fAzimuthalRoughness("Azimuthal Roughness"),
			fOffset("Offset"),
			fRandomnessFrequency("Randomness Frequency"),
			fRandomnessOffset("Randomness Offset"),
			fRandomnessIntensity("Randomness Intensity"),
			fRandomnessAlbedo("Random Albedo"),
			fRandomRoughness("Random roughness"),
			fOpacity("Opacity"),
			tEmission("Emission"),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_HAIR, "ShaderNodeOctHairMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAlbedo, fSpecular, fMelanin, fPheomelanin, iMode, fIndexOfRefraction, fLongitudinalRoughness, fAzimuthalRoughness, fOffset,
			fRandomnessFrequency, fRandomnessOffset, fRandomnessIntensity, fRandomnessAlbedo, fRandomRoughness,
			fOpacity, tEmission, iCustomAOV, iCustomAOVChannel, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneHairMaterial

	struct OctaneNullMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	tMedium,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bAffectAplha,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOBool)		bSmoothShadowTerminator,
		(OctaneDTOFloat)	fRoundedEdgeRadius
		)

		OctaneNullMaterial() :
			tMedium("Medium"),
			fOpacity("Opacity"),
			bAffectAplha("Affect alpha"),
			tDisplacement("Displacement"),
			bSmooth("Smooth"),
			bSmoothShadowTerminator("Smooth Shadow Terminator"),
			fRoundedEdgeRadius("Edges rounding"),
			OctaneNodeBase(Octane::NT_MAT_NULL, "ShaderNodeOctNullMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(tMedium, fOpacity, bAffectAplha, tDisplacement, bSmooth, bSmoothShadowTerminator, fRoundedEdgeRadius, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneNullMaterial

	struct OctaneGroupLayer : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string>	sLayers;

		OctaneGroupLayer() :
			OctaneNodeBase(Octane::NT_MAT_LAYER_GROUP, "ShaderNodeOctGroupLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(sLayers, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneGroupLayer

	struct OctaneDiffuseLayer : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fDiffuse,
		(OctaneDTOFloat)	fTransmission,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOFloat)	fLayerOpacity
		)

		OctaneDiffuseLayer() :
			fDiffuse("Diffuse"),
			fTransmission("Transmission"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			sBump("Bump"),
			tNormal("Normal"),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_DIFFUSE_LAYER, "ShaderNodeOctDiffuseLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDiffuse, fTransmission, iBRDFModel, fRoughness, sBump, tNormal, fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDiffuseLayer

	struct OctaneMetallicLayer : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fSpecular,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTOEnum)		iIORModel,
		(OctaneDTOFloat2)	fIndexOfReflection,
		(OctaneDTOFloat2)	fIndexOfReflectionGreen,
		(OctaneDTOFloat2)	fIndexOfReflectionBlue,
		(OctaneDTOBool)		bAllowCaustics,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOFloat)	fLayerOpacity
		)

		OctaneMetallicLayer() :
			fSpecular("Specular"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			iIORModel("metallic_reflection_mode", false),
			fIndexOfReflection("IOR"),
			fIndexOfReflectionGreen("IOR(green)"),
			fIndexOfReflectionBlue("IOR(blue)"),
			bAllowCaustics("Allow caustics"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			tBump("Bump"),
			tNormal("Normal"),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_METALLIC_LAYER, "ShaderNodeOctMetallicLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fSpecular, iBRDFModel, 
			fRoughness, fAnisotropy, fRotation, 
			iIORModel, fIndexOfReflection, fIndexOfReflectionGreen, fIndexOfReflectionBlue, bAllowCaustics,
			fFilmWidth, fFilmIndex,
			tBump, tNormal,
			fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMetallicLayer

	struct OctaneSheenLayer : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fSheen,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAffectRoughness,
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOFloat)	fLayerOpacity
		)

		OctaneSheenLayer() :
			fSheen("Sheen"),
			fRoughness("Roughness"),
			fAffectRoughness("Affect roughness"),
			tBump("Bump"),
			tNormal("Normal"),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_SHEEN_LAYER, "ShaderNodeOctSheenLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fSheen, fRoughness, fAffectRoughness, tBump, tNormal, fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSheenLayer

	struct OctaneSpecularLayer : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTORGB)		fSpecular,
		(OctaneDTORGB)		fTransmission,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAffectRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTOFloat)	fIOR,
		(OctaneDTOBool)		bAllowCaustics,
		(OctaneDTOShader)	tIORMap,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
		(OctaneDTOBool)		bThinLayer,
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOFloat)	fDispersionCoef,
		(OctaneDTOFloat)	fLayerOpacity
		)

		OctaneSpecularLayer() :
			fSpecular("Specular"),
			fTransmission("Transmission"),
			iBRDFModel("brdf_model", false),
			fRoughness("Roughness"),
			fAffectRoughness("Affect roughness"),
			fAnisotropy("Anisotropy"),
			fRotation("Rotation"),
			fIOR("IOR"),
			bAllowCaustics("Allow caustics"),
			tIORMap("1|IOR map"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			bThinLayer("Thin Layer"),
			tBump("Bump"),
			tNormal("Normal"),
			fDispersionCoef("Dispersion Coef."),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_SPECULAR_LAYER, "ShaderNodeOctSpecularLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fSpecular, fTransmission, iBRDFModel,
			fRoughness, fAffectRoughness, fAnisotropy, fRotation,
			fIOR, bAllowCaustics, tIORMap,
			fFilmWidth, fFilmIndex,
			bThinLayer,
			tBump, tNormal, 
			fDispersionCoef, fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSpecularLayer

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// TEXTURES
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	/// The structure holding a greycolor texture data that is going to be uploaded to the Octane server.
	struct OctaneGrayscaleColorTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fValue
		)


		OctaneGrayscaleColorTexture() :
			fValue("Value"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT, "ShaderNodeOctFloatTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fValue, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a RGB spectrum texture data that is going to be uploaded to the Octane server.
	struct OctaneRGBSpectrumTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)	fColor
		)


		OctaneRGBSpectrumTexture() :
			fColor("Color"),
			OctaneNodeBase(Octane::NT_TEX_RGB, "ShaderNodeOctRGBSpectrumTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fColor, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a gaussian spectrum texture data that is going to be uploaded to the Octane server.
	struct OctaneGaussianSpectrumTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fWaveLength,
		(OctaneDTOFloat)	fWidth,
		(OctaneDTOFloat)	fPower

		)

		OctaneGaussianSpectrumTexture() :
			fWaveLength("Wave Length"),
			fWidth("Width"),
			fPower("Power"),
			OctaneNodeBase(Octane::NT_TEX_GAUSSIANSPECTRUM, "ShaderNodeOctGaussSpectrumTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fWaveLength, fWidth, fPower, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a checks texture data that is going to be uploaded to the Octane server.
	struct OctaneChecksTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection

		)

		OctaneChecksTexture() :
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_CHECKS, "ShaderNodeOctChecksTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMarbleTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOInt)		iOctaves,
		(OctaneDTOFloat)	fOmega,
		(OctaneDTOFloat)	fVariance,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)


		OctaneMarbleTexture() :
			fPower("Power"),
			fOffset("Offset"),
			iOctaves("Octaves"),
			fOmega("Omega"),
			fVariance("Variance"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_MARBLE, "ShaderNodeOctMarbleTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fOffset, iOctaves, fOmega, fVariance, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneRidgedFractalTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fRidgeHeight,
		(OctaneDTOInt)		iOctaves,
		(OctaneDTOFloat)	fOmega,
		(OctaneDTOFloat)	fLacunarity,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)

		OctaneRidgedFractalTexture() :
			fPower("Power"),
			fRidgeHeight("Offset"),
			iOctaves("Octaves"),
			fOmega("Omega"),
			fLacunarity("Lacunarity"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_RGFRACTAL, "ShaderNodeOctRidgedFractalTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fRidgeHeight, iOctaves, fOmega, fLacunarity, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSawWaveTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)


		OctaneSawWaveTexture() :
			fOffset("Offset"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_SAWWAVE, "ShaderNodeOctSawWaveTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSineWaveTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)

		OctaneSineWaveTexture() :
			fOffset("Offset"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_SINEWAVE, "ShaderNodeOctSineWaveTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriangleWaveTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)

		OctaneTriangleWaveTexture() :
			fOffset("Offset"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_TRIANGLEWAVE, "ShaderNodeOctTriWaveTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTurbulenceTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fOffset,
		(OctaneDTOInt)		iOctaves,
		(OctaneDTOFloat)	fOmega,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bTurbulence,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)

		OctaneTurbulenceTexture() :
			fPower("Power"),
			fOffset("Offset"),
			iOctaves("Octaves"),
			fOmega("Omega"),
			fGamma("Gamma"),
			bTurbulence("Turbulence"),
			bInvert("Invert"),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_TURBULENCE, "ShaderNodeOctTurbulenceTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fOffset, iOctaves, fOmega, fGamma, bTurbulence, bInvert, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneNoiseTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iNoiseType,
		(OctaneDTOInt)		iOctaves,
		(OctaneDTOFloat)	fOmega,				
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOFloat)	fContrast
		)

		OctaneNoiseTexture() :
			iNoiseType("noise_type", false),
			iOctaves("Octaves"),
			fOmega("Omega"),						
			sTransform("Transform"),
			sProjection("Projection"),
			bInvert("Invert"),
			fGamma("Gamma"),
			fContrast("Contrast"),
			OctaneNodeBase(Octane::NT_TEX_NOISE, "ShaderNodeOctNoiseTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iNoiseType, iOctaves, fOmega, sTransform, sProjection, bInvert, fGamma, fContrast, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCinema4DNoiseTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iC4DNoiseType,
		(OctaneDTOFloat)	fOctaves,
		(OctaneDTOFloat)	fLacunarity,
		(OctaneDTOFloat)	fGain,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection,
		(OctaneDTOFloat)	fT,
		(OctaneDTOBool)		bAbsolute,
		(OctaneDTOBool)		bUse4DNoise,
		(OctaneDTOFloat)	fSampleRadius,
		(OctaneDTOInt)		iRandomSeed
		)

		OctaneCinema4DNoiseTexture() :
			iC4DNoiseType("c4d_noise_type", false),
			fOctaves("Octaves"),
			fLacunarity("Lacunarity"),
			fGain("Gain"),
			sTransform("Transform"),
			sProjection("Projection"),
			fT("T"),
			bAbsolute("Absolute"),
			bUse4DNoise("Use 4D noise"),
			fSampleRadius("Sample radius"),
			iRandomSeed("Random seed"),
			OctaneNodeBase(Octane::NT_TEX_C4D_NOISE, "ShaderNodeOctCinema4DNoiseTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iC4DNoiseType, fOctaves, fLacunarity, fGain, sTransform, sProjection, fT, bAbsolute, bUse4DNoise, fSampleRadius, iRandomSeed, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneClampTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOFloat)	fMin,
		(OctaneDTOFloat)	fMax
		)

		OctaneClampTexture() :
			fTexture("Input"),
			fMin("Min"),
			fMax("Max"),
			OctaneNodeBase(Octane::NT_TEX_CLAMP, "ShaderNodeOctClampTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, fMin, fMax, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCosineMixTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fAmount,
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)


		OctaneCosineMixTexture() :
			fAmount("Amount"),
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_COSINEMIX, "ShaderNodeOctCosineMixTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAmount, fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInvertTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sTexture
		)

		OctaneInvertTexture() :
			sTexture("Texture"),
			OctaneNodeBase(Octane::NT_TEX_INVERT, "ShaderNodeOctInvertTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sTexture, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMixTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fAmount,
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)

		OctaneMixTexture() :
			fAmount("Amount"),
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_MIX, "ShaderNodeOctMixTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAmount, fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMultiplyTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)

		OctaneMultiplyTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_MULTIPLY, "ShaderNodeOctMultiplyTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneAddTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)

		OctaneAddTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_ADD, "ShaderNodeOctAddTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSubtractTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)

		OctaneSubtractTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_SUBTRACT, "ShaderNodeOctSubtractTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCompareTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fInputA,
		(OctaneDTOFloat)	fInputB,
		(OctaneDTOFloat)	fASmallerThanB,
		(OctaneDTOFloat)	fAEqOrLargerThanB
		)

		OctaneCompareTexture() :
			fInputA("InputA"),
			fInputB("InputB"),
			fASmallerThanB("If A < B"),
			fAEqOrLargerThanB("If A >= B"),
			OctaneNodeBase(Octane::NT_TEX_COMPARE, "ShaderNodeOctCompareTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fInputA, fInputB, fASmallerThanB, fAEqOrLargerThanB, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriplanarTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fBlendAngle,
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform,
		(OctaneDTORGB)		f3PositiveXTexture,
		(OctaneDTORGB)		f3NegativeXTexture,
		(OctaneDTORGB)		f3PositiveYTexture,
		(OctaneDTORGB)		f3NegativeYTexture,
		(OctaneDTORGB)		f3PositiveZTexture,
		(OctaneDTORGB)		f3NegativeZTexture		
		)

		OctaneTriplanarTexture() :
			fBlendAngle("Blend angle"),
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Blend cube transform"),
			f3PositiveXTexture("Positive X axis"),
			f3NegativeXTexture("Negative X axis"),
			f3PositiveYTexture("Positive Y axis"),
			f3NegativeYTexture("Negative Y axis"),
			f3PositiveZTexture("Positive Z axis"),
			f3NegativeZTexture("Negative Z axis"),
			OctaneNodeBase(Octane::NT_TEX_TRIPLANAR, "ShaderNodeOctTriplanarTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fBlendAngle, iCoordinateSpace, sTransform, f3PositiveXTexture, f3NegativeXTexture, f3PositiveYTexture, f3NegativeYTexture, f3PositiveZTexture, f3NegativeZTexture, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneFalloffTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iFalloffMode,
		(OctaneDTOFloat)	fNormal,
		(OctaneDTOFloat)	fGrazing,
		(OctaneDTOFloat)	fFalloff,
		(OctaneDTOFloat3)	f3Direction
		)

		OctaneFalloffTexture() :
			iFalloffMode("falloff_map_mode", false),
			fNormal("Normal"),
			fGrazing("Grazing"),
			fFalloff("Falloff Skew Factor"),
			f3Direction("Falloff direction"),
			OctaneNodeBase(Octane::NT_TEX_FALLOFF, "ShaderNodeOctFalloffTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iFalloffMode, fNormal, fGrazing, fFalloff, f3Direction, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneColorCorrectTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOFloat)	fBrightness,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOFloat)	fHue,
		(OctaneDTOFloat)	fSaturation,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOFloat)	fContrast,
		(OctaneDTOFloat)	fGain,
		(OctaneDTOFloat)	fExposure,
		(OctaneDTOFloat)	fMask
		)

		OctaneColorCorrectTexture() :
			fTexture("Texture"),
			fBrightness("Brightness"),
			bInvert("Invert"),
			fHue("Hue"),
			fSaturation("Saturation"),
			fGamma("Gamma"),
			fContrast("Contrast"),
			fGain("Gain"),
			fExposure("Exposure"),
			fMask("Mask"),
			OctaneNodeBase(Octane::NT_TEX_COLORCORRECTION, "ShaderNodeOctColorCorrectTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, fBrightness, bInvert, fHue, fSaturation, fGamma, fContrast, fGain, fExposure, fMask, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneImageData : public OctaneNodeBase {
		OctaneDTOInt		iHDRDepthType;
		OctaneDTOInt		iIESMode;
		OctaneDTOString		sFilePath;
		OctaneDTOBool		bReload;
		OctaneDTOInt		iWidth;
		OctaneDTOInt		iHeight;
		OctaneDTOInt		iChannelNum;
		std::vector<float>	fImageData;
		std::vector<uint8_t> iImageData;
		uint32_t			fDataLength;
		uint32_t			iDataLength;
		float*				pFData;
		uint8_t*			pIData;
		std::string			sImageDataMD5Hex;

		OctaneImageData() :
			OctaneNodeBase(Octane::ENT_IMAGE_DATA, "OctaneImageData")
		{
		}

		void Clear() {
			fDataLength = 0;
			iDataLength = 0;
			fImageData.clear();
			iImageData.clear();
			sFilePath = "";
			sImageDataMD5Hex = "";
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		MSGPACK_DEFINE(iHDRDepthType, iIESMode, sFilePath, bReload, iWidth, iHeight, iChannelNum, fDataLength, iDataLength, sImageDataMD5Hex, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneBaseImageNode : public OctaneNodeBase {
		OctaneImageData		oImageData;
		OctaneBaseImageNode(int octaneType, std::string pluginType) : OctaneNodeBase(octaneType, pluginType) {}

		void PackAttributes() {
			if (oImageData.fDataLength > 0) {
				this->arrayData = (void*)oImageData.pFData;
				this->arraySize = sizeof(float) * oImageData.fDataLength;
			}
			else if (oImageData.iDataLength > 0) {
				this->arrayData = (void*)oImageData.pIData;
				this->arraySize = sizeof(uint8_t) * oImageData.iDataLength;
			}
			else {
				this->arrayData = NULL;
				this->arraySize = 0;
			}
		}

		void UnpackAttributes() {
			oImageData.pFData = NULL;
			oImageData.pIData = NULL;
			if (oImageData.fDataLength > 0) {
				oImageData.pFData = (float*)this->arrayData;
			}
			else if (oImageData.iDataLength > 0) {
				oImageData.pIData = (uint8_t*)this->arrayData;
			}
		}

		OCTANE_NODE_PRE_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(oImageData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneImageTexture : public OctaneBaseImageNode {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOShader)	sColorSpace,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderModeU,
		(OctaneDTOEnum)		iBorderModeV
		)

		OctaneImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			sColorSpace("Color space"),
			bInvert("Invert"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderModeU("border_mode_u", false),
			iBorderModeV("border_mode_v", false),
			OctaneBaseImageNode(Octane::NT_TEX_IMAGE, "ShaderNodeOctImageTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fGamma, sColorSpace, bInvert, bLinearSpaceInvert, tTransform, tProjection, iBorderModeU, iBorderModeV, MSGPACK_BASE(OctaneBaseImageNode));
	}; 

	struct OctaneImageTileTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iHDRDepthType,
		(OctaneDTOInt)		iGridSizeX,
		(OctaneDTOInt)		iGridSizeY,
		(OctaneDTOInt)		iStart,
		(OctaneDTOInt)		iDigits,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOShader)	sColorSpace,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTORGB)		fEmptyTileColor,
		(OctaneDTOInt2)		iGridSize
		)
		std::vector<std::string>	sFiles;

		OctaneImageTileTexture() :
			iHDRDepthType("hdr_tex_bit_depth", false),
			iGridSizeX("Grid size(X)"),
			iGridSizeY("Grid size(Y)"),
			iStart("Start"),
			iDigits("Digits"),
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			sColorSpace("Color space"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			fEmptyTileColor("Empty tile color"),
			OctaneNodeBase(Octane::NT_TEX_IMAGE_TILES, "ShaderNodeOctImageTileTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_PRE_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(iHDRDepthType, iGridSizeX, iGridSizeY, iStart, iDigits, fPower, sColorSpace, fGamma, bInvert, bLinearSpaceInvert, tTransform, tProjection, fEmptyTileColor, iGridSize, sFiles, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneImageTileTexture

	struct OctaneFloatVertexAttributeTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOString)	sSetName
		)

		OctaneFloatVertexAttributeTexture() :
			sSetName("Name"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT_VERTEXATTRIBUTE, "ShaderNodeOctFloatVertexTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sSetName, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneColorVertexAttributeTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOString)	sSetName
		)

		OctaneColorVertexAttributeTexture() :
			sSetName("Name"),
			OctaneNodeBase(Octane::NT_TEX_COLOUR_VERTEXATTRIBUTE, "ShaderNodeOctColorVertexTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sSetName, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInstanceColorTexture : public OctaneBaseImageNode {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	sColorSpace,
		(OctaneDTOBool)		bLinearSpaceInvert
		)

		OctaneInstanceColorTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			sColorSpace("Color space"),
			bLinearSpaceInvert("Linear space invert"),
			OctaneBaseImageNode(Octane::NT_TEX_INSTANCE_COLOR, "ShaderNodeOctInstanceColorTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fGamma, sColorSpace, bInvert, bLinearSpaceInvert, MSGPACK_BASE(OctaneBaseImageNode));
	}; 

	struct OSLNodeInfo : public OctaneNodeBase
	{
		Octane::CompilationResult mCompileResult;
		std::string mCompileInfo;
		OSLNodePinInfo mPinInfo;
		OSLNodeInfo() : OctaneNodeBase(Octane::ENT_OSL_NODE_INFO, "OSLNodeInfo") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		MSGPACK_DEFINE(mCompileResult, mCompileInfo, mPinInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a osl node data that is going to be uploaded to the Octane server.
	struct OctaneOSLNodeBase : public OctaneNodeBase {
		std::string     sShaderCode;
		std::string		sFilePath;
		OSLNodeInfo		oOSLNodeInfo;		
		OctaneOSLNodeBase(int octaneType, std::string pluginType) : OctaneNodeBase(octaneType, pluginType, 0, 1) {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		MSGPACK_DEFINE(sShaderCode, sFilePath, oOSLNodeInfo, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneOSLNodeBase

	struct OctaneOSLTexture : public OctaneOSLNodeBase {
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OctaneOSLTexture() : OctaneOSLNodeBase(Octane::NT_TEX_OSL, "ShaderNodeOctOSLTex") {}
	};

	struct OctaneOSLProjection : public OctaneOSLNodeBase {
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OctaneOSLProjection() : OctaneOSLNodeBase(Octane::NT_PROJ_OSL, "ShaderNodeOctOSLProjection") {}
	};

	struct OctaneOSLCamera : public OctaneOSLNodeBase {		
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OctaneOSLCamera() : OctaneOSLNodeBase(Octane::NT_CAM_OSL, "ShaderNodeOctOSLCamera") {}
	};

	struct OctaneOSLBakingCamera : public OctaneOSLNodeBase {
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OctaneOSLBakingCamera() : OctaneOSLNodeBase(Octane::NT_CAM_OSL_BAKING, "ShaderNodeOctOSLBakingCamera") {}
	};

	struct OctaneVectron : public OctaneOSLNodeBase {
		std::string     sMaterialName;
		std::string		sVectronNodeName;

		OctaneVectron() : OctaneOSLNodeBase(Octane::NT_GEO_OSL, "ShaderNodeOctVectron") {}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		MSGPACK_DEFINE(sMaterialName, sVectronNodeName, MSGPACK_BASE(OctaneOSLNodeBase));
	};

	struct OctaneFloatImageTexture : public OctaneBaseImageNode {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	sColorSpace,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderModeU,
		(OctaneDTOEnum)		iBorderModeV
		)

		OctaneFloatImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			sColorSpace("Color space"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderModeU("border_mode_u", false),
			iBorderModeV("border_mode_v", false),
			OctaneBaseImageNode(Octane::NT_TEX_FLOATIMAGE, "ShaderNodeOctFloatImageTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fGamma, bInvert, sColorSpace, bLinearSpaceInvert, tTransform, tProjection, iBorderModeU, iBorderModeV, MSGPACK_BASE(OctaneBaseImageNode));
	}; 

	struct OctaneAlphaImageTexture : public OctaneBaseImageNode {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	sColorSpace,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderModeU,
		(OctaneDTOEnum)		iBorderModeV
		)

		OctaneAlphaImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			sColorSpace("Color space"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderModeU("border_mode_u", false),
			iBorderModeV("border_mode_v", false),
			OctaneBaseImageNode(Octane::NT_TEX_ALPHAIMAGE, "ShaderNodeOctAlphaImageTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fPower, fGamma, sColorSpace, bInvert, bLinearSpaceInvert, tTransform, tProjection, iBorderModeU, iBorderModeV, MSGPACK_BASE(OctaneBaseImageNode));
	}; 

	struct OctaneDirtTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iBiasCoordinateSpaceType,
		(OctaneDTOEnum)		iIncludeObjectMode,
		(OctaneDTOFloat)	fStrength,
		(OctaneDTOFloat)	fDetails,
		(OctaneDTOFloat)	fRadius,
		(OctaneDTOFloat)	fRadiusMap,
		(OctaneDTOFloat)	fTolerance,
		(OctaneDTOFloat)	fSpread,
		(OctaneDTOFloat)	fDistribution,
		(OctaneDTOFloat3)	fBias,
		(OctaneDTOBool)		bInvert
		)

		OctaneDirtTexture() :
			iBiasCoordinateSpaceType("bias_coordinate_space_type", false),
			iIncludeObjectMode("include_object_mode", false),
			fStrength("Strength"),
			fDetails("Details"),
			fRadius("Radius"),
			fRadiusMap("Radius map"),
			fTolerance("Tolerance"),
			fSpread("Spread"),
			fDistribution("Distribution"),
			fBias("Bias"),
			bInvert("Invert Normal"),
			OctaneNodeBase(Octane::NT_TEX_DIRT, "ShaderNodeOctDirtTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iBiasCoordinateSpaceType, iIncludeObjectMode, fStrength, fDetails, fRadius, fRadiusMap, fTolerance, fSpread, fDistribution, fBias, bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneBaseRampNode : public OctaneNodeBase {
		std::vector<float>  fPosData;
		std::vector<float>  fColorData;
    std::vector<std::string> sTextureData;
    std::vector<std::string> sPositionData;
		OctaneBaseRampNode(int octaneType, std::string pluginType) : OctaneNodeBase(octaneType, pluginType) {}

		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(fPosData, fColorData, sTextureData, sPositionData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneGradientTexture : public OctaneBaseRampNode {
		REFLECTABLE
		(
		(OctaneDTOShader)	sTexture,
		(OctaneDTOEnum)		iInterpolationType
		)

		OctaneGradientTexture() :
			sTexture("Texture"),
			OctaneBaseRampNode(Octane::NT_TEX_GRADIENT, "ShaderNodeOctGradientTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(sTexture, iInterpolationType, MSGPACK_BASE(OctaneBaseRampNode));
	};

	struct OctaneToonRampTexture : public OctaneBaseRampNode {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iInterpolationType
		)

		OctaneToonRampTexture() :
		OctaneBaseRampNode(Octane::NT_TOON_RAMP, "ShaderNodeOctToonRampTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(iInterpolationType, MSGPACK_BASE(OctaneBaseRampNode));
	};

	struct OctaneVolumeRampTexture : public OctaneBaseRampNode {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fMaxGridValue,
		(OctaneDTOEnum)		iInterpolationType
		)

		OctaneVolumeRampTexture() :
			fMaxGridValue("Max grid val."),
			OctaneBaseRampNode(Octane::NT_VOLUME_RAMP, "ShaderNodeOctVolumeRampTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(fMaxGridValue, iInterpolationType, MSGPACK_BASE(OctaneBaseRampNode));
	};

	struct OctaneRandomColorTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOInt)		iSeed
		)

		OctaneRandomColorTexture() :
			iSeed("Random Seed"),
			OctaneNodeBase(Octane::NT_TEX_RANDOMCOLOR, "ShaderNodeOctRandomColorTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iSeed, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctanePolygonSideTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOBool)		bInvert
		)

		OctanePolygonSideTexture() :
			bInvert("Invert"),
			OctaneNodeBase(Octane::NT_TEX_SIDE, "ShaderNodeOctPolygonSideTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneChaosTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sTexture,
		(OctaneDTOInt)		iResolutionX,
		(OctaneDTOInt)		iResolutionY,
		(OctaneDTOInt2)		i2Resolution,
		(OctaneDTOFloat)	fTileScale,
		(OctaneDTOFloat)	fCoverage,
		(OctaneDTOFloat)	fBlendingExponent,
		(OctaneDTOBool)		bHistogramInvariant,
		(OctaneDTOBool)		bShowTileStructure,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOBool)		bEnableRotation,
		(OctaneDTOInt)		iRotationSeed,
		(OctaneDTOInt)		iMaxRotation
		)

		OctaneChaosTexture() :
			sTexture("Texture"),
			iResolutionX("Resolution X"),
			iResolutionY("Resolution Y"),
			fTileScale("Tile scale"),
			fCoverage("Coverage"),
			fBlendingExponent("Blend exponent"),
			bHistogramInvariant("Histogram invariant blending"),
			bShowTileStructure("Show tile structure"),
			tTransform("UV transform"),
			bEnableRotation("Enable rotation"),
			iRotationSeed("Rotation seed"),
			iMaxRotation("Max rotation"),
			OctaneNodeBase(Octane::NT_TEX_CHAOS, "ShaderNodeOctChaosTex")
		{
		}

		void PackAttributes() {
			i2Resolution.iVal.x = iResolutionX.iVal;
			i2Resolution.iVal.y = iResolutionY.iVal;
		}

		void UnpackAttributes() {
			iResolutionX.iVal = i2Resolution.iVal.x;
			iResolutionY.iVal = i2Resolution.iVal.y;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sTexture, i2Resolution, fTileScale, fCoverage, fBlendingExponent, bHistogramInvariant,
			bShowTileStructure, tTransform, bEnableRotation, iRotationSeed, iMaxRotation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneChannelInverterTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sInput,
		(OctaneDTOBool)		bInvertRedChannel,
		(OctaneDTOBool)		bInvertGreenChannel,
		(OctaneDTOBool)		bInvertBlueChannel
		)

		OctaneChannelInverterTexture() :
			sInput("Input"),
			bInvertRedChannel("Invert red channel"),
			bInvertGreenChannel("Invert green channel"),
			bInvertBlueChannel("Invert blue channel"),
			OctaneNodeBase(Octane::NT_TEX_CHANNEL_INVERT, "ShaderNodeOctChannelInverterTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, bInvertRedChannel, bInvertGreenChannel, bInvertBlueChannel, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneChannelMapperTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sInput,
		(OctaneDTOInt)		iRedChannelIndex,
		(OctaneDTOInt)		iGreenChannelIndex,
		(OctaneDTOInt)		iBlueChannelIndex
		)

		OctaneChannelMapperTexture() :
			sInput("Input"),
			iRedChannelIndex("Red channel index"),
			iGreenChannelIndex("Green channel index"),
			iBlueChannelIndex("Blue channel index"),
			OctaneNodeBase(Octane::NT_TEX_CHANNEL_MAP, "ShaderNodeOctChannelMapperTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, iRedChannelIndex, iGreenChannelIndex, iBlueChannelIndex, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneChannelMergerTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sRedChannel,
		(OctaneDTOShader)	sGreenChannel,
		(OctaneDTOShader)	sBlueChannel
		)

		OctaneChannelMergerTexture() :
			sRedChannel("Red channel"),
			sGreenChannel("Green channel"),
			sBlueChannel("Blue channel"),
			OctaneNodeBase(Octane::NT_TEX_CHANNEL_MERGE, "ShaderNodeOctChannelMergerTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sRedChannel, sGreenChannel, sBlueChannel, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneChannelPickerTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sInput,
		(OctaneDTOEnum)		iChannel
		)

		OctaneChannelPickerTexture() :
			sInput("Input"),
			iChannel("channel", false),
			OctaneNodeBase(Octane::NT_TEX_CHANNEL_PICK, "ShaderNodeOctChannelPickerTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, iChannel, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneRaySwitchTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fCameraRay,
		(OctaneDTOFloat)	fShadowRay,
		(OctaneDTOFloat)	fDiffuseRay,
		(OctaneDTOFloat)	fReflectionRay,
		(OctaneDTOFloat)	fRefractionRay,
		(OctaneDTOFloat)	fAORay
		)

		OctaneRaySwitchTexture() :
			fCameraRay("Camera ray"),
			fShadowRay("Shadow ray"),
			fDiffuseRay("Diffuse ray"),
			fReflectionRay("Reflection ray"),
			fRefractionRay("Refraction ray"),
			fAORay("AO ray"),
			OctaneNodeBase(Octane::NT_TEX_RAY_SWITCH, "ShaderNodeOctRaySwitchTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fCameraRay, fShadowRay, fDiffuseRay, fReflectionRay, fRefractionRay, fAORay, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSpotlightTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iOrientation,
		(OctaneDTOFloat3)	f3DirectionOfTarget,
		(OctaneDTOFloat)	fConeAngle,
		(OctaneDTOFloat)	fHardness
		)

		OctaneSpotlightTexture() :
			iOrientation("orientation", false),
			f3DirectionOfTarget("Direction of target"),
			fConeAngle("Cone angle"),
			fHardness("Hardness"),
			OctaneNodeBase(Octane::NT_TEX_SPOTLIGHT, "ShaderNodeOctSpotlightTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iOrientation, f3DirectionOfTarget, fConeAngle, fHardness, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCompositeLayerTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	sInput,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOEnum)		iBlendMode,
		(OctaneDTOEnum)		iOverlayMode,
		(OctaneDTOEnum)		iAlphaOperationMode
		)

		OctaneCompositeLayerTexture() :
			sInput("Input"),
			fOpacity("Opacity"),
			iBlendMode("blend_mode", false),
			iOverlayMode("overlay_mode", false),
			iAlphaOperationMode("alpha_operation_mode", false),
			OctaneNodeBase(Octane::NT_TEX_COMPOSITE_LAYER, "ShaderNodeOctCompositeLayerTex")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, fOpacity, iBlendMode, iOverlayMode, iAlphaOperationMode, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCompositeTexture : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOBool)		bClamp
		)
		std::vector<std::string>	sLayers;

		OctaneCompositeTexture() :
			bClamp("Clamp"),
			OctaneNodeBase(Octane::NT_TEX_COMPOSITE, "ShaderNodeOctCompositeTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(bClamp, sLayers, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneDisplacementTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	tTexture,
		(OctaneDTOFloat)	fMidLevel,
		(OctaneDTOEnum)		iDetailsLevel,		
		(OctaneDTOFloat)	fHeight,
		(OctaneDTOEnum)		iDisplacementDirectionType,
		(OctaneDTOEnum)		iFilterType,
		(OctaneDTOInt)		iFilterRadius
		)

		OctaneDisplacementTexture() :
			tTexture("Texture"),
			fMidLevel("Mid level"),
			iDetailsLevel("displacement_level", false),			
			fHeight("Height"),
			iDisplacementDirectionType("displacement_surface", false),
			iFilterType("displacement_filter", false),
			iFilterRadius("Filter radius"),
			OctaneNodeBase(Octane::NT_DISPLACEMENT, "ShaderNodeOctDisplacementTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(tTexture, fMidLevel, iDetailsLevel, fMidLevel, fHeight, iDisplacementDirectionType, iFilterType, iFilterRadius, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDisplacementTexture

	struct OctaneVertexDisplacementTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	tTexture,
		(OctaneDTOFloat)	fMidLevel,	
		(OctaneDTOFloat)	fHeight,		
		(OctaneDTOEnum)		iMapType,	
		(OctaneDTOEnum)		iVertexSpace,
		(OctaneDTOBool)		bAutoBumpMap,
		(OctaneDTOInt)		iSubdivisionLevel
		)

		OctaneVertexDisplacementTexture() :
			tTexture("Texture"),
			fHeight("Height"),
			fMidLevel("Mid level"),
			iMapType("map_type", false),
			iVertexSpace("vertex_space", false),
			bAutoBumpMap("Auto bump map"),
			iSubdivisionLevel("Subdivision level"),
			OctaneNodeBase(Octane::NT_VERTEX_DISPLACEMENT, "ShaderNodeOctVertexDisplacementTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(tTexture, fHeight, fMidLevel, iMapType, iVertexSpace, bAutoBumpMap, iSubdivisionLevel, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneVertexDisplacementTexture

	struct OctaneVertexDisplacementMixer : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string>	sDisplacements;
		std::vector<std::string>	sWeightLinks;
		std::vector<float>			fWeights;

		OctaneVertexDisplacementMixer() :
			OctaneNodeBase(Octane::NT_VERTEX_DISPLACEMENT_MIXER, "ShaderNodeOctVertexDisplacementMixerTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(sDisplacements, sWeightLinks, fWeights, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneVertexDisplacementMixer

	struct OctaneBakingTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOBool)		bEnableBaking,
		(OctaneDTOInt2)		iResolution,
		(OctaneDTOInt)		iResolutionX,
		(OctaneDTOInt)		iResolutionY,
		(OctaneDTOInt)		iSamplePerPixel,
		(OctaneDTOEnum)		iTextureType,
		(OctaneDTOBool)		bRGBBaking,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderModeU,
		(OctaneDTOEnum)		iBorderModeV
		)

		OctaneBakingTexture() :
			fTexture("Texture"),
			bEnableBaking("Enable baking"),
			iResolutionX("Resolution Width"),
			iResolutionY("Resolution Height"),
			iSamplePerPixel("Samples per pixel"),
			iTextureType("texture_type", false),
			bRGBBaking("RGB baking"),
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderModeU("border_mode_u", false),
			iBorderModeV("border_mode_v", false),
			OctaneNodeBase(Octane::NT_TEX_BAKED_IMAGE, "ShaderNodeOctBakingTex")
		{
		}

		void PackAttributes() {
			iResolution.iVal.x = iResolutionX.iVal;
			iResolution.iVal.y = iResolutionY.iVal;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, bEnableBaking, iResolution, iResolutionX, iResolutionY, iSamplePerPixel, iTextureType, bRGBBaking, fPower, fGamma, bInvert, tTransform, tProjection, iBorderModeU, iBorderModeV, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneUVWTransformTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOShader)	sTransform	
		)

		OctaneUVWTransformTexture() :
			fTexture("Texture"),
			sTransform("Transform"),
			OctaneNodeBase(Octane::NT_TEX_UVW_TRANSFORM, "ShaderNodeOctUVWTransformTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInstaceRangeTexture : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iMaximumID,
		(OctaneDTOBool)		bInvert
		)

		OctaneInstaceRangeTexture() :
			iMaximumID("Maximum ID"),
			bInvert("Invert"),
			OctaneNodeBase(Octane::NT_TEX_INSTANCE_RANGE, "ShaderNodeOctInstanceRangeTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iMaximumID, bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneWTexture : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneWTexture() :
			OctaneNodeBase(Octane::NT_TEX_W, "ShaderNodeOctWTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneBlackBodyEmission : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTextureOrEff,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOBool)		bSurfaceBrightness,
		(OctaneDTOBool)		bKeepInstancePower,
		(OctaneDTOBool)		bDoubeSided,
		(OctaneDTOFloat)	fTemperature,
		(OctaneDTOBool)		bNormalized,
		(OctaneDTOFloat)	fDistribution,
		(OctaneDTOFloat)	fSampleRate,
		(OctaneDTOInt)		iLightPassID,
		(OctaneDTOBool)		bVisibleOnDiffuse,
		(OctaneDTOBool)		bVisibleOnSpecular,
		(OctaneDTOBool)		bTransparentEmission,
		(OctaneDTOBool)		bCastShadow
		)

		OctaneBlackBodyEmission() :
			fTextureOrEff("Texture"),
			fPower("Power"),
			bSurfaceBrightness("Surface brightness"),
			bKeepInstancePower("Keep instance power"),
			bDoubeSided("Double-sided"),
			fTemperature("Temperature"),
			bNormalized("Normalize"),
			fDistribution("Distribution"),
			fSampleRate("Sampling Rate"),
			iLightPassID("Ligth pass ID"),
			bVisibleOnDiffuse("Visible on diffuse"),
			bVisibleOnSpecular("Visible on specular"),
			bTransparentEmission("Transparent emission"),
			bCastShadow("Cast shadows"),
			OctaneNodeBase(Octane::NT_EMIS_BLACKBODY, "ShaderNodeOctBlackBodyEmission")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTextureOrEff, fPower, bSurfaceBrightness, bKeepInstancePower, bDoubeSided, fTemperature, bNormalized, fDistribution, fSampleRate, iLightPassID, bVisibleOnDiffuse, bVisibleOnSpecular, bTransparentEmission, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneBlackBodyEmission

	struct OctaneTextureEmission : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOFloat)	fPower,
		(OctaneDTOBool)		bSurfaceBrightness,
		(OctaneDTOBool)		bKeepInstancePower,
		(OctaneDTOBool)		bDoubeSided,
		(OctaneDTOFloat)	fDistribution,
		(OctaneDTOFloat)	fSampleRate,
		(OctaneDTOInt)		iLightPassID,
		(OctaneDTOBool)		bVisibleOnDiffuse,
		(OctaneDTOBool)		bVisibleOnSpecular,
		(OctaneDTOBool)		bTransparentEmission,
		(OctaneDTOBool)		bCastShadow
		)

		OctaneTextureEmission() :
			fTexture("Texture"),
			fPower("Power"),
			bSurfaceBrightness("Surface brightness"),
			bKeepInstancePower("Keep instance power"),
			bDoubeSided("Double-sided"),
			fDistribution("Distribution"),
			fSampleRate("Sampling Rate"),
			iLightPassID("Ligth pass ID"),
			bVisibleOnDiffuse("Visible on diffuse"),
			bVisibleOnSpecular("Visible on specular"),
			bTransparentEmission("Transparent emission"),
			bCastShadow("Cast shadows"),
			OctaneNodeBase(Octane::NT_EMIS_TEXTURE, "ShaderNodeOctTextureEmission")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, fPower, bSurfaceBrightness, bKeepInstancePower, bDoubeSided, fDistribution, fSampleRate, iLightPassID, bVisibleOnDiffuse, bVisibleOnSpecular, bTransparentEmission, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneTextureEmission

	struct OctaneToonPointLight : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)		fTexture,
		(OctaneDTOFloat)		fPower,
		(OctaneDTOInt)			iLightPassID,
		(OctaneDTOBool)			bCastShadow
		)

		OctaneToonPointLight() :
			fTexture("Texture"),
			fPower("Power"),
			iLightPassID("Light pass ID"),
			bCastShadow("Cast shadows"),
			OctaneNodeBase(Octane::NT_TOON_POINT_LIGHT, "ShaderNodeOctToonPointLight")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, fPower, iLightPassID, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneToonDirectionalLight : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)		fTexture,
		(OctaneDTOEnum)			iUseLightObjectDirection,
		(OctaneDTOFloat3)		f3SunDirection,
		(OctaneDTOFloat)		fPower,
		(OctaneDTOInt)			iLightPassID,
		(OctaneDTOBool)			bCastShadow
		)

		OctaneToonDirectionalLight() :
			fTexture("Texture"),
			iUseLightObjectDirection("light_direction_type", false),
			f3SunDirection("Sun direction"),
			fPower("Power"),
			iLightPassID("Light pass ID"),
			bCastShadow("Cast shadows"),
			OctaneNodeBase(Octane::NT_TOON_DIRECTIONAL_LIGHT, "ShaderNodeOctToonDirectionLight")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fTexture, f3SunDirection, fPower, iLightPassID, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneSchlick : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fScatteringDirection
		)

		OctaneSchlick() :
			fScatteringDirection("Scattering direction"),
			OctaneNodeBase(Octane::NT_PHASE_SCHLICK, "ShaderNodeOctSchlick")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fScatteringDirection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneAbsorptionMedium : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fAbsorption,
		(OctaneDTOBool)		bInvertAbsorption,
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength,
		(OctaneDTOFloat)	fVolumeShadowRayStepLength,
		(OctaneDTOEnum)		iLockStepLengthMode,
		(OctaneDTOBool)		bLockStepLengthPin,
		(OctaneDTOShader)	sSamplePositionDisplacement
		)

		OctaneAbsorptionMedium() :
			fAbsorption("Absorption Tex"),
			bInvertAbsorption("Invert abs."),
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			fVolumeShadowRayStepLength("Vol. shadow ray step length"),
			iLockStepLengthMode("lock_step_length_mode", false),
			bLockStepLengthPin("Lock step length pins"),
			sSamplePositionDisplacement("Sample position displacement"),
			OctaneNodeBase(Octane::NT_MED_ABSORPTION, "ShaderNodeOctAbsorptionMedium")
		{
		}

		void PackAttributes() {
#ifdef OCTANE_SERVER
			iLockStepLengthMode.iVal = bLockStepLengthPin.bVal ? 1 : 0;
#else
			bLockStepLengthPin.bVal = iLockStepLengthMode.iVal > 0;
			bLockStepLengthPin.bUseLinked = false;
			if (bLockStepLengthPin.bVal) {
				fVolumeShadowRayStepLength.fVal = fVolumeStepLength.fVal;
			}
#endif
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAbsorption, bInvertAbsorption, fDensity, fVolumeStepLength, fVolumeShadowRayStepLength, bLockStepLengthPin, iLockStepLengthMode, sSamplePositionDisplacement, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatteringMedium : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fAbsorption,
		(OctaneDTOBool)		bInvertAbsorption,
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength,
		(OctaneDTORGB)		fScattering,
		(OctaneDTOFloat)	fPhase,
		(OctaneDTOShader)	sEmission,
		(OctaneDTOFloat)	fVolumeShadowRayStepLength,
		(OctaneDTOEnum)		iLockStepLengthMode,
		(OctaneDTOBool)		bLockStepLengthPin,
		(OctaneDTOShader)	sSamplePositionDisplacement
		)

		OctaneScatteringMedium() :
			fAbsorption("Absorption Tex"),
			bInvertAbsorption("Invert abs."),
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			fScattering("Scattering Tex"),
			fPhase("Phase"),
			sEmission("Emission"),
			fVolumeShadowRayStepLength("Vol. shadow ray step length"),
			iLockStepLengthMode("lock_step_length_mode", false),
			bLockStepLengthPin("Lock step length pins"),
			sSamplePositionDisplacement("Sample position displacement"),
			OctaneNodeBase(Octane::NT_MED_SCATTERING, "ShaderNodeOctScatteringMedium")
		{
		}

		void PackAttributes() {
#ifdef OCTANE_SERVER
			iLockStepLengthMode.iVal = bLockStepLengthPin.bVal ? 1 : 0;
#else
			bLockStepLengthPin.bVal = iLockStepLengthMode.iVal > 0;
			bLockStepLengthPin.bUseLinked = false;
			if (bLockStepLengthPin.bVal) {
				fVolumeShadowRayStepLength.fVal = fVolumeStepLength.fVal;
			}
#endif
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAbsorption, bInvertAbsorption, fDensity, fVolumeStepLength, fScattering, fPhase, sEmission, fVolumeShadowRayStepLength, iLockStepLengthMode, bLockStepLengthPin, sSamplePositionDisplacement, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneVolumeMedium : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTORGB)		fAbsorption,
		(OctaneDTOShader)	sAbsorptionRamp,
		(OctaneDTOBool)		bInvertAbsorption,
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength,
		(OctaneDTORGB)		fScattering,
		(OctaneDTOShader)	sScatteringRamp,
		(OctaneDTOFloat)	fPhase,
		(OctaneDTOShader)	sEmission,
		(OctaneDTOShader)	sEmissionRamp,
		(OctaneDTOFloat)	fVolumeShadowRayStepLength,
		(OctaneDTOEnum)		iLockStepLengthMode,
		(OctaneDTOBool)		bLockStepLengthPin,
		(OctaneDTOShader)	sSamplePositionDisplacement
		)

		OctaneVolumeMedium() :
			fAbsorption("Absorption Tex"),
			sAbsorptionRamp("Abs. ramp"),
			bInvertAbsorption("Invert abs."),
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			fScattering("Scattering Tex"),
			sScatteringRamp("Scat. ramp"),
			fPhase("Phase"),
			sEmission("Emission"),
			sEmissionRamp("Emiss. ramp"),
			fVolumeShadowRayStepLength("Vol. shadow ray step length"),
			iLockStepLengthMode("lock_step_length_mode", false),
			bLockStepLengthPin("Lock step length pins"),
			sSamplePositionDisplacement("Sample position displacement"),
			OctaneNodeBase(Octane::NT_MED_VOLUME, "ShaderNodeOctVolumeMedium")
		{
		}

		void PackAttributes() {
#ifdef OCTANE_SERVER
			iLockStepLengthMode.iVal = bLockStepLengthPin.bVal ? 1 : 0;
#else
			bLockStepLengthPin.bVal = iLockStepLengthMode.iVal > 0;
			bLockStepLengthPin.bUseLinked = false;
			if (bLockStepLengthPin.bVal) {
				fVolumeShadowRayStepLength.fVal = fVolumeStepLength.fVal;
			}
#endif
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fAbsorption, sAbsorptionRamp, bInvertAbsorption, fDensity, fVolumeStepLength, fScattering, sScatteringRamp, fPhase, sEmission, sEmissionRamp, fVolumeShadowRayStepLength, bLockStepLengthPin, iLockStepLengthMode, sSamplePositionDisplacement, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneRandomWalkMedium : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength,
		(OctaneDTOFloat)	fVolumeShadowRayStepLength,
		(OctaneDTOEnum)		iLockStepLengthMode,
		(OctaneDTOBool)		bLockStepLengthPin,
		(OctaneDTOShader)	sSamplePositionDisplacement,
		(OctaneDTORGB)		fAlbedo,
		(OctaneDTORGB)		fRadius,
		(OctaneDTOFloat)	fBias
		)

		OctaneRandomWalkMedium() :
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			fVolumeShadowRayStepLength("Vol. shadow ray step length"),
			iLockStepLengthMode("lock_step_length_mode", false),
			bLockStepLengthPin("Lock step length pins"),
			sSamplePositionDisplacement("Sample position displacement"),
			fAlbedo("Albedo"),
			fRadius("Radius"),
			fBias("Bias"),
			OctaneNodeBase(Octane::NT_MED_RANDOMWALK, "ShaderNodeOctRandomWalkMedium")
		{
		}

		void PackAttributes() {
#ifdef OCTANE_SERVER
			iLockStepLengthMode.iVal = bLockStepLengthPin.bVal ? 1 : 0;
#else
			bLockStepLengthPin.bVal = iLockStepLengthMode.iVal > 0;
			bLockStepLengthPin.bUseLinked = false;
			if (bLockStepLengthPin.bVal) {
				fVolumeShadowRayStepLength.fVal = fVolumeStepLength.fVal;
			}
#endif
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fDensity, fVolumeStepLength, fVolumeShadowRayStepLength, bLockStepLengthPin, iLockStepLengthMode, sSamplePositionDisplacement, fAlbedo, fRadius, fBias, MSGPACK_BASE(OctaneNodeBase));
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// VALUES
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneFloatValue : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3Value
		)

		OctaneFloatValue() :
			f3Value("Value"),
			OctaneNodeBase(Octane::NT_FLOAT, "ShaderNodeOctFloatValue")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3Value, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneIntValue : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOInt)		iValue
		)

		OctaneIntValue() :
			iValue("Value"),
			OctaneNodeBase(Octane::NT_INT, "ShaderNodeOctIntValue")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iValue, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSunDirection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOFloat)	fLatitude,
		(OctaneDTOFloat)	fLongtitude,		
		(OctaneDTOInt)		iMonth,
		(OctaneDTOInt)		iDay,
		(OctaneDTOFloat)	fLocalTime,
		(OctaneDTOInt)		iGMTOffset
		)

		OctaneSunDirection() :
			fLatitude("Latitude"),
			fLongtitude("Longtitude"),
			iMonth("Month"),
			iDay("Day"),
			fLocalTime("Local time"),
			iGMTOffset("GMT offset"),
			OctaneNodeBase(Octane::NT_SUN_DIRECTION, "ShaderNodeOctSunDirectionValue")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fLatitude, fLongtitude, iMonth, iDay, fLocalTime, iGMTOffset, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSunDirection

	struct OctaneRoundEdges : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iMode,
		(OctaneDTOFloat)	fRadius,
		(OctaneDTOFloat)	fRoundness,
		(OctaneDTOInt)		iSample,
		(OctaneDTOBool)		bConsiderOtherObjects
		)

		OctaneRoundEdges() :
			iMode("round_edges_mode", false),
			fRadius("Radius"),
			fRoundness("Roundness"),
			iSample("Samples"),
			bConsiderOtherObjects("Consider other objects"),
			OctaneNodeBase(Octane::NT_ROUND_EDGES, "ShaderNodeOctRoundEdges")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iMode, fRadius, fRoundness, iSample, bConsiderOtherObjects, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneOCIOInfo : public OctaneNodeBase {
		std::string					sPath;
		bool						bUseOtherConfig;
		bool						bAutomatic;
		int							iIntermediateColorSpaceOctane;
		std::string					sIntermediateColorSpaceOCIO;
		std::vector<std::string>	sRoleNames;
		std::vector<std::string>	sRoleColorSpaceNames;
		std::vector<std::string>	sColorSpaceNames;
		std::vector<std::string>	sColorSpaceFamilyNames;
		std::vector<std::string>	sDisplayNames;
		std::vector<std::string>	sDisplayViewNames;
		std::vector<std::string>	sLookNames;

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		OctaneOCIOInfo() : OctaneNodeBase(Octane::ENT_OCIO_INFO, "OCIOInfo", 0, 1) {
			sPath = "";
			bUseOtherConfig = false;
			bAutomatic = false;
			iIntermediateColorSpaceOctane = 0;
			sIntermediateColorSpaceOCIO = "";
			sRoleNames.clear();
			sRoleColorSpaceNames.clear();
			sColorSpaceNames.clear();
			sColorSpaceFamilyNames.clear();
			sDisplayNames.clear();
			sDisplayViewNames.clear();
			sLookNames.clear();
		}
		MSGPACK_DEFINE(sPath, bUseOtherConfig, bAutomatic, iIntermediateColorSpaceOctane, sIntermediateColorSpaceOCIO, sRoleNames, sRoleColorSpaceNames, sColorSpaceNames, sColorSpaceFamilyNames, sDisplayNames, sDisplayViewNames, sLookNames, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneAovOutputGroup : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string>	sGroups;

		OctaneAovOutputGroup() :
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_GROUP, "ShaderNodeOctAovOutputGroup")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(sGroups, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneAovOutputGroup

	struct OctaneColorAovOutput : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOFloat3)		f3Color,
		(OctaneDTOFloat)		fAlpha
		)

		OctaneColorAovOutput() :
			f3Color("Color"),
			fAlpha("Alpha"),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_COLOR, "ShaderNodeOctColorAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3Color, fAlpha, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneColorAovOutput

	struct OctaneCompositeAovOutput : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOBool)		bEnableImager,
		(OctaneDTOBool)		bEnablePostProcessing
		)
		std::vector<std::string>	sLayers;

		OctaneCompositeAovOutput() :
			bEnableImager("Enable imager"),
			bEnablePostProcessing("Enable post processing"),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_COMPOSITE, "ShaderNodeOctCompositeAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		MSGPACK_DEFINE(bEnableImager, bEnablePostProcessing, sLayers, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCompositeAovOutput

	struct OctaneCompositeAovOutputLayer : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOBool)		bEnable,
		(OctaneDTOShader)	sInput,
		(OctaneDTOShader)	sMask,
		(OctaneDTOEnum)		iMaskChannel,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOFloat)	fScale,
		(OctaneDTOFloat3)	f3ColorMultiplier,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOEnum)		iBlendMode,
		(OctaneDTOEnum)		iAlphaOperation
		)

		OctaneCompositeAovOutputLayer() :
			bEnable("Enable"),
			sInput("Input"),
			sMask("Mask"),
			iMaskChannel("mask_channel", false),
			bInvert("Invert"),
			fScale("Scale"),
			f3ColorMultiplier("Color multiplier"),
			fOpacity("Opacity"),
			iBlendMode("blend_mode", false),
			iAlphaOperation("alpha_operation", false),
			OctaneNodeBase(Octane::NT_COMPOSITE_AOV_LAYER, "ShaderNodeOctCompositeAovOutputLayer")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnable, sInput, sMask, iMaskChannel, bInvert, fScale, f3ColorMultiplier, fOpacity, iBlendMode, iAlphaOperation, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCompositeAovOutputLayer

	struct OctaneImageAovOutput : public OctaneBaseImageNode {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iColorSpace,
		(OctaneDTOEnum)		iOutputChannels,
		(OctaneDTOBool)		bPreMultiplyAlpha,
		(OctaneDTOBool)		bEnableImager,
		(OctaneDTOBool)		bEnablePostProcessing
		)

		OctaneImageAovOutput() :
			iColorSpace("color_space", false),
			iOutputChannels("output_channel", false),
			bPreMultiplyAlpha("Pre multiply alpha"),
			bEnableImager("Enable imager"),
			bEnablePostProcessing("Enable post processing"),
			OctaneBaseImageNode(Octane::NT_OUTPUT_AOV_IMAGE, "ShaderNodeOctImageAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iColorSpace, iOutputChannels, bPreMultiplyAlpha, bEnableImager, bEnablePostProcessing, MSGPACK_BASE(OctaneBaseImageNode));
	}; //struct OctaneImageAovOutput

	struct OctaneRenderAovOutput : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iInput,
		(OctaneDTOEnum)		iOutputChannels,
		(OctaneDTOBool)		bEnableImager,
		(OctaneDTOBool)		bEnablePostProcessing
		)

		OctaneRenderAovOutput() :
			iInput("input", false),
			iOutputChannels("output_channel", false),
			bEnableImager("Enable imager"),
			bEnablePostProcessing("Enable post processing"),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_RENDER, "ShaderNodeOctRenderAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iInput, iOutputChannels, bEnableImager, bEnablePostProcessing, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneRenderAovOutput

	struct OctaneReadVDBTexture : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOEnum)		iGridID,
		(OctaneDTOShader)	sVDB,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection
		)

		OctaneReadVDBTexture() :
			iGridID("grid_id", false),
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_READ_VDB, "ShaderNodeOctReadVDBTex")
		{
			sVDB = "";
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iGridID, sVDB, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneClippingMaterial : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnabled,
		(OctaneDTOShader)	sIntersection,
		(OctaneDTOInt)		iPriority
		)

		OctaneClippingMaterial() :
			bEnabled("Enabled"),
			sIntersection("Intersection"),
			iPriority("Priority"),
			OctaneNodeBase(Octane::NT_MAT_CLIPPING, "ShaderNodeOctClippingMat")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnabled, sIntersection, iPriority, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneClippingMaterial

	struct OctaneCaptureToCutomAOVTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)		sCaptureTexture,
		(OctaneDTOEnum)			iCustomAOV,
		(OctaneDTOShader)		sOverrideTexture
		)

		OctaneCaptureToCutomAOVTexture() :
			sCaptureTexture("Capture texture"),
			iCustomAOV("custom_aov", false),
			sOverrideTexture("Override texture"),
			OctaneNodeBase(Octane::NT_TEX_CAPTURE, "ShaderNodeOctCaptureToCustomAOVTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sCaptureTexture, iCustomAOV, sOverrideTexture, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCaptureToCutomAOVTexture

	struct OctaneSurfaceTangentDPduTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneSurfaceTangentDPduTexture() :
			OctaneNodeBase(Octane::NT_TEX_DPDU, "ShaderNodeOctSurfaceTangentDPduTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSurfaceTangentDPduTexture

	struct OctaneSurfaceTangentDPdvTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneSurfaceTangentDPdvTexture() :
			OctaneNodeBase(Octane::NT_TEX_DPDV, "ShaderNodeOctSurfaceTangentDPdvTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSurfaceTangentDPdvTexture

	struct OctaneFloatToGreyscaleTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fValue
		)

		OctaneFloatToGreyscaleTexture() :
			fValue("Value"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT_TO_GREYSCALE, "ShaderNodeOctFloatToGreyscaleTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fValue, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneFloatToGreyscaleTexture

	struct OctaneFloat3ToColorTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3Values
		)

		OctaneFloat3ToColorTexture() :
			f3Values("Values"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT3_TO_COLOR, "ShaderNodeOctFloat3ToColorTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(f3Values, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneFloat3ToColorTexture

	struct OctaneFloatsToColorTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fR,
		(OctaneDTOFloat)	fG,
		(OctaneDTOFloat)	fB
		)

		OctaneFloatsToColorTexture() :
			fR("R"),
			fG("G"),
			fB("B"),
			OctaneNodeBase(Octane::NT_TEX_FLOATS_TO_COLOR, "ShaderNodeOctFloatsToColorTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fR, fG, fB, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneFloatsToColorTexture

	struct OctaneGradientGeneratorTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOEnum)		iGradientType,
		(OctaneDTOFloat)	fRepetitions,
		(OctaneDTOInt)		iPolygonSides,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection,
		(OctaneDTOEnum)		iRepetitionMode
		)

		OctaneGradientGeneratorTexture() :
			iGradientType("gradient_type", false),
			fRepetitions("Repetitions"),
			iPolygonSides("Polygon sides"),
			fGamma("Gamma"),
			bInvert("Invert"),
			sTransform("Transform"),
			sProjection("Projection"),
			iRepetitionMode("repetition_mode", false),
			OctaneNodeBase(Octane::NT_TEX_GRADIENT_GENERATOR, "ShaderNodeOctGradientGeneratorTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iGradientType, fRepetitions, iPolygonSides, fGamma, 
			bInvert, sTransform, sProjection, iRepetitionMode, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneGradientGeneratorTexture

	struct OctaneUVCoordinateTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	sProjection,
		(OctaneDTOFloat)	fUVMax
		)

		OctaneUVCoordinateTexture() :
			sProjection("Projection"),
			fUVMax("UV max"),
			OctaneNodeBase(Octane::NT_TEX_UV, "ShaderNodeOctUVCoordinateTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sProjection, fUVMax, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneUVCoordinateTexture

	struct OctaneBinaryMathOperationTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	sArugumentA,
		(OctaneDTOShader)	sArugumentB,
		(OctaneDTOEnum)		iOperation
		)

		OctaneBinaryMathOperationTexture() :
			sArugumentA("Argument A"),
			sArugumentB("Argument B"),
			iOperation("operation", false),
			OctaneNodeBase(Octane::NT_TEX_MATH_BINARY, "ShaderNodeOctBinaryMathOperationTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sArugumentA, sArugumentB, iOperation, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneBinaryMathOperationTexture

	struct OctaneUnaryMathOperationTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	sArugument,
		(OctaneDTOEnum)		iOperation
		)

		OctaneUnaryMathOperationTexture() :
			sArugument("Argument"),
			iOperation("operation", false),
			OctaneNodeBase(Octane::NT_TEX_MATH_UNARY, "ShaderNodeOctUnaryMathOperationTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sArugument, iOperation, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneUnaryMathOperationTexture

	struct OctaneNormalTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOEnum)		iNormalType,
		(OctaneDTOEnum)		iCoordinateSystem,
		(OctaneDTOBool)		bNormalizeResult
		)

		OctaneNormalTexture() :
			iNormalType("normal_type", false),
			iCoordinateSystem("coordinate_system", false),
			bNormalizeResult("Normalize result"),
			OctaneNodeBase(Octane::NT_TEX_NORMAL, "ShaderNodeOctNormalTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iNormalType, iCoordinateSystem, bNormalizeResult, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneNormalTexture

	struct OctanePositionTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOEnum)		iCoordinateSystem
		)

		OctanePositionTexture() :
			iCoordinateSystem("coordinate_system", false),
			OctaneNodeBase(Octane::NT_TEX_POSITION, "ShaderNodeOctPositionTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSystem, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctanePositionTexture

	struct OctaneZDepthTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOBool)		bNormalizeResult,
		(OctaneDTOFloat)	fNormalizationRangeX,
		(OctaneDTOFloat)	fNormalizationRangeY,
		(OctaneDTOFloat2)	f2NormalizationRange
		)

		OctaneZDepthTexture() :
			bNormalizeResult("Normalize result"),
			fNormalizationRangeX("Normalization range X"),
			fNormalizationRangeY("Normalization range Y"),
			OctaneNodeBase(Octane::NT_TEX_Z_DEPTH, "ShaderNodeOctZDepthTex")
		{
		}

		void PackAttributes() {
			f2NormalizationRange.fVal.x = fNormalizationRangeX.fVal;
			f2NormalizationRange.fVal.y = fNormalizationRangeY.fVal;
		}

		void UnpackAttributes() {
			fNormalizationRangeX.fVal = f2NormalizationRange.fVal.x;
			fNormalizationRangeY.fVal = f2NormalizationRange.fVal.y;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bNormalizeResult, f2NormalizationRange, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneZDepthTexture

	struct OctaneSamplePositionTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneSamplePositionTexture() :
			OctaneNodeBase(Octane::NT_TEX_SAMPLE_POSITION, "ShaderNodeOctSamplePositionTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSamplePositionTexture

	struct OctaneRelativeDistanceTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOEnum)		iDistanceMode,
		(OctaneDTOShader)	sReferenceTransform,
		(OctaneDTOBool)		bUseFullTransform,
		(OctaneDTOBool)		bNormalizeResult,
		(OctaneDTOFloat)	fNormalizationRangeX,
		(OctaneDTOFloat)	fNormalizationRangeY,
		(OctaneDTOFloat2)	f2NormalizationRange
		)

		OctaneRelativeDistanceTexture() :
			iDistanceMode("distance_mode", false),
			sReferenceTransform("Reference transform"),
			bUseFullTransform("Use full transform"),
			bNormalizeResult("Normalize result"),
			fNormalizationRangeX("Normalization range X"),
			fNormalizationRangeY("Normalization range Y"),
			OctaneNodeBase(Octane::NT_TEX_RELATIVE_DISTANCE, "ShaderNodeOctRelativeDistanceTex")
		{
		}

		void PackAttributes() {
			f2NormalizationRange.fVal.x = fNormalizationRangeX.fVal;
			f2NormalizationRange.fVal.y = fNormalizationRangeY.fVal;
		}

		void UnpackAttributes() {
			fNormalizationRangeX.fVal = f2NormalizationRange.fVal.x;
			fNormalizationRangeY.fVal = f2NormalizationRange.fVal.y;
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iDistanceMode, sReferenceTransform, bUseFullTransform,
			bNormalizeResult, f2NormalizationRange, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneRelativeDistanceTexture

	struct OctaneRayDirectionTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOBool)		bViewDirection,
		(OctaneDTOEnum)		iCoordinateSystem,
		(OctaneDTOBool)		bNormalizeResult
		)

		OctaneRayDirectionTexture() :
			bViewDirection("View direction"),
			iCoordinateSystem("coordinate_system", false),
			bNormalizeResult("Normalize result"),
			OctaneNodeBase(Octane::NT_TEX_RAY_DIRECTION, "ShaderNodeOctRayDirectionTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bViewDirection, iCoordinateSystem, bNormalizeResult, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneRayDirectionTexture

	struct OctaneRandomMapTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	sInputTexture,
		(OctaneDTOInt)		iInputScale,
		(OctaneDTOEnum)		iNoiseFunction
		)

		OctaneRandomMapTexture() :
			sInputTexture("Input texture"),
			iInputScale("Input scale"),
			iNoiseFunction("noise_function", false),
			OctaneNodeBase(Octane::NT_TEX_RANDOM_MAP, "ShaderNodeOctRandomMapTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInputTexture, iInputScale, iNoiseFunction, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneRandomMapTexture

	struct OctaneRangeTexture : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOShader)	sValue,
		(OctaneDTOEnum)		iInterpolation,
		(OctaneDTOFloat)	fInputMin,
		(OctaneDTOFloat)	fInputMax,
		(OctaneDTOFloat)	fOutputMin,
		(OctaneDTOFloat)	fOutputMax,
		(OctaneDTOInt)		iSteps,
		(OctaneDTOBool)		bClamp
		)

		OctaneRangeTexture() :
			sValue("Value"),
			iInterpolation("interpolation", false),
			fInputMin("Input min"),
			fInputMax("Input max"),
			fOutputMin("Output min"),
			fOutputMax("Output max"),
			iSteps("Steps"),
			bClamp("Clamp"),
			OctaneNodeBase(Octane::NT_TEX_RANGE, "ShaderNodeOctRangeTex")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sValue, iInterpolation, fInputMin, fInputMax, fOutputMin, fOutputMax, 
			iSteps, bClamp, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneRangeTexture

	struct OctaneLightMixingAovOutput : public OctaneNodeBase {
		REFLECTABLE
		(	
		(OctaneDTOBool)		bEnableImager,
		(OctaneDTOBool)		bEnablePostFX,
		(OctaneDTOBool)		bEnableSunlight,
		(OctaneDTOFloat3)	f3TintSunlight,
		(OctaneDTOFloat)	fScaleSunlight,
		(OctaneDTOBool)		bEnableEnvironment,
		(OctaneDTOFloat3)	f3TintEnvironment,
		(OctaneDTOFloat)	fScaleEnvironment,
		(OctaneDTOBool)		bEnableLightID1,
		(OctaneDTOFloat3)	f3TintLightID1,
		(OctaneDTOFloat)	fScaleLightID1,
		(OctaneDTOBool)		bEnableLightID2,
		(OctaneDTOFloat3)	f3TintLightID2,
		(OctaneDTOFloat)	fScaleLightID2,
		(OctaneDTOBool)		bEnableLightID3,
		(OctaneDTOFloat3)	f3TintLightID3,
		(OctaneDTOFloat)	fScaleLightID3,
		(OctaneDTOBool)		bEnableLightID4,
		(OctaneDTOFloat3)	f3TintLightID4,
		(OctaneDTOFloat)	fScaleLightID4,
		(OctaneDTOBool)		bEnableLightID5,
		(OctaneDTOFloat3)	f3TintLightID5,
		(OctaneDTOFloat)	fScaleLightID5,
		(OctaneDTOBool)		bEnableLightID6,
		(OctaneDTOFloat3)	f3TintLightID6,
		(OctaneDTOFloat)	fScaleLightID6,
		(OctaneDTOBool)		bEnableLightID7,
		(OctaneDTOFloat3)	f3TintLightID7,
		(OctaneDTOFloat)	fScaleLightID7,
		(OctaneDTOBool)		bEnableLightID8,
		(OctaneDTOFloat3)	f3TintLightID8,
		(OctaneDTOFloat)	fScaleLightID8,
		(OctaneDTOInt)		iEnableLightIDMask
		)

		OctaneLightMixingAovOutput() :
			bEnableImager("Enable imager"),
			bEnablePostFX("Enable post FX"),
			bEnableSunlight("Sunlight Enable"),
			f3TintSunlight("Sunlight Tint"),
			fScaleSunlight("Sunlight Scale"),
			bEnableEnvironment("Environment Enable"),
			f3TintEnvironment("Environment Tint"),
			fScaleEnvironment("Environment Scale"),
			bEnableLightID1("LightID 1 Enable"),
			f3TintLightID1("LightID 1 Tint"),
			fScaleLightID1("LightID 1 Scale"),
			bEnableLightID2("LightID 2 Enable"),
			f3TintLightID2("LightID 2 Tint"),
			fScaleLightID2("LightID 2 Scale"),
			bEnableLightID3("LightID 3 Enable"),
			f3TintLightID3("LightID 3 Tint"),
			fScaleLightID3("LightID 3 Scale"),
			bEnableLightID4("LightID 4 Enable"),
			f3TintLightID4("LightID 4 Tint"),
			fScaleLightID4("LightID 4 Scale"),
			bEnableLightID5("LightID 5 Enable"),
			f3TintLightID5("LightID 5 Tint"),
			fScaleLightID5("LightID 5 Scale"),
			bEnableLightID6("LightID 6 Enable"),
			f3TintLightID6("LightID 6 Tint"),
			fScaleLightID6("LightID 6 Scale"),
			bEnableLightID7("LightID 7 Enable"),
			f3TintLightID7("LightID 7 Tint"),
			fScaleLightID7("LightID 7 Scale"),
			bEnableLightID8("LightID 8 Enable"),
			f3TintLightID8("LightID 8 Tint"),
			fScaleLightID8("LightID 8 Scale"),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_LIGHT_MIXING, "ShaderNodeOctLightMixingAovOutput")
		{
		}
		
		void PackAttributes() {
			iEnableLightIDMask.iVal |= ((bEnableLightID1.bVal ? 1 : 0) << 1);
			iEnableLightIDMask.iVal |= ((bEnableLightID2.bVal ? 1 : 0) << 2);
			iEnableLightIDMask.iVal |= ((bEnableLightID3.bVal ? 1 : 0) << 3);
			iEnableLightIDMask.iVal |= ((bEnableLightID4.bVal ? 1 : 0) << 4);
			iEnableLightIDMask.iVal |= ((bEnableLightID5.bVal ? 1 : 0) << 5);
			iEnableLightIDMask.iVal |= ((bEnableLightID6.bVal ? 1 : 0) << 6);
			iEnableLightIDMask.iVal |= ((bEnableLightID7.bVal ? 1 : 0) << 7);
			iEnableLightIDMask.iVal |= ((bEnableLightID8.bVal ? 1 : 0) << 8);
		}

		void UnpackAttributes() {
			bEnableLightID1 = iEnableLightIDMask.iVal & (1 << 1);
			bEnableLightID2 = iEnableLightIDMask.iVal & (1 << 2);
			bEnableLightID3 = iEnableLightIDMask.iVal & (1 << 3);
			bEnableLightID4 = iEnableLightIDMask.iVal & (1 << 4);
			bEnableLightID5 = iEnableLightIDMask.iVal & (1 << 5);
			bEnableLightID6 = iEnableLightIDMask.iVal & (1 << 6);
			bEnableLightID7 = iEnableLightIDMask.iVal & (1 << 7);
			bEnableLightID8 = iEnableLightIDMask.iVal & (1 << 8);
		}
			
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(bEnableImager, bEnablePostFX, 
			bEnableSunlight, f3TintSunlight, fScaleSunlight, 
			bEnableEnvironment, f3TintEnvironment, fScaleEnvironment,
			f3TintLightID1, fScaleLightID1,
			f3TintLightID2, fScaleLightID2,
			f3TintLightID3, fScaleLightID3,
			f3TintLightID4, fScaleLightID4,
			f3TintLightID5, fScaleLightID5,
			f3TintLightID6, fScaleLightID6,
			f3TintLightID7, fScaleLightID7,
			f3TintLightID8, fScaleLightID8,
			iEnableLightIDMask,
			MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneLightMixingAovOutput

	struct OctaneMapRangeAovOutput : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOShader)	sInput,
		(OctaneDTOFloat)	fInputMinimum,
		(OctaneDTOFloat)	fInputMaximum,
		(OctaneDTOFloat)	fOutputMinimum,
		(OctaneDTOFloat)	fOutputMaximum,
		(OctaneDTOBool)		bClamp,
		(OctaneDTOEnum)		iChannels
		)

		OctaneMapRangeAovOutput() :
			sInput("Input"),
			fInputMinimum("Input minimum"),
			fInputMaximum("Input maximum"),
			fOutputMinimum("Output minimum"),
			fOutputMaximum("Output maximum"),
			bClamp("Clamp"),
			iChannels("channel", false),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_MAP_RANGE, "ShaderNodeOctMapRangeAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, fInputMinimum, fInputMaximum, fOutputMinimum, fOutputMaximum,
			bClamp, iChannels,
			MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMapRangeAovOutput

	struct OctaneColorCorrectionAovOutput : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOShader)	sInput,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOFloat)	fHue,
		(OctaneDTOFloat)	fSaturation,
		(OctaneDTOFloat)	fContrast,
		(OctaneDTOFloat)	fGain,		
		(OctaneDTOFloat)	fExposure,
		(OctaneDTOFloat)	fMask
		)

		OctaneColorCorrectionAovOutput() :
			sInput("Input"),
			bInvert("Invert"),
			fHue("Hue"),
			fSaturation("Saturation"),
			fContrast("Contrast"),
			fGain("Gain"),
			fExposure("Exposure"),
			fMask("Mask"),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_COLOR_CORRECTION, "ShaderNodeOctColorCorrectionAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, bInvert, fHue, fSaturation, fContrast, fGain, fExposure, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneColorCorrectionAovOutput

	struct OctaneClampAovOutput : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOShader)	sInput,
		(OctaneDTOFloat)	fMinimum,	
		(OctaneDTOFloat)	fMaximum,
		(OctaneDTOEnum)		iColorChannels
		)

		OctaneClampAovOutput() :
			sInput("Input"),
			fMinimum("Minimum"),
			fMaximum("Maximum"),
			iColorChannels("color_channels", false),
			OctaneNodeBase(Octane::NT_OUTPUT_AOV_CLAMP, "ShaderNodeOctClampAovOutput")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sInput, fMinimum, fMaximum, iColorChannels, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneClampAovOutput

	struct OctaneOcioColorSpace : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOString)	sOcioName
		)

		OctaneOcioColorSpace() :
			OctaneNodeBase(Octane::NT_OCIO_COLOR_SPACE, "OctaneOCIOColorSpace")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(sOcioName, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneOcioColorSpace

	struct OctaneCustomNode : public OctaneNodeBase{
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::string						sClientNodeName;
		int								iOctaneNodeType;
		std::string						sCustomDataHeader;
		std::string						sCustomDataBody;
		std::vector<OctaneDTOBool>		oBoolSockets;
		std::vector<OctaneDTOEnum>		oEnumSockets;
		std::vector<OctaneDTOInt>		oIntSockets;
		std::vector<OctaneDTOInt2>		oInt2Sockets;
		std::vector<OctaneDTOInt3>		oInt3Sockets;
		std::vector<OctaneDTOFloat>		oFloatSockets;
		std::vector<OctaneDTOFloat2>	oFloat2Sockets;
		std::vector<OctaneDTOFloat3>	oFloat3Sockets;
		std::vector<OctaneDTOString>	oStringSockets;
		std::vector<OctaneDTORGB>		oRGBSockets;
		std::vector<OctaneDTOShader>	oLinkSockets;

		OctaneCustomNode() :
			OctaneNodeBase(Octane::ENT_CUSTOM_NODE, "OctaneCustomNode", 0, 1)
		{
			Clear();
		}

		void Clear() {
			sClientNodeName = "";
			iOctaneNodeType = 0;
			sCustomDataHeader = "";
			sCustomDataBody = "";
			oBoolSockets.clear();
			oEnumSockets.clear();
			oIntSockets.clear();
			oInt2Sockets.clear();
			oInt3Sockets.clear();
			oFloatSockets.clear();
			oFloat2Sockets.clear();
			oFloat3Sockets.clear();
			oStringSockets.clear();
			oRGBSockets.clear();
			oLinkSockets.clear();
		}

		bool PreSpecificProcessDispatcher(void* data);
		bool PostSpecificProcessDispatcher(void* data);
		
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		OCTANE_NODE_OCTANEDB_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		MSGPACK_DEFINE(sClientNodeName, iOctaneNodeType, sCustomDataHeader, sCustomDataBody, oBoolSockets, oEnumSockets, oIntSockets, oInt2Sockets, oInt3Sockets,
			oFloatSockets, oFloat2Sockets, oFloat3Sockets, oStringSockets, oRGBSockets, oLinkSockets, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCustomNode
}

#endif
// clang-format on
