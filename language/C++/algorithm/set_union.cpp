#include <iostream>
#include <vector>
#include <algorithm>


void test01(){
    std::vector<int> v1;
    std::vector<int> v2;

    for (int i = 0; i < 10; i++)
    {
        v1.push_back(i);
        v2.push_back(i +5);
    }
    
    std::vector<int> v3;
    v3.resize(v1.size() + v2.size());
    std::vector<int>::iterator End = std::set_union(v1.begin(),v1.end(),v2.begin(),v2.end(),v3.begin());

    for (std::vector<int>::iterator it = v3.begin() ; it < End; it++)
    {
        std::cout <<*it << std::endl;
    }
    
}

int main(){

    test01();
    return 0;
}