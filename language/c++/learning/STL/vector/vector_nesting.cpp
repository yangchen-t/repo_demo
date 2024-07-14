#include<iostream>
#include<vector>
using namespace std;


void test01()
{
    vector<vector<int>> vv;
    vector<int>v1;
    vector<int>v2;
    vector<int>v3;
    vector<int>v4;
    // add data
    for (int i = 0; i < 4; i++)
    {
        v1.push_back(i + 1);
        v2.push_back(i + 3);
        v3.push_back(i + 5);
        v4.push_back(i + 7);
    }
    vv.push_back(v1);
    vv.push_back(v2);
    vv.push_back(v3);
    vv.push_back(v4);


    for (vector<vector<int>>::iterator it = vv.begin(); it != vv.end(); it++)
    {
        for (vector<int>::iterator vit = (*it).begin(); vit != (*it).end(); vit++)
        {
            cout << *vit << " ";
        }  
        cout << endl;   
    }
}

int main()
{
    test01();
    return 0;

}