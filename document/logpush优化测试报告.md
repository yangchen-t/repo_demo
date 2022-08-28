# logpush优化测试报告

- 分别模拟单个/双个/三个/同时进行logpush时的系统资源占比
- 分别从指令进程系统占用与gzip指令系统资源占用来比较优化情况

## 测试准备：

- IGV     = tj801
- qomolo-gcs-scripts = 0.3.21-79912
- 车辆运动状态下

## 测试过程：

### 日常占比：

![日常资源占用](/home/westwell/Pictures/日常资源占用.png)

**分析：**

大约整体cpu占比≈ 65%           浮动≈10%

### 单logpush_test:

指令进程图：

![单logpush_test](/home/westwell/Pictures/单logpush_test.png)

压缩图：

![gzip_limit](/home/westwell/Pictures/gzip_limit.png)

**分析：**

大约整体占比≈70%      浮动≈10%

### 双logpush_test:

指令进程图：

![双logpush_test](/home/westwell/Pictures/双logpush_test.png)

gzip 图：

![2022-08-17 15-01-44屏幕截图](/home/westwell/Pictures/2022-08-17 15-01-44屏幕截图.png)

**分析：**

大约整体占比≈75%      浮动≈10%      

### 三logpush_test：

指令进程占比图：

![三logpush_test](/home/westwell/Pictures/三logpush_test.png)

gzip压缩占比图：

![2022-08-17 15-15-15屏幕截图](/home/westwell/Pictures/2022-08-17 15-15-15屏幕截图.png)

**分析：**

大约整体占比≈75%      浮动≈10%  

进程约束较为理想： ≈78%    ，可以看到gzip压缩居高，≈87%   浮动≈10%

## 结论：

综上来看，使用此方法对数据备份有很大的优化系统资源占用，tar指令压缩占比仍居高，考虑到同时执行三个logpush,且同时压缩情况较少，并且设置gzip NI为最低级，故目前优化方案暂定为可行。

