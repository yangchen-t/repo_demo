#include <iostream>
#include <vector>
#include <algorithm>


void PrintVector(std::vector<int> v) 
{
    // for (int i = 0; i < v.size();i++)
    // {
    //     std::cout << v[i] << std::endl;
    // }
    for(std::vector<int>::iterator i = v.begin(); i!=v.end(); i++)
    {
        std::cout << *i  << std::endl;
    }
}

void test01()
{
    std::vector<int> v1;
    for (int i = 10; i > 0; i--)
    {
        v1.push_back(i);
    }
    PrintVector(v1);
    sort(v1.begin(), v1.end());
    PrintVector(v1);
}

int main(){
    test01();
    return 0;
}
