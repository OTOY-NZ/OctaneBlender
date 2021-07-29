
###########################################################################

set(GLEW_INCLUDE_DIR "${GLEW_INCLUDE_PATH}")

if(WITH_SYSTEM_GLEW)
	set(OCTANE_GLEW_LIBRARY ${GLEW_LIBRARY})
else()
	set(OCTANE_GLEW_LIBRARY extern_glew)
endif()
