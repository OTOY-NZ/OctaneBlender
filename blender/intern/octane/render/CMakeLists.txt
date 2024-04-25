
set(INC
	../blender/rpc/include
	..
	../../guardedalloc
	../../glew-mx
	../../../source/blender/makesdna
	../../../source/blender/makesrna
	../../../source/blender/blenlib
	../../../source/blender/gpu
  ../../../source/blender/blenkernel
	${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
  ${Epoxy_INCLUDE_DIRS}
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
	common_d3d.cpp
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
	octane_scatter.h
	common_d3d.hpp	

	kernel/kernel_types.h
	kernel/kernel_math.h
)

if(WIN32)
set(LIB
	d3d11.lib
	dxgi.lib 
)
else()
set(LIB
)
endif()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${RTTI_DISABLE_FLAGS}")

include_directories(${INC})
include_directories(SYSTEM ${INC_SYS})

add_definitions(${GL_DEFINITIONS})

octane_add_library(octane_render "${LIB}" ${SRC} ${SRC_HEADERS})
target_link_libraries(octane_render
  ${LIB}
)
