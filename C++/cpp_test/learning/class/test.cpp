#include <iostream>
#include <string>

using namespace std;


struct stud
{
    string name;
    int student_numbers;
};

class student
{
    public:

    string name;
    int numbers;

    void print_inf(string name, int numbers) 
    {
        cout << "name is " << name << endl;
        cout << "numbers is " << numbers << endl;

    }

};

int main()
{
    student n1;
    n1.name = "张富豪";
    n1.numbers = 250;
    n1.print_inf(n1.name, n1.numbers);
    return 0;
}