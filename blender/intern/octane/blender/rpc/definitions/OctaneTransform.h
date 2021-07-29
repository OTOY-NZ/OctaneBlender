// clang-format off
#ifndef __OCTANE_TRANSFORM_H__
#define __OCTANE_TRANSFORM_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {

	struct OctaneRotationTransform : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iOrder,
		(OctaneDTOFloat3)	fRotation
		)

		OctaneRotationTransform() :
			iOrder("rotation_order", false),
			fRotation("Rotation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_ROTATION, "ShaderNodeOctRotateTransform")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iOrder, fRotation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScaleTransform : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOFloat3)	fScale
		)

		OctaneScaleTransform() :
			fScale("Scale"),
			OctaneNodeBase(Octane::NT_TRANSFORM_SCALE, "ShaderNodeOctScaleTransform")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fScale, MSGPACK_BASE(OctaneNodeBase));
	};

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
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		OCTANE_NODE_POST_UPDATE_FUNCTIONS
		MSGPACK_DEFINE(iOrder, fRotation, fScale, fTranslation, oMatrix, bUseMatrix, MSGPACK_BASE(OctaneNodeBase));
	};

	struct Octane2DTransform : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOFloat2)	fRotation,
		(OctaneDTOFloat2)	fScale,
		(OctaneDTOFloat2)	fTranslation
		)

		Octane2DTransform() :
			fRotation("Rotation"),
			fScale("Scale"),
			fTranslation("Translation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_2D, "ShaderNodeOct2DTransform")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fRotation, fScale, fTranslation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct Octane3DTransform : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iOrder,
		(OctaneDTOFloat3)	fRotation,
		(OctaneDTOFloat3)	fScale,
		(OctaneDTOFloat3)	fTranslation
		)

		Octane3DTransform() :
			iOrder("rotation_order", false),
			fRotation("Rotation"),
			fScale("Scale"),
			fTranslation("Translation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_3D, "ShaderNodeOct3DTransform")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iOrder, fRotation, fScale, fTranslation, MSGPACK_BASE(OctaneNodeBase));
	};

}

#endif
// clang-format on
