#include <iostream>

using namespace std;

int main(){

    int  score = 0;
    cout << "please rate the film ： " << endl;
    cin >> score;
    switch (score)
    {
    case 10:
        cout << "good" << endl;
        break;  
    
    default:
        break;
    }

    return 0;
}