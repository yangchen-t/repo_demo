#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>

// 内建函数 - 关系仿函数 - 大于仿函数

class myCompare
{
public:
    bool operator ()(int v1, int v2)
    {
        return v1 > v2;
    }
};

void printMyVector(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin();it != v.end();it++)
    {
        std::cout << *it << std::endl;
    }
}

void mySort(std::vector<int> *v)
{
    // sort(v->begin(),v->end(), myCompare());   // myCompare() 匿名函数对象
    sort(v->begin(), v->end(), std::greater<int>());
}

int test01() 
{
    std::vector<int>v;
    v.push_back(30);      
    v.push_back(20);
    v.push_back(10);
    v.push_back(60);
    v.push_back(70);
    v.push_back(80);
    printMyVector(v);
    mySort(&v);
    std::cout << "sort end" << std::endl;
    printMyVector(v);
    return 0;
}

int main()
{
    test01();
    return 0;
}