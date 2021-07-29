#ifndef __OCTANE_CLIENT_H__
#define __OCTANE_CLIENT_H__

#define MAX_OCTANE_UV_SETS 3

#define GLOBAL_MESH_NAME "__global"
#define GLOBAL_MESH_LAYERMAP_NAME "__global_lm"
#define GLOBAL_LIGHT_NAME "__global_lights"
#define GLOBAL_LIGHT_LAYERMAP_NAME "__global_lights_lm"

#include "octane_data_type.h"
#include "octane_network_const.h"

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

#ifdef _WIN32
#  define LOCK_MUTEX(x) ::EnterCriticalSection(&(x));
#else
#  define LOCK_MUTEX(x) pthread_mutex_lock(&(x));
#endif  //#ifdef _WIN32

#ifdef _WIN32
#  define UNLOCK_MUTEX(x) ::LeaveCriticalSection(&(x));
#else
#  define UNLOCK_MUTEX(x) pthread_mutex_unlock(&(x));
#endif  //#ifdef _WIN32

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Render Server
/// OctaneClient class is used to communicate with OctaneEngine.
/// Create the instance of OctaneClient class and connect it to the server using
/// connectToServer(). You need to check that the server has the proper version using
/// checkServerVersion(). To start the rendering of the scene, first call the reset() method to
/// prepare the scene for rendering. Then upload the scene data using all the upload methods. End
/// the scene uploading by startRender() method. Refresh the image buffer cache by the currently
/// rendered image from the server by downloadImageBuffer() method. Get the image by
/// getImgBuffer8bit(), getCopyImgBuffer8bit(), getImgBufferFloat() or getCopyImgBufferFloat().
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class OctaneClient {
 public:
  ////////////////////////////////////////////////////////////////////////////////////////////////
  // Render Server structures

  /// The information about the server we are currently connected to.
  struct RenderServerInfo {
    string sNetAddress;            ///< The network address of the server.
    string sDescription;           ///< Server description (currently not used).
    std::vector<string> gpuNames;  ///< Names of active GPUs on a server.
  };                               // struct RenderServerInfo

  /// The render statistics returned by the **GET_IMAGE** packet.
  struct RenderStatistics {
    uint32_t uiCurSamples,    ///< Amount of samples per pixel currently rendered.
        uiCurDenoiseSamples,  ///< Amount of denoise samples per pixel currently rendered.
        uiMaxSamples;         ///< Max. samples to render.
    uint64_t ulVramUsed,      ///< Amount of VRAM used.
        ulVramFree,           ///< Amount of free VRAM.
        ulVramTotal;          ///< Total amount of VRAM.
    float fSPS,               ///< The current rendering speed (in samples per second).
        fRenderTime,          ///< Render time.
        fGamma;               ///< Image gamma.
    uint32_t uiTrianglesCnt,  ///< The total amount of triangles in currently rendered scene.
        uiMeshesCnt,          ///< The total amount of meshes in currently rendered scene.
        uiSpheresCnt,     ///< The total amount of sphere primitives in currently rendered scene.
        uiVoxelsCnt,      ///< The total amount of voxels in currently rendered scene.
        uiDisplCnt,       ///< The total amount of displacement polygons.
        uiHairsCnt;       ///< The total amount of hairs.
    uint32_t uiRgb32Cnt,  ///< The total amount of RGB-32 textures in currently rendered scene.
        uiRgb64Cnt,       ///< The total amount of RGB-64 textures in currently rendered scene.
        uiGrey8Cnt,       ///< The total amount of Grey-8 textures in currently rendered scene.
        uiGrey16Cnt;      ///< The total amount of Grey-16 textures in currently rendered scene.
    uint32_t uiNetGPUs,   ///< The amount of available network GPUs.
        uiNetGPUsUsed;    ///< The amount of network GPUs used by current rendering session.
    int32_t iExpiryTime;  ///< Expiry time (in seconds) for the subscription version.
    int32_t iComponentsCnt;  ///< Number of color components in image.
    uint32_t uiW,            ///< Render width.
        uiH,                 ///< Render height.
        uiRegW,              ///< Render region width.
        uiRegH;              ///< Render region height.
  };                         // struct RenderStatistics

  OctaneClient();
  ~OctaneClient();

  /// Sets the output path for alembic or ORBX export file, or for deep image file.
  /// Should be a full path containing file name without extension.
  /// @param [in] szOutPath - path for the assets.
  void setOutputPath(const char *szOutPath, const char *szCachePath);

  /// Sets the type of export (no export, alembic or ORBX).
  /// @param [in] exportSceneType - type of scene export.
  void setExportType(const SceneExportTypes::SceneExportTypesEnum exportSceneType);

  /// Connects to the given Octane server.
  /// @param [in] szAddr - server address
  /// @return **true** if connection has been successful, **false** otherwise.
  bool connectToServer(const char *szAddr, int port = RENDER_SERVER_PORT);
  /// Disconnects from the currently connected Octane server. Safe to call when not connected.
  /// @return **true** if disconnection has been successful, **false** otherwise.
  bool disconnectFromServer();
  /// Check if connected to server.
  /// @return **true** if connected, **false** otherwise.
  bool checkServerConnection();
  bool testProfileTransferData();
  std::string getServerAdress();

  bool downloadOctaneDB(OctaneDataTransferObject::OctaneDBNodes &nodes);

  /// Block any server updates (all data upload functions will do nothing).
  /// @param [in] bBlocked - current "blocked" status.
  void setUpdatesBlocked(bool bBlocked);

  /// Get the current error message returned by Octane server.
  /// @return A reference to **std::string** value containing the message.
  const string &getServerErrorMessage();
  /// Clear the current error message returned by Octane server.
  void clearServerErrorMessage();
  /// Get the info about the currently connected Octane server.
  /// @return RenderServerInfo structure containing information about the server.
  RenderServerInfo &getServerInfo(void);
  /// Get the current fail reason.
  /// @return Enum value of FailReasons type.
  FailReasons::FailReasonsEnum getFailReason(void);

  bool initOctaneApi();
  bool ReleaseOctaneApi();

  /// Check the connected OctaneEngine version.
  /// @return **true** if the server has the corresponding version, **false** otherwise.
  /// Disconnets from the server if wrong version.
  bool checkServerVersion();
  /// Activate the Octane license on server.
  /// @param [in] sStandLogin - The login of standalone license.
  /// @param [in] sStandPass - The password of standalone license.
  /// @param [in] sLogin - The login of a plugin license.
  /// @param [in] sPass - The password of a plugin license.
  /// @return **true** if successfully activated, **false** otherwise.
  bool activate(string const &sStandLogin,
                string const &sStandPass,
                string const &sLogin,
                string const &sPass);

  /// Reset the project on the server.
  /// @param [in] exportSceneType - Type of the scene export (NONE if just rendering).
  /// @param [in] fFrameTimeSampling - Time sampling of the frames (for the animation and motion
  /// blur).
  /// @param [in] fFps - Frames per second value.
  void reset(bool bInteractive,
             SceneExportTypes::SceneExportTypesEnum exportSceneType,
             float fFrameTimeSampling,
             float fFps,
             bool bDeepImage,
             bool bExportWithObjectLayers);

  /// Delete all the nodes int the project currently loaded on the server. Does nothing if a file
  /// export session is active.
  void clear();

  /// Update current render project on the server.
  /// @return **true** if successfully updated, **false** otherwise.
  bool update();

  /// Start the rendering process on the server.
  /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
  /// @param [in] iWidth - The width of the the rendered image.
  /// @param [in] iHeigth - The heigth of the the rendered image.
  /// @param [in] imgType - The type of the rendered image.
  /// @param [in] bOutOfCoreEnabled - Enable "out of core" mode.
  /// @param [in] iOutOfCoreMemLimit - Memory limit for "out of core" mode.
  /// @param [in] iOutOfCoreGPUHeadroom - GPU headroom for "out of core" mode.
  void startRender(bool bInteractive,
                   int32_t iWidth,
                   int32_t iHeigth,
                   ImageType imgType,
                   bool bOutOfCoreEnabled,
                   int32_t iOutOfCoreMemLimit,
                   int32_t iOutOfCoreGPUHeadroom,
                   int32_t iRenderPriority,
                   int32_t iResourceCacheType);
  /// Stop the render process on the server.
  /// Mostly needed to close the animation export sequence on the server.
  /// @param [in] fFPS - Frames per second value.
  void stopRender(float fFPS);
  /// Check if the scene has already been loaded onto the server and startRender() has been
  /// called.
  bool isRenderStarted();
  /// Pause the current rendering.
  void pauseRender(int32_t bPause);
  /// Start the frame uploading.
  /// Mostly needed to upload the animation export sequence to the server or for motion blur.
  void startFrameUpload();
  /// Indicate to the server that the frame uploading has been finished.
  /// Mostly needed to upload the animation export sequence to the server.
  /// @param [in] bUpdate - Do the update of the loaded scene on the server or for motion blur.
  void finishFrameUpload(bool bUpdate);

  /// Upload camera to render server.
  /// @param [in] pCamera - Camera data structure.
  /// @param [in] uiFrameIdx - The index of the frame the camera is loaded for.
  /// @param [in] uiTotalFrames - First time the animated frames of camera are uploaded (starting
  /// from 0) - this value contains the total amount of frames this camera node is going to be
  /// uploaded for.
  void uploadCamera(Camera *pCamera, uint32_t uiFrameIdx, uint32_t uiTotalFrames);
  bool checkUniversalCameraUpdated(bool useUniversalCamera, OctaneDataTransferObject::OctaneUniversalCamera& current);

  /// Upload kernel configuration to render server.
  /// @param [in] pKernel - Kernel data structure.
  void uploadKernel(Kernel *pKernel);

  /// Upload the configuration of region of image to render.
  /// @param [in] pCamera - Camera data structure.
  /// @param [in] bInteractive - Is the session ment to be interactive or "final render".
  void uploadRenderRegion(Camera *pCamera, bool bInteractive);

  /// Delete the node on the server.
  /// @param [in] pNodeData - Pointer to node data structure holding node's type and name.
  void deleteNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData);

  /// Upload scatter node to server. Only one matrix upload is supported for "movable" mode at
  /// the time.
  /// @param [in] sScatterName - Statter's unique name.
  /// @param [in] sMeshName - Unique name of geometry node being scattered.
  /// @param [in] piInstanceIds - id for each scatter instance (used in instance range or
  /// instance color nodes).
  /// @param [in] pfMatrices - Array of 4x3 matrices. Only one matrix upload is supported for
  /// "movable" mode at the time.
  /// @param [in] ulMatrCnt - Count of matrices. Only one matrix upload is supported for
  /// "movable" mode at the time, so this must always be 1 if **bMovable** is set to **true**.
  /// @param [in] bMovable - Load the scatter as movable. That means the animated sequence of
  /// matrices will be loaded for every frame on the server. See **uiFrameIdx** and
  /// **uiTotalFrames**.
  /// @param [in] asShaderNames - Array of names of shaders assigned to scatters.
  /// @param [in] uiFrameIdx - The index of the frame the scatter is loaded for. Makes sense only
  /// if **bMovable** is set to **true**, otherwise must be 0.
  /// @param [in] uiTotalFrames - First time the animated frames of scatter are uploaded
  /// (starting from 0) - this value contains the total amount of frames this scatter node is
  /// going to be uploaded for. To re-upload the scatter node for some already loaded frames -
  /// set this parameter to 0 and **uiFrameIdx** to needed frame index.
  void uploadScatter(string &sScatterName,
                     string &sMeshName,
                     bool bUseGeoMat,
                     float *pfMatrices,
                     int32_t *piInstanceIds,
                     uint64_t ulMatrCnt,
                     bool bMovable,
                     vector<string> &asShaderNames,
                     uint32_t uiFrameIdx,
                     uint32_t uiTotalFrames);
  /// Delete the scatter node on the server.
  /// @param [in] sName - Unique name of the scatter node that is going to be deleted on the
  /// server.
  void deleteScatter(string const &sName);
  void uploadOctaneObjects(OctaneDataTransferObject::OctaneObjects &objects);

  void uploadOctaneMesh(OctaneDataTransferObject::OctaneMeshes &meshes);
  void getOctaneGeoNodes(std::set<std::string> &nodeNames);
  /// Delete the mesh node on the server.
  /// @param [in] bGlobal - Set to **true** if the global world-space mesh needs to be deleted.
  /// @param [in] sName - Unique name of the mesh node that is going to be deleted on the server.
  /// Does not make sense if **bGloabl** is true.
  void deleteMesh(bool bGlobal, string const &sName);
  /// Upload layer map node to the server.
  /// @param [in] bGlobal - If **true**, the layer map of global mesh is going to be loaded.
  /// @param [in] sName - Unique name of the layer map node.
  /// @param [in] sMeshName - Unique name of geometry node being layered.
  /// @param [in] iLayersCnt - Number of layers in this map.
  /// @param [in] piLayerId - Array with layer number for each layer node.
  /// @param [in] piBakingGroupId - Array with baking group number for each layer node.
  /// @param [in] pfGeneralVis - Array with "General visibility" value for each layer node.
  /// @param [in] pbCamVis - Array with "Camera visibility" value for each layer node.
  /// @param [in] pbShadowVis - Array with "Shadow visibility" value for each layer node.
  /// @param [in] piRandColorSeed - Array with "Random color seed" value for each layer node.
  void uploadLayerMap(bool bGlobal,
                      string const &sLayerMapName,
                      string const &sMeshName,
                      int32_t iLayersCnt,
                      int32_t *piLayerId,
                      int32_t *piBakingGroupId,
                      float *pfGeneralVis,
                      bool *pbCamVis,
                      bool *pbShadowVis,
                      int32_t *piRandColorSeed,
                      int32_t *piLightPassMask);
  /// Delete the layer node on the server.
  /// @param [in] sName - Unique name of the layer node that is going to be deleted on the
  /// server.
  void deleteLayerMap(string const &sName);
  /// Upload the OpenVDB volume node to the server.
  /// @param [in] pNode - Volume data structure.
  void uploadVolume(OctaneDataTransferObject::OctaneVolume *pNode);
  /// Delete the volume node on the server.
  /// @param [in] sName - Unique name of the volume node that is going to be deleted on the
  /// server.
  void deleteVolume(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // LIGHTS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  void uploadLight(OctaneDataTransferObject::OctaneLight *light);
  void deleteLight(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // MATERIALS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the material node on the server.
  /// @param [in] sName - Unique name of the material.
  void deleteMaterial(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // TEXTURES
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  void uploadOctaneNode(OctaneDataTransferObject::OctaneNodeBase *node,
                        OctaneDataTransferObject::OctaneNodeResponse *pResponse = NULL);

  /// Delete the texture node on the server.
  /// @param [in] sName - Unique name of the texture.
  void deleteTexture(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // EMISSIONS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the emission node on the server.
  /// @param [in] sName - Unique name of the emission.
  void deleteEmission(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // MEDIUMS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the medium node on the server.
  /// @param [in] sName - Unique name of the medium.
  void deleteMedium(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // TRANSFORMS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the transform node on the server.
  /// @param [in] sName - Unique name of the transform.
  void deleteTransform(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // PROJECTIONS
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Delete the projection node on the server.
  /// @param [in] sName - Unique name of the projection.
  void deleteProjection(string const &sName);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // VALUES
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  void deleteValue(string const &sName);

  /// Get current render-buffer pass type.
  Octane::RenderPassId currentPassType();

  /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently cached image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
  /// @param [out] pucBuf - Pointer to cached image buffer.
  /// @param [in] iWidth - Requested width of the whole image. If **iWidth <= 0** or **iHeight <=
  /// 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iRegionWidth - Requested width of the region. Must be equal to iWidth if you
  /// need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <=
  /// 0** or
  /// **iRegionHeight <= 0** this method returns the current cache (if any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if you
  /// need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or **iRegionWidth <=
  /// 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its size
  /// in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  bool getImgBuffer8bit(int &iComponentsCnt,
                        uint8_t *&pucBuf,
                        int iWidth,
                        int iHeight,
                        int iRegionWidth,
                        int iRegionHeight);
  /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
  /// @param [out] pucBuf - Pointer to the buffer holding the copy of cached image buffer. It is
  /// caller's responsibility to **delete[]** this buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  bool getCopyImgBuffer8bit(int iComponentsCnt,
                            uint8_t *&pucBuf,
                            int iWidth,
                            int iHeight,
                            int iRegionWidth,
                            int iRegionHeight);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // Get Image-buffer of given pass
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /// Get a pointer to cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different image and region size in parameters. In this case you'll
  /// get the empty image buffer of requested size if the cache contains the image of different
  /// size of does not contain an image so far, but the next call to downloadImageBuffer() will
  /// refresh the size of rendered image on the server according to size requested here.
  /// @param [out] iComponentsCnt - Number of components in the returned image buffer.
  /// @param [out] pfBuf - Pointer to cached image buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  bool getImgBufferFloat(int &iComponentsCnt,
                         float *&pfBuf,
                         int iWidth,
                         int iHeight,
                         int iRegionWidth,
                         int iRegionHeight);
  /// Get a copy of the cached image buffer. Use downloadImageBuffer() to download and cache the
  /// image buffer from Octane server. This method is made a way it **always** returns the image
  /// buffer of requested size, even if it has not been downloaded from the server so far (just
  /// empty image in this case). You can change the size of currently rendered image by this
  /// method: requesting the different size in parameters. In this case you'll get the empty
  /// image buffer of requested size if the cache contains the image of different size of does
  /// not contain an image so far, but the next call to downloadImageBuffer() will refresh the
  /// size of rendered image on the server according to size requested here.
  /// @param [in] iComponentsCnt - Number of components expected in the returned image buffer.
  /// @param [out] pfBuf - Pointer to the buffer holding the copy of cached image buffer. It is
  /// caller's responsibility to **delete[]** this buffer.
  /// @param [in,out] iWidth - Requested width of the whole image. If **iWidth <= 0** or
  /// **iHeight
  /// <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current
  /// cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iHeight - Requested heigth of the whole image. If **iWidth <= 0** or
  /// **iHeight <= 0** or **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the
  /// current cache (if any) and its size in **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionWidth - Requested width of the region. Must be equal to iWidth if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth <= 0** or **iRegionHeight <= 0** this method returns the current cache (if
  /// any) and its size in
  /// **iRegionWidth** and **iRegionHeight**.
  /// @param [in,out] iRegionHeight - Requested heigth of the region. Must be equal to iHeight if
  /// you need to render the whole image. If **iWidth <= 0** or **iHeight <= 0** or
  /// **iRegionWidth
  /// <= 0** or **iRegionHeight <= 0** this method returns the current cache (if any) and its
  /// size in **iRegionWidth** and **iRegionHeight**.
  /// @return **true** if image cache contains image of requested size, **false** otherwise
  /// (empty image buffer having requested size is returned in this case).
  bool getCopyImgBufferFloat(int iComponentsCnt,
                             float *&pfBuf,
                             int iWidth,
                             int iHeight,
                             int iRegionWidth,
                             int iRegionHeight);

  /// Downloads and caches the currently rendered image buffer from the server. Gets the
  /// rendering statistics in addition to that.
  /// @param [out] renderStat - RenderStatistics structure.
  /// @param [in] imgType - The type of rendered image.
  /// @param [in] passType - The pass type.
  /// @param [in] bForce - Force to download a buffer even if no buffer refresh has been made on
  /// a server.
  bool downloadImageBuffer(RenderStatistics &renderStat,
                           ImageType const imgType,
                           RenderPassId &passType,
                           bool const bForce = false);

  /// Get a preiview for material or texture by node Id. The node must be already uploaded to the
  /// server.
  /// @param [out] renderStat - RenderStatistics structure.
  /// @param [in] sName - The Id of a node.
  /// @param [in] uiWidth - Preview width in pixels.
  /// @param [in] uiHeight - Preview height in pixels.
  /// @return - A pointer to the downloaded image buffer or NULL if error. The caller is
  /// responsible for freeing a buffer.
  unsigned char *getPreview(std::string sName, uint32_t &uiWidth, uint32_t &uiHeight);

  bool checkImgBuffer8bit(uint8_4 *&puc4Buf,
                          int iWidth,
                          int iHeight,
                          int iRegionWidth,
                          int iRegionHeight,
                          bool bCopyToBuf = false);
  bool checkImgBufferFloat(int iComponentsCnt,
                           float *&pfBuf,
                           int iWidth,
                           int iHeight,
                           int iRegionWidth,
                           int iRegionHeight,
                           bool bCopyToBuf = false);

  bool compileOSL(OctaneDataTransferObject::OctaneNodeBase *pNode,
                  OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo);

  bool commandToOctane(int cmd_type,
                       const std::vector<int> &iParams,
                       const std::vector<float> &fParams,
                       const std::vector<std::string> &sParams);

  int getSocket()
  {
    return m_Socket;
  }

 private:
#ifdef _WIN32
  CRITICAL_SECTION m_SocketMutex;
  CRITICAL_SECTION m_ImgBufMutex;
#else
  pthread_mutex_t m_SocketMutex;
  pthread_mutex_t m_ImgBufMutex;
#endif

  uint8_t *m_pucImageBuf;
  float *m_pfImageBuf;
  int32_t m_iComponentCnt;
  size_t m_stImgBufLen;

  SceneExportTypes::SceneExportTypesEnum m_ExportSceneType;
  bool m_bDeepImage;
  bool m_bExportWithObjectLayers;
  FailReasons::FailReasonsEnum m_FailReason;
  char m_cBlockUpdates;

  int32_t m_iCurImgBufWidth, m_iCurImgBufHeight, m_iCurRegionWidth, m_iCurRegionHeight;
  bool m_bUnpackedTexturesMsgShown;
  string m_sErrorMsg;

  RenderPassId m_CurPassType;
  string m_sAddress;
  string m_sOutPath;
  string m_sCachePath;
  RenderServerInfo m_ServerInfo;
  int m_Socket;

  std::vector<Camera> m_CameraCache;
  std::vector<Kernel> m_KernelCache;
  std::vector<Passes> m_PassesCache;

  bool m_bRenderStarted;
  bool m_bLastUseUniversalCamera;

  bool checkResponsePacket(OctaneDataTransferObject::PacketType packetType,
                           const char *szErrorMsg = 0);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  //
  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  string getFileName(string &sFullPath);
  uint64_t getFileTime(string &sFullPath);
  bool uploadFile(string &sFilePath, string &sFileName);

};  // class OctaneClient

}  // namespace OctaneEngine

#endif /* __OCTANECLIENT_H__ */
