#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 find 
    // 查找内置数据类型 
    // 查找自定义数据类型


class Person  {
public:
    Person(std::string name, int age)
    {
        this->name = name;
        this->age = age;
    }
    // 重载 == 告诉底层find知道如何对比Person数据类型
    bool operator == (const Person & p)
    {
        if (this->name == p.name && this->age == p.age)
        {
            return true; 
        }
    }
    std::string name;
    int age;
};


void print(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin() ; it != v.end() ; it++)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

// 查找内置数据类型
template <typename T>
void test(std::vector<T> list ,T value)
{
    if ( find(list.begin(),list.end(), value) == list.end())
    {
         std::cout << "not find value" << std::endl;
    } else {
        std::cout << "find value" << std::endl;
    }
}


int main()
{
    std::vector<int>v;
    for (int i = 1; i < 10 ; i++)
    {
        v.push_back(i);
    }
    int testValue = 2;
    test<int>(v, testValue);

    std::vector<Person>p;
    Person p1("aaa", 10);
    Person p2("bbb", 20);
    Person p3("ccc", 30);
    Person p4("ddd", 40);
    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    p.push_back(p4);
    test<Person>(p,p4);
}