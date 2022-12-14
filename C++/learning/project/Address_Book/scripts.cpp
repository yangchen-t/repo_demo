#include <iostream>
#include <string>

#include "function_implementation.h"

int main(){

    Addressbooks abs;
    abs.size = 0;
    int len = sizeof(abs.p1)/sizeof(abs.p1[0]);

    int number = 0;
    while (true)
    {
        print_start();  
        cin >> number;
        switch (number)
        {
        case 1:
            add_people(&abs);
            break;
        case 2:
            print_info(abs, abs.size);
            break;
        case 3:
            delete_p(&abs);
            break;
        case 4:
            search_p(&abs);
            break;
        case 5:
            modify_p(&abs);
            break;
        case 6:
            clean_p(&abs);
            break;
        case 0:
            cout << "Welcome to use next time" << endl;
            return 0;
            break;
        // default:
        //     break;
        } 
    }
    return 0;
}