#include <stdlib.h>
#include <string>
#include <vector>
#include <unordered_set>
#include <memory>

enum OctaneResourceType {
  GEOMETRY = 0,
  OBJECT,
  MATERIAL,
  TEXTURE,
  LAST_TYPE = TEXTURE
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
