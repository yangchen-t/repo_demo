#!/bin/bash


while true
do
	while read line
	do	
		sleep 2 
		echo $line
	done < numbers.csv
done
