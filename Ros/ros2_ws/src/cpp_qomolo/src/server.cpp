#include "rclcpp/rclcpp.hpp"
#include "interfaces/srv/test.hpp"

#include <memory>

const int avg = 3;

void add(const std::shared_ptr<interfaces::srv::Test::Request> request,
          std::shared_ptr<interfaces::srv::Test::Response> response)
{
  response->v = (request->x + request->y + request->z) / avg;

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request\na: %ld" " b: %ld" " c: %ld",
                request->x, request->y, request->z);
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "sending back response: [%ld]", (long int)response->v);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("add_two_ints_server");

  rclcpp::Service<interfaces::srv::Test>::SharedPtr service =
    node->create_service<interfaces::srv::Test>("test", &add);

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add two ints.");

  rclcpp::spin(node);
  rclcpp::shutdown();
}
