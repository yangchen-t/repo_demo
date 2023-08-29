#include <iostream>
#include <vector>
#include <algorithm>

// 常用遍历算法 transform 


// 普通函数
int func(int val)
{
    return val * 2;
}

// 仿函数
class TransForm {
public:
    int operator()(int v)
    {
        return v;
    }
};

// 仿函数
class ForEach 
{
public:
    void  operator()(int v)
    {
        std::cout << v << " ";
    }   
};

void print(std::vector<int> &v)
{
    for_each(v.begin(), v.end(), ForEach());
}

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < 20; i++)
    {
        v.push_back(i);
    }
    std::vector<int>v1;
    v1.resize(v.size()); // 开辟空间
    // transform(v.begin(), v.end(), v1.begin(), TransForm());
    transform(v.begin(), v.end(), v1.begin(), func);
    print(v1);
    v.clear();
    v1.clear();
}

int main()
{
    test01();
}