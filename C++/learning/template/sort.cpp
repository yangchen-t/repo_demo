#include <iostream>
#include <string>

using namespace std;

template<typename T>
void Swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

// Exchange sort algorithm 
template<typename T>
void Sort(T arr[], int len)
{
    for (int  i = 0; i < len; i++)
    {
        int max = i;
        for (int j = i+1; j < len; j++)
        {
            if (arr[max] < arr[j])
            {
                max = j;
            }
        }
        if (max != i)
        {
            Swap(arr[max], arr[i]); // TODO
        }   
    }
}

template<typename T>
void printarr(T arr[], int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}


void test01()
{
    // create char array;
    char chararr[] = "scgahdbte";
    int len = sizeof(chararr)/sizeof(char);
    Sort(chararr, len);
    printarr(chararr, len);
}   

void test02()
{
    // create int array;
    int intarr[] = {9,2,3,4,1,6,8};
    int len = sizeof(intarr)/sizeof(int);
    Sort(intarr, len);
    printarr(intarr, len);
}

int main()
{
    // test01();
    test02();
    return 0;
}


