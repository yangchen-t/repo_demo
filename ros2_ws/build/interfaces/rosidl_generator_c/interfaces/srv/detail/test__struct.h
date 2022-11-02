// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/Test.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__TEST__STRUCT_H_
#define INTERFACES__SRV__DETAIL__TEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/Test in the package interfaces.
typedef struct interfaces__srv__Test_Request
{
  int64_t x;
  int64_t y;
  int64_t z;
} interfaces__srv__Test_Request;

// Struct for a sequence of interfaces__srv__Test_Request.
typedef struct interfaces__srv__Test_Request__Sequence
{
  interfaces__srv__Test_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__Test_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/Test in the package interfaces.
typedef struct interfaces__srv__Test_Response
{
  int64_t v;
} interfaces__srv__Test_Response;

// Struct for a sequence of interfaces__srv__Test_Response.
typedef struct interfaces__srv__Test_Response__Sequence
{
  interfaces__srv__Test_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__Test_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__DETAIL__TEST__STRUCT_H_