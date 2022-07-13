echo "暂时不更新可以回车跳过！！"
read -p "input qpilot version :" qpilot
read -p "input qpilot-param version :" qpilot_param
read -p "input qpilot-setup version :" qpilot_setup
if [[ $qpilot != "" && $qpilot_param != "" && $qpilot_setup != "" ]];then
	echo "ok"
else
	echo "$qpilot"
fi
