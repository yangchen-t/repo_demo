#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用排序算法 merge  
    // 查找内置数据类型 
    // 查找自定义数据类型


// 仿函数 谓词
bool FakeFunc(int v1, int v2)
{
    return v1 < v2;
}

void Print(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
}

void test01()
{
    std::vector<int>v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    sort(v1.begin(), v1.end(), FakeFunc);
    std::vector<int>v2;
    for (int i = 3; i < 13; i++)
    {
        v2.push_back(i);
    }
    sort(v2.begin(), v2.end(), FakeFunc);
    std::vector<int>v3;
    v3.resize(v1.size() + v2.size());
    merge(v1.begin(), v1.end(), v2.begin(), v2.end(),v3.begin());
    Print(v3);
}

int main()
{
    test01();
    return 0;
}