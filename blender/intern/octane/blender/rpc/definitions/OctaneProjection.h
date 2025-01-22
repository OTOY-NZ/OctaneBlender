// clang-format off
#ifndef __OCTANE_PROJECTION_H__
#define __OCTANE_PROJECTION_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {
	struct OctaneOSLUVProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneOSLUVProjection() :
			OctaneNodeBase(Octane::NT_PROJ_OSL_UV, "ShaderNodeOctOSLUVProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneDistortedMeshUVProjection : public OctaneNodeBase{
		REFLECTABLE
		(
		(OctaneDTOFloat)	fRotation,
		(OctaneDTOFloat2)	f2RotationRange,
		(OctaneDTOFloat)	fScale,
		(OctaneDTOFloat2)	f2ScaleRange,
		(OctaneDTOFloat)	fTranslation,
		(OctaneDTOFloat2)	f2TranslationRange
		)

		OctaneDistortedMeshUVProjection() :
			fRotation("Rotation"),
			f2RotationRange("Rotation range"),
			fScale("Scale"),
			f2ScaleRange("Scale range"),
			fTranslation("Translation"),
			f2TranslationRange("Translation range"),
			OctaneNodeBase(Octane::NT_PROJ_DISTORTED_MESH_UV, "ShaderNodeOctDistortedMeshUVProjection")
		{
		}

		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(fRotation, f2RotationRange, fScale, f2ScaleRange,
			fTranslation, f2TranslationRange, MSGPACK_BASE(OctaneNodeBase));
	};
}

#endif
// clang-format on
