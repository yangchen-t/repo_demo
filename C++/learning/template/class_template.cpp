#include <iostream>
#include <string>

using namespace std;

template<class NameType, class AgeType>
class test
{
public:
    test(NameType name, AgeType age)
    {
        this->m_name = name;
        this->m_age = age;
    }

    void Showinfo()
    {
        cout << "name: " << this->m_name 
        <<  " age:" << this->m_age << endl;
    }

    NameType m_name;
    AgeType m_age;
};

void test01()
{
    test<string, int> t1("chen", 100);
    t1.Showinfo();
}

int main()
{
    test01();
    return 0;
}