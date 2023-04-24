//--------------------------------------------------------------------------------
/// @ref OctaneServerModule
/// @file common_d3d.cpp
///
//	(c) 2021 OTOY, Inc.
//--------------------------------------------------------------------------------
#include "common_d3d.hpp"
#include "util/util_opengl.h"
#if defined(WIN32)
#  include <d3d11_1.h>
#  include <dxgi.h>
//--------------------------------------------------------------------------------

static ID3D11Device1 *mDevice11_1 = nullptr;
static ID3D11DeviceContext *mContext11 = nullptr;
static D3D11_TEXTURE2D_DESC mCopyTextureDesc;
static ID3D11Texture2D *mTexCopy = nullptr;
static LUID mRendererLuid;
static bool mIsD3DInited = false;
//--------------------------------------------------------------------------------

void *CommonD3D::GetD3DDevice()
{
  return mDevice11_1;
}
//--------------------------------------------------------------------------------

void CommonD3D::ReleaseD3D11()
{
  if (mTexCopy)
    mTexCopy->Release();
  if (mContext11)
    mContext11->Release();
  if (mDevice11_1)
    mDevice11_1->Release();

  mTexCopy = nullptr;
  mContext11 = nullptr;
  mDevice11_1 = nullptr;
  mIsD3DInited = false;
}
//--------------------------------------------------------------------------------

void CommonD3D::InitD3D11()
{
  GLubyte deviceLUID[GL_LUID_SIZE_EXT];  // 8 bytes identifier.
  GLint nodeMask;  // Node mask used together with the LUID to identify OpenGL device uniquely.
  memset(deviceLUID, 0, sizeof(deviceLUID));
  // It is not expected that a single context will be associated with multiple DXGI adapters,
  // so only one LUID is returned.
  glGetUnsignedBytevEXT(GL_DEVICE_LUID_EXT, deviceLUID);
  glGetIntegerv(GL_DEVICE_NODE_MASK_EXT, &nodeMask);
  memcpy(&mRendererLuid, (LUID *)&deviceLUID, sizeof(LUID));
  IDXGIFactory2 *pFactory2;
  HRESULT result = CreateDXGIFactory1(__uuidof(IDXGIFactory2), (void **)(&pFactory2));
  if (result != S_OK) {
    return;
  }
  UINT index = 0;
  IDXGIAdapter *pAdapter = NULL;
  while (SUCCEEDED(pFactory2->EnumAdapters(index, &pAdapter))) {
    DXGI_ADAPTER_DESC desc;
    pAdapter->GetDesc(&desc);
    if (mRendererLuid.HighPart == desc.AdapterLuid.HighPart &&
        mRendererLuid.LowPart == desc.AdapterLuid.LowPart) {
      // Identified a matching adapter.
      break;
    }
    pAdapter->Release();
    pAdapter = NULL;
    index++;
  }
  ID3D11Device *device11;
  D3D_FEATURE_LEVEL l = D3D_FEATURE_LEVEL_11_1;
  if (FAILED(result = D3D11CreateDevice(pAdapter,
                                        D3D_DRIVER_TYPE_UNKNOWN,
                                        nullptr,
                                        0,
                                        &l,
                                        1,  // feature levels
                                        D3D11_SDK_VERSION,
                                        &device11,
                                        NULL,        // feature level
                                        &mContext11  // immediate context
                                        ))) {
    return;
  }
  result = device11->QueryInterface(__uuidof(ID3D11Device1), (void **)&mDevice11_1);
  device11->Release();
  if (result != S_OK) {
    return;
  }
  mIsD3DInited = true;
}

bool CommonD3D::IsD3DInited()
{
  return mIsD3DInited;
}

void CommonD3D::GetD3DDeviceLuid(unsigned long &LowPart, long &HighPart)
{
  LowPart = mRendererLuid.LowPart;
  HighPart = mRendererLuid.HighPart;
}
#endif
