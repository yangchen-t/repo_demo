#!/bin/bash

for i in {1..10}
do
	clear
	python3 time.py | figlet | cowsay -f moose -n | lolcat
	sleep 1 
done 
