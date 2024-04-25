#ifndef __BLENDER_OCTANEDB_H__
#define __BLENDER_OCTANEDB_H__

#include <stdio.h>
#include <mutex>
extern "C" {
#include "BKE_context.h"
}

#include "blender/rpc/definitions/OctaneNode.h"

OCT_NAMESPACE_BEGIN

struct GetOctaneDBJobData {
  bContext *context;
  std::mutex *mutex;
  char server_address[256];

  bool was_canceled;
  bool *stop;
  bool *do_update;
  float *progress;
};  // struct OctaneDBJobData

class BlenderOctaneDb {
 public:
  static bool generate_blender_material_from_octanedb(
      std::string name,
      OctaneDataTransferObject::OctaneDBNodes &dbNodes,
      GetOctaneDBJobData &jobData);
};

OCT_NAMESPACE_END

#endif /* __BLENDER_OCTANEDB_H__ */
