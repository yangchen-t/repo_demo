
#include "include/getTime.h"
#include <functional>

#include "build/config.h"
#include "add/add.h"

int main()
{

    if (flag)
    {
        std::cout << "YES is true" << std::endl;
        std::cout << "test print:" << Add(1, 20) << std::endl;
    }
    else
    {
        std::plus<int> add;
        std::cout << add(1, 2) << std::endl;
        gettime();
    }
}