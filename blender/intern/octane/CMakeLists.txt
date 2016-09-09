
set(OCTANE_INSTALL_PATH "scripts/addons/octane")
set(STARTUP_INSTALL_PATH "scripts/startup")

# External Libraries

include(cmake/external_libs.cmake)

# Build Flags

if(WIN32 AND MSVC)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /fp:fast -D_CRT_SECURE_NO_WARNINGS /EHsc")
	set(RTTI_DISABLE_FLAGS "/GR- -DBOOST_NO_RTTI -DBOOST_NO_TYPEID")
elseif(APPLE)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffast-math -std=c++11 -stdlib=libc++")
	set(RTTI_DISABLE_FLAGS "-fno-rtti -DBOOST_NO_RTTI -DBOOST_NO_TYPEID")
elseif(CMAKE_COMPILER_IS_GNUCC)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffast-math")
	set(RTTI_DISABLE_FLAGS "-fno-rtti -DBOOST_NO_RTTI -DBOOST_NO_TYPEID -std=c++0x")
endif()

# Definitions and Includes

add_definitions(${BOOST_DEFINITIONS} ${OPENIMAGEIO_DEFINITIONS})

add_definitions(-DOCT_NAMESPACE_BEGIN=namespace\ oct\ {)
add_definitions(-DOCT_NAMESPACE_END=})

include_directories(
	SYSTEM
	${BOOST_INCLUDE_DIR}
	${OPENIMAGEIO_INCLUDE_DIRS}
	${OPENIMAGEIO_INCLUDE_DIRS}/OpenImageIO
	${PNG_INCLUDE_DIRS}
	${OPENEXR_INCLUDE_DIR})

# Subdirectories

add_subdirectory(blender)
add_subdirectory(doc)
