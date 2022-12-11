#include <iostream>

using namespace std;

int main(){
    

    int score = 0;
    cout << "请输入分数： " << endl;
    cin >> score;
    if (score > 600){
        cout << "恭喜你考上一本大学" << endl;
        if (score > 700){
            cout << "你可以上北大" << endl;
        }
        else if (score > 650){
            cout << "你可以上清华"  << endl; 
        }
        else{
            cout << "你可以上人大"  << endl;
        }
    }
    else if (score > 500){
        cout << "恭喜你考上二本大学" << endl;        
    }
    else if (score > 400){
        cout << "恭喜你考上一本大学" << endl;
    }
    else {
        cout << "再接在励！！" << endl;
    }

    return 0 ;
}