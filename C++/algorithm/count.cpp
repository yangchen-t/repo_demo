#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 count   
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10
#define Value 0

// 查找内置数据类型 
void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MaxSize; i++) 
    {
        v.push_back(i);
    }
    v.push_back(0);
    int ret = count(v.begin(), v.end(), Value);
    std::cout << ret  << std::endl;
}

// 查找自定义数据类型
class Person{
public:
    Person(std::string name, int age)
    {
        this->name = name;
        this->age = age;
    }
    bool operator==(const Person &p)
    {
        if (this->age == p.age)
        {
            return true;
        } else {
            return false;
        }
    }
    std::string name;
    int age;
};

void test02()
{
    std::vector<Person>p;
    Person p1("1",123);
    Person p2("2",123);
    Person p3("3",123);
    Person p4("4",423);
    Person p5("5",523);
    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    p.push_back(p4);
    p.push_back(p5);
    Person p6("123",123);
    int ret = count(p.begin(), p.end(), p6);
    std::cout << ret << std::endl;
}


int main()
{
    // test01();
    test02();
    return 0 ;
}