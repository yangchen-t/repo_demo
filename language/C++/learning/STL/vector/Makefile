
Build = g++ 
Src = vector.cpp
Executable  = vector 
Cmd = -o 

${Executable}:${Src}
	@${Build} ${Src} ${Cmd} ${Executable}

clean:
	@rm -v ${Executable}

custom:
	@${Build} -g vector_custom.cpp ${Cmd} ${Executable}

nesting:
	@${Build} -g vector_nesting.cpp ${Cmd} ${Executable}