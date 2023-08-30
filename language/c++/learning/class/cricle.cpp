#include "./include/Cricle.h"


void Cricle::setRadius(int R)
{
    Radius = R;
}
int Cricle::getRadius()
{
    return Radius;
}
Point Cricle::getCenter()
{
    return Centerl;
}
void Cricle::setcenterl(int x, int y)
{
    Centerl.setxy(x, y);
}
