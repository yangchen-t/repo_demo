#pragma once 
#include <iostream>
#include "Obasic_types.h"
#include "bx_dual_sdk.h"
#include "bx_sdk_dual.h"


struct path_select
{
    std::string path;
    int numbers;
};
void gettime();
Ouint8 * TypeConversion(std::string str);
void turn_picture_display(int mode);
path_select return_path();