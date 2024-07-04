system_performance

memory

note:

>调整开始启用swap的默认值，由于内存的速度要比磁盘快的多，理论来说，减少磁盘接入或者延迟提前使用swap做交换分区均能达到优化的效果。
>
>内存在使用到100-60=40%的时候，就开始出现有交换分区的使用。大家知道，内存的速度会比磁盘快很多，这样子会加大系统io，同时造的成大量页的换进换出，严重影响系统的性能，所以我们在操作系统层面，要尽可能使用内存，对该参数进行调整。
>
>config:  cat /proc/sys/vm/swappiness  # default = 60

临时调整：

```bash
sudo sysctl vm.swappiness=10
sudo sysctl -p
```

永久调整：

```bash
cat /etc/sysctl.conf
vm.swappiness=xx
sudo sysctl -p
sudo reboot
```

>refer: https://www.cnblogs.com/erlou96/p/13291663.html

cache&buffer

note：

>清除Linux系统缓存
>
>/proc/sys/vm/drop_caches   default: 0

drop_caches的值可以是0-3之间的数字，代表不同的含义：

0：不释放（系统默认值）;默认情况下表示不释放内存，由操作系统自动管理;
1：释放页缓存;To free pagecache.
2：释放dentries和inodes；To free dentries and inodes.
3：释放所有缓存；To free pagecache, dentries and inodes.

临时调整：

```bash
echo 1 >/proc/sys/vm/drop_caches
echo 2 >/proc/sys/vm/drop_caches
echo 3 >/proc/sys/vm/drop_caches
sudo sysctl -w vm.drop_caches=1
sudo sysctl -w vm.drop_caches=2
sudo sysctl -w vm.drop_caches=3
sysctl -p
```

永久调整：

```bash
cat /etc/sysctl.conf
vm.drop_caches=1/2/3
sysctl -p 
sudo reboot
```

官方描述:

```txt
drop_caches

Writing to this will cause the kernel to drop clean caches, as well as
reclaimable slab objects like dentries and inodes.  Once dropped, their
memory becomes free.

To free pagecache:
	echo 1 > /proc/sys/vm/drop_caches
To free reclaimable slab objects (includes dentries and inodes):
	echo 2 > /proc/sys/vm/drop_caches
To free slab objects and pagecache:
	echo 3 > /proc/sys/vm/drop_caches

This is a non-destructive operation and will not free any dirty objects.
To increase the number of objects freed by this operation, the user may run
`sync' prior to writing to /proc/sys/vm/drop_caches.  This will minimize the
number of dirty objects on the system and create more candidates to be
dropped.

This file is not a means to control the growth of the various kernel caches
(inodes, dentries, pagecache, etc...)  These objects are automatically
reclaimed by the kernel when memory is needed elsewhere on the system.

Use of this file can cause performance problems.  Since it discards cached
objects, it may cost a significant amount of I/O and CPU to recreate the
dropped objects, especially if they were under heavy use.  Because of this,
use outside of a testing or debugging environment is not recommended.

You may see informational messages in your kernel log when this file is
used:

	cat (1234): drop_caches: 3

These are informational only.  They do not mean that anything is wrong
with your system.  To disable them, echo 4 (bit 2) into drop_caches.
```



>refer:
>
>https://www.kernel.org/doc/Documentation/sysctl/vm.txt
>
>https://blog.51cto.com/moerjinrong/2141884