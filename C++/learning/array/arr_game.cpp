#include <iostream>

using namespace std;


int main(){
    

    int arr[] = {300,350,800,400,250};

    int max = 0;

    for (int i = 0; i < (sizeof(arr)/sizeof(arr[0])) ; i++)
    {
        max = max > arr[i] ? max : arr[i];
    }
    cout << max << endl;
    

    return 0;
}