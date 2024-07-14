#include <chrono>

#include <memory>

#include "rclcpp/rclcpp.hpp"

// #include "interfaces/msg/num.hpp" // CHANGE
#include "std_msgs/msg/u_int8.hpp"

using namespace std::chrono_literals;

std::string GetEnv()
{
    char *Robot;
    if (Robot = getenv("QOMOLO_ROBOT_ID"))
    {
        std::string ROBOT_ID = Robot;
        return ROBOT_ID;
    }
    else
    {
        std::cout << "robot_id is empty" << std::endl;
    }
}

class MinimalPublisher : public rclcpp::Node

{

public:
    MinimalPublisher() : Node("led_server_pub_node"), count_(0)
    {
        publisher_ = this->create_publisher<std_msgs::msg::UInt8>("/" + GetEnv() + "/agent/led_display", 10); // CHANGE
        timer_ = this->create_wall_timer(
            500ms, std::bind(&MinimalPublisher::timer_callback, this));
    }

private:
    void timer_callback()

    {
        auto message = std_msgs::msg::UInt8();                      // CHANGE
        message.data = 53;                                          // CHANGE
        RCLCPP_INFO(this->get_logger(), "Pub: '%d'", message.data); // CHANGE
        publisher_->publish(message);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::UInt8>::SharedPtr publisher_; // CHANGE
    size_t count_;
};

int main(int argc, char *argv[])

{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalPublisher>());
    rclcpp::shutdown();
    return 0;
}

