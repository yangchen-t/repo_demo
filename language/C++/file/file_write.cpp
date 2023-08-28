#include<iostream>
using namespace std;
#include<fstream>
int main()
{
	/*C:\Users\admin\Desktop\c++基础\c++文件的读写*/
	ofstream ofs;
	ofs.open("./test.txt", ios::out);
	ofs << "姓名：张三" << endl;
	ofs << "年龄：28" << endl;
	ofs << "性别：男" << endl;
	return 0;
}

