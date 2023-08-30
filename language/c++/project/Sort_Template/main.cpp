#include <iostream>
#include <string>
#include <list>


class Person 
{
public:
    Person(std::string name, int age, int height)
    {
        this->p_name = name;
        this->p_age = age;
        this->p_height = height; 
    }
    std::string p_name;
    int p_age;
    int p_height;
    ~Person(){};
private:
    int count;
};


void PrintMyPerson(const std::list<Person> &p);
void CreateList(std::list<Person>&P);
void MySort(std::list<Person>*p);
bool MyPersionCompate(Person &p1, Person &p2);
void test01();


int main()
{
    test01();
    return 0;
}


void test01()
{
    std::list<Person>P;
    CreateList(P);
    PrintMyPerson(P);
    MySort(&P);
    std::cout << "--" << std::endl;
    PrintMyPerson(P);
 
}

void PrintMyPerson(const std::list<Person>&p)
{
    for (std::list<Person>::const_iterator it = p.begin(); it != p.end(); it++)
    {
        std::cout << "name: " << it->p_name << " "
        << "age: " << it->p_age << " "
        << "height: " << it->p_height << std::endl;
    }
}

void CreateList(std::list<Person>&P)
{
    Person p1("张三", 20, 182);
    Person p2("李四", 10, 130);
    Person p3("王二", 30, 100);
    Person p4("麻子", 20, 190);

    P.push_back(p1);
    P.push_back(p2);
    P.push_back(p3);
    P.push_back(p4);
}

// Sort Conditions 
bool MyPersionCompate(Person &p1, Person &p2)
{
    if (p1.p_age == p2.p_age)
    { 
        return p1.p_height > p2.p_height;
    }else
    {
        return p1.p_age < p2.p_age;
    }
}

void MySort(std::list<Person> *p)
{
    p->sort(MyPersionCompate);
}
