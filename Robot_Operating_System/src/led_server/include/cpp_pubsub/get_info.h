#pragma once 
#include <iostream>
#include "Obasic_types.h"
#include "bx_dual_sdk.h"
#include "bx_sdk_dual.h"


// extern const std::string PicturesPath = "/debug/test";
// extern const std::string PicturesNumbersPath = "/scripts/pic/lib/numbers.csv";


struct path_select
{
    std::string path;
    int numbers;
};
void gettime();
void turn_picture_display(int mode);
