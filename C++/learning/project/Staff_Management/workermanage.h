#pragma once           // 防止头文件重复包含
#include <iostream>    // 包含输入输出流
#include <fstream>
#include "worker.h"
#include "staff.h"
#include "manager.h"
#include "boss.h"

#define FILENAME "staff_msg.txt"

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
    bool m_FILEISEMPTY;
    void Add_Staff();
    void save();
    int get_staffnum();
    void init_staff();
// 2
    void show_staff();


    ~WorkerManager();
};