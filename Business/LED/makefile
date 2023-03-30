.DEFAULT_GOAL := build

CXX = g++
FILE = get_info.cpp led_server.cpp libbx_sdkDual.so.1.0.0 libiconv.so.2.6.0 libcharset.so.1.0.0 libiconv.so.2.6.0   
EXECTABLE = t
CMD = -o

clean:
	rm -r ${EXECTABLE}
build:	
	@export CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}:$(pwd)
	@${CXX} ${FILE}  ${CMD} ${EXECTABLE}
	@echo "build finish" 

