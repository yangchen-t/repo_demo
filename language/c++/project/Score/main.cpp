#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>


class Person
{
public:
    Person(std::string name, int score)
    {
        this->m_Name = name;
        this->m_score = score;
    }
    std::string m_Name;
    int m_score;
};

void PrintPerson(const std::vector<Person> &pp);
void CreatePersion(std::vector<Person> &p);
void SetScore(std::vector<Person> &p);
void test01();

// 入口
int main()
{
    srand((unsigned int)time(NULL)); // 随机种子
    test01();
    return 0;
}

// 打印所有的成员信息
void PrintPerson(const std::vector<Person> &pp)
{
    for (int i =0 ; i< pp.size(); i++)
    {
        std::cout << "name : " <<pp[i].m_Name << " score : " << pp[i].m_score << std::endl;
    }
}

// 创建成员
void CreatePersion(std::vector<Person> &p)
{       
    std::string nameSeed = "ABCDE";
    for (int i =0;i<5; i++)
    {
        std::string newName = "person";
        newName += nameSeed[i];
        int score = 0;
        Person person(newName, score);
        p.push_back(person);
    }
}

//  随机分数 ： 60~100之间
void SetScore(std::vector<Person> &p)
{
    for (std::vector<Person>::iterator i = p.begin();i != p.end();i++)
    {
        std::deque<int>d;
        for (int i = 0; i < 10; i++)
        {
            int score = rand() %41 +60 ;
            d.push_back(score);
        }
        sort(d.begin(), d.end());
        d.pop_front();
        d.pop_back();
        int allSize = 0;
        for (int i = 0; i < d.size(); i++)
        {
            allSize += d[i];
        }
        i->m_score = allSize / d.size();
    }
}

void test01()
{
    // std::vector<std::string> v1 = {"A","B","C","D","E"};
    // for(int i=0;i< v1.size();i++)
    // {
    //     std::cout << v1[i] << std::endl;
    // }
    std::vector<Person> p;
    CreatePersion(p);
    SetScore(p);
    PrintPerson(p);
}