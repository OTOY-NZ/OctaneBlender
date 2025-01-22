#include <memory>
#include <stdlib.h>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

enum OctaneResourceType { GEOMETRY = 0, OBJECT, MATERIAL, TEXTURE, LAST_TYPE = TEXTURE };

struct PinInfo {
  std::string blender_name_;
  int32_t id_;
  std::string name_;
  int32_t index_;
  int32_t pin_type_;
  int32_t socket_type_;
  int32_t default_node_type_;
  std::string default_node_name_;
  bool use_as_legacy_attribute_;
};

struct AttributeInfo {
  std::string blender_name_;
  int32_t id_;
  std::string name_;
  int32_t attribute_type_;
};

struct LegacyDataInfo {
  std::string name_;
  bool is_socket_;
  int32_t data_type_;
  bool is_pin_;
  int32_t octane_type_;
  bool is_internal_data_;
  bool is_internal_data_pin_;
  int32_t internal_data_octane_type_;
};

typedef std::shared_ptr<PinInfo> PinInfoPtr;
typedef std::shared_ptr<AttributeInfo> AttributeInfoPtr;
typedef std::shared_ptr<LegacyDataInfo> LegacyDataInfoPtr;
typedef std::unordered_map<int32_t, PinInfoPtr> PinIdInfoMap;
typedef std::unordered_map<std::string, PinInfoPtr> PinNameInfoMap;
typedef std::unordered_map<int32_t, AttributeInfoPtr> AttributeIdInfoMap;
typedef std::unordered_map<std::string, AttributeInfoPtr> AttributeNameInfoMap;
typedef std::unordered_map<int32_t, LegacyDataInfoPtr> LegacyDataInfoIdMap;
typedef std::unordered_map<std::string, LegacyDataInfoPtr> LegacyDataInfoBlenderNameMap;

class OctaneInfo {
 public:
  static OctaneInfo &instance()
  {
    static OctaneInfo instance;
    return instance;
  }

  static const int32_t INVALID_NODE_TYPE = 0;

  void add_node_name(int32_t node_type, std::string node_name);
  void add_legacy_node_name(int32_t node_type, std::string node_name);
  void add_attribute_info(int32_t node_type,
                          std::string blender_name,
                          int32_t attribute_id,
                          std::string attribute_name,
                          int32_t attribute_type);
  void add_pin_info(int32_t node_type,
                    std::string blender_name,
                    int32_t pin_id,
                    std::string pin_name,
                    int32_t pin_index,
                    int32_t pin_type,
                    int32_t socket_type,
                    int32_t default_node_type,
                    std::string default_node_name);
  void add_legacy_data_info(int32_t node_type,
                            std::string name,
                            bool is_socket,
                            int32_t socket_data_type,
                            bool is_pin,
                            int32_t octane_type,
                            bool is_internal_data,
                            bool is_internal_data_pin,
                            int32_t internal_data_octane_type);
  void set_static_pin_count(int32_t node_type, int32_t pin_count);
  bool need_to_use_new_custom_node(std::string node_bl_idname);
  const LegacyDataInfoPtr get_legacy_data_info(int32_t node_type, int32_t octane_id, bool is_pin);


  const PinIdInfoMap &get_pin_id_info_map(int32_t node_type)
  {
    return pin_id_to_pin_info_[node_type];
  }

  const PinNameInfoMap &get_pin_name_info_map(int32_t node_type)
  {
    return pin_name_to_pin_info_[node_type];
  }

  const AttributeIdInfoMap &get_attribute_id_info_map(int32_t node_type)
  {
    return attribute_id_to_attribute_info_[node_type];
  }

  const AttributeNameInfoMap &get_attribute_name_info_map(int32_t node_type)
  {
    return attribute_name_to_attribute_info_[node_type];
  }

  const LegacyDataInfoIdMap &get_legacy_data_info_id_map(int32_t node_type)
  {
    return octane_id_to_legacy_data_info_[node_type];
  }

  const LegacyDataInfoBlenderNameMap &get_legacy_data_info_blender_name_map(int32_t node_type)
  {
    return blender_name_to_legacy_data_info_[node_type];
  }

  int32_t get_node_type(std::string name)
  {
    if (node_name_to_type_.find(name) != node_name_to_type_.end()) {
      return node_name_to_type_[name];
    }
    return INVALID_NODE_TYPE;
  }

  int32_t get_legacy_node_type(std::string name)
  {
    if (legacy_node_name_to_type_.find(name) != legacy_node_name_to_type_.end()) {
      return legacy_node_name_to_type_[name];
    }
    return INVALID_NODE_TYPE;
  }

  std::string get_node_name(int32_t type)
  {
    if (node_type_to_name_.find(type) != node_type_to_name_.end()) {
      return node_type_to_name_[type];
    }
    return "";
  }

  int32_t get_static_pin_count(int32_t type)
  {
    return node_type_to_static_pin_count_[type];
  }

 private:
  OctaneInfo();
  ~OctaneInfo();
  void reset();
  OctaneInfo(OctaneInfo const &);
  OctaneInfo &operator=(OctaneInfo const &);

 private:
  std::unordered_map<int32_t, std::string> node_type_to_name_;
  std::unordered_map<int32_t, std::string> legacy_node_type_to_name_;
  std::unordered_map<int32_t, int32_t> node_type_to_static_pin_count_;
  std::unordered_map<std::string, int32_t> node_name_to_type_;
  std::unordered_map<std::string, int32_t> legacy_node_name_to_type_;
  std::unordered_map<int32_t, PinIdInfoMap> pin_id_to_pin_info_;
  std::unordered_map<int32_t, PinNameInfoMap> pin_name_to_pin_info_;
  std::unordered_map<int32_t, AttributeIdInfoMap> attribute_id_to_attribute_info_;
  std::unordered_map<int32_t, AttributeNameInfoMap> attribute_name_to_attribute_info_;
  std::unordered_map<int32_t, LegacyDataInfoIdMap> octane_id_to_legacy_data_info_;
  std::unordered_map<int32_t, LegacyDataInfoBlenderNameMap> blender_name_to_legacy_data_info_;
  std::unordered_set<std::string> need_new_custom_node_legacy_names_;
};

class OctaneManager {
 public:
  static OctaneManager &getInstance()
  {
    static OctaneManager instance;
    return instance;
  }

  void Reset();
  bool IsResharpableCandidate(std::string name);
  bool IsMovableCandidate(std::string name);
  void TagResharpableCandidate(std::string name);
  void TagMovableCandidate(std::string name);
  void UntagResharpableCandidate(std::string name);
  void UntagMovableCandidate(std::string name);
  bool IsResourceSynced(std::string name, OctaneResourceType type);
  void SyncedResource(std::string name, OctaneResourceType type);
  void UnsyncedResource(std::string name, OctaneResourceType type);

 private:
  OctaneManager();
  ~OctaneManager();
  OctaneManager(OctaneManager const &);
  OctaneManager &operator=(OctaneManager const &);

 private:
  std::vector<std::unordered_set<std::string>> mSyncedResources;
  std::unordered_set<std::string> mResharpableCandidates;
  std::unordered_set<std::string> mMovableCandidates;
};
