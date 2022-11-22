# C++ 编译 , 一文搞懂 动态库与静态库

[TOC]

## 目的：

>
>
>我们都知道编译的过程分为三步：[预处理](https://so.csdn.net/so/search?q=预处理&spm=1001.2101.3001.7020)、编译和汇编，本文的实验目的就是探究在汇编过程中生成静态库.a和动态库.so的过程。



## 静态库：

> 我们通常把一些公用函数制作成函数库，供其它程序使用。函数库分为静态库和动态库两种。 静态库在程序编译时会被连接到目标代码中，程序运行时将不再需要该静态库。动态库在程 序编译时并不会被连接到目标代码中，而是在程序运行是才被载入，因此在程序运行时还需 要动态库存在。

### 创建静态库

```c++
gcc编译得到 .o 文件
> gcc -c hello.c++                 // 会生成一个 hello.o 的文件

创建一个名为myhello的静态库文件
创建静态库的工具：ar
静态库文件命名规范：以lib作为前缀,是.a文件
指令为：

> ar -crv libmyhello.a hello.o     // 会生成 libmyhello.a
    

    
```

###  程序中引用静态库

>
>
>静态库制作完了，如何使用它内部的函数呢？只需要在使用到这些公用函数的源程序中包 含     这些公用函数的原型声明，然后在用 gcc 命令生成目标文件时指明静态库名，gcc 将会从     静态库中将公用函数连接到目标文件中。注意，gcc 会在静态库名前加上前缀 lib，然后追     加扩展名.a 得到的静态库文件名来查找静态库文件。
>共有以下三种方法在程序中引用静态库：

1， 键入命令：

```c++
> gcc -o hello main.c++ -L. -lmyhello  
这条命令的语义是从lmyhello静态库中将公用函数hello连接到我们的目标程序			main.c++文件中。
需要注意的是，自定义的库时，main.c++ 还可放在-L.和 –lmyhello 之间，但是不能放在它俩之后，否则会提 示 myhello 没定义，但是是系统的库时，如 g++ -o main（/usr/lib） -lpthread main.cpp 就不出错。
```

2， 

```c++
gcc main.c++ libmyhello.a -o hello
```

3，

```c++
先生成 main.o
> gcc -c main.c++ 
再生成可执行文件
> gcc -o hello main.o libmyhellio.a
动态库连接时也可以这样做。  
```



------



## 动态库：

1， 创建动态库

```c++
创建动态库的工具：gcc
动态库文件命名规范：以lib作为前缀,是.so文件

> gcc -shared -fPIC -o libmyhello.so hello.o
shared:表示指定生成动态链接库，不可省略
-fPIC：表示编译为位置独立的代码，不可省略
命令中的-o一定不能够被省略
```

2， 在程序中执行动态库

```c++
> gcc -o hello main.c++ -L. myhello 
    或 > gcc main.c++ libmyhello.so -o hello
再运行可执行文件hello，会出现错误
```

>
>
>问题的解决方法：将libmyhello.so复制到目录/usr/lib中。由于运行时，是在/usr/lib中找库文件的。 <cp/mv 即可>

3， 动态库和静态库的比较

```c++
gcc编译得到.o文件
    > gcc -c hello.c++
创建静态库 
    > ar -crv libmyhello.a hello.o

    VS
    
创建动态库 
    > gcc -shared -fPIC -o libmyhello.so hello.o
使用库生成可执行文件 
    > gcc -o hello main.c -L. -lmyhello
执行可执行文件 
    > ./hello
```

>
>
>当静态库与动态库同时存在的时候，会优先使用动态库。





## 总结:

```c++
验证静态库的特点:
在删掉静态库的情况下，运行可执行文件，发现程序仍旧正常运行，表明静态库跟程序执行没有联系。同时，也表明静态库是在程序编译的时候被连接到代码中的。
    
当静态库与动态库同时存在的时候，会优先使用动态库。 
```















