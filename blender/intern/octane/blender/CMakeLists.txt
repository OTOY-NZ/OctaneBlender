
set(INC
	.
	./render
	./server
	./util
	./subd
	../../guardedalloc
	../../../source/blender/makesdna
	../../../source/blender/makesrna
	../../../source/blender/blenloader
	../../../source/blender/blenlib
	${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
	${PYTHON_INCLUDE_DIRS}
	${GLEW_INCLUDE_PATH}
	${OPENGL_INCLUDE_DIR}
)

set(SRC
	blender_camera.cpp
	blender_mesh.cpp
	blender_object.cpp
	blender_python.cpp
	blender_session.cpp
	blender_shader.cpp
	blender_sync.cpp

	OCT_api.h
	blender_sync.h
	blender_session.h
	blender_util.h

	./server/server.cpp

	./server/server.h

	./render/environment.cpp
	./render/buffers.cpp
	./render/camera.cpp
	./render/graph.cpp
	./render/kernel.cpp
	./render/light.cpp
	./render/mesh.cpp
	./render/nodes.cpp
	./render/object.cpp
	./render/scene.cpp
	./render/session.cpp
	./render/shader.cpp

	./render/environment.h
	./render/buffers.h
	./render/camera.h
	./render/graph.h
	./render/kernel.h
	./render/light.h
	./render/mesh.h
	./render/nodes.h
	./render/object.h
	./render/scene.h
	./render/session.h
	./render/shader.h

	./util/util_path.cpp
	./util/util_string.cpp
	./util/util_time.cpp
	./util/util_transform.cpp
	./util/util_progress.cpp

	./util/util_hash.h
	./util/util_lists.h
	./util/util_math.h
	./util/util_opengl.h
	./util/util_path.h
	./util/util_progress.h
	./util/util_string.h
	./util/util_thread.h
	./util/util_time.h
	./util/util_transform.h
	./util/util_types.h
)

set(ADDON_FILES
	addon/__init__.py
	addon/engine.py 
	addon/types.py
	addon/presets.py
	addon/properties.py
	addon/ui.py
)

set(STARTUP_FILES
	addon/nodeitems_octane.py
)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${RTTI_DISABLE_FLAGS}")

add_definitions(-DGLEW_STATIC)

blender_add_lib(bf_intern_octane "${SRC}" "${INC}" "${INC_SYS}")

add_dependencies(bf_intern_octane bf_rna)

delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_FILES}" ${OCTANE_INSTALL_PATH})
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${STARTUP_FILES}" ${STARTUP_INSTALL_PATH})

