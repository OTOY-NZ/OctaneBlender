#pragma once
#include <string>
#include <unordered_map>

namespace OctaneEngine {
class OctaneClient;
}

class OctaneClientBase {
 public:
  OctaneClientBase();
  virtual ~OctaneClientBase();
  bool start_client();
  bool is_alive();
  std::string utils_function(int32_t command, std::string data);

 private:
  OctaneEngine::OctaneClient *client_;
};

class OctaneClientManager {
 public:
  static OctaneClientManager &instance()
  {
    static OctaneClientManager instance;
    return instance;
  }
  void reset();
  bool start_utils_client(std::string name);
  bool stop_utils_client(std::string name);
  std::string utils_function(int32_t command_type, std::string data, std::string util_client_name);

 private:
  OctaneClientManager();
  ~OctaneClientManager();  
  OctaneClientManager(OctaneClientManager const &);
  OctaneClientManager &operator=(OctaneClientManager const &);

 private:
  std::unordered_map<std::string, OctaneClientBase*> utils_clients_;
};
