# CMake 最低版本号要求
cmake_minimum_required(VERSION 2.8...3.2)

# 项目信息
project(cmake VERSION 1.0
        DESCRIPTION "this is cmake test project"
        LANGUAGES CXX)

set(EXEC main)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# 是否使用自己的 MathFunctions 库
option (USE_MYMATH
	   "Use provided math implementation" ON)

# 是否加入 MathFunctions 库
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/math")
  add_subdirectory (math)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)
# 加入一个配置头文件，用于处理 CMake 对源码的设置
# configure_file 必须放在 option下面
configure_file (
  "${PROJECT_SOURCE_DIR}/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(func DIR_SRCS)
# 指定生成目标
add_executable (${EXEC} main.cpp ${DIR_SRCS})
target_link_libraries (${EXEC} ${EXTRA_LIBS})

# add  gdb
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# defualt install on /usr/local/
install (TARGETS main DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h" DESTINATION include)
install (FILES "math/math.hpp" DESTINATION include)