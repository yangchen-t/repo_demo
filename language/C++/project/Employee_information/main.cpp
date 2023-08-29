#include <iostream>
#include <vector>
#include <ctime>
#include <map>

#define DESIGN 0
#define ART 1 
#define DEVELOP 2 
 
// 定义一个 worker类
class Worker
{
public:
    std::string m_name;
    int m_salary;
};       

void CreateWorker(std::vector<Worker>&v);
void PrintVector(std::vector<Worker>&v);
void SetGroup(std::vector<Worker>&vm, std::multimap<int, Worker>&m);
void ShowWorkerByGroup(std::multimap<int,Worker>&m);
void showworkerbygroup(std::multimap<int, Worker>&m);  // update version

int main()
{
    srand((unsigned int)time(NULL));  // 随机种子 使用时间
    std::vector<Worker>vw;            // 创建一个 worker类型的vector容器
    CreateWorker(vw);              
    // PrintVector(vw);
    std::multimap<int,Worker>m;       // 创建一个 <int,worker>类型的multimap容器
    SetGroup(vw,m);          
    // ShowWorkerByGroup(m);
    showworkerbygroup(m);
    return 0;
}

void CreateWorker(std::vector<Worker>&v)
{
    std::string namelist = "abcdefghij";
    for (int i =0 ; i < 10; i++)
    {
        Worker worker;
        worker.m_name = "员工";
        worker.m_name += namelist[i];   // 字符串切片相加 生成新的name
        worker.m_salary = rand() % 10000 + 10000;  //  随机数  10000~19999
        v.push_back(worker);            // 全部添加到v中
    }
    return ;
}

void PrintVector(std::vector<Worker>&v)
{
    // for (std::vector<Worker>::iterator it = v.begin(); it != v.end(); it++)  // 迭代器遍历
    for (int i = 0; i < 10; i++)                             
    {
        std::cout << "name: " << v[i].m_name << ", salary: " << v[i].m_salary << std::endl;
    }
}

void SetGroup(std::vector<Worker>&vm, std::multimap<int, Worker>&m)
{
    for (std::vector<Worker>::iterator it = vm.begin(); it != vm.end(); it++)
    {
        int random = rand()%3 ;                 // 设置随机数为 0 1 2  = DESIGN / ART / DEVELOP 
        m.insert(std::make_pair(random,*it));   // pair类型插入multimap容器, first = random, second = vector_elem
    }
    
}
void ShowWorkerByGroup(std::multimap<int,Worker>&m)
{
    for (std::multimap<int, Worker>::iterator mit = m.begin() ; mit != m.end(); mit++)  // 迭代器遍历 整个multimap容器
    {
        if (mit->first == DESIGN)       // 判断index类型 区分不同职位
        {
            std::cout << "Design \t" << 
            "name : " << mit->second.m_name << " salary: " << mit->second.m_salary << std::endl; 
        }
        else if (mit->first == ART)
        {
            std::cout << "ART \t" << " name : " << mit->second.m_name << " salary: " << mit->second.m_salary << std::endl; 
        }
        else if (mit->first == DEVELOP)
        {
            std::cout << "DEVELOP\t " << " name : " << mit->second.m_name << " salary: " << mit->second.m_salary << std::endl; 
        }
    }
}


void showworkerbygroup(std::multimap<int, Worker>&m)
{
    std::cout  << "design" << std::endl;
    std::multimap<int, Worker>::iterator pos = m.find(DESIGN);    // 查找第一次出现的位置，使用pos接受当前迭代器的位置
    int count = m.count(DESIGN);                                  // 统计multimap容器中出现的次数
    int index = 0;
    for (; pos != m.end() && index < count ; pos++,index++)       // 不满足循环到!end()迭代器和 index < count 时循环完毕
    {
        std::cout << "name : " << pos->second.m_name << " salary: " << pos->second.m_salary << std::endl;
    }

    std::cout << "art" << std::endl;
    pos = m.find(ART);
    count = m.count(ART);
    index = 0;
    for (; pos != m.end() && index < count ; pos++,index++)
    {
        std::cout << "name : " << pos->second.m_name << " salary: " << pos->second.m_salary << std::endl;
    }

    std::cout << "develop" << std::endl;
    pos = m.find(DEVELOP);
    count = m.count(DEVELOP);
    index = 0;
    for (; pos != m.end() && index < count ; pos++,index++)
    {
        std::cout << "name : " << pos->second.m_name << " salary: " << pos->second.m_salary << std::endl;
    }
}