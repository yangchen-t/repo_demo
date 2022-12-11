#include <iostream>
#include <string>
#include <ctime>

using namespace std;


void allocalteather(struct  teachar t1[], int len);
void print_info(struct teachar t1[], int len);

struct student{
    string name;
    int score;
};
struct teachar
{
    string name;
    struct student s1[5];

};

int main(){
    srand((unsigned int)time(NULL));       // 随机种子，利用当前的时间生成随机数
    teachar t1[3];

    int len = sizeof(t1)/sizeof(t1[0]);
    allocalteather(t1, len);
    print_info(t1, len);

    return 0;
}


void allocalteather(struct teachar t1[], int len)
{
    string number  = "ABCDE";
    int random = rand() % 71 + 30;
    for (int i = 0; i < len; i++)
    {
        t1[i].name = "teather_";
        t1[i].name += number[i];
        for (int j = 0; j < 5; j++)
        {
            t1[i].s1[j].name = "student_";
            t1[i].s1[j].name += number[j];
            t1[i].s1[j].score =  random;
        }
        
    }
    
};

void print_info(struct teachar t1[], int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << "teather : " << t1[i].name << endl;
        for (int j = 0; j < 5; j++)
        {
            cout << "\tstudent: " << t1[i].s1[j].name << "score : " << t1[i].s1[j].score << endl; 
        }
        
    }
    
};
