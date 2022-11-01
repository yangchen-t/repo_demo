// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/Test.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TEST__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__TEST__TRAITS_HPP_

#include "interfaces/srv/detail/test__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Test_Request>()
{
  return "interfaces::srv::Test_Request";
}

template<>
inline const char * name<interfaces::srv::Test_Request>()
{
  return "interfaces/srv/Test_Request";
}

template<>
struct has_fixed_size<interfaces::srv::Test_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::Test_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::Test_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Test_Response>()
{
  return "interfaces::srv::Test_Response";
}

template<>
inline const char * name<interfaces::srv::Test_Response>()
{
  return "interfaces/srv/Test_Response";
}

template<>
struct has_fixed_size<interfaces::srv::Test_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::Test_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::Test_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Test>()
{
  return "interfaces::srv::Test";
}

template<>
inline const char * name<interfaces::srv::Test>()
{
  return "interfaces/srv/Test";
}

template<>
struct has_fixed_size<interfaces::srv::Test>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::Test_Request>::value &&
    has_fixed_size<interfaces::srv::Test_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::Test>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::Test_Request>::value &&
    has_bounded_size<interfaces::srv::Test_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::Test>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::Test_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::Test_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__TEST__TRAITS_HPP_
