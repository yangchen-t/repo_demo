#pragma once           // 防止头文件重复包含
#include <iostream>    // 包含输入输出流
#include "worker.h"
#include "staff.h"
#include "manager.h"
#include "boss.h"

using namespace std;   // 使用标准命名空间


class WorkerManager
{
public:
    WorkerManager();

    void Show_Func();
// 0    
    void Exit_System();
// 1
    int m_staff;
    Worker ** m_workarray;
    void Add_Staff();
// 2

    ~WorkerManager();
};