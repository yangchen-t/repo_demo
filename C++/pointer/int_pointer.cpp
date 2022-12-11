#include <iostream>

using namespace std;

int main(){
	
	int var =20;
	int A = 40;
	int& B = A;
	int *ip;
	ip = &var;
	
	cout << *ip << endl;
	cout << ip << endl;
	cout << "A position: "<< &A << endl;
	cout << A << endl;
	cout << "B position:" << &B << endl;
	return 0;
}
