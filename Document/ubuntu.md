# ubuntu

>#### 本文主要用于记录日常遇到的问题及解决方法，留下备份，为下次出现提供快速的解决方法。



## Q：如何设置磁盘的自动挂载？

```shell
A：
1.使用命令查看分区
sudo fdisk -l  
2.创建挂载目录
sudo mkdir /mnt/data
3.开始挂载
sudo mount /dev/sda/ /mnt/data/
4.设置开机自动挂载
4.1查询挂载硬盘UUID
sudo blkid /dev/sda2
返回信息为
/dev/sda2: LABEL="Data" UUID="88069947069936E2" TYPE="ntfs" 
PARTLABEL="Basic data partition" PARTUUID="7170f9a7-9c9f-43d8-
9916-da47aa9101f7"
格式化硬盘文件类型：
sudo mkfs.ext4 /dev/xxxxx 
4.2修改文件
打开文件/etc/fstab文件。
sudo gedit /etc/fstab
在文档末尾添加裹在磁盘的信息。
格式为：
[UUID=************] [挂载磁盘分区]  [挂载磁盘格式]  0  2
UUID=88069947069936E2 /mnt/data ntfs defaults  0  2
第一个数字：0表示开机不检查磁盘，1表示开机检查磁盘；
第二个数字：0表示交换分区，1代表启动分区（Linux），2表示普通分区
我挂载的分区是在WIn系统下创建的分区，磁盘格式为ntfs
 
请注意：如若改错，无法进入桌面，系统无法系统，意味着系统崩溃！请再三核对！否则只有重新安装系统!!       #谨慎操作
```

## Q： 如何实现scp 断点续传

```shell
# rsync -P --rsh=ssh pic.tar.gz 192.168.205.304:/home/199_home.tar

说明：
-P: 是包含了 "–partial –progress"， 部分传送和显示进度
-rsh=ssh 表示使用ssh协议传送数据
```

## 	Q:  显卡及显卡驱动

```bash
## 查看显卡驱动信息
nvidia-smi  

## 查看显卡信息

ubuntu-drives devices 

## 查看显卡信息 （已安装显卡驱动）
nvidia-smi -L 
```





## Q:   tcpdump

```bash
> tcpdump 
# 默认抓取 第一个网络接口上的所有的数据包。
#第一列： 
时间 ： 21：25：39.013621
#第二列：
网络协议 IP
#第三列
发送方的ip地址+端口 ，其中 ssh 是协议，22端口
#第四列
箭头>,表示数据流向
#第五列
接收方的ip地址+端口
#第六列
数据包内容，包括Flags标识符，seq号，ack号，win窗口，数据长度length,其中[p.]表示PUSH标志位为1



# man tcpdump
抓包选项：
-c：指定要抓取的包数量。

-i interface：指定tcpdump需要监听的接口。默认会抓取第一个网络接口

-n：对地址以数字方式显式，否则显式为主机名，也就是说-n选项不做主机名解析。

-nn：除了-n的作用外，还把端口显示为数值，否则显示端口服务名。

-P：指定要抓取的包是流入还是流出的包。可以给定的值为"in"、"out"和"inout"，默认为"inout"。

-s len：设置tcpdump的数据包抓取长度为len，如果不设置默认将会是65535字节。对于要抓取的数据包较大时，长度设置不够可能会产生包截断，若出现包截断，
：输出行中会出现"[|proto]"的标志(proto实际会显示为协议名)。但是抓取len越长，包的处理时间越长，并且会减少tcpdump可缓存的数据包的数量，
：从而会导致数据包的丢失，所以在能抓取我们想要的包的前提下，抓取长度越小越好。

输出选项：
-e：输出的每行中都将包括数据链路层头部信息，例如源MAC和目标MAC。

-q：快速打印输出。即打印很少的协议相关信息，从而输出行都比较简短。

-X：输出包的头部数据，会以16进制和ASCII两种方式同时输出。

-XX：输出包的头部数据，会以16进制和ASCII两种方式同时输出，更详细。

-v：当分析和打印的时候，产生详细的输出。

-vv：产生比-v更详细的输出。
-vvv：产生比-vv更详细的输出。

其他功能性选项：
-D：列出可用于抓包的接口。将会列出接口的数值编号和接口名，它们都可以用于"-i"后。

-F：从文件中读取抓包的表达式。若使用该选项，则命令行中给定的其他表达式都将失效。

-w：将抓包数据输出到文件中而不是标准输出。可以同时配合"-G

time"选项使得输出文件每time秒就自动切换到另一个文件。可通过"-r"选项载入这些文件以进行分析和打印。

-r：从给定的数据包文件中读取数据。使用"-"表示从标准输入中读取。


# 常用方式
监听指定网卡
sudo tcpdump -i xx 
监听指定网段并且只抓取10个包
sudo tcpdump -i xx -c 10 net 192.168
数据保留为pcap
sudo tcpdump -i xx -w file_name.pcap
监听所有网卡及设置文件大小及文件个数
sudo tcpdump -i any -C 1 -W 10 -w file_name          # -C 文件大小（MB） -W 文件个数
抓取单向数据
sudo tcpdump src/dst host 192.168.xx.xx              # src 源  dst目的
显示数据链路层的信息
sudo tcpdump -e 
过滤一系列端口
sudo tcpdump portrange 80-10000
```

## Q:  iftop

```bash
界面相关说明：
中间的<= =>这两个左右箭头，表示的是流量的方向。

TX：发送流量
RX：接收流量
TOTAL：总流量
Cumm：运行iftop到目前时间的总流量
peak：流量峰值
rates：分别表示过去 2s 10s 40s 的平均流量
常用参数：
-i设定监测的网卡，如：# iftop -i eth1
-B 以bytes为单位显示流量(默认是bits)，如：# iftop -B
-n使host信息默认直接都显示IP，如：# iftop -n
-N使端口信息默认直接都显示端口号，如: # iftop -N
-F显示特定网段的进出流量，如# iftop -F 10.10.1.0/24或# iftop -F 10.10.1.0/255.255.255.0
-h（display this message），帮助，显示参数信息
-p使用这个参数后，中间的列表显示的本地主机信息，出现了本机以外的IP信息;
-b使流量图形条默认就显示;
-f这个暂时还不太会用，过滤计算包用的;
-P使host信息及端口信息默认就都显示;
-m设置界面最上边的刻度的最大值，刻度分五个大段显示，例：# iftop -m 100M
其余参考资料： https://www.vpser.net/manage/iftop.html
```



## Q:  nmap 

## Q: mcjoin

## Q: dig 

## Q:限制cpu核数

- #### MD5SUM /dev/zero

```bash
> sudo md5sum /dev/zero & 
```

- #### stress

```bahs 
stress --cpu 2  # 限制的核数
```

- ####  屏蔽cpu

某些虚拟化环境允许在运行虚拟机的同时添加或去除 CPU。

要安全去除 CPU，请先执行以下命令以停用这些 CPU

```
root # echo 0 > /sys/devices/system/cpu/cpuX/online
```

COPY

请将 *X* 替换为 CPU 编号。要使 CPU 重新联机，请执行

```
root # echo 1 > /sys/devices/system/cpu/cpuX/online
```

## Q: 查看文件夹的创建时间

- #### stat

1. stat filename /dir   //       ls -i filename 

1. 获取文件inode号 

- #### df -h 

1. df -Th 
2. 找到对应的磁盘

- ####  debugfs

1. sudo debugfs -R 'stat  <Inode>'  /dev/device
2. crtime 为创建的时间Q

## Q: 脚本自动传参 tab补全

template

>complete   : https://www.jianshu.com/p/aa140acbfa62
>
>sudo apt install bash-completion

```bash
# demo.sh
#!/bin/bash

case "$1:$2:$3" in 
edit:test2-2:)
    echo "ok !!!!!!!!!!!"
;;
info::)
    echo "info"
;;
gateway::)
    echo "gateway"
;;
test:test1-3:)
	echo "test ok !!!!!!"
;;
esac 
```

```bash
# tools         save path : /etc/bash-completion.d/
#!/bin/bash

function _test_tools(){
        case $COMP_CWORD in
        1)
                COMPREPLY=($(compgen -W "info gateway edit test" -- ${COMP_WORDS[COMP_CWORD]}))
                ;;
        2)
                if [[ ${COMP_WORDS[1]} == "test" ]];then
                COMPREPLY=($(compgen -W "test1-1 test1-2 test1-3" -- ${COMP_WORDS[COMP_CWORD]}))
                fi
                if [[ ${COMP_WORDS[1]} == "edit" ]];then
                COMPREPLY=($(compgen -W "test2-1 test2-2 test2-3 test2-4" -- ${COMP_WORDS[COMP_CWORD]}))
                fi
                ;;
        esac
}

complete -F _test_tools demo.sh
```

other cfg   # add auto source 

```bash
# vim ~/.bashrc or .zshrc
for i in $(ls /etc/bash_completion.d/)
do
        . /etc/bash_completion.d/$i
done
```

## Q: C++编译保留coredump文件

```bash
> ulimit -c  
0表示没有打开，unlimited表示不限制产生文件大小   
# ulimit -c unlimited  打开core文件生成且不限制    ulimit -c 4194304(示例设置2G，单位为kbyte)
临时修改：
修改/proc/sys/kernel/core_pattern文件，但/proc目录本身是动态加载的，每次系统重启都会重新加载，因此这种方法只能作为临时修改
> echo /tmp/corefile/core-%e-%p-%t > /proc/sys/kernel/core_pattern
永久修改：
> vim /etc/sysctl.conf
'kernel.core_pattern = /tmp/corefile/core-%e-%p-%t'
'kernel.core_uses_pid = 0'
# 添加这两行 
#kernel.core_uses_pid 这个参数控制core文件的文件名是否添加pid作为扩展，如果这个文件的内容被配置成1，即使core_pattern中没有设置%p，最后生成的core dump文件名仍会加上进程ID
> sysctl –p /etc/sysctl.conf   # 使生效

参数list:
%p - insert pid into filename 添加pid(进程id)
%u - insert current uid into filename 添加当前uid(用户id)
%g - insert current gid into filename 添加当前gid(用户组id)
%s - insert signal that caused the coredump into the filename 添加导致产生core的信号
%t - insert UNIX time that the coredump occurred into filename 添加core文件生成时的unix时间
%h - insert hostname where the coredump happened into filename 添加主机名
%e - insert coredumping executable name into filename 添加导致产生core的命令名
```

## Q: **GDB**

```c++
gdb ./a.out coredump.xxxx 
```

