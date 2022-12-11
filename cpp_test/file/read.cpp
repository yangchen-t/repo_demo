#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void test01()
{

    fstream ifs;
    ifs.open("test.h", ios::in);
    if (!ifs.is_open())
    {
        cout << "file open is failed" << endl;
        return;
    }

// i
    // char buf[1024] = {0};
    // while (ifs >> buf)
    // {
    //     cout << buf << endl;
    // }

// ii 
    // char buf[1024] = {0};
    // while (ifs.getline(buf, sizeof(buf)))
    // {
    //     cout << buf <<endl;
    // }

// iii 
    // string buf;
    // while (getline(ifs, buf))
    // {
    //     cout <<  buf << endl;
    // }
    
// iiii
    char s;
    while ( (s = ifs.get()) != EOF )  // EOF  end of file 
    {
        cout << s;
    }
    


    ifs.close();
}


int main()
{
    test01();
    return 0;
}