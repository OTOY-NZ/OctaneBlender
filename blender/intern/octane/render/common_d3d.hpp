#pragma once

class CommonD3D {
 public:
#if defined(WIN32)
  static void InitD3D11();
  static void ReleaseD3D11();
  static bool IsD3DInited();
  static void *GetD3DDevice();
  static void GetD3DDeviceLuid(unsigned long &LowPart, long &HighPart);
#endif
};