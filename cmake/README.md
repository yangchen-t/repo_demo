## cmake build 
- https://zhuanlan.zhihu.com/p/267803605
- https://modern-cmake-cn.github.io/Modern-CMake-zh_CN/chapters/basics/functions.html
- https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html

## USE 
```cmake
# 指定 make install 路径
-  cmake .. -D CMAKE_INSTALL_PREFIX="/home/westwell" 

# 指定 src 路径 和 bin 路径  参数 -S = src -B = bin 
- cmake -S . -B build 

# 指定 CMakeCache.txt 进行 编译
- cmake -S . -B build -C CMakeCache.txt

# Cmakelist > -D CMAKE_INSTALL_PREFIX > default 
# CMaekLists.txt  
# set(CMAKE_INSTALL_PREFIX "/home/westwell")
```

### build share_libaray 
```cmake
g++ -share -o libxx.so lib.cpp -fPIC 
g++ -o main main.cpp -l lib.so 
```