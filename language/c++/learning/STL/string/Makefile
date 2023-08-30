
Build = g++ 
Src = find.cpp
Executable  = find 
Cmd = -o 

${Executable}:${Src}
	@${Build} ${Src} ${Cmd} ${Executable}

clean:
	@rm -v ${Executable}

custom:
	@${Build} -g vector_custom.cpp ${Cmd} ${Executable}

nesting:
	@${Build} -g vector_nesting.cpp ${Cmd} ${Executable}