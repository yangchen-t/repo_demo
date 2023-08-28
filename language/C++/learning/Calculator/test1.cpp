#include <iostream>
#include <string>


using namespace std;

class Calculator
{

public:

    void setnum(int n1, int n2)
    {
        this->num1 = n1;
        this->num2 = n2;
    }

    int opration(string opration_computor)
    {
        if (opration_computor == "+")
        {
            int num3 = num1 + num2;
            return num3;
        }
        else if (opration_computor == "-")
        {
            int num3 = num1 - num2 ;
            return num3; 
        }
        else if (opration_computor == "*")
        {
            int num3 = num1 * num2;
            return num3;
        }
        else if (opration_computor == "/")
        {
            int num3 = num1 / num2;
            return num3;
        }
        return 0;
    }

private:
    int num1;
    int num2;

};

void test01()
{
    Calculator c;
    c.setnum(10,20);
    cout << c.opration("/") << endl;
}

int main()
{
    test01();
    return 0;
}