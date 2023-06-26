
set(LIBADD libadd)

aux_source_directory(. SRC_LIST)
add_library(${LIBADD} ${SRC_LIST})
