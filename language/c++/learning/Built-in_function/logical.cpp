#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>


// 内置函数 - 逻辑内置函数 - 逻辑非

void printMyVector(std::vector<bool> b)
{
    for (std::vector<bool>::iterator it = b.begin(); it != b.end(); it++)
    {
        std::cout << *it << " ";
    }
     std::cout << "" << std::endl;
}

void test01()
{
    std::vector<bool>b;
    b.push_back(true);
    b.push_back(false);
    b.push_back(true);
    b.push_back(false);
    printMyVector(b);
    std::vector<bool>v2;
    v2.resize(b.size());
    std::transform(b.begin(),b.end(),v2.begin(), std::logical_not<bool>());
    printMyVector(v2);
}

int main()
{
    test01();
    return 0;
}