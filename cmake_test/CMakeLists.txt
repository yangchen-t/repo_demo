cmake_minimum_required(VERSION 2.8...3.2)

project(cmake_test VERSION 1.0
    DESCRIPTION "this is cmake test project"
    LANGUAGES CXX)

set(EXECUTABLE main)

configure_file (
  "${PROJECT_SOURCE_DIR}/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
)

aux_source_directory(func SrcList)

option (USE_MYADD
       "Use provided add implementation" ON)

if (USE_MYADD)
    include_directories ("${PROJECT_SOURCE_DIR}/add")
    add_subdirectory(add)
    set (EXTRA_LIBS ${EXTRA_LIBS} Add)
endif()

add_executable(${EXECUTABLE} main.cpp ${SrcList})
target_link_libraries(${EXECUTABLE} ${EXTRA_LIBS})

# add  gdb
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# install on /usr/local/
install (TARGETS ${EXECUTABLE} DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h"
         DESTINATION include)