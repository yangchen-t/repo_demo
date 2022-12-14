#include <iostream>
#include "workermanage.h"

#include "worker.h"
#include "staff.h"
#include "manager.h"
#include "boss.h"


using namespace std;

int main()
{
    WorkerManager WM;
    int Choose = 0;

    while (true)
    {
        WM.Show_Func();
        cout << "please input your want opration number: " << endl;
        cin >> Choose;    // received opration
        switch (Choose)
        {
        case 0:
            WM.Exit_System();
            break;
        case 1:
            WM.Add_Staff();
            break;
        case 2:
            WM.show_staff();
            break;
        case 3:
            break;
        case 4:
            break;
        case 5:
            break;
        case 6:
            break;
        case 7:
            break;
        default:
            cout << "I do not understand you" << endl;
            break;
        }
        // system("clear");
    }
    return 0;
}


// void test01()
// {
//     Worker * worker = NULL;
//     worker = new Staff(1, "张三", 1);
//     worker->showinfo();
//     delete worker;
//     worker = new Manager(2, "李四", 2);
//     worker->showinfo();
//     delete worker;
//     worker = new Boss(3, "王二", 3);
//     worker->showinfo();
//     delete worker;   
// }