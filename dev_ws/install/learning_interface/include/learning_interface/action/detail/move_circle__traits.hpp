// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from learning_interface:action/MoveCircle.idl
// generated code does not contain a copyright notice

#ifndef LEARNING_INTERFACE__ACTION__DETAIL__MOVE_CIRCLE__TRAITS_HPP_
#define LEARNING_INTERFACE__ACTION__DETAIL__MOVE_CIRCLE__TRAITS_HPP_

#include "learning_interface/action/detail/move_circle__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_Goal>()
{
  return "learning_interface::action::MoveCircle_Goal";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_Goal>()
{
  return "learning_interface/action/MoveCircle_Goal";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<learning_interface::action::MoveCircle_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_Result>()
{
  return "learning_interface::action::MoveCircle_Result";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_Result>()
{
  return "learning_interface/action/MoveCircle_Result";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_Result>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<learning_interface::action::MoveCircle_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_Feedback>()
{
  return "learning_interface::action::MoveCircle_Feedback";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_Feedback>()
{
  return "learning_interface/action/MoveCircle_Feedback";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<learning_interface::action::MoveCircle_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "learning_interface/action/detail/move_circle__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_SendGoal_Request>()
{
  return "learning_interface::action::MoveCircle_SendGoal_Request";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_SendGoal_Request>()
{
  return "learning_interface/action/MoveCircle_SendGoal_Request";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<learning_interface::action::MoveCircle_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<learning_interface::action::MoveCircle_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<learning_interface::action::MoveCircle_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_SendGoal_Response>()
{
  return "learning_interface::action::MoveCircle_SendGoal_Response";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_SendGoal_Response>()
{
  return "learning_interface/action/MoveCircle_SendGoal_Response";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<learning_interface::action::MoveCircle_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_SendGoal>()
{
  return "learning_interface::action::MoveCircle_SendGoal";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_SendGoal>()
{
  return "learning_interface/action/MoveCircle_SendGoal";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<learning_interface::action::MoveCircle_SendGoal_Request>::value &&
    has_fixed_size<learning_interface::action::MoveCircle_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<learning_interface::action::MoveCircle_SendGoal_Request>::value &&
    has_bounded_size<learning_interface::action::MoveCircle_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<learning_interface::action::MoveCircle_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<learning_interface::action::MoveCircle_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<learning_interface::action::MoveCircle_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_GetResult_Request>()
{
  return "learning_interface::action::MoveCircle_GetResult_Request";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_GetResult_Request>()
{
  return "learning_interface/action/MoveCircle_GetResult_Request";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<learning_interface::action::MoveCircle_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "learning_interface/action/detail/move_circle__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_GetResult_Response>()
{
  return "learning_interface::action::MoveCircle_GetResult_Response";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_GetResult_Response>()
{
  return "learning_interface/action/MoveCircle_GetResult_Response";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<learning_interface::action::MoveCircle_Result>::value> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<learning_interface::action::MoveCircle_Result>::value> {};

template<>
struct is_message<learning_interface::action::MoveCircle_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_GetResult>()
{
  return "learning_interface::action::MoveCircle_GetResult";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_GetResult>()
{
  return "learning_interface/action/MoveCircle_GetResult";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<learning_interface::action::MoveCircle_GetResult_Request>::value &&
    has_fixed_size<learning_interface::action::MoveCircle_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<learning_interface::action::MoveCircle_GetResult_Request>::value &&
    has_bounded_size<learning_interface::action::MoveCircle_GetResult_Response>::value
  >
{
};

template<>
struct is_service<learning_interface::action::MoveCircle_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<learning_interface::action::MoveCircle_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<learning_interface::action::MoveCircle_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "learning_interface/action/detail/move_circle__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<learning_interface::action::MoveCircle_FeedbackMessage>()
{
  return "learning_interface::action::MoveCircle_FeedbackMessage";
}

template<>
inline const char * name<learning_interface::action::MoveCircle_FeedbackMessage>()
{
  return "learning_interface/action/MoveCircle_FeedbackMessage";
}

template<>
struct has_fixed_size<learning_interface::action::MoveCircle_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<learning_interface::action::MoveCircle_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<learning_interface::action::MoveCircle_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<learning_interface::action::MoveCircle_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<learning_interface::action::MoveCircle_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<learning_interface::action::MoveCircle>
  : std::true_type
{
};

template<>
struct is_action_goal<learning_interface::action::MoveCircle_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<learning_interface::action::MoveCircle_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<learning_interface::action::MoveCircle_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // LEARNING_INTERFACE__ACTION__DETAIL__MOVE_CIRCLE__TRAITS_HPP_
