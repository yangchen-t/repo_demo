#include "workermanage.h"




WorkerManager::WorkerManager()
{
    this->m_staff = 0;
    this->m_workarray = NULL;
}

void WorkerManager::Show_Func()
{
    cout << "=========================================" << endl; 
    cout << "Staff Management system" << endl;
    cout << " 0 ，Exit system " << endl;  
    cout << " 1 , Add staff Information " << endl;
    cout << " 2 , display staff Information " << endl;
    cout << " 3 , del staff " << endl;
    cout << " 4 , modify staff Information " << endl;
    cout << " 5 , select staff Information " << endl;
    cout << " 6 , sort staff Information " << endl;
    cout << " 7 , clear all Information and Documents " << endl;
    cout << "=========================================" << endl; 
}
// 0 
void WorkerManager::Exit_System()
{
    cout << "welcome play again ..." << endl;
    exit(-1);
}
// 1 
void WorkerManager::Add_Staff()
{
    cout << "please tell me your want add staff Quantity： " << endl;
    int AddNum = 0;
    cin >> AddNum; 
    if (AddNum > 0)
    {
        int NewSize = this->m_staff + AddNum;
        Worker ** newSpace = new Worker*[NewSize];
        if (this->m_workarray != NULL)
        {
            for (int i =0; i < this->m_staff; i++)
            {
                newSpace[i] = this->m_workarray[i];
            }
        }
        for (int i = 0; i < AddNum; i++)
        {
            int id;
            string name;
            int dselect;

            cout << "please input " << i + 1 << " new staff Quantity : " << endl;
            cin >> id;
            cout << "please input " << i + 1 << " new staff Name : " << endl;
            cin >> name;  
            cout << "please select staff post:" << endl;
            cout << " 1，Normal staff " << endl;
            cout << " 2, Manager " << endl;
            cout << " 3, Boss " << endl;
            cin >> dselect;
            Worker * addworker = NULL;
            switch (dselect)
            {
            case 1:
                addworker = new Staff(id, name, 1);
                break;
            case 2:
                addworker = new Manager(id, name, 2);
                break;            
            case 3:
                addworker = new Boss(id, name, 3);
                break;
            default:
                break;
            }
            newSpace[this->m_staff + i] = addworker;
        }
        
        delete[] this->m_workarray;
        this->m_workarray = newSpace;
        this->m_staff = NewSize;
        cout << "!<< Congratulations add " << AddNum << " new staff >>!" << endl;
    }
    else 
    {
        cout << "input error"  << endl;
    }
    system("sleep 5");
    system("clear");
}

WorkerManager::~WorkerManager(){}

 