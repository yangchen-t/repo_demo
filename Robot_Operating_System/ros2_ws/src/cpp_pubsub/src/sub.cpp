#include <memory>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "interfaces/msg/num.hpp" // CHANGE

#include "get_info.h"

using std::placeholders::_1;
class MinimalSubscriber : public rclcpp::Node
{
public:
    MinimalSubscriber(): Node("test_led_sub_node")
    {
        subscription_ = this->create_subscription<interfaces::msg::Num>( // CHANGE
            "led_topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    }
    // Pic::gettime();
    // path_select pl = Pic::return_path();
    // std::cout << pl.path << std::endl;
private:
    void topic_callback(const interfaces::msg::Num::SharedPtr msg) const // CHANGE
    {
        RCLCPP_INFO(this->get_logger(), "%d", msg->num);
        gettime();
    }
    rclcpp::Subscription<interfaces::msg::Num>::SharedPtr subscription_; // CHANGE
};



int main(int argc, char *argv[])

{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalSubscriber>());
    rclcpp::shutdown();
    return 0;
}


