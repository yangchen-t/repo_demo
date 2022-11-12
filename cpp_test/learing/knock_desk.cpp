#include <iostream>


using namespace std;



int main(){

    for (int i = 1; i < 100; i++)
    {
        if (i % 10 == 7 or i / 10 % 10 == 7 or i % 7 == 0){
            cout << "this is numbers satisty : " << i << " << knock_desk >> " << endl;
        }
        else {
            cout << i << endl;
        }
    }
    

    return 0;
}
