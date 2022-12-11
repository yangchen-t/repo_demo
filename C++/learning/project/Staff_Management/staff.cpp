#include "staff.h"


Staff::Staff(int id, string name, int department)
{
    this->m_Id = id;
    this->m_Name = name;
    this->m_Department = department;
}

void Staff::showinfo()
{
    cout << "PID:  " << this->m_Id 
        << "\t NAME:  " << this->m_Name
        << "\t Post： " << this->getdutyinfo()
        << "\t Job Description:  To complete the leadership issued " << endl;
}


string Staff::getdutyinfo()
{
    return string("Staff");
}