#include <iostream>


// reverse

using namespace std;


int main(){


    int arr[] = {1,2,3,4,5,6,7,8,9};

    int start = 0;
    int end = sizeof(arr) / sizeof(arr[0]) -1;
    int temp = 0;

    while (start < end)
    { 
        // 元素互换
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }

    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << endl;
    }



    return 0;
}