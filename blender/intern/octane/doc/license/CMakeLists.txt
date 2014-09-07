
set(LICENSES
	Blender.txt
	GPL.txt
	readme.txt
)

delayed_install(${CMAKE_CURRENT_SOURCE_DIR}  "${LICENSES}" ${OCTANE_INSTALL_PATH}/license)
