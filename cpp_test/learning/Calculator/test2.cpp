#include <iostream>
#include <string>

using namespace std;

// 多态
class BaseCalculator
{
public:
    // local var
    int n1;
    int n2;

    virtual int get_result()
    {
        return 0;
    };


};

class AddCalculator : public BaseCalculator 
{
    int get_result()
    {
        return n1 + n2;
    }
};

class SubCalculator : public BaseCalculator 
{
    int get_result()
    {
        return n1 - n2;
    }
};

class MluCalculator : public BaseCalculator 
{
    int get_result()
    {
        return n1 * n2;
    }
};

void test01()
{
    BaseCalculator * abc = new AddCalculator;
    abc->n1 = 20;
    abc->n1 = 100;
    cout << abc->get_result() << endl;
    delete abc;

    abc = new MluCalculator;
    abc->n1 = 20;
    abc->n2 = 100;
    cout << abc->get_result() << endl;
    delete abc;
}

int main()
{
    test01();
    return 0;
}