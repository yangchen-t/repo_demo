#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// 常用拷贝算法 replace_if  
    // 查找内置数据类型 
    // 查找自定义数据类型

#define MaxSize 10

// fake function
void FF(int &v)
{
    std::cout << v << " ";
}

// 仿函数 谓词
class fakeFunc
{
public:
    bool operator()(const int &val)
    {   
        return val > 3;
    } 
};

void test01()
{
    std::vector<int>v;
    for (int i = 0; i < MaxSize; i++)
    {
        v.push_back(i);
    }
    for_each(v.begin(), v.end(), FF);
    std::cout << std::endl;
    replace_if(v.begin(), v.end(),fakeFunc() , 5);
    for_each(v.begin(), v.end(), FF);
}

int main()
{
    test01();
    return 0;
}