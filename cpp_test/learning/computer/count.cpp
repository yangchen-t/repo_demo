#include <iostream>

using namespace std;


// 内置递减的重载方法：

class jian
{
    friend ostream & operator<<(ostream &cout, jian jianhao);

public:
    // 前置递减
    jian& operator--()
    {
        --my_num;
        return *this;
    } 
    // 后置递减
    jian operator--(int)
    {
        jian tmp = *this;
        this->my_num--;
        return tmp;
    }

private:
    int my_num = 5;
};


ostream & operator<<(ostream &cout, jian jianhao)
{
    cout << "my_num:  " << jianhao.my_num << endl;
    return cout;
}


// 前置递减测试
void test01()
{
    jian test;
    cout << --(--test) << endl;
    cout << test << endl;
}
// 后置递减测试
void test02()
{
    jian test;
    cout << (test--)-- << endl;
    cout << test << endl; 
}


int main()
{
    // test01();

    test02();

    return 0;
}