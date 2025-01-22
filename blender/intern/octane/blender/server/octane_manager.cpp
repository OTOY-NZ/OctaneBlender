#include "octane_manager.h"

OctaneInfo::OctaneInfo()
{
  reset();
}

OctaneInfo::~OctaneInfo()
{
  reset();
}

void OctaneInfo::reset()
{
  node_type_to_name_.clear();
  legacy_node_type_to_name_.clear();
  node_type_to_static_pin_count_.clear();
  node_name_to_type_.clear();
  legacy_node_name_to_type_.clear();
  pin_id_to_pin_info_.clear();
  pin_name_to_pin_info_.clear();
  attribute_id_to_attribute_info_.clear();
  attribute_name_to_attribute_info_.clear();
  octane_id_to_legacy_data_info_.clear();
  blender_name_to_legacy_data_info_.clear();
  need_new_custom_node_legacy_names_.clear();
  // Configure the legacy nodes to be handled as new custom node
  need_new_custom_node_legacy_names_ = {"ShaderNodeOctDiffuseMat",
                                        "ShaderNodeOctPortalMat",
                                        "ShaderNodeOctMixMat",
                                        "ShaderNodeOctGlossyMat",
                                        "ShaderNodeOctSpecularMat",
                                        "ShaderNodeOctToonMat",
                                        "ShaderNodeOctMetalMat",
                                        "ShaderNodeOctUniversalMat",
                                        "ShaderNodeOctShadowCatcherMat",
                                        "ShaderNodeOctHairMat",
                                        "ShaderNodeOctNullMat",
                                        "ShaderNodeOctClippingMat",
                                        "ShaderNodeOctDiffuseLayer",
                                        "ShaderNodeOctMetallicLayer",
                                        "ShaderNodeOctSheenLayer",
                                        "ShaderNodeOctSpecularLayer",
                                        "ShaderNodeOctFloatTex",
                                        "ShaderNodeOctGaussSpectrumTex",
                                        "ShaderNodeOctChecksTex",
                                        "ShaderNodeOctMarbleTex",
                                        "ShaderNodeOctRidgedFractalTex",
                                        "ShaderNodeOctSawWaveTex",
                                        "ShaderNodeOctSineWaveTex",
                                        "ShaderNodeOctTriWaveTex",
                                        "ShaderNodeOctTurbulenceTex",
                                        "ShaderNodeOctNoiseTex",
                                        "ShaderNodeOctCinema4DNoiseTex",
                                        "ShaderNodeOctClampTex",
                                        "ShaderNodeOctCosineMixTex",
                                        "ShaderNodeOctInvertTex",
                                        "ShaderNodeOctMixTex",
                                        "ShaderNodeOctMultiplyTex",
                                        "ShaderNodeOctAddTex",
                                        "ShaderNodeOctSubtractTex",
                                        "ShaderNodeOctCompareTex",
                                        "ShaderNodeOctTriplanarTex",
                                        "ShaderNodeOctFalloffTex",
                                        "ShaderNodeOctColorCorrectTex",
                                        "ShaderNodeOctFloatVertexTex",
                                        "ShaderNodeOctColorVertexTex",
                                        "ShaderNodeOctDirtTex",
                                        "ShaderNodeOctRandomColorTex",
                                        "ShaderNodeOctPolygonSideTex",
                                        "ShaderNodeOctChaosTex",
                                        "ShaderNodeOctChannelInverterTex",
                                        "ShaderNodeOctChannelMapperTex",
                                        "ShaderNodeOctChannelMergerTex",
                                        "ShaderNodeOctChannelPickerTex",
                                        "ShaderNodeOctRaySwitchTex",
                                        "ShaderNodeOctSpotlightTex",
                                        "ShaderNodeOctCompositeLayerTex",
                                        "ShaderNodeOctUVWTransformTex",
                                        "ShaderNodeOctInstanceRangeTex",
                                        "ShaderNodeOctWTex",
                                        "ShaderNodeOctBlackBodyEmission",
                                        "ShaderNodeOctTextureEmission",
                                        "ShaderNodeOctColorAovOutput",
                                        "ShaderNodeOctCompositeAovOutputLayer",
                                        "ShaderNodeOctRenderAovOutput",
                                        "ShaderNodeOctCaptureToCustomAOVTex",
                                        "ShaderNodeOctSurfaceTangentDPduTex",
                                        "ShaderNodeOctSurfaceTangentDPdvTex",
                                        "ShaderNodeOctFloatToGreyscaleTex",
                                        "ShaderNodeOctFloat3ToColorTex",
                                        "ShaderNodeOctFloatsToColorTex",
                                        "ShaderNodeOctGradientGeneratorTex",
                                        "ShaderNodeOctUVCoordinateTex",
                                        "ShaderNodeOctBinaryMathOperationTex",
                                        "ShaderNodeOctUnaryMathOperationTex",
                                        "ShaderNodeOctNormalTex",
                                        "ShaderNodeOctPositionTex",
                                        "ShaderNodeOctZDepthTex",
                                        "ShaderNodeOctSamplePositionTex",
                                        "ShaderNodeOctRelativeDistanceTex",
                                        "ShaderNodeOctRayDirectionTex",
                                        "ShaderNodeOctRandomMapTex",
                                        "ShaderNodeOctRangeTex",
                                        "ShaderNodeOctMapRangeAovOutput",
                                        "ShaderNodeOctColorCorrectionAovOutput",
                                        "ShaderNodeOctClampAovOutput",
                                        "ShaderNodeOctXYZProjection",
                                        "ShaderNodeOctBoxProjection",
                                        "ShaderNodeOctCylProjection",
                                        "ShaderNodeOctPerspProjection",
                                        "ShaderNodeOctSphericalProjection",
                                        "ShaderNodeOctUVWProjection",
                                        "ShaderNodeOctTriplanarProjection",
                                        "ShaderNodeOctSamplePosToUVProjection",
                                        "ShaderNodeOctMatCapProjection",
                                        "ShaderNodeOctColorToUVWProjection",
                                        "ShaderNodeOctRotateTransform",
                                        "ShaderNodeOctScaleTransform",
                                        "ShaderNodeOct2DTransform",
                                        "ShaderNodeOct3DTransform"};
}

void OctaneInfo::add_node_name(int32_t node_type, std::string node_name)
{
  node_type_to_name_[node_type] = node_name;
  node_name_to_type_[node_name] = node_type;
}

void OctaneInfo::add_legacy_node_name(int32_t node_type, std::string node_name)
{
  legacy_node_type_to_name_[node_type] = node_name;
  legacy_node_name_to_type_[node_name] = node_type;
}

bool OctaneInfo::need_to_use_new_custom_node(std::string node_bl_idname)
{
  return need_new_custom_node_legacy_names_.find(node_bl_idname) !=
         need_new_custom_node_legacy_names_.end();
}

const LegacyDataInfoPtr OctaneInfo::get_legacy_data_info(int32_t node_type,
                                                         int32_t octane_id,
                                                         bool is_pin)
{
  const LegacyDataInfoIdMap &legacy_data_info = get_legacy_data_info_id_map(node_type);
  if (!is_pin) {
    octane_id *= -1;
  }
  if (legacy_data_info.find(octane_id) != legacy_data_info.end()) {
    return legacy_data_info.at(octane_id);
  }
  return nullptr;
}

void OctaneInfo::add_attribute_info(int32_t node_type,
                                    std::string blender_name,
                                    int32_t attribute_id,
                                    std::string attribute_name,
                                    int32_t attribute_type)
{
  AttributeInfoPtr attribute_info_ptr = std::make_shared<AttributeInfo>();
  attribute_info_ptr->blender_name_ = blender_name;
  attribute_info_ptr->id_ = attribute_id;
  attribute_info_ptr->name_ = attribute_name;
  attribute_info_ptr->attribute_type_ = attribute_type;
  attribute_id_to_attribute_info_[node_type][attribute_id] = attribute_info_ptr;
  attribute_name_to_attribute_info_[node_type][attribute_name] = attribute_info_ptr;
}

void OctaneInfo::add_pin_info(int32_t node_type,
                              std::string blender_name,
                              int32_t pin_id,
                              std::string pin_name,
                              int32_t pin_index,
                              int32_t pin_type,
                              int32_t socket_type,
                              int32_t default_node_type,
                              std::string default_node_name)
{
  PinInfoPtr pin_info_ptr = std::make_shared<PinInfo>();
  pin_info_ptr->blender_name_ = blender_name;
  pin_info_ptr->id_ = pin_id;
  pin_info_ptr->name_ = pin_name;
  pin_info_ptr->index_ = pin_index;
  pin_info_ptr->pin_type_ = pin_type;
  pin_info_ptr->socket_type_ = socket_type;
  pin_info_ptr->default_node_type_ = default_node_type;
  pin_info_ptr->default_node_name_ = default_node_name;
  pin_info_ptr->use_as_legacy_attribute_ = false;
  pin_id_to_pin_info_[node_type][pin_id] = pin_info_ptr;
  pin_name_to_pin_info_[node_type][pin_name] = pin_info_ptr;
}

void OctaneInfo::add_legacy_data_info(int32_t node_type,
                                      std::string name,
                                      bool is_socket,
                                      int32_t socket_data_type,
                                      bool is_pin,
                                      int32_t octane_type,
                                      bool is_internal_data,
                                      bool is_internal_data_pin,
                                      int32_t internal_data_octane_type)
{
  LegacyDataInfoPtr legacy_data_info_ptr = std::make_shared<LegacyDataInfo>();
  legacy_data_info_ptr->name_ = name;
  legacy_data_info_ptr->is_socket_ = is_socket;
  legacy_data_info_ptr->data_type_ = socket_data_type;
  legacy_data_info_ptr->is_pin_ = is_pin;
  legacy_data_info_ptr->octane_type_ = octane_type;
  legacy_data_info_ptr->is_internal_data_ = is_internal_data;
  legacy_data_info_ptr->is_internal_data_pin_ = is_internal_data_pin;
  legacy_data_info_ptr->internal_data_octane_type_ = internal_data_octane_type;
  int32_t octane_id = is_internal_data ? internal_data_octane_type : octane_type;
  if (!is_pin) {
    // use minus value to represent attribute id
    octane_id *= -1;
  }
  octane_id_to_legacy_data_info_[node_type][octane_id] = legacy_data_info_ptr;
  blender_name_to_legacy_data_info_[node_type][name] = legacy_data_info_ptr;
}

void OctaneInfo::set_static_pin_count(int32_t node_type, int32_t pin_count)
{
  node_type_to_static_pin_count_[node_type] = pin_count;
}

OctaneManager::OctaneManager()
{
  mSyncedResources.resize(OctaneResourceType::LAST_TYPE + 1);
}

OctaneManager::~OctaneManager()
{
  Reset();
}

void OctaneManager::Reset()
{
  for (int i = 0; i < mSyncedResources.size(); ++i) {
    mSyncedResources[i].clear();
  }
  mResharpableCandidates.clear();
  mMovableCandidates.clear();
}

bool OctaneManager::IsResourceSynced(std::string name, OctaneResourceType type)
{
  return mSyncedResources[type].find(name) != mSyncedResources[type].end();
}

void OctaneManager::SyncedResource(std::string name, OctaneResourceType type)
{
  mSyncedResources[type].insert(name);
}

void OctaneManager::UnsyncedResource(std::string name, OctaneResourceType type)
{
  if (mSyncedResources[type].find(name) != mSyncedResources[type].end()) {
    mSyncedResources[type].erase(name);
  }
}

bool OctaneManager::IsResharpableCandidate(std::string name)
{
  return mResharpableCandidates.find(name) != mResharpableCandidates.end();
}

bool OctaneManager::IsMovableCandidate(std::string name)
{
  return mMovableCandidates.find(name) != mMovableCandidates.end();
}

void OctaneManager::TagResharpableCandidate(std::string name)
{
  mResharpableCandidates.insert(name);
}

void OctaneManager::TagMovableCandidate(std::string name)
{
  mMovableCandidates.insert(name);
}

void OctaneManager::UntagResharpableCandidate(std::string name)
{
  if (mResharpableCandidates.find(name) != mResharpableCandidates.end()) {
    mResharpableCandidates.erase(name);
  }
}

void OctaneManager::UntagMovableCandidate(std::string name)
{
  if (mMovableCandidates.find(name) != mMovableCandidates.end()) {
    mMovableCandidates.erase(name);
  }
}