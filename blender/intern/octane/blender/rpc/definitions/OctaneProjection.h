// clang-format off
#ifndef __OCTANE_PROJECTION_H__
#define __OCTANE_PROJECTION_H__
#include "OctaneNode.h"

namespace OctaneDataTransferObject {

	struct OctaneXYZProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneXYZProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("XYZ Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_LINEAR, "ShaderNodeOctXYZProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneBoxProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneBoxProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Box Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_BOX, "ShaderNodeOctBoxProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneCylindricalProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneCylindricalProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Cylinder Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_CYLINDRICAL, "ShaderNodeOctCylProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctanePerspectiveProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctanePerspectiveProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Plane Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_PERSPECTIVE, "ShaderNodeOctPerspProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneSphericalProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOEnum)		iCoordinateSpace,
		(OctaneDTOShader)	sTransform
		)

		OctaneSphericalProjection() :
			iCoordinateSpace("coordinate_space_mode", false),
			sTransform("Sphere Transformation"),
			OctaneNodeBase(Octane::NT_PROJ_SPHERICAL, "ShaderNodeOctSphericalProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iCoordinateSpace, sTransform, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMeshProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iUVSet
		)

		OctaneMeshProjection() :
			iUVSet("UV set"),
			OctaneNodeBase(Octane::NT_PROJ_UVW, "ShaderNodeOctUVWProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iUVSet, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneTriplanarProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneTriplanarProjection() :
			OctaneNodeBase(Octane::NT_PROJ_TRIPLANAR, "ShaderNodeOctTriplanarProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

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

	struct OctaneSamplePosToUVProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneSamplePosToUVProjection() :
			OctaneNodeBase(Octane::NT_PROJ_SAMPLE_POSITION, "ShaderNodeOctSamplePosToUVProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneMatCapProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOInt)		iPlaceHolder
		)

		OctaneMatCapProjection() :
			OctaneNodeBase(Octane::NT_PROJ_MATCAP, "ShaderNodeOctMatCapProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(iPlaceHolder, MSGPACK_BASE(OctaneNodeBase));
	};

	struct OctaneColorToUVWProjection : public OctaneNodeBase {
		REFLECTABLE
		(		
		(OctaneDTOShader)	sTexture
		)

		OctaneColorToUVWProjection() :
			sTexture("Texture"),
			OctaneNodeBase(Octane::NT_PROJ_COLOR_TO_UVW, "ShaderNodeOctColorToUVWProjection")
		{
		}
		OCTANE_NODE_SERIALIZARION_FUNCTIONS
		OCTANE_NODE_VISIT_FUNCTIONS
		MSGPACK_DEFINE(sTexture, MSGPACK_BASE(OctaneNodeBase));
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
