set(OCTANE_INSTALL_PATH "scripts/addons/octane")
set(STARTUP_INSTALL_PATH "scripts/startup")

# External Libraries

include(cmake/external_libs.cmake)
include(cmake/macros.cmake)

# Build Flags
# todo: this code could be refactored a bit to avoid duplication
# note: CXX_HAS_SSE is needed in case passing SSE flags fails altogether (gcc-arm)

if(WITH_OCTANE_NATIVE_ONLY)
  set(CXX_HAS_SSE FALSE)
  set(CXX_HAS_AVX FALSE)
  set(CXX_HAS_AVX2 FALSE)
  add_definitions(
    -DWITH_KERNEL_NATIVE
  )

  if(NOT MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
    set(OCTANE_KERNEL_FLAGS "-march=native")
  endif()
elseif(NOT WITH_CPU_SSE)
  set(CXX_HAS_SSE FALSE)
  set(CXX_HAS_AVX FALSE)
  set(CXX_HAS_AVX2 FALSE)
elseif(WIN32 AND MSVC AND NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  set(CXX_HAS_SSE TRUE)
  set(CXX_HAS_AVX TRUE)
  set(CXX_HAS_AVX2 TRUE)

  # /arch:AVX for VC2012 and above
  if(NOT MSVC_VERSION LESS 1700)
    set(OCTANE_AVX_ARCH_FLAGS "/arch:AVX")
    set(OCTANE_AVX2_ARCH_FLAGS "/arch:AVX /arch:AVX2")
  elseif(NOT CMAKE_CL_64)
    set(OCTANE_AVX_ARCH_FLAGS "/arch:SSE2")
    set(OCTANE_AVX2_ARCH_FLAGS "/arch:SSE2")
  endif()

  # Unlike GCC/clang we still use fast math, because there is no fine
  # grained control and the speedup we get here is too big to ignore.
  set(OCTANE_KERNEL_FLAGS "/fp:fast -D_CRT_SECURE_NO_WARNINGS /GS-")

  # there is no /arch:SSE3, but intrinsics are available anyway
  if(CMAKE_CL_64)
    set(OCTANE_SSE2_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_SSE3_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_SSE41_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_AVX_KERNEL_FLAGS "${OCTANE_AVX_ARCH_FLAGS} ${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_AVX2_KERNEL_FLAGS "${OCTANE_AVX2_ARCH_FLAGS} ${OCTANE_KERNEL_FLAGS}")
  else()
    set(OCTANE_SSE2_KERNEL_FLAGS "/arch:SSE2 ${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_SSE3_KERNEL_FLAGS "/arch:SSE2 ${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_SSE41_KERNEL_FLAGS "/arch:SSE2 ${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_AVX_KERNEL_FLAGS "${OCTANE_AVX_ARCH_FLAGS} ${OCTANE_KERNEL_FLAGS}")
    set(OCTANE_AVX2_KERNEL_FLAGS "${OCTANE_AVX2_ARCH_FLAGS} ${OCTANE_KERNEL_FLAGS}")
  endif()

  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OCTANE_KERNEL_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Ox")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO} /Ox")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL} /Ox")
elseif(CMAKE_COMPILER_IS_GNUCC OR (CMAKE_CXX_COMPILER_ID MATCHES "Clang"))
  check_cxx_compiler_flag(-msse CXX_HAS_SSE)
  check_cxx_compiler_flag(-mavx CXX_HAS_AVX)
  check_cxx_compiler_flag(-mavx2 CXX_HAS_AVX2)

  # Assume no signal trapping for better code generation.
  set(OCTANE_KERNEL_FLAGS "-fno-trapping-math")
  # Avoid overhead of setting errno for NaNs.
  set(OCTANE_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -fno-math-errno")
  # Let compiler optimize 0.0 - x without worrying about signed zeros.
  set(OCTANE_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -fno-signed-zeros")

  if(CMAKE_COMPILER_IS_GNUCC)
    # Assume no signal trapping for better code generation.
    set(OCTANE_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -fno-signaling-nans")
    # Assume a fixed rounding mode for better constant folding.
    set(OCTANE_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -fno-rounding-math")
  endif()

  if(CXX_HAS_SSE)
    if(CMAKE_COMPILER_IS_GNUCC)
      set(OCTANE_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -mfpmath=sse")
    endif()

    set(OCTANE_SSE2_KERNEL_FLAGS "${OCTANE_KERNEL_FLAGS} -msse -msse2")
    set(OCTANE_SSE3_KERNEL_FLAGS "${OCTANE_SSE2_KERNEL_FLAGS} -msse3 -mssse3")
    set(OCTANE_SSE41_KERNEL_FLAGS "${OCTANE_SSE3_KERNEL_FLAGS} -msse4.1")
    if(CXX_HAS_AVX)
      set(OCTANE_AVX_KERNEL_FLAGS "${OCTANE_SSE41_KERNEL_FLAGS} -mavx")
    endif()
    if(CXX_HAS_AVX2)
      set(OCTANE_AVX2_KERNEL_FLAGS "${OCTANE_SSE41_KERNEL_FLAGS} -mavx -mavx2 -mfma -mlzcnt -mbmi -mbmi2 -mf16c")
    endif()
  endif()

  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OCTANE_KERNEL_FLAGS}")
elseif(WIN32 AND CMAKE_CXX_COMPILER_ID MATCHES "Intel")
  check_cxx_compiler_flag(/QxSSE2 CXX_HAS_SSE)
  check_cxx_compiler_flag(/arch:AVX CXX_HAS_AVX)
  check_cxx_compiler_flag(/QxCORE-AVX2 CXX_HAS_AVX2)

  if(CXX_HAS_SSE)
    set(OCTANE_SSE2_KERNEL_FLAGS "/QxSSE2")
    set(OCTANE_SSE3_KERNEL_FLAGS "/QxSSSE3")
    set(OCTANE_SSE41_KERNEL_FLAGS "/QxSSE4.1")

    if(CXX_HAS_AVX)
      set(OCTANE_AVX_KERNEL_FLAGS "/arch:AVX")
    endif()

    if(CXX_HAS_AVX2)
      set(OCTANE_AVX2_KERNEL_FLAGS "/QxCORE-AVX2")
    endif()
  endif()
elseif(CMAKE_CXX_COMPILER_ID MATCHES "Intel")
  if(APPLE)
    # ICC does not support SSE2 flag on MacOSX
    check_cxx_compiler_flag(-xssse3 CXX_HAS_SSE)
  else()
    check_cxx_compiler_flag(-xsse2 CXX_HAS_SSE)
  endif()

  check_cxx_compiler_flag(-xavx CXX_HAS_AVX)
  check_cxx_compiler_flag(-xcore-avx2 CXX_HAS_AVX2)

  if(CXX_HAS_SSE)
    if(APPLE)
      # ICC does not support SSE2 flag on MacOSX
      set(OCTANE_SSE2_KERNEL_FLAGS "-xssse3")
    else()
      set(OCTANE_SSE2_KERNEL_FLAGS "-xsse2")
    endif()

    set(OCTANE_SSE3_KERNEL_FLAGS "-xssse3")
    set(OCTANE_SSE41_KERNEL_FLAGS "-xsse4.1")

    if(CXX_HAS_AVX)
      set(OCTANE_AVX_KERNEL_FLAGS "-xavx")
    endif()

    if(CXX_HAS_AVX2)
      set(OCTANE_AVX2_KERNEL_FLAGS "-xcore-avx2")
    endif()
  endif()
endif()

if(CXX_HAS_SSE)
  add_definitions(
    -DWITH_KERNEL_SSE2
    -DWITH_KERNEL_SSE3
    -DWITH_KERNEL_SSE41
  )
endif()

if(CXX_HAS_AVX)
  add_definitions(-DWITH_KERNEL_AVX)
endif()

if(CXX_HAS_AVX2)
  add_definitions(-DWITH_KERNEL_AVX2)
endif()

if(NOT OPENIMAGEIO_PUGIXML_FOUND)
  add_definitions(-DWITH_SYSTEM_PUGIXML)
endif()

# Definitions and Includes

add_definitions(
	${BOOST_DEFINITIONS}
	${OPENIMAGEIO_DEFINITIONS}
)

add_definitions(
	-DOCT_NAMESPACE_BEGIN=namespace\ oct\ {
	-DOCT_NAMESPACE_END=}
)

if(WITH_OPENSUBDIV)
	add_definitions(-DWITH_OPENSUBDIV)
	include_directories(
		SYSTEM
		${OPENSUBDIV_INCLUDE_DIR}
	)
endif()

# Logging capabilities using GLog library.
if(WITH_OCTANE_LOGGING)
	add_definitions(-DWITH_OCTANE_LOGGING)
	add_definitions(${GLOG_DEFINES})
	add_definitions(-DOCTANE_GFLAGS_NAMESPACE=${GFLAGS_NAMESPACE})
	include_directories(
		SYSTEM
		${GLOG_INCLUDE_DIRS}
		${GFLAGS_INCLUDE_DIRS}
	)
endif()

include_directories(
	SYSTEM
	${BOOST_INCLUDE_DIR}
	${OPENIMAGEIO_INCLUDE_DIRS}
	${OPENIMAGEIO_INCLUDE_DIRS}/OpenImageIO
	${PNG_INCLUDE_DIRS}
	${OPENEXR_INCLUDE_DIR}
	${OPENVDB_INCLUDE_DIRS}
	${PUGIXML_INCLUDE_DIR}	
)

list(APPEND LIB
	${OPENVDB_LIBRARIES}
)

include_directories(../atomic)

# Warnings
if(CMAKE_COMPILER_IS_GNUCXX)
	ADD_CHECK_CXX_COMPILER_FLAG(CMAKE_CXX_FLAGS _has_no_error_unused_macros "-Wno-error=unused-macros")
	unset(_has_cxxflag_float_conversion)
	unset(_has_cxxflag_double_promotion)
	unset(_has_no_error_unused_macros)
endif()

# Subdirectories

if(WITH_OPENCOLORIO)
	add_definitions(-DWITH_OCIO)
	include_directories(
		SYSTEM
		${OPENCOLORIO_INCLUDE_DIRS}
	)
endif()

add_definitions(-DWITH_BLENDER_GUARDEDALLOC)

add_subdirectory(blender)
add_subdirectory(graph)
add_subdirectory(render)
add_subdirectory(util)
add_subdirectory(doc)


