#include <chrono>

#include <memory>

#include "rclcpp/rclcpp.hpp"

#include "interfaces/msg/num.hpp" // CHANGE

using namespace std::chrono_literals;

class MinimalPublisher : public rclcpp::Node

{

public:
    MinimalPublisher(): Node("test_led_pub_node"), count_(0)
    {
        publisher_ = this->create_publisher<interfaces::msg::Num>("led_topic", 10); // CHANGE
        timer_ = this->create_wall_timer(
            500ms, std::bind(&MinimalPublisher::timer_callback, this));
    }

private:
    void timer_callback()

    {
        auto message = interfaces::msg::Num(); // CHANGE
        message.num = this->count_++; // CHANGE
        RCLCPP_INFO(this->get_logger(), "Pub: '%d'", message.num); // CHANGE
        publisher_->publish(message);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<interfaces::msg::Num>::SharedPtr publisher_; // CHANGE
    size_t count_;
};

int main(int argc, char *argv[])

{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalPublisher>());
    rclcpp::shutdown();
    return 0;
}
