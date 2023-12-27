#include <iostream>
#include <fstream>

using namespace std;


class test
{
public:
    char m_Name[64];
    int age;
};


void test01()
{
    ifstream ifs;
    ifs.open("test.b", ios::in|ios::binary);
    if (!ifs.is_open())
    {
        cout << "file open is failed" << endl;
        return;
    }
    test p;

    ifs.read( (char *)&p, sizeof(test));

    cout << p.age << p.m_Name << endl;

}

int main()
{
    test01();
    return 0;
}