#include <stdio.h>
#include <iostream>


using namespace std; 


struct people
{
    int age;
    int id;
}a;//a代表什么？
 
typedef struct
{
    int age;
    int id;
}b;
  
  
int main()
{
	a.age = 20;
	cout << a.age << endl;
	b tom;
	tom.age = 100;
	cout << tom.age << endl;
    return 0;
}
