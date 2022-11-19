#include <iostream>
#include <string>

using namespace std;

#define MAX 1000

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


int main(){

    Addressbooks abs;
    abs.size = 0;
    int len = sizeof(abs.p1)/sizeof(abs.p1[0]);


    int number = 0;
    while (true)
    {
        print_start();  
        cin >> number;
        switch (number)
        {
        case 1:
            add_people(&abs);
            break;
        case 2:
            print_info(abs, abs.size);
            break;
        case 3:
            delete_p(&abs);
            break;
        case 4:
            search_p(&abs);
            break;
        case 5:
            modify_p(&abs);
            break;
        case 6:
            clean_p(&abs);
            break;
        case 0:
            cout << "Welcome to use next time" << endl;
            return 0;
            break;
        // default:
        //     break;
        } 
    }
    return 0;
}

void print_start()
{
    cout << "*****************************" << endl;
    cout << "******  1, 添加联系人  ******" << endl;
    cout << "******  2, 显示联系人  ******" << endl;
    cout << "******  3, 删除联系人  ******" << endl;
    cout << "******  4, 查找联系人  ******" << endl;
    cout << "******  5, 修改联系人  ******" << endl;
    cout << "******  6, 清空联系人  ******" << endl;
    cout << "******  0, 退出通信录  ******" << endl;
    cout << "*****************************" << endl;
}

void print_people(Addressbooks * abs, int i)
{
    cout << "name：" << abs->p1[i].name << " ";
    cout << "sex：" << abs->p1[i].sex << " ";
    cout << "age：" << abs->p1[i].age << " ";
    cout << "addr：" << abs->p1[i].position << " ";
    cout << "phone：" << abs->p1[i].phone << " ";
    cout << endl;

}
// add info function
void add_people_info(Addressbooks * abs, int index)
{
    string name;
    cout << "输入姓名：" ;
    cin >> name;
    abs->p1[index].name = name; 
    int sex;
    cout << "输入性别" << endl;
    cout << "1=男或者2=女 : " ;
    while (true)
    {
        cin >> sex;
        if (sex == 1 or sex == 2)
        {
            if (sex == 1)
            {
                string sex = "男";
                abs->p1[index].sex = sex; 
                break;
            }
            else
            {
                string sex = "女";
                abs->p1[index].sex = sex; 
                break;
            }   
        }
        else
        {
            cout << "please retry input!" << endl;
        }
    }
    int age;
    cout << "输入年龄：" ;
    cin >> age;
    abs->p1[index].age = age; 
    string position;
    cout << "输入地址：" ;
    cin >> position;
    abs->p1[index].position = position; 
    string phone;
    cout << "输入电话：" ;
    cin >> phone;
    abs->p1[index].phone = phone; 
    cout << endl;
    cout << "添加成功" << endl;
    system("sleep 1");
    system("clear");
}

void add_people(Addressbooks * abs)
{

    if (abs->size == MAX)
    {
        cout << "超过最大添加数量，无法添加！" << endl;
        return ; 
    }
    else
    {
        add_people_info(abs, abs->size);
        abs->size++;
    } 
}

void print_info(const Addressbooks abs, int len)
{
    if (len == 0)
    {
        cout << "当前通信录为空" << endl;
    }
    else
    {
        cout << "start search" << endl;
        for (int i = 0; i < len; i++)
        {
            cout << "name：" << abs.p1[i].name << " ";
            cout << "sex：" << abs.p1[i].sex << " ";
            cout << "age：" << abs.p1[i].age << " ";
            cout << "addr：" << abs.p1[i].position << " ";
            cout << "phone：" << abs.p1[i].phone << " ";
            cout << endl;
        }
    }
}

int isExist(const Addressbooks * abs, string name)
{
    for (int i = 0; i < abs->size; i++)
    {
        if (abs->p1[i].name == name)
        {
            return i;
        }
    }
    return -1;
}

void delete_p(Addressbooks * abs)
{
    cout << "输入你要删除的名字：" << endl;
    string name;
    cin >> name;
    if (isExist(abs, name) == -1)
    {
        cout << "查无此人" << endl;
    } 
    else
    {
        cout << "是否确认删除 <y or n> : " << " ";
        string choose;
        cin >> choose;
        if (choose == "y")
        {
            for (int i = isExist(abs, name); i < abs->size; i++)
            {
                abs->p1[i] = abs->p1[i+1];
                abs->size--;
            }
            cout << "删除成功" << endl;
        }
        else
        {
            cout << "这也许是一个正确的决定" << endl;
        }
    }
}

void search_p(Addressbooks * abs)
{
    cout << "输入你要查询通信录信息的名称：" << endl;
    string name{0};
    cin >> name;
    if (isExist(abs, name) == -1)
    {
        cout << "查无此人" << endl;
    } 
    else
    {
        print_people(abs, isExist(abs, name));
    }    
}

void modify_p(Addressbooks * abs)
{
    cout << "输入你要修改通信录信息的名称：" << endl;
    string name{0};
    cin >> name;
    if (isExist(abs, name) == -1)
    {
        cout << "查无此人" << endl;
    } 
    else
    {
        add_people_info(abs, isExist(abs, name));
    }  
}

void clean_p(Addressbooks * abs)
{
    // 将当前记录的联系人重置为0，做逻辑清空操作
    string reset;
    cout << "是否确定要清空[该操作具有危险性]：<y or n >" << "\t";
    cin >> reset;
    if (reset == "y")
    {
        abs->size = 0;
        cout << "数据已经清空" << endl;
    }
    else
    {
        cout << "您保持了理智" << endl;
    }
}