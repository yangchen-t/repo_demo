#include <iostream>
#include <fstream>
#include <string>

using namespace std;


class test
{
public:

    test(int age)
    {
        this->age =age;
    } 

    char m_Name[64] = "张三";
    int age ;
};



void test01()
{

    ofstream ofs;
    ofs.open("test.b", ios::binary|ios::out);
    if (!ofs.is_open())
    {
        cout << "file open is failed" << endl;
    }
    char name[64] = "张三";
    test t{18};
    // t.m_Name = "c";

    ofs.write( (const char * )&t, sizeof(test));

    ofs.close();
}


int main()
{
    test01();
    return 0;
}