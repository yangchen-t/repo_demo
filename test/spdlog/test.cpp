#include <iostream>
#include <string>
#include <vector>
#include <typeinfo>


template <typename T, typename S>
struct MyStruct {
    T up;
    S down;
};
template <typename T>
auto getType(T value) -> decltype(value) {
    return value;
}
struct RosData
{
    std::vector<int> _data;
    std::vector<std::string> _msg;
} RosDataTest;


RosData* test01()
{
    RosDataTest._msg.push_back("123");
    RosDataTest._data.push_back(2);
    return &RosDataTest;
}

void handle()
{   
    RosData *p = test01();
    std::cout << p->_msg[0] << std::endl;
}

void test02()
{
    int num = 10;
    const std::type_info& type = typeid(decltype(num));
    std::cout << type.name() << std::endl;
    decltype(num) x = 20;  // x的类型与num相同，都是int

    auto result = getType(num);
    std::cout << result << std::endl;  // 输出：10
}

int main()
{
    std::vector<int> v1;
    v1.push_back(1);
    std::vector<std::string> v2;
    v2.push_back("str");
    RosData  rd;
    rd._data = v1;
    rd._msg = v2;
    std::cout << rd._msg[0] << std::endl;
    // handle();
    test02();
}
