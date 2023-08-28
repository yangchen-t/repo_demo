

#.EXPORT_ALL_VARIABLES:
#all: test blah.c blah.o blah
#
#MY_VAR= test.cpp test.h
#
#blah: blah.o
#	cc blah.o -o blah # 第三步
#
#blah.o: blah.c
#	cc -c blah.c -o blah.o # 第二步
#
#blah.c:
#	echo "int main() { return 0; }" > blah.c # 第一步
#
#
#one ?= one ${MY_VAR}
#one += two $(MY_VAR)
#
#print:
#	@echo ${one}
#	@echo $(two)
#clean:
#	rm -r *.c *.o blah


# Print out file information about every .c file
#print: $(wildcard *.cpp *.c )
#	ls -la  $?
#	@echo "================"
#foo = o

#all:
#ifeq ($(foo), o)
#	echo "foo equals ok"
#else
#	echo "nope"
#endif


.DEFAULT_GOAL := build

CXX = g++
FILE = test.cpp 
EXECTABLE = t
CMD = -o

clean:
	rm -r ${EXECTABLE}
build:	
	@${CXX} ${FILE} ${CMD} ${EXECTABLE}
	@echo "build finish" 
say_hello:
	@echo "hello"
