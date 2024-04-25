#ifndef __OCTANE_DATA_TYPE_H__
#define __OCTANE_DATA_TYPE_H__

#include "blender/rpc/definitions/OctaneMesh.h"
#include "blender/rpc/definitions/OctaneNode.h"
#include "blender/rpc/definitions/OctaneNodeFactory.h"
#include "blender/rpc/definitions/OctanePinInfo.h"
#include "blender/rpc/definitions/OctaneProjection.h"
#include "blender/rpc/definitions/OctaneTransform.h"

namespace OctaneEngine {

using namespace Octane;
using OctaneDataTransferObject::float_2;
using OctaneDataTransferObject::float_3;
using OctaneDataTransferObject::float_4;
using OctaneDataTransferObject::int32_t;
using OctaneDataTransferObject::int64_t;
using OctaneDataTransferObject::int8_t;
using OctaneDataTransferObject::MatrixF;
using OctaneDataTransferObject::uint32_t;
using OctaneDataTransferObject::uint64_t;
using OctaneDataTransferObject::uint8_t;
using std::string;
using std::vector;

using OctaneDataTransferObject::int8_2;
using OctaneDataTransferObject::int8_3;
using OctaneDataTransferObject::int8_4;
using OctaneDataTransferObject::uint8_2;
using OctaneDataTransferObject::uint8_3;
using OctaneDataTransferObject::uint8_4;

using OctaneDataTransferObject::int32_2;
using OctaneDataTransferObject::int32_3;
using OctaneDataTransferObject::int32_4;
using OctaneDataTransferObject::uint32_2;
using OctaneDataTransferObject::uint32_3;
using OctaneDataTransferObject::uint32_4;

using OctaneDataTransferObject::int64_2;
using OctaneDataTransferObject::int64_3;
using OctaneDataTransferObject::int64_4;
using OctaneDataTransferObject::uint64_2;
using OctaneDataTransferObject::uint64_3;
using OctaneDataTransferObject::uint64_4;

using OctaneDataTransferObject::ComplexValue;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OCTANE SERVER
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/// Wrapper structure for the enum of the fail reasons returned by getFailReason().
struct FailReasons {
  /// The fail reasons returned by getFailReason().
  enum FailReasonsEnum {
    NONE = -1,      ///< No failure.
    UNKNOWN,        ///< Unknown fail reason.
    WRONG_VERSION,  ///< The OctaneEngine version differs from that of the current client
                    ///< library.
    NO_CONNECTION,  ///< No network connection to the server.
    NOT_ACTIVATED,  ///< The Octane license is not activated on the server. Use the activate()
                    ///< method to activate the license on the server.
    NO_GPUS         ///< No CUDA GPUs available on a server.
  };                // enum FailReasonsEnum
};

/// Wrapper structure for the enum of the types of scene export.
struct SceneExportTypes {
  /// Type of scene export.
  enum SceneExportTypesEnum {
    NONE = 0,  ///< No export, just render.
    ALEMBIC,   ///< Export alembic file.
    ORBX       ///< Export ORBX file.
  };           // enum SceneExportTypesEnum
};

/// The type of the rendered image.
enum ImageType {
  IMAGE_8BIT = 0,         ///< RGBA 8 bit per channel image.
  IMAGE_FLOAT,            ///< RGBA 32 bit per channel image.
  IMAGE_FLOAT_TONEMAPPED  ///< RGBA 32 bit per channel tonemapped image.
};                        // enum ImageType

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Camera
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a camera data that is going to be uploaded to the Octane server.
struct CameraMotionParam {
  float_3 f3EyePoint;
  float_3 f3LookAt;
  float_3 f3UpVector;
  float fFOV;

  inline bool operator!=(const CameraMotionParam &other)
  {
    return f3EyePoint != other.f3EyePoint || f3LookAt != other.f3LookAt ||
           f3UpVector != other.f3UpVector || fFOV != other.fFOV;
  }

  inline bool operator==(const CameraMotionParam &other)
  {
    return f3EyePoint == other.f3EyePoint && f3LookAt == other.f3LookAt &&
           f3UpVector == other.f3UpVector && fFOV == other.fFOV;
  }

  inline CameraMotionParam &operator=(const CameraMotionParam &other)
  {
    if (f3EyePoint != other.f3EyePoint)
      f3EyePoint = other.f3EyePoint;
    if (f3LookAt != other.f3LookAt)
      f3LookAt = other.f3LookAt;
    if (f3UpVector != other.f3UpVector)
      f3UpVector = other.f3UpVector;
    if (fFOV != other.fFOV)
      fFOV = other.fFOV;
    return *this;
  }
};

struct CameraMotionParams {
  std::map<float, CameraMotionParam> motions;

  inline bool equal(const CameraMotionParams &other)
  {
    bool result = motions.size() == other.motions.size();
    if (result) {
      for (auto it : other.motions) {
        if (motions.find(it.first) == motions.end() || motions.at(it.first) != it.second) {
          result = false;
          break;
        }
      }
    }
    return result;
  }

  inline bool operator!=(const CameraMotionParams &other)
  {
    return !equal(other);
  }

  inline bool operator==(const CameraMotionParams &other)
  {
    return equal(other);
  }

  inline CameraMotionParams &operator=(const CameraMotionParams &other)
  {
    if (!equal(other)) {
      motions.clear();
      motions = other.motions;
    }
    return *this;
  }
};  // namespace OctaneEngine

struct Camera {
  enum CameraType { CAMERA_PERSPECTIVE, CAMERA_PANORAMA, CAMERA_BAKING, NONE };

  CameraType type;

  bool bUseRegion;
  bool bUseBlenderCamera;
  bool bUseUniversalCamera;
  bool bUseCameraDimensionAsPreviewResolution;
  uint32_4 ui4Region;
  uint32_2 ui2BlenderCameraDimension;
  float_2 f2BlenderCameraCenter;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Camera
  float_3 f3EyePoint;
  float_3 f3LookAt;
  float_3 f3UpVector;
  float fFOV;  // Holds ortho scale in the case of orthographic camera
  float fFOVx;
  float fFOVy;
  CameraMotionParams oMotionParams;
  bool bUseFstopValue;
  float fAperture;
  float fApertureEdge;
  float fDistortion;
  bool bAutofocus;
  float fFocalDepth;
  float fNearClipDepth;
  float fFarClipDepth;
  float_2 f2LensShift;
  bool bPerspCorr;
  float fStereoDist;
  float fStereoDistFalloff;
  float fTolerance;
  bool bOrtho;
  PanoramicCameraMode panCamMode;
  StereoMode stereoMode;
  StereoOutput stereoOutput;
  int32_t iBakingGroupId;
  int32_t iPadding;
  int32_t iUvSet;
  bool bBakeOutwards;
  bool bUseBakingPosition;
  bool bBackfaceCulling;
  float_3 f3LeftFilter, f3RightFilter;
  float fPixelAspect, fApertureAspect, fBlackoutLat;
  float fBokehRotation, fBokehRoundness;
  int32_t iBokehSidecount;
  bool bKeepUpright;
  float_2 f2UVboxMin;
  float_2 f2UVboxSize;
  float_3 f3UVWBakingTransformTranslation;
  float_3 f3UVWBakingTransformRotation;
  float_3 f3UVWBakingTransformScale;
  int32_t iUVWBakingTransformRotationOrder;
  std::string sOSLCameraNodeName;
  std::string sOSLCameraNodeMaterialName;
  bool bUseOSLCamera;
  bool bPreviewCameraMode;
  OctaneDataTransferObject::OctaneUniversalCamera universalCamera;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Imager
  bool bEnableImager;
  float_3 f3WhiteBalance;
  int32_t iCameraImagerOrder;
  int32_t iResponseCurve;
  float fExposure;
  float fGamma;
  float fVignetting;
  float fSaturation;
  float fHotPixelFilter;
  bool bPremultipliedAlpha;
  int32_t iMinDisplaySamples;
  bool bDithering;
  float fWhiteSaturation;
  bool bACESToneMapping;
  float fHighlightCompression;
  int32_t iMaxTonemapInterval;
  bool bNeutralResponse;
  bool bDisablePartialAlpha;
  bool bSwapEyes;
  std::string sCustomLut;
  float fLutStrength;

  // Ocio
  std::string sOcioViewDisplay;
  std::string sOcioViewDisplayView;
  std::string sOcioLook;
  bool bForceToneMapping;

  // Denoiser
  bool bEnableDenoiser;
  bool bDenoiseVolumes;
  bool bDenoiseOnCompletion;
  int32_t iMinDenoiserSample;
  int32_t iMaxDenoiserInterval;
  float fDenoiserBlend;

  // AI Up-Sampler
  int32_t iSamplingMode;
  bool bEnableAIUpSampling;
  bool bUpSamplingOnCompletion;
  int32_t iMinUpSamplerSamples;
  int32_t iMaxUpSamplerInterval;

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Postprocessor
  bool bUsePostprocess;
  float fCutoff;
  float fBloomPower;
  float fGlarePower;
  int32_t iGlareRayCount;
  float fGlareAngle;
  float fGlareBlur;
  float fSpectralIntencity;
  float fSpectralShift;
  float fSpreadStart;
  float fSpreadEnd;
  float fChromaticAberrationIntensity;
  float fLensFlare;
  float fLensFlareExtent;
  bool bScaleWithFilm;
  bool bLightBeams;
  float fMediumDensityForPostfxLightBeams;
  bool bEnableFog;
  float fFogExtinctionDistance;
  float fFogBaseLevel;
  float fFogHalfDensityHeight;
  float fFogEnvContribution;
  float_3 f3BaseFogColor;
  float fMediumRadius;

  inline Camera() : type(NONE)
  {
  }
  inline bool operator!=(const Camera &otherCam)
  {
    return (
        type != otherCam.type

        || bUseRegion != otherCam.bUseRegion || bUseBlenderCamera != otherCam.bUseBlenderCamera ||
        bUseUniversalCamera != otherCam.bUseUniversalCamera ||
        bUseCameraDimensionAsPreviewResolution !=
            otherCam.bUseCameraDimensionAsPreviewResolution ||
        ui4Region != otherCam.ui4Region ||
        ui2BlenderCameraDimension != otherCam.ui2BlenderCameraDimension ||
        f2BlenderCameraCenter != otherCam.f2BlenderCameraCenter ||
        f3EyePoint != otherCam.f3EyePoint || f3LookAt != otherCam.f3LookAt ||
        f3UpVector != otherCam.f3UpVector || fFOV != otherCam.fFOV || fFOVx != otherCam.fFOVx ||
        fFOVy != otherCam.fFOVy || oMotionParams != otherCam.oMotionParams ||
        bUseFstopValue != otherCam.bUseFstopValue || fAperture != otherCam.fAperture ||
        fApertureEdge != otherCam.fApertureEdge || fDistortion != otherCam.fDistortion ||
        bAutofocus != otherCam.bAutofocus || fFocalDepth != otherCam.fFocalDepth ||
        fNearClipDepth != otherCam.fNearClipDepth || fFarClipDepth != otherCam.fFarClipDepth ||
        f2LensShift != otherCam.f2LensShift || bPerspCorr != otherCam.bPerspCorr ||
        fStereoDist != otherCam.fStereoDist || fStereoDistFalloff != otherCam.fStereoDistFalloff ||
        fTolerance != otherCam.fTolerance || bOrtho != otherCam.bOrtho ||
        panCamMode != otherCam.panCamMode || stereoMode != otherCam.stereoMode ||
        stereoOutput != otherCam.stereoOutput || iBakingGroupId != otherCam.iBakingGroupId ||
        iPadding != otherCam.iPadding || iUvSet != otherCam.iUvSet ||
        bBakeOutwards != otherCam.bBakeOutwards ||
        bUseBakingPosition != otherCam.bUseBakingPosition || f2UVboxMin != otherCam.f2UVboxMin ||
        f2UVboxSize != otherCam.f2UVboxSize || bBackfaceCulling != otherCam.bBackfaceCulling ||
        f3LeftFilter != otherCam.f3LeftFilter || f3RightFilter != otherCam.f3RightFilter ||
        fPixelAspect != otherCam.fPixelAspect || fApertureAspect != otherCam.fApertureAspect ||
        fBlackoutLat != otherCam.fBlackoutLat || bKeepUpright != otherCam.bKeepUpright ||
        fBokehRotation != otherCam.fBokehRotation || fBokehRoundness != otherCam.fBokehRoundness ||
        iBokehSidecount != otherCam.iBokehSidecount

        || bEnableImager != otherCam.bEnableImager || f3WhiteBalance != otherCam.f3WhiteBalance ||
        iResponseCurve != otherCam.iResponseCurve ||
        iCameraImagerOrder != otherCam.iCameraImagerOrder || fExposure != otherCam.fExposure ||
        fGamma != otherCam.fGamma || fVignetting != otherCam.fVignetting ||
        fSaturation != otherCam.fSaturation || fHotPixelFilter != otherCam.fHotPixelFilter ||
        bPremultipliedAlpha != otherCam.bPremultipliedAlpha ||
        bACESToneMapping != otherCam.bACESToneMapping ||
        iMinDisplaySamples != otherCam.iMinDisplaySamples || bDithering != otherCam.bDithering ||
        fWhiteSaturation != otherCam.fWhiteSaturation ||
        fHighlightCompression != otherCam.fHighlightCompression ||
        iMaxTonemapInterval != otherCam.iMaxTonemapInterval ||
        bNeutralResponse != otherCam.bNeutralResponse ||
        bDisablePartialAlpha != otherCam.bDisablePartialAlpha || bSwapEyes != otherCam.bSwapEyes ||
        sCustomLut != otherCam.sCustomLut || fLutStrength != otherCam.fLutStrength ||
        sOcioLook != otherCam.sOcioLook || sOcioViewDisplay != otherCam.sOcioViewDisplay ||
        sOcioViewDisplayView != otherCam.sOcioViewDisplayView ||
        bForceToneMapping != otherCam.bForceToneMapping

        || bEnableDenoiser != otherCam.bEnableDenoiser ||
        bDenoiseVolumes != otherCam.bDenoiseVolumes ||
        bDenoiseOnCompletion != otherCam.bDenoiseOnCompletion ||
        iMinDenoiserSample != otherCam.iMinDenoiserSample ||
        iMaxDenoiserInterval != otherCam.iMaxDenoiserInterval ||
        fDenoiserBlend != otherCam.fDenoiserBlend

        || iSamplingMode != otherCam.iSamplingMode ||
        bEnableAIUpSampling != otherCam.bEnableAIUpSampling ||
        bUpSamplingOnCompletion != otherCam.bUpSamplingOnCompletion ||
        iMinUpSamplerSamples != otherCam.iMinUpSamplerSamples ||
        iMaxUpSamplerInterval != otherCam.iMaxUpSamplerInterval

        || bUsePostprocess != otherCam.bUsePostprocess || fBloomPower != otherCam.fBloomPower ||
        fCutoff != otherCam.fCutoff || fGlarePower != otherCam.fGlarePower ||
        iGlareRayCount != otherCam.iGlareRayCount || fGlareAngle != otherCam.fGlareAngle ||
        fGlareBlur != otherCam.fGlareBlur || fSpectralIntencity != otherCam.fSpectralIntencity ||
        fSpectralShift != otherCam.fSpectralShift || fSpreadStart != otherCam.fSpreadStart ||
        fSpreadEnd != otherCam.fSpreadEnd ||
        fChromaticAberrationIntensity != otherCam.fChromaticAberrationIntensity ||
        fLensFlare != otherCam.fLensFlare || fLensFlareExtent != otherCam.fLensFlareExtent ||
        bLightBeams != otherCam.bLightBeams ||
        bScaleWithFilm != otherCam.bScaleWithFilm ||
        fMediumDensityForPostfxLightBeams != otherCam.fMediumDensityForPostfxLightBeams ||
        bEnableFog != otherCam.bEnableFog || fFogExtinctionDistance != otherCam.fFogExtinctionDistance ||
        fFogBaseLevel != otherCam.fFogBaseLevel ||
        fFogHalfDensityHeight != otherCam.fFogHalfDensityHeight ||
        fFogEnvContribution != otherCam.fFogEnvContribution ||
        f3BaseFogColor != otherCam.f3BaseFogColor || fMediumRadius != otherCam.fMediumRadius ||
        universalCamera.iCameraMode.iVal != otherCam.universalCamera.iCameraMode.iVal ||
        universalCamera.fSensorWidth.fVal != otherCam.universalCamera.fSensorWidth.fVal ||
        universalCamera.fFocalLength.fVal != otherCam.universalCamera.fFocalLength.fVal ||
        universalCamera.fFstop.fVal != otherCam.universalCamera.fFstop.fVal ||
        universalCamera.bUseFstop.bVal != otherCam.universalCamera.bUseFstop.bVal ||
        universalCamera.fFieldOfView.fVal != otherCam.universalCamera.fFieldOfView.fVal ||
        universalCamera.fScaleOfView.fVal != otherCam.universalCamera.fScaleOfView.fVal ||
        universalCamera.f2LensShift.fVal != otherCam.universalCamera.f2LensShift.fVal ||
        universalCamera.fPixelAspectRatio.fVal !=
            otherCam.universalCamera.fPixelAspectRatio.fVal ||
        universalCamera.bPerspectiveCorrection.bVal !=
            otherCam.universalCamera.bPerspectiveCorrection.bVal ||
        universalCamera.fFisheyeAngle.fVal != otherCam.universalCamera.fFisheyeAngle.fVal ||
        universalCamera.iFisheyeType.iVal != otherCam.universalCamera.iFisheyeType.iVal ||
        universalCamera.bHardVignette.bVal != otherCam.universalCamera.bHardVignette.bVal ||
        universalCamera.iFisheyeProjection.iVal !=
            otherCam.universalCamera.iFisheyeProjection.iVal ||
        universalCamera.fHorizontalFiledOfView.fVal !=
            otherCam.universalCamera.fHorizontalFiledOfView.fVal ||
        universalCamera.fVerticalFiledOfView.fVal !=
            otherCam.universalCamera.fVerticalFiledOfView.fVal ||
        universalCamera.iCubemapLayout.iVal != otherCam.universalCamera.iCubemapLayout.iVal ||
        universalCamera.bEquiAngularCubemap.bVal !=
            otherCam.universalCamera.bEquiAngularCubemap.bVal ||
        universalCamera.bUseDistortionTexture.bVal !=
            otherCam.universalCamera.bUseDistortionTexture.bVal ||
        universalCamera.sDistortionTexture.sLinkNodeName !=
            otherCam.universalCamera.sDistortionTexture.sLinkNodeName ||
        universalCamera.fSphereDistortion.fVal !=
            otherCam.universalCamera.fSphereDistortion.fVal ||
        universalCamera.fBarrelDistortion.fVal !=
            otherCam.universalCamera.fBarrelDistortion.fVal ||
        universalCamera.fBarrelDistortionCorners.fVal !=
            otherCam.universalCamera.fBarrelDistortionCorners.fVal ||
        universalCamera.fSphereAberration.fVal !=
            otherCam.universalCamera.fSphereAberration.fVal ||
        universalCamera.fComa.fVal != otherCam.universalCamera.fComa.fVal ||
        universalCamera.fAstigmatism.fVal != otherCam.universalCamera.fAstigmatism.fVal ||
        universalCamera.fFieldCurvature.fVal != otherCam.universalCamera.fFieldCurvature.fVal ||
        universalCamera.fNearClipDepth.fVal != otherCam.universalCamera.fNearClipDepth.fVal ||
        universalCamera.fFarClipDepth.fVal != otherCam.universalCamera.fFarClipDepth.fVal ||
        universalCamera.bAutoFocus.bVal != otherCam.universalCamera.bAutoFocus.bVal ||
        universalCamera.fFocalDepth.fVal != otherCam.universalCamera.fFocalDepth.fVal ||
        universalCamera.fAperture.fVal != otherCam.universalCamera.fAperture.fVal ||
        universalCamera.fApertureAspectRatio.fVal !=
            otherCam.universalCamera.fApertureAspectRatio.fVal ||
        universalCamera.iApertureShape.iVal != otherCam.universalCamera.iApertureShape.iVal ||
        universalCamera.fApertureEdge.fVal != otherCam.universalCamera.fApertureEdge.fVal ||
        universalCamera.iApertureBladeCount.iVal !=
            otherCam.universalCamera.iApertureBladeCount.iVal ||
        universalCamera.fApertureRotation.fVal !=
            otherCam.universalCamera.fApertureRotation.fVal ||
        universalCamera.fApertureRoundedness.fVal !=
            otherCam.universalCamera.fApertureRoundedness.fVal ||
        universalCamera.fCentralObstruction.fVal !=
            otherCam.universalCamera.fCentralObstruction.fVal ||
        universalCamera.fNorchPosition.fVal != otherCam.universalCamera.fNorchPosition.fVal ||
        universalCamera.fNorchScale.fVal != otherCam.universalCamera.fNorchScale.fVal ||
        universalCamera.sCustomAperture.sLinkNodeName !=
            otherCam.universalCamera.sCustomAperture.sLinkNodeName ||
        universalCamera.fOpticalVignetteDistance.fVal !=
            otherCam.universalCamera.fOpticalVignetteDistance.fVal ||
        universalCamera.fOpticalVignetteScale.fVal !=
            otherCam.universalCamera.fOpticalVignetteScale.fVal ||
        universalCamera.bEnableSplitFocusDiopter.bVal !=
            otherCam.universalCamera.bEnableSplitFocusDiopter.bVal ||
        universalCamera.fDiopterFocalDepth.fVal !=
            otherCam.universalCamera.fDiopterFocalDepth.fVal ||
        universalCamera.fDiopterRotation.fVal != otherCam.universalCamera.fDiopterRotation.fVal ||
        universalCamera.f2DiopterTranslation.fVal !=
            otherCam.universalCamera.f2DiopterTranslation.fVal ||
        universalCamera.fDiopterBoundaryWidth.fVal !=
            otherCam.universalCamera.fDiopterBoundaryWidth.fVal ||
        universalCamera.fDiopterBoundaryFalloff.fVal !=
            otherCam.universalCamera.fDiopterBoundaryFalloff.fVal ||
        universalCamera.bShowDiopterGuide.bVal !=
            otherCam.universalCamera.bShowDiopterGuide.bVal ||
        universalCamera.f3Position.fVal != otherCam.universalCamera.f3Position.fVal ||
        universalCamera.f3Target.fVal != otherCam.universalCamera.f3Target.fVal ||
        universalCamera.f3Up.fVal != otherCam.universalCamera.f3Up.fVal ||
        universalCamera.bKeepUpright.bVal != otherCam.universalCamera.bKeepUpright.bVal ||
        universalCamera.oPositoin.oMotionPositions !=
            otherCam.universalCamera.oPositoin.oMotionPositions ||
        universalCamera.oPositoin.oMotionTargets !=
            otherCam.universalCamera.oPositoin.oMotionTargets ||
        universalCamera.oPositoin.oMotionUps != otherCam.universalCamera.oPositoin.oMotionUps ||
        universalCamera.oPositoin.oMotionFOVs != otherCam.universalCamera.oPositoin.oMotionFOVs);
  }
  inline bool operator==(const Camera &otherCam)
  {
    return (
        type == otherCam.type

        && bUseRegion == otherCam.bUseRegion && ui4Region == otherCam.ui4Region &&
        bUseBlenderCamera == otherCam.bUseBlenderCamera &&
        bUseUniversalCamera == otherCam.bUseUniversalCamera &&
        bUseCameraDimensionAsPreviewResolution ==
            otherCam.bUseCameraDimensionAsPreviewResolution &&
        ui2BlenderCameraDimension == otherCam.ui2BlenderCameraDimension &&
        f2BlenderCameraCenter == otherCam.f2BlenderCameraCenter &&
        f3EyePoint == otherCam.f3EyePoint && f3LookAt == otherCam.f3LookAt &&
        f3UpVector == otherCam.f3UpVector && fFOV == otherCam.fFOV && fFOVx == otherCam.fFOVx &&
        fFOVy == otherCam.fFOVy && oMotionParams == otherCam.oMotionParams &&
        bUseFstopValue == otherCam.bUseFstopValue && fAperture == otherCam.fAperture &&
        fApertureEdge == otherCam.fApertureEdge && fDistortion == otherCam.fDistortion &&
        bAutofocus == otherCam.bAutofocus && fFocalDepth == otherCam.fFocalDepth &&
        fNearClipDepth == otherCam.fNearClipDepth && fFarClipDepth == otherCam.fFarClipDepth &&
        f2LensShift == otherCam.f2LensShift && bPerspCorr == otherCam.bPerspCorr &&
        fStereoDist == otherCam.fStereoDist && fStereoDistFalloff == otherCam.fStereoDistFalloff &&
        fTolerance == otherCam.fTolerance && bOrtho == otherCam.bOrtho &&
        panCamMode == otherCam.panCamMode && stereoMode == otherCam.stereoMode &&
        stereoOutput == otherCam.stereoOutput && iBakingGroupId == otherCam.iBakingGroupId &&
        iPadding == otherCam.iPadding && iUvSet == otherCam.iUvSet &&
        bBakeOutwards == otherCam.bBakeOutwards &&
        bUseBakingPosition == otherCam.bUseBakingPosition && f2UVboxMin == otherCam.f2UVboxMin &&
        f2UVboxSize == otherCam.f2UVboxSize && bBackfaceCulling == otherCam.bBackfaceCulling &&
        f3LeftFilter == otherCam.f3LeftFilter && f3RightFilter == otherCam.f3RightFilter &&
        fPixelAspect == otherCam.fPixelAspect && fApertureAspect == otherCam.fApertureAspect &&
        fBlackoutLat == otherCam.fBlackoutLat && bKeepUpright == otherCam.bKeepUpright &&
        fBokehRotation == otherCam.fBokehRotation && fBokehRoundness == otherCam.fBokehRoundness &&
        iBokehSidecount == otherCam.iBokehSidecount &&
        f3UVWBakingTransformTranslation == otherCam.f3UVWBakingTransformTranslation &&
        f3UVWBakingTransformRotation == otherCam.f3UVWBakingTransformRotation &&
        f3UVWBakingTransformScale == otherCam.f3UVWBakingTransformScale &&
        iUVWBakingTransformRotationOrder == otherCam.iUVWBakingTransformRotationOrder &&
        sOSLCameraNodeMaterialName == otherCam.sOSLCameraNodeMaterialName &&
        sOSLCameraNodeName == otherCam.sOSLCameraNodeName &&
        bUseOSLCamera == otherCam.bUseOSLCamera

        && bEnableImager == otherCam.bEnableImager && f3WhiteBalance == otherCam.f3WhiteBalance &&
        iResponseCurve == otherCam.iResponseCurve &&
        iCameraImagerOrder == otherCam.iCameraImagerOrder && fExposure == otherCam.fExposure &&
        fGamma == otherCam.fGamma && fVignetting == otherCam.fVignetting &&
        fSaturation == otherCam.fSaturation && fHotPixelFilter == otherCam.fHotPixelFilter &&
        bPremultipliedAlpha == otherCam.bPremultipliedAlpha &&
        bACESToneMapping == otherCam.bACESToneMapping &&
        iMinDisplaySamples == otherCam.iMinDisplaySamples && bDithering == otherCam.bDithering &&
        fWhiteSaturation == otherCam.fWhiteSaturation &&
        fHighlightCompression == otherCam.fHighlightCompression &&
        iMaxTonemapInterval == otherCam.iMaxTonemapInterval &&
        bNeutralResponse == otherCam.bNeutralResponse &&
        bDisablePartialAlpha == otherCam.bDisablePartialAlpha && bSwapEyes == otherCam.bSwapEyes &&
        sCustomLut == otherCam.sCustomLut && fLutStrength == otherCam.fLutStrength &&
        sOcioLook == otherCam.sOcioLook && sOcioViewDisplay == otherCam.sOcioViewDisplay &&
        sOcioViewDisplayView == otherCam.sOcioViewDisplayView &&
        bForceToneMapping == otherCam.bForceToneMapping

        && bEnableDenoiser == otherCam.bEnableDenoiser &&
        bDenoiseVolumes == otherCam.bDenoiseVolumes &&
        bDenoiseOnCompletion == otherCam.bDenoiseOnCompletion &&
        iMinDenoiserSample == otherCam.iMinDenoiserSample &&
        iMaxDenoiserInterval == otherCam.iMaxDenoiserInterval &&
        fDenoiserBlend == otherCam.fDenoiserBlend

        && iSamplingMode == otherCam.iSamplingMode &&
        bEnableAIUpSampling == otherCam.bEnableAIUpSampling &&
        bUpSamplingOnCompletion == otherCam.bUpSamplingOnCompletion &&
        iMinUpSamplerSamples == otherCam.iMinUpSamplerSamples &&
        iMaxUpSamplerInterval == otherCam.iMaxUpSamplerInterval

        && bUsePostprocess == otherCam.bUsePostprocess && fBloomPower == otherCam.fBloomPower &&
        fCutoff == otherCam.fCutoff && fGlarePower == otherCam.fGlarePower &&
        iGlareRayCount == otherCam.iGlareRayCount && fGlareAngle == otherCam.fGlareAngle &&
        fGlareBlur == otherCam.fGlareBlur && fSpectralIntencity == otherCam.fSpectralIntencity &&
        fSpectralShift == otherCam.fSpectralShift && fSpreadStart == otherCam.fSpreadStart &&
        fSpreadEnd == otherCam.fSpreadEnd &&
        fChromaticAberrationIntensity == otherCam.fChromaticAberrationIntensity &&
        fLensFlare == otherCam.fLensFlare && fLensFlareExtent == otherCam.fLensFlareExtent &&
        bLightBeams == otherCam.bLightBeams &&
        bScaleWithFilm == otherCam.bScaleWithFilm &&
        fMediumDensityForPostfxLightBeams == otherCam.fMediumDensityForPostfxLightBeams &&
        bEnableFog == otherCam.bEnableFog && fFogExtinctionDistance == otherCam.fFogExtinctionDistance &&
        fFogBaseLevel == otherCam.fFogBaseLevel &&
        fFogHalfDensityHeight == otherCam.fFogHalfDensityHeight &&
        fFogEnvContribution == otherCam.fFogEnvContribution &&
        f3BaseFogColor == otherCam.f3BaseFogColor && fMediumRadius == otherCam.fMediumRadius &&
        universalCamera.iCameraMode.iVal == otherCam.universalCamera.iCameraMode.iVal &&
        universalCamera.fSensorWidth.fVal == otherCam.universalCamera.fSensorWidth.fVal &&
        universalCamera.fFocalLength.fVal == otherCam.universalCamera.fFocalLength.fVal &&
        universalCamera.fFstop.fVal == otherCam.universalCamera.fFstop.fVal &&
        universalCamera.bUseFstop.bVal == otherCam.universalCamera.bUseFstop.bVal &&
        universalCamera.fFieldOfView.fVal == otherCam.universalCamera.fFieldOfView.fVal &&
        universalCamera.fScaleOfView.fVal == otherCam.universalCamera.fScaleOfView.fVal &&
        universalCamera.f2LensShift.fVal == otherCam.universalCamera.f2LensShift.fVal &&
        universalCamera.fPixelAspectRatio.fVal ==
            otherCam.universalCamera.fPixelAspectRatio.fVal &&
        universalCamera.bPerspectiveCorrection.bVal ==
            otherCam.universalCamera.bPerspectiveCorrection.bVal &&
        universalCamera.fFisheyeAngle.fVal == otherCam.universalCamera.fFisheyeAngle.fVal &&
        universalCamera.iFisheyeType.iVal == otherCam.universalCamera.iFisheyeType.iVal &&
        universalCamera.bHardVignette.bVal == otherCam.universalCamera.bHardVignette.bVal &&
        universalCamera.iFisheyeProjection.iVal ==
            otherCam.universalCamera.iFisheyeProjection.iVal &&
        universalCamera.fHorizontalFiledOfView.fVal ==
            otherCam.universalCamera.fHorizontalFiledOfView.fVal &&
        universalCamera.fVerticalFiledOfView.fVal ==
            otherCam.universalCamera.fVerticalFiledOfView.fVal &&
        universalCamera.iCubemapLayout.iVal == otherCam.universalCamera.iCubemapLayout.iVal &&
        universalCamera.bEquiAngularCubemap.bVal ==
            otherCam.universalCamera.bEquiAngularCubemap.bVal &&
        universalCamera.bUseDistortionTexture.bVal ==
            otherCam.universalCamera.bUseDistortionTexture.bVal &&
        universalCamera.sDistortionTexture.sLinkNodeName ==
            otherCam.universalCamera.sDistortionTexture.sLinkNodeName &&
        universalCamera.fSphereDistortion.fVal ==
            otherCam.universalCamera.fSphereDistortion.fVal &&
        universalCamera.fBarrelDistortion.fVal ==
            otherCam.universalCamera.fBarrelDistortion.fVal &&
        universalCamera.fBarrelDistortionCorners.fVal ==
            otherCam.universalCamera.fBarrelDistortionCorners.fVal &&
        universalCamera.fSphereAberration.fVal ==
            otherCam.universalCamera.fSphereAberration.fVal &&
        universalCamera.fComa.fVal == otherCam.universalCamera.fComa.fVal &&
        universalCamera.fAstigmatism.fVal == otherCam.universalCamera.fAstigmatism.fVal &&
        universalCamera.fFieldCurvature.fVal == otherCam.universalCamera.fFieldCurvature.fVal &&
        universalCamera.fNearClipDepth.fVal == otherCam.universalCamera.fNearClipDepth.fVal &&
        universalCamera.fFarClipDepth.fVal == otherCam.universalCamera.fFarClipDepth.fVal &&
        universalCamera.bAutoFocus.bVal == otherCam.universalCamera.bAutoFocus.bVal &&
        universalCamera.fFocalDepth.fVal == otherCam.universalCamera.fFocalDepth.fVal &&
        universalCamera.fAperture.fVal == otherCam.universalCamera.fAperture.fVal &&
        universalCamera.fApertureAspectRatio.fVal ==
            otherCam.universalCamera.fApertureAspectRatio.fVal &&
        universalCamera.iApertureShape.iVal == otherCam.universalCamera.iApertureShape.iVal &&
        universalCamera.fApertureEdge.fVal == otherCam.universalCamera.fApertureEdge.fVal &&
        universalCamera.iApertureBladeCount.iVal ==
            otherCam.universalCamera.iApertureBladeCount.iVal &&
        universalCamera.fApertureRotation.fVal ==
            otherCam.universalCamera.fApertureRotation.fVal &&
        universalCamera.fApertureRoundedness.fVal ==
            otherCam.universalCamera.fApertureRoundedness.fVal &&
        universalCamera.fCentralObstruction.fVal ==
            otherCam.universalCamera.fCentralObstruction.fVal &&
        universalCamera.fNorchPosition.fVal == otherCam.universalCamera.fNorchPosition.fVal &&
        universalCamera.fNorchScale.fVal == otherCam.universalCamera.fNorchScale.fVal &&
        universalCamera.sCustomAperture.sLinkNodeName ==
            otherCam.universalCamera.sCustomAperture.sLinkNodeName &&
        universalCamera.fOpticalVignetteDistance.fVal ==
            otherCam.universalCamera.fOpticalVignetteDistance.fVal &&
        universalCamera.fOpticalVignetteScale.fVal ==
            otherCam.universalCamera.fOpticalVignetteScale.fVal &&
        universalCamera.bEnableSplitFocusDiopter.bVal ==
            otherCam.universalCamera.bEnableSplitFocusDiopter.bVal &&
        universalCamera.fDiopterFocalDepth.fVal ==
            otherCam.universalCamera.fDiopterFocalDepth.fVal &&
        universalCamera.fDiopterRotation.fVal == otherCam.universalCamera.fDiopterRotation.fVal &&
        universalCamera.f2DiopterTranslation.fVal ==
            otherCam.universalCamera.f2DiopterTranslation.fVal &&
        universalCamera.fDiopterBoundaryWidth.fVal ==
            otherCam.universalCamera.fDiopterBoundaryWidth.fVal &&
        universalCamera.fDiopterBoundaryFalloff.fVal ==
            otherCam.universalCamera.fDiopterBoundaryFalloff.fVal &&
        universalCamera.bShowDiopterGuide.bVal ==
            otherCam.universalCamera.bShowDiopterGuide.bVal &&
        universalCamera.f3Position.fVal == otherCam.universalCamera.f3Position.fVal &&
        universalCamera.f3Target.fVal == otherCam.universalCamera.f3Target.fVal &&
        universalCamera.f3Up.fVal == otherCam.universalCamera.f3Up.fVal &&
        universalCamera.bKeepUpright.bVal == otherCam.universalCamera.bKeepUpright.bVal &&
        universalCamera.oPositoin.oMotionPositions ==
            otherCam.universalCamera.oPositoin.oMotionPositions &&
        universalCamera.oPositoin.oMotionTargets ==
            otherCam.universalCamera.oPositoin.oMotionTargets &&
        universalCamera.oPositoin.oMotionUps == otherCam.universalCamera.oPositoin.oMotionUps &&
        universalCamera.oPositoin.oMotionFOVs == otherCam.universalCamera.oPositoin.oMotionFOVs);
  }
  inline Camera &operator=(const Camera &otherCam)
  {
    if (type != otherCam.type)
      type = otherCam.type;

    if (bUseRegion != otherCam.bUseRegion)
      bUseRegion = otherCam.bUseRegion;
    if (bUseBlenderCamera != otherCam.bUseBlenderCamera)
      bUseBlenderCamera = otherCam.bUseBlenderCamera;
    if (bUseUniversalCamera != otherCam.bUseUniversalCamera)
      bUseUniversalCamera = otherCam.bUseUniversalCamera;
    if (bUseCameraDimensionAsPreviewResolution != otherCam.bUseCameraDimensionAsPreviewResolution)
      bUseCameraDimensionAsPreviewResolution = otherCam.bUseCameraDimensionAsPreviewResolution;
    if (ui4Region != otherCam.ui4Region)
      ui4Region = otherCam.ui4Region;
    if (ui2BlenderCameraDimension != otherCam.ui2BlenderCameraDimension)
      ui2BlenderCameraDimension = otherCam.ui2BlenderCameraDimension;
    if (f2BlenderCameraCenter != otherCam.f2BlenderCameraCenter)
      f2BlenderCameraCenter = otherCam.f2BlenderCameraCenter;

    if (f3EyePoint != otherCam.f3EyePoint)
      f3EyePoint = otherCam.f3EyePoint;
    if (f3LookAt != otherCam.f3LookAt)
      f3LookAt = otherCam.f3LookAt;
    if (f3UpVector != otherCam.f3UpVector)
      f3UpVector = otherCam.f3UpVector;
    if (fFOV != otherCam.fFOV)
      fFOV = otherCam.fFOV;
    if (fFOVx != otherCam.fFOVx)
      fFOVx = otherCam.fFOVx;
    if (fFOVy != otherCam.fFOVy)
      fFOVy = otherCam.fFOVy;
    if (oMotionParams != otherCam.oMotionParams)
      oMotionParams = otherCam.oMotionParams;
    if (bUseFstopValue != otherCam.bUseFstopValue)
      bUseFstopValue = otherCam.bUseFstopValue;
    if (fAperture != otherCam.fAperture)
      fAperture = otherCam.fAperture;
    if (fApertureEdge != otherCam.fApertureEdge)
      fApertureEdge = otherCam.fApertureEdge;
    if (fDistortion != otherCam.fDistortion)
      fDistortion = otherCam.fDistortion;
    if (bAutofocus != otherCam.bAutofocus)
      bAutofocus = otherCam.bAutofocus;
    if (fFocalDepth != otherCam.fFocalDepth)
      fFocalDepth = otherCam.fFocalDepth;
    if (fNearClipDepth != otherCam.fNearClipDepth)
      fNearClipDepth = otherCam.fNearClipDepth;
    if (fFarClipDepth != otherCam.fFarClipDepth)
      fFarClipDepth = otherCam.fFarClipDepth;
    if (f2LensShift != otherCam.f2LensShift)
      f2LensShift = otherCam.f2LensShift;
    if (bPerspCorr != otherCam.bPerspCorr)
      bPerspCorr = otherCam.bPerspCorr;
    if (fStereoDist != otherCam.fStereoDist)
      fStereoDist = otherCam.fStereoDist;
    if (fStereoDistFalloff != otherCam.fStereoDistFalloff)
      fStereoDistFalloff = otherCam.fStereoDistFalloff;
    if (fTolerance != otherCam.fTolerance)
      fTolerance = otherCam.fTolerance;
    if (bOrtho != otherCam.bOrtho)
      bOrtho = otherCam.bOrtho;
    if (panCamMode != otherCam.panCamMode)
      panCamMode = otherCam.panCamMode;
    if (stereoMode != otherCam.stereoMode)
      stereoMode = otherCam.stereoMode;
    if (stereoOutput != otherCam.stereoOutput)
      stereoOutput = otherCam.stereoOutput;
    if (iBakingGroupId != otherCam.iBakingGroupId)
      iBakingGroupId = otherCam.iBakingGroupId;
    if (iPadding != otherCam.iPadding)
      iPadding = otherCam.iPadding;
    if (iUvSet != otherCam.iUvSet)
      iUvSet = otherCam.iUvSet;
    if (bBakeOutwards != otherCam.bBakeOutwards)
      bBakeOutwards = otherCam.bBakeOutwards;
    if (bUseBakingPosition != otherCam.bUseBakingPosition)
      bUseBakingPosition = otherCam.bUseBakingPosition;
    if (f2UVboxMin != otherCam.f2UVboxMin)
      f2UVboxMin = otherCam.f2UVboxMin;
    if (f2UVboxSize != otherCam.f2UVboxSize)
      f2UVboxSize = otherCam.f2UVboxSize;
    if (bBackfaceCulling != otherCam.bBackfaceCulling)
      bBackfaceCulling = otherCam.bBackfaceCulling;
    if (f3LeftFilter != otherCam.f3LeftFilter)
      f3LeftFilter = otherCam.f3LeftFilter;
    if (f3RightFilter != otherCam.f3RightFilter)
      f3RightFilter = otherCam.f3RightFilter;
    if (fPixelAspect != otherCam.fPixelAspect)
      fPixelAspect = otherCam.fPixelAspect;
    if (fApertureAspect != otherCam.fApertureAspect)
      fApertureAspect = otherCam.fApertureAspect;
    if (fBlackoutLat != otherCam.fBlackoutLat)
      fBlackoutLat = otherCam.fBlackoutLat;
    if (bKeepUpright != otherCam.bKeepUpright)
      bKeepUpright = otherCam.bKeepUpright;
    if (fBokehRotation != otherCam.fBokehRotation)
      fBokehRotation = otherCam.fBokehRotation;
    if (fBokehRoundness != otherCam.fBokehRoundness)
      fBokehRoundness = otherCam.fBokehRoundness;
    if (iBokehSidecount != otherCam.iBokehSidecount)
      iBokehSidecount = otherCam.iBokehSidecount;
    if (f3UVWBakingTransformTranslation != otherCam.f3UVWBakingTransformTranslation)
      f3UVWBakingTransformTranslation = otherCam.f3UVWBakingTransformTranslation;
    if (f3UVWBakingTransformRotation != otherCam.f3UVWBakingTransformRotation)
      f3UVWBakingTransformRotation = otherCam.f3UVWBakingTransformRotation;
    if (f3UVWBakingTransformScale != otherCam.f3UVWBakingTransformScale)
      f3UVWBakingTransformScale = otherCam.f3UVWBakingTransformScale;
    if (iUVWBakingTransformRotationOrder != otherCam.iUVWBakingTransformRotationOrder)
      iUVWBakingTransformRotationOrder = otherCam.iUVWBakingTransformRotationOrder;
    if (sOSLCameraNodeMaterialName != otherCam.sOSLCameraNodeMaterialName)
      sOSLCameraNodeMaterialName = otherCam.sOSLCameraNodeMaterialName;
    if (sOSLCameraNodeName != otherCam.sOSLCameraNodeName)
      sOSLCameraNodeName = otherCam.sOSLCameraNodeName;
    if (bUseOSLCamera != otherCam.bUseOSLCamera)
      bUseOSLCamera = otherCam.bUseOSLCamera;

    if (bEnableImager != otherCam.bEnableImager)
      bEnableImager = otherCam.bEnableImager;
    if (f3WhiteBalance != otherCam.f3WhiteBalance)
      f3WhiteBalance = otherCam.f3WhiteBalance;
    if (iResponseCurve != otherCam.iResponseCurve)
      iResponseCurve = otherCam.iResponseCurve;
    if (iCameraImagerOrder != otherCam.iCameraImagerOrder)
      iCameraImagerOrder = otherCam.iCameraImagerOrder;
    if (fExposure != otherCam.fExposure)
      fExposure = otherCam.fExposure;
    if (fGamma != otherCam.fGamma)
      fGamma = otherCam.fGamma;
    if (fVignetting != otherCam.fVignetting)
      fVignetting = otherCam.fVignetting;
    if (fSaturation != otherCam.fSaturation)
      fSaturation = otherCam.fSaturation;
    if (fHotPixelFilter != otherCam.fHotPixelFilter)
      fHotPixelFilter = otherCam.fHotPixelFilter;
    if (bPremultipliedAlpha != otherCam.bPremultipliedAlpha)
      bPremultipliedAlpha = otherCam.bPremultipliedAlpha;
    if (bACESToneMapping != otherCam.bACESToneMapping)
      bACESToneMapping = otherCam.bACESToneMapping;
    if (iMinDisplaySamples != otherCam.iMinDisplaySamples)
      iMinDisplaySamples = otherCam.iMinDisplaySamples;
    if (bDithering != otherCam.bDithering)
      bDithering = otherCam.bDithering;
    if (fWhiteSaturation != otherCam.fWhiteSaturation)
      fWhiteSaturation = otherCam.fWhiteSaturation;
    if (fHighlightCompression != otherCam.fHighlightCompression)
      fHighlightCompression = otherCam.fHighlightCompression;
    if (iMaxTonemapInterval != otherCam.iMaxTonemapInterval)
      iMaxTonemapInterval = otherCam.iMaxTonemapInterval;
    if (bNeutralResponse != otherCam.bNeutralResponse)
      bNeutralResponse = otherCam.bNeutralResponse;
    if (bDisablePartialAlpha != otherCam.bDisablePartialAlpha)
      bDisablePartialAlpha = otherCam.bDisablePartialAlpha;
    if (bSwapEyes != otherCam.bSwapEyes)
      bSwapEyes = otherCam.bSwapEyes;
    if (sCustomLut != otherCam.sCustomLut)
      sCustomLut = otherCam.sCustomLut;
    if (fLutStrength != otherCam.fLutStrength)
      fLutStrength = otherCam.fLutStrength;

    if (sOcioLook != otherCam.sOcioLook)
      sOcioLook = otherCam.sOcioLook;
    if (sOcioViewDisplay != otherCam.sOcioViewDisplay)
      sOcioViewDisplay = otherCam.sOcioViewDisplay;
    if (sOcioViewDisplayView != otherCam.sOcioViewDisplayView)
      sOcioViewDisplayView = otherCam.sOcioViewDisplayView;
    if (bForceToneMapping != otherCam.bForceToneMapping)
      bForceToneMapping = otherCam.bForceToneMapping;

    if (bEnableDenoiser != otherCam.bEnableDenoiser)
      bEnableDenoiser = otherCam.bEnableDenoiser;
    if (bDenoiseVolumes != otherCam.bDenoiseVolumes)
      bDenoiseVolumes = otherCam.bDenoiseVolumes;
    if (bDenoiseOnCompletion != otherCam.bDenoiseOnCompletion)
      bDenoiseOnCompletion = otherCam.bDenoiseOnCompletion;
    if (iMinDenoiserSample != otherCam.iMinDenoiserSample)
      iMinDenoiserSample = otherCam.iMinDenoiserSample;
    if (iMaxDenoiserInterval != otherCam.iMaxDenoiserInterval)
      iMaxDenoiserInterval = otherCam.iMaxDenoiserInterval;
    if (fDenoiserBlend != otherCam.fDenoiserBlend)
      fDenoiserBlend = otherCam.fDenoiserBlend;

    if (iSamplingMode != otherCam.iSamplingMode)
      iSamplingMode = otherCam.iSamplingMode;
    if (bEnableAIUpSampling != otherCam.bEnableAIUpSampling)
      bEnableAIUpSampling = otherCam.bEnableAIUpSampling;
    if (bUpSamplingOnCompletion != otherCam.bUpSamplingOnCompletion)
      bUpSamplingOnCompletion = otherCam.bUpSamplingOnCompletion;
    if (iMinUpSamplerSamples != otherCam.iMinUpSamplerSamples)
      iMinUpSamplerSamples = otherCam.iMinUpSamplerSamples;
    if (iMaxUpSamplerInterval != otherCam.iMaxUpSamplerInterval)
      iMaxUpSamplerInterval = otherCam.iMaxUpSamplerInterval;

    if (bUsePostprocess != otherCam.bUsePostprocess)
      bUsePostprocess = otherCam.bUsePostprocess;
    if (fBloomPower != otherCam.fBloomPower)
      fBloomPower = otherCam.fBloomPower;
    if (fCutoff != otherCam.fCutoff)
      fCutoff = otherCam.fCutoff;
    if (fGlarePower != otherCam.fGlarePower)
      fGlarePower = otherCam.fGlarePower;
    if (iGlareRayCount != otherCam.iGlareRayCount)
      iGlareRayCount = otherCam.iGlareRayCount;
    if (fGlareAngle != otherCam.fGlareAngle)
      fGlareAngle = otherCam.fGlareAngle;
    if (fGlareBlur != otherCam.fGlareBlur)
      fGlareBlur = otherCam.fGlareBlur;
    if (fSpectralIntencity != otherCam.fSpectralIntencity)
      fSpectralIntencity = otherCam.fSpectralIntencity;
    if (fSpectralShift != otherCam.fSpectralShift)
      fSpectralShift = otherCam.fSpectralShift;
    if (fSpreadStart != otherCam.fSpreadStart)
      fSpreadStart = otherCam.fSpreadStart;
    if (fSpreadEnd != otherCam.fSpreadEnd)
      fSpreadEnd = otherCam.fSpreadEnd;
    if (fChromaticAberrationIntensity != otherCam.fChromaticAberrationIntensity)
      fChromaticAberrationIntensity = otherCam.fChromaticAberrationIntensity;
    if (fLensFlare != otherCam.fLensFlare)
      fLensFlare = otherCam.fLensFlare;
    if (fLensFlareExtent != otherCam.fLensFlareExtent)
      fLensFlareExtent = otherCam.fLensFlareExtent;
    if (bLightBeams != otherCam.bLightBeams)
      bLightBeams = otherCam.bLightBeams;
    if (bScaleWithFilm != otherCam.bScaleWithFilm)
      bScaleWithFilm = otherCam.bScaleWithFilm;
    if (fMediumDensityForPostfxLightBeams != otherCam.fMediumDensityForPostfxLightBeams)
      fMediumDensityForPostfxLightBeams = otherCam.fMediumDensityForPostfxLightBeams;
    if (bEnableFog != otherCam.bEnableFog)
      bEnableFog = otherCam.bEnableFog;
    if (fFogExtinctionDistance != otherCam.fFogExtinctionDistance)
      fFogExtinctionDistance = otherCam.fFogExtinctionDistance;
    if (fFogBaseLevel != otherCam.fFogBaseLevel)
      fFogBaseLevel = otherCam.fFogBaseLevel;
    if (fFogHalfDensityHeight != otherCam.fFogHalfDensityHeight)
      fFogHalfDensityHeight = otherCam.fFogHalfDensityHeight;
    if (fFogEnvContribution != otherCam.fFogEnvContribution)
      fFogEnvContribution = otherCam.fFogEnvContribution;
    if (f3BaseFogColor != otherCam.f3BaseFogColor)
      f3BaseFogColor = otherCam.f3BaseFogColor;
    if (fMediumRadius != otherCam.fMediumRadius)
      fMediumRadius = otherCam.fMediumRadius;

    universalCamera.iCameraMode.iVal = otherCam.universalCamera.iCameraMode.iVal;
    universalCamera.fSensorWidth.fVal = otherCam.universalCamera.fSensorWidth.fVal;
    universalCamera.fFocalLength.fVal = otherCam.universalCamera.fFocalLength.fVal;
    universalCamera.fFstop.fVal = otherCam.universalCamera.fFstop.fVal;
    universalCamera.bUseFstop.bVal = otherCam.universalCamera.bUseFstop.bVal;
    universalCamera.fFieldOfView.fVal = otherCam.universalCamera.fFieldOfView.fVal;
    universalCamera.fScaleOfView.fVal = otherCam.universalCamera.fScaleOfView.fVal;
    universalCamera.f2LensShift.fVal = otherCam.universalCamera.f2LensShift.fVal;
    universalCamera.fPixelAspectRatio.fVal = otherCam.universalCamera.fPixelAspectRatio.fVal;
    universalCamera.bPerspectiveCorrection.bVal =
        otherCam.universalCamera.bPerspectiveCorrection.bVal;
    universalCamera.fFisheyeAngle.fVal = otherCam.universalCamera.fFisheyeAngle.fVal;
    universalCamera.iFisheyeType.iVal = otherCam.universalCamera.iFisheyeType.iVal;
    universalCamera.bHardVignette.bVal = otherCam.universalCamera.bHardVignette.bVal;
    universalCamera.iFisheyeProjection.iVal = otherCam.universalCamera.iFisheyeProjection.iVal;
    universalCamera.fHorizontalFiledOfView.fVal =
        otherCam.universalCamera.fHorizontalFiledOfView.fVal;
    universalCamera.fVerticalFiledOfView.fVal = otherCam.universalCamera.fVerticalFiledOfView.fVal;
    universalCamera.iCubemapLayout.iVal = otherCam.universalCamera.iCubemapLayout.iVal;
    universalCamera.bEquiAngularCubemap.bVal = otherCam.universalCamera.bEquiAngularCubemap.bVal;
    universalCamera.bUseDistortionTexture.bVal =
        otherCam.universalCamera.bUseDistortionTexture.bVal;
    universalCamera.sDistortionTexture.sLinkNodeName =
        otherCam.universalCamera.sDistortionTexture.sLinkNodeName;
    universalCamera.fSphereDistortion.fVal = otherCam.universalCamera.fSphereDistortion.fVal;
    universalCamera.fBarrelDistortion.fVal = otherCam.universalCamera.fBarrelDistortion.fVal;
    universalCamera.fBarrelDistortionCorners.fVal =
        otherCam.universalCamera.fBarrelDistortionCorners.fVal;
    universalCamera.fSphereAberration.fVal = otherCam.universalCamera.fSphereAberration.fVal;
    universalCamera.fComa.fVal = otherCam.universalCamera.fComa.fVal;
    universalCamera.fAstigmatism.fVal = otherCam.universalCamera.fAstigmatism.fVal;
    universalCamera.fFieldCurvature.fVal = otherCam.universalCamera.fFieldCurvature.fVal;
    universalCamera.fNearClipDepth.fVal = otherCam.universalCamera.fNearClipDepth.fVal;
    universalCamera.fFarClipDepth.fVal = otherCam.universalCamera.fFarClipDepth.fVal;
    universalCamera.bAutoFocus.bVal = otherCam.universalCamera.bAutoFocus.bVal;
    universalCamera.fFocalDepth.fVal = otherCam.universalCamera.fFocalDepth.fVal;
    universalCamera.fAperture.fVal = otherCam.universalCamera.fAperture.fVal;
    universalCamera.fApertureAspectRatio.fVal = otherCam.universalCamera.fApertureAspectRatio.fVal;
    universalCamera.iApertureShape.iVal = otherCam.universalCamera.iApertureShape.iVal;
    universalCamera.fApertureEdge.fVal = otherCam.universalCamera.fApertureEdge.fVal;
    universalCamera.iApertureBladeCount.iVal = otherCam.universalCamera.iApertureBladeCount.iVal;
    universalCamera.fApertureRotation.fVal = otherCam.universalCamera.fApertureRotation.fVal;
    universalCamera.fApertureRoundedness.fVal = otherCam.universalCamera.fApertureRoundedness.fVal;
    universalCamera.fCentralObstruction.fVal = otherCam.universalCamera.fCentralObstruction.fVal;
    universalCamera.fNorchPosition.fVal = otherCam.universalCamera.fNorchPosition.fVal;
    universalCamera.fNorchScale.fVal = otherCam.universalCamera.fNorchScale.fVal;
    universalCamera.sCustomAperture.sLinkNodeName =
        otherCam.universalCamera.sCustomAperture.sLinkNodeName;
    universalCamera.fOpticalVignetteDistance.fVal =
        otherCam.universalCamera.fOpticalVignetteDistance.fVal;
    universalCamera.fOpticalVignetteScale.fVal =
        otherCam.universalCamera.fOpticalVignetteScale.fVal;
    universalCamera.bEnableSplitFocusDiopter.bVal =
        otherCam.universalCamera.bEnableSplitFocusDiopter.bVal;
    universalCamera.fDiopterFocalDepth.fVal = otherCam.universalCamera.fDiopterFocalDepth.fVal;
    universalCamera.fDiopterRotation.fVal = otherCam.universalCamera.fDiopterRotation.fVal;
    universalCamera.f2DiopterTranslation.fVal = otherCam.universalCamera.f2DiopterTranslation.fVal;
    universalCamera.fDiopterBoundaryWidth.fVal =
        otherCam.universalCamera.fDiopterBoundaryWidth.fVal;
    universalCamera.fDiopterBoundaryFalloff.fVal =
        otherCam.universalCamera.fDiopterBoundaryFalloff.fVal;
    universalCamera.bShowDiopterGuide.bVal = otherCam.universalCamera.bShowDiopterGuide.bVal;
    universalCamera.f3Position.fVal = otherCam.universalCamera.f3Position.fVal;
    universalCamera.f3Target.fVal = otherCam.universalCamera.f3Target.fVal;
    universalCamera.f3Up.fVal = otherCam.universalCamera.f3Up.fVal;
    universalCamera.bKeepUpright.bVal = otherCam.universalCamera.bKeepUpright.bVal;
    universalCamera.oPositoin.oMotionPositions =
        otherCam.universalCamera.oPositoin.oMotionPositions;
    universalCamera.oPositoin.oMotionTargets = otherCam.universalCamera.oPositoin.oMotionTargets;
    universalCamera.oPositoin.oMotionUps = otherCam.universalCamera.oPositoin.oMotionUps;
    universalCamera.oPositoin.oMotionFOVs = otherCam.universalCamera.oPositoin.oMotionFOVs;

    return *this;
  }
};  // struct Camera

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Passes
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// The structure holding a passes data that is going to be uploaded to the Octane server.
struct Passes {
  bool bUsePasses;
  RenderPassId curPassType;

  bool bBeautyPass;

  bool bEmittersPass;
  bool bEnvironmentPass;
  bool bDiffusePass;
  bool bDiffuseDirectPass;
  bool bDiffuseIndirectPass;
  bool bDiffuseFilterPass;
  bool bReflectionPass;
  bool bReflectionDirectPass;
  bool bReflectionIndirectPass;
  bool bReflectionFilterPass;
  bool bRefractionPass;
  bool bRefractionFilterPass;
  bool bTransmissionPass;
  bool bTransmissionFilterPass;
  bool bSubsurfScatteringPass;
  bool bPostProcessingPass;
  bool bNoisePass;
  bool bShadowPass;
  bool bIrradiancePass;
  bool bLightDirPass;

  bool bVolumePass;
  bool bVolumeMaskPass;
  bool bVolumeEmissionPass;
  bool bVolumeZFrontPass;
  bool bVolmueZBackPass;

  bool bDenoiserBeauty;
  bool bDenoiserDiffDir;
  bool bDenoiserDiffIndir;
  bool bDenoiserReflectDir;
  bool bDenoiserReflectIndir;
  bool bDenoiserRefraction;
  bool bDenoiserRemainder;
  bool bDenoiserEmission;
  bool bDenoiserVolume;
  bool bDenoiserVolumeEmission;

  bool bLayerShadowsPass;
  bool bLayerBlackShadowsPass;
  bool bLayerReflectionsPass;

  bool bAmbientLightPass;
  bool bSunlightPass;
  bool bLight1Pass;
  bool bLight2Pass;
  bool bLight3Pass;
  bool bLight4Pass;
  bool bLight5Pass;
  bool bLight6Pass;
  bool bLight7Pass;
  bool bLight8Pass;

  bool bAmbientLightDirectPass;
  bool bSunLightDirectPass;
  bool bLightDirect1Pass;
  bool bLightDirect2Pass;
  bool bLightDirect3Pass;
  bool bLightDirect4Pass;
  bool bLightDirect5Pass;
  bool bLightDirect6Pass;
  bool bLightDirect7Pass;
  bool bLightDirect8Pass;

  bool bAmbientLightIndirectPass;
  bool bSunLightIndirectPass;
  bool bLightIndirect1Pass;
  bool bLightIndirect2Pass;
  bool bLightIndirect3Pass;
  bool bLightIndirect4Pass;
  bool bLightIndirect5Pass;
  bool bLightIndirect6Pass;
  bool bLightIndirect7Pass;
  bool bLightIndirect8Pass;

  bool bBackinGroupIdPass;
  bool bOpacityPass;
  bool bRoughnessPass;
  bool bIorPass;
  bool bDiffuseFilterInfoPass;
  bool bReflectionFilterInfoPass;
  bool bRefractionFilterInfoPass;
  bool bTransmissionFilterInfoPass;

  bool bGeomNormalsPass;
  bool bShadingNormalsPass;
  bool bSmoothNormalsPass;
  bool bTangentNormalsPass;
  bool bPositionPass;
  bool bZdepthPass;
  bool bMaterialIdPass;
  bool bUVCoordinatesPass;
  bool bTangentsPass;
  bool bWireframePass;
  bool bMotionVectorPass;
  bool bObjectIdPass;
  bool bLayerIdPass;
  bool bLayerMaskPass;
  bool bLightPassIdPass;
  bool bObjectLayerColorPass;

  bool bAOPass;

  int32_t iInfoPassMaxSamples;
  bool iSamplingMode;
  bool bPassesRaw;
  bool bPostProcEnvironment;
  bool bBump;
  bool bAoAlphaShadows;
  float fZdepthMax;
  float fUVMax;
  int32_t iUVCoordinateSelection;
  float fMaxSpeed;
  float fAODistance;
  float fOpacityThreshold;

  int32_t iCryptomatteChannel;
  int32_t iCryptomatteSeedFactor;
  bool bCryptomatteInstance;
  bool bCryptomatteMaterialNodeName;
  bool bCryptomatteMaterialPinName;
  bool bCryptomatteMaterialNode;
  bool bCryptomatteObjectNodeName;
  bool bCryptomatteObjectPinName;
  bool bCryptomatteObjectNode;

  inline Passes() : bUsePasses(false), curPassType((RenderPassId)-1)
  {
    bDenoiserBeauty = false;
    bDenoiserDiffDir = false;
    bDenoiserDiffIndir = false;
    bDenoiserReflectDir = false;
    bDenoiserReflectIndir = false;
    bDenoiserRefraction = false;
    bDenoiserRemainder = false;
    bDenoiserEmission = false;
    bDenoiserVolume = false;
    bDenoiserVolumeEmission = false;
    bCryptomatteInstance = false;
    bCryptomatteMaterialNodeName = false;
    bCryptomatteMaterialPinName = false;
    bCryptomatteMaterialNode = false;
    bCryptomatteObjectNodeName = false;
    bCryptomatteObjectPinName = false;
    bCryptomatteObjectNode = false;
  }
  inline bool operator==(const Passes &otherPasses)
  {
    return (curPassType == otherPasses.curPassType && bUsePasses == otherPasses.bUsePasses

            && bBeautyPass == otherPasses.bBeautyPass

            && bEmittersPass == otherPasses.bEmittersPass &&
            bEnvironmentPass == otherPasses.bEnvironmentPass &&
            bDiffusePass == otherPasses.bDiffusePass &&
            bDiffuseDirectPass == otherPasses.bDiffuseDirectPass &&
            bDiffuseIndirectPass == otherPasses.bDiffuseIndirectPass &&
            bDiffuseFilterPass == otherPasses.bDiffuseFilterPass &&
            bReflectionPass == otherPasses.bReflectionPass &&
            bReflectionDirectPass == otherPasses.bReflectionDirectPass &&
            bReflectionIndirectPass == otherPasses.bReflectionIndirectPass &&
            bReflectionFilterPass == otherPasses.bReflectionFilterPass &&
            bRefractionPass == otherPasses.bRefractionPass &&
            bRefractionFilterPass == otherPasses.bRefractionFilterPass &&
            bTransmissionPass == otherPasses.bTransmissionPass &&
            bTransmissionFilterPass == otherPasses.bTransmissionFilterPass &&
            bSubsurfScatteringPass == otherPasses.bSubsurfScatteringPass &&
            bPostProcessingPass == otherPasses.bPostProcessingPass &&
            bNoisePass == otherPasses.bNoisePass && bShadowPass == otherPasses.bShadowPass &&
            bIrradiancePass == otherPasses.bIrradiancePass &&
            bLightDirPass == otherPasses.bLightDirPass

            && bVolumePass == otherPasses.bVolumePass &&
            bVolumeMaskPass == otherPasses.bVolumeMaskPass &&
            bVolumeEmissionPass == otherPasses.bVolumeEmissionPass &&
            bVolumeZFrontPass == otherPasses.bVolumeZFrontPass &&
            bVolmueZBackPass == otherPasses.bVolmueZBackPass

            && bDenoiserBeauty == otherPasses.bDenoiserBeauty &&
            bDenoiserDiffDir == otherPasses.bDenoiserDiffDir &&
            bDenoiserDiffIndir == otherPasses.bDenoiserDiffIndir &&
            bDenoiserReflectDir == otherPasses.bDenoiserReflectDir &&
            bDenoiserReflectIndir == otherPasses.bDenoiserReflectIndir &&
            bDenoiserRefraction == otherPasses.bDenoiserRefraction &&
            bDenoiserRemainder == otherPasses.bDenoiserRemainder &&
            bDenoiserEmission == otherPasses.bDenoiserEmission &&
            bDenoiserVolume == otherPasses.bDenoiserVolume &&
            bDenoiserVolumeEmission == otherPasses.bDenoiserVolumeEmission

            && bLayerShadowsPass == otherPasses.bLayerShadowsPass &&
            bLayerBlackShadowsPass == otherPasses.bLayerBlackShadowsPass &&
            bLayerReflectionsPass == otherPasses.bLayerReflectionsPass

            && bAmbientLightPass == otherPasses.bAmbientLightPass &&
            bSunlightPass == otherPasses.bSunlightPass && bLight1Pass == otherPasses.bLight1Pass &&
            bLight2Pass == otherPasses.bLight2Pass && bLight3Pass == otherPasses.bLight3Pass &&
            bLight4Pass == otherPasses.bLight4Pass && bLight5Pass == otherPasses.bLight5Pass &&
            bLight6Pass == otherPasses.bLight6Pass && bLight7Pass == otherPasses.bLight7Pass &&
            bLight8Pass == otherPasses.bLight8Pass

            && bAmbientLightDirectPass == otherPasses.bAmbientLightDirectPass &&
            bSunLightDirectPass == otherPasses.bSunLightDirectPass &&
            bLightDirect1Pass == otherPasses.bLightDirect1Pass &&
            bLightDirect2Pass == otherPasses.bLightDirect2Pass &&
            bLightDirect3Pass == otherPasses.bLightDirect3Pass &&
            bLightDirect4Pass == otherPasses.bLightDirect4Pass &&
            bLightDirect5Pass == otherPasses.bLightDirect5Pass &&
            bLightDirect6Pass == otherPasses.bLightDirect6Pass &&
            bLightDirect7Pass == otherPasses.bLightDirect7Pass &&
            bLightDirect8Pass == otherPasses.bLightDirect8Pass

            && bAmbientLightIndirectPass == otherPasses.bAmbientLightIndirectPass &&
            bSunLightIndirectPass == otherPasses.bSunLightIndirectPass &&
            bLightIndirect1Pass == otherPasses.bLightIndirect1Pass &&
            bLightIndirect2Pass == otherPasses.bLightIndirect2Pass &&
            bLightIndirect3Pass == otherPasses.bLightIndirect3Pass &&
            bLightIndirect4Pass == otherPasses.bLightIndirect4Pass &&
            bLightIndirect5Pass == otherPasses.bLightIndirect5Pass &&
            bLightIndirect6Pass == otherPasses.bLightIndirect6Pass &&
            bLightIndirect7Pass == otherPasses.bLightIndirect7Pass &&
            bLightIndirect8Pass == otherPasses.bLightIndirect8Pass

            && bBackinGroupIdPass == otherPasses.bBackinGroupIdPass &&
            bOpacityPass == otherPasses.bOpacityPass &&
            bRoughnessPass == otherPasses.bRoughnessPass && bIorPass == otherPasses.bIorPass &&
            bDiffuseFilterInfoPass == otherPasses.bDiffuseFilterInfoPass &&
            bReflectionFilterInfoPass == otherPasses.bReflectionFilterInfoPass &&
            bRefractionFilterInfoPass == otherPasses.bRefractionFilterInfoPass &&
            bTransmissionFilterInfoPass == otherPasses.bTransmissionFilterInfoPass

            && bGeomNormalsPass == otherPasses.bGeomNormalsPass &&
            bShadingNormalsPass == otherPasses.bShadingNormalsPass &&
            bSmoothNormalsPass == otherPasses.bSmoothNormalsPass &&
            bTangentNormalsPass == otherPasses.bTangentNormalsPass &&
            bPositionPass == otherPasses.bPositionPass && bZdepthPass == otherPasses.bZdepthPass &&
            bMaterialIdPass == otherPasses.bMaterialIdPass &&
            bUVCoordinatesPass == otherPasses.bUVCoordinatesPass &&
            bTangentsPass == otherPasses.bTangentsPass &&
            bWireframePass == otherPasses.bWireframePass &&
            bMotionVectorPass == otherPasses.bMotionVectorPass &&
            bObjectIdPass == otherPasses.bObjectIdPass &&
            bLayerIdPass == otherPasses.bLayerIdPass &&
            bLayerMaskPass == otherPasses.bLayerMaskPass &&
            bLightPassIdPass == otherPasses.bLightPassIdPass &&
            bObjectLayerColorPass == otherPasses.bObjectLayerColorPass

            && bAOPass == otherPasses.bAOPass

            && iInfoPassMaxSamples == otherPasses.iInfoPassMaxSamples &&
            iSamplingMode == otherPasses.iSamplingMode && bPassesRaw == otherPasses.bPassesRaw &&
            bPostProcEnvironment == otherPasses.bPostProcEnvironment &&
            bBump == otherPasses.bBump && bAoAlphaShadows == otherPasses.bAoAlphaShadows &&
            fZdepthMax == otherPasses.fZdepthMax && fUVMax == otherPasses.fUVMax &&
            iUVCoordinateSelection == otherPasses.iUVCoordinateSelection &&
            fMaxSpeed == otherPasses.fMaxSpeed && fAODistance == otherPasses.fAODistance &&
            fOpacityThreshold == otherPasses.fOpacityThreshold &&
            iCryptomatteChannel == otherPasses.iCryptomatteChannel &&
            iCryptomatteSeedFactor == otherPasses.iCryptomatteSeedFactor)

           && bCryptomatteInstance == otherPasses.bCryptomatteInstance &&
           bCryptomatteMaterialNodeName == otherPasses.bCryptomatteMaterialNodeName &&
           bCryptomatteMaterialPinName == otherPasses.bCryptomatteMaterialPinName &&
           bCryptomatteMaterialNode == otherPasses.bCryptomatteMaterialNode &&
           bCryptomatteObjectNodeName == otherPasses.bCryptomatteObjectNodeName &&
           bCryptomatteObjectPinName == otherPasses.bCryptomatteObjectPinName &&
           bCryptomatteObjectNode == otherPasses.bCryptomatteObjectNode;
  }
  inline Passes &operator=(const Passes &otherPasses)
  {
    if (curPassType != otherPasses.curPassType)
      curPassType = otherPasses.curPassType;
    if (bUsePasses != otherPasses.bUsePasses)
      bUsePasses = otherPasses.bUsePasses;

    if (bBeautyPass != otherPasses.bBeautyPass)
      bBeautyPass = otherPasses.bBeautyPass;

    if (bEmittersPass != otherPasses.bEmittersPass)
      bEmittersPass = otherPasses.bEmittersPass;
    if (bEnvironmentPass != otherPasses.bEnvironmentPass)
      bEnvironmentPass = otherPasses.bEnvironmentPass;
    if (bDiffusePass != otherPasses.bDiffusePass)
      bDiffusePass = otherPasses.bDiffusePass;
    if (bDiffuseDirectPass != otherPasses.bDiffuseDirectPass)
      bDiffuseDirectPass = otherPasses.bDiffuseDirectPass;
    if (bDiffuseIndirectPass != otherPasses.bDiffuseIndirectPass)
      bDiffuseIndirectPass = otherPasses.bDiffuseIndirectPass;
    if (bDiffuseFilterPass != otherPasses.bDiffuseFilterPass)
      bDiffuseFilterPass = otherPasses.bDiffuseFilterPass;
    if (bReflectionPass != otherPasses.bReflectionPass)
      bReflectionPass = otherPasses.bReflectionPass;
    if (bReflectionDirectPass != otherPasses.bReflectionDirectPass)
      bReflectionDirectPass = otherPasses.bReflectionDirectPass;
    if (bReflectionIndirectPass != otherPasses.bReflectionIndirectPass)
      bReflectionIndirectPass = otherPasses.bReflectionIndirectPass;
    if (bReflectionFilterPass != otherPasses.bReflectionFilterPass)
      bReflectionFilterPass = otherPasses.bReflectionFilterPass;
    if (bRefractionPass != otherPasses.bRefractionPass)
      bRefractionPass = otherPasses.bRefractionPass;
    if (bRefractionFilterPass != otherPasses.bRefractionFilterPass)
      bRefractionFilterPass = otherPasses.bRefractionFilterPass;
    if (bTransmissionPass != otherPasses.bTransmissionPass)
      bTransmissionPass = otherPasses.bTransmissionPass;
    if (bTransmissionFilterPass != otherPasses.bTransmissionFilterPass)
      bTransmissionFilterPass = otherPasses.bTransmissionFilterPass;
    if (bSubsurfScatteringPass != otherPasses.bSubsurfScatteringPass)
      bSubsurfScatteringPass = otherPasses.bSubsurfScatteringPass;
    if (bPostProcessingPass != otherPasses.bPostProcessingPass)
      bPostProcessingPass = otherPasses.bPostProcessingPass;
    if (bNoisePass != otherPasses.bNoisePass)
      bNoisePass = otherPasses.bNoisePass;
    if (bShadowPass != otherPasses.bShadowPass)
      bShadowPass = otherPasses.bShadowPass;
    if (bIrradiancePass != otherPasses.bIrradiancePass)
      bIrradiancePass = otherPasses.bIrradiancePass;
    if (bLightDirPass != otherPasses.bLightDirPass)
      bLightDirPass = otherPasses.bLightDirPass;

    if (bVolumePass != otherPasses.bVolumePass)
      bVolumePass = otherPasses.bVolumePass;
    if (bVolumeMaskPass != otherPasses.bVolumeMaskPass)
      bVolumeMaskPass = otherPasses.bVolumeMaskPass;
    if (bVolumeEmissionPass != otherPasses.bVolumeEmissionPass)
      bVolumeEmissionPass = otherPasses.bVolumeEmissionPass;
    if (bVolumeZFrontPass != otherPasses.bVolumeZFrontPass)
      bVolumeZFrontPass = otherPasses.bVolumeZFrontPass;
    if (bVolmueZBackPass != otherPasses.bVolmueZBackPass)
      bVolmueZBackPass = otherPasses.bVolmueZBackPass;

    if (bDenoiserBeauty != otherPasses.bDenoiserBeauty)
      bDenoiserBeauty = otherPasses.bDenoiserBeauty;
    if (bDenoiserDiffDir != otherPasses.bDenoiserDiffDir)
      bDenoiserDiffDir = otherPasses.bDenoiserDiffDir;
    if (bDenoiserDiffIndir != otherPasses.bDenoiserDiffIndir)
      bDenoiserDiffIndir = otherPasses.bDenoiserDiffIndir;
    if (bDenoiserReflectDir != otherPasses.bDenoiserReflectDir)
      bDenoiserReflectDir = otherPasses.bDenoiserReflectDir;
    if (bDenoiserReflectIndir != otherPasses.bDenoiserReflectIndir)
      bDenoiserReflectIndir = otherPasses.bDenoiserReflectIndir;
    if (bDenoiserRefraction != otherPasses.bDenoiserRefraction)
      bDenoiserRefraction = otherPasses.bDenoiserRefraction;
    if (bDenoiserRemainder != otherPasses.bDenoiserRemainder)
      bDenoiserRemainder = otherPasses.bDenoiserRemainder;
    if (bDenoiserEmission != otherPasses.bDenoiserEmission)
      bDenoiserEmission = otherPasses.bDenoiserEmission;
    if (bDenoiserVolume != otherPasses.bDenoiserVolume)
      bDenoiserVolume = otherPasses.bDenoiserVolume;
    if (bDenoiserVolumeEmission != otherPasses.bDenoiserVolumeEmission)
      bDenoiserVolumeEmission = otherPasses.bDenoiserVolumeEmission;

    if (bLayerShadowsPass != otherPasses.bLayerShadowsPass)
      bLayerShadowsPass = otherPasses.bLayerShadowsPass;
    if (bLayerBlackShadowsPass != otherPasses.bLayerBlackShadowsPass)
      bLayerBlackShadowsPass = otherPasses.bLayerBlackShadowsPass;
    if (bLayerReflectionsPass != otherPasses.bLayerReflectionsPass)
      bLayerReflectionsPass = otherPasses.bLayerReflectionsPass;

    if (bAmbientLightPass != otherPasses.bAmbientLightPass)
      bAmbientLightPass = otherPasses.bAmbientLightPass;
    if (bSunlightPass != otherPasses.bSunlightPass)
      bSunlightPass = otherPasses.bSunlightPass;
    if (bLight1Pass != otherPasses.bLight1Pass)
      bLight1Pass = otherPasses.bLight1Pass;
    if (bLight2Pass != otherPasses.bLight2Pass)
      bLight2Pass = otherPasses.bLight2Pass;
    if (bLight3Pass != otherPasses.bLight3Pass)
      bLight3Pass = otherPasses.bLight3Pass;
    if (bLight4Pass != otherPasses.bLight4Pass)
      bLight4Pass = otherPasses.bLight4Pass;
    if (bLight5Pass != otherPasses.bLight5Pass)
      bLight5Pass = otherPasses.bLight5Pass;
    if (bLight6Pass != otherPasses.bLight6Pass)
      bLight6Pass = otherPasses.bLight6Pass;
    if (bLight7Pass != otherPasses.bLight7Pass)
      bLight7Pass = otherPasses.bLight7Pass;
    if (bLight8Pass != otherPasses.bLight8Pass)
      bLight8Pass = otherPasses.bLight8Pass;

    if (bAmbientLightDirectPass != otherPasses.bAmbientLightDirectPass)
      bAmbientLightDirectPass = otherPasses.bAmbientLightDirectPass;
    if (bSunLightDirectPass != otherPasses.bSunLightDirectPass)
      bSunLightDirectPass = otherPasses.bSunLightDirectPass;
    if (bLightDirect1Pass != otherPasses.bLightDirect1Pass)
      bLightDirect1Pass = otherPasses.bLightDirect1Pass;
    if (bLightDirect2Pass != otherPasses.bLightDirect2Pass)
      bLightDirect2Pass = otherPasses.bLightDirect2Pass;
    if (bLightDirect3Pass != otherPasses.bLightDirect3Pass)
      bLightDirect3Pass = otherPasses.bLightDirect3Pass;
    if (bLightDirect4Pass != otherPasses.bLightDirect4Pass)
      bLightDirect4Pass = otherPasses.bLightDirect4Pass;
    if (bLightDirect5Pass != otherPasses.bLightDirect5Pass)
      bLightDirect5Pass = otherPasses.bLightDirect5Pass;
    if (bLightDirect6Pass != otherPasses.bLightDirect6Pass)
      bLightDirect6Pass = otherPasses.bLightDirect6Pass;
    if (bLightDirect7Pass != otherPasses.bLightDirect7Pass)
      bLightDirect7Pass = otherPasses.bLightDirect7Pass;
    if (bLightDirect8Pass != otherPasses.bLightDirect8Pass)
      bLightDirect8Pass = otherPasses.bLightDirect8Pass;

    if (bAmbientLightIndirectPass != otherPasses.bAmbientLightIndirectPass)
      bAmbientLightIndirectPass = otherPasses.bAmbientLightIndirectPass;
    if (bSunLightIndirectPass != otherPasses.bSunLightIndirectPass)
      bSunLightIndirectPass = otherPasses.bSunLightIndirectPass;
    if (bLightIndirect1Pass != otherPasses.bLightIndirect1Pass)
      bLightIndirect1Pass = otherPasses.bLightIndirect1Pass;
    if (bLightIndirect2Pass != otherPasses.bLightIndirect2Pass)
      bLightIndirect2Pass = otherPasses.bLightIndirect2Pass;
    if (bLightIndirect3Pass != otherPasses.bLightIndirect3Pass)
      bLightIndirect3Pass = otherPasses.bLightIndirect3Pass;
    if (bLightIndirect4Pass != otherPasses.bLightIndirect4Pass)
      bLightIndirect4Pass = otherPasses.bLightIndirect4Pass;
    if (bLightIndirect5Pass != otherPasses.bLightIndirect5Pass)
      bLightIndirect5Pass = otherPasses.bLightIndirect5Pass;
    if (bLightIndirect6Pass != otherPasses.bLightIndirect6Pass)
      bLightIndirect6Pass = otherPasses.bLightIndirect6Pass;
    if (bLightIndirect7Pass != otherPasses.bLightIndirect7Pass)
      bLightIndirect7Pass = otherPasses.bLightIndirect7Pass;
    if (bLightIndirect8Pass != otherPasses.bLightIndirect8Pass)
      bLightIndirect8Pass = otherPasses.bLightIndirect8Pass;

    if (bBackinGroupIdPass != otherPasses.bBackinGroupIdPass)
      bBackinGroupIdPass = otherPasses.bBackinGroupIdPass;
    if (bOpacityPass != otherPasses.bOpacityPass)
      bOpacityPass = otherPasses.bOpacityPass;
    if (bRoughnessPass != otherPasses.bRoughnessPass)
      bRoughnessPass = otherPasses.bRoughnessPass;
    if (bIorPass != otherPasses.bIorPass)
      bIorPass = otherPasses.bIorPass;
    if (bDiffuseFilterInfoPass != otherPasses.bDiffuseFilterInfoPass)
      bDiffuseFilterInfoPass = otherPasses.bDiffuseFilterInfoPass;
    if (bReflectionFilterInfoPass != otherPasses.bReflectionFilterInfoPass)
      bReflectionFilterInfoPass = otherPasses.bReflectionFilterInfoPass;
    if (bRefractionFilterInfoPass != otherPasses.bRefractionFilterInfoPass)
      bRefractionFilterInfoPass = otherPasses.bRefractionFilterInfoPass;
    if (bTransmissionFilterInfoPass != otherPasses.bTransmissionFilterInfoPass)
      bTransmissionFilterInfoPass = otherPasses.bTransmissionFilterInfoPass;

    if (bGeomNormalsPass != otherPasses.bGeomNormalsPass)
      bGeomNormalsPass = otherPasses.bGeomNormalsPass;
    if (bShadingNormalsPass != otherPasses.bShadingNormalsPass)
      bShadingNormalsPass = otherPasses.bShadingNormalsPass;
    if (bSmoothNormalsPass != otherPasses.bSmoothNormalsPass)
      bSmoothNormalsPass = otherPasses.bSmoothNormalsPass;
    if (bTangentNormalsPass != otherPasses.bTangentNormalsPass)
      bTangentNormalsPass = otherPasses.bTangentNormalsPass;
    if (bPositionPass != otherPasses.bPositionPass)
      bPositionPass = otherPasses.bPositionPass;
    if (bZdepthPass != otherPasses.bZdepthPass)
      bZdepthPass = otherPasses.bZdepthPass;
    if (bMaterialIdPass != otherPasses.bMaterialIdPass)
      bMaterialIdPass = otherPasses.bMaterialIdPass;
    if (bUVCoordinatesPass != otherPasses.bUVCoordinatesPass)
      bUVCoordinatesPass = otherPasses.bUVCoordinatesPass;
    if (bTangentsPass != otherPasses.bTangentsPass)
      bTangentsPass = otherPasses.bTangentsPass;
    if (bWireframePass != otherPasses.bWireframePass)
      bWireframePass = otherPasses.bWireframePass;
    if (bMotionVectorPass != otherPasses.bMotionVectorPass)
      bMotionVectorPass = otherPasses.bMotionVectorPass;
    if (bObjectIdPass != otherPasses.bObjectIdPass)
      bObjectIdPass = otherPasses.bObjectIdPass;
    if (bLayerIdPass != otherPasses.bLayerIdPass)
      bLayerIdPass = otherPasses.bLayerIdPass;
    if (bLayerMaskPass != otherPasses.bLayerMaskPass)
      bLayerMaskPass = otherPasses.bLayerMaskPass;
    if (bLightPassIdPass != otherPasses.bLightPassIdPass)
      bLightPassIdPass = otherPasses.bLightPassIdPass;
    if (bObjectLayerColorPass != otherPasses.bObjectLayerColorPass)
      bObjectLayerColorPass = otherPasses.bObjectLayerColorPass;

    if (bAOPass != otherPasses.bAOPass)
      bAOPass = otherPasses.bAOPass;

    if (iInfoPassMaxSamples != otherPasses.iInfoPassMaxSamples)
      iInfoPassMaxSamples = otherPasses.iInfoPassMaxSamples;
    if (iSamplingMode != otherPasses.iSamplingMode)
      iSamplingMode = otherPasses.iSamplingMode;
    if (bPassesRaw != otherPasses.bPassesRaw)
      bPassesRaw = otherPasses.bPassesRaw;
    if (bPostProcEnvironment != otherPasses.bPostProcEnvironment)
      bPostProcEnvironment = otherPasses.bPostProcEnvironment;
    if (bBump != otherPasses.bBump)
      bBump = otherPasses.bBump;
    if (bAoAlphaShadows != otherPasses.bAoAlphaShadows)
      bAoAlphaShadows = otherPasses.bAoAlphaShadows;
    if (fZdepthMax != otherPasses.fZdepthMax)
      fZdepthMax = otherPasses.fZdepthMax;
    if (fUVMax != otherPasses.fUVMax)
      fUVMax = otherPasses.fUVMax;
    if (iUVCoordinateSelection != otherPasses.iUVCoordinateSelection)
      iUVCoordinateSelection = otherPasses.iUVCoordinateSelection;
    if (fMaxSpeed != otherPasses.fMaxSpeed)
      fMaxSpeed = otherPasses.fMaxSpeed;
    if (fAODistance != otherPasses.fAODistance)
      fAODistance = otherPasses.fAODistance;
    if (fOpacityThreshold != otherPasses.fOpacityThreshold)
      fOpacityThreshold = otherPasses.fOpacityThreshold;
    if (iCryptomatteChannel != otherPasses.iCryptomatteChannel)
      iCryptomatteChannel = otherPasses.iCryptomatteChannel;
    if (iCryptomatteSeedFactor != otherPasses.iCryptomatteSeedFactor)
      iCryptomatteSeedFactor = otherPasses.iCryptomatteSeedFactor;

    if (bCryptomatteInstance != otherPasses.bCryptomatteInstance)
      bCryptomatteInstance = otherPasses.bCryptomatteInstance;
    if (bCryptomatteMaterialNodeName != otherPasses.bCryptomatteMaterialNodeName)
      bCryptomatteMaterialNodeName = otherPasses.bCryptomatteMaterialNodeName;
    if (bCryptomatteMaterialPinName != otherPasses.bCryptomatteMaterialPinName)
      bCryptomatteMaterialPinName = otherPasses.bCryptomatteMaterialPinName;
    if (bCryptomatteMaterialNode != otherPasses.bCryptomatteMaterialNode)
      bCryptomatteMaterialNode = otherPasses.bCryptomatteMaterialNode;
    if (bCryptomatteObjectNodeName != otherPasses.bCryptomatteObjectNodeName)
      bCryptomatteObjectNodeName = otherPasses.bCryptomatteObjectNodeName;
    if (bCryptomatteObjectPinName != otherPasses.bCryptomatteObjectPinName)
      bCryptomatteObjectPinName = otherPasses.bCryptomatteObjectPinName;
    if (bCryptomatteObjectNode != otherPasses.bCryptomatteObjectNode)
      bCryptomatteObjectNode = otherPasses.bCryptomatteObjectNode;

    return *this;
  }
};  // struct Passes

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
    PHOTON_TRACING,
    NONE
  };
  enum DirectLightMode {
    GI_NONE,
    GI_AMBIENT,
    GI_SAMPLE_AMBIENT,
    GI_AMBIENT_OCCLUSION,
    GI_DIFFUSE
  };
  enum MBAlignmentType { OFF = 0, BEFORE = 1, SYMMETRIC, AFTER };
  enum LayersMode { NORMAL = 0, HIDE_INACTIVE, ONLY_SIDE_EFFECTS, HIDE_FROM_CAMERA };

  KernelType type;

  bool bUseNodeTree;

  float fShutterTime;
  float fCurrentTime;
  MBAlignmentType mbAlignment;  
  float fSubframeStart;
  float fSubframeEnd;
  bool bEmulateOldMotionBlurBehavior;
  float fFrameCount;

  // COMMON
  int32_t iMaxSamples;
  float fFilterSize;
  float fRayEpsilon;
  bool bAlphaChannel;
  float fPathTermPower;
  int32_t iMaxSubdivisionLevel;

  int32_t iWhiteLightSpectrum;
  bool bUseOldPipeline;

  // PATH_TRACE + PMC + DIRECT_LIGHT
  bool bAlphaShadows;
  bool bKeepEnvironment;
  bool bIrradianceMode;
  bool bNestDielectrics;
  bool bEmulateOldVolumeBehavior;

  // AI Light: PATH_TRACE + PMC + DIRECT_LIGHT
  bool bAILightEnable;
  bool bAILightUpdate;
  float fAILightStrength;
  int32_t iLightIDsAction;
  int32_t iLightIDsMask;
  int32_t iLightLinkingInvertMask;
  float fAffectRoughness;

  // PATH_TRACE + PMC
  float fCausticBlur;
  int32_t iMaxDiffuseDepth, iMaxGlossyDepth, iMaxScatterDepth;
  float fGIClamp;

  // DIRECT_LIGHT + INFO_CHANNEL
  float fAODist;

  // PATH_TRACE + DIRECT_LIGHT
  float fCoherentRatio;
  bool bStaticNoise;
  bool bDeepImageEnable;
  bool bDeepRenderPasses;
  int iMaxDepthSamples;
  float fDepthTolerance;

  bool bAdaptiveSampling;
  float fAdaptiveNoiseThreshold;
  float fAdaptiveExpectedExposure;
  int iAdaptiveMinSamples;
  ::Octane::AsPixelGroupMode adaptiveGroupPixels;

  // PATH_TRACE + DIRECT_LIGHT + INFO_CHANNEL
  int iParallelSamples;
  int iMaxTileSamples;
  bool bMinimizeNetTraffic;

  // DIRECT_LIGHT
  int32_t iDiffuseDepth;
  int32_t iGlossyDepth;
  int32_t iSpecularDepth;
  DirectLightMode GIMode;
  int32_t iClayMode;
  std::string sAoTexture;

  // PATH_TRACE

  // PMC
  float fExploration;
  float fDLImportance;
  int32_t iMaxRejects;
  int32_t iParallelism;
  int iWorkChunkSize;

  // INFO_CHANNEL
  OctaneEngine::InfoChannelType infoChannelType;
  float fZdepthMax;
  float fUVMax;
  bool iSamplingMode;
  float fMaxSpeed;
  bool bAoAlphaShadows;
  float fOpacityThreshold;
  bool bBumpNormalMapping;
  bool bBkFaceHighlight;

  // PHOTON TRACING
  int32_t iPhotonDepth;
  bool bAccurateColors;
  float fPhotonGatherRadius;
  float fPhotonGatherMultiplier;
  int iPhotonGatherSamples;
  float fExplorationStrength;

  // Object layers
  bool bLayersEnable;
  int32_t iLayersCurrent;
  bool bLayersInvert;
  LayersMode layersMode;

  float_3 f3ToonShadowAmbient;

  int32_t iSubsampleMode;

  inline Kernel() : type(NONE)
  {
    bUseNodeTree = false;
  }
  inline bool operator==(const Kernel &otherKernel)
  {
    return (
        type == otherKernel.type

        && bUseNodeTree == otherKernel.bUseNodeTree

        && iMaxSamples == otherKernel.iMaxSamples && fFilterSize == otherKernel.fFilterSize &&
        fRayEpsilon == otherKernel.fRayEpsilon && bAlphaChannel == otherKernel.bAlphaChannel &&
        fPathTermPower == otherKernel.fPathTermPower &&
        iMaxSubdivisionLevel == otherKernel.iMaxSubdivisionLevel &&

        iWhiteLightSpectrum == otherKernel.iWhiteLightSpectrum &&
        bUseOldPipeline == otherKernel.bUseOldPipeline

        && bAlphaShadows == otherKernel.bAlphaShadows &&
        bKeepEnvironment == otherKernel.bKeepEnvironment &&
        bIrradianceMode == otherKernel.bIrradianceMode &&
        bNestDielectrics == otherKernel.bNestDielectrics &&
        bEmulateOldVolumeBehavior == otherKernel.bEmulateOldVolumeBehavior

        && bAILightEnable == otherKernel.bAILightEnable &&
        bAILightUpdate == otherKernel.bAILightUpdate &&
        fAILightStrength == otherKernel.fAILightStrength &&
        iLightIDsAction == otherKernel.iLightIDsAction &&
        iLightIDsMask == otherKernel.iLightIDsMask &&
        iLightLinkingInvertMask == otherKernel.iLightLinkingInvertMask

        && fCausticBlur == otherKernel.fCausticBlur &&
        fAffectRoughness == otherKernel.fAffectRoughness &&
        iMaxDiffuseDepth == otherKernel.iMaxDiffuseDepth &&
        iMaxGlossyDepth == otherKernel.iMaxGlossyDepth &&
        iMaxScatterDepth == otherKernel.iMaxScatterDepth && fGIClamp == otherKernel.fGIClamp

        && fAODist == otherKernel.fAODist

        && fCoherentRatio == otherKernel.fCoherentRatio &&
        bStaticNoise == otherKernel.bStaticNoise &&
        bDeepImageEnable == otherKernel.bDeepImageEnable &&
        bDeepRenderPasses == otherKernel.bDeepRenderPasses &&
        iMaxDepthSamples == otherKernel.iMaxDepthSamples &&
        fDepthTolerance == otherKernel.fDepthTolerance

        && bAdaptiveSampling == otherKernel.bAdaptiveSampling &&
        fAdaptiveNoiseThreshold == otherKernel.fAdaptiveNoiseThreshold &&
        fAdaptiveExpectedExposure == otherKernel.fAdaptiveExpectedExposure &&
        iAdaptiveMinSamples == otherKernel.iAdaptiveMinSamples &&
        adaptiveGroupPixels == otherKernel.adaptiveGroupPixels

        && iParallelSamples == otherKernel.iParallelSamples &&
        iMaxTileSamples == otherKernel.iMaxTileSamples &&
        bMinimizeNetTraffic == otherKernel.bMinimizeNetTraffic

        && iDiffuseDepth == otherKernel.iDiffuseDepth &&
        iGlossyDepth == otherKernel.iGlossyDepth && iSpecularDepth == otherKernel.iSpecularDepth &&
        GIMode == otherKernel.GIMode && iClayMode == otherKernel.iClayMode &&
        iSubsampleMode == otherKernel.iSubsampleMode && sAoTexture == otherKernel.sAoTexture

        && fExploration == otherKernel.fExploration &&
        fDLImportance == otherKernel.fDLImportance && iMaxRejects == otherKernel.iMaxRejects &&
        iParallelism == otherKernel.iParallelism && iWorkChunkSize == otherKernel.iWorkChunkSize

        && iPhotonDepth == otherKernel.iPhotonDepth &&
        bAccurateColors == otherKernel.bAccurateColors &&
        fPhotonGatherRadius == otherKernel.fPhotonGatherRadius &&
        fPhotonGatherMultiplier == otherKernel.fPhotonGatherMultiplier &&
        iPhotonGatherSamples == otherKernel.iPhotonGatherSamples &&
        fExplorationStrength == otherKernel.fExplorationStrength

        && infoChannelType == otherKernel.infoChannelType &&
        fZdepthMax == otherKernel.fZdepthMax && fUVMax == otherKernel.fUVMax &&
        iSamplingMode == otherKernel.iSamplingMode && fMaxSpeed == otherKernel.fMaxSpeed &&
        bAoAlphaShadows == otherKernel.bAoAlphaShadows &&
        fOpacityThreshold == otherKernel.fOpacityThreshold &&
        bBumpNormalMapping == otherKernel.bBumpNormalMapping &&
        bBkFaceHighlight == otherKernel.bBkFaceHighlight

        && bLayersEnable == otherKernel.bLayersEnable &&
        iLayersCurrent == otherKernel.iLayersCurrent &&
        bLayersInvert == otherKernel.bLayersInvert && layersMode == otherKernel.layersMode

        && fShutterTime == otherKernel.fShutterTime && fCurrentTime == otherKernel.fCurrentTime &&
        fSubframeStart == otherKernel.fSubframeStart && fSubframeEnd == otherKernel.fSubframeEnd &&
        fFrameCount == otherKernel.fFrameCount &&
        bEmulateOldMotionBlurBehavior == otherKernel.bEmulateOldMotionBlurBehavior &&
        mbAlignment == otherKernel.mbAlignment

        && f3ToonShadowAmbient == otherKernel.f3ToonShadowAmbient);
  }
  inline Kernel &operator=(const Kernel &otherKernel)
  {
    if (type != otherKernel.type)
      type = otherKernel.type;

    if (bUseNodeTree != otherKernel.bUseNodeTree)
      bUseNodeTree = otherKernel.bUseNodeTree;

    if (iMaxSamples != otherKernel.iMaxSamples)
      iMaxSamples = otherKernel.iMaxSamples;
    if (fFilterSize != otherKernel.fFilterSize)
      fFilterSize = otherKernel.fFilterSize;
    if (fRayEpsilon != otherKernel.fRayEpsilon)
      fRayEpsilon = otherKernel.fRayEpsilon;
    if (bAlphaChannel != otherKernel.bAlphaChannel)
      bAlphaChannel = otherKernel.bAlphaChannel;
    if (fPathTermPower != otherKernel.fPathTermPower)
      fPathTermPower = otherKernel.fPathTermPower;
    if (iMaxSubdivisionLevel != otherKernel.iMaxSubdivisionLevel)
      iMaxSubdivisionLevel = otherKernel.iMaxSubdivisionLevel;

    if (iWhiteLightSpectrum != otherKernel.iWhiteLightSpectrum)
      iWhiteLightSpectrum = otherKernel.iWhiteLightSpectrum;
    if (bUseOldPipeline != otherKernel.bUseOldPipeline)
      bUseOldPipeline = otherKernel.bUseOldPipeline;

    if (bAlphaShadows != otherKernel.bAlphaShadows)
      bAlphaShadows = otherKernel.bAlphaShadows;
    if (bKeepEnvironment != otherKernel.bKeepEnvironment)
      bKeepEnvironment = otherKernel.bKeepEnvironment;
    if (bIrradianceMode != otherKernel.bIrradianceMode)
      bIrradianceMode = otherKernel.bIrradianceMode;
    if (bNestDielectrics != otherKernel.bNestDielectrics)
      bNestDielectrics = otherKernel.bNestDielectrics;
    if (bEmulateOldVolumeBehavior != otherKernel.bEmulateOldVolumeBehavior)
      bEmulateOldVolumeBehavior = otherKernel.bEmulateOldVolumeBehavior;

    if (bAILightEnable != otherKernel.bAILightEnable)
      bAILightEnable = otherKernel.bAILightEnable;
    if (bAILightUpdate != otherKernel.bAILightUpdate)
      bAILightUpdate = otherKernel.bAILightUpdate;
    if (fAILightStrength != otherKernel.fAILightStrength)
      fAILightStrength = otherKernel.fAILightStrength;
    if (iLightIDsAction != otherKernel.iLightIDsAction)
      iLightIDsAction = otherKernel.iLightIDsAction;
    if (iLightIDsMask != otherKernel.iLightIDsMask)
      iLightIDsMask = otherKernel.iLightIDsMask;
    if (iLightLinkingInvertMask != otherKernel.iLightLinkingInvertMask)
      iLightLinkingInvertMask = otherKernel.iLightLinkingInvertMask;

    if (fCausticBlur != otherKernel.fCausticBlur)
      fCausticBlur = otherKernel.fCausticBlur;
    if (fAffectRoughness != otherKernel.fAffectRoughness)
      fAffectRoughness = otherKernel.fAffectRoughness;
    if (iMaxDiffuseDepth != otherKernel.iMaxDiffuseDepth)
      iMaxDiffuseDepth = otherKernel.iMaxDiffuseDepth;
    if (iMaxGlossyDepth != otherKernel.iMaxGlossyDepth)
      iMaxGlossyDepth = otherKernel.iMaxGlossyDepth;
    if (iMaxScatterDepth != otherKernel.iMaxScatterDepth)
      iMaxScatterDepth = otherKernel.iMaxScatterDepth;
    if (fGIClamp != otherKernel.fGIClamp)
      fGIClamp = otherKernel.fGIClamp;

    if (fAODist != otherKernel.fAODist)
      fAODist = otherKernel.fAODist;

    if (fCoherentRatio != otherKernel.fCoherentRatio)
      fCoherentRatio = otherKernel.fCoherentRatio;
    if (bStaticNoise != otherKernel.bStaticNoise)
      bStaticNoise = otherKernel.bStaticNoise;
    if (bDeepImageEnable != otherKernel.bDeepImageEnable)
      bDeepImageEnable = otherKernel.bDeepImageEnable;
    if (bDeepRenderPasses != otherKernel.bDeepRenderPasses)
      bDeepRenderPasses = otherKernel.bDeepRenderPasses;
    if (iMaxDepthSamples != otherKernel.iMaxDepthSamples)
      iMaxDepthSamples = otherKernel.iMaxDepthSamples;
    if (fDepthTolerance != otherKernel.fDepthTolerance)
      fDepthTolerance = otherKernel.fDepthTolerance;

    if (bAdaptiveSampling != otherKernel.bAdaptiveSampling)
      bAdaptiveSampling = otherKernel.bAdaptiveSampling;
    if (fAdaptiveNoiseThreshold != otherKernel.fAdaptiveNoiseThreshold)
      fAdaptiveNoiseThreshold = otherKernel.fAdaptiveNoiseThreshold;
    if (fAdaptiveExpectedExposure != otherKernel.fAdaptiveExpectedExposure)
      fAdaptiveExpectedExposure = otherKernel.fAdaptiveExpectedExposure;
    if (iAdaptiveMinSamples != otherKernel.iAdaptiveMinSamples)
      iAdaptiveMinSamples = otherKernel.iAdaptiveMinSamples;
    if (adaptiveGroupPixels != otherKernel.adaptiveGroupPixels)
      adaptiveGroupPixels = otherKernel.adaptiveGroupPixels;

    if (iParallelSamples != otherKernel.iParallelSamples)
      iParallelSamples = otherKernel.iParallelSamples;
    if (iMaxTileSamples != otherKernel.iMaxTileSamples)
      iMaxTileSamples = otherKernel.iMaxTileSamples;
    if (bMinimizeNetTraffic != otherKernel.bMinimizeNetTraffic)
      bMinimizeNetTraffic = otherKernel.bMinimizeNetTraffic;

    if (iDiffuseDepth != otherKernel.iDiffuseDepth)
      iDiffuseDepth = otherKernel.iDiffuseDepth;
    if (iGlossyDepth != otherKernel.iGlossyDepth)
      iGlossyDepth = otherKernel.iGlossyDepth;
    if (iSpecularDepth != otherKernel.iSpecularDepth)
      iSpecularDepth = otherKernel.iSpecularDepth;
    if (GIMode != otherKernel.GIMode)
      GIMode = otherKernel.GIMode;
    if (iClayMode != otherKernel.iClayMode)
      iClayMode = otherKernel.iClayMode;
    if (iSubsampleMode != otherKernel.iSubsampleMode)
      iSubsampleMode = otherKernel.iSubsampleMode;
    if (sAoTexture != otherKernel.sAoTexture)
      sAoTexture = otherKernel.sAoTexture;

    if (fExploration != otherKernel.fExploration)
      fExploration = otherKernel.fExploration;
    if (fDLImportance != otherKernel.fDLImportance)
      fDLImportance = otherKernel.fDLImportance;
    if (iMaxRejects != otherKernel.iMaxRejects)
      iMaxRejects = otherKernel.iMaxRejects;
    if (iParallelism != otherKernel.iParallelism)
      iParallelism = otherKernel.iParallelism;
    if (iWorkChunkSize != otherKernel.iWorkChunkSize)
      iWorkChunkSize = otherKernel.iWorkChunkSize;

    if (iPhotonDepth != otherKernel.iPhotonDepth)
      iPhotonDepth = otherKernel.iPhotonDepth;
    if (bAccurateColors != otherKernel.bAccurateColors)
      bAccurateColors = otherKernel.bAccurateColors;
    if (fPhotonGatherRadius != otherKernel.fPhotonGatherRadius)
      fPhotonGatherRadius = otherKernel.fPhotonGatherRadius;
    if (fPhotonGatherMultiplier != otherKernel.fPhotonGatherMultiplier)
      fPhotonGatherMultiplier = otherKernel.fPhotonGatherMultiplier;
    if (iPhotonGatherSamples != otherKernel.iPhotonGatherSamples)
      iPhotonGatherSamples = otherKernel.iPhotonGatherSamples;
    if (fExplorationStrength != otherKernel.fExplorationStrength)
      fExplorationStrength = otherKernel.fExplorationStrength;

    if (infoChannelType != otherKernel.infoChannelType)
      infoChannelType = otherKernel.infoChannelType;
    if (fZdepthMax != otherKernel.fZdepthMax)
      fZdepthMax = otherKernel.fZdepthMax;
    if (fUVMax != otherKernel.fUVMax)
      fUVMax = otherKernel.fUVMax;
    if (iSamplingMode != otherKernel.iSamplingMode)
      iSamplingMode = otherKernel.iSamplingMode;
    if (fMaxSpeed != otherKernel.fMaxSpeed)
      fMaxSpeed = otherKernel.fMaxSpeed;
    if (bAoAlphaShadows != otherKernel.bAoAlphaShadows)
      bAoAlphaShadows = otherKernel.bAoAlphaShadows;
    if (fOpacityThreshold != otherKernel.fOpacityThreshold)
      fOpacityThreshold = otherKernel.fOpacityThreshold;
    if (bBumpNormalMapping != otherKernel.bBumpNormalMapping)
      bBumpNormalMapping = otherKernel.bBumpNormalMapping;
    if (bBkFaceHighlight != otherKernel.bBkFaceHighlight)
      bBkFaceHighlight = otherKernel.bBkFaceHighlight;

    if (bLayersEnable != otherKernel.bLayersEnable)
      bLayersEnable = otherKernel.bLayersEnable;
    if (iLayersCurrent != otherKernel.iLayersCurrent)
      iLayersCurrent = otherKernel.iLayersCurrent;
    if (bLayersInvert != otherKernel.bLayersInvert)
      bLayersInvert = otherKernel.bLayersInvert;
    if (layersMode != otherKernel.layersMode)
      layersMode = otherKernel.layersMode;

    if (fShutterTime != otherKernel.fShutterTime)
      fShutterTime = otherKernel.fShutterTime;
    if (fCurrentTime != otherKernel.fCurrentTime)
      fCurrentTime = otherKernel.fCurrentTime;
    if (fSubframeStart != otherKernel.fSubframeStart)
      fSubframeStart = otherKernel.fSubframeStart;
    if (fSubframeEnd != otherKernel.fSubframeEnd)
      fSubframeEnd = otherKernel.fSubframeEnd;
    if (fFrameCount != otherKernel.fFrameCount)
      fFrameCount = otherKernel.fFrameCount;
    if (mbAlignment != otherKernel.mbAlignment)
      mbAlignment = otherKernel.mbAlignment;
    if (bEmulateOldMotionBlurBehavior != otherKernel.bEmulateOldMotionBlurBehavior)
      bEmulateOldMotionBlurBehavior = otherKernel.bEmulateOldMotionBlurBehavior;

    if (f3ToonShadowAmbient != otherKernel.f3ToonShadowAmbient)
      f3ToonShadowAmbient = otherKernel.f3ToonShadowAmbient;

    return *this;
  }
};  // struct Kernel

}  // namespace OctaneEngine

#endif
