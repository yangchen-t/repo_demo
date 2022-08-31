# ubuntu

>#### 本文主要用于记录日常遇到的问题及解决方法，留下备份，为下次出现提供快速的解决方法。



### Q：如何设置磁盘的自动挂载？

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

### Q： 如何实现scp 断点续传

```shell
# rsync -P --rsh=ssh pic.tar.gz 192.168.205.304:/home/199_home.tar

说明：
-P: 是包含了 "–partial –progress"， 部分传送和显示进度
-rsh=ssh 表示使用ssh协议传送数据
```

