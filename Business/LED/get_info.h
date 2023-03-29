#pragma once 
#include <iostream>
#include "Obasic_types.h"
#include "bx_dual_sdk.h"
#include "bx_sdk_dual.h"


struct path_select
{
    Ouint8 * path;
    int numbers;
};
void gettime();
void turn_picture_display(int mode);
path_select * return_path(path_select * pl);