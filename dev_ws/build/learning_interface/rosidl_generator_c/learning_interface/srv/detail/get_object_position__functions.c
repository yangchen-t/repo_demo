// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from learning_interface:srv/GetObjectPosition.idl
// generated code does not contain a copyright notice
#include "learning_interface/srv/detail/get_object_position__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
learning_interface__srv__GetObjectPosition_Request__init(learning_interface__srv__GetObjectPosition_Request * msg)
{
  if (!msg) {
    return false;
  }
  // get
  return true;
}

void
learning_interface__srv__GetObjectPosition_Request__fini(learning_interface__srv__GetObjectPosition_Request * msg)
{
  if (!msg) {
    return;
  }
  // get
}

learning_interface__srv__GetObjectPosition_Request *
learning_interface__srv__GetObjectPosition_Request__create()
{
  learning_interface__srv__GetObjectPosition_Request * msg = (learning_interface__srv__GetObjectPosition_Request *)malloc(sizeof(learning_interface__srv__GetObjectPosition_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(learning_interface__srv__GetObjectPosition_Request));
  bool success = learning_interface__srv__GetObjectPosition_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
learning_interface__srv__GetObjectPosition_Request__destroy(learning_interface__srv__GetObjectPosition_Request * msg)
{
  if (msg) {
    learning_interface__srv__GetObjectPosition_Request__fini(msg);
  }
  free(msg);
}


bool
learning_interface__srv__GetObjectPosition_Request__Sequence__init(learning_interface__srv__GetObjectPosition_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  learning_interface__srv__GetObjectPosition_Request * data = NULL;
  if (size) {
    data = (learning_interface__srv__GetObjectPosition_Request *)calloc(size, sizeof(learning_interface__srv__GetObjectPosition_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = learning_interface__srv__GetObjectPosition_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        learning_interface__srv__GetObjectPosition_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
learning_interface__srv__GetObjectPosition_Request__Sequence__fini(learning_interface__srv__GetObjectPosition_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      learning_interface__srv__GetObjectPosition_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

learning_interface__srv__GetObjectPosition_Request__Sequence *
learning_interface__srv__GetObjectPosition_Request__Sequence__create(size_t size)
{
  learning_interface__srv__GetObjectPosition_Request__Sequence * array = (learning_interface__srv__GetObjectPosition_Request__Sequence *)malloc(sizeof(learning_interface__srv__GetObjectPosition_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = learning_interface__srv__GetObjectPosition_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
learning_interface__srv__GetObjectPosition_Request__Sequence__destroy(learning_interface__srv__GetObjectPosition_Request__Sequence * array)
{
  if (array) {
    learning_interface__srv__GetObjectPosition_Request__Sequence__fini(array);
  }
  free(array);
}


bool
learning_interface__srv__GetObjectPosition_Response__init(learning_interface__srv__GetObjectPosition_Response * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  return true;
}

void
learning_interface__srv__GetObjectPosition_Response__fini(learning_interface__srv__GetObjectPosition_Response * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
}

learning_interface__srv__GetObjectPosition_Response *
learning_interface__srv__GetObjectPosition_Response__create()
{
  learning_interface__srv__GetObjectPosition_Response * msg = (learning_interface__srv__GetObjectPosition_Response *)malloc(sizeof(learning_interface__srv__GetObjectPosition_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(learning_interface__srv__GetObjectPosition_Response));
  bool success = learning_interface__srv__GetObjectPosition_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
learning_interface__srv__GetObjectPosition_Response__destroy(learning_interface__srv__GetObjectPosition_Response * msg)
{
  if (msg) {
    learning_interface__srv__GetObjectPosition_Response__fini(msg);
  }
  free(msg);
}


bool
learning_interface__srv__GetObjectPosition_Response__Sequence__init(learning_interface__srv__GetObjectPosition_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  learning_interface__srv__GetObjectPosition_Response * data = NULL;
  if (size) {
    data = (learning_interface__srv__GetObjectPosition_Response *)calloc(size, sizeof(learning_interface__srv__GetObjectPosition_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = learning_interface__srv__GetObjectPosition_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        learning_interface__srv__GetObjectPosition_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
learning_interface__srv__GetObjectPosition_Response__Sequence__fini(learning_interface__srv__GetObjectPosition_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      learning_interface__srv__GetObjectPosition_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

learning_interface__srv__GetObjectPosition_Response__Sequence *
learning_interface__srv__GetObjectPosition_Response__Sequence__create(size_t size)
{
  learning_interface__srv__GetObjectPosition_Response__Sequence * array = (learning_interface__srv__GetObjectPosition_Response__Sequence *)malloc(sizeof(learning_interface__srv__GetObjectPosition_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = learning_interface__srv__GetObjectPosition_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
learning_interface__srv__GetObjectPosition_Response__Sequence__destroy(learning_interface__srv__GetObjectPosition_Response__Sequence * array)
{
  if (array) {
    learning_interface__srv__GetObjectPosition_Response__Sequence__fini(array);
  }
  free(array);
}
