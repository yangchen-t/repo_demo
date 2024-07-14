#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>

// 常用排序算法 random_shuffle  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10

void Print(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin(); it != v.end();it++)
    {
        std::cout << *it << " ";
    }
    std::cout << std::endl;    
}

void test01()
{
    srand((unsigned int) time(NULL));   // 随机数种子，以时间为基
    std::vector<int>v;
    for (int i = 0; i < MaxSize; i++)
    {
        v.push_back(i);
    }
    // 洗牌算法， 随机打乱
    random_shuffle(v.begin(), v.end());
    Print(v);
}

int main()
{
    test01();
    return 0;
}