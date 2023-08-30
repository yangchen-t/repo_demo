#include <iostream>
#include <functional>

// 内建仿函数   算术仿函数 

// 二元 - 加法仿函数(plus)  and  一元 - 取余仿函数(negate)


void test01()
{
    std::negate<int>n;
    std::cout << n(50) << std::endl;
}

void test02()
{
    std::plus<int>p;
    std::cout << p(3,10) <<std::endl;
}

int main(){

    test01();
    test02();
    return 0;
}