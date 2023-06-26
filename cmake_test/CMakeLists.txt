cmake_minimum_required(VERSION 2.8...3.2)

project(cmake_test VERSION 1.0
    DESCRIPTION "this is cmake test project"
    LANGUAGES CXX)

set(EXECUTABLE main)
set(FLAG false)

# tell CMake to generate config.h
configure_file (
  "${PROJECT_SOURCE_DIR}/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
  )
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")


aux_source_directory(func SECLIST)

option (USE_MYADD
       "Use provided add implementation" ON)

if (USE_MYADD)
    message(STATUS "use libadd")
    include_directories ("${PROJECT_SOURCE_DIR}/add")
    add_subdirectory(add)   # sub Cmakefile.txt
    set (LIBADD libadd)

    # set(LIBADD Add)
    # aux_source_directory(./add SRC_LIST)
    # add_library(${LIBADD} ${SRC_LIST})
endif(USE_MYADD)

add_executable(${EXECUTABLE} main.cpp ${SECLIST})
target_link_libraries(${EXECUTABLE} ${LIBADD})


# add  gdb
# set(CMAKE_BUILD_TYPE "Debug")
# set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
# set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# install on /usr/local/
install (TARGETS ${EXECUTABLE} DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h" DESTINATION include)
install (FILES add.h DESTINATION include)