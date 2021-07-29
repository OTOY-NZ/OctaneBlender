// clang-format off
#ifndef __OCTANE_PROJECTION_H__
#define __OCTANE_PROJECTION_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {

	struct OctaneXYZProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_XYZ;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneXYZProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("XYZ Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_LINEAR)
		{
		}
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneBoxProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_BOX;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneBoxProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Box Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_BOX)
		{
		}
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCylindricalProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_CYL;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneCylindricalProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Cylinder Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_CYLINDRICAL)
		{
		}
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctanePerspectiveProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_PERSP;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctanePerspectiveProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Plane Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_PERSPECTIVE)
		{
		}
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSphericalProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_SPHERICAL;

		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneSphericalProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Sphere Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_SPHERICAL)
		{
		}
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_UVW;

		REFLECTABLE
		(		
		(OctaneDTOInt)		iUVSet
		)

		OctaneMeshProjection() :
			iUVSet("UV set"),
			OctaneNodeBase(Octane::NT_PROJ_UVW)
		{
		}
		MSGPACK_DEFINE(iUVSet, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriplanarProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_TRIPLANAR;

		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneTriplanarProjection() :
			OctaneNodeBase(Octane::NT_PROJ_TRIPLANAR)
		{
		}
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneOSLUVProjection : public OctaneNodeBase {
		const static PacketType packetType = LOAD_PROJECTION_OSL_UV;

		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneOSLUVProjection() :
			OctaneNodeBase(Octane::NT_PROJ_OSL_UV)
		{
		}
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};
}

#endif
// clang-format on
