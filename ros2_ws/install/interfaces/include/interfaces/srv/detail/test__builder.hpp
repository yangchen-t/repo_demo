// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/Test.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TEST__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__TEST__BUILDER_HPP_

#include "interfaces/srv/detail/test__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_Test_Request_z
{
public:
  explicit Init_Test_Request_z(::interfaces::srv::Test_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::Test_Request z(::interfaces::srv::Test_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::Test_Request msg_;
};

class Init_Test_Request_y
{
public:
  explicit Init_Test_Request_y(::interfaces::srv::Test_Request & msg)
  : msg_(msg)
  {}
  Init_Test_Request_z y(::interfaces::srv::Test_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Test_Request_z(msg_);
  }

private:
  ::interfaces::srv::Test_Request msg_;
};

class Init_Test_Request_x
{
public:
  Init_Test_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_Request_y x(::interfaces::srv::Test_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Test_Request_y(msg_);
  }

private:
  ::interfaces::srv::Test_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::Test_Request>()
{
  return interfaces::srv::builder::Init_Test_Request_x();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_Test_Response_v
{
public:
  Init_Test_Response_v()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::Test_Response v(::interfaces::srv::Test_Response::_v_type arg)
  {
    msg_.v = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::Test_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::Test_Response>()
{
  return interfaces::srv::builder::Init_Test_Response_v();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__TEST__BUILDER_HPP_
