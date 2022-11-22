#include <iostream>
#include <string>

using namespace std;


class Cube
{
    public:
        int get_L()
        {
            return m_L;
        }
        int get_W()
        {
            return m_W;
        }
        int get_H()
        {
            return m_H;
        }
        int set_L(int L)
        {
            m_L = L;
            return 1;
        }
        int set_W(int w)
        {
            m_W = w;
            return 1;
        }
        int set_H(int h)
        {
            m_H = h;
            return 1;
        }

        int getArea()
        {
            return m_L * m_W * m_H; 
        }
        int getVolume()
        {
            return 2 * ((m_L * m_W) + (m_L * m_H) + (m_H * m_W));
        }

        bool isSamebyclass(Cube &c2)
        {   
            if (m_L == c2.get_L() && m_H == c2.get_H() && m_W == c2.get_W())
            {
                return true;
            }
            return false;
        }

    private:
        int m_L, m_W, m_H;
};

bool isSame(Cube &c1, Cube &c2)
{
    if (c1.get_H() == c2.get_H() && c1.get_L() == c2.get_L() && c1.get_W() == c2.get_W())
    {   
        return true;
    }
    return false;
}



int main()
{
    Cube c1;
    
    c1.get_W();
    c1.set_H(8);
    c1.set_L(7);
    c1.set_W(3);

    Cube c2;

    c2.set_H(8);
    c2.set_L(7);
    c2.set_W(3);


    bool ret = c1.isSamebyclass(c2);
    if (ret)
    {
        cout << "yes" << endl;
    }
    else
    {
        cout << "no" << endl;
    }

    if (isSame(c1, c2))
    {
        cout << "相同！" << endl;
    }
    else
    {
        cout << "不同！" << endl; 
    }

    return 0;
}