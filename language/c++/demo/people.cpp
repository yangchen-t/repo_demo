#include <iostream>
#include <cstring>


using namespace std;
void print_people(struct people &p);

typedef struct PEOPLE
{
	char name[50];
	int age;
	char sex[20];
}people;


int main()
{
	people p1;
	people p2;

	strcpy(p1.name,"zhangfuhao");
	strcpy(p1.sex, "man");
	p1.age = 1000;
	
	strcpy(p2.name, "zhang");
	strcpy(p2.sex, "woman");
	p2.age = 1;

	print_people(p1);
	print_people(p2);

	return 0 ;
}

void print_people(struct people &p)
{
	cout << "====================================" << endl; 
	cout << "name:" << p.name << endl;
	cout << "age:" << p.age << endl;
	cout << "sex:" << p.sex << endl;
}
