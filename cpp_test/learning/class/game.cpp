#include <iostream>
#include "./include/Point.h"
#include "./include/Cricle.h"

using namespace std;

// class Point
// {
//     public:
//         void setxy(int x, int y)
//         {
//             C_x = x;
//             C_y = y;
//         }
//         int getx()
//         {
//             return C_x;
//         }
//         int gety()
//         {
//             return C_y;
//         }

//     private:
//         int C_x;
//         int C_y;
// };

// class Cricle
// {
//     public:
//         void setRadius(int R)
//         {
//             Radius = R;
//         }
//         int getRadius()
//         {
//             return Radius;
//         }
//         Point getCenter()
//         {
//             return Centerl;
//         }
//         void setcenterl(int x, int y)
//         {
//             Centerl.setxy(x, y);
//         }

//     private:
//         int Radius;
//         Point Centerl;
// };


void iswherePoint(Cricle &c, Point p)
{
    int distance = 
    (c.getCenter().getx() - p.getx()) * (c.getCenter().getx() - p.getx()) +
    (c.getCenter().gety() - p.gety()) * (c.getCenter().gety() - p.gety());

    int Rdistance = (c.getRadius() * c.getRadius());
    
    if (distance == Rdistance)
    {
        cout << "ok" << endl;
    }
    else if (distance > Rdistance)
    {
        cout << "out" << endl;
    }
    else
    {
        cout << "in" << endl;
    }
}

int main()
{
    Cricle c1;
    c1.setRadius(10);     // 半径
    c1.setcenterl(10,0);  // 圆心

    Point p1;
    p1.setxy(10,10);      // 点的坐标

    // 判断点的位置
    iswherePoint(c1,p1);

    return 0;
}