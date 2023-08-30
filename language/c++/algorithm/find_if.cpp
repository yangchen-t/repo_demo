#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 find_if  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MAX 10
#define GREATER 4

// 查找内置数据类型 
// 仿函数
class Conditions {
public:
    bool operator () (int val)
    {
        return val > GREATER; 
    }
};

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MAX; i++)
    {
        v.push_back(i);
    }
    std::vector<int>::iterator ret = find_if(v.begin(), v.end(), Conditions());
    if (ret == v.end())
    {
        std::cout << "not found" << std::endl;
    } else {
        std::cout << "result :" << *ret << std::endl;
    }
}

// 查找自定义数据类型
// 仿函数
class Person {
    public:
        Person(std::string name, int age)
        {
            this->name = name;
            this->age = age;
        }
        // 名字相同，年龄大于的
        bool operator()(Person &p)
        {
            if (this->name == p.name && this->age < p.age)
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
    std::vector<Person>v;
    Person p1("123",123);
    Person p2("456",456);
    Person p3("789",789);
    Person p4("987",987);
    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);

    std::vector<Person>::iterator ret = find_if(v.begin(), v.end(), Person("987",123));
    if (ret == v.end())
    {
        std::cout << "not found" << std::endl;
    } else {
        std::cout << "result -- <name: " << ret->name << ">, <age: " << ret->age << ">" << std::endl;
    }
}


int main() 
{
    // test01();
    test02();
}