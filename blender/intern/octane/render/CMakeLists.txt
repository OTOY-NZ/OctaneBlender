
set(INC
	../blender/rpc/include
	..
	../../glew-mx
	../../../source/blender/makesdna
	../../../source/blender/makesrna
	../../../source/blender/blenlib
	${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
	${GLEW_INCLUDE_DIR}
)

set(SRC
	graph.cpp
	buffers.cpp
	camera.cpp
	environment.cpp
	kernel.cpp
	light.cpp
	mesh.cpp
	object.cpp
	passes.cpp
	scene.cpp
	session.cpp
	shader.cpp
  osl.cpp
	particles.cpp
)

set(SRC_HEADERS
	graph.h
	buffers.h
	camera.h
	environment.h
	kernel.h
	light.h
	mesh.h
	object.h
	passes.h
	scene.h
	session.h
	shader.h
  osl.h
	particles.h

	kernel/kernel_types.h
	kernel/kernel_math.h
)

set(LIB

)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${RTTI_DISABLE_FLAGS}")

include_directories(${INC})
include_directories(SYSTEM ${INC_SYS})

add_definitions(${GL_DEFINITIONS})

octane_add_library(octane_render "${LIB}" ${SRC} ${SRC_HEADERS})
