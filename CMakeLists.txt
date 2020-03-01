cmake_minimum_required(VERSION 3.5)
project(systemd-logger)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(PkgConfig REQUIRED)
#pkg_search_module(PKG_SYSTEMD REQUIRED IMPORTED_TARGET systemd)
#pkg_check_modules(logtest REQUIRED systemd)
add_executable(logtest src/Log.cpp)
#target_link_libraries(logtest PRIVATE PkgConfig::PKG_SYSTEMD)
target_link_libraries(logtest ${CONAN_LIBS})
foreach(system_includedir ${CONAN_SYSTEM_INCLUDEDIRS})
	message(STATUS "include: ${system_includedir}")	
	target_include_directories(logtest PRIVATE ${system_includedir})
endforeach()
foreach(system_libdir ${CONAN_SYSTEM_LIBDIRS})
	message(STATUS "lib: ${system_libdir}")	
	link_directories(logtest ${system_libdir})
endforeach()

foreach(system_lib ${CONAN_SYSTEM_LIBS})
	message(STATUS "lib: ${system_lib}")	
	target_link_libraries(logtest ${system_lib})
endforeach()


