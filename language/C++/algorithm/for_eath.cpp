#include <iostream>
#include <vector>
#include <algorithm>

// 常用遍历算法 for_each 


// 普通函数
void print01(int val)
{
    std::cout << val << " ";
}

// 仿函数
class print02{
public:
    void operator()(int val)
    {
        std::cout << val << " ";
    }
};

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < int(10); i++)
    {
        v.push_back(i);
    }
    for_each(v.begin(), v.end(), print01);
    std::cout << "============" << std::endl;
    for_each(v.begin(), v.end(), print02());
}

int main()
{
    test01();
}