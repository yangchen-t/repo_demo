#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	ifstream ifs;
	ifs.open("test.txt",ios::in);
	if (!ifs.is_open()){
		cout << "file open faild" << endl;	
	}else{
		char buf[1024] = { 0 };
		int numbers = 1;
		while (ifs >> buf) {
			cout << numbers++ << endl;
			cout << buf << endl;
	//		break;
		}
		cout << "file open success" << endl;
	}
	return 0;
		
}
