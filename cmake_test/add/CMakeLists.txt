
set(EXECUTABLE Add)

aux_source_directory(. SRC_LIST)
add_library(${EXECUTABLE} ${SRC_LIST})

install (TARGETS ${EXECUTABLE} DESTINATION bin)
install (FILES add.h DESTINATION include)