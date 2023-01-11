#!/bin/bash

#clear /key_log/key_log/ dir 

dir_num=`ls -alF -a /key_log/key_log/ | grep ^d | wc -l`

function clear_dir()
{
	for i in {1..$dir_num};
	do
		dir_name=`ls -alF -a /key_log/key_log | grep ^d | tail -n $i | head -n 1 |  awk '{print$9}'`
		echo $dir_name
		rm -r /key_log/key_log/$dir_name
	done
}

if [ $dir_num -ge 3 ];then
	echo "have dir, will del"
	sleep 1 
	echo "start clear"
	clear_dir 
else
	echo "no diff"
	false
fi
