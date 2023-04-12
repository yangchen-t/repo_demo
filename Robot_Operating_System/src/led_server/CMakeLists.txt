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

include_directories(include) # 添加项目中的include文件夹路径
add_executable(sub
  src/sub.cpp
  src/get_info.cpp
)
add_executable(pub
  src/pub.cpp
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(interfaces REQUIRED)


target_include_directories(sub PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)


ament_target_dependencies(
    sub 
    "rclcpp"
    interfaces
  )
ament_target_dependencies(
    pub
    "rclcpp"
    interfaces
  )

target_link_libraries(sub
  ${PROJECT_SOURCE_DIR}/lib/libbx_sdkDual.so.1.0.0
  ${PROJECT_SOURCE_DIR}/lib/libiconv.so.2.6.0
  ${PROJECT_SOURCE_DIR}/lib/libcharset.so.1.0.0
)

install(
  DIRECTORY lib/                       # 发现你项目中的lib中所有的文件
  DESTINATION lib/      # 拷贝到install目录中
)
install(TARGETS sub
  RUNTIME DESTINATION lib/${PROJECT_NAME}    # 程序运行的时候调用install中的路径
)

install(TARGETS 
  sub
  pub 
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

