cmake_minimum_required(VERSION 2.8)

project(cmake_test)

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

install (TARGETS ${EXECUTABLE} DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h"
         DESTINATION include)