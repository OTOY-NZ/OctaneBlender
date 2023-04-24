//--------------------------------------------------------------------------------
/// @ref OctaneServerModule
/// @file common_d3d.cpp
///
//	(c) 2021 OTOY, Inc.
//--------------------------------------------------------------------------------
#include "common_d3d.hpp"

#if defined(WIN32)
#  include <d3d11_1.h>
#  include <dxgi.h>
//--------------------------------------------------------------------------------

static ID3D11Device1 *mDevice11_1 = nullptr;
static ID3D11DeviceContext *mContext11 = nullptr;
static D3D11_TEXTURE2D_DESC mCopyTextureDesc;
static ID3D11Texture2D *mTexCopy = nullptr;
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
  bool result = false;
  HMODULE d3d_lib = LoadLibraryA("d3d11.dll");
  if (d3d_lib != nullptr) {
    PFN_D3D11_CREATE_DEVICE D3D11CreateDeviceFn = (PFN_D3D11_CREATE_DEVICE)GetProcAddress(
        d3d_lib, "D3D11CreateDevice");
    ID3D11Device *device11;
    HRESULT hresult = D3D11CreateDeviceFn(NULL,
                                         D3D_DRIVER_TYPE_HARDWARE,
                                         NULL,
                                         0,
                                         NULL,
                                         0,
                                         D3D11_SDK_VERSION,
                                         &device11,
                                         NULL,
                                         &mContext11);
    if (hresult == S_OK) {
      hresult = device11->QueryInterface(__uuidof(ID3D11Device1), (void **)&mDevice11_1);
      if (hresult == S_OK) {
        result = true;
        device11->Release();
      }
    }    
  }
  mIsD3DInited = result;
}

bool CommonD3D::IsD3DInited()
{
  return mIsD3DInited;
}
#endif
