#include <iostream> 

using namespace std;

char strlist[] = "str test";
char *id = strlist;

int main(){
	cout << strlist << endl;
	cout << &id << endl;
	cout << id << endl;
	return 0 ;
}
