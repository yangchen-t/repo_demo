#include "../include/color_tools.h"

void Color::bule(std::string str){std::cout << "\e[34m"<< str << ".\e[0m" << std::endl;}
void Color::black(std::string str){std::cout << "\e[30m"<< str << ".\e[0m" << std::endl;}
void Color::yellow(std::string str){std::cout << "\e[33m"<< str << ".\e[0m" << std::endl;}