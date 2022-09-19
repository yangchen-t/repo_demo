// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from learning_interface:action/MoveCircle.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "learning_interface/action/detail/move_circle__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_Goal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_Goal_type_support_ids_t;

static const _MoveCircle_Goal_type_support_ids_t _MoveCircle_Goal_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_Goal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_Goal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_Goal_type_support_symbol_names_t _MoveCircle_Goal_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_Goal)),
  }
};

typedef struct _MoveCircle_Goal_type_support_data_t
{
  void * data[2];
} _MoveCircle_Goal_type_support_data_t;

static _MoveCircle_Goal_type_support_data_t _MoveCircle_Goal_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_Goal_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_Goal_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_Goal_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_Goal_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_Goal_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_Goal_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_Goal>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_Goal_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_Goal)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_Goal>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_Result_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_Result_type_support_ids_t;

static const _MoveCircle_Result_type_support_ids_t _MoveCircle_Result_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_Result_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_Result_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_Result_type_support_symbol_names_t _MoveCircle_Result_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_Result)),
  }
};

typedef struct _MoveCircle_Result_type_support_data_t
{
  void * data[2];
} _MoveCircle_Result_type_support_data_t;

static _MoveCircle_Result_type_support_data_t _MoveCircle_Result_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_Result_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_Result_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_Result_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_Result_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_Result_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_Result_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_Result>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_Result_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_Result)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_Result>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_Feedback_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_Feedback_type_support_ids_t;

static const _MoveCircle_Feedback_type_support_ids_t _MoveCircle_Feedback_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_Feedback_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_Feedback_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_Feedback_type_support_symbol_names_t _MoveCircle_Feedback_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_Feedback)),
  }
};

typedef struct _MoveCircle_Feedback_type_support_data_t
{
  void * data[2];
} _MoveCircle_Feedback_type_support_data_t;

static _MoveCircle_Feedback_type_support_data_t _MoveCircle_Feedback_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_Feedback_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_Feedback_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_Feedback_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_Feedback_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_Feedback_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_Feedback_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_Feedback>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_Feedback_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_Feedback)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_Feedback>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_SendGoal_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_SendGoal_Request_type_support_ids_t;

static const _MoveCircle_SendGoal_Request_type_support_ids_t _MoveCircle_SendGoal_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_SendGoal_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_SendGoal_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_SendGoal_Request_type_support_symbol_names_t _MoveCircle_SendGoal_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_SendGoal_Request)),
  }
};

typedef struct _MoveCircle_SendGoal_Request_type_support_data_t
{
  void * data[2];
} _MoveCircle_SendGoal_Request_type_support_data_t;

static _MoveCircle_SendGoal_Request_type_support_data_t _MoveCircle_SendGoal_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_SendGoal_Request_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_SendGoal_Request_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_SendGoal_Request_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_SendGoal_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_SendGoal_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_SendGoal_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_SendGoal_Request>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_SendGoal_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_SendGoal_Request)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_SendGoal_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_SendGoal_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_SendGoal_Response_type_support_ids_t;

static const _MoveCircle_SendGoal_Response_type_support_ids_t _MoveCircle_SendGoal_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_SendGoal_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_SendGoal_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_SendGoal_Response_type_support_symbol_names_t _MoveCircle_SendGoal_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_SendGoal_Response)),
  }
};

typedef struct _MoveCircle_SendGoal_Response_type_support_data_t
{
  void * data[2];
} _MoveCircle_SendGoal_Response_type_support_data_t;

static _MoveCircle_SendGoal_Response_type_support_data_t _MoveCircle_SendGoal_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_SendGoal_Response_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_SendGoal_Response_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_SendGoal_Response_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_SendGoal_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_SendGoal_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_SendGoal_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_SendGoal_Response>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_SendGoal_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_SendGoal_Response)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_SendGoal_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_SendGoal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_SendGoal_type_support_ids_t;

static const _MoveCircle_SendGoal_type_support_ids_t _MoveCircle_SendGoal_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_SendGoal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_SendGoal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_SendGoal_type_support_symbol_names_t _MoveCircle_SendGoal_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_SendGoal)),
  }
};

typedef struct _MoveCircle_SendGoal_type_support_data_t
{
  void * data[2];
} _MoveCircle_SendGoal_type_support_data_t;

static _MoveCircle_SendGoal_type_support_data_t _MoveCircle_SendGoal_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_SendGoal_service_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_SendGoal_service_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_SendGoal_service_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_SendGoal_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t MoveCircle_SendGoal_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_SendGoal_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<learning_interface::action::MoveCircle_SendGoal>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_SendGoal_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_GetResult_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_GetResult_Request_type_support_ids_t;

static const _MoveCircle_GetResult_Request_type_support_ids_t _MoveCircle_GetResult_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_GetResult_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_GetResult_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_GetResult_Request_type_support_symbol_names_t _MoveCircle_GetResult_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_GetResult_Request)),
  }
};

typedef struct _MoveCircle_GetResult_Request_type_support_data_t
{
  void * data[2];
} _MoveCircle_GetResult_Request_type_support_data_t;

static _MoveCircle_GetResult_Request_type_support_data_t _MoveCircle_GetResult_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_GetResult_Request_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_GetResult_Request_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_GetResult_Request_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_GetResult_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_GetResult_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_GetResult_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_GetResult_Request>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_GetResult_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_GetResult_Request)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_GetResult_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_GetResult_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_GetResult_Response_type_support_ids_t;

static const _MoveCircle_GetResult_Response_type_support_ids_t _MoveCircle_GetResult_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_GetResult_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_GetResult_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_GetResult_Response_type_support_symbol_names_t _MoveCircle_GetResult_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_GetResult_Response)),
  }
};

typedef struct _MoveCircle_GetResult_Response_type_support_data_t
{
  void * data[2];
} _MoveCircle_GetResult_Response_type_support_data_t;

static _MoveCircle_GetResult_Response_type_support_data_t _MoveCircle_GetResult_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_GetResult_Response_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_GetResult_Response_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_GetResult_Response_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_GetResult_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_GetResult_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_GetResult_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_GetResult_Response>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_GetResult_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_GetResult_Response)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_GetResult_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_GetResult_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_GetResult_type_support_ids_t;

static const _MoveCircle_GetResult_type_support_ids_t _MoveCircle_GetResult_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_GetResult_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_GetResult_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_GetResult_type_support_symbol_names_t _MoveCircle_GetResult_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_GetResult)),
  }
};

typedef struct _MoveCircle_GetResult_type_support_data_t
{
  void * data[2];
} _MoveCircle_GetResult_type_support_data_t;

static _MoveCircle_GetResult_type_support_data_t _MoveCircle_GetResult_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_GetResult_service_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_GetResult_service_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_GetResult_service_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_GetResult_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t MoveCircle_GetResult_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_GetResult_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<learning_interface::action::MoveCircle_GetResult>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_GetResult_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _MoveCircle_FeedbackMessage_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _MoveCircle_FeedbackMessage_type_support_ids_t;

static const _MoveCircle_FeedbackMessage_type_support_ids_t _MoveCircle_FeedbackMessage_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _MoveCircle_FeedbackMessage_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _MoveCircle_FeedbackMessage_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MoveCircle_FeedbackMessage_type_support_symbol_names_t _MoveCircle_FeedbackMessage_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, action, MoveCircle_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, action, MoveCircle_FeedbackMessage)),
  }
};

typedef struct _MoveCircle_FeedbackMessage_type_support_data_t
{
  void * data[2];
} _MoveCircle_FeedbackMessage_type_support_data_t;

static _MoveCircle_FeedbackMessage_type_support_data_t _MoveCircle_FeedbackMessage_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MoveCircle_FeedbackMessage_message_typesupport_map = {
  2,
  "learning_interface",
  &_MoveCircle_FeedbackMessage_message_typesupport_ids.typesupport_identifier[0],
  &_MoveCircle_FeedbackMessage_message_typesupport_symbol_names.symbol_name[0],
  &_MoveCircle_FeedbackMessage_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MoveCircle_FeedbackMessage_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MoveCircle_FeedbackMessage_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::action::MoveCircle_FeedbackMessage>()
{
  return &::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_FeedbackMessage_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, action, MoveCircle_FeedbackMessage)() {
  return get_message_type_support_handle<learning_interface::action::MoveCircle_FeedbackMessage>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

#include "action_msgs/msg/goal_status_array.hpp"
#include "action_msgs/srv/cancel_goal.hpp"
// already included above
// #include "learning_interface/action/detail/move_circle__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_typesupport_cpp/action_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"

namespace learning_interface
{

namespace action
{

namespace rosidl_typesupport_cpp
{

static rosidl_action_type_support_t MoveCircle_action_type_support_handle = {
  NULL, NULL, NULL, NULL, NULL};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_action_type_support_t *
get_action_type_support_handle<learning_interface::action::MoveCircle>()
{
  using ::learning_interface::action::rosidl_typesupport_cpp::MoveCircle_action_type_support_handle;
  // Thread-safe by always writing the same values to the static struct
  MoveCircle_action_type_support_handle.goal_service_type_support = get_service_type_support_handle<::learning_interface::action::MoveCircle::Impl::SendGoalService>();
  MoveCircle_action_type_support_handle.result_service_type_support = get_service_type_support_handle<::learning_interface::action::MoveCircle::Impl::GetResultService>();
  MoveCircle_action_type_support_handle.cancel_service_type_support = get_service_type_support_handle<::learning_interface::action::MoveCircle::Impl::CancelGoalService>();
  MoveCircle_action_type_support_handle.feedback_message_type_support = get_message_type_support_handle<::learning_interface::action::MoveCircle::Impl::FeedbackMessage>();
  MoveCircle_action_type_support_handle.status_message_type_support = get_message_type_support_handle<::learning_interface::action::MoveCircle::Impl::GoalStatusMessage>();
  return &MoveCircle_action_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
