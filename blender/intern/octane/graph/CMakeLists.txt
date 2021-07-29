
set(INC
	..
)

set(SRC
	node.cpp
	node_type.cpp
	node_xml.cpp
)

set(SRC_HEADERS
	node.h
	node_enum.h
	node_type.h
	node_xml.h
)

set(LIB

)

include_directories(${INC})
include_directories(SYSTEM ${INC_SYS})

octane_add_library(octane_graph "${LIB}" ${SRC} ${SRC_HEADERS})
