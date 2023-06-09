#include <iostream>
// #include "build/config.h"
#include "include/getTime.h"
#include "add/add.h"

// #ifdef USE_MYADD
//     #include "add/add.h"
// #else
//     #include "include/getTime.h"
// #endif

int main()
{
        std::cout << "test print:" << Add(1,2)<< std::endl;
        gettime();
}