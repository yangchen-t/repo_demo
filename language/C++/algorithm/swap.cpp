#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用拷贝算法 swap  
    // 查找内置数据类型 
    // 查找自定义数据类型


void FF(const int &v)
{
    std::cout << v  << " ";
}

void test01()
{   
    std::vector<int>v1;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    std::vector<int>v2;
    for (int i = 10; i > 0; i--)
    {
        v2.push_back(i);
    }
    
    for_each(v1.begin(), v1.end(),FF);
    std::cout << std::endl;
    for_each(v2.begin(), v2.end(),FF);
    std::cout << std::endl;
    swap(v1,v2);
    for_each(v1.begin(), v1.end(),FF);
    std::cout << std::endl;
    for_each(v2.begin(), v2.end(),FF);

}

int main()
{
    test01();
    return 0;
}