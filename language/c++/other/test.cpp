#include <iostream>
#include <future>

int multiply(int a, int b, int count) {
    static int tmp = 0;
    for (size_t i = 0; i < count; i++)
    {
        tmp = a * b * count;
    }
    
    return tmp;
}

void test(int count){
        // 启动异步任务，并获得 future 对象
    std::future<int> result = std::async(std::launch::async, multiply, 10, 20, count);

    // 这里可以做一些其他的工作
    for (size_t i = 0; i < count; i++)
    {
        std::cout << "print: " << i << " " ;
    }
    std::cout << std::endl;
    // 获取异步任务的结果
    int product = result.get();
    std::cout << "The product is: " << product << std::endl;
}

int main() {

    for (int i = 0; i < 10; i++)
    {
        test(i);
    }
    std::cout << "finish" << std::endl;
    return 0;
}
