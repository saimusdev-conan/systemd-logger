import os
from conans import ConanFile, tools, CMake

class SystemdLogger(ConanFile):
	name = "systemd-logger"
	version = "0.0.1"

	settings = "os", "compiler", "build_type", "arch"
	generators = "cmake"

	exports_sources = ["CMakeLists.txt", "src/*"]

	@property
	def default_user(self):
		return "saimusdev-conan"

	@property
	def default_channel(self):
		return "testing"

	
	def build(self):
		self.output.warn("build")
		cmake = CMake(self)
		with tools.environment_append({'PKG_CONFIG_PATH': "/tmp/logtest"}):
			pkg_config = tools.PkgConfig("libsystemd")
			include_dir = os.path.join(pkg_config.variables["includedir"], "systemd")
			lib_dir = os.path.join(pkg_config.variables["libdir"])
			print("CFLAGS: %s" % pkg_config.cflags)
			print("Includes: %s" % pkg_config.cflags_only_I)
			print("Include dir: %s" % include_dir)
			print("Libs: %s" % pkg_config.libs_only_L)
			print("More Libs: %s" % pkg_config.libs_only_l)
			print("lib dir: %s" % lib_dir)
			print("variables: %s" % pkg_config.variables)
			cmake.definitions["CMAKE_VERBOSE_MAKEFILE"] = "TRUE"
			cmake.definitions["CONAN_SYSTEM_INCLUDEDIRS"] = include_dir
			cmake.definitions["CONAN_SYSTEM_LIBDIRS"] = lib_dir
			cmake.definitions["CONAN_SYSTEM_LIBS"] = "systemd"
			cmake.configure()
			cmake.build()

