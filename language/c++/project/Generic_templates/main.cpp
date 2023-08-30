#include <iostream>
#include "MyArray.hpp"

using namespace std;

void test01()      // 因为是函数数据 在栈上，执行完毕会自动释放
{
    MyArray<int> arr1(5);     //  有参构造
    MyArray<int> arr2(arr1);  //  拷贝构造
    MyArray<int> arr3(100);   //  有参构造
    arr3 = arr1;              //  opertor=
}
void test02()
{
    MyArray<int> arr1(5);
    for (int i = 0; i < 5; i++)
    {
        // 利用尾插法 循环插入数据
        arr1.Push_Back(i);
    }
    arr1.Get_size();
}

int main()
{
    test01();
    test02();
    return 0;
}