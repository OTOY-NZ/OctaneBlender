// clang-format off
#include "OctaneNodeFactory.h"

namespace OctaneDataTransferObject {

 	template<typename T>
	OctaneNodeBase* createOctaneNodeInstance(){ return new T(); }

	OctaneNodeFactory::OctaneNodeFactory() {
#ifndef OCTANE_NODE_CREATOR
#define OCTANE_NODE_CREATOR(NODE_CLASS) \
	do { \
			NODE_CLASS instance; \
			octaneToPluginTypeMap[instance.octaneType] = instance.pluginType; \
			pluginToOctaneTypeMap[instance.pluginType] = instance.octaneType; \
			creatorsMap[instance.octaneType] = &createOctaneNodeInstance<NODE_CLASS>; \
		} while (0)
#endif
		OCTANE_NODE_CREATOR(OctaneTextureEnvironment);
		OCTANE_NODE_CREATOR(OctaneDaylightEnvironment);
		OCTANE_NODE_CREATOR(OctanePlanetaryEnvironment);
		OCTANE_NODE_CREATOR(OctaneUniversalCamera);
		OCTANE_NODE_CREATOR(OctaneRenderPasses);
		OCTANE_NODE_CREATOR(OctaneCommand);
		OCTANE_NODE_CREATOR(OctaneDBNodes);
		OCTANE_NODE_CREATOR(OctaneSaveImage);
		OCTANE_NODE_CREATOR(OctaneCameraData);
		OCTANE_NODE_CREATOR(OctaneEngineData);
		OCTANE_NODE_CREATOR(OctaneOrbxPreview);
		OCTANE_NODE_CREATOR(OctaneGeoNode);

		OCTANE_NODE_CREATOR(OctaneLayeredMaterial);
		OCTANE_NODE_CREATOR(OctaneCompositeMaterial);
		OCTANE_NODE_CREATOR(OctaneGroupLayer);

		OCTANE_NODE_CREATOR(OctaneRGBSpectrumTexture);
		OCTANE_NODE_CREATOR(OctaneImageData);
		OCTANE_NODE_CREATOR(OctaneImageTexture);
		OCTANE_NODE_CREATOR(OctaneImageTileTexture);
		OCTANE_NODE_CREATOR(OctaneInstanceColorTexture);
		OCTANE_NODE_CREATOR(OSLNodeInfo);
		OCTANE_NODE_CREATOR(OctaneOSLTexture);
		OCTANE_NODE_CREATOR(OctaneOSLProjection);
		OCTANE_NODE_CREATOR(OctaneOSLCamera);
		OCTANE_NODE_CREATOR(OctaneOSLBakingCamera);
		OCTANE_NODE_CREATOR(OctaneVectron);
		OCTANE_NODE_CREATOR(OctaneFloatImageTexture);
		OCTANE_NODE_CREATOR(OctaneAlphaImageTexture);
		OCTANE_NODE_CREATOR(OctaneGradientTexture);
		OCTANE_NODE_CREATOR(OctaneToonRampTexture);
		OCTANE_NODE_CREATOR(OctaneVolumeRampTexture);
		OCTANE_NODE_CREATOR(OctaneDisplacementTexture);
		OCTANE_NODE_CREATOR(OctaneVertexDisplacementTexture);
		OCTANE_NODE_CREATOR(OctaneVertexDisplacementMixer);
		OCTANE_NODE_CREATOR(OctaneBakingTexture);
		OCTANE_NODE_CREATOR(OctaneToonPointLight);
		OCTANE_NODE_CREATOR(OctaneToonDirectionalLight);
		OCTANE_NODE_CREATOR(OctaneSchlick);
		OCTANE_NODE_CREATOR(OctaneAbsorptionMedium);
		OCTANE_NODE_CREATOR(OctaneScatteringMedium);
		OCTANE_NODE_CREATOR(OctaneVolumeMedium);
		OCTANE_NODE_CREATOR(OctaneRandomWalkMedium);

		OCTANE_NODE_CREATOR(OctaneCompositeTexture);

		OCTANE_NODE_CREATOR(OctaneFloatValue);
		OCTANE_NODE_CREATOR(OctaneIntValue);
		OCTANE_NODE_CREATOR(OctaneSunDirection);
		OCTANE_NODE_CREATOR(OctaneRoundEdges);

		OCTANE_NODE_CREATOR(OctaneOSLUVProjection);
		OCTANE_NODE_CREATOR(OctaneDistortedMeshUVProjection);

		OCTANE_NODE_CREATOR(OctaneValueTransform);

		OCTANE_NODE_CREATOR(OctaneVolume);
		OCTANE_NODE_CREATOR(OctaneVolumeInfo);

		OCTANE_NODE_CREATOR(OctaneScatterToolSurface);
		OCTANE_NODE_CREATOR(OctaneScatterToolVolume);

		OCTANE_NODE_CREATOR(OctaneOCIOInfo);

		OCTANE_NODE_CREATOR(OctanePlacement);
		OCTANE_NODE_CREATOR(OctaneGeometryGroup);

		OCTANE_NODE_CREATOR(OctaneAovOutputGroup);
		OCTANE_NODE_CREATOR(OctaneCompositeAovOutput);
		OCTANE_NODE_CREATOR(OctaneImageAovOutput);
		OCTANE_NODE_CREATOR(OctaneLightMixingAovOutput);

		OCTANE_NODE_CREATOR(OctaneReadVDBTexture);

		OCTANE_NODE_CREATOR(OctaneOcioColorSpace);

		OCTANE_NODE_CREATOR(OctaneCustomNode);
#undef OCTANE_NODE_CREATOR
	};

	int OctaneNodeFactory::GetOctaneNodeType(const std::string &pluginType) {
		if (pluginToOctaneTypeMap.find(pluginType) != pluginToOctaneTypeMap.end()){
			return pluginToOctaneTypeMap[pluginType];
		}
		return Octane::NT_UNKNOWN;
	}

	OctaneNodeBase* OctaneNodeFactory::CreateOctaneNode(const std::string &pluginType) {
		return CreateOctaneNode(GetOctaneNodeType(pluginType));
	}

	OctaneNodeBase* OctaneNodeFactory::CreateOctaneNode(int octaneType) {
		OctaneNodeBase* node = NULL;
		if (creatorsMap.find(octaneType) != creatorsMap.end()) {
			node = creatorsMap[octaneType]();
		}
		if (!node) {
			node = creatorsMap[Octane::ENT_CUSTOM_NODE]();
		}
		return node;
	}

#ifdef OCTANE_SERVER
	OctaneNodeBase* OctaneNodeFactory::CreateOctaneCustomNode(int octaneType) {
		OctaneNodeBase* node = NULL;
		switch (octaneType) {
		case Octane::NT_TEX_IMAGE:
		case Octane::NT_TEX_IMAGE_TILES:
		case Octane::NT_TEX_ALPHAIMAGE:
		case Octane::NT_TEX_FLOATIMAGE:
		case Octane::NT_TEX_BAKED_IMAGE:
		case Octane::NT_TOON_RAMP:
		case Octane::NT_TEX_GRADIENT:
		case Octane::NT_VOLUME_RAMP:
		case Octane::NT_TEX_OSL:
		case Octane::NT_PROJ_OSL:
		case Octane::NT_PROJ_OSL_UV:
		case Octane::NT_CAM_OSL:
		case Octane::NT_CAM_OSL_BAKING:
		case Octane::NT_VERTEX_DISPLACEMENT_MIXER:
		case Octane::NT_MAT_LAYER:
		case Octane::NT_MAT_COMPOSITE:
		case Octane::NT_MAT_LAYER_GROUP:
			node = OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(octaneType);
			break;
		default:
			node = creatorsMap[Octane::ENT_CUSTOM_NODE]();
			break;
		}
		return node;
	}
#endif

	NodeResourceType OctaneNodeFactory::GetNodeResourceType(const std::string &pluginType) {
		return GetNodeResourceType(GetOctaneNodeType(pluginType));
	}

	NodeResourceType OctaneNodeFactory::GetNodeResourceType(int octaneType) {
		switch (octaneType) {
		case Octane::NT_TEX_IMAGE:
		case Octane::NT_TEX_IMAGE_TILES:
		case Octane::NT_TEX_ALPHAIMAGE:
		case Octane::NT_TEX_FLOATIMAGE:
		case Octane::NT_TEX_BAKED_IMAGE:
			return NodeResourceType::TEXTURE;
		case Octane::NT_GEO_MESH:
			return NodeResourceType::GEOMETRY;
		default:
			return NodeResourceType::LIGHT;
		}
	}
}

OctaneDataTransferObject::OctaneNodeFactory GlobalOctaneNodeFactory;

// clang-format on
