#!/bin/bash


# input 80 change 10000 port
echo " " | sudo -S iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.103.172:10000
