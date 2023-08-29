#include <vector>
#include <iostream>
#include <algorithm>


void test01()
{
    std::vector<int>v1;
    std::vector<int>v2;
    std::vector<int>v3;
    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
    }
    for (int s = 5; s < 15; s++)
    {
        v2.push_back(s);
    }

    v3.resize(std::min(v1.size(), v2.size()));
    std::vector<int>::iterator isEnd = std::set_intersection(
        v1.begin(), v1.end(),v2.begin(), v2.end(), v3.begin()
    );
    for (std::vector<int>::iterator  it = v3.begin() ; it < isEnd; it++)
    {
        std::cout << *it << std::endl;
    }
    
    // std::vector<int>::iterator bing = std::set_union(
    //     v1.begin(), v1.end(),v2.begin(), v2.end(), v3.begin()
    // );
    // for (std::vector<int>::iterator  itb = v3.begin() ; itb < bing; itb++)
    // {
    //     std::cout << *itb << std::endl;
    // }

}

int main()
{
    test01();
    return 0;
}