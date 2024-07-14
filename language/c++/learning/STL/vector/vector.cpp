// 内置数据类型存放

#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>  // 标准算法库

void my_print(int val)
{
    cout << val << endl;
}

void test01()
{
    vector<int> v;  // 创建vector数组
    // 尾插法
    v.push_back(10);
    v.push_back(20);

    vector<int>::iterator itBegin = v.begin();  // 初始迭代器， 指向第一个元素
    vector<int>::iterator itEnd = v.end();      // 结束迭代器， 指向最后一个元素的下一个位置

    // template 1 
    while (itBegin != itEnd)
    {
        cout <<*itBegin << endl;
        itBegin++;
    }
 
    // template 2 
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++)
    {
        cout <<*it << endl;
    }

    // template 3
    // STL 提供标准遍历算法 头文件 algorithm
    for_each(v.begin(), v.end(), my_print);
}


int main()
{
    test01();

    return 0;
}