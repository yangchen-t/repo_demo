#include <iostream>
#include <string>

using namespace std;

class Cpu
{
public:
    virtual void cpu() = 0;
};

class VideoCard
{
public:
    virtual void videocard() = 0;
};

class Memory
{
public:
    virtual void memory() = 0;
};

class Computer
{
public:
    Computer(Cpu * cpu, VideoCard * vc, Memory * mem)
    {
        this->m_cpu = cpu;
        this->m_mem = mem;
        this->m_vc = vc;
    }

    void work()
    {
        m_cpu->cpu();
        m_vc->videocard();
        m_mem->memory();
    }
    ~Computer()
    {
        if (this->m_cpu != NULL)
        {
            delete this->m_cpu;
            this->m_cpu = NULL;
        }
        if (this->m_vc != NULL)
        {
            delete this->m_vc;
            this->m_vc = NULL;
        }
        if (this->m_mem != NULL)
        {
            delete this->m_mem;
            this->m_mem = NULL;
        }
    }
private:
    Cpu * m_cpu;
    VideoCard * m_vc;
    Memory * m_mem;

};

// Inter 
class InterCpu : public Cpu
{
    void cpu()
    {
        cout << "Inter cpu is work ..." << endl;
    }
};
class InterVideoCard : public VideoCard
{
    void videocard()
    {
        cout << "Inter VideoCard is work ..." << endl;
    }
};
class InterMemory : public Memory
{
    void memory()
    {
        cout << "Inter Memory is work ..." << endl;
    }
};

// Lenove
class LenovoCpu : public Cpu
{
    void cpu()
    {
        cout << "Lenovo cpu is work ..." << endl;
    }
};
class LenovoVideoCard : public VideoCard
{
    void videocard()
    {
        cout << "Lenovo VideoCard is work ..." << endl;
    }
};
class LenovoMemory : public Memory
{
    void memory()
    {
        cout << "Lenovo Memory is work ..." << endl;
    }
};


void test01()
{
    // // Lenovo
    // LenovoCpu L_cpu;
    // LenovoVideoCard L_vc;
    // LenovoMemory L_mem;    
    // // Inter
    // InterCpu I_cpu;
    // InterVideoCard I_vc;
    // InterMemory I_mem;  
    // cout << "Lenovo computer" << endl;
    // Computer c1(&L_cpu, &L_vc, &L_mem);
    // c1.work();

    // cout << "Inter computer" << endl;
    // Computer c2(&I_cpu, &I_vc, &I_mem);
    // c2.work();

    // cout << "Hybrid computer" << endl;
    // Computer c3(&I_cpu, &L_vc, &I_mem);
    // c3.work();

//
    Cpu * L_cpu = new LenovoCpu;
    VideoCard * L_vc = new LenovoVideoCard;
    Memory * L_mem = new LenovoMemory;
    Cpu * I_cpu = new InterCpu;
    VideoCard * I_vc = new InterVideoCard;
    Memory * I_mem = new InterMemory;

    cout << "Lenovo computer" << endl;
    Computer * computer1 = new Computer(L_cpu, L_vc, L_mem);
    computer1->work();
    delete computer1;

    cout << "Inter computer" << endl;
    Computer * computer2 = new Computer(I_cpu, I_vc, I_mem);
    computer2->work();
    delete computer2;   

    cout << "Hybrid computer" << endl;    
    Computer * computer3 = new Computer(new LenovoCpu, new InterVideoCard, new InterMemory);
    computer3->work();
    delete computer3;    
}

int main()
{
    test01();
    return 0;
} 