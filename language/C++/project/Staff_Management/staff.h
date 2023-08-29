#pragma once
#include <iostream>

#include "worker.h"

using namespace std;


class Staff : public Worker
{
public:

    Staff(int id, string name, int department);

    virtual void showinfo();
    virtual string getdutyinfo();
};


