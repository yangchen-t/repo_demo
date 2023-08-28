#pragma once
#include <iostream>

#include "worker.h"

using namespace std;


class Manager : public Worker
{
public:

    Manager(int id, string name, int department);

    virtual void showinfo();
    virtual string getdutyinfo();
};


