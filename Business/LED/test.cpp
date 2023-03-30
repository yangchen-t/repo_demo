#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <sstream>
#include <cxxabi.h>


typedef unsigned char Ouint8;

struct path_select
{
    std::string path;
    int numbers;
};

// print datatype
std::string getClearName(const char* name)
{
    int status = -1;
    char* clear_name = abi::__cxa_demangle(name, NULL, NULL, &status);
    const char* demangle_name = (status==0) ? clear_name : name;
    std::string ret_val(demangle_name);
    free(clear_name);
    return ret_val;
}

path_select return_path()
{
	std::ifstream inFile("./number.csv", std::ios::in);
	std::stringstream stream;
	std::string num;
	int n ;
    path_select pl;
    while (getline(inFile, num)){
		stream << num;
		stream >> n;            // 文件读取
		pl.numbers = n;
		pl.path = "/debug/test" + std::to_string(n);
		return pl;
	}
    return pl;
}


int main()
{
    path_select p = return_path();
    std::cout << p.numbers << std::endl;
    std::cout << p.path << std::endl;
    Ouint8* path = (unsigned char *)p.path.c_str();
    std::cout << path << "type is : " << getClearName(typeid(path).name()) <<  std::endl;
    return 0;
}