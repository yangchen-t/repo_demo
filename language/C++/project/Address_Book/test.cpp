#include <iostream>

using namespace std;

#define PI 3.14

class person
{
    public:
        person():m_a(PI),m_b(20),m_c(23){};
        double m_a, m_b, m_c;

};


int main()
{
    person c;

    cout << c.m_a << endl;

    return 0;
}