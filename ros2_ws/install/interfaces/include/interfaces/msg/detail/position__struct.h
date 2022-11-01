// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_
#define INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Position in the package interfaces.
typedef struct interfaces__msg__Position
{
  int64_t x;
  int64_t y;
  int64_t z;
} interfaces__msg__Position;

// Struct for a sequence of interfaces__msg__Position.
typedef struct interfaces__msg__Position__Sequence
{
  interfaces__msg__Position * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Position__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__POSITION__STRUCT_H_
