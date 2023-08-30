#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用查找算法 adjacent_find  
    // 查找内置数据类型 
    // 查找自定义数据类型


void test01()
{
    std::vector<int>v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(1);
    if (adjacent_find(v.begin(), v.end()) == v.end())
    {
        std::cout << "not found" << std::endl;
    } else {
        std::cout << *adjacent_find(v.begin(), v.end()) << std::endl;
    }
}

int main()
{  
    test01();
    return 0;
}