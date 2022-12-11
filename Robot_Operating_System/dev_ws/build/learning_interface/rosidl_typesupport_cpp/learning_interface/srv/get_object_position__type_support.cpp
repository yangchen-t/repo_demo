// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from learning_interface:srv/GetObjectPosition.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "learning_interface/srv/detail/get_object_position__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace learning_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetObjectPosition_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetObjectPosition_Request_type_support_ids_t;

static const _GetObjectPosition_Request_type_support_ids_t _GetObjectPosition_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetObjectPosition_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetObjectPosition_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetObjectPosition_Request_type_support_symbol_names_t _GetObjectPosition_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, srv, GetObjectPosition_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, srv, GetObjectPosition_Request)),
  }
};

typedef struct _GetObjectPosition_Request_type_support_data_t
{
  void * data[2];
} _GetObjectPosition_Request_type_support_data_t;

static _GetObjectPosition_Request_type_support_data_t _GetObjectPosition_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetObjectPosition_Request_message_typesupport_map = {
  2,
  "learning_interface",
  &_GetObjectPosition_Request_message_typesupport_ids.typesupport_identifier[0],
  &_GetObjectPosition_Request_message_typesupport_symbol_names.symbol_name[0],
  &_GetObjectPosition_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetObjectPosition_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetObjectPosition_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::srv::GetObjectPosition_Request>()
{
  return &::learning_interface::srv::rosidl_typesupport_cpp::GetObjectPosition_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, srv, GetObjectPosition_Request)() {
  return get_message_type_support_handle<learning_interface::srv::GetObjectPosition_Request>();
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
// #include "learning_interface/srv/detail/get_object_position__struct.hpp"
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

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetObjectPosition_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetObjectPosition_Response_type_support_ids_t;

static const _GetObjectPosition_Response_type_support_ids_t _GetObjectPosition_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetObjectPosition_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetObjectPosition_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetObjectPosition_Response_type_support_symbol_names_t _GetObjectPosition_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, srv, GetObjectPosition_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, srv, GetObjectPosition_Response)),
  }
};

typedef struct _GetObjectPosition_Response_type_support_data_t
{
  void * data[2];
} _GetObjectPosition_Response_type_support_data_t;

static _GetObjectPosition_Response_type_support_data_t _GetObjectPosition_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetObjectPosition_Response_message_typesupport_map = {
  2,
  "learning_interface",
  &_GetObjectPosition_Response_message_typesupport_ids.typesupport_identifier[0],
  &_GetObjectPosition_Response_message_typesupport_symbol_names.symbol_name[0],
  &_GetObjectPosition_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetObjectPosition_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetObjectPosition_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<learning_interface::srv::GetObjectPosition_Response>()
{
  return &::learning_interface::srv::rosidl_typesupport_cpp::GetObjectPosition_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, learning_interface, srv, GetObjectPosition_Response)() {
  return get_message_type_support_handle<learning_interface::srv::GetObjectPosition_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "learning_interface/srv/detail/get_object_position__struct.hpp"
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

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetObjectPosition_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetObjectPosition_type_support_ids_t;

static const _GetObjectPosition_type_support_ids_t _GetObjectPosition_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetObjectPosition_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetObjectPosition_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetObjectPosition_type_support_symbol_names_t _GetObjectPosition_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, learning_interface, srv, GetObjectPosition)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, learning_interface, srv, GetObjectPosition)),
  }
};

typedef struct _GetObjectPosition_type_support_data_t
{
  void * data[2];
} _GetObjectPosition_type_support_data_t;

static _GetObjectPosition_type_support_data_t _GetObjectPosition_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetObjectPosition_service_typesupport_map = {
  2,
  "learning_interface",
  &_GetObjectPosition_service_typesupport_ids.typesupport_identifier[0],
  &_GetObjectPosition_service_typesupport_symbol_names.symbol_name[0],
  &_GetObjectPosition_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t GetObjectPosition_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetObjectPosition_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace learning_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<learning_interface::srv::GetObjectPosition>()
{
  return &::learning_interface::srv::rosidl_typesupport_cpp::GetObjectPosition_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
