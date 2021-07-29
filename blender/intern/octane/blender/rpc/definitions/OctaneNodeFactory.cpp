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

		OCTANE_NODE_CREATOR(OctaneDiffuseMaterial);
		OCTANE_NODE_CREATOR(OctaneMixMaterial);
		OCTANE_NODE_CREATOR(OctanePortalMaterial);
		OCTANE_NODE_CREATOR(OctaneGlossyMaterial);
		OCTANE_NODE_CREATOR(OctaneSpecularMaterial);
		OCTANE_NODE_CREATOR(OctaneToonMaterial);
		OCTANE_NODE_CREATOR(OctaneMetalMaterial);
		OCTANE_NODE_CREATOR(OctaneUniversalMaterial);
		OCTANE_NODE_CREATOR(OctaneShadowCatcherMaterial);
		OCTANE_NODE_CREATOR(OctaneLayeredMaterial);
		OCTANE_NODE_CREATOR(OctaneCompositeMaterial);
		OCTANE_NODE_CREATOR(OctaneHairMaterial);
		OCTANE_NODE_CREATOR(OctaneNullMaterial);
		OCTANE_NODE_CREATOR(OctaneGroupLayer);
		OCTANE_NODE_CREATOR(OctaneDiffuseLayer);
		OCTANE_NODE_CREATOR(OctaneMetallicLayer);
		OCTANE_NODE_CREATOR(OctaneSheenLayer);
		OCTANE_NODE_CREATOR(OctaneSpecularLayer);

		OCTANE_NODE_CREATOR(OctaneGrayscaleColorTexture);
		OCTANE_NODE_CREATOR(OctaneRGBSpectrumTexture);
		OCTANE_NODE_CREATOR(OctaneGaussianSpectrumTexture);
		OCTANE_NODE_CREATOR(OctaneChecksTexture);
		OCTANE_NODE_CREATOR(OctaneMarbleTexture);
		OCTANE_NODE_CREATOR(OctaneRidgedFractalTexture);
		OCTANE_NODE_CREATOR(OctaneSawWaveTexture);
		OCTANE_NODE_CREATOR(OctaneSineWaveTexture);
		OCTANE_NODE_CREATOR(OctaneTriangleWaveTexture);
		OCTANE_NODE_CREATOR(OctaneTurbulenceTexture);
		OCTANE_NODE_CREATOR(OctaneNoiseTexture);
		OCTANE_NODE_CREATOR(OctaneCinema4DNoiseTexture);
		OCTANE_NODE_CREATOR(OctaneClampTexture);
		OCTANE_NODE_CREATOR(OctaneCosineMixTexture);
		OCTANE_NODE_CREATOR(OctaneInvertTexture);
		OCTANE_NODE_CREATOR(OctaneMixTexture);
		OCTANE_NODE_CREATOR(OctaneMultiplyTexture);
		OCTANE_NODE_CREATOR(OctaneAddTexture);
		OCTANE_NODE_CREATOR(OctaneSubtractTexture);
		OCTANE_NODE_CREATOR(OctaneCompareTexture);
		OCTANE_NODE_CREATOR(OctaneTriplanarTexture);
		OCTANE_NODE_CREATOR(OctaneFalloffTexture);
		OCTANE_NODE_CREATOR(OctaneColorCorrectTexture);
		OCTANE_NODE_CREATOR(OctaneChaosTexture);
		OCTANE_NODE_CREATOR(OctaneImageData);
		OCTANE_NODE_CREATOR(OctaneImageTexture);
		OCTANE_NODE_CREATOR(OctaneImageTileTexture);
		OCTANE_NODE_CREATOR(OctaneFloatVertexAttributeTexture);
		OCTANE_NODE_CREATOR(OctaneColorVertexAttributeTexture);
		OCTANE_NODE_CREATOR(OctaneInstanceColorTexture);
		OCTANE_NODE_CREATOR(OSLNodeInfo);
		OCTANE_NODE_CREATOR(OctaneOSLTexture);
		OCTANE_NODE_CREATOR(OctaneOSLProjection);
		OCTANE_NODE_CREATOR(OctaneOSLCamera);
		OCTANE_NODE_CREATOR(OctaneOSLBakingCamera);
		OCTANE_NODE_CREATOR(OctaneVectron);
		OCTANE_NODE_CREATOR(OctaneFloatImageTexture);
		OCTANE_NODE_CREATOR(OctaneAlphaImageTexture);
		OCTANE_NODE_CREATOR(OctaneDirtTexture);
		OCTANE_NODE_CREATOR(OctaneGradientTexture);
		OCTANE_NODE_CREATOR(OctaneToonRampTexture);
		OCTANE_NODE_CREATOR(OctaneVolumeRampTexture);
		OCTANE_NODE_CREATOR(OctaneRandomColorTexture);
		OCTANE_NODE_CREATOR(OctanePolygonSideTexture);
		OCTANE_NODE_CREATOR(OctaneDisplacementTexture);
		OCTANE_NODE_CREATOR(OctaneVertexDisplacementTexture);
		OCTANE_NODE_CREATOR(OctaneVertexDisplacementMixer);
		OCTANE_NODE_CREATOR(OctaneBakingTexture);
		OCTANE_NODE_CREATOR(OctaneUVWTransformTexture);
		OCTANE_NODE_CREATOR(OctaneInstaceRangeTexture);
		OCTANE_NODE_CREATOR(OctaneWTexture);
		OCTANE_NODE_CREATOR(OctaneBlackBodyEmission);
		OCTANE_NODE_CREATOR(OctaneTextureEmission);
		OCTANE_NODE_CREATOR(OctaneToonPointLight);
		OCTANE_NODE_CREATOR(OctaneToonDirectionalLight);
		OCTANE_NODE_CREATOR(OctaneSchlick);
		OCTANE_NODE_CREATOR(OctaneAbsorptionMedium);
		OCTANE_NODE_CREATOR(OctaneScatteringMedium);
		OCTANE_NODE_CREATOR(OctaneVolumeMedium);
		OCTANE_NODE_CREATOR(OctaneRandomWalkMedium);

		OCTANE_NODE_CREATOR(OctaneChannelInverterTexture);
		OCTANE_NODE_CREATOR(OctaneChannelMapperTexture);
		OCTANE_NODE_CREATOR(OctaneChannelMergerTexture);
		OCTANE_NODE_CREATOR(OctaneChannelPickerTexture);
		OCTANE_NODE_CREATOR(OctaneRaySwitchTexture);
		OCTANE_NODE_CREATOR(OctaneSpotlightTexture);
		OCTANE_NODE_CREATOR(OctaneCompositeLayerTexture);
		OCTANE_NODE_CREATOR(OctaneCompositeTexture);

		OCTANE_NODE_CREATOR(OctaneFloatValue);
		OCTANE_NODE_CREATOR(OctaneIntValue);
		OCTANE_NODE_CREATOR(OctaneSunDirection);
		OCTANE_NODE_CREATOR(OctaneRoundEdges);

		OCTANE_NODE_CREATOR(OctaneXYZProjection);
		OCTANE_NODE_CREATOR(OctaneBoxProjection);
		OCTANE_NODE_CREATOR(OctaneCylindricalProjection);
		OCTANE_NODE_CREATOR(OctanePerspectiveProjection);
		OCTANE_NODE_CREATOR(OctaneSphericalProjection);
		OCTANE_NODE_CREATOR(OctaneMeshProjection);
		OCTANE_NODE_CREATOR(OctaneTriplanarProjection);
		OCTANE_NODE_CREATOR(OctaneOSLUVProjection);

		OCTANE_NODE_CREATOR(OctaneRotationTransform);
		OCTANE_NODE_CREATOR(OctaneScaleTransform);
		OCTANE_NODE_CREATOR(OctaneValueTransform);
		OCTANE_NODE_CREATOR(Octane2DTransform);
		OCTANE_NODE_CREATOR(Octane3DTransform);

		OCTANE_NODE_CREATOR(OctaneVolume);
		OCTANE_NODE_CREATOR(OctaneVolumeInfo);

		OCTANE_NODE_CREATOR(OctaneScatterToolSurface);
		OCTANE_NODE_CREATOR(OctaneScatterToolVolume);

		OCTANE_NODE_CREATOR(OctaneOCIOInfo);

		OCTANE_NODE_CREATOR(OctanePlacement);
		OCTANE_NODE_CREATOR(OctaneGeometryGroup);

		OCTANE_NODE_CREATOR(OctaneAovOutputGroup);
		OCTANE_NODE_CREATOR(OctaneColorAovOutput);
		OCTANE_NODE_CREATOR(OctaneCompositeAovOutput);
		OCTANE_NODE_CREATOR(OctaneCompositeAovOutputLayer);
		OCTANE_NODE_CREATOR(OctaneImageAovOutput);
		OCTANE_NODE_CREATOR(OctaneRenderAovOutput);
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
		return node;
	}

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
