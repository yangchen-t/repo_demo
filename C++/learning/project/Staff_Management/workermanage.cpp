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
        // create new space
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
            if (this->isRepetition(id))
            {
                cout << "id is repeat" << endl;
                return;
            }
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
            newSpace[this->m_staff + i] = addworker;   // add new staff 
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
    return count;   // count data 
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
        this->m_workarray[index] = worker;  //  add new array size;
        index++;
    }
    ifs.close();
}
bool WorkerManager::isRepetition(int id)
{
    bool Flag = false;
    for (int i = 0; i < m_staff; i++)
    {
        if (this->m_workarray[i]->m_Id == id)
        {
            Flag = true;
            break;
        }
    }
    return Flag;
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
    system("sleep 2");
    // system("clear");
}

// 3 
int WorkerManager::isExist(int id)
{
    int index = -1;
    for (int i = 0; i < this->m_staff; i++)
    {
        if (this->m_workarray[i]->m_Id == id)
        {
            index = i;
            break;
        }
    } 
    return index;
} 

void WorkerManager::Del_Staff()
{
    if (this->m_FILEISEMPTY)
    {
        cout << "file open failed or file is not exist" << endl;
    }
    else
    {
        cout << "please input want del staff number or id" << endl;
        int index = 0;
        cin >> index;
        int ret = this->isExist(index);
        if (ret != -1)
        {
            for (int i = ret; i < this->m_staff -1; i++)
            {
                this->m_workarray[i] = this->m_workarray[i+1];
            }
            this->m_staff--;
            cout << "del finish" << endl;
            this->save();
        }
        else
        {
            cout << "input id is invaild!" << endl;
        }
    }
}
// 4 
void WorkerManager::Modify_staff()
{
    if (this->m_FILEISEMPTY)
    {
        cout << "file open failed or file is not exist" << endl;
    }
    else
    {
        int index = 0;
        cout << "please input want modify staff id" << endl;
        cin >> index;
        int ret = this->isExist(index);
        if (ret != -1)
        {
            delete this->m_workarray[ret];
            int newid = 0;
            string newname = "";
            int newDepartment = 0;

            cout << "select finish id: " << index << endl;
            cout << "please modify new staff id: " << endl;
            cin >> newid;
            cout << "please modify new staff name: " << endl;
            cin >> newname;
            cout << "please select staff post:" << endl;
            cout << " 1，Normal staff " << endl;
            cout << " 2, Manager " << endl;
            cout << " 3, Boss " << endl;
            cin >> newDepartment; 
            Worker * addworker = NULL;
            switch (newDepartment)
            {
            case 1:
                addworker = new Staff(newid, newname, newDepartment);
                break;
            case 2:
                addworker = new Manager(newid, newname, newDepartment);
                break;            
            case 3:
                addworker = new Boss(newid, newname, newDepartment);
                break;
            default:
                break;
            }
            this->m_workarray[ret] = addworker;
            cout << "success" << endl;
            this->save();
        }
        else
        {
            cout << "Modify failed, index select is not exist" << endl; 
        }

    }

}
// 5 
void WorkerManager::Find_staff()
{
    if (this->m_FILEISEMPTY)
    {
        cout << "file open failed or file is not exist" << endl;
    }
    else
    {
        cout << "Please select how you want to find it" << endl;
        cout << "1. Search by employee number" << endl;
        cout << "2. Search by employee name" << endl;
        int select = 0;
        cin >> select;
        if (select == 1)
        {
            cout << "please input search staff id: " << endl;
            int id = 0;
            cin >> id;
            if (this->isExist(id) != -1)
            {
                cout << "search finish, print msg" << endl;
                this->m_workarray[this->isExist(id)]->showinfo();
            }
            else
            {
                cout << "search failed" << endl;
            }
        }
        else if (select == 2)
        {
            string newname;
            cout << "please input search staff name:" << endl;
            cin >> newname;
            bool flag = false;
            for (int i = 0; i < m_staff; i++)
            {
                if (this->m_workarray[i]->m_Name == newname)
                {
                    flag = true;
                    this->m_workarray[i]->showinfo();
                }
            }
            if (!flag)
            {
                cout << "search error,please retry!" << endl;
            }
        }
        else
        {
            cout << "Do not understand what you want to use the search method" << endl;
        }
    
         
    }
}
// 6 
void WorkerManager::Sort_staff()
{
    if (this->m_FILEISEMPTY)
    {
        cout << "file open failed or file is not exist" << endl;
    }
    else
    {
        int select = 0;
        cout << "Select the method for sorting" << endl;
        cout << "1. Positive order" << endl;
        cout << "2. Reverse  order" << endl;
        cin >> select;
        for (int i = 0; i < this->m_staff; i++)
        {
            int minormax = i;
            for (int j = i+1 ; j < this->m_staff; j++)
            {
                if (select == 1)
                {
                    if(this->m_workarray[minormax]->m_Id > this->m_workarray[j]->m_Id)
                    {
                        minormax = j;
                    }
                }
                else
                {
                    if(this->m_workarray[minormax]->m_Id < this->m_workarray[j]->m_Id)
                    {
                        minormax = j;
                    }
                }
            }

            if (i != minormax)
            {
                Worker * temp = this->m_workarray[i];
                this->m_workarray[i] = this->m_workarray[minormax];
                this->m_workarray[minormax] = temp;
            }
        } 
    }
    cout << "sort success" << endl;
    this->save();
    this->show_staff();
}
// 7 
void WorkerManager::Clear_staff()
{
    cout << "Are you sure you want to clear everything?" << endl;
    cout << "1. Y" << endl;
    cout << "2. N" << endl;
    int select = 0;cin >> select;
    if (select == 1)
    {
        ofstream ofs(FILENAME, ios::trunc);
        ofs.close();

        if (this->m_workarray != NULL)
        {
            for (int i = 0; i < m_staff; i++)
            {
                if (this->m_workarray[i] != NULL)
                {
                    delete this->m_workarray[i];
                    this->m_workarray[i] = NULL;
                }
            }
            this->m_staff = 0;
            delete[] this->m_workarray;
            this->m_workarray = NULL;
            this->m_FILEISEMPTY = true;
        }
    }
    cout << "clear finish" << endl;
}

WorkerManager::~WorkerManager()
{
    if (this->m_workarray != NULL)
    {
        for (int i = 0; i < m_staff; i++)
        {
            if (this->m_workarray[i] != NULL)
            {
                delete this->m_workarray[i];                
            }
        delete[] this->m_workarray;
        this->m_workarray = NULL;
        }
    }
}

 