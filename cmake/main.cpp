
#include <functional>
#include <iostream>
#include "build/config.h"
#include "include/color_tools.h"
#include "include/getTime.h"

#ifdef USE_MYMATH
    #include <math/math.h>
#else
  #include <math.h>
#endif

// using namespace Color;

int main()
{
#ifdef USE_MYMATH
    gettime();
    std::cout << "Now we use our own Math library." << std::endl;
    std::cout << "test print:" << Add(1, 20) << std::endl;
    std::string test = "bule test print";
    Color::bule(test);
#else
    std::cout << "Now we use the standard library." << std::endl;
    std::plus<int> add;
    std::cout << add(1, 2) << std::endl;
    Color::black("black test print");
#endif
    Color::yellow("yellow test print");
    return 0;
}