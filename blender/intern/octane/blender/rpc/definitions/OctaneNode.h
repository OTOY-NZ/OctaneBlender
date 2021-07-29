// clang-format off
#ifndef __OCTANE_NODE_H__
#define __OCTANE_NODE_H__
#include "OctaneBase.h"
#include "OctanePinInfo.h"
#include "OctaneReflection.h"

#define ENVIRONMENT_NODE_NAME "Environment"
#define VISIBLE_ENVIRONMENT_NODE_NAME "VisibleEnvironment"

namespace OctaneDataTransferObject {

	enum CommandType {
		SHOW_NODEGRAPH = 1,
		SHOW_NETWORK_PREFERENCE = 2,
		STOP_RENDERING = 3,
		SHOW_LOG = 4,
		SHOW_DEVICE_SETTINGS = 5,
		SHOW_LIVEDB = 6,
		SHOW_ACTIVATION = 7,
		SAVE_OCTANDB = 8
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// NODE BASE
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneNodeBase {
		std::string sName;
		Octane::NodeType nodeType;
		const static PacketType packetType;

		OctaneNodeBase(Octane::NodeType _nodeType) : nodeType(_nodeType) {}
		virtual ~OctaneNodeBase() {}		
		virtual void PackAttributes() {}
		virtual void UnpackAttributes() {}
		friend std::ostream& operator<< (std::ostream& out, const OctaneNodeBase& obj);
		MSGPACK_DEFINE(sName, nodeType);		
	}; //struct OctaneNodeBase

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// LIGHTS
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneLightDirection : public OctaneNodeBase {
		const static PacketType packetType = NONE;

		REFLECTABLE
		(		
		(OctaneDTOFloat)	fLatitude,
		(OctaneDTOFloat)	fLongtitude,
		(OctaneDTOFloat)	fLocalTime,
		(OctaneDTOInt)		iMonth,
		(OctaneDTOInt)		iDay,
		(OctaneDTOInt)		iGMTOffset,
		(OctaneDTOBool)		bEnableSunDir,
		(OctaneDTOFloat3)	f3Direction
		)
		OctaneLightDirection() :
			OctaneNodeBase(Octane::NT_UNKNOWN)
		{
		}
		friend std::ostream& operator<< (std::ostream& out, const OctaneLightDirection& obj);
		MSGPACK_DEFINE(fLatitude, fLongtitude, fLocalTime, iMonth, iDay, iGMTOffset, bEnableSunDir, f3Direction, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneLightDirection

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// ENVIRONMENTS
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneEnvironment : public OctaneNodeBase {
		const static PacketType packetType = NONE;
		bool	bUsed;
		OctaneEnvironment(Octane::NodeType _nodeType) : 
			bUsed(true),
			OctaneNodeBase(_nodeType)
		{
		}
		MSGPACK_DEFINE(bUsed, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneEnvironment

	struct OctaneTextureEnvironment : public OctaneEnvironment{
		const static PacketType packetType = LOAD_TEXTURE_ENVIRONMENT;
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
			OctaneEnvironment(Octane::NT_ENV_TEXTURE)
		{
		}
		MSGPACK_DEFINE(fTexture, fPower, bImportanceSampling, tMedium, fMediumRadius, bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};

	struct OctaneDaylightEnvironment : public OctaneEnvironment{
		const static PacketType packetType = LOAD_DAYLIGHT_ENVIRONMENT;
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
			OctaneEnvironment(Octane::NT_ENV_DAYLIGHT)
		{
		}
		MSGPACK_DEFINE(f3SunDirection, fSkyTurbidity, fPower, fNorthOffset, iDaylightModel,
			fSkyColor, fSunsetColor, fSunSize, fGroundColor, fGroundStartAngle, fGroundBlendAngle, tSkyTexture,
			bImportanceSampling, tMedium, fMediumRadius, bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};

	struct OctanePlanetaryEnvironment : public OctaneEnvironment{
		const static PacketType packetType = LOAD_PLANETARY_ENVIRONMENT;
		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3SunDirection,
		(OctaneDTOFloat)	fSkyTurbidity,
		(OctaneDTOFloat)	fPower,
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
			OctaneEnvironment(Octane::NT_ENV_PLANETARY)
		{
		}
		MSGPACK_DEFINE(f3SunDirection, fSkyTurbidity, fPower, fNorthOffset,
			fSunSize, fAltitude, fAltitude, tStarField,
			bImportanceSampling, tMedium, fMediumRadius,
			fLatitude, fLongtitude, fGroundAlbedo, tGroundReflection, tGroundGlossiness, fGroundEmission, tGroundNormalMap, tGroundElevation,
			bVisableEnvBackplate, bVisableReflections, bVisableRefractions, MSGPACK_BASE(OctaneEnvironment));
	};


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
		(OctaneDTOBool)		bAOAlphaShadows
		)
		OctaneDTOInt		iBeautyPasses;
		OctaneDTOInt		iDenoiserPasses;
		OctaneDTOInt		iPostProcessingPasses;
		OctaneDTOInt		iRenderLayerPasses;
		OctaneDTOInt		iLightingPasses;
		OctaneDTOInt		iCryptomattePasses;
		OctaneDTOInt		iInfoPasses;
		OctaneDTOInt		iMaterialPasses;

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
			OctaneNodeBase(Octane::NT_RENDER_PASSES)
		{
			sName = "RenderPasses";
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
				&& iBeautyPasses.iVal == other.iBeautyPasses.iVal
				&& iDenoiserPasses.iVal == other.iDenoiserPasses.iVal
				&& iPostProcessingPasses.iVal == other.iPostProcessingPasses.iVal
				&& iRenderLayerPasses.iVal == other.iRenderLayerPasses.iVal
				&& iLightingPasses.iVal == other.iLightingPasses.iVal
				&& iCryptomattePasses.iVal == other.iCryptomattePasses.iVal
				&& iInfoPasses.iVal == other.iInfoPasses.iVal
				&& iMaterialPasses.iVal == other.iMaterialPasses.iVal;
		}

		MSGPACK_DEFINE(bUsePasses, iPreviewPass, bIncludeEnvironment, iCryptomatteBins, iCryptomatteSeedFactor,
			iMaxInfoSample, iSamplingMode, bBumpAndNormalMapping, fOpacityThreshold, fZDepthMax, fUVMax, iUVCoordinateSelection,
			fMaxSpeed, fAODistance, bAOAlphaShadows,
			iBeautyPasses, iDenoiserPasses, iPostProcessingPasses, iRenderLayerPasses, iLightingPasses, iCryptomattePasses, iInfoPasses, iMaterialPasses,
			MSGPACK_BASE(OctaneNodeBase));
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// BASIC INFO NODE
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	struct OctaneCommand : public OctaneNodeBase {
		const static PacketType packetType = COMMAND;
		int							iCommandType;
		std::vector<int>			iParams;
		std::vector<float>			fParams;
		std::vector<std::string>	sParams;
		OctaneCommand() : iCommandType(iCommandType), OctaneNodeBase(Octane::NT_UNKNOWN) {}
		OctaneCommand(int cmdType, const std::vector<int>& iParams, const std::vector<float>& fParams, const std::vector<std::string>& sParams) :
			iCommandType(cmdType), iParams(iParams), fParams(fParams), sParams(sParams), OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(iCommandType, iParams, fParams, sParams, MSGPACK_BASE(OctaneNodeBase));
	};

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// MATERIALS
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	/// The structure holding a diffuse material data that is going to be uploaded to the Octane server.
	struct OctaneDiffuseMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_DIFFUSE_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTORGB)		fDiffuse,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOFloat)	fTransmission,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOShader)	tEmission,
		(OctaneDTOBool)		bShadowCatcher,
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
			fRoundedEdgeRadius("Edges rounding"),
			fTransmission("Transmission"),
			tMedium("Medium"),
			tEmission("Emission"),
			bShadowCatcher("Shadow catcher"),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_DIFFUSE)
		{
		}
		MSGPACK_DEFINE(fDiffuse, fRoughness, sBump, tNormal, tDisplacement, fOpacity, bSmooth, fRoundedEdgeRadius, fTransmission, tMedium, tEmission, bShadowCatcher, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDiffuseMaterial

	struct OctaneMixMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_MIX_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTOFloat)	fAmount,
		(OctaneDTOShader)	tMaterial1,
		(OctaneDTOShader)	tMaterial2,
		(OctaneDTOShader)	tDisplacement
		)

		OctaneMixMaterial() :
			fAmount("Amount"),
			tMaterial1("Material1"),
			tMaterial2("Material2"),
			tDisplacement("Displacement"),
			OctaneNodeBase(Octane::NT_MAT_MIX)
		{
		}
		MSGPACK_DEFINE(fAmount, tMaterial1, tMaterial2, tDisplacement, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMixMaterial

	struct OctanePortalMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_PORTAL_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnabled
		)

		OctanePortalMaterial() :
			bEnabled("Enabled"),
			OctaneNodeBase(Octane::NT_MAT_PORTAL)
		{
		}
		MSGPACK_DEFINE(bEnabled, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctanePortalMaterial

	struct OctaneGlossyMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_GLOSSY_MATERIAL;
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
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOFloat)	fRoundedEdgeRadius,		
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
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
			sBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			fRoundedEdgeRadius("Edges rounding"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_GLOSSY)
		{
		}
		MSGPACK_DEFINE(fDiffuse, fSpecular, iBRDFModel, fRoughness, fAnisotropy, fRotation, fSheen, fSheenRoughness, fIndexOfReflection, sBump, tNormal, tDisplacement, fOpacity, bSmooth, fRoundedEdgeRadius, fFilmWidth, fFilmIndex, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneGlossyMaterial

	struct OctaneSpecularMaterial : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SPECULAR_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTORGB)		fReflection,
		(OctaneDTORGB)		fTransmission,
		(OctaneDTOEnum)		iBRDFModel,
		(OctaneDTOFloat)	fRoughness,
		(OctaneDTOFloat)	fAnisotropy,
		(OctaneDTOFloat)	fRotation,
		(OctaneDTOFloat)	fIndexOfReflection,
		(OctaneDTOFloat)	fDispersionCoef,
		(OctaneDTOShader)	sBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOShader)	tMedium,
		(OctaneDTOBool)		bFakeShadows,
		(OctaneDTOBool)		bAffectAplha,
		(OctaneDTOBool)		bThinWall,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
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
			fDispersionCoef("Dispersion Coef."),
			sBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			fRoundedEdgeRadius("Edges rounding"),
			tMedium("Medium"),
			bFakeShadows("Fake Shadows"),
			bAffectAplha("Affect aplha"),
			bThinWall("Thin wall"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_SPECULAR)
		{
		}
		MSGPACK_DEFINE(fReflection, fTransmission, iBRDFModel, fRoughness, fAnisotropy, fRotation, fIndexOfReflection, fDispersionCoef, sBump, tNormal, tDisplacement, fOpacity, bSmooth, fRoundedEdgeRadius, tMedium, bFakeShadows, bAffectAplha, bThinWall, fFilmWidth, fFilmIndex, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSpecularMaterial

	struct OctaneToonMaterial : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TOON_MATERIAL;
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
		(OctaneDTOFloat)	fRoundedEdgeRadius
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
			fRoundedEdgeRadius("Rounded Edge Radius"),
			OctaneNodeBase(Octane::NT_MAT_TOON)
		{
		}
		MSGPACK_DEFINE(fDiffuse, fSpecular, fRoughness, iToonLightMode, tToonDiffuseRamp, tToonSpecularRamp, tBump, tNormal, tDisplacement, fOutlineColor, fOutlineThickness, fOpacity, bSmooth, fRoundedEdgeRadius, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneToonMaterial

	struct OctaneMetalMaterial : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MATEL_MATERIAL;
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
		(OctaneDTOShader)	tBump,
		(OctaneDTOShader)	tNormal,
		(OctaneDTOShader)	tDisplacement,
		(OctaneDTOFloat)	fOpacity,
		(OctaneDTOBool)		bSmooth,
		(OctaneDTOFloat)	fRoundedEdgeRadius,
		(OctaneDTOFloat)	fFilmWidth,
		(OctaneDTOFloat)	fFilmIndex,
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
			tBump("Bump"),
			tNormal("Normal"),
			tDisplacement("Displacement"),
			fOpacity("Opacity"),
			bSmooth("Smooth"),
			fRoundedEdgeRadius("Rounded Edge Radius"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_METAL)
		{
		}
		MSGPACK_DEFINE(tDiffuse, fSpecular, tSpecularMap, iBRDFModel, fRoughness, fAnisotropy, fRotation, fSheen, fSheenRoughness, iIORModel, fIndexOfReflection, fIndexOfReflectionGreen, fIndexOfReflectionBlue, tBump, tNormal, tDisplacement, fOpacity, bSmooth, fRoundedEdgeRadius, fFilmWidth, fFilmIndex, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMetalMaterial

	struct OctaneUniversalIOR : public OctaneNodeBase {
        const static PacketType packetType = NONE;
        REFLECTABLE
        (
		(OctaneDTOFloat)	fBaseIOR,
		(OctaneDTOShader)	tBaseIORMap,
		(OctaneDTOEnum)		iIORModel,
		(OctaneDTOFloat2)	fIOR,
		(OctaneDTOFloat2)	fIORGreen,
		(OctaneDTOFloat2)	fIORBlue
        )

		OctaneUniversalIOR() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(fBaseIOR, tBaseIORMap, iIORModel, fIOR, fIORGreen, fIORBlue, MSGPACK_BASE(OctaneNodeBase));
    };

	struct OctaneUniversalCoating : public OctaneNodeBase {
		const static PacketType packetType = NONE;
		REFLECTABLE
		(
		(OctaneDTORGB)		fCoating,
		(OctaneDTOFloat)	fCoatingRoughness,
		(OctaneDTOFloat)	fCoatingIOR,
		(OctaneDTOShader)	tCoatingBump,
		(OctaneDTOShader)	tCoatingNormal
		)

		OctaneUniversalCoating() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(fCoating, fCoatingRoughness, fCoatingIOR, tCoatingBump, tCoatingNormal, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneUniversalMaterial : public OctaneNodeBase {
		const static PacketType packetType = LOAD_UNIVERSAL_MATERIAL;
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
		(OctaneDTOFloat)	fRoundedEdgeRadius,		
		(OctaneDTOShader)	tEmission,
		(OctaneDTOBool)		bShadowCatcher,
		(OctaneDTOShader)   tMaterialLayer
		)
		OctaneUniversalIOR	oOctaneUniversalIOR;
		OctaneUniversalCoating oOctaneUniversalCoating;


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
			fRoundedEdgeRadius("Rounded Edge Radius"),
			tEmission("Emission"),
			bShadowCatcher("Shadow catcher"),
			tMaterialLayer("Material layer"),
			OctaneNodeBase(Octane::NT_MAT_UNIVERSAL)
		{
		}

		void PackAttributes() {
			oOctaneUniversalIOR.fBaseIOR = fBaseIOR;
			oOctaneUniversalIOR.tBaseIORMap = tBaseIORMap;
			oOctaneUniversalIOR.iIORModel = iIORModel;
			oOctaneUniversalIOR.fIOR = fIndexOfReflection;
			oOctaneUniversalIOR.fIORGreen = fIndexOfReflectionGreen;
			oOctaneUniversalIOR.fIORBlue = fIndexOfReflectionBlue;

			oOctaneUniversalCoating.fCoating = fCoating;
			oOctaneUniversalCoating.fCoatingRoughness = fCoatingRoughness;
			oOctaneUniversalCoating.fCoatingIOR = fCoatingIOR;
			oOctaneUniversalCoating.tCoatingBump = tCoatingBump;
			oOctaneUniversalCoating.tCoatingNormal = tCoatingNormal;
		}
		void UnpackAttributes() {
			fBaseIOR = oOctaneUniversalIOR.fBaseIOR;
			tBaseIORMap = oOctaneUniversalIOR.tBaseIORMap;
			iIORModel = oOctaneUniversalIOR.iIORModel;
			fIndexOfReflection = oOctaneUniversalIOR.fIOR;
			fIndexOfReflectionGreen = oOctaneUniversalIOR.fIORGreen;
			fIndexOfReflectionBlue = oOctaneUniversalIOR.fIORBlue;

			fCoating = oOctaneUniversalCoating.fCoating;
			fCoatingRoughness = oOctaneUniversalCoating.fCoatingRoughness;
			fCoatingIOR = oOctaneUniversalCoating.fCoatingIOR;
			tCoatingBump = oOctaneUniversalCoating.tCoatingBump;
			tCoatingNormal = oOctaneUniversalCoating.tCoatingNormal;
		}

		MSGPACK_DEFINE(fTransmission, iTransmissionType, fAlbedoColor, fMetallic, iBRDFModel, fSpecular, fRoughness, fAnisotropy, fRotation,
			oOctaneUniversalIOR, 
			oOctaneUniversalCoating,
			fFilmWidth, fFilmIndex, fSheen, fSheenRoughness, tSheenBump, tSheenNormal, fDispersionCoef, tMedium, fOpacity, bFakeShadows, bAffectAplha,
			tBump, tNormal, tDisplacement, bSmooth, fRoundedEdgeRadius, tEmission, bShadowCatcher, tMaterialLayer, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneUniversalMaterial

	struct OctaneShadowCatcherMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_SHADOW_CATCHER_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTOBool)		bEnabled
		)

		OctaneShadowCatcherMaterial() :
			bEnabled("Enabled"),
			OctaneNodeBase(Octane::NT_MAT_SHADOW_CATCHER)
		{
		}
		MSGPACK_DEFINE(bEnabled, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneShadowCatcherMaterial

	struct OctaneLayeredMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_LAYERED_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTOShader)		tBaseMaterial
		)
		std::vector<std::string>	sLayers;

		OctaneLayeredMaterial() :
			tBaseMaterial("Base Material"),
			OctaneNodeBase(Octane::NT_MAT_LAYER)
		{
		}
		MSGPACK_DEFINE(tBaseMaterial, sLayers, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneLayeredMaterial

	struct OctaneCompositeMaterial : public OctaneNodeBase{
		const static PacketType packetType = LOAD_COMPOSITE_MATERIAL;
		REFLECTABLE
		(
		(OctaneDTOShader)		tDisplacement
		)
		std::vector<std::string>	sMaterials;
		std::vector<std::string>	sMasks;

			OctaneCompositeMaterial() :
			tDisplacement("Displacement"),
			OctaneNodeBase(Octane::NT_MAT_COMPOSITE)
		{
		}
		MSGPACK_DEFINE(tDisplacement, sMaterials, sMasks, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneCompositeMaterial

	struct OctaneGroupLayer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_GROUP_LAYER;
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string>	sLayers;

		OctaneGroupLayer() :
			OctaneNodeBase(Octane::NT_MAT_LAYER_GROUP)
		{
		}
		MSGPACK_DEFINE(sLayers, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneGroupLayer

	struct OctaneDiffuseLayer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_DIFFUSE_LAYER;
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
			OctaneNodeBase(Octane::NT_MAT_DIFFUSE_LAYER)
		{
		}
		MSGPACK_DEFINE(fDiffuse, fTransmission, iBRDFModel, fRoughness, sBump, tNormal, fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDiffuseLayer

	struct OctaneMetallicLayer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_METALLIC_LAYER;
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
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			tBump("Bump"),
			tNormal("Normal"),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_METALLIC_LAYER)
		{
		}
		MSGPACK_DEFINE(fSpecular, iBRDFModel, 
			fRoughness, fAnisotropy, fRotation, 
			iIORModel, fIndexOfReflection, fIndexOfReflectionGreen, fIndexOfReflectionBlue,
			fFilmWidth, fFilmIndex,
			tBump, tNormal,
			fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneMetallicLayer

	struct OctaneSheenLayer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_SHEEN_LAYER;
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
			OctaneNodeBase(Octane::NT_MAT_SHEEN_LAYER)
		{
		}
		MSGPACK_DEFINE(fSheen, fRoughness, fAffectRoughness, tBump, tNormal, fLayerOpacity, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSheenLayer

	struct OctaneSpecularLayer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_SPECULAR_LAYER;
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
			tIORMap("1|IOR map"),
			fFilmWidth("Film Width"),
			fFilmIndex("Film Index"),
			bThinLayer("Thin Layer"),
			tBump("Bump"),
			tNormal("Normal"),
			fDispersionCoef("Dispersion Coef."),
			fLayerOpacity("Layer opacity"),
			OctaneNodeBase(Octane::NT_MAT_SPECULAR_LAYER)
		{
		}
		MSGPACK_DEFINE(fSpecular, fTransmission, iBRDFModel,
			fRoughness, fAffectRoughness, fAnisotropy, fRotation,
			fIOR, tIORMap,
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
		const static PacketType packetType = LOAD_GRAYSCALE_COLOR_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fValue
		)


		OctaneGrayscaleColorTexture() :
			fValue("Value"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT)
		{
		}
		MSGPACK_DEFINE(fValue, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a RGB spectrum texture data that is going to be uploaded to the Octane server.
	struct OctaneRGBSpectrumTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_RGB_SPECTRUM_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTORGB)	fColor
		)


		OctaneRGBSpectrumTexture() :
			fColor("Color"),
			OctaneNodeBase(Octane::NT_TEX_RGB)
		{
		}
		MSGPACK_DEFINE(fColor, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a gaussian spectrum texture data that is going to be uploaded to the Octane server.
	struct OctaneGaussianSpectrumTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_GAUSSIAN_SPECTRUM_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_GAUSSIANSPECTRUM)
		{
		}
		MSGPACK_DEFINE(fWaveLength, fWidth, fPower, MSGPACK_BASE(OctaneNodeBase));
	};

	/// The structure holding a checks texture data that is going to be uploaded to the Octane server.
	struct OctaneChecksTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_CHECKS_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOShader)	sTransform,
		(OctaneDTOShader)	sProjection

		)


		OctaneChecksTexture() :
			sTransform("Transform"),
			sProjection("Projection"),
			OctaneNodeBase(Octane::NT_TEX_CHECKS)
		{
		}
		MSGPACK_DEFINE(sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMarbleTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MARBLE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_MARBLE)
		{
		}
		MSGPACK_DEFINE(fPower, fOffset, iOctaves, fOmega, fVariance, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneRidgedFractalTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_RIDGED_FRACTAL_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_RGFRACTAL)
		{
		}
		MSGPACK_DEFINE(fPower, fRidgeHeight, iOctaves, fOmega, fLacunarity, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSawWaveTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SAW_WAVE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_SAWWAVE)
		{
		}
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSineWaveTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SINE_WAVE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_SINEWAVE)
		{
		}
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriangleWaveTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TRIANGLE_WAVE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_TRIANGLEWAVE)
		{
		}
		MSGPACK_DEFINE(fOffset, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTurbulenceTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TURBULENCE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_TURBULENCE)
		{
		}
		MSGPACK_DEFINE(fPower, fOffset, iOctaves, fOmega, fGamma, bTurbulence, bInvert, sTransform, sProjection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneNoiseTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_NOISE_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_NOISE)
		{
		}
		MSGPACK_DEFINE(iNoiseType, iOctaves, fOmega, sTransform, sProjection, bInvert, fGamma, fContrast, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneClampTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_CLAMP_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_CLAMP)
		{
		}
		MSGPACK_DEFINE(fTexture, fMin, fMax, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCosineMixTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_COSINE_MIX_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_COSINEMIX)
		{
		}
		MSGPACK_DEFINE(fAmount, fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInvertTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_INVERT_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOShader)	sTexture
		)


		OctaneInvertTexture() :
			sTexture("Texture"),
			OctaneNodeBase(Octane::NT_TEX_INVERT)
		{
		}
		MSGPACK_DEFINE(sTexture, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMixTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MIX_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_MIX)
		{
		}
		MSGPACK_DEFINE(fAmount, fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMultiplyTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MULTIPLY_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)


		OctaneMultiplyTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_MULTIPLY)
		{
		}
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneAddTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_ADD_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)


		OctaneAddTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_ADD)
		{
		}
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSubtractTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SUBTRACT_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2
		)


		OctaneSubtractTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			OctaneNodeBase(Octane::NT_TEX_SUBTRACT)
		{
		}
		MSGPACK_DEFINE(fTexture1, fTexture2, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCompareTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_COMPARE_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture1,
		(OctaneDTOFloat)	fTexture2,
		(OctaneDTOFloat)	fTexture3,
		(OctaneDTOFloat)	fTexture4
		)


		OctaneCompareTexture() :
			fTexture1("Texture1"),
			fTexture2("Texture2"),
			fTexture3("Texture3"),
			fTexture4("Texture4"),
			OctaneNodeBase(Octane::NT_TEX_COMPARE)
		{
		}
		MSGPACK_DEFINE(fTexture1, fTexture2, fTexture3, fTexture4, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriplanarTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TRIPLANAR_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_TRIPLANAR)
		{
		}
		MSGPACK_DEFINE(fBlendAngle, iCoordinateSpace, sTransform, f3PositiveXTexture, f3NegativeXTexture, f3PositiveYTexture, f3NegativeYTexture, f3PositiveZTexture, f3NegativeZTexture, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneFalloffTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_FALLOFF_TEXTURE;

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
			OctaneNodeBase(Octane::NT_TEX_FALLOFF)
		{
		}
		MSGPACK_DEFINE(iFalloffMode, fNormal, fGrazing, fFalloff, f3Direction, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneColorCorrectTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_COLOR_CORRECT_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOFloat)	fBrightness,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOFloat)	fHue,
		(OctaneDTOFloat)	fSaturation,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOFloat)	fContrast
		)


		OctaneColorCorrectTexture() :
			fTexture("Texture"),
			fBrightness("Brightness"),
			bInvert("Invert"),
			fHue("Hue"),
			fSaturation("Saturation"),
			fGamma("Gamma"),
			fContrast("Contrast"),
			OctaneNodeBase(Octane::NT_TEX_COLORCORRECTION)
		{
		}
		MSGPACK_DEFINE(fTexture, fBrightness, bInvert, fHue, fSaturation, fGamma, fContrast, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneImageData : public OctaneNodeBase {
		OctaneDTOInt		iHDRDepthType;
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

		OctaneImageData() :
			OctaneNodeBase(Octane::NT_UNKNOWN)
		{
		}

		void Clear() {
			fDataLength = 0;
			iDataLength = 0;
			fImageData.clear();
			iImageData.clear();
			sFilePath = "";
		}
		MSGPACK_DEFINE(iHDRDepthType, sFilePath, bReload, iWidth, iHeight, iChannelNum, fDataLength, iDataLength, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneImageTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_IMAGE_TEXTURE;
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderMode
		)
		OctaneImageData		oImageData;

		OctaneImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderMode("border_mode", false),
			OctaneNodeBase(Octane::NT_TEX_IMAGE)
		{
		}
		MSGPACK_DEFINE(fPower, fGamma, bInvert, bLinearSpaceInvert, tTransform, tProjection, iBorderMode, oImageData, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneImageTileTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_IMAGE_TILE_TEXTURE;
		REFLECTABLE
		(
		(OctaneDTOEnum)		iHDRDepthType,
		(OctaneDTOInt)		iGridSizeX,
		(OctaneDTOInt)		iGridSizeY,
		(OctaneDTOInt)		iStart,
		(OctaneDTOInt)		iDigits,
		(OctaneDTOFloat)	fPower,
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
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			fEmptyTileColor("Empty tile color"),
			OctaneNodeBase(Octane::NT_TEX_IMAGE_TILES)
		{
		}
		MSGPACK_DEFINE(iHDRDepthType, iGridSizeX, iGridSizeY, iStart, iDigits, fPower, fGamma, bInvert, bLinearSpaceInvert, tTransform, tProjection, fEmptyTileColor, iGridSize, sFiles, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneImageTileTexture

	struct OctaneFloatVertexAttributeTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_FLOAT_VERTEXATTRIBUTE_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOString)	sSetName
		)


		OctaneFloatVertexAttributeTexture() :
			sSetName("Name"),
			OctaneNodeBase(Octane::NT_TEX_FLOAT_VERTEXATTRIBUTE)
		{
		}
		MSGPACK_DEFINE(sSetName, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneColorVertexAttributeTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_COLOUR_VERTEXATTRIBUTE_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOString)	sSetName
		)


		OctaneColorVertexAttributeTexture() :
			sSetName("Name"),
			OctaneNodeBase(Octane::NT_TEX_COLOUR_VERTEXATTRIBUTE)
		{
		}
		MSGPACK_DEFINE(sSetName, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInstanceColorTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_INSTANCE_COLOR_TEXTURE;
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert
		)
		OctaneImageData		oImageData;

		OctaneInstanceColorTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			bLinearSpaceInvert("Linear space invert"),
			OctaneNodeBase(Octane::NT_TEX_INSTANCE_COLOR)
		{
		}
		MSGPACK_DEFINE(fPower, fGamma, bInvert, bLinearSpaceInvert, oImageData, MSGPACK_BASE(OctaneNodeBase));
	}; 

	/// The structure holding a osl node data that is going to be uploaded to the Octane server.
	struct OctaneOSLNodeBase : public OctaneNodeBase {
		std::string     sShaderCode;
		std::string		sFilePath;
		OSLNodeInfo		oOSLNodeInfo;		
		OctaneOSLNodeBase(Octane::NodeType _nodeType) : OctaneNodeBase(_nodeType) {}
		MSGPACK_DEFINE(sShaderCode, sFilePath, oOSLNodeInfo, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneOSLNodeBase

	struct OctaneOSLTexture : public OctaneOSLNodeBase {	
		const static PacketType packetType = LOAD_OSL_TEXTURE;
		OctaneOSLTexture() : OctaneOSLNodeBase(Octane::NT_TEX_OSL) {}
	};

	struct OctaneOSLProjection : public OctaneOSLNodeBase {
		const static PacketType packetType = LOAD_OSL_PROJECTION;
		OctaneOSLProjection() : OctaneOSLNodeBase(Octane::NT_PROJ_OSL) {}
	};

	struct OctaneOSLCamera : public OctaneOSLNodeBase {		
		const static PacketType packetType = LOAD_OSL_CAMERA;
		OctaneOSLCamera() : OctaneOSLNodeBase(Octane::NT_CAM_OSL) {}
	};

	struct OctaneOSLBakingCamera : public OctaneOSLNodeBase {
		const static PacketType packetType = LOAD_OSL_BAKING_CAMERA;
		OctaneOSLBakingCamera() : OctaneOSLNodeBase(Octane::NT_CAM_OSL_BAKING) {}
	};

	struct OctaneVectron : public OctaneOSLNodeBase {
		const static PacketType packetType = LOAD_OSL_GEO;
		std::string     sMaterialName;
		std::string		sVectronNodeName;

		OctaneVectron() : OctaneOSLNodeBase(Octane::NT_GEO_OSL) {}
		MSGPACK_DEFINE(sMaterialName, sVectronNodeName, MSGPACK_BASE(OctaneOSLNodeBase));
	};

	struct OctaneFloatImageTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_FLOAT_IMAGE_TEXTURE;
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderMode
		)
		OctaneImageData		oImageData;

		OctaneFloatImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderMode("border_mode", false),
			OctaneNodeBase(Octane::NT_TEX_FLOATIMAGE)
		{
		}
		MSGPACK_DEFINE(fPower, fGamma, bInvert, bLinearSpaceInvert, tTransform, tProjection, iBorderMode, oImageData, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneAlphaImageTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_ALPHA_IMAGE_TEXTURE;
		REFLECTABLE
		(
		(OctaneDTOFloat)	fPower,
		(OctaneDTOFloat)	fGamma,
		(OctaneDTOBool)		bInvert,
		(OctaneDTOBool)		bLinearSpaceInvert,
		(OctaneDTOShader)	tTransform,
		(OctaneDTOShader)	tProjection,
		(OctaneDTOEnum)		iBorderMode
		)
		OctaneImageData		oImageData;

		OctaneAlphaImageTexture() :
			fPower("Power"),
			fGamma("Gamma"),
			bInvert("Invert"),
			bLinearSpaceInvert("Linear space invert"),
			tTransform("Transform"),
			tProjection("Projection"),
			iBorderMode("border_mode", false),
			OctaneNodeBase(Octane::NT_TEX_ALPHAIMAGE)
		{
		}
		MSGPACK_DEFINE(fPower, fGamma, bInvert, bLinearSpaceInvert, tTransform, tProjection, iBorderMode, oImageData, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneDirtTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_DIRT_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fStrength,
		(OctaneDTOFloat)	fDetails,
		(OctaneDTOFloat)	fRadius,
		(OctaneDTOFloat)	fTolerance,
		(OctaneDTOBool)		bInvert
		)


		OctaneDirtTexture() :
			fStrength("Strength"),
			fDetails("Details"),
			fRadius("Radius"),
			fTolerance("Tolerance"),
			bInvert("Invert Normal"),
			OctaneNodeBase(Octane::NT_TEX_DIRT)
		{
		}
		MSGPACK_DEFINE(fStrength, fDetails, fRadius, fTolerance, bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneGradientTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_GRADIENT_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOShader)	sTexture,
		(OctaneDTOEnum)		iInterpolationType
		)
		std::vector<float>  fPosData;
		std::vector<float>  fColorData;

		OctaneGradientTexture() :
			sTexture("Texture"),
			OctaneNodeBase(Octane::NT_TEX_GRADIENT)
		{
		}
		MSGPACK_DEFINE(sTexture, iInterpolationType, fPosData, fColorData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneToonRampTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TOON_RAMP_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOEnum)		iInterpolationType
		)
		std::vector<float>  fPosData;
		std::vector<float>  fColorData;

		OctaneToonRampTexture() :
			OctaneNodeBase(Octane::NT_TOON_RAMP)
		{
		}
		MSGPACK_DEFINE(iInterpolationType, fPosData, fColorData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneVolumeRampTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VOLUMERAMP_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fMaxGridValue,
		(OctaneDTOEnum)		iInterpolationType
		)
		std::vector<float>  fPosData;
		std::vector<float>  fColorData;

		OctaneVolumeRampTexture() :
			fMaxGridValue("Max grid val."),
			OctaneNodeBase(Octane::NT_VOLUME_RAMP)
		{
		}
		MSGPACK_DEFINE(fMaxGridValue, iInterpolationType, fPosData, fColorData, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneRandomColorTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_RANDOM_COLOR_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOInt)		iSeed
		)


		OctaneRandomColorTexture() :
			iSeed("Random Seed"),
			OctaneNodeBase(Octane::NT_TEX_RANDOMCOLOR)
		{
		}
		MSGPACK_DEFINE(iSeed, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctanePolygonSideTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_POLYGON_SIDE_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOBool)		bInvert
		)


		OctanePolygonSideTexture() :
			bInvert("Invert"),
			OctaneNodeBase(Octane::NT_TEX_SIDE)
		{
		}
		MSGPACK_DEFINE(bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneDisplacementTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_DISPLACEMENT_TEXTURE;
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
			OctaneNodeBase(Octane::NT_DISPLACEMENT)
		{
		}
		MSGPACK_DEFINE(tTexture, fMidLevel, iDetailsLevel, fMidLevel, fHeight, iDisplacementDirectionType, iFilterType, iFilterRadius, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneDisplacementTexture

	struct OctaneVertexDisplacementTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VERTEX_DISPLACEMENT_TEXTURE;
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
			OctaneNodeBase(Octane::NT_VERTEX_DISPLACEMENT)
		{
		}
		MSGPACK_DEFINE(tTexture, fHeight, fMidLevel, iMapType, iVertexSpace, bAutoBumpMap, iSubdivisionLevel, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneVertexDisplacementTexture

	struct OctaneVertexDisplacementMixer : public OctaneNodeBase{
		const static PacketType packetType = LOAD_VERTEX_DISPLACEMENT_MIXER_TEXTURE;
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string>	sDisplacements;
		std::vector<std::string>	sWeightLinks;
		std::vector<float>			fWeights;

		OctaneVertexDisplacementMixer() :
			OctaneNodeBase(Octane::NT_VERTEX_DISPLACEMENT_MIXER)
		{
		}
		MSGPACK_DEFINE(sDisplacements, sWeightLinks, fWeights, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneVertexDisplacementMixer


	struct OctaneBakingTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_BAKING_TEXTURE;
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
		(OctaneDTOEnum)		iBorderMode
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
			iBorderMode("border_mode", false),
			OctaneNodeBase(Octane::NT_TEX_BAKED_IMAGE)
		{
		}

		void PackAttributes() {
			iResolution.iVal.x = iResolutionX.iVal;
			iResolution.iVal.y = iResolutionY.iVal;
		}

		MSGPACK_DEFINE(fTexture, bEnableBaking, iResolution, iResolutionX, iResolutionY, iSamplePerPixel, iTextureType, bRGBBaking, fPower, fGamma, bInvert, tTransform, tProjection, iBorderMode, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneUVWTransformTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_UVW_TRANSFORM_TEXTURE;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fTexture,
		(OctaneDTOShader)	sTransform	
		)


		OctaneUVWTransformTexture() :
			fTexture("Texture"),
			sTransform("Transform"),
			OctaneNodeBase(Octane::NT_TEX_UVW_TRANSFORM)
		{
		}
		MSGPACK_DEFINE(fTexture, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneInstaceRangeTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_INSTANCE_RANGE_TEXTURE;

		REFLECTABLE
		(		
		(OctaneDTOInt)		iMaximumID,
		(OctaneDTOBool)		bInvert
		)


		OctaneInstaceRangeTexture() :
			iMaximumID("Maximum ID"),
			bInvert("Invert"),
			OctaneNodeBase(Octane::NT_TEX_INSTANCE_RANGE)
		{
		}
		MSGPACK_DEFINE(iMaximumID, bInvert, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneWTexture : public OctaneNodeBase {
		const static PacketType packetType = LOAD_W_TEXTURE;

		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)


		OctaneWTexture() :
			OctaneNodeBase(Octane::NT_TEX_W)
		{
		}
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneBlackBodyEmission : public OctaneNodeBase{
		const static PacketType packetType = LOAD_BLACKBODY_EMISSION;
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
			OctaneNodeBase(Octane::NT_EMIS_BLACKBODY)
		{
		}
		MSGPACK_DEFINE(fTextureOrEff, fPower, bSurfaceBrightness, bKeepInstancePower, bDoubeSided, fTemperature, bNormalized, fDistribution, fSampleRate, iLightPassID, bVisibleOnDiffuse, bVisibleOnSpecular, bTransparentEmission, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneBlackBodyEmission

	struct OctaneTextureEmission : public OctaneNodeBase{
		const static PacketType packetType = LOAD_TEXTURE_EMISSION;
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
			OctaneNodeBase(Octane::NT_EMIS_TEXTURE)
		{
		}
		MSGPACK_DEFINE(fTexture, fPower, bSurfaceBrightness, bKeepInstancePower, bDoubeSided, fDistribution, fSampleRate, iLightPassID, bVisibleOnDiffuse, bVisibleOnSpecular, bTransparentEmission, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneBlackBodyEmission

	struct OctaneToonPointLight : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TOON_POINT_LIGHT;

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
			OctaneNodeBase(Octane::NT_TOON_POINT_LIGHT)
		{
		}
		MSGPACK_DEFINE(fTexture, fPower, iLightPassID, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneToonDirectionalLight : public OctaneNodeBase {
		const static PacketType packetType = LOAD_TOON_DIRECTIONAL_LIGHT;

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
			OctaneNodeBase(Octane::NT_TOON_DIRECTIONAL_LIGHT)
		{
		}
		MSGPACK_DEFINE(fTexture, f3SunDirection, fPower, iLightPassID, bCastShadow, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneSchlick : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SCHLICK;

		REFLECTABLE
		(
		(OctaneDTOFloat)	fScatteringDirection
		)

		OctaneSchlick() :
			fScatteringDirection("Scattering direction"),
			OctaneNodeBase(Octane::NT_PHASE_SCHLICK)
		{
		}
		MSGPACK_DEFINE(fScatteringDirection, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneAbsorptionMedium : public OctaneNodeBase {
		const static PacketType packetType = LOAD_ABSORPTION_MEDIUM;

		REFLECTABLE
		(
		(OctaneDTORGB)		fAbsorption,
		(OctaneDTOBool)		bInvertAbsorption,
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength
		)

		OctaneAbsorptionMedium() :
			fAbsorption("Absorption Tex"),
			bInvertAbsorption("Invert abs."),
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			OctaneNodeBase(Octane::NT_MED_ABSORPTION)
		{
		}
		MSGPACK_DEFINE(fAbsorption, bInvertAbsorption, fDensity, fVolumeStepLength, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScatteringMedium : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SCATTERING_MEDIUM;

		REFLECTABLE
		(
		(OctaneDTORGB)		fAbsorption,
		(OctaneDTOBool)		bInvertAbsorption,
		(OctaneDTOFloat)	fDensity,
		(OctaneDTOFloat)	fVolumeStepLength,
		(OctaneDTORGB)		fScattering,
		(OctaneDTOFloat)	fPhase,
		(OctaneDTOShader)	sEmission
		)

		OctaneScatteringMedium() :
			fAbsorption("Absorption Tex"),
			bInvertAbsorption("Invert abs."),
			fDensity("Density"),
			fVolumeStepLength("Vol. step length"),
			fScattering("Scattering Tex"),
			fPhase("Phase"),
			sEmission("Emission"),
			OctaneNodeBase(Octane::NT_MED_SCATTERING)
		{
		}
		MSGPACK_DEFINE(fAbsorption, bInvertAbsorption, fDensity, fVolumeStepLength, fScattering, fPhase, sEmission, MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneVolumeMedium : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VOLUME_MEDIUM;

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
		(OctaneDTOShader)	sEmissionRamp
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
			OctaneNodeBase(Octane::NT_MED_VOLUME)
		{
		}
		MSGPACK_DEFINE(fAbsorption, sAbsorptionRamp, bInvertAbsorption, fDensity, fVolumeStepLength, fScattering, sScatteringRamp, fPhase, sEmission, sEmissionRamp, MSGPACK_BASE(OctaneNodeBase));
	}; 

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// VOLUME
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	/// The structure holding an OpenVDB volume data that is going to be uploaded to the Octane server.
	struct OctaneVolume : public OctaneNodeBase {
		std::string  sFileName;
		float   *pfRegularGrid;
		int32_t iGridSize;
		MatrixF gridMatrix;
		float_3 f3Resolution;
		float   fISO;
		std::string  sMedium;
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
		bool	bSDF;
		std::string  sAbsorptionId;
		std::string  sEmissionId;
		std::string  sScatterId;
		std::string  sVelocityId;
		std::string  sVelocityIdX;
		std::string  sVelocityIdY;
		std::string  sVelocityIdZ;

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
	struct OctaneFloatValue : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VALUE_FLOAT;

		REFLECTABLE
		(
		(OctaneDTOFloat3)	f3Value
		)


		OctaneFloatValue() :
			f3Value("Value"),
			OctaneNodeBase(Octane::NT_FLOAT)
		{
		}
		MSGPACK_DEFINE(f3Value, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneIntValue : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VALUE_INT;

		REFLECTABLE
		(
		(OctaneDTOInt)		iValue
		)


		OctaneIntValue() :
			iValue("Value"),
			OctaneNodeBase(Octane::NT_INT)
		{
		}
		MSGPACK_DEFINE(iValue, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSunDirection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VALUE_SUN_DIRECTION;

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
			OctaneNodeBase(Octane::NT_SUN_DIRECTION)
		{
		}
		MSGPACK_DEFINE(fLatitude, fLongtitude, iMonth, iDay, fLocalTime, iGMTOffset, MSGPACK_BASE(OctaneNodeBase));
	}; //struct OctaneSunDirection

	struct OctaneRoundEdges : public OctaneNodeBase {
		const static PacketType packetType = LOAD_ROUND_EDGES;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iMode,
		(OctaneDTOFloat)	fRadius,
		(OctaneDTOFloat)	fRoundness,
		(OctaneDTOBool)		bConsiderOtherObjects
		)


		OctaneRoundEdges() :
			iMode("round_edges_mode", false),
			fRadius("Radius"),
			fRoundness("Roundness"),
			bConsiderOtherObjects("Consider other objects"),
			OctaneNodeBase(Octane::NT_ROUND_EDGES)
		{
		}
		MSGPACK_DEFINE(iMode, fRadius, fRoundness, bConsiderOtherObjects, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneDBNodes {
    bool bClose;

		MSGPACK_DEFINE(bClose);
	};
}

#endif
// clang-format on
