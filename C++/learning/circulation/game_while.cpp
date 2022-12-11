#include <iostream>
#include <ctime>

using namespace std;

int main(){

    srand((unsigned int)time(NULL));       // 随机种子，利用当前的时间生成随机数
    int numbers{rand()%100 + 1};
    
    cout << "random number is :" << numbers << endl;
    int input_num = 0;
    int timer = 5;
    while (input_num != numbers)
    {   
        cout << " << your have : " << timer << " retry >> " << endl;
        if (timer == 0) 
        {
            cout << "=== game over !! ===" << endl;
            break;
        }
        else{
            --timer;
        }
        cout << "please input 1~100 numebrs: " << endl;
        cin >> input_num;
        if (input_num > numbers){
            cout << "input numbers is big" << endl;
            continue;
        }
        else if (input_num < numbers)
        {
            cout << "input numbers is small" << endl;
            continue;
        }
        else{
            cout << "this`s right !! " << endl;
        }
    }
    return 0;
} 