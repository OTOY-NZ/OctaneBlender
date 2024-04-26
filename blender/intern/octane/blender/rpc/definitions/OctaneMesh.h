// clang-format off
#ifndef __OCTANE_MESH_H__
#define __OCTANE_MESH_H__
#include "OctaneNode.h"
#include "OctaneTransform.h"
#define MAX_OCTANE_COLOR_VERTEX_SETS 2
#define MAX_OCTANE_FLOAT_VERTEX_SETS 4
#define ARRAY_INFO_POINT_DATA "POINT"
#define ARRAY_INFO_NORMAL_DATA "NORMAL"
#define ARRAY_INFO_POINT_INDEX_DATA "POINT_INDEX"
#define ARRAY_INFO_NORMAL_INDEX_DATA "NORMAL_INDEX"
#define ARRAY_INFO_SMOOTH_GROUP_PER_POLY_DATA "SMOOTH_GROUP_PER_POLY"
#define ARRAY_INFO_VERTEX_PER_POLY_DATA "VERTEX_PER_POLY"
#define ARRAY_INFO_MAT_ID_POLY_DATA "MATERIAL_ID_PER_POLY"
#define ARRAY_INFO_OBJ_ID_POLY_DATA "OBJECT_ID_PER_POLY"
#define ARRAY_INFO_UV_DATA "UV"
#define ARRAY_INFO_UV_INDEX_DATA "UV_INDEX"
#define ARRAY_INFO_CANDIDATE_UV_DATA "CANDIDATE_UV"
#define ARRAY_INFO_CANDIDATE_UV_INDEX_DATA "CANDIDATE_UV_INDEX"
#define ARRAY_INFO_VERTEX_COLOR_DATA "VERTEX_COLOR"
#define ARRAY_INFO_VERTEX_FLOAT_DATA "VERTEX_FLOAT"
#define ARRAY_INFO_VELOCITY_DATA "VERTEX_VELOCITY"
#define ARRAY_INFO_HAIR_POINT_DATA "HAIR_POINT"
#define ARRAY_INFO_HAIR_VERTEX_PER_HAIR_DATA "HAIR_VERTEX_PER_HAIR"
#define ARRAY_INFO_HAIR_THICKNESS_DATA "HAIR_THICKNESS"
#define ARRAY_INFO_HAIR_MAT_INDEX_DATA "HAIR_MAT_INDEX"
#define ARRAY_INFO_HAIR_UV_DATA "HAIR_UV"
#define ARRAY_INFO_HAIR_W_DATA "HAIR_W"
#define ARRAY_INFO_OPENSUBDIVISION_CREASE_INDEX "OPENSUBDIVISION_CREASE_INDEX"
#define ARRAY_INFO_OPENSUBDIVISION_CREASE_SHARPNESS "OPENSUBDIVISION_CREASE_SHARPNESS"
#define ARRAY_INFO_MATRIX_DATA "MATRIX"
#define ARRAY_INFO_INSTANCE_ID_DATA "INSTANCE_ID"
#define ARRAY_INFO_SPHERE_CENTER_DATA "SPHERE_CENTER"
#define ARRAY_INFO_SPHERE_RADIUS_DATA "SPHERE_RADIUS"
#define ARRAY_INFO_SPHERE_SPEED_DATA "SPHERE_SPEED"
#define ARRAY_INFO_SPHERE_UV_DATA "SPHERE_UV"
#define ARRAY_INFO_SPHERE_VERTEX_COLOR_DATA "SPHERE_VERTEX_COLOR"
#define ARRAY_INFO_SPHERE_VERTEX_FLOAT_DATA "SPHERE_VERTEX_FLOAT"
#define ARRAY_INFO_SPHERE_MATERIAL_INDEX_DATA "SPHERE_MATERIAL_INDEX"

#define MESH_TAG "[Mesh]"
#define LIGHT_TAG "[Light]"
#define OBJECT_TAG "[Object]"
#define COLLECTION_TAG "[Collection]"
#define OBJECT_MATERIAL_MAP_TAG "[ObjMM]"
#define OBJECT_LAYER_MAP_TAG "[ObjLM]"
#define TOON_DIRECTIONAL_LIGHT_OBJECT_DIRECTION_TAG "[ToonDirLightObjDir]"

namespace OctaneDataTransferObject {

	struct OctaneSphereAttributeData : public OctaneNodeBase {
		bool	bEnable;
		float	fRadius;
		int		iRandomSeed;
		float	fMinRandomizedRadius;
		float	fMaxRandomizedRadius;
		OctaneSphereAttributeData() : OctaneNodeBase(Octane::ENT_MESH_SPHERE_ATTRIBUTE, "OctaneMeshSphereAttribute") {}
		MSGPACK_DEFINE(bEnable, fRadius, iRandomSeed, fMinRandomizedRadius, fMaxRandomizedRadius, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshData : public OctaneNodeBase {
		bool					bUpdate;
		bool					bShowVertexData;
		bool					bUseFaceNormal;
		int						iSamplesNum;
		std::vector<float_3>	f3Points;		
		std::vector<float_3>	f3Normals;
		std::vector<int32_t>	iPointIndices;
		std::vector<int32_t>	iNormalIndices;
		std::vector<int32_t>	iSmoothGroupPerPoly;
		std::vector<int32_t>	iVertexPerPoly;
		std::vector<int32_t>	iPolyMaterialIndex;
		std::vector<int32_t>	iPolyObjectIndex;
		std::vector<float_3>	f3UVs;
		std::vector<int32_t>	iUVIndices;		
		std::vector<std::vector<float_3>>	f3CandidateUVs;
		std::vector<std::vector<int32_t>>	iCandidateUVIndices;
		std::vector<float_3>	f3Velocities;	
		std::vector<float_3>	f3HairPoints;
		std::vector<int32_t>	iVertexPerHair;
		std::vector<float>		fHairThickness;
		std::vector<int32_t>	iHairMaterialIndices;
		std::vector<float_2>	f2HairUVs;
		std::vector<float_2>	f2HairWs;		
		std::vector<std::string>	sVertexFloatNames;
		std::vector<std::vector<float>>	fVertexFloats;
		std::vector<std::string>	sVertexColorNames;
		std::vector<std::vector<float_3>>	f3VertexColors;	
		std::map<float, std::vector<float_3>>	oMotionf3Points;
		std::map<float, std::vector<float_3>>	oMotionf3HairPoints;
		OctaneSphereAttributeData	oMeshSphereAttribute;
		std::vector<float_3>	f3SphereCenters;
		std::vector<float>		fSphereRadiuses;
		std::vector<float_3>	f3SphereSpeeds;
		std::vector<float_2>	f2SphereUVs;		
		std::vector<std::string>	sSphereVertexFloatNames;
		std::vector<std::vector<float>>	fSphereVertexFloats;
		std::vector<std::string>	sSphereVertexColorNames;
		std::vector<std::vector<float_3>>	f3SphereVertexColors;
		std::vector<int32_t>		iSphereMaterialIndices;
		std::map<std::string, std::pair<uint32_t, uint32_t>>	oArrayInfo;
		OctaneMeshData() : OctaneNodeBase(Octane::ENT_MESH_DATA, "OctaneMeshData") {}
		void Clear() 
		{ 
			bUpdate = false;
			bShowVertexData = true;
			bUseFaceNormal = false;
			iSamplesNum = 0;
			f3Points.clear();
			f3Normals.clear();
			iPointIndices.clear();
			iNormalIndices.clear();
			iSmoothGroupPerPoly.clear();
			iVertexPerPoly.clear();
			iPolyMaterialIndex.clear();
			iPolyObjectIndex.clear();
			f3UVs.clear();
			iUVIndices.clear();
			f3Velocities.clear();
			f3HairPoints.clear();
			iVertexPerHair.clear();
			fHairThickness.clear();
			iHairMaterialIndices.clear();
			f2HairUVs.clear();
			f2HairWs.clear();
			sVertexFloatNames.clear();
			fVertexFloats.clear();
			sVertexColorNames.clear();			
			f3VertexColors.clear();
			for (auto &f3CandidateUV : f3CandidateUVs) { f3CandidateUV.clear(); }
			f3CandidateUVs.clear();
			for (auto &iCandidateUVIndice : iCandidateUVIndices) { iCandidateUVIndice.clear(); }
			iCandidateUVIndices.clear();
			oMotionf3Points.clear();
			oMotionf3HairPoints.clear();
			f3SphereCenters.clear();
			fSphereRadiuses.clear();
			f3SphereSpeeds.clear();
			f2SphereUVs.clear();
			sSphereVertexFloatNames.clear();
			fSphereVertexFloats.clear();
			sSphereVertexColorNames.clear();
			f3SphereVertexColors.clear();
			iSphereMaterialIndices.clear();
			oArrayInfo.clear();
		}
		MSGPACK_DEFINE(bUpdate, bShowVertexData, bUseFaceNormal, iSamplesNum, sVertexFloatNames, sVertexColorNames, oMeshSphereAttribute, sSphereVertexFloatNames, sSphereVertexColorNames, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshOpenSubdivision : public OctaneNodeBase {
		bool						bUpdate;
		bool						bOpenSubdEnable;
		int32_t						iOpenSubdScheme;
		int32_t						iOpenSubdLevel;
		float						fOpenSubdSharpness;
		int32_t						iOpenSubdBoundInterp;
		std::vector<int32_t>		iOpenSubdCreasesIndices;
		std::vector<float>			fOpenSubdCreasesSharpnesses;
		std::map<std::string, std::pair<uint32_t, uint32_t>>	oArrayInfo;
		OctaneMeshOpenSubdivision() : OctaneNodeBase(Octane::ENT_MESH_SUBD_DATA, "OctaneMeshOpenSubdivision") {}
		void Clear() 
		{
			bUpdate = false;
			bOpenSubdEnable = false;
			iOpenSubdCreasesIndices.clear();
			fOpenSubdCreasesSharpnesses.clear();
		}
		MSGPACK_DEFINE(bUpdate, bOpenSubdEnable, iOpenSubdScheme, iOpenSubdLevel, fOpenSubdSharpness, iOpenSubdBoundInterp, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshVolume : public OctaneNodeBase {		
		bool	bEnable;
		bool	bSDF;
		float	fVoxelSize;
		float	fBorderThicknessInside;
		float	fBorderThicknessOutside;
		OctaneMeshVolume() : OctaneNodeBase(Octane::ENT_MESH_VOLUME_SDF, "OctaneMeshVolumeSDF") {}
		void Clear() 
		{
			bEnable = false;
			bSDF = false;
			fVoxelSize = 0.1f;
			fBorderThicknessInside = 3.f;
			fBorderThicknessOutside = 3.f;
		}
		MSGPACK_DEFINE(bEnable, bSDF, fVoxelSize, fBorderThicknessInside, fBorderThicknessOutside, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneObjectLayer : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iRenderLayerID,
		(OctaneDTOFloat)	fGeneralVisibility,
		(OctaneDTOBool)		bCameraVisibility,
		(OctaneDTOBool)		bShadowVisibility,
		(OctaneDTOBool)		bDirtVisibility,
		(OctaneDTOBool)		bCurvatureVisibility,
		(OctaneDTOBool)		bRoundEdgeVisibility,
		(OctaneDTOInt)		iRandomColorSeed,
		(OctaneDTOFloat3)	f3Color,
		(OctaneDTOInt)		iBakingGroupId,
		(OctaneDTOFloat)	fRotationZ,
		(OctaneDTOFloat)	fScaleX,
		(OctaneDTOFloat)	fScaleY,
		(OctaneDTOFloat)	fTranslationX,
		(OctaneDTOFloat)	fTranslationY,
		(OctaneDTOInt)		iLightPassMask,
		(OctaneDTOInt3)		i3Color,
		(OctaneDTOEnum)		iCustomAOV,
		(OctaneDTOEnum)		iCustomAOVChannel
		)
		OctaneValueTransform oBakingTransform;

		OctaneObjectLayer() :
			iRenderLayerID("render_layer_id", false),
			fGeneralVisibility("general_visibility", false),
			bCameraVisibility("camera_visibility", false),
			bShadowVisibility("shadow_visibility", false),
			bDirtVisibility("dirt_visibility", false),
			bCurvatureVisibility("curvature_visibility", false),
			bRoundEdgeVisibility("round_edge_visibility", false),
			iRandomColorSeed("random_color_seed", false),
			f3Color("color", false),
			iBakingGroupId("baking_group_id", false),
			fRotationZ("baking_uv_transform_rz", false),
			fScaleX("baking_uv_transform_sx", false),
			fScaleY("baking_uv_transform_sy", false),
			fTranslationX("baking_uv_transform_tx", false),
			fTranslationY("baking_uv_transform_ty", false),
			iCustomAOV("custom_aov", false),
			iCustomAOVChannel("custom_aov_channel", false),
			OctaneNodeBase(Octane::NT_OBJECTLAYER, "OctaneObjectLayer") 
		{
		}

    inline bool IsSameValue(const OctaneObjectLayer& other) {
      return iRenderLayerID.IsSameValue(other.iRenderLayerID) &&
        fGeneralVisibility.IsSameValue(other.fGeneralVisibility) &&
        bCameraVisibility.IsSameValue(other.bCameraVisibility) &&
        bShadowVisibility.IsSameValue(other.bShadowVisibility) &&
        bDirtVisibility.IsSameValue(other.bDirtVisibility) &&
        bCurvatureVisibility.IsSameValue(other.bCurvatureVisibility) &&
		bRoundEdgeVisibility.IsSameValue(other.bRoundEdgeVisibility) &&
        iRandomColorSeed.IsSameValue(other.iRandomColorSeed) &&
        iLightPassMask.IsSameValue(other.iLightPassMask) &&
        f3Color.IsSameValue(other.f3Color) &&
        fRotationZ.IsSameValue(other.fRotationZ) &&
        fScaleX.IsSameValue(other.fScaleX) &&
        fScaleY.IsSameValue(other.fScaleY) &&
        fTranslationX.IsSameValue(other.fTranslationX) &&
        fTranslationY.IsSameValue(other.fTranslationY) &&
        iCustomAOV.IsSameValue(other.iCustomAOV) &&
        iCustomAOVChannel.IsSameValue(other.iCustomAOVChannel) &&
        oBakingTransform.IsSameValue(other.oBakingTransform);
    }

		MSGPACK_DEFINE(iRenderLayerID, fGeneralVisibility, bCameraVisibility, bShadowVisibility, bDirtVisibility, bCurvatureVisibility, bRoundEdgeVisibility, iRandomColorSeed, iLightPassMask, i3Color,
			iBakingGroupId, oBakingTransform, iCustomAOV, iCustomAOVChannel, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMesh : public OctaneNodeBase {
		std::string					sMeshName;
		std::string					sScriptGeoName;
		std::string					sOrbxPath;
    bool                bEnableAnimationTimeTransformation;
    float               fAnimationTimeTransformationDelay;
    float               fAnimationTimeTransformationScale;
		std::vector<std::string>	sShaderNames;
		std::vector<std::string>	sObjectNames;		
		int32_t						iCurrentActiveUVSetIdx;
		int32_t						iHairWsSize;
		int32_t						iHairInterpolations;
		bool						bInfinitePlane;
		bool						bReshapeable;
		float						fMaxSmoothAngle;
		OctaneMeshData				oMeshData;
		OctaneMeshOpenSubdivision	oMeshOpenSubdivision;
		OctaneMeshVolume			oMeshVolume;
		OctaneObjectLayer			oObjectLayer;		
		OctaneMesh() : OctaneNodeBase(Octane::ENT_MESH, "OctaneMesh") {}
		void Clear()
		{
			iCurrentActiveUVSetIdx = 0;
      bEnableAnimationTimeTransformation = false;
      fAnimationTimeTransformationDelay = 0;
      fAnimationTimeTransformationScale = 0;
			sShaderNames.clear();
			sObjectNames.clear();
			oMeshData.Clear();
			oMeshOpenSubdivision.Clear();
			oMeshVolume.Clear();
		}
		MSGPACK_DEFINE(sMeshName, sScriptGeoName, sOrbxPath,
      bEnableAnimationTimeTransformation, fAnimationTimeTransformationDelay, fAnimationTimeTransformationScale,
			sShaderNames, sObjectNames, 
			iCurrentActiveUVSetIdx, iHairWsSize, iHairInterpolations, bInfinitePlane, bReshapeable, fMaxSmoothAngle, 
			oMeshData, oMeshOpenSubdivision, oMeshVolume, oObjectLayer, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshes : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MESH;
		bool						bUpdateRender;
		bool						bGlobal;
		std::string					sGlobalMeshName;
		std::string					sGlobalLayerName;
		int32_t						iCurrentFrameIdx;
		int32_t						iTotalFrameIdx;
		std::vector<OctaneMesh>		oMeshes;
		OctaneMesh					oGlobalMesh;
		int32_t*					iData;
		float*						fData;
		OctaneMeshes() : bUpdateRender(true), OctaneNodeBase(Octane::ENT_MESHES, "OctaneMeshes") {}
		MSGPACK_DEFINE(bUpdateRender, bGlobal, sGlobalMeshName, sGlobalLayerName, iCurrentFrameIdx, iTotalFrameIdx, oMeshes, oGlobalMesh);
	};

	struct OctaneGeoNodes : public OctaneNodeBase {
		const static PacketType packetType = GET_GEO_NODES;
		int32_t						iMeshNodeType;
		std::set<std::string>		sMeshNames;
		OctaneGeoNodes() : OctaneNodeBase(Octane::ENT_GEO_NODES, "OctaneGeoNodes") {}
		MSGPACK_DEFINE(iMeshNodeType, sMeshNames);
	};

	struct OctaneObject : public OctaneNodeBase {
		const static int NO_OBJECT_LAYER = 0;
		const static int WITH_OBJECT_LAYER = 1;
		const static int WITH_OBJECT_LAYER_FOR_ORBX_PROXY = 2;

		std::string					sObjectName;
		std::string					sMeshName;
		int32_t						iInstanceSize;
		MatrixF						oMatrix;
		std::map<float, MatrixF>	oMotionMatrices;
		int32_t						iSamplesNum;
		int32_t						iInstanceId;
		bool						bMovable;
		int8_t						iUseObjectLayer;
		OctaneObjectLayer			oObjectLayer;		
		std::map<std::string, std::pair<uint32_t, uint32_t>>	oArrayInfo;
		OctaneObject() : OctaneNodeBase(Octane::ENT_OBJECT, "OctaneObject")
    {
      iInstanceSize = 1;
      iInstanceId = 0;
      iSamplesNum = 1;
      iUseObjectLayer = NO_OBJECT_LAYER;
    }
    bool isSameValue(const OctaneObject& other) {
      return sObjectName == other.sObjectName
        && sMeshName == other.sMeshName
        && iInstanceSize == other.iInstanceSize
        && oMatrix == other.oMatrix
        && oMotionMatrices == other.oMotionMatrices
        && iSamplesNum == other.iSamplesNum
        && iInstanceId == other.iInstanceId
        && bMovable == other.bMovable
        && iUseObjectLayer == other.iUseObjectLayer
        && oObjectLayer.IsSameValue(other.oObjectLayer);
    }
		MSGPACK_DEFINE(sObjectName, sMeshName, iInstanceSize, bMovable, iUseObjectLayer, iSamplesNum, oObjectLayer, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneObjects : public OctaneNodeBase {
		const static PacketType packetType = LOAD_OBJECT;
		bool						bUpdateRender;
		bool						bGlobal;
		int32_t						iCurrentFrameIdx;
		int32_t						iTotalFrameIdx;
		std::vector<OctaneObject>	oObjects;
		std::unordered_map<std::string, std::vector<uint32_t>> iInstanceIDMap;
		std::unordered_map<std::string, std::vector<float>> fMatrixMap;
		int32_t*					iData;
		float*						fData;
		OctaneObjects() : bUpdateRender(true), OctaneNodeBase(Octane::ENT_OBJECTS, "OctaneObjects") {}
		MSGPACK_DEFINE(bUpdateRender, bGlobal, iCurrentFrameIdx, iTotalFrameIdx, oObjects, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneLight : public OctaneNodeBase {
		const static PacketType packetType = LOAD_LIGHT;

		std::string					sLightName;
		std::string					sShaderName;
		int32_t						iLightNodeType;
		float						fRadius;
		float						fSizeX;
		float						fSizeY;
		float_3						f3Direction;		
		std::string					sLightObjectPath;
		std::string					sLightMeshName;
		std::string					sLightMatMapName;
		OctaneObject				oObject;
		OctaneLight() : OctaneNodeBase(Octane::ENT_LIGHT, "OctaneLight") {}
		MSGPACK_DEFINE(sLightName, sShaderName, iLightNodeType, fRadius, fSizeX, fSizeY, f3Direction, sLightObjectPath, sLightMeshName, sLightMatMapName, oObject, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneVolume : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VOLUME;

		REFLECTABLE
		(	
		(OctaneDTOBool)		bSDF,
		(OctaneDTOFloat)	fISO,
		(OctaneDTOFloat)	fBorderThicknessInside,
		(OctaneDTOFloat)	fBorderThicknessOutside,
		(OctaneDTOEnum)		iImportScale,
		(OctaneDTOFloat)	fAbsorptionScale,
		(OctaneDTOString)	sAbsorptionGridId,
		(OctaneDTOFloat)	fEmissionScale,
		(OctaneDTOString)	sEmissionGridId,
		(OctaneDTOFloat)	fScatterScale,
		(OctaneDTOString)	sScatterGridId,
		(OctaneDTOBool)		bMotionBlurEnabled,
		(OctaneDTOEnum)		iVelocityGridType,
		(OctaneDTOFloat)	fVelocityScale,	
		(OctaneDTOString)	sVelocityGridId,
		(OctaneDTOString)	sXComponentGridId,
		(OctaneDTOString)	sYComponentGridId,
		(OctaneDTOString)	sZComponentGridId
		)

		std::string			sVolumePath;
		MatrixF				oMatrix;
		std::string			sShaderName;
		float_3				f3Resolution;
		int32_t				iAbsorptionOffset;
		int32_t				iEmissionOffset;
		int32_t				iScatterOffset;
		int32_t				iVelocityOffsetX;
		int32_t				iVelocityOffsetY;
		int32_t				iVelocityOffsetZ;
		std::vector<float>	fRegularGridData;
		OctaneVolume() : 
			bSDF("vdb_sdf", false),
			fISO("vdb_iso", false),
			fBorderThicknessInside("border_thickness_inside", false),
			fBorderThicknessOutside("border_thickness_outside", false),
			iImportScale("vdb_import_scale", false),
			fAbsorptionScale("vdb_abs_scale", false),
			sAbsorptionGridId("vdb_absorption_grid_id", false),
			fEmissionScale("vdb_emiss_scale", false),
			sEmissionGridId("vdb_emission_grid_id", false),
			fScatterScale("vdb_scatter_scale", false),
			sScatterGridId("vdb_scattering_grid_id", false),
			bMotionBlurEnabled("vdb_motion_blur_enabled", false),
			iVelocityGridType("vdb_velocity_grid_type", false),
			fVelocityScale("vdb_vel_scale", false),
			sVelocityGridId("vdb_vector_grid_id", false),
			sXComponentGridId("vdb_x_components_grid_id", false),
			sYComponentGridId("vdb_y_components_grid_id", false),
			sZComponentGridId("vdb_z_components_grid_id", false),
			iAbsorptionOffset(0),
			iEmissionOffset(0),
			iScatterOffset(0),
			iVelocityOffsetX(-1),
			iVelocityOffsetY(-1),
			iVelocityOffsetZ(-1),
			OctaneNodeBase(Octane::NT_GEO_VOLUME, "OctaneVolume") {}
		void Clear()
		{
			fRegularGridData.clear();
		}

		MSGPACK_DEFINE(bSDF, fISO, fBorderThicknessInside, fBorderThicknessOutside, iImportScale, fAbsorptionScale, sAbsorptionGridId, fEmissionScale, sEmissionGridId, fScatterScale, sScatterGridId,
			bMotionBlurEnabled, iVelocityGridType, fVelocityScale, sVelocityGridId, sXComponentGridId, sYComponentGridId, sZComponentGridId,
			sVolumePath, oMatrix, sShaderName, f3Resolution, iAbsorptionOffset, iEmissionOffset, iScatterOffset, iVelocityOffsetX, iVelocityOffsetY, iVelocityOffsetZ,
			MSGPACK_BASE(OctaneNodeBase));
	}; 

	struct OctaneVolumeInfo : public OctaneNodeBase {
		std::string					sVolumePath;
		std::vector<std::string>	sFloatGridNames;
		std::vector<std::string>	sVectorGridNames;

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_GENERATE_RESPONSE_FUNCTIONS
		OctaneVolumeInfo() : OctaneNodeBase(Octane::ENT_VDB_INFO, "VDBInfo", 0, 1) {}
		MSGPACK_DEFINE(sVolumePath, sFloatGridNames, sVectorGridNames, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctanePlacement : public OctaneNodeBase {
		REFLECTABLE
		(
		(OctaneDTOShader)	oTransform,
		(OctaneDTOShader)	oMesh
		)

		OctanePlacement() :
			oTransform("Transform"),
			oMesh("Mesh"),
			OctaneNodeBase(Octane::NT_GEO_PLACEMENT, "ShaderNodeOctPlacement")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(oTransform, oMesh, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneGeometryGroup : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)
		std::vector<std::string> sGeometries;

		OctaneGeometryGroup() :
			OctaneNodeBase(Octane::NT_GEO_GROUP, "GeometryCollection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, sGeometries, MSGPACK_BASE(OctaneNodeBase));
	};
}

#endif
// clang-format on
