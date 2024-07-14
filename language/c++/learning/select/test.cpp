#include <iostream>

using namespace std;

int third_max(int a,int b,int c);

int main(){
    int pigA = 0;
    int pigB = 0;
    int pigC = 0;
    cout << "依次输入小猪的体重： "  << endl;
    cin >> pigA;
    cin >> pigB;
    cin >> pigC;
    cout << "最重的小猪为： " << third_max(pigA,pigB,pigC) << endl;

    return 0;
}

int third_max(int a,int b,int c){
    if (a > b){
        if (a > c){
            return a;
        }   
        else{
            return c;
        }
    }
    else {
        if (b > c){
            return b ;
        }
        else {
            return c ;
        }
    }
} 