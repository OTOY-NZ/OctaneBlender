#include "octane_network.h"

namespace OctaneEngine {

RPCSend::RPCSend(int socket,
                 uint64_t ulBufSize,
                 OctaneDataTransferObject::PacketType packetType,
                 const char *szName)
    : m_PacketType(packetType), m_Socket(socket)
{
  m_ulBufSize = ulBufSize + sizeof(uint64_t) * 2;
  size_t stNameLen, stNameBufLen;

  if (szName) {
    stNameLen = strlen(szName);
    if (stNameLen > 245)
      stNameLen = 245;
    stNameBufLen = stNameLen + 1 + 1;
    stNameBufLen += sizeof(uint64_t) - stNameBufLen % sizeof(uint64_t);
    m_ulBufSize += stNameBufLen;
  }
  else {
    stNameLen = 0;
    stNameBufLen = 0;
  }
  m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];

  *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = static_cast<uint64_t>(packetType);
  m_pucCurBuffer += sizeof(uint64_t);
  *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = m_ulBufSize - sizeof(uint64_t) * 2;
  m_pucCurBuffer += sizeof(uint64_t);
  if (szName) {
    *reinterpret_cast<uint8_t *>(m_pucCurBuffer) = static_cast<uint8_t>(stNameBufLen);
#ifndef WIN32
    strncpy(reinterpret_cast<char *>(m_pucCurBuffer + 1), szName, stNameLen + 1);
#else
    strncpy_s(reinterpret_cast<char *>(m_pucCurBuffer + 1), stNameLen + 1, szName, stNameLen);
#endif
    m_pucCurBuffer += stNameBufLen;
  }
}

RPCSend::~RPCSend()
{
  if (m_pucBuffer)
    delete[] m_pucBuffer;
}

RPCSend &RPCSend::operator<<(OctaneEngine::Camera::CameraType const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(PanoramicCameraMode const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(StereoOutput const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(StereoMode const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(RenderPassId const &enumVal)
{
  uint32_t uiVal = static_cast<uint32_t>(enumVal);
  return this->operator<<(uiVal);
}

RPCSend &RPCSend::operator<<(HairInterpolationType const &enumVal)
{
  uint32_t uiVal = static_cast<uint32_t>(enumVal);
  return this->operator<<(uiVal);
}

RPCSend &RPCSend::operator<<(ImageType const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(Kernel::KernelType const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(OctaneEngine::InfoChannelType const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(Kernel::LayersMode const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(::Octane::AsPixelGroupMode const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(Kernel::DirectLightMode const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(Kernel::MBAlignmentType const &enumVal)
{
  int32_t iVal = static_cast<int32_t>(enumVal);
  return this->operator<<(iVal);
}

RPCSend &RPCSend::operator<<(SceneExportTypes::SceneExportTypesEnum const &enumVal)
{
  uint32_t uiVal = static_cast<uint32_t>(enumVal);
  return this->operator<<(uiVal);
}

RPCSend &RPCSend::operator<<(ComplexValue const &val)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(ComplexValue) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<ComplexValue *>(m_pucCurBuffer) = val;
    m_pucCurBuffer += sizeof(ComplexValue);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(float const &fVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<float *>(m_pucCurBuffer) = fVal;
    m_pucCurBuffer += sizeof(float);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(float_3 const &f3Val)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
    reinterpret_cast<float *>(m_pucCurBuffer)[0] = f3Val.x;
    reinterpret_cast<float *>(m_pucCurBuffer)[1] = f3Val.y;
    reinterpret_cast<float *>(m_pucCurBuffer)[2] = f3Val.z;
    m_pucCurBuffer += sizeof(float) * 3;
  }
  return *this;
}

RPCSend &RPCSend::operator<<(float_2 const &f2Val)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
    reinterpret_cast<float *>(m_pucCurBuffer)[0] = f2Val.x;
    reinterpret_cast<float *>(m_pucCurBuffer)[1] = f2Val.y;
    m_pucCurBuffer += sizeof(float) * 2;
  }
  return *this;
}

RPCSend &RPCSend::operator<<(double const &dVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(double) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<double *>(m_pucCurBuffer) = dVal;
    m_pucCurBuffer += sizeof(double);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(int64_t const &lVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(int64_t) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<int64_t *>(m_pucCurBuffer) = lVal;
    m_pucCurBuffer += sizeof(int64_t);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(uint64_t const &ulVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint64_t) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<uint64_t *>(m_pucCurBuffer) = ulVal;
    m_pucCurBuffer += sizeof(uint64_t);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(uint32_t const &uiVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<uint32_t *>(m_pucCurBuffer) = uiVal;
    m_pucCurBuffer += sizeof(uint32_t);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(int32_t const &iVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<int32_t *>(m_pucCurBuffer) = iVal;
    m_pucCurBuffer += sizeof(int32_t);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(bool const &bVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
    *reinterpret_cast<uint32_t *>(m_pucCurBuffer) = bVal;
    m_pucCurBuffer += sizeof(uint32_t);
  }
  return *this;
}

RPCSend &RPCSend::operator<<(char const *szVal)
{
  if (!szVal)
    return this->writeChar("");
  else
    return this->writeChar(szVal);
}

RPCSend &RPCSend::operator<<(string const &sVal)
{
  return this->writeChar(sVal.c_str());
}

bool RPCSend::writeBuffer(void *pvBuf, uint64_t ulLen)
{
  if (m_pucBuffer && (m_pucCurBuffer + ulLen <= m_pucBuffer + m_ulBufSize)) {
    memcpy(m_pucCurBuffer, pvBuf, static_cast<size_t>(ulLen));
    m_pucCurBuffer += ulLen;
    return true;
  }
  else
    return false;
}  // writeBuffer()

bool RPCSend::writeFloat3Buffer(float_3 *pf3Buf, uint64_t ulLen)
{
  if (m_pucBuffer && (m_pucCurBuffer + ulLen * sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
    register float *pfPtr = (float *)m_pucCurBuffer;
    for (register uint64_t i = 0; i < ulLen; ++i) {
      *(pfPtr++) = pf3Buf[i].x;
      *(pfPtr++) = pf3Buf[i].y;
      *(pfPtr++) = pf3Buf[i].z;
    }
    m_pucCurBuffer = (uint8_t *)pfPtr;
    return true;
  }
  else
    return false;
}  // writeFloat3Buffer()

bool RPCSend::writeFloat2Buffer(float_2 *pf2Buf, uint64_t ulLen)
{
  if (m_pucBuffer && (m_pucCurBuffer + ulLen * sizeof(float) * 2 <= m_pucBuffer + m_ulBufSize)) {
    register float *pfPtr = (float *)m_pucCurBuffer;
    for (register uint64_t i = 0; i < ulLen; ++i) {
      *(pfPtr++) = pf2Buf[i].x;
      *(pfPtr++) = pf2Buf[i].y;
    }
    m_pucCurBuffer = (uint8_t *)pfPtr;
    return true;
  }
  else
    return false;
}  // writeFloat2Buffer()

bool RPCSend::write()
{
  if (!m_pucBuffer)
    return false;

  unsigned int uiHeaderSize = sizeof(uint64_t) * 2;
  if (::send(m_Socket, (const char *)m_pucBuffer, uiHeaderSize, 0) < 0)
    return false;

  uint64_t ulDataBufSize = m_ulBufSize - uiHeaderSize;
  unsigned int uiChunksCnt = static_cast<unsigned int>(ulDataBufSize / SEND_CHUNK_SIZE);
  unsigned int uiLastChunkSize = ulDataBufSize % SEND_CHUNK_SIZE;
  for (unsigned int i = 0; i < uiChunksCnt; ++i) {
    if (::send(m_Socket,
               (const char *)m_pucBuffer + uiHeaderSize + i * SEND_CHUNK_SIZE,
               SEND_CHUNK_SIZE,
               0) < 0)
      return false;
  }
  if (uiLastChunkSize &&
      ::send(m_Socket,
             (const char *)m_pucBuffer + uiHeaderSize + uiChunksCnt * SEND_CHUNK_SIZE,
             uiLastChunkSize,
             0) < 0)
    return false;

  delete[] m_pucBuffer;
  m_pucBuffer = 0;
  m_ulBufSize = 0;
  m_pucCurBuffer = 0;

  return true;
}  // write()

bool RPCSend::writeFile(string const &path)
{
  if (!m_pucBuffer || !m_ulBufSize || !path.length())
    return false;
  bool bRet = false;
  uint8_t *pucBuf = 0;
  int64_t lFileSize = 0;

  FILE *hFile = ufopen(path.c_str(), "rb");
  if (!hFile)
    goto exit3;

#ifndef WIN32
  fseek(hFile, 0, SEEK_END);
  lFileSize = ftell(hFile);
#else
  _fseeki64(hFile, 0, SEEK_END);
  lFileSize = _ftelli64(hFile);
#endif
  rewind(hFile);

  reinterpret_cast<uint64_t *>(m_pucBuffer)[1] = lFileSize;
  if (::send(m_Socket, (const char *)m_pucBuffer, sizeof(uint64_t) * 2, 0) < 0)
    goto exit2;

  pucBuf = new uint8_t[lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize];
  while (pucBuf && lFileSize) {
    unsigned int uiSizeToRead = (lFileSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : lFileSize);

    if (!fread(pucBuf, uiSizeToRead, 1, hFile))
      goto exit1;

    if (::send(m_Socket, (const char *)pucBuf, uiSizeToRead, 0) < 0)
      goto exit1;

    lFileSize -= uiSizeToRead;
  }
  bRet = true;
exit1:
  if (pucBuf)
    delete[] pucBuf;
exit2:
  fclose(hFile);
exit3:
  delete[] m_pucBuffer;
  m_pucCurBuffer = m_pucBuffer = 0;
  m_PacketType = OctaneDataTransferObject::NONE;
  m_ulBufSize = 0;

  return bRet;
}  // writeFile()

RPCSend &RPCSend::writeChar(char const *szVal)
{
  if (m_pucBuffer) {
    size_t stLen = strlen(szVal);
    if (m_pucCurBuffer + stLen + 2 > m_pucBuffer + m_ulBufSize)
      return *this;
    if (stLen > 4096)
      stLen = 4096;
    *reinterpret_cast<uint8_t *>(m_pucCurBuffer) = static_cast<uint8_t>(stLen);
    m_pucCurBuffer += sizeof(uint8_t);
#ifndef WIN32
    strncpy(reinterpret_cast<char *>(m_pucCurBuffer), szVal, stLen + 1);
#else
    strncpy_s(reinterpret_cast<char *>(m_pucCurBuffer), stLen + 1, szVal, stLen);
#endif
    m_pucCurBuffer += stLen + 1;
  }
  return *this;
}

RPCReceive::RPCReceive(int socket) : m_Socket(socket), m_pucBuffer(0), m_pucCurBuffer(0)
{
  uint64_t ulTmp[2];
  if (::recv(socket, (char *)ulTmp, sizeof(uint64_t) * 2, MSG_WAITALL) != sizeof(uint64_t) * 2) {
    m_PacketType = OctaneDataTransferObject::NONE;
    m_ulBufSize = 0;
    return;
  }
  else {
    m_PacketType = static_cast<OctaneDataTransferObject::PacketType>(ulTmp[0]);
    m_ulBufSize = ulTmp[1];
  }

  if (m_PacketType < OctaneDataTransferObject::NONE ||
      m_PacketType > OctaneDataTransferObject::LAST_PACKET_TYPE) {
    m_PacketType = OctaneDataTransferObject::NONE;
    m_ulBufSize = 0;
    return;
  }

  if (m_ulBufSize > 0) {
    unsigned int uiChunksCnt = static_cast<unsigned int>(m_ulBufSize / SEND_CHUNK_SIZE);
    int iLastChunkSize = static_cast<int>(m_ulBufSize % SEND_CHUNK_SIZE);

    if (m_PacketType == OctaneDataTransferObject::LOAD_FILE) {
      m_pucCurBuffer = m_pucBuffer =
          new uint8_t[m_ulBufSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE : m_ulBufSize];
      if (!m_pucBuffer) {
        delete[] m_pucBuffer;
        m_pucCurBuffer = m_pucBuffer = 0;
        m_PacketType = OctaneDataTransferObject::NONE;
        m_ulBufSize = 0;
        return;
      }
    }
    else {
      m_pucCurBuffer = m_pucBuffer = new uint8_t[m_ulBufSize];
      for (unsigned int i = 0; i < uiChunksCnt; ++i) {
        if (::recv(
                socket, (char *)m_pucBuffer + i * SEND_CHUNK_SIZE, SEND_CHUNK_SIZE, MSG_WAITALL) !=
            SEND_CHUNK_SIZE) {
          delete[] m_pucBuffer;
          m_pucCurBuffer = m_pucBuffer = 0;
          m_PacketType = OctaneDataTransferObject::NONE;
          m_ulBufSize = 0;
          return;
        }
      }
      if (iLastChunkSize && ::recv(socket,
                                   (char *)m_pucBuffer + uiChunksCnt * SEND_CHUNK_SIZE,
                                   iLastChunkSize,
                                   MSG_WAITALL) != iLastChunkSize) {
        delete[] m_pucBuffer;
        m_pucCurBuffer = m_pucBuffer = 0;
        m_PacketType = OctaneDataTransferObject::NONE;
        m_ulBufSize = 0;
        return;
      }
    }
  }
  if (m_pucBuffer && m_PacketType >= OctaneDataTransferObject::FIRST_NAMED_PACKET &&
      m_PacketType <= OctaneDataTransferObject::LAST_NAMED_PACKET) {
    uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
    // m_pucCurBuffer += sizeof(uint8_t);

    m_szName = reinterpret_cast<char *>(m_pucCurBuffer + 1);
    m_pucCurBuffer += ucLen;
  }
}

RPCReceive::~RPCReceive()
{
  if (m_pucBuffer)
    delete[] m_pucBuffer;
}

bool RPCReceive::readFile(string &sPath, int *piErr)
{
  *piErr = 0;
  if (!m_pucBuffer || !m_ulBufSize || !sPath.length())
    return false;

  if (sPath[sPath.length() - 1] == '/' || sPath[sPath.length() - 1] == '\\')
    sPath.operator+=(m_szName);

  FILE *hFile = ufopen(sPath.c_str(), "wb");
  if (!hFile) {
    *piErr = errno;
    return false;
  }

  uint64_t ulCurSize = m_ulBufSize;
  while (ulCurSize) {
    int iSizeToRead = (ulCurSize > SEND_CHUNK_SIZE ? SEND_CHUNK_SIZE :
                                                     static_cast<int>(ulCurSize));
    if (::recv(m_Socket, (char *)m_pucBuffer, iSizeToRead, MSG_WAITALL) != iSizeToRead) {
      *piErr = errno;
      fclose(hFile);
      delete[] m_pucBuffer;
      m_pucCurBuffer = m_pucBuffer = 0;
      m_PacketType = OctaneDataTransferObject::NONE;
      m_ulBufSize = 0;
      return false;
    }
    fwrite(m_pucBuffer, iSizeToRead, 1, hFile);
    ulCurSize -= iSizeToRead;
  }
  delete[] m_pucBuffer;
  m_pucCurBuffer = m_pucBuffer = 0;
  m_PacketType = OctaneDataTransferObject::NONE;
  m_ulBufSize = 0;
  fclose(hFile);

  return true;
}  // readFile()

RPCReceive &RPCReceive::operator>>(float &fVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) <= m_pucBuffer + m_ulBufSize)) {
    fVal = *reinterpret_cast<float *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(float);
  }
  else
    fVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(ComplexValue &val)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(ComplexValue) <= m_pucBuffer + m_ulBufSize)) {
    val = *reinterpret_cast<ComplexValue *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(ComplexValue);
  }
  else {
    val.iType = 0;
    val.f3Value.x = 0;
    val.f3Value.y = 0;
    val.f3Value.z = 0;
  }
  return *this;
}

RPCReceive &RPCReceive::operator>>(float_3 &f3Val)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(float) * 3 <= m_pucBuffer + m_ulBufSize)) {
    f3Val.x = reinterpret_cast<float *>(m_pucCurBuffer)[0];
    f3Val.y = reinterpret_cast<float *>(m_pucCurBuffer)[1];
    f3Val.z = reinterpret_cast<float *>(m_pucCurBuffer)[2];
    m_pucCurBuffer += sizeof(float) * 3;
  }
  else {
    f3Val.x = 0;
    f3Val.y = 0;
    f3Val.z = 0;
  }
  return *this;
}

RPCReceive &RPCReceive::operator>>(double &dVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(double) <= m_pucBuffer + m_ulBufSize)) {
    dVal = *reinterpret_cast<double *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(double);
  }
  else
    dVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(bool &bVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
    bVal = (*reinterpret_cast<uint32_t *>(m_pucCurBuffer) != 0);
    m_pucCurBuffer += sizeof(uint32_t);
  }
  else
    bVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(int64_t &lVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(int64_t) <= m_pucBuffer + m_ulBufSize)) {
    lVal = *reinterpret_cast<int64_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(int64_t);
  }
  else
    lVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(uint64_t &ulVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint64_t) <= m_pucBuffer + m_ulBufSize)) {
    ulVal = *reinterpret_cast<uint64_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(uint64_t);
  }
  else
    ulVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(uint32_t &uiVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(uint32_t) <= m_pucBuffer + m_ulBufSize)) {
    uiVal = *reinterpret_cast<uint32_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(uint32_t);
  }
  else
    uiVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(RenderPassId &enumVal)
{
  uint32_t uiVal = static_cast<uint32_t>(enumVal);
  this->operator>>(uiVal);
  enumVal = static_cast<RenderPassId>(uiVal);
  return *this;
}

RPCReceive &RPCReceive::operator>>(int32_t &iVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + sizeof(int32_t) <= m_pucBuffer + m_ulBufSize)) {
    iVal = *reinterpret_cast<int32_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(int32_t);
  }
  else
    iVal = 0;
  return *this;
}

RPCReceive &RPCReceive::operator>>(char *&szVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
    uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(uint8_t);
    if (m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
      szVal = "";
      return *this;
    }
    szVal = reinterpret_cast<char *>(m_pucCurBuffer);
    m_pucCurBuffer += ucLen + 1;
  }
  else
    szVal = "";
  return *this;
}

RPCReceive &RPCReceive::operator>>(string &sVal)
{
  if (m_pucBuffer && (m_pucCurBuffer + 1 <= m_pucBuffer + m_ulBufSize)) {
    uint8_t ucLen = *reinterpret_cast<uint8_t *>(m_pucCurBuffer);
    m_pucCurBuffer += sizeof(uint8_t);
    if (m_pucCurBuffer + ucLen + 1 > m_pucBuffer + m_ulBufSize) {
      sVal = "";
      return *this;
    }
    sVal = reinterpret_cast<char *>(m_pucCurBuffer);
    m_pucCurBuffer += ucLen + 1;
  }
  else
    sVal = "";
  return *this;
}

void *RPCReceive::readBuffer(uint64_t ulLen)
{
  if (m_pucBuffer && (m_pucCurBuffer + ulLen <= m_pucBuffer + m_ulBufSize)) {
    void *pvRet = reinterpret_cast<void *>(m_pucCurBuffer);
    m_pucCurBuffer += ulLen;
    return pvRet;
  }
  else
    return 0;
}

bool RPCMsgPackObj::sendOctaneNode(int socket,
                                   std::string name,
                                   OctaneDataTransferObject::OctaneNodeBase *pNode)
{
  if (!pNode) {
    return false;
  }
  pNode->PackAttributes();
  msgpack::sbuffer sbuf;
  pNode->Serialize(sbuf);
  RPCSend snd(socket,
              sizeof(int32_t) + sizeof(uint32_t) + sbuf.size() + pNode->arraySize,
              OctaneDataTransferObject::LOAD_OCTANE_NODE,
              name.c_str());
  snd << static_cast<int32_t>(pNode->octaneType) << static_cast<uint32_t>(sbuf.size());
  snd.writeBuffer(sbuf.data(), sbuf.size());
  if (pNode->arraySize) {
    snd.writeBuffer(pNode->arrayData, pNode->arraySize);
  }
  return snd.write();
}

OctaneDataTransferObject::OctaneNodeBase *RPCMsgPackObj::receiveOctaneNode(int socket)
{
  RPCReceive rcv(socket);
  OctaneDataTransferObject::OctaneNodeBase *pNode = NULL;
  if (rcv.m_PacketType != OctaneDataTransferObject::LOAD_OCTANE_NODE) {
    return pNode;
  }
  int32_t octaneType;
  rcv >> octaneType;
  pNode = OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(octaneType);
  if (!pNode) {
    return pNode;
  }
  uint32_t nodeSize;
  rcv >> nodeSize;
  void *buf = rcv.readBuffer(nodeSize);
  if (buf) {
    msgpack::object_handle oh = msgpack::unpack(static_cast<char *>(buf),
                                                static_cast<size_t>(nodeSize));
    msgpack::object obj = oh.get();
    pNode->Deserialize(obj);
    if (pNode->arraySize) {
      pNode->arrayData = rcv.readBuffer(pNode->arraySize);
    }
  }
  if (pNode) {
    pNode->UnpackAttributes();
  }
  return pNode;
}

}  // namespace OctaneEngine
