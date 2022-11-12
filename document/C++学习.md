# C++学习

## 说明:

```c++
变量的定义方式： 
    变量类型 变量名称 = 变量初始值;
    // int a = 10;
```

```c++
常量：
    作用: 用于记录程序中不可更改的数据
1. #define 宏常量： #define 常量名 常量值
        通常在文件上方定义 ，表示一下常量
2. const修饰的变量： const 数据类型 常量名 = 常量值
        通常在变量定义前加关键字 const ,修饰该变量为常量， 不可修改
```

内存空间占比大小

```c++
// 整型
short 2字节 {-2^15 ~ 2^15-1}
int 4字节 {-2^31 ~ 2^31-1}
long long 8字节 {-2^63 ~ 2^63-1}

//浮点型
float 4字节 {7位有效}
double 8字节 {15~16位有效}

//字符
char 1字节 {}

// c风格 字符串 
char string[] = "" 
// c++风格 字符串
string str = ""      // 需要 #include <string>
    
// 布尔
bool 1字节 {非0都为真}
```



## 选择结构：

```c++
// if 和 switch 的区别？

// switch 缺点： 判断的时候只能是整形或者字符型，不可以是一个区间
// switch 优点： 结构清晰，执行效率高
```

## 循环结构：

```c++
1. while 循环语句
    作用： 满足循环条件， 执行循环语句
    语法： while (循环条件){循环语句}
2. do...while 循环语句
    作用：  满足循环条件， 执行循环语句
    语法： do{循环语句} while(循环条件)；
    注意： 与while的区别在于do...while会先执行一次循环语句，再判断循环条件
3  for 循环语句
    作用： 满足循环条件，执行循环语句
    语法： for(起始表达式;条件表达式；末尾循环体) {循环语句}
```





## 常用函数:

>
>
>### 常用函数篇

### sizeof()

```c++
语法： sizeof(数据类型/变量) // sizeof(int) 4字节
```





## 文件篇:

>### 文件篇

- ios::in 为读文件而打开文件
  ios::out 为写文件而打开文件
  ios::ate 初始位置，文件末尾
  ios::app 追加方式写文件
  ios::trunc 如果文件已经存在，先删除，在创建
  ios::binary 二进制

```c++
#include<iostream>
using namespace std;
#include<fstream>
int main()i
{
	/*C:\Users\admin\Desktop\c++基础\c++文件的读写*/
	ofstream ofs;
	ofs.open("C://Users//admin//Desktop//c++基础//c++文件的读写//test.txt", ios::out);
	ofs << "姓名：张三" << endl;
	ofs << "年龄：28" << endl;
	ofs << "性别：男" << endl;
	system("pause");
	return 0;
}
```

