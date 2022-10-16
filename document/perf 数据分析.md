# `perf 数据分析`

## 编译：

>参考文档： https://developer.nvidia.com/embedded/downloads

```bash 
https://developer.nvidia.com/embedded/downloads
sudo wget https://developer.nvidia.com/embedded/l4t/r32_release_v7.1/sources/t186/public_sources.tbz2
bzip2 -d public_sources.tbz2
tar -xvf public_sources.tar
cd Linux_for_Tegra/source/public/
cp kernel_src.tbz2 ~
 bzip2 -d kernel_src.tbz2
 tar -xvf kernel_src.tar
 cd kernel/kernel-5.10/tools/perf 
 make && sudo cp perf  /usr/bin/perf
```

## 使用：

>参考文档：
>
>https://blog.csdn.net/code_peak/article/details/120813726?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120813726-blog-113463743.pc_relevant_aa_2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120813726-blog-113463743.pc_relevant_aa_2&utm_relevant_index=1



```bash
git clone https://github.com/brendangregg/FlameGraph.git

sudo apt install linux-tools-common
sudo apt install linux-tools-generic linux-cloud-tools-generic

$ perf 
WARNING: perf not found for kernel 5.4.0-77

  You may need to install the following packages for this specific kernel:
    linux-tools-5.4.0-77-generic
    linux-cloud-tools-5.4.0-77-generic

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install linux-tools-5.4.0-77-generic linux-cloud-tools-5.4.0-77-generic
```

示例：

```bash
sudo perf record -F 99 -p 2512 -g -- sleep 60

$ sudo perf record -F 99 -p 3092020 -g -- sleep 30
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.013 MB perf.data ]

$ ls
perf.data

# 统计每个调用栈出现的百分比，然后从高到低排列
$ sudo perf report -n --stdio

# 生成折叠后的调用栈
sudo perf script -i perf.data &> perf.unfold

# 生成火焰图
./stackcollapse-perf.pl perf.unfold &> perf.folded

./flamegraph.pl perf.folded > perf.svg
#简化。
sudo perf script | FlameGraph/stackcollapse-perf.pl | FlameGraph/flamegraph.pl > perf.svg
```



# `pprof监测C/C++程序`

## version:1

>参考文档：
>
>http://www.javashuo.com/article/p-gtvfkecj-go.html

##1 

```bash
$ sudo apt-get install autoconf
$ sudo apt-get install automake
$ sudo apt-get install libtool  
$ ./autogen.sh
$ ./configure
$ make
$ sudo  make install
$ su root
# echo /usr/local/lib > /etc/ld.so.conf.d/libtcmalloc.conf
# exit
$  sudo ldconfig
```

示例：

```bash
#include <iostream>
#include <unistd.h>
using namespace std;

class Person {
private:
    string name;
public:
    void setName(string name) {
        this->name = name;
    }

    const string& getName() {
        return this->name;
    }
};

int main() {
    Person *someone;
    for(int i=0; i<10; ++i) {
        someone = new Person;
        someone->setName("Li Ming"); 
        cout << someone->getName() << endl;
        // sleep(2);
    }
}
```

```bash
$ g++ example.cpp -ltcmalloc
$ HEAPPROFILE=test   ./a.out
```

程序运行结束后，当前目录会出现 `test.0001.heap`文件。node

生成pdf：ios

```bash
$ pprof --pdf a.out test.0001.heap > test.pdf
```

### 查看内存泄漏

```bash
$ export PPROF_PATH=/usr/local/bin/pprof
$ HEAPCHECK=normal ./a.out              
WARNING: Perftools heap leak checker is active -- Performance may suffer
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Li Ming
Have memory regions w/o callers: might report false leaks
Leak check _main_ detected leaks of 400 bytes in 20 objects
The 2 largest leaks:
Using local file ./a.out.
Leak of 320 bytes in 10 objects allocated from:
	@ 7fb33ee69249 std::string::_Rep::_S_create
	@ 7fb33ee6a971 std::string::_S_construct
	@ 7fb33ee6ad88 std::basic_string::basic_string
	@ 400d8e main
	@ 7fb33e7f5f45 __libc_start_main
	@ 400c79 _start
Leak of 80 bytes in 10 objects allocated from:
	@ 400d5e main
	@ 7fb33e7f5f45 __libc_start_main
	@ 400c79 _start


If the preceding stack traces are not enough to find the leaks, try running THIS shell command:

pprof ./a.out "/tmp/a.out.31217._main_-end.heap" --inuse_objects --lines --heapcheck  --edgefraction=1e-10 --nodefraction=1e-10 --gv

If you are still puzzled about why the leaks are there, try rerunning this program with HEAP_CHECK_TEST_POINTER_ALIGNMENT=1 and/or with HEAP_CHECK_MAX_POINTER_OFFSET=-1
If the leak report occurs in a small fraction of runs, try running with TCMALLOC_MAX_FREE_QUEUE_SIZE of few hundred MB or with TCMALLOC_RECLAIM_MEMORY=false, it might help find leaks more repeatab
Exiting with error code (instead of crashing) because of whole-program memory leaks
```

```bash
g++ example03.cpp -ltcmalloc
HEAPPROFILE=test   ./a.out
```

### 错误解决

１、｀sh: 1: dot: not found｀

```bash
sudo apt-get install graphviz
```

二、"gv": No such filegit参考
```bash
tcmalloc安装，使用以及解析（一）
error while loading shared libraries: xxx.so.x"错误的缘由和解决办法 shel
```

其余：

```bash
#用gperftools对C/C++程序进行profile缓
http://www.javashuo.com/link?url=http://airekans.github.io/cpp/2014/07/04/gperftools-profile
#https://github.com/gperftools/gperftools工
http://www.javashuo.com/link?url=https://github.com/gperftools/gperftools
#关于gperftoolsui
http://www.javashuo.com/link?url=http://www.cnblogs.com/caosiyang/archive/2013/01/25/2876244.html
#Google CPU Profiler使用指南及小工具th
http://www.javashuo.com/link?url=http://www.searchtb.com/2012/12/google-cpu-profiler.html
#TCMalloc：线程缓存的Malloc
http://www.javashuo.com/link?url=http://shiningray.cn/tcmalloc-thread-caching-malloc.html
#TCMalloc小记
http://www.javashuo.com/link?url=http://blog.csdn.net/chosen0ne/article/details/9338591
```

## version:2

>参考链接
>
>https://zhuanlan.zhihu.com/p/539840046

### 0 前言

在进行模块的负载优化时，使用到了 Google 开发的 [gperftools](https://link.zhihu.com/?target=https%3A//github.com/gperftools/gperftools) 工具来进行代码性能分析。正如 [gperftools wiki](https://link.zhihu.com/?target=https%3A//github.com/gperftools/gperftools) 中所描述的：

> gperftools is a collection of a high-performance multi-threaded `malloc()` implementation, plus some pretty nifty performance analysis tools.
> gperftools 是一系列高性能多线程 `malloc()` 实现的集合，同时添加了一些精巧的性能分析工具。

gperftools 性能分析工具主要包含五部分：

- [TC Malloc](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/tcmalloc.html)
- [Heap Checker](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/heap_checker.html)
- [Heap Profiler](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/heapprofile.html)
- [CPU Profiler](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/cpuprofile.html)
- [pprof](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/pprof_remote_servers.html)

本文中将使用 CPU Profiler 和 pprof 进行代码性能分析。其中，CPU Profiler 用于生成后缀为 `.prof` 的 profile 性能描述文件，pprof 是用于解析 profile 文件的 perl 脚本工具。

### 1 安装

#### 1.1 基础软件

在命令行中通过 `apt` 安装 autoconf、automake、libtool：

```bash
sudo apt install autoconf automake libtool
```

#### 1.2 libunwind

gperftools 在 64 位操作系统下需要 [libunwind](https://link.zhihu.com/?target=https%3A//github.com/libunwind/libunwind) 库的支持，libunwind 提供了可用于分析程序调用栈的 API，可直接执行下述命令行进行安装：

```bash
cd ~
wget https://github.com/libunwind/libunwind/releases/download/v1.6.2/libunwind-1.6.2.tar.gz
tar -zxvf libunwind-1.6.2.tar.gz
cd libunwind-1.6.2
./configure
make -j8
sudo make install
cd ~
rm -rf libunwind-1.6.2.tar.gz libunwind-1.6.2
```

#### 1.3 graphviz

gperftools 使用 [graphviz](https://link.zhihu.com/?target=http%3A//www.graphviz.org/) 将代码性能分析结果进行图形化显示。graphviz 是一个由 AT&T 实验室开发的开源工具包，用于绘制 DOT 语言脚本描述的图形，Ubuntu 中可通过 `apt` 直接安装：

```bash
sudo apt install graphviz
```

#### 1.4 gperftools

gperftools 可直接执行下述命令行进行安装：

```bash
cd ~
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.10/gperftools-2.10.tar.gz
tar -zxvf gperftools-2.10.tar.gz
cd gperftools-2.10
./configure
make -j8
sudo make install
cd ~
rm -rf gperftools-2.10.tar.gz gperftools-2.10
```

### 2 使用

下文中将使用的 C++ 工程 Demo 可点击[这里](https://zhuanlan.zhihu.com/download/cpp_demo.zip)下载。

#### 2.1 代码插桩

在使用 gperftools 进行代码性能分析前，需要进行代码插桩：

- 插入头文件：

```cpp
#include <gperftools/profiler.h>
```

- 在待分析的代码块前插入 Profiler 开始语句：

```text
ProfilerStart("file_name.prof");
```

`file_name.prof` 表示 `.prof` 文件的文件名。

- 在待分析的代码块后插入 Profiler 结束语句：

```cpp
ProfilerStop();
```

完整的插桩示例：

```cpp
#include "inc/func.hpp"
#include <gperftools/profiler.h>

int main()
{
    ProfilerStart("cpp_demo_perf.prof");

    PrintString("This's a demo.");
    Func();

    ProfilerStop();

    return 0;
}
```

#### 2.2 编译链接

编译时我们需要将 profiler 库和 libunwind 库链接到可执行程序，对应的 CMakeLists 文件中的语句为：

```cmake
target_link_libraries(${PROJECT_NAME} profiler unwind)
```

#### 2.3 运行可执行程序

找到编译得到的可执行程序，并在终端中运行：

```bash
./cpp_demo
```

正常情况下，会生成一个我们上文中所提到的 `.prof` 文件，如果报动态链接库找不到的问题，手动执行下动态链接库的管理命令 `ldconfig` 即可：

```bash
sudo ldconfig
```

`ldconfig` 可执行程序存放在 `/sbin` 目录下，通常在系统启动时运行，而当用户安装了一个新的动态链接库时，需要手动运行这个命令。运行 `ldconfig` 会刷新动态装入程序 `ld.so` 所需的链接和缓存文件 `/etc/ld.so.cache`（此文件保存了已排好序的动态链接库名字列表），实现动态链接库为系统所共享。

#### 2.4 生成图形化分析报告

最后，通过上文提到的 pprof 解析 `.prof` 文件。pprof 有多种使用方法，下面的命令行将 `.prof` 文件解析为 `.pdf` 文件：

```bash
pprof --pdf cpp_demo cpp_demo_perf.prof > cpp_demo_perf.pdf
```

解析得到的 `.pdf` 文件中保存了图形化的代码性能分析结果，从中我们可以查找代码的性能瓶颈：

![img](https://pic2.zhimg.com/80/v2-e99278f30d23ea970d3a16b3574c04d1_720w.webp)图形化性能分析报告

每一个方框表示一个进程，有向边表示进程间的调用关系。方框越大，表示该进程耗时越高，这里我们可以发现，`Func2` 函数占了程序总耗时的 67%，是程序的性能瓶颈。需要注意的是，gperftools 的 CPU Profiler 是通过采样的方式工作的，如果程序运行时间太短，会导致样本不足从而造成分析结果不准确。

关于图形化分析结果更详细的解释，可以参考[这里](https://link.zhihu.com/?target=https%3A//gperftools.github.io/gperftools/cpuprofile.html)。



