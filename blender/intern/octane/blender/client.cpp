#include "client.h"
#include "session.h"
#include "blender/server/octane_client.h"

OctaneClientBase::OctaneClientBase()
{
  client_ = new ::OctaneEngine::OctaneClient();
}

OctaneClientBase::~OctaneClientBase()
{
  delete client_;
}

bool OctaneClientBase::start_client()
{
  return oct::BlenderSession::connect_to_render_server(client_);
}

bool OctaneClientBase::is_alive()
{
  return client_ && client_->checkServerConnection();
}

std::string OctaneClientBase::utils_function(int32_t command, std::string data)
{
  std::string result;
  OctaneDataTransferObject::OctaneNodeBase *cur_node =
      OctaneDataTransferObject::GlobalOctaneNodeFactory.CreateOctaneNode(Octane::ENT_CUSTOM_NODE);
  OctaneDataTransferObject::OctaneCustomNode *cur_custom_node =
      (OctaneDataTransferObject::OctaneCustomNode *)cur_node;
  cur_custom_node->sCustomDataHeader = "[COMMAND]UTILS_FUNCTION";
  cur_custom_node->iOctaneNodeType = command;
  cur_custom_node->sCustomDataBody = data;
  std::vector<OctaneDataTransferObject::OctaneNodeBase *> response;
  client_->uploadOctaneNode(cur_custom_node, &response);
  if (response.size() == 1) {
    OctaneDataTransferObject::OctaneCustomNode *pCustomNode =
        (OctaneDataTransferObject::OctaneCustomNode *)(response[0]);
    result = pCustomNode->sCustomDataBody;
  }
  delete cur_node;
  for (auto pResponseNode : response) {
    delete pResponseNode;
  }
  return result;
}

OctaneClientManager::OctaneClientManager()
{
  reset();
}

OctaneClientManager::~OctaneClientManager()
{
  reset();
}

void OctaneClientManager::reset()
{
  for (auto &it : utils_clients_) {
    delete it.second;
  }
  utils_clients_.clear();
}

bool OctaneClientManager::start_utils_client(std::string name)
{
  OctaneClientBase *client = new OctaneClientBase();
  bool result = client->start_client();
  if (result) {
    utils_clients_[name] = client;    
  }
  else {
    if (client) {
      delete client;
    }    
  }
  return result;
}

bool OctaneClientManager::stop_utils_client(std::string name)
{
  if (utils_clients_.find(name) == utils_clients_.end()) {
    return false;
  }
  delete utils_clients_[name];
  utils_clients_.erase(name);
  return true;
}

std::string OctaneClientManager::utils_function(int32_t command_type,
                                         std::string data,
                                         std::string util_client_name)
{
  std::string result;
  if (util_client_name.length() && utils_clients_.find(util_client_name) != utils_clients_.end()) {
    result = utils_clients_[util_client_name]->utils_function(command_type, data);
  }
  else {
    // Use a temporal connection
    OctaneClientBase *client = new OctaneClientBase();
    if (client->start_client()) {
      result = client->utils_function(command_type, data);
    }    
    delete client;
  }
  return result;
}