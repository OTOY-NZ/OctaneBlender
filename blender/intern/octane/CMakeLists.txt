
set(OCTANE_INSTALL_PATH "scripts/addons/octane")
set(STARTUP_INSTALL_PATH "scripts/startup")

# External Libraries

include(cmake/external_libs.cmake)

# Build Flags

if(SUPPORT_SSE_BUILD)
	set(WITH_OCTANE_OPTIMIZED ON)
endif()

if(WIN32 AND MSVC)
	set(OCTANE_OPTIMIZED_FLAGS "/arch:SSE2 -D_CRT_SECURE_NO_WARNINGS /fp:fast /EHsc")
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /fp:fast -D_CRT_SECURE_NO_WARNINGS /EHsc")
	set(RTTI_DISABLE_FLAGS "/GR- -DBOOST_NO_RTTI -DBOOST_NO_TYPEID")
elseif(CMAKE_COMPILER_IS_GNUCC)
	set(OCTANE_OPTIMIZED_FLAGS "-ffast-math -msse -msse2 -msse3 -mfpmath=sse")
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffast-math")
	set(RTTI_DISABLE_FLAGS "-fno-rtti -DBOOST_NO_RTTI -DBOOST_NO_TYPEID")
endif()

# Definitions and Includes

add_definitions(${BOOST_DEFINITIONS} ${OPENIMAGEIO_DEFINITIONS})

add_definitions(-DOCT_NAMESPACE_BEGIN=namespace\ oct\ {)
add_definitions(-DOCT_NAMESPACE_END=})

if(WITH_OCTANE_OPTIMIZED)
	add_definitions(-DWITH_OCTANE_OPTIMIZED)
endif()

include_directories(
	SYSTEM
	${BOOST_INCLUDE_DIR}
	${OPENIMAGEIO_INCLUDE_DIRS}
	${OPENIMAGEIO_INCLUDE_DIRS}/OpenImageIO
	${OPENEXR_INCLUDE_DIR})

# Subdirectories

add_subdirectory(blender)
add_subdirectory(doc)

