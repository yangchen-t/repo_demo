# 完美仿真器启动教程（Step by step）

[TOC]

## 安装apt源（如已安装，可跳过）

```
sudo wget https://repo.qomolo.com/repository/raw/gpg/public.gpg.key -O- | sudo apt-key add
echo "deb [arch=amd64] https://repo.qomolo.com/repository/alpha/ focal main" | sudo tee /etc/apt/sources.list.d/qomolo-foxy.list
sudo apt update
```



## 安装二进制（如已安装，可跳过）
安装最新的版本

```
sudo apt install ws-onsite-ws-perfect-simstraddle
```

指定使用一个版本

```
sudo apt install ws-onsite-ws-perfect-simstraddle=指定版本
```



## 安装setup脚本（如已安装，可跳过）

```
sudo apt install qomolo-ws-setup
```



## 配置启动脚本

配置脚本的目的主要是在于

1. 设置启动多少辆车？
2. 设置启动的命名空间？



在此部分，我们用到的部分就是`/opt/qomolo/utils/ws_setup/perfectsim`下面的所有

### 1. 更改权限

/opt/qomolo/下面的启动脚本默认属于root

```
cd /opt/qomolo/utils/ws_setup
sudo chown $USER:$USER -R perfectsim
```

更改完权限后，就可以不用`sudo`启动脚本了



### 2. 修改启动文件

#### 修改`start`文件

`start`文件主要用来启动仿真车

```
vim /opt/qomolo/utils/ws_setup/perfectsim/start
```

打开后可以看到下面

```
#!/bin/bash

ROBOT_NS=ahs
ROBOT_START_IDX=1
ROBOT_END_IDX=1
ROS_WORKSPACE=qpilot
HOST_IP=localhost
INTERVAL=1 # seconds

QOMOLO_CONFIGURATION_PATH=/opt/qomolo/$ROS_WORKSPACE/share/qpilot_parameters
QOMOLO_DATA_DIR=/opt/qomolo/utils/ws_setup/perfectsim/data
```

需要设置：

* ROBOT_NS：仿真车的命名空间，同QOMOLO_ROBOT_ID
* ROBOT_START_IDX：仿真车如果起很多车的话，车号从ROBOT_START_IDX开始
* ROBOT_END_IDX：仿真车如果起很多车的话，车号到ROBOT_END_IDX结束
* ROS_WORKSPACE：二进制的名称，如何设置这个呢？你只需要知道你的二进制目录的地址就行了，例如
  * `/opt/qomolo/qpilot`，那么设置为ROS_WORKSPACE=qpilot
  * `/opt/qomolo/ws_cpc_ng`，那么设置ROS_WORKSPACE=ws_cpc_ng
* INTERVAL：车与车之间调用启动的间隔时间，INTERVAL=1相当于每隔1秒启动一个车。为什么设置这个值呢，是因为连续启动很多仿真车对机器的性能时有要求的，对于一些服务器，不能启动的太快，就要调大启动间隔。
* QOMOLO_CONFIGURATION_PATH：这个自动设置为和ROS_WORKSPACE相关联了，这个无需改动
* QOMOLO_DATA_DIR：因为`perfectsim`下面自带一个/data文件夹，所以默认使用`/opt/qomolo/utils/ws_setup/perfectsim/data`，这个也可以自定义路径
* HOST_IP：设置这个IP为当前本机服务器的IP，也可以设置为localhost，但是与此同时要在`docker run`里面加入`--network host`，这样和宿主机通的，可以用于可视化



举例1

我现在想跑ceke仿真，20辆车，从ck1到ck20，每隔5秒启动一辆车，当前机器在局域网地址为192.168.103.15，那么修改相关变量如下：

```
#!/bin/bash

ROBOT_NS=ck
ROBOT_START_IDX=1
ROBOT_END_IDX=20
ROS_WORKSPACE=qpilot
HOST_IP=192.168.103.15
INTERVAL=5 # seconds
```

举例2

我现在想跑ctn仿真，1辆车7号车，每隔1秒启动一辆车（事实上启动一辆车这个变量无所谓），那么修改相关变量如下：

```
#!/bin/bash

ROBOT_NS=ctn
ROBOT_START_IDX=7
ROBOT_END_IDX=7
ROS_WORKSPACE=qpilot
HOST_IP=192.168.103.15
INTERVAL=1 # seconds
```

#### 修改`stop`文件

`stop`文件主要用来关闭仿真车

```
vim /opt/qomolo/utils/ws_setup/perfectsim/stop
```

打开后可以看到下面

```
#!/bin/bash

ROBOT_NS=ctn
ROBOT_START_IDX=1
ROBOT_END_IDX=2
```

需要设置：

* ROBOT_NS：仿真车的命名空间，同QOMOLO_ROBOT_ID
* ROBOT_START_IDX：仿真车如果起很多车的话，车号从ROBOT_START_IDX开始
* ROBOT_END_IDX：仿真车如果起很多车的话，车号到ROBOT_END_IDX结束

这三个变量和start同理



## 修改启动文件（可能需要，可能不需要）

仿真器启动将会找

```
vim /opt/qomolo/ws_perfect_simstraddle/share/simulation_bringup/launch/simulation.launch.py
```
在这个路径下修改


## 启动/关闭

启动

```
./start
```

关闭

```
./stop
```



## Q&A

### 1. perfectsim启动做了哪些改动？

1. 使用supervisorctl，管理每一个节点，每个车带一个。每个车的port不一样，port=10000+车号。
2. 添加了一个node，启动的时候，自动发送command=1的ros2 topic，将仿真器带起来
3. 每个车分配一个不同的ROS_DOMAIN_ID，各自隔离起来，不会串扰。每个车的ROS_DOMAIN_ID不一样，ROS_DOMAIN_ID=10+车号
4. 加入了一些shell打印，帮助理解发生了什么



### 2. 用perfectsim需要具备哪些前提条件？

* 会使用supervisorctl
* 理解ROS_DOMAIN_ID的含义



### 3. 仿真器起来了，但是我想可视化看车走？

首先要把docker网络设置为localhost,这样才能把ROS的topic传到外面  
比如ctn1起来了，你想看ctn1的路径，那么需要打开一个terminal

```
export ROS_DOMAIN_ID=你的车的DOMAIN_ID
ros2 run rviz2 rviz2 --ros-args --remap /tf:=/ctn1/tf --remap /tf_static:=/ctn1/tf_static
```



### 4. 日志哪里可以看到？

日志在docker内外都可以看到，如果要看某一辆车，就需要进这辆车的docker里面

```
docker exec -it perfectsimctn1 bash
cd /log
```

也可以在docker外面看，启动仿真器会自动创建`~/qlog`，下面会有很多类似于`1`,`2`,`3`的文件夹，代表几号车的日志



### 5. 日志里面有很多.log，分别代表什么节点？

```
agent.log  container.log  entrypoint.log  init.log  mqtt.log  navigation.log
```

navigation.log：这个是simulator的日志

container.log：跨运车集装箱操作的日志

mqtt.log：mqtt的日志

以上是最常用的



### 6. 我想跑跨运车仿真，需要额外做一些什么？

container的模块其实也起了一个可以发送function_control/state的东西，而simulator本身也发送了，所以记得在`simulation.launch.py`里面将simulator部分的remap掉，比如把它remap成function_control/state/backup，默认用container里面提供的function_control

```
remapping.append(("function_control/state",  "function_control/state/backup"))
```



### 7. 我想跑非跨运车仿真，需要额外注意些什么？

container模块是根据命名空间识别的，如果不是跨运车（ahs, ctn），是不需要也不能起container模块的。所以不需要做任何其他操作