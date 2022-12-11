#include <iostream>
#include <cstring>

using namespace std;

int main(){
	const int numbers = 0;
	int result ;
	char str1[100] = "pic path:/opt/qomolo";
	char str2[100] =  "/scripts";
	strcat(str1,str2);
	cout << str1 << endl;
	result = strcmp(str1,str2);
	cout << result << endl;
	cout << numbers << endl;
	if (result > numbers){
		cout << "str1 小于 str2" << endl;
	}else{
	cout << "str1 > str2" << endl;
	}
	return 0 ;
}
