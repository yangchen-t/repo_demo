#include <iostream>
#include <vector>
#include <algorithm>

void myPrint(int val)
{
    std::cout << val << std::endl;
}

void test01()
{
    std::vector<int> v1; 
    std::vector<int> v2;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
        v2.push_back(i + 3);
    }
    
    std::vector<int> v;
    v.resize(std::max(v1.size(),v2.size()));
    std::vector<int>::iterator isEnd = std::set_difference
    (
        v1.begin(),v1.end(), v2.begin(), v2.end(),v.begin()
    );
    std::for_each(v.begin(),isEnd, myPrint);
}

int main()
{
    test01();
    return 0;
}