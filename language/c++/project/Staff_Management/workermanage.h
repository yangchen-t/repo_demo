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
    int m_staff;
    Worker ** m_workarray;
    bool m_FILEISEMPTY;

    WorkerManager();
    void Show_Func();
// 0    
    void Exit_System();
// 1
    void Add_Staff();
    void save();
    int get_staffnum();
    void init_staff();
    bool isRepetition(int id);
// 2
    void show_staff();
// 3
    int isExist(int id);
    void Del_Staff();
// 4 
    void Modify_staff();
// 5 
    void Find_staff();
// 6 
    void Sort_staff();
// 7 
    void Clear_staff();
    
    ~WorkerManager();
};