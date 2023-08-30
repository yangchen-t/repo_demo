#pragma once
#include <iostream>
#include "Point.h"

using namespace std;

class Cricle
{
    public:
        void setRadius(int R);
        int getRadius();
        Point getCenter();

        void setcenterl(int x, int y);
    private:
        int Radius;
        Point Centerl;
};
