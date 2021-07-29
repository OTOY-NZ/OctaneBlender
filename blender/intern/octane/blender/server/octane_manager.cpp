#include "octane_manager.h"

OctaneManager::OctaneManager()
{
  mSyncedResources.resize(OctaneResourceType::LAST_TYPE + 1);
}

OctaneManager::~OctaneManager()
{
  Reset();
}

void OctaneManager::Reset()
{
  for (int i = 0; i < mSyncedResources.size(); ++i) {
    mSyncedResources[i].clear();
  }
  mResharpableCandidates.clear();
  mMovableCandidates.clear();
}

bool OctaneManager::IsResourceSynced(std::string name, OctaneResourceType type)
{
  return mSyncedResources[type].find(name) != mSyncedResources[type].end();
}

void OctaneManager::SyncedResource(std::string name, OctaneResourceType type)
{
  mSyncedResources[type].insert(name);
}

void OctaneManager::UnsyncedResource(std::string name, OctaneResourceType type)
{
  if (mSyncedResources[type].find(name) != mSyncedResources[type].end()) {
    mSyncedResources[type].erase(name);
  }
}

bool OctaneManager::IsResharpableCandidate(std::string name)
{
  return mResharpableCandidates.find(name) != mResharpableCandidates.end();
}

bool OctaneManager::IsMovableCandidate(std::string name)
{
  return mMovableCandidates.find(name) != mMovableCandidates.end();
}

void OctaneManager::TagResharpableCandidate(std::string name)
{
  mResharpableCandidates.insert(name);
}

void OctaneManager::TagMovableCandidate(std::string name)
{
  mMovableCandidates.insert(name);
}

void OctaneManager::UntagResharpableCandidate(std::string name)
{
  if (mResharpableCandidates.find(name) != mResharpableCandidates.end()) {
    mResharpableCandidates.erase(name);  
  }
}

void OctaneManager::UntagMovableCandidate(std::string name)
{
  if (mMovableCandidates.find(name) != mMovableCandidates.end()) {
    mMovableCandidates.erase(name);
  }
}