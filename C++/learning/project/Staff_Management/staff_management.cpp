#include <iostream>
#include "workermanage.h"


using namespace std;



int main()
{
    WorkerManager worker;
    int Choose = 0;


    while (true)
    {
        worker.Show_Func();
        cout << "please input your wank opration number: " << endl;
        cin >> Choose;
        switch (Choose)
        {
        case 0:
            worker.Exit_System();
            break;
        case 1:
            break;
        case 2:
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
        system("clear");

    }



    return 0;
}