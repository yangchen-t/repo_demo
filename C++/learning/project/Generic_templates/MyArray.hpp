#pragma once
#include <iostream>
#include <string>
using namespace std;


template <class T>
class MyArray
{

public:
    // 有参构造
    MyArray(int capacity)
    {
        this->C_Capacity = capacity;
        this->C_Size = 0;
        this->pAddress = new T[this.C_Capacity];
    }

    // 拷贝构造
    MyArray(const MyArray & arr)
    {
        this->C_Capacity = arr.C_Capacity;
        this->C_Size = arr .C_Size;
        this->pAddress = new T[arr.C_Capacity]；  //  深拷贝
        // 假设数组有数据情况下,进行数据拷贝
        for (int i = 0; i < this,C_Size; i++)
        {
            this.pAddress[i] = arr->pAddress[i];
        } 
    }

    ~MyArray()
    {
        if (this->pAddress != NULL)
        {
            delete[] this->pAddress;
            this->pAddress =  NULL;
        }
    }

private:
    T * pAddress;  // 指针指向堆区开辟的真实数组
    int C_Capacity;
    int C_Size;
};


 