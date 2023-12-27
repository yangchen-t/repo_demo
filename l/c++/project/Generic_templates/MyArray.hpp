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
        // cout << "有参构造" << endl;
        this->C_Capacity = capacity;
        this->C_Size = 0;
        this->pAddress = new T[this->C_Capacity];
    }

    // 拷贝构造
    MyArray(const MyArray & arr)
    {
        // cout << "拷贝构造" << endl;
        this->C_Capacity = arr.C_Capacity;
        this->C_Size = arr .C_Size;
        this->pAddress = new T[arr.C_Capacity];  //  深拷贝
        // 假设数组有数据情况下,进行数据拷贝
        for (int i = 0; i < this->C_Size; i++)
        {
            this->pAddress[i] = arr.pAddress[i];
        } 
    }

    // operator= 防止浅拷贝问题
    MyArray & operator=(const MyArray & arr)
    {
        // cout << "operator=" << endl;
        if (this->pAddress != NULL)
        {
            delete [] this->pAddress;
            this->pAddress = NULL;
            this->C_Capacity = 0;
            this->C_Size = 0;
        }
        this->C_Capacity = arr.C_Capacity;
        this->C_Size = arr .C_Size;
        this->pAddress = new T[arr.C_Capacity];  
        // 假设数组有数据情况下,进行数据拷贝
        for (int i = 0; i < this->C_Size; i++)
        {
            this->pAddress[i] = arr.pAddress[i];
        }
        return * this;
    }

    // 尾插法
    void Push_Back(const T & val)
    {
        // 判断容量是否等于大小
        if (this->C_Capacity == this->C_Size)
        {
            cout << "capcacity is Max";
            return;
        }
        this->pAddress[this->C_Size] = val; // insert new var
        this->C_Size++;      // update array size
    }

    // 尾删法
    void Pop_Back()
    {
        // 让用户访问不到最后一个元素  <逻辑删除>
        if (this->C_Size == 0)
        {
            cout << "size is emtry";
            return;
        }
        this->C_Size--;
    }

    // 下标访问
    T& operator[](int index)
    {
        return this->pAddress[index];
    }

    // return size
    void Get_size()
    {
        cout << "size :" << this->C_Size << endl;
    }

    // return capacity
    void Get_capacity()
    {
        cout << "capacity" << this->C_Capacity << endl;
    }

    ~MyArray()
    {
        if (this->pAddress != NULL)
        {
            // cout << "析构" << endl;
            delete[] this->pAddress;
            this->pAddress =  NULL;
        }
    }

private:
    T * pAddress;  // 指针指向堆区开辟的真实数组
    int C_Capacity;
    int C_Size;
};


 