#include <iostream>


using namespace std;



int main(){

    int arr[] = {1,4,3,9,13,45,121,435,23};

    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;


    // 冒泡排序
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]) -1 ; i++)
    {
        for (int j = 0; j < sizeof(arr)/sizeof(arr[0]) -i -1 ; j++){
            if (arr[j] > arr[j+1]){
                int tmp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = tmp;
            }
        }
        
    }
    cout << "*" << endl;

    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;


    return 0;
}