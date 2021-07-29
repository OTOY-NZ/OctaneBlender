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
  short *stop;
  short *do_update;
  float *progress;
};  // struct OctaneDBJobData

class BlenderOctaneDb {
 public:
  static bool generate_blender_material_from_octanedb(
      std::string name,
      std::vector<OctaneDataTransferObject::OctaneNodeBase *> &octaneNodes,
      GetOctaneDBJobData &jobData);
};

OCT_NAMESPACE_END

#endif /* __BLENDER_OCTANEDB_H__ */
