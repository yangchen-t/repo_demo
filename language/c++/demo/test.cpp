#include <iostream>


int count;
extern void test_func();

int main()
{
	count = 10;
	test_func();
}
