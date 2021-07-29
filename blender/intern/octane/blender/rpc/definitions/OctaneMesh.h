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
#define ARRAY_INFO_VERTEX_PER_POLY_DATA "VERTEX_PER_POLY"
#define ARRAY_INFO_MAT_ID_POLY_DATA "MATERIAL_ID_PER_POLY"
#define ARRAY_INFO_OBJ_ID_POLY_DATA "OBJECT_ID_PER_POLY"
#define ARRAY_INFO_UV_DATA "UV"
#define ARRAY_INFO_UV_INDEX_DATA "UV_INDEX"
#define ARRAY_INFO_CANDIDATE_UV_DATA "CANDIDATE_UV"
#define ARRAY_INFO_CANDIDATE_UV_INDEX_DATA "CANDIDATE_UV_INDEX"
#define ARRAY_INFO_VERTEX_COLOR_DATA "VERTEX_COLOR"
#define ARRAY_INFO_VERTEX_FLOAT_DATA "VERTEX_FLOAT"
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

#define MESH_TAG "[Mesh]"
#define LIGHT_TAG "[Light]"
#define OBJECT_TAG "[Object]"
#define OBJECT_MATERIAL_MAP_TAG "[ObjMM]"
#define OBJECT_LAYER_MAP_TAG "[ObjLM]"
#define TOON_DIRECTIONAL_LIGHT_OBJECT_DIRECTION_TAG "[ToonDirLightObjDir]"

namespace OctaneDataTransferObject {

	struct OctaneMeshData : public OctaneNodeBase {
		const static PacketType packetType = NONE;
		bool					bUpdate;
		int						iSamplesNum;
		std::vector<float_3>	f3Points;		
		std::vector<float_3>	f3Normals;
		std::vector<int32_t>	iPointIndices;
		std::vector<int32_t>	iNormalIndices;
		std::vector<int32_t>	iVertexPerPoly;
		std::vector<int32_t>	iPolyMaterialIndex;
		std::vector<int32_t>	iPolyObjectIndex;
		std::vector<float_3>	f3UVs;
		std::vector<int32_t>	iUVIndices;		
		std::vector<std::vector<float_3>>	f3CandidateUVs;
		std::vector<std::vector<int32_t>>	iCandidateUVIndices;
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
		std::map<std::string, std::pair<uint32_t, uint32_t>>	oArrayInfo;
		OctaneMeshData() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		void Clear() 
		{ 
			bUpdate = false;
			iSamplesNum = 0;
			f3Points.clear();
			f3Normals.clear();
			iPointIndices.clear();
			iNormalIndices.clear();
			iVertexPerPoly.clear();
			iPolyMaterialIndex.clear();
			iPolyObjectIndex.clear();
			f3UVs.clear();
			iUVIndices.clear();
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
			oArrayInfo.clear();
		}
		MSGPACK_DEFINE(bUpdate, iSamplesNum, sVertexFloatNames, sVertexColorNames, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
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
		OctaneMeshOpenSubdivision() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		void Clear() 
		{
			bUpdate = false;
			bOpenSubdEnable = false;
			iOpenSubdCreasesIndices.clear();
			fOpenSubdCreasesSharpnesses.clear();
		}
		MSGPACK_DEFINE(bUpdate, bOpenSubdEnable, iOpenSubdScheme, iOpenSubdLevel, fOpenSubdSharpness, iOpenSubdBoundInterp, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneObjectLayer : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iRenderLayerID,
		(OctaneDTOFloat)	fGeneralVisibility,
		(OctaneDTOBool)		bCameraVisibility,
		(OctaneDTOBool)		bShadowVisibility,
		(OctaneDTOInt)		iRandomColorSeed,
		(OctaneDTOFloat3)	f3Color,
		(OctaneDTOInt)		iBakingGroupId,
		(OctaneDTOFloat)	fRotationZ,
		(OctaneDTOFloat)	fScaleX,
		(OctaneDTOFloat)	fScaleY,
		(OctaneDTOFloat)	fTranslationX,
		(OctaneDTOFloat)	fTranslationY,
		(OctaneDTOInt)		iLightPassMask,
		(OctaneDTOInt3)		i3Color
		)
		OctaneValueTransform oBakingTransform;

		OctaneObjectLayer() :
			iRenderLayerID("render_layer_id", false),
			fGeneralVisibility("general_visibility", false),
			bCameraVisibility("camera_visibility", false),
			bShadowVisibility("shadow_visibility", false),
			iRandomColorSeed("random_color_seed", false),
			f3Color("color", false),
			iBakingGroupId("baking_group_id", false),
			fRotationZ("baking_uv_transform_rz", false),
			fScaleX("baking_uv_transform_sx", false),
			fScaleY("baking_uv_transform_sy", false),
			fTranslationX("baking_uv_transform_tx", false),
			fTranslationY("baking_uv_transform_ty", false),
			OctaneNodeBase(Octane::NT_OBJECTLAYER) 
		{
		}
		MSGPACK_DEFINE(iRenderLayerID, fGeneralVisibility, bCameraVisibility, bShadowVisibility, iRandomColorSeed, iLightPassMask, i3Color,
			iBakingGroupId, oBakingTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMesh : public OctaneNodeBase {
		std::string					sMeshName;
		std::string					sScriptGeoName;
		std::string					sOrbxPath;
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
		OctaneObjectLayer			oObjectLayer;
		OctaneMesh() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		void Clear()
		{
			iCurrentActiveUVSetIdx = 0;
			sShaderNames.clear();
			sObjectNames.clear();
			oMeshData.Clear();
			oMeshOpenSubdivision.Clear();
		}
		MSGPACK_DEFINE(sMeshName, sScriptGeoName, sOrbxPath,
			sShaderNames, sObjectNames, 
			iCurrentActiveUVSetIdx, iHairWsSize, iHairInterpolations, bInfinitePlane, bReshapeable, fMaxSmoothAngle, 
			oMeshData, oMeshOpenSubdivision, oObjectLayer, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshes : public OctaneNodeBase {
		const static PacketType packetType = LOAD_MESH;		
		bool						bGlobal;
		std::string					sGlobalMeshName;
		std::string					sGlobalLayerName;
		int32_t						iCurrentFrameIdx;
		int32_t						iTotalFrameIdx;
		std::vector<OctaneMesh>		oMeshes;
		OctaneMesh					oGlobalMesh;
		int32_t*					iData;
		float*						fData;
		OctaneMeshes() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(bGlobal, sGlobalMeshName, sGlobalLayerName, iCurrentFrameIdx, iTotalFrameIdx, oMeshes, oGlobalMesh);
	};

	struct OctaneGeoNodes : public OctaneNodeBase {
		const static PacketType packetType = GET_GEO_NODES;
		int32_t						iMeshNodeType;
		std::set<std::string>		sMeshNames;
		OctaneGeoNodes() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(iMeshNodeType, sMeshNames);
	};

	struct OctaneObject : public OctaneNodeBase {
		std::string					sObjectName;
		std::string					sMeshName;
		int32_t						iInstanceSize;
		MatrixF						oMatrix;
		std::map<float, MatrixF>	oMotionMatrices;
		int32_t						iSamplesNum;
		int32_t						iInstanceId;
		bool						bMovable;
		bool						bUseObjectLayer;
		OctaneObjectLayer			oObjectLayer;		
		std::map<std::string, std::pair<uint32_t, uint32_t>>	oArrayInfo;
		OctaneObject() : OctaneNodeBase(Octane::NT_UNKNOWN) { iInstanceSize = 1; }
		MSGPACK_DEFINE(sObjectName, sMeshName, iInstanceSize, bMovable, bUseObjectLayer, iSamplesNum, oObjectLayer, oArrayInfo, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneObjects : public OctaneNodeBase {
		const static PacketType packetType = LOAD_OBJECT;

		bool						bGlobal;
		int32_t						iCurrentFrameIdx;
		int32_t						iTotalFrameIdx;
		std::vector<OctaneObject>	oObjects;
		std::unordered_map<std::string, std::vector<uint32_t>> iInstanceIDMap;
		std::unordered_map<std::string, std::vector<float>> fMatrixMap;
		int32_t*					iData;
		float*						fData;
		OctaneObjects() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(bGlobal, iCurrentFrameIdx, iTotalFrameIdx, oObjects, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneLight : public OctaneNodeBase {
		const static PacketType packetType = LOAD_LIGHT;

		std::string					sLightName;
		std::string					sShaderName;
		int32_t						iLightNodeType;
		float_3						f3Direction;		
		std::string					sLightObjectPath;
		std::string					sLightMeshName;
		std::string					sLightMatMapName;
		OctaneObject				oObject;
		OctaneLight() : OctaneNodeBase(Octane::NT_UNKNOWN) {}
		MSGPACK_DEFINE(sLightName, sShaderName, iLightNodeType, f3Direction, sLightObjectPath, sLightMeshName, sLightMatMapName, oObject, MSGPACK_BASE(OctaneNodeBase));
	};
}

#endif
// clang-format on
