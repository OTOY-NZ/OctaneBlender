/*
 * Copyright 2011-2013 Blender Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __OSL_H__
#define __OSL_H__

#include "blender/rpc/definitions/OctanePinInfo.h"
#include <unordered_map>

namespace OctaneEngine {
class OctaneClient;
}

OCT_NAMESPACE_BEGIN

class OSLManager {
 public:
  static OSLManager &Instance()
  {
    static OSLManager s_Instance;
    return s_Instance;
  }
  bool record_osl(const std::string &identifier,
                  const OctaneDataTransferObject::OSLNodeInfo &node_info);
  bool query_osl(const std::string &identifier, OctaneDataTransferObject::OSLNodeInfo &node_info);
  void reset_osl()
  {
    m_oslNodeInfos.clear();
  }

 protected:
  OSLManager(void)
  {
    return;
  }
  ~OSLManager()
  {
    return;
  }

 private:
  std::unordered_map<std::string, OctaneDataTransferObject::OSLNodeInfo> m_oslNodeInfos;
  OSLManager(const OSLManager &)
  {
    return;
  }
  OSLManager &operator=(const OSLManager &)
  {
    return *this;
  }
};

OCT_NAMESPACE_END

#endif /* __OSL_H__ */
