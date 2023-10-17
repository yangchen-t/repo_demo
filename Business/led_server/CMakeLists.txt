cmake_minimum_required(VERSION 3.5)
project(led_server)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN:$ORIGIN/../")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

include_directories(include) # 添加项目中的include文件夹路径
add_executable(server 
  src/led_server.cpp
)
add_executable(test_pub
  src/pub.cpp
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)



target_include_directories(server PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)


ament_target_dependencies(
    server
    "rclcpp"
)
ament_target_dependencies(
    test_pub
    "rclcpp"
)

target_link_libraries(server
  ${PROJECT_SOURCE_DIR}/lib/libbx_sdkDual.so.1.0.0
  ${PROJECT_SOURCE_DIR}/lib/libiconv.so.2
  ${PROJECT_SOURCE_DIR}/lib/libcharset.so.1.0.0
)

install(
  DIRECTORY lib/                         
  DESTINATION lib/                        
)
install(TARGETS server
  RUNTIME DESTINATION lib/${PROJECT_NAME}   
)

install(TARGETS 
  server
  test_pub 
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()