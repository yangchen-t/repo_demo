#include <numeric>
#include <iostream>
#include <vector>

const int count = 100;

void Print(std::vector<int> &v)
{
    for (std::vector<int>::iterator it = v.begin() ; it != v.end(); it++)
    {
        std::cout << *it << std::endl;
    }
    
}

void test()
{
    std::vector<int>v;
    for (int i = 0; i < count; i++)
    {
        v.push_back(i);
    } // 5050
    // Print(v);
    int total = std::accumulate(v.begin(),v.end(),0);
    // Print(v);
    std::cout << total << std::endl;
}


int main()
{
    test();
    return 0;
}