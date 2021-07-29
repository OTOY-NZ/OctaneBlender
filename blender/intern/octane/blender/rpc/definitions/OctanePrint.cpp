// clang-format off
#include "OctaneBase.h"
#include "OctaneNode.h"
#include "OctaneReflection.h"

namespace OctaneDataTransferObject {

	std::ostream& operator<< (std::ostream& out, const OctaneDTOBase& obj)
	{
		out << "Name: " << obj.sName << ", Type: " << obj.type << ", Use Socket: " << obj.bUseSocket << ", Use Link: " << obj.bUseLinked << ", Link Name: " << obj.sLinkNodeName << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOBool& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "bVal: " << obj.bVal << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.fVal << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat2& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.fVal.x << ", " << obj.fVal.y << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOFloat3& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.fVal.x << ", " << obj.fVal.y << ", " << obj.fVal.z << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTORGB& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.fVal.x << ", " << obj.fVal.y << ", " << obj.fVal.z << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOEnum& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "iVal: " << obj.iVal << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOInt& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "iVal: " << obj.iVal << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOInt2& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.iVal.x << ", " << obj.iVal.y << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOInt3& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "fVal: " << obj.iVal.x << ", " << obj.iVal.y << ", " << obj.iVal.z << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOString& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj) << "sVal: " << obj.sVal << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneDTOShader& obj)
	{
		out << static_cast<const OctaneDTOBase&>(obj);
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneNodeBase& obj){		
		out << "[" << obj.sName.c_str() << "]: " << "[" << obj.nodeType << "]" << std::endl;
		return out;
	}

	std::ostream& operator<< (std::ostream& out, const OctaneLightDirection& obj){
		out << static_cast<const OctaneNodeBase&>(obj);
		print_fields(obj, out);
		return out;
	}
}
// clang-format on