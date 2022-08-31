# FMS-vpn





```  shell
sudo apt-get install wireguard   

安装好之后，配置文件改名改成wg0.conf
然后mv wg0.conf /etc/wireguard/目录下
启动命令sudo wg-quick up wg0
关闭命令是sudo wg-quick down wg0

10.1.200.1             westwell/westwell        #跳板机
10.253.253.6        westwell/westwell       #单车模拟器
10.253.253.8        westwell/westwell       # mqtt server
```

