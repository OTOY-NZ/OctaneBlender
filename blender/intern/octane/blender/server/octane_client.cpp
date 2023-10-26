#include "octane_client.h"
#include "octane_network.h"
#include <chrono>

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

OctaneClient::OctaneClient()
    : m_bRenderStarted(false),
      m_bLastUseUniversalCamera(false),
      m_cBlockUpdates(0),
      m_iComponentCnt(0),
      m_iSharedHandler(0),
      m_bServerUseSharedSurface(false),
      m_stImgBufLen(0),
      m_pucImageBuf(0),
      m_pfImageBuf(0),
      m_iCurImgBufWidth(0),
      m_iCurImgBufHeight(0),
      m_iCurRegionWidth(0),
      m_iCurRegionHeight(0),
      m_Socket(-1),
      m_ExportSceneType(SceneExportTypes::NONE),
      m_bDeepImage(false),
      m_bExportWithObjectLayers(true),
      m_FailReason(FailReasons::NONE),
      m_CurPassType(Octane::RenderPassId::PASS_NONE)
{

#ifdef _WIN32
  ::InitializeCriticalSection(&m_SocketMutex);
  ::InitializeCriticalSection(&m_ImgBufMutex);
#else
  pthread_mutex_init(&m_SocketMutex, 0);
  pthread_mutex_init(&m_ImgBufMutex, 0);
#endif
  m_sOutPath = "";
  m_sCachePath = "";
}  // OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// DESTRUCTOR
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::~OctaneClient()
{
  if (m_Socket >= 0)
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
  if (m_pucImageBuf)
    delete[] m_pucImageBuf;
  if (m_pfImageBuf)
    delete[] m_pfImageBuf;

#ifdef _WIN32
  ::DeleteCriticalSection(&m_SocketMutex);
  ::DeleteCriticalSection(&m_ImgBufMutex);
#else
  pthread_mutex_destroy(&m_SocketMutex);
  pthread_mutex_destroy(&m_ImgBufMutex);
#endif
}  //~OctaneClient()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::setOutputPath(const char *szOutPath, const char *szCachePath)
{
  m_sOutPath = szOutPath;
  m_sCachePath = szCachePath;
}  // setOutputPath()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::setExportType(const SceneExportTypes::SceneExportTypesEnum exportSceneType)
{
  m_ExportSceneType = exportSceneType;
}  // setExportType()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::connectToServer(const char *szAddr, int port)
{
  LOCK_MUTEX(m_SocketMutex);

  struct hostent *host;
  struct sockaddr_in sa;

  m_ServerInfo.sNetAddress = szAddr;

  m_sAddress = szAddr;
  host = gethostbyname(szAddr);
  if (!host || host->h_length != sizeof(struct in_addr)) {
    m_FailReason = FailReasons::UNKNOWN;

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }

  memset(&sa, 0, sizeof(sa));
  sa.sin_family = AF_INET;

  if (m_Socket < 0) {
#ifdef __APPLE__
    m_Socket = ::socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
#else
    m_Socket = ::socket(AF_INET, SOCK_STREAM, 0);
#endif
    if (m_Socket < 0) {
      m_FailReason = FailReasons::UNKNOWN;

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
#ifdef __APPLE__
    int value = 1;
    ::setsockopt(m_Socket, SOL_SOCKET, SO_NOSIGPIPE, &value, sizeof(value));
#endif

    sa.sin_family = AF_INET;
    sa.sin_port = htons(0);
    sa.sin_addr.s_addr = htonl(INADDR_ANY);
    if (::bind(m_Socket, (struct sockaddr *)&sa, sizeof(sa)) < 0) {
#ifndef WIN32
      close(m_Socket);
#else
      closesocket(m_Socket);
#endif
      m_FailReason = FailReasons::UNKNOWN;
      m_Socket = -1;

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
  }

  sa.sin_port = htons(port);
  sa.sin_addr = *(struct in_addr *)host->h_addr;
  if (::connect(m_Socket, (struct sockaddr *)&sa, sizeof(sa)) < 0) {
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
    m_FailReason = FailReasons::NO_CONNECTION;
    m_Socket = -1;

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }

  UNLOCK_MUTEX(m_SocketMutex);

  if (port == RENDER_SERVER_PORT && !initOctaneApi())
    return false;

  if (port == RENDER_SERVER_PORT && !checkServerVersion())
    return false;

  LOCK_MUTEX(m_SocketMutex);
  m_FailReason = FailReasons::NONE;

  // m_ServerInfo.sNetAddress  = szAddr;
  m_ServerInfo.sDescription = "";

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // connectToServer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::disconnectFromServer()
{
  LOCK_MUTEX(m_SocketMutex);

  if (m_Socket >= 0) {
#ifndef WIN32
    close(m_Socket);
#else
    closesocket(m_Socket);
#endif
    m_Socket = -1;
  }

  m_ServerInfo.sNetAddress = "";
  m_ServerInfo.sDescription = "";
  m_ServerInfo.gpuNames.clear();

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}

std::string OctaneClient::getServerAdress()
{
  return m_sAddress;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::checkServerConnection()
{
  bool bRet;
  LOCK_MUTEX(m_SocketMutex);

  if (m_Socket < 0)
    bRet = false;
  else {
    int iError = 0;
    socklen_t iLen = sizeof(iError);
    int iRet = ::getsockopt(m_Socket, SOL_SOCKET, SO_ERROR, (char *)(&iError), &iLen);

    if (iRet != 0)
      bRet = false;
    else if (iError != 0) {
      // fprintf(stderr, "socket error: %s\n", strerror(error));
      bRet = false;
    }
    else {
      RPCSend snd(m_Socket, 0, OctaneDataTransferObject::TEST_PACKET);
      if (snd.write())
        bRet = true;
      else
        bRet = false;
    }
  }

  if (!bRet) {
    if (m_Socket >= 0) {
#ifndef WIN32
      close(m_Socket);
#else
      closesocket(m_Socket);
#endif
      m_Socket = -1;
    }

    // m_ServerInfo.sNetAddress  = "";
    m_ServerInfo.sDescription = "";
    m_ServerInfo.gpuNames.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return bRet;
}

bool OctaneClient::testProfileTransferData()
{
  bool bRet = true;
  LOCK_MUTEX(m_SocketMutex);

  if (m_Socket >= 0) {

    uint32_t float_size = 1024 * 1024 * 16;
    float *data = new float[float_size];
    for (uint32_t i = 0; i < float_size; ++i) {
      data[i] = i;
    }
    using milli = std::chrono::milliseconds;
    auto start = std::chrono::high_resolution_clock::now();
    RPCSend snd(m_Socket,
                sizeof(uint32_t) + float_size * sizeof(float),
                OctaneDataTransferObject::PROFILE_DATA_TRANSFER);
    snd << static_cast<uint32_t>(float_size);
    snd.writeBuffer(data, float_size * sizeof(float));
    snd.write();
    auto finish = std::chrono::high_resolution_clock::now();
    long long gap = std::chrono::duration_cast<milli>(finish - start).count();
    delete[] data;
    std::string output = "testProfileTransferData() took " + std::to_string(gap) + " ms\n";
    fprintf(stderr, output.c_str());
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return bRet;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const string &OctaneClient::getServerErrorMessage()
{
  return m_sErrorMsg;
}  // getServerErrorMessage()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::clearServerErrorMessage()
{
  m_sErrorMsg.clear();
}  // clearServerErrorMessage()

bool OctaneClient::initOctaneApi()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::INIT_API);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::INIT_API) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of initialization or activation on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }
}

bool OctaneClient::ReleaseOctaneApi()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::RELEASE_API);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::RELEASE_API) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of releasing on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::checkServerVersion()
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  m_ServerInfo.gpuNames.clear();
  RPCSend snd(m_Socket, sizeof(uint32_t), OctaneDataTransferObject::DESCRIPTION);
  // snd << (G.debug != 0);
  snd << 0;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::DESCRIPTION) {
    m_FailReason = FailReasons::UNKNOWN;

    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR getting render-server description.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    m_FailReason = FailReasons::NONE;

    uint32_t num_gpus;
    bool active;
    std::string server_version_str;
    rcv >> server_version_str >> num_gpus >> active;

    std::string client_version_str = version(OCTANE_SERVER_MAJOR_VERSION,
                                             OCTANE_SERVER_MINOR_VERSION);

    if (server_version_str != client_version_str) {
      m_FailReason = FailReasons::WRONG_VERSION;
      fprintf(stderr,
              "Octane: ERROR: Wrong version of render-server %s, %s is needed\n",
              server_version_str.c_str(),
              client_version_str.c_str());

      if (m_Socket >= 0)
#ifndef WIN32
        close(m_Socket);
#else
        closesocket(m_Socket);
#endif
      m_Socket = -1;
      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }

    if (num_gpus) {
      m_ServerInfo.gpuNames.resize(num_gpus);
      string *str = &m_ServerInfo.gpuNames[0];
      for (uint32_t i = 0; i < num_gpus; ++i)
        rcv >> str[i];
    }
    else {
      m_FailReason = FailReasons::NO_GPUS;
      fprintf(stderr, "Octane: ERROR: no available CUDA GPUs on a server\n");
    }

    if (!active) {
      m_FailReason = FailReasons::NOT_ACTIVATED;
      fprintf(stderr, "Octane: ERROR: server is not activated\n");
    }

    UNLOCK_MUTEX(m_SocketMutex);
    return m_FailReason == FailReasons::NONE;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // checkServerVersion()

bool OctaneClient::downloadOctaneDB(OctaneDataTransferObject::OctaneDBNodes &nodes)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return false;
  LOCK_MUTEX(m_SocketMutex);

  OctaneDataTransferObject::OctaneDBNodes *pOctaneDBNodes =
      (OctaneDataTransferObject::OctaneDBNodes *)RPCMsgPackObj::receiveOctaneNode(m_Socket);
  nodes.sName = pOctaneDBNodes->sName;
  nodes.bClose = pOctaneDBNodes->bClose;
  nodes.iOctaneDBType = pOctaneDBNodes->iOctaneDBType;
  nodes.iNodesNum = pOctaneDBNodes->iNodesNum;
  for (int i = 0; i < pOctaneDBNodes->iNodesNum; ++i) {
    OctaneDataTransferObject::OctaneNodeBase *pResponseNode = RPCMsgPackObj::receiveOctaneNode(
        m_Socket);
    if (pResponseNode) {
      nodes.octaneDBNodes.emplace_back(pResponseNode);
    }
  }
  delete pOctaneDBNodes;
  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // downloadOctaneDB

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::activate(string const &sStandLogin,
                            string const &sStandPass,
                            string const &sLogin,
                            string const &sPass)
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket,
              sStandLogin.length() + 2 + sStandPass.length() + 2 + sLogin.length() + 2 +
                  sPass.length() + 2,
              OctaneDataTransferObject::SET_LIC_DATA);
  snd << sStandLogin << sStandPass << sLogin << sPass;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::SET_LIC_DATA) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR of the license activation on render-server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");

    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // activate()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::reset(bool bInteractive,
                         SceneExportTypes::SceneExportTypesEnum exportSceneType,
                         float fFrameTimeSampling,
                         float fFps,
                         bool bDeepImage,
                         bool bExportWithObjectLayers)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  m_bUnpackedTexturesMsgShown = false;

  LOCK_MUTEX(m_SocketMutex);

  m_ExportSceneType = exportSceneType;
  m_bDeepImage = bDeepImage;
  m_bExportWithObjectLayers = exportSceneType == SceneExportTypes::SceneExportTypesEnum::NONE ||
                              bExportWithObjectLayers;

  RPCSend snd(m_Socket,
              sizeof(float) * 2 + sizeof(uint32_t) * 4 + (m_sOutPath.size() + 2) +
                  (m_sCachePath.size() + 2),
              OctaneDataTransferObject::RESET);
  snd << bInteractive << fFrameTimeSampling << fFps << m_ExportSceneType << bDeepImage
      << m_bExportWithObjectLayers << m_sOutPath.c_str() << m_sCachePath.c_str();

  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::RESET) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR resetting render server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_CameraCache.clear();
    m_KernelCache.clear();
    m_PassesCache.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // reset()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::clear()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  m_bUnpackedTexturesMsgShown = false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::CLEAR);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::CLEAR) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR clearing render server.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_CameraCache.clear();
    m_KernelCache.clear();
    m_PassesCache.clear();
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // clear()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::update()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::UPDATE);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::UPDATE) {
    UNLOCK_MUTEX(m_SocketMutex);
    return false;
  }
  else {
    UNLOCK_MUTEX(m_SocketMutex);
    return true;
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return false;
}  // update()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::startRender(bool bInteractive,
                               bool bUseSharedSurface,
                               uint64_t iClientProcessId,
                               uint64_t iDeviceLuid,
                               int32_t iWidth,
                               int32_t iHeigth,
                               ImageType imgType,
                               bool bOutOfCoreEnabled,
                               int32_t iOutOfCoreMemLimit,
                               int32_t iOutOfCoreGPUHeadroom,
                               int32_t iRenderPriority,
                               int32_t iResourceCacheType)
{
  if (m_bRenderStarted)
    m_bRenderStarted = false;

  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket,
              sizeof(int32_t) * 8 + sizeof(uint32_t) * 2 + sizeof(uint64_t) * 2 +
                  (m_sOutPath.size() + 2) + m_sCachePath.size() + 2,
              OctaneDataTransferObject::START);
  snd << bInteractive << bUseSharedSurface << iClientProcessId << iDeviceLuid << bOutOfCoreEnabled
      << iOutOfCoreMemLimit << iOutOfCoreGPUHeadroom << iRenderPriority << iResourceCacheType
      << iWidth << iHeigth << imgType << m_sOutPath.c_str() << m_sCachePath.c_str();
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::START) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR starting render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else
    m_bRenderStarted = true;

  UNLOCK_MUTEX(m_SocketMutex);
}  // startRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef _WIN32
#  pragma warning(push)
#  pragma warning(disable : 4706)
#endif
void OctaneClient::stopRender(float fFPS)
{
  if (m_Socket < 0)
    return;
  if (m_cBlockUpdates)
    m_cBlockUpdates = 0;

  LOCK_MUTEX(m_SocketMutex);

  bool is_alembic = (m_ExportSceneType == SceneExportTypes::ALEMBIC ? true : false);
  RPCSend snd(m_Socket,
              m_ExportSceneType != SceneExportTypes::NONE ? sizeof(float) + sizeof(uint32_t) : 0,
              OctaneDataTransferObject::STOP);
  if (m_ExportSceneType != SceneExportTypes::NONE)
    snd << fFPS << is_alembic;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::STOP) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR stopping render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else if (m_ExportSceneType != SceneExportTypes::NONE && m_sOutPath.length()) {
    int err;
    RPCReceive rcv(m_Socket);
    string s_out_path(m_sOutPath);
    if (m_ExportSceneType == SceneExportTypes::ALEMBIC)
      s_out_path += ".abc";
    else
      s_out_path += ".orbx";

    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_FILE) {
      rcv >> m_sErrorMsg;
    }
    else if (!rcv.readFile(s_out_path, &err)) {
      char *err_str;
    }
#ifdef _WIN32
#  pragma warning(pop)
#endif
  }
  else if (m_bDeepImage && m_sOutPath.length()) {
    int err;
    RPCReceive rcv(m_Socket);
    string s_out_path(m_sOutPath);
    s_out_path += "_deep.exr";

    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_FILE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else if (!rcv.readFile(s_out_path, &err)) {
      char *err_str;
      fprintf(stderr, "Octane: ERROR downloading deep image file from server.");
      if (err && (err_str = strerror(err)) && err_str[0])
        fprintf(stderr, " Description: %s\n", err_str);
      else
        fprintf(stderr, "\n");
    }
  }

  m_CameraCache.clear();
  m_KernelCache.clear();
  m_PassesCache.clear();

  UNLOCK_MUTEX(m_SocketMutex);

  m_bRenderStarted = false;
  m_bLastUseUniversalCamera = false;
}  // stopRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::isRenderStarted()
{
  return m_bRenderStarted;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::pauseRender(int32_t bPause)
{
  if (m_Socket < 0)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, sizeof(int32_t), OctaneDataTransferObject::PAUSE);
  snd << bPause;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::PAUSE) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR pause render.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // pauseRender()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::startFrameUpload()
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, 0, OctaneDataTransferObject::START_FRAME_LOAD);
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::START_FRAME_LOAD) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR starting frame load.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // startFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::finishFrameUpload(bool bUpdate)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  RPCSend snd(m_Socket, sizeof(int32_t), OctaneDataTransferObject::FINISH_FRAME_LOAD);
  snd << bUpdate;
  snd.write();

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::FINISH_FRAME_LOAD) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR finishing frame load.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // finishFrameUpload()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadCamera(Camera *pCamera, uint32_t uiFrameIdx, uint32_t uiTotalFrames)
{
  if (m_Socket < 0 || m_cBlockUpdates || !pCamera)
    return;

  size_t stCacheSize = m_CameraCache.size();
  if (uiTotalFrames && stCacheSize != uiTotalFrames) {
    std::vector<Camera>().swap(m_CameraCache);
    m_CameraCache.resize(uiTotalFrames);
  }
  else if (stCacheSize > uiFrameIdx && *pCamera == m_CameraCache[uiFrameIdx])
    return;

  LOCK_MUTEX(m_SocketMutex);
  pCamera->universalCamera.sName = "UniversalCamera";
  bool isUniversalCameraUpdated = checkUniversalCameraUpdated(pCamera->bUseUniversalCamera,
                                                              pCamera->universalCamera);
  if (pCamera->bUseUniversalCamera) {
    if (isUniversalCameraUpdated) {
      RPCMsgPackObj::sendOctaneNode(
          m_Socket, pCamera->universalCamera.sName, &pCamera->universalCamera);
      if (checkResponsePacket(OctaneDataTransferObject::LOAD_OCTANE_NODE)) {
        m_CameraCache[uiFrameIdx] = *pCamera;
      }
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }

    // temp fix
    // use lens camera upload here to upload imager and postprocess data
    {
      uint32_t motoin_data_num = pCamera->oMotionParams.motions.size();
      std::vector<float_3> motion_eye_point_data;
      std::vector<float_3> motion_look_at_data;
      std::vector<float_3> motion_up_vector_data;
      std::vector<float> motion_fov_data;
      for (auto it : pCamera->oMotionParams.motions) {
        motion_eye_point_data.push_back(it.second.f3EyePoint);
        motion_look_at_data.push_back(it.second.f3LookAt);
        motion_up_vector_data.push_back(it.second.f3UpVector);
        motion_fov_data.push_back(it.second.fFOV);
      }

      RPCSend snd(m_Socket,
                  (sizeof(uint32_t) + (sizeof(float_3) * 3 + sizeof(float)) * motoin_data_num) +
                      sizeof(float_3) * 7 + sizeof(float) * 41 + sizeof(int32_t) * 33 +
                      sizeof(uint32_t) * 6 + (pCamera->sCustomLut.length() + 2) +
                      (pCamera->sOcioViewDisplay.length() + 2) +
                      (pCamera->sOcioViewDisplayView.length() + 2) +
                      (pCamera->sOcioLook.length() + 2),
                  OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA);

      snd << pCamera->bUseUniversalCamera;
      snd << motoin_data_num;
      snd.writeBuffer(&motion_eye_point_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_look_at_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_up_vector_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_fov_data[0], sizeof(float) * motoin_data_num);

      snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector
          << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance

          << pCamera->fAperture << pCamera->fApertureEdge << pCamera->fDistortion
          << pCamera->fFocalDepth << pCamera->fNearClipDepth << pCamera->fFarClipDepth
          << pCamera->f2LensShift.x << pCamera->f2LensShift.y << pCamera->fStereoDist
          << pCamera->fFOV << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting
          << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
          << pCamera->fBloomPower << pCamera->fCutoff << pCamera->fGlarePower
          << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift
          << pCamera->fSpectralIntencity << pCamera->fSpreadStart << pCamera->fSpreadEnd
          << pCamera->fChromaticAberrationIntensity << pCamera->fLensFlare
          << pCamera->fLensFlareExtent << pCamera->bLightBeams << pCamera->bScaleWithFilm
          << pCamera->fMediumDensityForPostfxLightBeams << pCamera->bEnableFog
          << pCamera->fFogExtinctionDistance << pCamera->fFogBaseLevel
          << pCamera->fFogHalfDensityHeight << pCamera->fFogEnvContribution
          << pCamera->f3BaseFogColor << pCamera->fMediumRadius << pCamera->fHighlightCompression
          << pCamera->fPixelAspect << pCamera->fApertureAspect << pCamera->fBokehRotation
          << pCamera->fBokehRoundness << pCamera->fLutStrength << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->iResponseCurve << pCamera->iMinDisplaySamples
          << pCamera->iGlareRayCount << pCamera->stereoMode << pCamera->stereoOutput
          << pCamera->iMaxTonemapInterval << uiFrameIdx << uiTotalFrames
          << pCamera->iBokehSidecount

          << pCamera->bEnableImager << pCamera->bOrtho << pCamera->bAutofocus
          << pCamera->bPremultipliedAlpha << pCamera->bACESToneMapping << pCamera->bDithering
          << pCamera->bUsePostprocess << pCamera->bPerspCorr << pCamera->bNeutralResponse
          << pCamera->bUseFstopValue << pCamera->bDisablePartialAlpha << pCamera->bSwapEyes
          << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode << pCamera->sCustomLut.c_str()
          << pCamera->sOcioViewDisplay.c_str() << pCamera->sOcioViewDisplayView.c_str()
          << pCamera->sOcioLook.c_str() << pCamera->bForceToneMapping;
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }
  else if (pCamera->type == Camera::CAMERA_PANORAMA) {
    {
      RPCSend snd(
          m_Socket,
          sizeof(float_3) * 7 + sizeof(float) * 38 + sizeof(int32_t) * 34 +
              (pCamera->sCustomLut.length() + 2) + (pCamera->sOcioViewDisplay.length() + 2) +
              (pCamera->sOcioViewDisplayView.length() + 2) + (pCamera->sOcioLook.length() + 2),
          OctaneDataTransferObject::LOAD_PANORAMIC_CAMERA);
      snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector
          << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance

          << pCamera->fFOVx << pCamera->fFOVy << pCamera->fNearClipDepth << pCamera->fFarClipDepth
          << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting << pCamera->fSaturation
          << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation << pCamera->fBloomPower
          << pCamera->fCutoff << pCamera->fGlarePower << pCamera->fGlareAngle
          << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity

          << pCamera->fSpreadStart << pCamera->fSpreadEnd << pCamera->fChromaticAberrationIntensity
          << pCamera->fLensFlare << pCamera->fLensFlareExtent << pCamera->bLightBeams
          << pCamera->bScaleWithFilm << pCamera->fMediumDensityForPostfxLightBeams
          << pCamera->bEnableFog << pCamera->fFogExtinctionDistance << pCamera->fFogBaseLevel
          << pCamera->fFogHalfDensityHeight << pCamera->fFogEnvContribution
          << pCamera->f3BaseFogColor << pCamera->fMediumRadius

          << pCamera->fHighlightCompression << pCamera->fBlackoutLat << pCamera->fStereoDist
          << pCamera->fStereoDistFalloff << pCamera->fAperture << pCamera->fApertureEdge
          << pCamera->fApertureAspect << pCamera->fFocalDepth << pCamera->fBokehRotation
          << pCamera->fBokehRoundness << pCamera->fLutStrength << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->panCamMode << pCamera->iResponseCurve
          << pCamera->iMinDisplaySamples << pCamera->iGlareRayCount << pCamera->stereoOutput
          << pCamera->iMaxTonemapInterval << pCamera->iBokehSidecount

          << pCamera->bEnableImager << pCamera->bPremultipliedAlpha << pCamera->bACESToneMapping
          << pCamera->bDithering << pCamera->bUsePostprocess << pCamera->bKeepUpright
          << pCamera->bNeutralResponse << pCamera->bDisablePartialAlpha << pCamera->bUseFstopValue
          << pCamera->bAutofocus << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode
          << pCamera->sCustomLut.c_str() << pCamera->sOcioViewDisplay.c_str()
          << pCamera->sOcioViewDisplayView.c_str() << pCamera->sOcioLook.c_str()
          << pCamera->bForceToneMapping;
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_PANORAMIC_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }
  else if (pCamera->type == Camera::CAMERA_BAKING) {
    {
      RPCSend snd(
          m_Socket,
          sizeof(float_3) * 6 + sizeof(float_2) * 2 + sizeof(float) * 27 + sizeof(int32_t) * 34 +
              (pCamera->sCustomLut.length() + 2) + (pCamera->sOcioViewDisplay.length() + 2) +
              (pCamera->sOcioViewDisplayView.length() + 2) + (pCamera->sOcioLook.length() + 2),
          OctaneDataTransferObject::LOAD_BAKING_CAMERA);
      snd << pCamera->f3EyePoint << pCamera->f3WhiteBalance
          << pCamera->f3UVWBakingTransformTranslation << pCamera->f3UVWBakingTransformRotation
          << pCamera->f3UVWBakingTransformScale << pCamera->f2UVboxMin << pCamera->f2UVboxSize

          << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting << pCamera->fSaturation
          << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation << pCamera->fBloomPower
          << pCamera->fCutoff << pCamera->fGlarePower << pCamera->fGlareAngle
          << pCamera->fGlareBlur << pCamera->fSpectralShift << pCamera->fSpectralIntencity

          << pCamera->fSpreadStart << pCamera->fSpreadEnd << pCamera->fChromaticAberrationIntensity
          << pCamera->fLensFlare << pCamera->fLensFlareExtent << pCamera->bLightBeams
          << pCamera->bScaleWithFilm << pCamera->fMediumDensityForPostfxLightBeams
          << pCamera->bEnableFog << pCamera->fFogExtinctionDistance << pCamera->fFogBaseLevel
          << pCamera->fFogHalfDensityHeight << pCamera->fFogEnvContribution
          << pCamera->f3BaseFogColor << pCamera->fMediumRadius

          << pCamera->fHighlightCompression << pCamera->fTolerance << pCamera->fLutStrength
          << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->iResponseCurve << pCamera->iMinDisplaySamples
          << pCamera->iGlareRayCount << pCamera->iMaxTonemapInterval << pCamera->iBakingGroupId
          << pCamera->iPadding << pCamera->iUvSet << pCamera->iUVWBakingTransformRotationOrder

          << pCamera->bEnableImager << pCamera->bPremultipliedAlpha << pCamera->bACESToneMapping
          << pCamera->bDithering << pCamera->bUsePostprocess << pCamera->bNeutralResponse
          << pCamera->bBakeOutwards << pCamera->bUseBakingPosition << pCamera->bBackfaceCulling
          << pCamera->bDisablePartialAlpha << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode
          << pCamera->sCustomLut.c_str() << pCamera->sOcioViewDisplay.c_str()
          << pCamera->sOcioViewDisplayView.c_str() << pCamera->sOcioLook.c_str()
          << pCamera->bForceToneMapping;
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_BAKING_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }
  else {
    {
      uint32_t motoin_data_num = pCamera->oMotionParams.motions.size();
      std::vector<float_3> motion_eye_point_data;
      std::vector<float_3> motion_look_at_data;
      std::vector<float_3> motion_up_vector_data;
      std::vector<float> motion_fov_data;
      for (auto it : pCamera->oMotionParams.motions) {
        motion_eye_point_data.push_back(it.second.f3EyePoint);
        motion_look_at_data.push_back(it.second.f3LookAt);
        motion_up_vector_data.push_back(it.second.f3UpVector);
        motion_fov_data.push_back(it.second.fFOV);
      }

      RPCSend snd(m_Socket,
                  (sizeof(uint32_t) + (sizeof(float_3) * 4 + sizeof(float)) * motoin_data_num) +
                      sizeof(float_3) * 6 + sizeof(float) * 41 + sizeof(int32_t) * 33 +
                      sizeof(uint32_t) * 6 + (pCamera->sCustomLut.length() + 2) +
                      (pCamera->sOcioViewDisplay.length() + 2) +
                      (pCamera->sOcioViewDisplayView.length() + 2) +
                      (pCamera->sOcioLook.length() + 2),
                  OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA);

      snd << pCamera->bUseUniversalCamera;
      snd << motoin_data_num;
      snd.writeBuffer(&motion_eye_point_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_look_at_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_up_vector_data[0], sizeof(float) * 3 * motoin_data_num);
      snd.writeBuffer(&motion_fov_data[0], sizeof(float) * motoin_data_num);

      snd << pCamera->f3EyePoint << pCamera->f3LookAt << pCamera->f3UpVector
          << pCamera->f3LeftFilter << pCamera->f3RightFilter << pCamera->f3WhiteBalance

          << pCamera->fAperture << pCamera->fApertureEdge << pCamera->fDistortion
          << pCamera->fFocalDepth << pCamera->fNearClipDepth << pCamera->fFarClipDepth
          << pCamera->f2LensShift.x << pCamera->f2LensShift.y << pCamera->fStereoDist
          << pCamera->fFOV << pCamera->fExposure << pCamera->fGamma << pCamera->fVignetting
          << pCamera->fSaturation << pCamera->fHotPixelFilter << pCamera->fWhiteSaturation
          << pCamera->fBloomPower << pCamera->fCutoff << pCamera->fGlarePower
          << pCamera->fGlareAngle << pCamera->fGlareBlur << pCamera->fSpectralShift
          << pCamera->fSpectralIntencity

          << pCamera->fSpreadStart << pCamera->fSpreadEnd << pCamera->fChromaticAberrationIntensity
          << pCamera->fLensFlare << pCamera->fLensFlareExtent << pCamera->bLightBeams
          << pCamera->bScaleWithFilm << pCamera->fMediumDensityForPostfxLightBeams
          << pCamera->bEnableFog << pCamera->fFogExtinctionDistance << pCamera->fFogBaseLevel
          << pCamera->fFogHalfDensityHeight << pCamera->fFogEnvContribution
          << pCamera->f3BaseFogColor << pCamera->fMediumRadius

          << pCamera->fHighlightCompression << pCamera->fPixelAspect << pCamera->fApertureAspect
          << pCamera->fBokehRotation << pCamera->fBokehRoundness << pCamera->fLutStrength
          << pCamera->fDenoiserBlend

          << pCamera->bEnableDenoiser << pCamera->bDenoiseVolumes << pCamera->bDenoiseOnCompletion
          << pCamera->iMinDenoiserSample << pCamera->iMaxDenoiserInterval

          << pCamera->iSamplingMode << pCamera->bEnableAIUpSampling
          << pCamera->bUpSamplingOnCompletion << pCamera->iMinUpSamplerSamples
          << pCamera->iMaxUpSamplerInterval

          << pCamera->iCameraImagerOrder << pCamera->iResponseCurve << pCamera->iMinDisplaySamples
          << pCamera->iGlareRayCount << pCamera->stereoMode << pCamera->stereoOutput
          << pCamera->iMaxTonemapInterval << uiFrameIdx << uiTotalFrames
          << pCamera->iBokehSidecount

          << pCamera->bEnableImager << pCamera->bOrtho << pCamera->bAutofocus
          << pCamera->bPremultipliedAlpha << pCamera->bACESToneMapping << pCamera->bDithering
          << pCamera->bUsePostprocess << pCamera->bPerspCorr << pCamera->bNeutralResponse
          << pCamera->bUseFstopValue << pCamera->bDisablePartialAlpha << pCamera->bSwapEyes
          << pCamera->bUseOSLCamera << pCamera->bPreviewCameraMode << pCamera->sCustomLut.c_str()
          << pCamera->sOcioViewDisplay.c_str() << pCamera->sOcioViewDisplayView.c_str()
          << pCamera->sOcioLook.c_str() << pCamera->bForceToneMapping;
      snd.write();
    }

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_THIN_LENS_CAMERA) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading camera.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
    else {
      m_CameraCache[uiFrameIdx] = *pCamera;
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadCamera()

bool OctaneClient::checkUniversalCameraUpdated(
    bool useUniversalCamera, OctaneDataTransferObject::OctaneUniversalCamera &current)
{
  static OctaneDataTransferObject::OctaneUniversalCamera lastUniversalCamera;
  bool isUpdated = !(
      m_bLastUseUniversalCamera == useUniversalCamera &&
      lastUniversalCamera.iCameraMode.iVal == current.iCameraMode.iVal &&
      lastUniversalCamera.fSensorWidth.fVal == current.fSensorWidth.fVal &&
      lastUniversalCamera.fFocalLength.fVal == current.fFocalLength.fVal &&
      lastUniversalCamera.fFstop.fVal == current.fFstop.fVal &&
      lastUniversalCamera.fFieldOfView.fVal == current.fFieldOfView.fVal &&
      lastUniversalCamera.fScaleOfView.fVal == current.fScaleOfView.fVal &&
      lastUniversalCamera.f2LensShift.fVal == current.f2LensShift.fVal &&
      lastUniversalCamera.fPixelAspectRatio.fVal == current.fPixelAspectRatio.fVal &&
      lastUniversalCamera.bPerspectiveCorrection.bVal == current.bPerspectiveCorrection.bVal &&
      lastUniversalCamera.fFisheyeAngle.fVal == current.fFisheyeAngle.fVal &&
      lastUniversalCamera.iFisheyeType.iVal == current.iFisheyeType.iVal &&
      lastUniversalCamera.bHardVignette.bVal == current.bHardVignette.bVal &&
      lastUniversalCamera.iFisheyeProjection.iVal == current.iFisheyeProjection.iVal &&
      lastUniversalCamera.fHorizontalFiledOfView.fVal == current.fHorizontalFiledOfView.fVal &&
      lastUniversalCamera.fVerticalFiledOfView.fVal == current.fVerticalFiledOfView.fVal &&
      lastUniversalCamera.iCubemapLayout.iVal == current.iCubemapLayout.iVal &&
      lastUniversalCamera.bEquiAngularCubemap.bVal == current.bEquiAngularCubemap.bVal &&
      lastUniversalCamera.bUseDistortionTexture.bVal == current.bUseDistortionTexture.bVal &&
      lastUniversalCamera.sDistortionTexture.sLinkNodeName ==
          current.sDistortionTexture.sLinkNodeName &&
      lastUniversalCamera.fSphereDistortion.fVal == current.fSphereDistortion.fVal &&
      lastUniversalCamera.fBarrelDistortion.fVal == current.fBarrelDistortion.fVal &&
      lastUniversalCamera.fBarrelDistortionCorners.fVal == current.fBarrelDistortionCorners.fVal &&
      lastUniversalCamera.fSphereAberration.fVal == current.fSphereAberration.fVal &&
      lastUniversalCamera.fComa.fVal == current.fComa.fVal &&
      lastUniversalCamera.fAstigmatism.fVal == current.fAstigmatism.fVal &&
      lastUniversalCamera.fFieldCurvature.fVal == current.fFieldCurvature.fVal &&
      lastUniversalCamera.fNearClipDepth.fVal == current.fNearClipDepth.fVal &&
      lastUniversalCamera.fFarClipDepth.fVal == current.fFarClipDepth.fVal &&
      lastUniversalCamera.bAutoFocus.bVal == current.bAutoFocus.bVal &&
      lastUniversalCamera.fFocalDepth.fVal == current.fFocalDepth.fVal &&
      lastUniversalCamera.fAperture.fVal == current.fAperture.fVal &&
      lastUniversalCamera.fApertureAspectRatio.fVal == current.fApertureAspectRatio.fVal &&
      lastUniversalCamera.iApertureShape.iVal == current.iApertureShape.iVal &&
      lastUniversalCamera.fApertureEdge.fVal == current.fApertureEdge.fVal &&
      lastUniversalCamera.iApertureBladeCount.iVal == current.iApertureBladeCount.iVal &&
      lastUniversalCamera.fApertureRotation.fVal == current.fApertureRotation.fVal &&
      lastUniversalCamera.fApertureRoundedness.fVal == current.fApertureRoundedness.fVal &&
      lastUniversalCamera.fCentralObstruction.fVal == current.fCentralObstruction.fVal &&
      lastUniversalCamera.fNorchPosition.fVal == current.fNorchPosition.fVal &&
      lastUniversalCamera.fNorchScale.fVal == current.fNorchScale.fVal &&
      lastUniversalCamera.sCustomAperture.sLinkNodeName == current.sCustomAperture.sLinkNodeName &&
      lastUniversalCamera.fOpticalVignetteDistance.fVal == current.fOpticalVignetteDistance.fVal &&
      lastUniversalCamera.fOpticalVignetteScale.fVal == current.fOpticalVignetteScale.fVal &&
      lastUniversalCamera.bEnableSplitFocusDiopter.bVal == current.bEnableSplitFocusDiopter.bVal &&
      lastUniversalCamera.fDiopterFocalDepth.fVal == current.fDiopterFocalDepth.fVal &&
      lastUniversalCamera.fDiopterRotation.fVal == current.fDiopterRotation.fVal &&
      lastUniversalCamera.f2DiopterTranslation.fVal == current.f2DiopterTranslation.fVal &&
      lastUniversalCamera.fDiopterBoundaryWidth.fVal == current.fDiopterBoundaryWidth.fVal &&
      lastUniversalCamera.fDiopterBoundaryFalloff.fVal == current.fDiopterBoundaryFalloff.fVal &&
      lastUniversalCamera.bShowDiopterGuide.bVal == current.bShowDiopterGuide.bVal &&
      lastUniversalCamera.f3Position.fVal == current.f3Position.fVal &&
      lastUniversalCamera.f3Target.fVal == current.f3Target.fVal &&
      lastUniversalCamera.f3Up.fVal == current.f3Up.fVal &&
      lastUniversalCamera.bKeepUpright.bVal == current.bKeepUpright.bVal &&
      lastUniversalCamera.oPositoin.oMotionPositions == current.oPositoin.oMotionPositions &&
      lastUniversalCamera.oPositoin.oMotionTargets == current.oPositoin.oMotionTargets &&
      lastUniversalCamera.oPositoin.oMotionUps == current.oPositoin.oMotionUps &&
      lastUniversalCamera.oPositoin.oMotionFOVs == current.oPositoin.oMotionFOVs);
  m_bLastUseUniversalCamera = useUniversalCamera;
  lastUniversalCamera.iCameraMode.iVal = current.iCameraMode.iVal;
  lastUniversalCamera.fSensorWidth.fVal = current.fSensorWidth.fVal;
  lastUniversalCamera.fFocalLength.fVal = current.fFocalLength.fVal;
  lastUniversalCamera.fFstop.fVal = current.fFstop.fVal;
  lastUniversalCamera.fFieldOfView.fVal = current.fFieldOfView.fVal;
  lastUniversalCamera.fScaleOfView.fVal = current.fScaleOfView.fVal;
  lastUniversalCamera.f2LensShift.fVal = current.f2LensShift.fVal;
  lastUniversalCamera.fPixelAspectRatio.fVal = current.fPixelAspectRatio.fVal;
  lastUniversalCamera.bPerspectiveCorrection.bVal = current.bPerspectiveCorrection.bVal;
  lastUniversalCamera.fFisheyeAngle.fVal = current.fFisheyeAngle.fVal;
  lastUniversalCamera.iFisheyeType.iVal = current.iFisheyeType.iVal;
  lastUniversalCamera.bHardVignette.bVal = current.bHardVignette.bVal;
  lastUniversalCamera.iFisheyeProjection.iVal = current.iFisheyeProjection.iVal;
  lastUniversalCamera.fHorizontalFiledOfView.fVal = current.fHorizontalFiledOfView.fVal;
  lastUniversalCamera.fVerticalFiledOfView.fVal = current.fVerticalFiledOfView.fVal;
  lastUniversalCamera.iCubemapLayout.iVal = current.iCubemapLayout.iVal;
  lastUniversalCamera.bEquiAngularCubemap.bVal = current.bEquiAngularCubemap.bVal;
  lastUniversalCamera.bUseDistortionTexture.bVal = current.bUseDistortionTexture.bVal;
  lastUniversalCamera.sDistortionTexture.sLinkNodeName = current.sDistortionTexture.sLinkNodeName;
  lastUniversalCamera.fSphereDistortion.fVal = current.fSphereDistortion.fVal;
  lastUniversalCamera.fBarrelDistortion.fVal = current.fBarrelDistortion.fVal;
  lastUniversalCamera.fBarrelDistortionCorners.fVal = current.fBarrelDistortionCorners.fVal;
  lastUniversalCamera.fSphereAberration.fVal = current.fSphereAberration.fVal;
  lastUniversalCamera.fComa.fVal = current.fComa.fVal;
  lastUniversalCamera.fAstigmatism.fVal = current.fAstigmatism.fVal;
  lastUniversalCamera.fFieldCurvature.fVal = current.fFieldCurvature.fVal;
  lastUniversalCamera.fNearClipDepth.fVal = current.fNearClipDepth.fVal;
  lastUniversalCamera.fFarClipDepth.fVal = current.fFarClipDepth.fVal;
  lastUniversalCamera.bAutoFocus.bVal = current.bAutoFocus.bVal;
  lastUniversalCamera.fFocalDepth.fVal = current.fFocalDepth.fVal;
  lastUniversalCamera.fAperture.fVal = current.fAperture.fVal;
  lastUniversalCamera.fApertureAspectRatio.fVal = current.fApertureAspectRatio.fVal;
  lastUniversalCamera.iApertureShape.iVal = current.iApertureShape.iVal;
  lastUniversalCamera.fApertureEdge.fVal = current.fApertureEdge.fVal;
  lastUniversalCamera.iApertureBladeCount.iVal = current.iApertureBladeCount.iVal;
  lastUniversalCamera.fApertureRotation.fVal = current.fApertureRotation.fVal;
  lastUniversalCamera.fApertureRoundedness.fVal = current.fApertureRoundedness.fVal;
  lastUniversalCamera.fCentralObstruction.fVal = current.fCentralObstruction.fVal;
  lastUniversalCamera.fNorchPosition.fVal = current.fNorchPosition.fVal;
  lastUniversalCamera.fNorchScale.fVal = current.fNorchScale.fVal;
  lastUniversalCamera.sCustomAperture.sLinkNodeName = current.sCustomAperture.sLinkNodeName;
  lastUniversalCamera.fOpticalVignetteDistance.fVal = current.fOpticalVignetteDistance.fVal;
  lastUniversalCamera.fOpticalVignetteScale.fVal = current.fOpticalVignetteScale.fVal;
  lastUniversalCamera.bEnableSplitFocusDiopter.bVal = current.bEnableSplitFocusDiopter.bVal;
  lastUniversalCamera.fDiopterFocalDepth.fVal = current.fDiopterFocalDepth.fVal;
  lastUniversalCamera.fDiopterRotation.fVal = current.fDiopterRotation.fVal;
  lastUniversalCamera.f2DiopterTranslation.fVal = current.f2DiopterTranslation.fVal;
  lastUniversalCamera.fDiopterBoundaryWidth.fVal = current.fDiopterBoundaryWidth.fVal;
  lastUniversalCamera.fDiopterBoundaryFalloff.fVal = current.fDiopterBoundaryFalloff.fVal;
  lastUniversalCamera.bShowDiopterGuide.bVal = current.bShowDiopterGuide.bVal;
  lastUniversalCamera.f3Position.fVal = current.f3Position.fVal;
  lastUniversalCamera.f3Target.fVal = current.f3Target.fVal;
  lastUniversalCamera.f3Up.fVal = current.f3Up.fVal;
  lastUniversalCamera.bKeepUpright.bVal = current.bKeepUpright.bVal;
  lastUniversalCamera.oPositoin.oMotionPositions = current.oPositoin.oMotionPositions;
  lastUniversalCamera.oPositoin.oMotionTargets = current.oPositoin.oMotionTargets;
  lastUniversalCamera.oPositoin.oMotionUps = current.oPositoin.oMotionUps;
  lastUniversalCamera.oPositoin.oMotionFOVs = current.oPositoin.oMotionFOVs;

  return isUpdated;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadKernel(Kernel *pKernel)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  uint32_t uiTotalFrames = 1, uiFrameIdx = 0;  // Temp

  size_t stCacheSize = m_KernelCache.size();
  if (uiTotalFrames && stCacheSize != uiTotalFrames) {
    std::vector<Kernel>().swap(m_KernelCache);
    m_KernelCache.resize(uiTotalFrames);
  }
  else if (stCacheSize > uiFrameIdx && *pKernel == m_KernelCache[uiFrameIdx])
    return;

  LOCK_MUTEX(m_SocketMutex);

  if (false && pKernel->bUseNodeTree) {
    RPCSend snd(m_Socket, sizeof(int32_t) * 2, OctaneDataTransferObject::LOAD_KERNEL);
    snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior;
    snd.write();
  }
  else {
    switch (pKernel->type) {
      case Kernel::DIRECT_LIGHT: {
        RPCSend snd(m_Socket,
                    sizeof(float) * 14 + sizeof(int32_t) * 39 + pKernel->sAoTexture.length() +
                        sizeof(float_3) + 2,
                    OctaneDataTransferObject::LOAD_KERNEL);
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << pKernel->type
            << pKernel->iMaxSamples << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->fFilterSize
            << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fCoherentRatio
            << pKernel->fAODist << pKernel->fDepthTolerance << pKernel->fAdaptiveNoiseThreshold
            << pKernel->fAdaptiveExpectedExposure << pKernel->fAILightStrength
            << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bStaticNoise
            << pKernel->bKeepEnvironment << pKernel->bIrradianceMode << pKernel->bNestDielectrics
            << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
            << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
            << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
            << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
            << pKernel->bDeepRenderPasses << pKernel->bAdaptiveSampling << pKernel->iSpecularDepth
            << pKernel->iGlossyDepth << pKernel->GIMode << pKernel->iDiffuseDepth
            << pKernel->iParallelSamples << pKernel->iMaxTileSamples << pKernel->iMaxDepthSamples
            << pKernel->iAdaptiveMinSamples << pKernel->adaptiveGroupPixels << pKernel->mbAlignment
            << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert
            << pKernel->layersMode << pKernel->iClayMode << pKernel->iSubsampleMode
            << pKernel->iMaxSubdivisionLevel << pKernel->iWhiteLightSpectrum
            << pKernel->bUseOldPipeline << pKernel->f3ToonShadowAmbient << pKernel->sAoTexture;
        snd.write();
      } break;
      case Kernel::PATH_TRACE: {
        RPCSend snd(m_Socket,
                    sizeof(float) * 15 + sizeof(int32_t) * 38 + sizeof(float_3),
                    OctaneDataTransferObject::LOAD_KERNEL);
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << pKernel->type
            << pKernel->iMaxSamples << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->fFilterSize
            << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fCoherentRatio
            << pKernel->fCausticBlur << pKernel->fGIClamp << pKernel->fDepthTolerance
            << pKernel->fAdaptiveNoiseThreshold << pKernel->fAdaptiveExpectedExposure
            << pKernel->fAILightStrength << pKernel->bAlphaChannel << pKernel->bAlphaShadows
            << pKernel->bStaticNoise << pKernel->bKeepEnvironment << pKernel->bIrradianceMode
            << pKernel->bNestDielectrics << pKernel->bEmulateOldVolumeBehavior
            << pKernel->fAffectRoughness << pKernel->bAILightEnable << pKernel->bAILightUpdate
            << pKernel->iLightIDsAction << pKernel->iLightIDsMask
            << pKernel->iLightLinkingInvertMask << pKernel->bMinimizeNetTraffic
            << pKernel->bDeepImageEnable << pKernel->bDeepRenderPasses
            << pKernel->bAdaptiveSampling << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth
            << pKernel->iMaxScatterDepth << pKernel->iParallelSamples << pKernel->iMaxTileSamples
            << pKernel->iMaxDepthSamples << pKernel->iAdaptiveMinSamples
            << pKernel->adaptiveGroupPixels << pKernel->mbAlignment << pKernel->bLayersEnable
            << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
            << pKernel->iClayMode << pKernel->iSubsampleMode << pKernel->iMaxSubdivisionLevel
            << pKernel->iWhiteLightSpectrum << pKernel->bUseOldPipeline
            << pKernel->f3ToonShadowAmbient;
        snd.write();
      } break;
      case Kernel::PMC: {
        RPCSend snd(m_Socket,
                    sizeof(float) * 12 + sizeof(int32_t) * 31 + sizeof(float_3),
                    OctaneDataTransferObject::LOAD_KERNEL);
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << pKernel->type
            << pKernel->iMaxSamples << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->fFilterSize
            << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fExploration
            << pKernel->fDLImportance << pKernel->fCausticBlur << pKernel->fGIClamp
            << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bKeepEnvironment
            << pKernel->bIrradianceMode << pKernel->bNestDielectrics
            << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
            << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
            << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
            << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth << pKernel->iMaxScatterDepth
            << pKernel->iMaxRejects << pKernel->iParallelism << pKernel->iWorkChunkSize
            << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent
            << pKernel->bLayersInvert << pKernel->layersMode << pKernel->iClayMode
            << pKernel->iSubsampleMode << pKernel->iMaxSubdivisionLevel
            << pKernel->iWhiteLightSpectrum << pKernel->bUseOldPipeline
            << pKernel->f3ToonShadowAmbient;
        snd.write();
      } break;
      case Kernel::INFO_CHANNEL: {
        RPCSend snd(m_Socket,
                    sizeof(float) * 11 + sizeof(int32_t) * 24 + sizeof(float_3),
                    OctaneDataTransferObject::LOAD_KERNEL);
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << pKernel->type
            << pKernel->infoChannelType << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->fFilterSize
            << pKernel->fZdepthMax << pKernel->fUVMax << pKernel->fRayEpsilon << pKernel->fAODist
            << pKernel->fMaxSpeed << pKernel->fOpacityThreshold << pKernel->bAlphaChannel
            << pKernel->bBumpNormalMapping << pKernel->bBkFaceHighlight << pKernel->bAoAlphaShadows
            << pKernel->bMinimizeNetTraffic << pKernel->iSamplingMode << pKernel->iMaxSamples
            << pKernel->bStaticNoise << pKernel->iParallelSamples << pKernel->iMaxTileSamples
            << pKernel->mbAlignment << pKernel->bLayersEnable << pKernel->iLayersCurrent
            << pKernel->bLayersInvert << pKernel->layersMode << pKernel->iClayMode
            << pKernel->iSubsampleMode << pKernel->iMaxSubdivisionLevel
            << pKernel->iWhiteLightSpectrum << pKernel->bUseOldPipeline
            << pKernel->f3ToonShadowAmbient;
        snd.write();
      } break;
      case Kernel::PHOTON_TRACING: {
        RPCSend snd(m_Socket,
                    sizeof(float) * 18 + sizeof(int32_t) * 41 + sizeof(float_3),
                    OctaneDataTransferObject::LOAD_KERNEL);
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << pKernel->type
            << pKernel->iMaxSamples << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->fFilterSize
            << pKernel->fRayEpsilon << pKernel->fPathTermPower << pKernel->fCoherentRatio
            << pKernel->fCausticBlur << pKernel->fGIClamp << pKernel->fDepthTolerance
            << pKernel->fAdaptiveNoiseThreshold << pKernel->fAdaptiveExpectedExposure
            << pKernel->fAILightStrength << pKernel->iPhotonDepth << pKernel->bAccurateColors
            << pKernel->fPhotonGatherRadius << pKernel->fPhotonGatherMultiplier
            << pKernel->iPhotonGatherSamples << pKernel->fExplorationStrength
            << pKernel->bAlphaChannel << pKernel->bAlphaShadows << pKernel->bStaticNoise
            << pKernel->bKeepEnvironment << pKernel->bIrradianceMode << pKernel->bNestDielectrics
            << pKernel->bEmulateOldVolumeBehavior << pKernel->fAffectRoughness
            << pKernel->bAILightEnable << pKernel->bAILightUpdate << pKernel->iLightIDsAction
            << pKernel->iLightIDsMask << pKernel->iLightLinkingInvertMask
            << pKernel->bMinimizeNetTraffic << pKernel->bDeepImageEnable
            << pKernel->bDeepRenderPasses << pKernel->bAdaptiveSampling
            << pKernel->iMaxDiffuseDepth << pKernel->iMaxGlossyDepth << pKernel->iMaxScatterDepth
            << pKernel->iParallelSamples << pKernel->iMaxTileSamples << pKernel->iMaxDepthSamples
            << pKernel->iAdaptiveMinSamples << pKernel->adaptiveGroupPixels << pKernel->mbAlignment
            << pKernel->bLayersEnable << pKernel->iLayersCurrent << pKernel->bLayersInvert
            << pKernel->layersMode << pKernel->iClayMode << pKernel->iSubsampleMode
            << pKernel->iMaxSubdivisionLevel << pKernel->iWhiteLightSpectrum
            << pKernel->bUseOldPipeline << pKernel->f3ToonShadowAmbient;
        snd.write();
      } break;
      default: {
        RPCSend snd(m_Socket,
                    sizeof(int32_t) * 13 + sizeof(float) * 4 + sizeof(float_3),
                    OctaneDataTransferObject::LOAD_KERNEL);
        OctaneEngine::Kernel::KernelType defType = OctaneEngine::Kernel::DEFAULT;
        snd << pKernel->bUseNodeTree << pKernel->bEmulateOldMotionBlurBehavior << defType
            << pKernel->mbAlignment << pKernel->fCurrentTime << pKernel->fShutterTime
            << pKernel->fSubframeStart << pKernel->fSubframeEnd << pKernel->bLayersEnable
            << pKernel->iLayersCurrent << pKernel->bLayersInvert << pKernel->layersMode
            << pKernel->iClayMode << pKernel->iSubsampleMode << pKernel->iMaxSubdivisionLevel
            << pKernel->iWhiteLightSpectrum << pKernel->bUseOldPipeline
            << pKernel->f3ToonShadowAmbient;
        snd.write();
      } break;
    }
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_KERNEL) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading kernel.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }
  else {
    m_KernelCache[uiFrameIdx] = *pKernel;
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadKernel()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadRenderRegion(Camera *pCamera, bool bInteractive)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket,
                sizeof(uint32_t) * 9 + sizeof(float) * 2,
                OctaneDataTransferObject::LOAD_RENDER_REGION);
    if (pCamera->bUseRegion)
      snd << pCamera->ui4Region.x << pCamera->ui4Region.y << pCamera->ui4Region.z
          << pCamera->ui4Region.w;
    else {
      uint32_t tmp = 0;
      snd << tmp << tmp << tmp << tmp;
    }
    snd << pCamera->bUseCameraDimensionAsPreviewResolution << pCamera->ui2BlenderCameraDimension.x
        << pCamera->ui2BlenderCameraDimension.y << pCamera->f2BlenderCameraCenter.x
        << pCamera->f2BlenderCameraCenter.y << pCamera->bUseBlenderCamera << bInteractive;
    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_RENDER_REGION) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR setting render region.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadRenderRegion()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteNode(OctaneDataTransferObject::OctaneNodeBase *pNodeData)
{
  switch (pNodeData->octaneType) {
    // case Octane::NT_BOOL:
    // case Octane::NT_STRING:
    // case Octane::NT_ENUM:
    case Octane::NT_FLOAT:
    case Octane::NT_INT:
      deleteValue(pNodeData->sName);
      break;
    case Octane::NT_EMIS_BLACKBODY:
    case Octane::NT_EMIS_TEXTURE:
      deleteEmission(pNodeData->sName);
      break;
    case Octane::NT_MAT_DIFFUSE:
    case Octane::NT_MAT_GLOSSY:
    case Octane::NT_MAT_MIX:
    case Octane::NT_MAT_PORTAL:
    case Octane::NT_MAT_SPECULAR:
    case Octane::NT_MAT_TOON:
    case Octane::NT_MAT_METAL:
    case Octane::NT_MAT_UNIVERSAL:
      deleteMaterial(pNodeData->sName);
      break;
    case Octane::NT_MED_ABSORPTION:
    case Octane::NT_MED_SCATTERING:
      deleteMedium(pNodeData->sName);
      break;
    // case Octane::NT_PHASE_SCHLICK:
    //    break;
    case Octane::NT_PROJ_BOX:
    case Octane::NT_PROJ_CYLINDRICAL:
    case Octane::NT_PROJ_LINEAR:
    case Octane::NT_PROJ_PERSPECTIVE:
    case Octane::NT_PROJ_SPHERICAL:
    case Octane::NT_PROJ_UVW:
    case Octane::NT_PROJ_TRIPLANAR:
      deleteProjection(pNodeData->sName);
      break;
    case Octane::NT_DISPLACEMENT:
    case Octane::NT_TEX_ALPHAIMAGE:
    case Octane::NT_TEX_CHECKS:
    case Octane::NT_TEX_CLAMP:
    case Octane::NT_TEX_COLORCORRECTION:
    case Octane::NT_TEX_COSINEMIX:
    case Octane::NT_TEX_DIRT:
    case Octane::NT_TEX_FALLOFF:
    case Octane::NT_TEX_FLOAT:
    case Octane::NT_TEX_FLOATIMAGE:
    case Octane::NT_TEX_GAUSSIANSPECTRUM:
    case Octane::NT_TEX_GRADIENT:
    case Octane::NT_TEX_IMAGE_TILES:
    case Octane::NT_TEX_IMAGE:
    case Octane::NT_TEX_INVERT:
    case Octane::NT_TEX_MARBLE:
    case Octane::NT_TEX_MIX:
    case Octane::NT_TEX_MULTIPLY:
    case Octane::NT_TEX_NOISE:
    case Octane::NT_TEX_RANDOMCOLOR:
    case Octane::NT_TEX_RGB:
    case Octane::NT_TEX_RGFRACTAL:
    case Octane::NT_TEX_SAWWAVE:
    case Octane::NT_TEX_SINEWAVE:
    case Octane::NT_TEX_SIDE:
    case Octane::NT_TEX_TRIANGLEWAVE:
    case Octane::NT_TEX_TURBULENCE:
    case Octane::NT_TEX_INSTANCE_COLOR:
    case Octane::NT_TEX_INSTANCE_RANGE:
    case Octane::NT_TEX_OSL:
    case Octane::NT_CAM_OSL:
      deleteTexture(pNodeData->sName);
      break;
    case Octane::NT_TRANSFORM_2D:
    case Octane::NT_TRANSFORM_3D:
    case Octane::NT_TRANSFORM_ROTATION:
    case Octane::NT_TRANSFORM_SCALE:
    case Octane::NT_TRANSFORM_VALUE:
      deleteTransform(pNodeData->sName);
      break;
    default:
      break;
  }
}  // deleteNode()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadScatter(string &sScatterName,
                                 string &sMeshName,
                                 bool bUseGeoMat,
                                 float *pfMatrices,
                                 int32_t *piInstanceIds,
                                 uint64_t ulMatrCnt,
                                 bool bMovable,
                                 vector<string> &asShaderNames,
                                 uint32_t uiFrameIdx,
                                 uint32_t uiTotalFrames)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  uint64_t shaders_cnt = asShaderNames.size();

  {
    uint64_t size = sizeof(uint64_t) + sizeof(uint32_t) + sMeshName.length() + 2;

    if (bUseGeoMat) {
      for (uint64_t n = 0; n < shaders_cnt; ++n)
        size += asShaderNames[n].length() + 2;
    }

    RPCSend snd(
        m_Socket, size, OctaneDataTransferObject::LOAD_GEO_MAT, (sScatterName + "_m__").c_str());
    snd << shaders_cnt << bUseGeoMat << sMeshName;

    if (bUseGeoMat) {
      for (uint64_t n = 0; n < shaders_cnt; ++n)
        snd << asShaderNames[n];
    }
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_MAT) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR loading materials of transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  {
    uint64_t size = sizeof(uint64_t) + sizeof(int32_t)  // Movable
                    + sizeof(int32_t)                   // bUseGeoMat
                    + sizeof(uint32_t) * 2              // Frame index
                    + sMeshName.length() + 2 + sScatterName.length() + 4 + 2 +
                    sizeof(float) * 12 * ulMatrCnt + sizeof(int32_t) * ulMatrCnt;

    RPCSend snd(m_Socket,
                size,
                OctaneDataTransferObject::LOAD_GEO_SCATTER,
                (sScatterName + "_s__").c_str());
    string tmp = sScatterName + "_m__";
    snd << ulMatrCnt;
    if (ulMatrCnt)
      snd.writeBuffer(pfMatrices, sizeof(float) * 12 * ulMatrCnt);
    if (ulMatrCnt)
      snd.writeBuffer(piInstanceIds, sizeof(int32_t) * ulMatrCnt);
    snd << bMovable << bUseGeoMat << uiFrameIdx << uiTotalFrames << sMeshName << tmp;
    snd.write();
  }
  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_SCATTER) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading transform.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadScatter()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteScatter(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_GEO_SCATTER, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_GEO_SCATTER) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  // UNLOCK_MUTEX(m_SocketMutex);
}  // deleteScatter()

void OctaneClient::uploadOctaneObjects(OctaneDataTransferObject::OctaneObjects &objects)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // Generate Array Info(cannot transfer object matrix/instance data in vector format directly
  // due to it is quite slow)
  uint64_t fDataOffset = 0, iDataOffset = 0;

  for (auto &object : objects.oObjects) {
    object.oArrayInfo[ARRAY_INFO_INSTANCE_ID_DATA] = std::pair<uint32_t, uint32_t>(
        objects.iInstanceIDMap[object.sObjectName].size(), iDataOffset);
    iDataOffset += objects.iInstanceIDMap[object.sObjectName].size();
    object.oArrayInfo[ARRAY_INFO_MATRIX_DATA] = std::pair<uint32_t, uint32_t>(
        objects.fMatrixMap[object.sObjectName].size(), fDataOffset);
    fDataOffset += objects.fMatrixMap[object.sObjectName].size();
  }

  LOCK_MUTEX(m_SocketMutex);

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, objects);
  RPCSend snd(m_Socket,
              sizeof(uint32_t) * 3 + sbuf.size() + fDataOffset * sizeof(float) +
                  iDataOffset * sizeof(int32_t),
              OctaneDataTransferObject::LOAD_OBJECT,
              objects.sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size()) << static_cast<uint32_t>(fDataOffset)
      << static_cast<uint32_t>(iDataOffset);
  snd.writeBuffer(sbuf.data(), sbuf.size());

  for (auto &object : objects.oObjects) {
    if (objects.fMatrixMap[object.sObjectName].size()) {
      snd.writeBuffer(reinterpret_cast<float *>(objects.fMatrixMap[object.sObjectName].data()),
                      objects.fMatrixMap[object.sObjectName].size() * sizeof(float));
    }
  }

  for (auto &object : objects.oObjects) {
    if (objects.iInstanceIDMap[object.sObjectName].size()) {
      snd.writeBuffer(
          reinterpret_cast<int32_t *>(objects.iInstanceIDMap[object.sObjectName].data()),
          objects.iInstanceIDMap[object.sObjectName].size() * sizeof(int32_t));
    }
  }

  snd.write();

  checkResponsePacket(OctaneDataTransferObject::LOAD_OBJECT);

  UNLOCK_MUTEX(m_SocketMutex);
}

void OctaneClient::uploadOctaneMesh(OctaneDataTransferObject::OctaneMeshes &meshes)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  // Generate Array Info(cannot transfer mesh data in vector format directly due to it is quite
  // slow)
  uint64_t fDataOffset = 0, iDataOffset = 0;
  size_t totalMeshSize = meshes.bGlobal ? 1 : meshes.oMeshes.size();
  OctaneDataTransferObject::OctaneMesh *meshData = meshes.bGlobal ? &meshes.oGlobalMesh :
                                                                    meshes.oMeshes.data();
  std::vector<OctaneDataTransferObject::OctaneMesh> &oMeshes = meshes.oMeshes;
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_POINT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3Points.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3Points.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_NORMAL_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3Normals.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3Normals.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_POINT_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPointIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPointIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_NORMAL_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iNormalIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iNormalIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SMOOTH_GROUP_PER_POLY_DATA] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshData.iSmoothGroupPerPoly.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iSmoothGroupPerPoly.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_PER_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iVertexPerPoly.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iVertexPerPoly.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_MAT_ID_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPolyMaterialIndex.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPolyMaterialIndex.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OBJ_ID_POLY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iPolyObjectIndex.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iPolyObjectIndex.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3UVs.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3UVs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_UV_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iUVIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iUVIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_CANDIDATE_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3CandidateUVs.size(), 0);
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_CANDIDATE_UV_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iCandidateUVIndices.size(), 0);
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_CANDIDATE_UV_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.f3CandidateUVs[i].size(), fDataOffset);
      fDataOffset += 3 * mesh.oMeshData.f3CandidateUVs[i].size();
      mesh.oMeshData
          .oArrayInfo[std::string(ARRAY_INFO_CANDIDATE_UV_INDEX_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.iCandidateUVIndices[i].size(), iDataOffset);
      iDataOffset += mesh.oMeshData.iCandidateUVIndices[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_COLOR_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3VertexColors.size(), 0);
    for (int i = 0; i < mesh.oMeshData.f3VertexColors.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_VERTEX_COLOR_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.f3VertexColors[i].size(), fDataOffset);
      fDataOffset += 3 * mesh.oMeshData.f3VertexColors[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VERTEX_FLOAT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fVertexFloats.size(), 0);
    for (int i = 0; i < mesh.oMeshData.fVertexFloats.size(); ++i) {
      mesh.oMeshData.oArrayInfo[std::string(ARRAY_INFO_VERTEX_FLOAT_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.fVertexFloats[i].size(), fDataOffset);
      fDataOffset += mesh.oMeshData.fVertexFloats[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_VELOCITY_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3Velocities.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3Velocities.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_POINT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3HairPoints.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3HairPoints.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_VERTEX_PER_HAIR_DATA] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshData.iVertexPerHair.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iVertexPerHair.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_THICKNESS_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fHairThickness.size(), fDataOffset);
    fDataOffset += mesh.oMeshData.fHairThickness.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_MAT_INDEX_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.iHairMaterialIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iHairMaterialIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f2HairUVs.size(), fDataOffset);
    fDataOffset += 2 * mesh.oMeshData.f2HairUVs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_HAIR_W_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f2HairWs.size(), fDataOffset);
    fDataOffset += 2 * mesh.oMeshData.f2HairWs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OPENSUBDIVISION_CREASE_INDEX] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size(),
                                      iDataOffset);
    iDataOffset += mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_OPENSUBDIVISION_CREASE_SHARPNESS] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size(),
                                      fDataOffset);
    fDataOffset += mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size();

    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_CENTER_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3SphereCenters.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3SphereCenters.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_RADIUS_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fSphereRadiuses.size(), fDataOffset);
    fDataOffset += mesh.oMeshData.fSphereRadiuses.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_SPEED_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3SphereSpeeds.size(), fDataOffset);
    fDataOffset += 3 * mesh.oMeshData.f3SphereSpeeds.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_UV_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f2SphereUVs.size(), fDataOffset);
    fDataOffset += 2 * mesh.oMeshData.f2SphereUVs.size();
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_VERTEX_COLOR_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.f3SphereVertexColors.size(), 0);
    for (int i = 0; i < mesh.oMeshData.f3SphereVertexColors.size(); ++i) {
      mesh.oMeshData
          .oArrayInfo[std::string(ARRAY_INFO_SPHERE_VERTEX_COLOR_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.f3SphereVertexColors[i].size(),
                                        fDataOffset);
      fDataOffset += 3 * mesh.oMeshData.f3SphereVertexColors[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_VERTEX_FLOAT_DATA] = std::pair<uint32_t, uint32_t>(
        mesh.oMeshData.fSphereVertexFloats.size(), 0);
    for (int i = 0; i < mesh.oMeshData.fSphereVertexFloats.size(); ++i) {
      mesh.oMeshData
          .oArrayInfo[std::string(ARRAY_INFO_SPHERE_VERTEX_FLOAT_DATA) + std::to_string(i)] =
          std::pair<uint32_t, uint32_t>(mesh.oMeshData.fSphereVertexFloats[i].size(), fDataOffset);
      fDataOffset += mesh.oMeshData.fSphereVertexFloats[i].size();
    }
    mesh.oMeshData.oArrayInfo[ARRAY_INFO_SPHERE_MATERIAL_INDEX_DATA] =
        std::pair<uint32_t, uint32_t>(mesh.oMeshData.iSphereMaterialIndices.size(), iDataOffset);
    iDataOffset += mesh.oMeshData.iSphereMaterialIndices.size();
  }

  LOCK_MUTEX(m_SocketMutex);

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, meshes);
  RPCSend snd(m_Socket,
              sizeof(uint32_t) * 3 + sbuf.size() + fDataOffset * sizeof(float) +
                  iDataOffset * sizeof(int32_t),
              OctaneDataTransferObject::LOAD_MESH,
              meshes.sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size()) << static_cast<uint32_t>(fDataOffset)
      << static_cast<uint32_t>(iDataOffset);
  snd.writeBuffer(sbuf.data(), sbuf.size());
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3Points.data()),
                    mesh.oMeshData.f3Points.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3Normals.data()),
                    mesh.oMeshData.f3Normals.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3UVs.data()),
                    mesh.oMeshData.f3UVs.size() * 3 * sizeof(float));
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3CandidateUVs[i].data()),
                      mesh.oMeshData.f3CandidateUVs[i].size() * 3 * sizeof(float));
    }
    for (int i = 0; i < mesh.oMeshData.f3VertexColors.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3VertexColors[i].data()),
                      mesh.oMeshData.f3VertexColors[i].size() * 3 * sizeof(float));
    }
    for (int i = 0; i < mesh.oMeshData.fVertexFloats.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fVertexFloats[i].data()),
                      mesh.oMeshData.fVertexFloats[i].size() * sizeof(float));
    }
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3Velocities.data()),
                    mesh.oMeshData.f3Velocities.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3HairPoints.data()),
                    mesh.oMeshData.f3HairPoints.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fHairThickness.data()),
                    mesh.oMeshData.fHairThickness.size() * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f2HairUVs.data()),
                    mesh.oMeshData.f2HairUVs.size() * 2 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f2HairWs.data()),
                    mesh.oMeshData.f2HairWs.size() * 2 * sizeof(float));
    snd.writeBuffer(
        reinterpret_cast<float *>(mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.data()),
        mesh.oMeshOpenSubdivision.fOpenSubdCreasesSharpnesses.size() * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3SphereCenters.data()),
                    mesh.oMeshData.f3SphereCenters.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fSphereRadiuses.data()),
                    mesh.oMeshData.fSphereRadiuses.size() * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3SphereSpeeds.data()),
                    mesh.oMeshData.f3SphereSpeeds.size() * 3 * sizeof(float));
    snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f2SphereUVs.data()),
                    mesh.oMeshData.f2SphereUVs.size() * 2 * sizeof(float));
    for (int i = 0; i < mesh.oMeshData.f3SphereVertexColors.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.f3SphereVertexColors[i].data()),
                      mesh.oMeshData.f3SphereVertexColors[i].size() * 3 * sizeof(float));
    }
    for (int i = 0; i < mesh.oMeshData.fSphereVertexFloats.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<float *>(mesh.oMeshData.fSphereVertexFloats[i].data()),
                      mesh.oMeshData.fSphereVertexFloats[i].size() * sizeof(float));
    }
  }
  for (int idx = 0; idx < totalMeshSize; ++idx) {
    OctaneDataTransferObject::OctaneMesh &mesh = *(meshData + idx);
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPointIndices.data()),
                    mesh.oMeshData.iPointIndices.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iNormalIndices.data()),
                    mesh.oMeshData.iNormalIndices.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iSmoothGroupPerPoly.data()),
                    mesh.oMeshData.iSmoothGroupPerPoly.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iVertexPerPoly.data()),
                    mesh.oMeshData.iVertexPerPoly.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPolyMaterialIndex.data()),
                    mesh.oMeshData.iPolyMaterialIndex.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iPolyObjectIndex.data()),
                    mesh.oMeshData.iPolyObjectIndex.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iUVIndices.data()),
                    mesh.oMeshData.iUVIndices.size() * sizeof(int32_t));
    for (int i = 0; i < mesh.oMeshData.f3CandidateUVs.size(); ++i) {
      snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iCandidateUVIndices[i].data()),
                      mesh.oMeshData.iCandidateUVIndices[i].size() * sizeof(int32_t));
    }
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iVertexPerHair.data()),
                    mesh.oMeshData.iVertexPerHair.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iHairMaterialIndices.data()),
                    mesh.oMeshData.iHairMaterialIndices.size() * sizeof(int32_t));
    snd.writeBuffer(
        reinterpret_cast<int32_t *>(mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.data()),
        mesh.oMeshOpenSubdivision.iOpenSubdCreasesIndices.size() * sizeof(int32_t));
    snd.writeBuffer(reinterpret_cast<int32_t *>(mesh.oMeshData.iSphereMaterialIndices.data()),
                    mesh.oMeshData.iSphereMaterialIndices.size() * sizeof(int32_t));
  }
  snd.write();

  checkResponsePacket(OctaneDataTransferObject::LOAD_MESH);

  UNLOCK_MUTEX(m_SocketMutex);
}

void OctaneClient::getOctaneGeoNodes(std::set<std::string> &nodeNames)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  OctaneDataTransferObject::OctaneGeoNodes nodes;
  nodes.sName = "GetOctaneGeoNodes";
  nodes.iMeshNodeType = Octane::NT_OBJECTLAYER_MAP;

  LOCK_MUTEX(m_SocketMutex);

  // RPCMsgPackObj::send<OctaneDataTransferObject::OctaneGeoNodes>(
  //    m_Socket, nodes.packetType, nodes, nodes.sName.c_str());
  // RPCMsgPackObj::receive<OctaneDataTransferObject::OctaneGeoNodes>(
  //    m_Socket, nodes.packetType, nodes);
  nodeNames = nodes.sMeshNames;

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteMesh(bool bGlobal, string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket,
                0,
                (bGlobal ? OctaneDataTransferObject::DEL_GLOBAL_MESH :
                           OctaneDataTransferObject::DEL_LOCAL_MESH),
                sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != (bGlobal ? OctaneDataTransferObject::DEL_GLOBAL_MESH :
                                       OctaneDataTransferObject::DEL_LOCAL_MESH))
    {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting mesh.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMesh()

void OctaneClient::uploadLight(OctaneDataTransferObject::OctaneLight *pLight)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);
  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, *pLight);
  RPCSend snd(m_Socket,
              sbuf.size() + sizeof(uint32_t),
              OctaneDataTransferObject::OctaneLight::packetType,
              pLight->sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size());
  snd.writeBuffer(sbuf.data(), sbuf.size());
  snd.write();
  checkResponsePacket(OctaneDataTransferObject::OctaneLight::packetType);
  UNLOCK_MUTEX(m_SocketMutex);
}

void OctaneClient::deleteLight(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_LIGHT, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_LIGHT) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting light.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadLayerMap(bool bGlobal,
                                  string const &sLayerMapName,
                                  string const &sMeshName,
                                  int32_t iLayersCnt,
                                  int32_t *piLayerId,
                                  int32_t *piBakingGroupId,
                                  float *pfGeneralVis,
                                  bool *pbCamVis,
                                  bool *pbShadowVis,
                                  int32_t *piRandColorSeed,
                                  int32_t *piLightPassMask)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    uint64_t size = sizeof(int32_t) + sMeshName.length() + 2 + sizeof(int32_t)  // Layers count;
                    + sizeof(int32_t) * iLayersCnt * 2   // Layer and Baking group IDs
                    + sizeof(int32_t) * iLayersCnt       // Color seeds
                    + sizeof(int32_t) * iLayersCnt       // Light pass masks
                    + sizeof(float) * iLayersCnt         // Gen visibilities
                    + sizeof(int32_t) * iLayersCnt * 2;  // Cam and shadow visibilities

    RPCSend snd(
        m_Socket, size, OctaneDataTransferObject::LOAD_GEO_LAYERMAP, sLayerMapName.c_str());

    snd << bGlobal << iLayersCnt;

    for (long i = 0; i < iLayersCnt; ++i)
      snd << pfGeneralVis[i] << piLayerId[i] << piBakingGroupId[i] << pbCamVis[i] << pbShadowVis[i]
          << piRandColorSeed[i] << piLightPassMask[i];

    snd << sMeshName;

    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_GEO_LAYERMAP) {
    rcv >> m_sErrorMsg;
    fprintf(stderr, "Octane: ERROR loading layer map.");
    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadMesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteLayerMap(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_GEO_LAYERMAP, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_GEO_LAYERMAP) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting layer map.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteLayerMap()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::uploadVolume(OctaneDataTransferObject::OctaneVolume *pNode)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  pNode->arraySize = pNode->fRegularGridData.size() * sizeof(float);
  pNode->arrayData = pNode->fRegularGridData.size() ? (void *)pNode->fRegularGridData.data() :
                                                      NULL;

  msgpack::sbuffer sbuf;
  msgpack::pack(sbuf, *pNode);
  RPCSend snd(m_Socket,
              sizeof(uint32_t) + sbuf.size() + pNode->arraySize,
              OctaneDataTransferObject::LOAD_VOLUME,
              pNode->sName.c_str());
  snd << static_cast<uint32_t>(sbuf.size());
  snd.writeBuffer(sbuf.data(), sbuf.size());
  if (pNode->arraySize) {
    snd.writeBuffer(pNode->arrayData, pNode->arraySize);
  }
  snd.write();

  checkResponsePacket(OctaneDataTransferObject::LOAD_VOLUME);

  UNLOCK_MUTEX(m_SocketMutex);
}  // uploadVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteVolume(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_VOLUME, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_VOLUME) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting volume.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteVolume()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::checkResponsePacket(OctaneDataTransferObject::PacketType packetType,
                                       const char *szErrorMsg)
{
  if (m_Socket < 0)
    return false;

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType != packetType) {
    rcv >> m_sErrorMsg;

    if (szErrorMsg && szErrorMsg[0])
      fprintf(stderr, "Octane: uploading ERROR: %s.", szErrorMsg);
    else
      fprintf(stderr, "Octane: uploading ERROR.");

    if (m_sErrorMsg.length() > 0)
      fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
    else
      fprintf(stderr, "\n");
    return false;
  }
  else
    return true;
}  // checkResponsePacket()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MATERIALS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteMaterial(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_MATERIAL, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_MATERIAL) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting material.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMaterial()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// TEXTURES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
string OctaneClient::getFileName(string &sFullPath)
{
  size_t sl1 = sFullPath.rfind('/');
  size_t sl2 = sFullPath.rfind('\\');
  string file_name;
  if (sl1 == string::npos && sl2 == string::npos) {
    file_name = sFullPath;
  }
  else {
    if (sl1 == string::npos)
      sl1 = sl2;
    else if (sl2 != string::npos)
      sl1 = sl1 > sl2 ? sl1 : sl2;
    file_name = sFullPath.substr(sl1 + 1);
  }
  return std::to_string(std::hash<std::string>{}(sFullPath)) + "_" + file_name;
}  // getFileName()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
uint64_t OctaneClient::getFileTime(string &sFullPath)
{
  if (!sFullPath.length())
    return 0;

#ifdef _WIN32
  struct _stat64i32 attrib;
#else
  struct stat attrib;
#endif
  ustat(sFullPath.c_str(), &attrib);

  return static_cast<uint64_t>(attrib.st_mtime);
}  // getFileTime()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::uploadFile(string &sFilePath, string &sFileName)
{
  FILE *hFile = ufopen(sFilePath.c_str(), "rb");
  if (hFile) {
    fseek(hFile, 0, SEEK_END);
    uint32_t ulFileSize = ftell(hFile);
    rewind(hFile);

    char *pCurPtr = new char[ulFileSize];

    if (!fread(pCurPtr, ulFileSize, 1, hFile)) {
      fclose(hFile);
      delete[] pCurPtr;
      return false;
    }
    fclose(hFile);

    RPCSend snd(m_Socket,
                sizeof(uint32_t) + ulFileSize,
                OctaneDataTransferObject::LOAD_IMAGE_FILE,
                sFileName.c_str());
    snd << ulFileSize;
    snd.writeBuffer(pCurPtr, ulFileSize);
    snd.write();
    delete[] pCurPtr;

    {
      RPCReceive rcv(m_Socket);
      if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_IMAGE_FILE) {
        rcv >> m_sErrorMsg;
        fprintf(stderr, "Octane: ERROR loading image file.");
        if (m_sErrorMsg.length() > 0)
          fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
        else
          fprintf(stderr, "\n");
        return false;
      }
    }
    return true;
  }
  else
    return false;
}  // uploadFile()

void OctaneClient::uploadOctaneNode(OctaneDataTransferObject::OctaneNodeBase *pNode,
                                    OctaneDataTransferObject::OctaneNodeResponse *pResponse)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;
  LOCK_MUTEX(m_SocketMutex);

  RPCMsgPackObj::sendOctaneNode(m_Socket, pNode->sName, pNode);
  for (int i = 0; i < pNode->responseNodeNum; ++i) {
    OctaneDataTransferObject::OctaneNodeBase *pResponseNode = RPCMsgPackObj::receiveOctaneNode(
        m_Socket);
    if (pResponseNode && pResponse) {
      pResponse->emplace_back(pResponseNode);
    }
  }
  checkResponsePacket(OctaneDataTransferObject::LOAD_OCTANE_NODE);

  UNLOCK_MUTEX(m_SocketMutex);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteTexture(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_TEXTURE, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_TEXTURE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting texture.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteTexture()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// EMISSIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteEmission(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_EMISSION, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_EMISSION) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting emission.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteEmission()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteMedium(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_MEDIUM, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_MEDIUM) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting medium.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteMedium()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteTransform(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_TRANSFORM, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_TRANSFORM) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting transform.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteTransform()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PROJECTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void OctaneClient::deleteProjection(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_PROJECTION, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_PROJECTION) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting projection.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteProjection()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// VALUES
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::deleteValue(string const &sName)
{
  if (m_Socket < 0 || m_cBlockUpdates)
    return;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(m_Socket, 0, OctaneDataTransferObject::DEL_VALUE, sName.c_str());
    snd.write();
  }
  {
    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType != OctaneDataTransferObject::DEL_VALUE) {
      rcv >> m_sErrorMsg;
      fprintf(stderr, "Octane: ERROR deleting value node.");
      if (m_sErrorMsg.length() > 0)
        fprintf(stderr, " Server log:\n%s\n", m_sErrorMsg.c_str());
      else
        fprintf(stderr, "\n");
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
}  // deleteValue()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// IMAGE BUFFER METHODS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Octane::RenderPassId OctaneClient::currentPassType()
{
  return m_CurPassType;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::checkImgBuffer8bit(uint8_4 *&puc4Buf,
                                      int iWidth,
                                      int iHeight,
                                      int iRegionWidth,
                                      int iRegionHeight,
                                      bool bCopyToBuf)
{
  if ((!m_pucImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight ||
       m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) &&
      iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0)
  {
    if (iWidth < 4)
      iWidth = 4;
    if (iHeight < 4)
      iHeight = 4;
    if (iRegionWidth < 4)
      iRegionWidth = 4;
    if (iRegionHeight < 4)
      iRegionHeight = 4;

    if (m_pucImageBuf)
      delete[] m_pucImageBuf;
    size_t stLen = iRegionWidth * iRegionHeight * 4;
    m_pucImageBuf = new unsigned char[stLen];

    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    memset(m_pucImageBuf, 1, stLen);
    if (bCopyToBuf) {
      // if(puc4Buf) delete[] puc4Buf;
      puc4Buf = new uint8_4[iRegionWidth * iRegionHeight];
      memcpy(puc4Buf, m_pucImageBuf, iRegionWidth * iRegionHeight * 4);
    }

    return false;
  }
  else if (iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
    if (!m_pucImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 ||
        m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4)
    {
      iWidth = m_iCurImgBufWidth = -1;
      iHeight = m_iCurImgBufHeight = -1;
      iRegionWidth = m_iCurRegionWidth = -1;
      iRegionHeight = m_iCurRegionHeight = -1;

      return false;
    }
    else {
      iWidth = m_iCurImgBufWidth;
      iHeight = m_iCurImgBufHeight;
      iRegionWidth = m_iCurRegionWidth;
      iRegionHeight = m_iCurRegionHeight;

      m_iCurImgBufWidth = -1;
      m_iCurImgBufHeight = -1;
      m_iCurRegionWidth = -1;
      m_iCurRegionHeight = -1;
    }
  }
  return true;
}  // checkImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 bool OctaneClient::getImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int
&iRegionWidth, int &iRegionHeight) { LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, false)) {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
    }
    else {
        puc4Buf = reinterpret_cast<uint8_4*>(m_pucImageBuf);
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getImgBuffer8bit()
*/

bool OctaneClient::isSharedSurfaceImage() {
  return m_bServerUseSharedSurface;
}

bool OctaneClient::getSharedSurfaceHandler(
    int64_t &iSharedHandler, int iWidth, int iHeight, int iRegionWidth, int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);
  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight)
  {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;
  }
  iSharedHandler = m_iSharedHandler;
  UNLOCK_MUTEX(m_ImgBufMutex);
  return iSharedHandler != 0;
}

bool OctaneClient::getImgBuffer8bit(int &iComponentsCnt,
                                    uint8_t *&pucBuf,
                                    int iWidth,
                                    int iHeight,
                                    int iRegionWidth,
                                    int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight)
  {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pucImageBuf) {
      delete[] m_pucImageBuf;
      m_pucImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pucImageBuf || !m_stImgBufLen) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  iComponentsCnt = m_iComponentCnt;
  pucBuf = m_pucImageBuf;
  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 bool OctaneClient::getCopyImgBuffer8bit(uint8_4 *&puc4Buf, int &iWidth, int &iHeight, int
&iRegionWidth, int &iRegionHeight) { LOCK_MUTEX(m_ImgBufMutex);

    if(checkImgBuffer8bit(puc4Buf, iWidth, iHeight, iRegionWidth, iRegionHeight, true)) {
        if(!puc4Buf) puc4Buf = new uint8_4[iWidth * iHeight];

        memcpy(puc4Buf, m_pucImageBuf, iWidth * iHeight * 4);
    }
    else {
        UNLOCK_MUTEX(m_ImgBufMutex);
        return false;
    }























































































































































































































































































































































































































    UNLOCK_MUTEX(m_ImgBufMutex);
    return true;
} //getCopyImgBuffer8bit()
*/
bool OctaneClient::getCopyImgBuffer8bit(int iComponentsCnt,
                                        uint8_t *&pucBuf,
                                        int iWidth,
                                        int iHeight,
                                        int iRegionWidth,
                                        int iRegionHeight)
{
  // FIXME: Make it respect 8-bit buffer alignment
  return false;

  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight)
  {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pucImageBuf) {
      delete[] m_pucImageBuf;
      m_pucImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pucImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  size_t stPixelSize = iRegionWidth * iRegionHeight;
  uint8_t *in = m_pucImageBuf;

  switch (iComponentsCnt) {
    case 1: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 1
    case 2: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = 255;
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = in[1];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
            pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
            pOut[1] = 255;
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
            pOut[0] = (uint8_t)floorf((in[0] + in[1] + in[2]) / 3.0f + 0.5f);
            pOut[1] = in[1];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 2
    case 3: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 3
    case 4: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = 255;
          }
          break;
        }
        case 2: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = in[1];
          }
          break;
        }
        case 3: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = 255;
          }
          break;
        }
        case 4: {
          if (!pucBuf)
            pucBuf = new uint8_t[stPixelSize];
          uint8_t *pOut = pucBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = in[3];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 4
    default: {
      UNLOCK_MUTEX(m_ImgBufMutex);
      return false;
      break;
    }  // default
  }

  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getCopyImgBuffer8bit()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::checkImgBufferFloat(int iComponentsCnt,
                                       float *&pfBuf,
                                       int iWidth,
                                       int iHeight,
                                       int iRegionWidth,
                                       int iRegionHeight,
                                       bool bCopyToBuf)
{
  if ((!m_pfImageBuf || m_iCurImgBufWidth != iWidth || m_iCurImgBufHeight != iHeight ||
       m_iCurRegionWidth != iRegionWidth || m_iCurRegionHeight != iRegionHeight) &&
      iWidth > 0 && iHeight > 0 && iRegionWidth > 0 && iRegionHeight > 0)
  {
    if (iWidth < 4)
      iWidth = 4;
    if (iHeight < 4)
      iHeight = 4;
    if (iRegionWidth < 4)
      iRegionWidth = 4;
    if (iRegionHeight < 4)
      iRegionHeight = 4;

    if (m_pfImageBuf)
      delete[] m_pfImageBuf;
    size_t stLen = iRegionWidth * iRegionHeight * 4;
    m_pfImageBuf = new float[stLen];

    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    memset(m_pfImageBuf, 0, stLen * sizeof(float));
    if (bCopyToBuf) {
      pfBuf = new float[iRegionWidth * iRegionHeight * iComponentsCnt];
      memset(pfBuf, 0, iRegionWidth * iRegionHeight * iComponentsCnt * sizeof(float));
    }

    return false;
  }
  else if (iWidth <= 0 || iHeight <= 0 || iRegionWidth <= 0 || iRegionHeight <= 0) {
    if (!m_pfImageBuf || m_iCurImgBufWidth < 4 || m_iCurImgBufHeight < 4 ||
        m_iCurRegionWidth < 4 || m_iCurRegionHeight < 4)
    {
      iWidth = m_iCurImgBufWidth = -1;
      iHeight = m_iCurImgBufHeight = -1;
      iRegionWidth = m_iCurRegionWidth = -1;
      iRegionHeight = m_iCurRegionHeight = -1;

      return false;
    }
    else {
      iWidth = m_iCurImgBufWidth;
      iHeight = m_iCurImgBufHeight;
      iRegionWidth = m_iCurRegionWidth;
      iRegionHeight = m_iCurRegionHeight;

      m_iCurImgBufWidth = -1;
      m_iCurImgBufHeight = -1;
      m_iCurRegionWidth = -1;
      m_iCurRegionHeight = -1;
    }
  }
  return true;
}  // checkImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::getImgBufferFloat(int &iComponentsCnt,
                                     float *&pfBuf,
                                     int iWidth,
                                     int iHeight,
                                     int iRegionWidth,
                                     int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight)
  {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pfImageBuf) {
      delete[] m_pfImageBuf;
      m_pfImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pfImageBuf || !m_stImgBufLen) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  iComponentsCnt = m_iComponentCnt;
  pfBuf = m_pfImageBuf;
  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::getCopyImgBufferFloat(int iComponentsCnt,
                                         float *&pfBuf,
                                         int iWidth,
                                         int iHeight,
                                         int iRegionWidth,
                                         int iRegionHeight)
{
  LOCK_MUTEX(m_ImgBufMutex);

  if (iWidth != m_iCurImgBufWidth || iHeight != m_iCurImgBufHeight ||
      iRegionWidth != m_iCurRegionWidth || iRegionHeight != m_iCurRegionHeight)
  {
    m_iCurImgBufWidth = iWidth;
    m_iCurImgBufHeight = iHeight;
    m_iCurRegionWidth = iRegionWidth;
    m_iCurRegionHeight = iRegionHeight;

    if (m_pfImageBuf) {
      delete[] m_pfImageBuf;
      m_pfImageBuf = 0;
      m_stImgBufLen = 0;
    }

    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  if (!m_pfImageBuf || !m_stImgBufLen || iComponentsCnt < 1 || iComponentsCnt > 4) {
    UNLOCK_MUTEX(m_ImgBufMutex);
    return false;
  }

  size_t stPixelSize = iRegionWidth * iRegionHeight;
  float *in = m_pfImageBuf;

  switch (iComponentsCnt) {
    case 1: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = (in[0] + in[1] + in[2]) / 3.0f;
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = (in[0] + in[1] + in[2]) / 3.0f;
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }           // case 1
    case -1: {  // Usable for MaterialId pass in host-applications requiring just one ID number
                // instead of color
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut++)
            *pOut = *in;
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut++)
            *pOut = *in;
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut++)
            *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) |
                    ((uint32_t)(in[2] * 255));
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut++)
            *pOut = ((uint32_t)(in[0] * 255) << 16) | ((uint32_t)(in[1] * 255) << 8) |
                    ((uint32_t)(in[2] * 255));
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case -1
    case 2: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = 1.0f;
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 2) {
            pOut[0] = in[0];
            pOut[1] = in[1];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 2) {
            pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
            pOut[1] = 1.0f;
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 2) {
            pOut[0] = (in[0] + in[1] + in[2]) / 3.0f;
            pOut[1] = in[1];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 2
    case 3: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 3) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 3
    case 4: {
      switch (m_iComponentCnt) {
        case 1: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 1, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = 1.0f;
          }
          break;
        }
        case 2: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 2, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[0];
            pOut[2] = in[0];
            pOut[3] = in[1];
          }
          break;
        }
        case 3: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 3, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = 1.0f;
          }
          break;
        }
        case 4: {
          if (!pfBuf)
            pfBuf = new float[stPixelSize];
          float *pOut = pfBuf;
          for (int i = 0; i < stPixelSize; ++i, in += 4, pOut += 4) {
            pOut[0] = in[0];
            pOut[1] = in[1];
            pOut[2] = in[2];
            pOut[3] = in[3];
          }
          break;
        }
        default: {
          UNLOCK_MUTEX(m_ImgBufMutex);
          return false;
          break;
        }
      }
      break;
    }  // case 4
    default: {
      UNLOCK_MUTEX(m_ImgBufMutex);
      return false;
      break;
    }  // default
  }

  UNLOCK_MUTEX(m_ImgBufMutex);
  return true;
}  // getCopyImgBufferFloat()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool OctaneClient::downloadImageBuffer(RenderStatistics &renderStat,
                                       ImageType const imgType,
                                       RenderPassId &passType,
                                       bool bUseSharedSurface,
                                       bool const bForce)
{
  if (m_Socket < 0)
    return false;

  LOCK_MUTEX(m_SocketMutex);

  while (true) {
    {
      RPCSend snd(
          m_Socket, sizeof(int32_t) * 4 + sizeof(uint32_t), OctaneDataTransferObject::GET_IMAGE);
      snd << bForce << imgType << m_iCurImgBufWidth << m_iCurImgBufHeight << passType;
      snd.write();
    }

    bool bServerUseSharedSurface = false;

    RPCReceive rcv(m_Socket);
    if (rcv.m_PacketType == OctaneDataTransferObject::GET_IMAGE) {
      uint32_t uiW, uiH, uiRegW, uiRegH, uiSamples, uiCurDenoiseSamples;
      rcv >> renderStat.ulVramUsed >> renderStat.ulVramFree >> renderStat.ulVramTotal >>
          renderStat.fSPS >> renderStat.fRenderTime >> renderStat.fGamma >> passType >>
          renderStat.iExpiryTime >> renderStat.iComponentsCnt >> renderStat.uiTrianglesCnt >>
          renderStat.uiMeshesCnt >> renderStat.uiSpheresCnt >> renderStat.uiVoxelsCnt >>
          renderStat.uiDisplCnt >> renderStat.uiHairsCnt >> renderStat.uiRgb32Cnt >>
          renderStat.uiRgb64Cnt >> renderStat.uiGrey8Cnt >> renderStat.uiGrey16Cnt >>
          uiCurDenoiseSamples >> uiSamples >> renderStat.uiMaxSamples >> uiW >> uiH >> uiRegW >>
          uiRegH >> renderStat.uiNetGPUs >> renderStat.uiNetGPUsUsed;
      rcv >> bServerUseSharedSurface;
      renderStat.uiW = uiW;
      renderStat.uiH = uiH;
      renderStat.uiRegW = uiRegW;
      renderStat.uiRegH = uiRegH;

      if (m_iComponentCnt != renderStat.iComponentsCnt)
        m_iComponentCnt = renderStat.iComponentsCnt;

      if (uiSamples && renderStat.uiCurSamples != uiSamples)
        renderStat.uiCurSamples = uiSamples;
      if (uiCurDenoiseSamples && renderStat.uiCurDenoiseSamples != uiCurDenoiseSamples)
        renderStat.uiCurDenoiseSamples = uiCurDenoiseSamples;

      if (m_iCurImgBufWidth < 0 || m_iCurImgBufHeight < 0 || m_iCurRegionWidth < 0 ||
          m_iCurRegionHeight < 0)
      {
        m_iCurImgBufWidth = static_cast<int>(uiW);
        m_iCurImgBufHeight = static_cast<int>(uiH);
        m_iCurRegionWidth = static_cast<int>(uiRegW);
        m_iCurRegionHeight = static_cast<int>(uiRegH);
      }
      bool bPassUseSharedSurface = true;
      switch (passType) {
        // case Octane::RENDER_PASS_Z_DEPTH:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_NODE:
        case Octane::RENDER_PASS_CRYPTOMATTE_MATERIAL_PIN_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_NODE:
        case Octane::RENDER_PASS_CRYPTOMATTE_OBJECT_PIN_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_RENDER_LAYER:
        case Octane::RENDER_PASS_CRYPTOMATTE_INSTANCE:
        case Octane::RENDER_PASS_CRYPTOMATTE_GEOMETRY_NODE_NAME:
        case Octane::RENDER_PASS_CRYPTOMATTE_USER_INSTANCE_ID:
          bPassUseSharedSurface = false;
          break;
        default:
          bPassUseSharedSurface = (passType < Octane::RENDER_PASS_OUTPUT_AOV_IDS_OFFSET);
      }
      if (bServerUseSharedSurface) {
        rcv >> renderStat.iSharedHandler;
        LOCK_MUTEX(m_ImgBufMutex);
        m_bServerUseSharedSurface = true;
        m_iSharedHandler = renderStat.iSharedHandler;
        UNLOCK_MUTEX(m_ImgBufMutex);
        if (m_CurPassType != passType) {
          m_CurPassType = passType;
        }
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
      }

      LOCK_MUTEX(m_ImgBufMutex);

      m_bServerUseSharedSurface = false;
      m_iSharedHandler = 0;

      size_t stLen = uiRegW * uiRegH * renderStat.iComponentsCnt;

      if (m_CurPassType != passType)
        m_CurPassType = passType;

      if (imgType == IMAGE_8BIT) {
        size_t stSrcStringSize = uiRegW * renderStat.iComponentsCnt;
        size_t stDstStringSize =
            ((uiRegW * renderStat.iComponentsCnt) / renderStat.iComponentsCnt +
             ((uiRegW * renderStat.iComponentsCnt) % renderStat.iComponentsCnt ? 1 : 0)) *
            renderStat.iComponentsCnt;
        size_t stDstLen = stDstStringSize * uiRegH;

        if (!m_pucImageBuf || m_stImgBufLen != stDstLen) {
          m_stImgBufLen = stDstLen;

          if (m_pucImageBuf)
            delete[] m_pucImageBuf;
          if (stLen)
            m_pucImageBuf = new unsigned char[stDstLen];
          else
            m_pucImageBuf = 0;

          if (m_pfImageBuf)
            delete[] m_pfImageBuf;
          if (stLen)
            m_pfImageBuf = new float[stLen];
          else
            m_pfImageBuf = 0;
        }

        if (!m_pucImageBuf) {
          UNLOCK_MUTEX(m_ImgBufMutex);
          UNLOCK_MUTEX(m_SocketMutex);
          return false;
        }

        uint8_t *ucBuf = (uint8_t *)rcv.readBuffer(stLen);

        // if(ucBuf) memcpy(m_pucImageBuf, ucBuf, stLen);
        uint8_t *p = m_pucImageBuf;
        uint8_t *s = ucBuf;
        for (int y = 0; y < uiRegH; ++y) {
          memcpy(p, s, stSrcStringSize);
          p += stDstStringSize;
          s += stSrcStringSize;
        }
      }
      else {
        if (!m_pfImageBuf || m_stImgBufLen != stLen) {
          m_stImgBufLen = stLen;

          if (m_pfImageBuf)
            delete[] m_pfImageBuf;
          if (stLen)
            m_pfImageBuf = new float[stLen];
          else
            m_pfImageBuf = 0;

          if (m_pucImageBuf)
            delete[] m_pucImageBuf;
          if (stLen)
            m_pucImageBuf = new unsigned char[stLen];
          else
            m_pucImageBuf = 0;
        }

        if (!m_pfImageBuf) {
          UNLOCK_MUTEX(m_ImgBufMutex);
          UNLOCK_MUTEX(m_SocketMutex);
          return false;
        }

        float *pfBuf = (float *)rcv.readBuffer(stLen * sizeof(float));

        if (pfBuf)
          memcpy(m_pfImageBuf, pfBuf, stLen * sizeof(float));
      }

      UNLOCK_MUTEX(m_ImgBufMutex);
      break;
    }
    else if (!bForce) {
      std::string sError;
      rcv >> sError;
      if (sError.length() > 0) {
        fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
        m_sErrorMsg += sError;
      }

      if (imgType == IMAGE_8BIT && m_pucImageBuf && m_stImgBufLen) {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
      }
      else if (imgType != IMAGE_8BIT && m_pfImageBuf && m_stImgBufLen) {
        UNLOCK_MUTEX(m_SocketMutex);
        return true;
      }
      else {
        UNLOCK_MUTEX(m_SocketMutex);
        return false;
      }
    }
    else {
      std::string sError;
      rcv >> sError;
      if (sError.length() > 0) {
        fprintf(stderr, "\nOctane: ERROR. Server log:\n%s\n", sError.c_str());
        m_sErrorMsg += sError;
      }

      UNLOCK_MUTEX(m_SocketMutex);
      return false;
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return true;
}  // downloadImageBuffer()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unsigned char *OctaneClient::getPreview(std::string sName, uint32_t &uiWidth, uint32_t &uiHeight)
{
  if (m_Socket < 0)
    return nullptr;
  unsigned char *pucImageBuf = 0;

  LOCK_MUTEX(m_SocketMutex);

  {
    RPCSend snd(
        m_Socket, sizeof(uint32_t) * 2, OctaneDataTransferObject::GET_PREVIEW, sName.c_str());
    snd << uiWidth << uiHeight;
    snd.write();
  }

  RPCReceive rcv(m_Socket);
  if (rcv.m_PacketType == OctaneDataTransferObject::GET_PREVIEW) {
    uint32_t uiW, uiH;
    rcv >> uiW >> uiH;

    size_t stLen = uiW * uiH * 4;

    if (stLen) {
      uiWidth = uiW;
      uiHeight = uiH;

      uint8_t *ucBuf = (uint8_t *)rcv.readBuffer(stLen);

      if (ucBuf) {
        pucImageBuf = new unsigned char[stLen];
        memcpy(pucImageBuf, ucBuf, stLen);
      }
    }
  }

  UNLOCK_MUTEX(m_SocketMutex);
  return pucImageBuf;
}  // getPreview()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void OctaneClient::setUpdatesBlocked(bool bBlocked)
{
  m_cBlockUpdates = bBlocked ? 1 : 0;
  return;
}  // getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
OctaneClient::RenderServerInfo &OctaneClient::getServerInfo(void)
{
  return m_ServerInfo;
}  // getServerInfo()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
FailReasons::FailReasonsEnum OctaneClient::getFailReason(void)
{
  return m_FailReason;
}  // getFailReason()

bool OctaneClient::compileOSL(OctaneDataTransferObject::OctaneNodeBase *pNode,
                              OctaneDataTransferObject::OSLNodeInfo &oslNodeInfo)
{
  std::vector<OctaneDataTransferObject::OctaneNodeBase *> pResponse;
  uploadOctaneNode(pNode, &pResponse);
  assert(pResponse.size() == 1);
  OctaneDataTransferObject::OSLNodeInfo *pNodeInfo =
      (OctaneDataTransferObject::OSLNodeInfo *)(pResponse[0]);
  oslNodeInfo.mCompileResult = pNodeInfo->mCompileResult;
  oslNodeInfo.mCompileInfo = pNodeInfo->mCompileInfo;
  oslNodeInfo.mPinInfo = pNodeInfo->mPinInfo;
  for (auto pResponseNode : pResponse) {
    delete pResponseNode;
  }
  return oslNodeInfo.mCompileResult == Octane::COMPILE_SUCCESS;
}

bool OctaneClient::commandToOctane(int cmdType,
                                   const std::vector<int> &iParams,
                                   const std::vector<float> &fParams,
                                   const std::vector<std::string> &sParams)
{
  OctaneDataTransferObject::OctaneCommand cmdNode(cmdType, iParams, fParams, sParams);
  uploadOctaneNode(&cmdNode);
  return true;
}

}  // namespace OctaneEngine
