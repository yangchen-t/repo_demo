#pragma once 
#include <iostream>
#include <string>


#define MAX 1000

using namespace std;


struct People
{
    string name;
    int age;
    string sex;
    string position;
    string phone;
};

struct Addressbooks
{
    struct People p1[MAX];
    int size;
};

void print_start();
void print_people(Addressbooks abs, int i);
void add_people_info(Addressbooks * abs, int index);
void add_people(Addressbooks * abs);
void print_info(const Addressbooks abs, int len);
int isExist(const Addressbooks abs, string name);
void delete_p(Addressbooks * abs);
void search_p(Addressbooks * abs);
void modify_p(Addressbooks * abs);
void clean_p(Addressbooks * abs);
