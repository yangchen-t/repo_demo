// 存放自定义数据类型

#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
 
class Person
{
public:
    Person(string name, int age)
    {
        this->C_name = name;
        this->C_age = age;
    }
    string get_name(){return this->C_name;};
    int get_age(){return this->C_age;};
private:
    string C_name;
    int C_age;
};

void vector_info_print(Person p)
{
    cout << " name : " << p.get_name() << " age : " << p.get_age() << endl;
}
void test01()
{
    vector<Person> vp;
    Person p1("aaaa", 10);
    Person p2("bbbb", 20);
    Person p3("cccd", 30);
    vp.push_back(p1);
    vp.push_back(p2);
    vp.push_back(p3);
    for_each(vp.begin(), vp.end(), vector_info_print);
}

// 传入指针
void test02()
{
    vector<Person*> vp;
    Person p1("aaaa", 10);
    Person p2("bbbb", 20);
    Person p3("cccd", 30);
    vp.push_back(&p1);
    vp.push_back(&p2);
    vp.push_back(&p3);

    for (vector<Person*>::iterator it = vp.begin(); it != vp.end() ; it++)
    {
        // return Person * 
        cout << "name: " << (*it)->get_age()  << " age: " << (*it)->get_name() << endl;

    }
    
}

int main()
{
    // test01();
    test02();
    return 0;
} 