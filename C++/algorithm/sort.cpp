#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用排序算法 sort  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10

// 仿函数
bool FakeFunc01(int v1, int v2)
{
    return v1 > v2;
}

// 仿函数
class FakeFunc02{
public:
    bool operator()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void Print(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin() ; it != v.end() ; it++)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

// 查找内置数据类型 
void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MaxSize; i++)
    {
        v.push_back(i);
    }
    v.push_back(2);
    v.push_back(5);
    Print(v);
    sort(v.begin(), v.end());
    Print(v);
    sort(v.begin(), v.end(), FakeFunc01);
    Print(v);
    v.pop_back();
    sort(v.begin(), v.end(), FakeFunc02());
    Print(v);
}


// 查找自定义数据类型
class Person {
    public:
        Person(std::string name , int age)
        {
            this->age = age;
            this->name = name;
        }
        bool operator()(const Person &p1, const Person &p2)
        {
            return p1.age < p2.age;
        }
        std::string name;
        int age;
};

void PersonPrint(std::vector<Person> &v)
{
    for (std::vector<Person>::iterator it = v.begin() ; it != v.end() ; it++)
    {
        std::cout << "name: " << it->name  << " age: " << it->age << std::endl;
    }
}

void test02()
{
    std::vector<Person>p;
    Person p1("123", 1);
    Person p2("123", 7);
    Person p3("123", 9);
    Person p4("123", 4);
    Person p5("123", 3);
    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    p.push_back(p4);
    p.push_back(p5);
    sort(p.begin(), p.end(), Person("test",123));
    PersonPrint(p);
}


int main()
{
    // test01();
    test02();
    return 0;
}