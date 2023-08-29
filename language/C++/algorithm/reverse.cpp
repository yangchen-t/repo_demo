#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用排序算法 reverse  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10 

void MySort(int &v)
{
    std::cout << v << " ";
}

void test01()
{
    std::vector<int>v; 
    for (int i = 0; i < MaxSize; i++)
    {
        v.push_back(i);
    }
    for_each(v.begin(),v.end(), MySort);
    std::cout << std::endl;
    reverse(v.begin(), v.end());
    for_each(v.begin(),v.end(), MySort); 
}

int main()
{
    test01();
    return 0;
}
