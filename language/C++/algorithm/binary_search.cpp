#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 binary_search  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10
#define Value 9

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MaxSize ; i++)
    {
        v.push_back(i);
    }
    
    // 容器必须是有序的序列
    if (binary_search(v.begin(), v.end(), Value))
    {
        std::cout << "found" << std::endl;
    }else {
        std::cout << "not found" << std::endl;
    }
}

int main()
{
    test01();
    return 0;
}