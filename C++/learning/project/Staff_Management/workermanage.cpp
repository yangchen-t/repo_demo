#include "workermanage.h"




WorkerManager::WorkerManager()
{
    // file is not exist
    ifstream ifs;
    ifs.open(FILENAME, ios::in);
    if (!ifs.is_open())
    {
        cout << "file is not exist！" << endl;
        this->m_staff = 0;
        this->m_workarray = NULL;
        this->m_FILEISEMPTY = true;
        ifs.close();
        return;
    } 
    // data is empty
    char ch;
    ifs >> ch;
    if (ifs.eof())
    {
        cout << "data is empty！" << endl;
        this->m_staff = 0;
        this->m_workarray = NULL;
        this->m_FILEISEMPTY = true;
        ifs.close();
        return;    
    }
    // read file to display
    int num = this->get_staffnum();
    // cout << "count staff " << num << endl;
    this->m_staff = num;

    this->m_workarray = new Worker * [this->m_staff];
    this->init_staff();

    // for (int i = 0; i < m_staff; i++)
    // {
    //     cout << "Pid: " << this->m_workarray[i]->m_Id << ""
    //     << "name: " << this->m_workarray[i]->m_Name << ""
    //     << "Post: " << this->m_workarray[i]->m_Department << endl;
    // }
    
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
        this->m_FILEISEMPTY = false;
        cout << "!<< Congratulations add " << AddNum << " new staff >>!" << endl;
        this->save();
    }
    else 
    {
        cout << "input error"  << endl;
    }
    system("sleep 5");
    system("clear");

}
void WorkerManager::save()
{
    ofstream ofs;
    ofs.open(FILENAME, ios::out);
    for (int i = 0; i < this->m_staff ; i++)
    {
        ofs << this->m_workarray[i]->m_Id << " "
        << this->m_workarray[i]->m_Name << " "
        << this->m_workarray[i]->m_Department << " " << endl;
    }
    ofs.close();
}
int WorkerManager::get_staffnum()
{
    ifstream ifs;
    ifs.open(FILENAME, ios::in);
    int id;
    string name;
    int did;
    int count = 0;
    while (ifs >> id && ifs >> name && ifs >> did)
    {
        count++;
    }
    ifs.close();
    return count;
}
void WorkerManager::init_staff()
{
    ifstream ifs;
    ifs.open(FILENAME, ios::in);
    
    int id;
    string name;
    int did;

    int index = 0;
    while (ifs >> id && ifs >> name && ifs >> did)
    {
        Worker * worker = NULL;
        switch (did)
        {
        case 1:
            worker = new Staff(id, name, did);    
            break;        
        case 2:
            worker = new Manager(id, name, did);
            break;
        case 3:
            worker = new Boss(id, name, did);
            break;
        default:
            break;
        }
        this->m_workarray[index] = worker;
        index++;
    }
    ifs.close();
}

// 2 
void WorkerManager::show_staff()
{
    if (this->m_FILEISEMPTY)
    {
        cout << "file is exist or data is empty!" << endl;
    }
    else
    {
        for (int i = 0; i < this->m_staff; i++)
        {
            this->m_workarray[i]->showinfo();
        }
        
    }
    system("sleep 5");
    system("clear");
}



WorkerManager::~WorkerManager()
{
    if (this->m_workarray != NULL)
    {
        delete[] this->m_workarray;
        this->m_workarray = NULL;
    }
}

 