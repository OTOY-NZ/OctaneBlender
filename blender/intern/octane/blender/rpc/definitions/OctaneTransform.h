// clang-format off
#ifndef __OCTANE_TRANSFORM_H__
#define __OCTANE_TRANSFORM_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {

	struct OctaneRotationTransform : public OctaneNodeBase {
		const static PacketType packetType = LOAD_ROTATION_TRANSFORM;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iOrder,
		(OctaneDTOFloat3)	fRotation
		)

		OctaneRotationTransform() :
			iOrder("rotation_order", false),
			fRotation("Rotation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_ROTATION)
		{
		}
		MSGPACK_DEFINE(iOrder, fRotation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneScaleTransform : public OctaneNodeBase {
		const static PacketType packetType = LOAD_SCALE_TRANSFORM;

		REFLECTABLE
		(		
		(OctaneDTOFloat3)	fScale
		)

		OctaneScaleTransform() :
			fScale("Scale"),
			OctaneNodeBase(Octane::NT_TRANSFORM_SCALE)
		{
		}
		MSGPACK_DEFINE(fScale, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneValueTransform : public OctaneNodeBase {
		const static PacketType packetType = LOAD_VALUE_TRANSFORM;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iOrder,
		(OctaneDTOFloat3)	fRotation,
		(OctaneDTOFloat3)	fScale,
		(OctaneDTOFloat3)	fTranslation
		)

		OctaneValueTransform() :
			iOrder("rotation_order", false),
			fRotation("Rotation"),
			fScale("Scale"),
			fTranslation("Translation"),
			OctaneNodeBase(Octane::NT_TRANSFORM_VALUE)
		{
		}
		MSGPACK_DEFINE(iOrder, fRotation, fScale, fTranslation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct Octane2DTransform : public OctaneNodeBase {
		const static PacketType packetType = LOAD_2D_TRANSFORM;

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
			OctaneNodeBase(Octane::NT_TRANSFORM_2D)
		{
		}
		MSGPACK_DEFINE(fRotation, fScale, fTranslation, MSGPACK_BASE(OctaneNodeBase));
	};

	struct Octane3DTransform : public OctaneNodeBase {
		const static PacketType packetType = LOAD_3D_TRANSFORM;

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
			OctaneNodeBase(Octane::NT_TRANSFORM_3D)
		{
		}
		MSGPACK_DEFINE(iOrder, fRotation, fScale, fTranslation, MSGPACK_BASE(OctaneNodeBase));
	};

}

#endif
// clang-format on
