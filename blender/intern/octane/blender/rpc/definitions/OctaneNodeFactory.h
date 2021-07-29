// clang-format off
#ifndef __OCTANE_NODE_FACTORY_H__
#define __OCTANE_NODEFACTORY_H__
#include <memory>
#include "OctaneNode.h"
#include "OctaneProjection.h"
#include "OctaneTransform.h"

namespace OctaneDataTransferObject {
	typedef std::unordered_map<int, OctaneNodeBase*(*)()> OctaneNodeBaseCreatorMap;

	template<typename T>
	OctaneNodeBase* createOctaneNodeInstance();

	class OctaneNodeFactory {
	private:
		std::unordered_map<int, std::string> octaneToPluginTypeMap;
		std::unordered_map<std::string, int> pluginToOctaneTypeMap;
		OctaneNodeBaseCreatorMap creatorsMap;
	public:
		OctaneNodeFactory();
		int GetOctaneNodeType(const std::string &pluginType);
		OctaneNodeBase* CreateOctaneNode(const std::string &pluginType);
		OctaneNodeBase* CreateOctaneNode(int octaneType);
	};

	static OctaneNodeFactory GlobalOctaneNodeFactory;
}

#endif
// clang-format on
