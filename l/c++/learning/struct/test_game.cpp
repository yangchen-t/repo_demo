#include <iostream>
#include <string>


using namespace std;

void bubblesort(struct brid_type b1[], int len);
void print_info(struct brid_type b1[], int len);

struct brid_type
{
    string name;
    int size;
    string color;
};


int main(){

    struct brid_type  b1[3] = 
    {
        {"x", 20, "red"},
        {"y", 50, "yellow"},
        {"z", 34, "orange"}
    };
    
    int len = sizeof(b1)/sizeof(b1[0]);
    bubblesort(b1, len);
    print_info(b1, len);
    return 0;
}

void bubblesort(struct brid_type t1[], int len)
{
    for (int i = 0; i < len -1 ; i++)
    {
        for (int f = 0; f < len -i -1; f++)
        {
            if (t1[f].size < t1[f+1].size)
            {
                struct brid_type tmp = t1[f];
                t1[f] = t1[f+1];
                t1[f+1] = tmp;
            }
        }
        
    }
    
};

void print_info(struct brid_type t1[], int len)
{
    for (int i = 0; i < len; i++)
    {
            cout << "name: " << t1[i].name <<
            " " << "size: " << t1[i].size <<
            " " << "color: " << t1[i].color << endl; 
        
    }
    
}