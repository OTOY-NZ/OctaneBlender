// clang-format off
#ifndef __OCTANE_TRANSFORM_H__
#define __OCTANE_TRANSFORM_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {
	struct OctaneValueTransform : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iOrder,
		(OctaneDTOFloat3)	fRotation,
		(OctaneDTOFloat3)	fScale,
		(OctaneDTOFloat3)	fTranslation
		)

		MatrixF oMatrix;
		bool	bUseMatrix;

		OctaneValueTransform() :
			iOrder("rotation_order", false),
			fRotation("Rotation"),
			fScale("Scale"),
			fTranslation("Translation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_VALUE, "ShaderNodeOctFullTransform")
		{
			bUseMatrix = false;
		}

    bool IsSameValue(const OctaneValueTransform& other) {
      return bUseMatrix == other.bUseMatrix
        && oMatrix == other.oMatrix
        && iOrder.IsSameValue(other.iOrder)
        && fRotation.IsSameValue(other.fRotation)
        && fScale.IsSameValue(other.fScale)
        && fTranslation.IsSameValue(other.fTranslation);
    }

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(iOrder, fRotation, fScale, fTranslation, oMatrix, bUseMatrix, MSGPACK_BASE(OctaneNodeBase));
	};
}

#endif
// clang-format on
