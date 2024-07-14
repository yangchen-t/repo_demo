//
// Created by dt on 2021/5/13.
//

#include "test.h"
#include <iostream>

int fun::add_a_b() {
    return this->a + this->b;
}

void fun::debug()
{
	std::cout << "this is debug msg" << std::endl;
}
fun::fun(int aa, int bb) {
    this->a = aa;
    this->b = bb;
}

fun::~fun() {

}


