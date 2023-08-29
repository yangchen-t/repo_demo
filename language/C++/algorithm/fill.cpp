#include <numeric>
#include <vector>
#include <iostream>
#include <algorithm>


void myPrint(int val)
{
    std::cout << val << " ";
}

void test01()
{
    std::vector<int>v;
    v.resize(20);
    std::fill(v.begin(), v.end(), 120);
    std::for_each(v.begin(), v.end(), myPrint);
    // std::cout << v.size() << std::endl;
}



int main()
{
    test01();
    return 0;
}