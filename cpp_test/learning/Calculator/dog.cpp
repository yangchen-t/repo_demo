#include <iostream>
#include <string>

using namespace std;

class Dog
{
public:
    virtual void run() = 0;
    virtual void eat() = 0;
    virtual void drink() = 0;
    virtual void speak() = 0 ;

    void makedog()
    {
        run();
        eat();
        drink();
        speak();
    }
};

class Yellow_Dog : public Dog
{
    virtual void run()
    {
        cout << "yellow dog is run" << endl;
    }
    virtual void eat()
    {
        cout << "current eat is good foot" << endl;
    }
    virtual void drink()
    {
        cout << "drink cola" << endl;
    }
    virtual void speak()
    {
        cout << "my name is yellow dog" << endl;
    }
};
class Blue_Dog : public Dog
{
    virtual void run()
    {
        cout << "Blue dog is run" << endl;
    }
    virtual void eat()
    {
        cout << "current eat is not good foot" << endl;
    }
    virtual void drink()
    {
        cout << "drink milk" << endl;
    }
    virtual void speak()
    {
        cout << "my name is bule dog" << endl;
    }
};


void make_dog(Dog * d)
{
    d->makedog();
    delete d;
}


void test01()
{
    // Dog * d = new Yellow_Dog;
    // d->makedog();
    // delete d;
    // d = new Blue_Dog;
    // d->makedog();
    make_dog(new Yellow_Dog);
};



int main()
{
    test01();
    return 0;
}