#include <iostream>
#include <cstdlib>
#include <string>


using namespace std;


int main(){


    string arr[] = {"MemFree", "Active(file)", "Inactive(file)", "SReclaimable"};
    long int memfree = 0;
    long int active = 0;
    long int inactive = 0;
    long int sr = 0;
    long int count = 0;

    memfree = system("cat /proc/meminfo | grep 'MemFree' | awk -F ':' '{print$2}' | awk -F 'k' '{print$1}'");
    active = system("cat /proc/meminfo | grep 'Active(file)' | awk -F ':' '{print$2}' | awk -F 'k' '{print$1}'");
    inactive = system("cat /proc/meminfo | grep 'Inactive(file)' | awk -F ':' '{print$2}' | awk -F 'k' '{print$1}'");
    sr = system("cat /proc/meminfo | grep 'SReclaimable' | awk -F ':' '{print$2}' | awk -F 'k' '{print$1}'");
    

    cout << "count:" << memfree + active + inactive + sr << endl;


    return 0 ;
}
