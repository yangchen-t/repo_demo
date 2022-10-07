# C++学习



>文件篇

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
int main()
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

