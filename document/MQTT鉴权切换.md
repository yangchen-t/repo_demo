# MQTT鉴权切换

## 了解：

- 鉴权文件
- 生产模式
- 预生产模式
- debug模式

## 鉴权文件

```shell
每个单车都存在一个 certificate       #鉴权证书
存放路径：          cd /data/code/all_ws/ws


#是否携带鉴权证书
程序会自动读取 /data/code/all_ws/ws/ certificate  鉴权文件
不携带 鉴权证书    只需要破坏他的文件名字即可
#例          mv  certificate  certificate_A001          or         mv  certificate ~       #（将文件移动出/data/code/all_ws/ws即可）
```

## 生产模式：

```shell
MQTT_SERVER_IP=172.31.3.191
MQTT_SERVER_PORT=8883                            #需要带鉴权证书
```

## 预生产模式：

```shell
MQTT_SERVER_IP=172.31.2.96
MQTT_SERVER_PORT=30845                          #不需要带鉴权证书
```

## DEBUG模式：

```shell
MQTT_SERVER_IP=10.159.201.208
MQTT_SERVER_PORT=1883                              #不需要带鉴权证书
```

## 详情：

```python
由于码头情况时常有变动，导致需要来回切换环境来配合码头进行测试，目前主要有上诉几种不同环境
只需要切换不同的MQTT_SERVER_IP/MQTT_SERVER_PORT 来进行更换,并且进行<<重启>>即可
#注     上诉备注了环境是否需要具备鉴权证书的情况。
```



