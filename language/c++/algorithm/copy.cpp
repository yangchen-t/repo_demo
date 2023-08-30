#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用拷贝算法 copy  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10

void FakeFunc(int v)
{
    std::cout << v << " ";
}

void test01()
{
    std::vector<int>v1;
    for (int i = 0; i < MaxSize; i++)
    {
        v1.push_back(i);
    }
    for_each(v1.begin(), v1.end(), FakeFunc);
    std::cout << std::endl;
    std::vector<int>v2;
    v2.resize(MaxSize);
    copy(v1.begin(),v1.end()-2 ,v2.begin());
    for_each(v2.begin(), v2.end(), FakeFunc);
}

int main()
{
    test01();
    return 0;
}