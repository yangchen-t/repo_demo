#include <iostream>
using namespace std;

extern int count;

void test_func()
{
	int count = 20;	
	int var = 10;
	cout << "this is test scripts : " << count << endl;
	cout << "var position:" << &var << endl;
}

