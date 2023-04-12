#include <iostream>


class Test 
{
public:
    Test(){};
    static void test();
    void runPrivateFunc()
    {
        this->PrivateFunc();
    }
    ~Test(){};
private:
    void PrivateFunc()
    {
        // std::cout << "PrivateFunc test msg" << std::endl;
        this->test();
    }
};

int main()
{
    // Test::test();
    Test t;
    t.runPrivateFunc();
    return 0;
}

void Test::test()
{
    std::cout << "test msg" << std::endl;
}



