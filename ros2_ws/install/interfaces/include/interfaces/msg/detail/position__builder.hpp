// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_

#include "interfaces/msg/detail/position__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Position_z
{
public:
  explicit Init_Position_z(::interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Position z(::interfaces::msg::Position::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Position msg_;
};

class Init_Position_y
{
public:
  explicit Init_Position_y(::interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_z y(::interfaces::msg::Position::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Position_z(msg_);
  }

private:
  ::interfaces::msg::Position msg_;
};

class Init_Position_x
{
public:
  Init_Position_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Position_y x(::interfaces::msg::Position::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Position_y(msg_);
  }

private:
  ::interfaces::msg::Position msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Position>()
{
  return interfaces::msg::builder::Init_Position_x();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
