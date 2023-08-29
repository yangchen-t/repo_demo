#include <iostream>


using namespace std;


int main(){

    int arr[3][3] = 
    {
        {100,100,100},
        {90,50,100},
        {60,70,80}
    };

    int a[] = {1,2,3};
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
    {
        int count = 0 ;
        for (int j = 0; j < sizeof(arr[0])/sizeof(arr[0][0]); j++)
        {   
            count +=arr[i][j];
        }   
        cout << a[i] << " ==> " << count << endl;

        
    }
    

    return 0;
}