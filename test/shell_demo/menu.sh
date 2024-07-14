#!/bin/bash

readonly PREFIX="/opt/qomolo/utils/gcs_setup/tools/"

menu() {
	clear
	echo
	echo -e "\t\tQOMOLO GCS tools Menu\n"
	echo -e "\tq. 退出菜单\n\n"
	echo -en "\t\tEnter option:"
	read -n 1 option
}

while true
do
	menu
	case $option in
	"q"|"0") break ;;
	1) ${PREFIX}/qomolo-cpc ;;
	2) diskspace ;;
	*) clear && echo "Sorry, wrong selection";;
	esac
	echo -e "\n\t\tHit any key to continue"
	read -n 2 line
done
clear
