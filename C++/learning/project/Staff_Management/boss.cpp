#include "boss.h"


Boss::Boss(int id, string name, int department)
{
    this->m_Id = id;
    this->m_Name = name;
    this->m_Department = department;
}

void Boss::showinfo()
{
    cout << "PID:  " << this->m_Id 
        << "\t NAME:  " << this->m_Name
        << "\t Post： " << this->getdutyinfo()
        << "\t Job Description:  Send out the mission/Task!" << endl;
}


string Boss::getdutyinfo()
{
    return string("Boss");
}