/*
 * Copyright 2011, Blender Foundation.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

#include "kernel.h"

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// CONSTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Kernel::Kernel()
{
  oct_node = new ::OctaneEngine::Kernel;

  oct_node->type = ::OctaneEngine::Kernel::DIRECT_LIGHT;

  // COMMON
  oct_node->fShutterTime = 0.0f;
  oct_node->fCurrentTime = 0.0f;
  oct_node->iMaxSamples = 10;
  oct_node->iMaxSubdivisionLevel = 10;
  // oct_node->iMaxPreviewSamples  = 16000;
  oct_node->fFilterSize = 1.2f;
  oct_node->fRayEpsilon = 0.0001f;
  oct_node->bAlphaChannel = false;
  oct_node->bAlphaShadows = true;
  oct_node->bBumpNormalMapping = false;
  oct_node->bBkFaceHighlight = false;
  oct_node->fPathTermPower = 0.3f;

  // PATH_TRACE + PMC + DIRECT_LIGHT
  oct_node->bKeepEnvironment = false;
  oct_node->bIrradianceMode = false;
  oct_node->bEmulateOldVolumeBehavior = false;

  // AI Light: PATH_TRACE + PMC + DIRECT_LIGHT
  oct_node->bAILightEnable = false;
  oct_node->bAILightUpdate = false;
  oct_node->fAILightStrength = 0.8f;
  oct_node->iLightIDsAction = 1;
  oct_node->iLightIDsMask = 0;
  oct_node->iLightLinkingInvertMask = 0;

  oct_node->fAffectRoughness = 0.2f;

  // PATH_TRACE + PMC
  oct_node->fCausticBlur = 0.0f;
  oct_node->iMaxDiffuseDepth = 3;
  oct_node->iMaxGlossyDepth = 24;
  oct_node->iMaxScatterDepth = 8;

  // PATH_TRACE + DIRECT_LIGHT
  oct_node->fCoherentRatio = 0.0f;
  oct_node->bStaticNoise = false;

  // DIRECT_LIGHT
  oct_node->iSpecularDepth = 5;
  oct_node->iGlossyDepth = 2;
  oct_node->fAODist = 3.0f;
  oct_node->GIMode = ::OctaneEngine::Kernel::GI_AMBIENT_OCCLUSION;
  oct_node->iClayMode = 0;
  oct_node->iDiffuseDepth = 2;
  oct_node->sAoTexture = "";

  // PATH_TRACE

  // PMC
  oct_node->fExploration = 0.7f;
  oct_node->fGIClamp = 1000000.0f;
  oct_node->fDLImportance = 0.1f;
  oct_node->iMaxRejects = 500;
  oct_node->iParallelism = 4;

  // INFO_CHANNEL
  oct_node->infoChannelType = ::Octane::IC_TYPE_GEOMETRIC_NORMAL;
  oct_node->fZdepthMax = 5.0f;
  oct_node->fUVMax = 1.0f;
  oct_node->iSamplingMode = 0;
  oct_node->fMaxSpeed = 1.0f;

  oct_node->bLayersEnable = false;
  oct_node->iLayersCurrent = 1;
  oct_node->bLayersInvert = false;
  oct_node->layersMode = ::OctaneEngine::Kernel::NORMAL;

  oct_node->mbAlignment = ::OctaneEngine::Kernel::OFF;

  need_update = true;
}  // Kernel()

Kernel::~Kernel()
{
  delete oct_node;
}  //~Kernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Load the kernel settings to Octane
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Kernel::server_update(::OctaneEngine::OctaneClient *server, Scene *scene, bool interactive)
{
  if (need_update) {
    server->uploadKernel(oct_node);
    need_update = false;
  }
}  // server_update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if kernel settings were modified
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool Kernel::modified(const Kernel &kernel)
{
  return !(*oct_node == *kernel.oct_node);
}  // modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Tag for update
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Kernel::tag_update(void)
{
  need_update = true;
}  // tag_update()

OCT_NAMESPACE_END
