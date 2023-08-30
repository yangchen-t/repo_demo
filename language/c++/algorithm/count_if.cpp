#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 count_if  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10


// 查找内置数据类型 
int Conditions(int val)
{
    return val > 2;
}

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MaxSize; i++) 
    {
        v.push_back(i);
    }
    
    int ret = count_if(v.begin(), v.end(),Conditions);
    std::cout << ret << std::endl;
}

// 查找自定义数据类型
class Person{
public:
    Person(std::string name, int age)
    {
        this->age = age;
        this->name = name;
    }
    bool operator()(const Person &p)
    {
        return this->age > p.age;
    }
    std::string name;
    int age;
};

void test02()
{
    std::vector<Person>p;
    Person p1("123",1);
    Person p2("123",2);
    Person p3("123",3);
    Person p4("123",7);
    Person p5("123",5);
    Person p6("123",123);
    Person p7("123",123);
    Person p8("123",23);
    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    p.push_back(p4);
    p.push_back(p5);
    p.push_back(p6);
    p.push_back(p7);
    p.push_back(p8);

    int ret = count_if(p.begin(), p.end(),Person("123",100));
    std::cout << ret << std::endl;
}

int main()
{
    // test01();
    test02();
    return 0;
}