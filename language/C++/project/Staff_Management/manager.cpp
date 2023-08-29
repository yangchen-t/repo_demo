#include "manager.h"


Manager::Manager(int id, string name, int department)
{
    this->m_Id = id;
    this->m_Name = name;
    this->m_Department = department;
}

void Manager::showinfo()
{
    cout << "PID:  " << this->m_Id 
        << "\t NAME:  " << this->m_Name
        << "\t Post： " << this->getdutyinfo()
        << "\t Job Description:  Give orders to the boss and finish them " << endl;
}


string Manager::getdutyinfo()
{
    return string("manager");
}