#include <iostream>

using namespace std;

int main(){
    int b{5};
    int a{7};
    int c{0};
    
    c = (a  > b ? a : b);
    // (a > b ? a:b) = 100;   // 返回的值为变量，可以继续赋值
    if (c == a){ 
        cout << "meet the condition" << endl;
        cout << c << endl;
    }
    else {
        cout << "condition not met" << endl;
        cout << c << endl;
    }

    return 0;
}