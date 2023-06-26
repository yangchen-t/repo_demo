
#include <functional>
#include <iostream>
#include "build/config.h"

#ifdef USE_MYMATH
  #include <math.hpp>
#else
  #include <math.h>
#endif


int main()
{
#ifdef USE_MYMATH
    std::cout << "Now we use our own Math library." << std::endl;
    std::cout << "YES is true" << std::endl;
    std::cout << "test print:" << Add(1, 20) << std::endl;
#else
    std::cout << "Now we use the standard library." << std::endl;
    std::plus<int> add;
    std::cout << add(1, 2) << std::endl;
#endif
    
    std::cout <<"test" << std::endl;
    return 0;
}