set(INC
	./rpc/include
	..
	../../glew-mx
	../../guardedalloc
	../../mikktspace
	../../../source/blender/makesdna
	../../../source/blender/makesrna
	../../../source/blender/blenlib
	../../../source/blender/blentranslation  
	../../../source/blender/blenkernel
  ../../../source/blender/depsgraph
  ../../../source/blender/windowmanager
  ../../../source/blender/render/intern/include
  ../../../source/blender/render/extern/include  
	${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
	${PYTHON_INCLUDE_DIRS}
	${BOOST_INCLUDE_DIR}
	${GLEW_INCLUDE_DIR}
)

set(SRC
	blender_python.cpp
	blender_session.cpp
	blender_sync.cpp
	blender_camera.cpp
	blender_object.cpp
	blender_mesh.cpp
	blender_shader.cpp
	blender_hair.cpp
	blender_octanedb.cpp

	blender_octanedb.h
	blender_sync.h
	blender_session.h
	blender_util.h
	OCT_api.h
	
	./server/octane_client.h
	./server/octane_data_type.h
	./server/octane_network_const.h
	./server/octane_network.h
  ./server/octane_manager.h
	./server/octane_network.cpp
	./server/octane_client.cpp
  ./server/octane_manager.cpp

	./rpc/definitions/OctaneNode.h
	./rpc/definitions/OctaneTransform.h
	./rpc/definitions/OctaneProjection.h
	./rpc/definitions/OctanePinInfo.h
	./rpc/definitions/OctaneMesh.h
	./rpc/definitions/OctaneNodeFactory.h
	./rpc/definitions/OctaneNodeFactory.cpp
)

set(LIB
  bf_render
	octane_graph
	octane_render	
	octane_util  
)

if(WITH_OCTANE_LOGGING)
	list(APPEND LIB
		extern_glog
	)
endif()

set(ADDON_FILES
	addon/__init__.py
	addon/engine.py
	addon/operators.py
	addon/presets.py
	addon/properties.py
	addon/ui.py
	addon/nodeitems_octane.py
	addon/osl.py
  addon/version_update.py
  addon/converters.py
)

set(STARTUP_FILES
	addon/nodeitems_octane.py
)

set(OBJECT_LIBRARY
	addon/libraries/objects/Circle.obj
	addon/libraries/objects/Square.obj	
)

set(ORBX_LIBRARY
	addon/libraries/orbx/CameraData.orbx
)

add_definitions(${GL_DEFINITIONS} ${BOOST_DEFINITIONS})

if(WIN32)
	add_compile_options(-bigobj)
endif()

blender_add_lib(bf_intern_octane "${SRC}" "${INC}" "${INC_SYS}" "${LIB}")

# avoid link failure with clang 3.4 debug
if(CMAKE_C_COMPILER_ID MATCHES "Clang" AND NOT ${CMAKE_C_COMPILER_VERSION} VERSION_LESS '3.4')
	set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -gline-tables-only")
endif()

add_dependencies(bf_intern_octane bf_rna)

delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_FILES}" ${OCTANE_INSTALL_PATH})
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${OBJECT_LIBRARY}" ${OCTANE_INSTALL_PATH}/libraries/objects)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ORBX_LIBRARY}" ${OCTANE_INSTALL_PATH}/libraries/orbx)
