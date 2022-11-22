#pragma once
#include <iostream>
using namespace std;

class Point
{
    public:
        void setxy(int x, int y);
        int getx();
        int gety();
    private:
        int C_x;
        int C_y;
};
