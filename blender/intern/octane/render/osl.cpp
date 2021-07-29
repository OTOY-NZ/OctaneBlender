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

#include "render/osl.h"

OCT_NAMESPACE_BEGIN

bool OSLManager::record_osl(const std::string &identifier,
                            const OctaneDataTransferObject::OSLNodeInfo &node_info)
{
  m_oslNodeInfos[identifier] = node_info;
  return true;
}

bool OSLManager::query_osl(const std::string &identifier,
                           OctaneDataTransferObject::OSLNodeInfo &node_info)
{
  if (m_oslNodeInfos.find(identifier) != m_oslNodeInfos.end()) {
    node_info = m_oslNodeInfos[identifier];
    return true;
  }
  return false;
}

OCT_NAMESPACE_END
