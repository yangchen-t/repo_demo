

## 0 实验环境

*	3 台 vm
*	glusterfs 共享存储目录
*	iptables 全开



## 1 安装pacemaker相关

```bash
apt-get -y install pacemaker corosync
```



## 2 配置corosync 

### 2.1 生成 authkey

```bash
apt install -y haveged

corosync-keygen
会在 /etc/corosync/下生成authkey
```

### 2.1 编辑 corosync.conf

```bash
totem {
	version: 2
	secauth: off
	cluster_name: pacemaker1
	transport: udpu

    interface {
        ringnumber: 0
        bindnetaddr: 192.168.122.251
        broadcast: yes
        mcastport: 5407
      }
}

nodelist {
	node {
		ring0_addr: 192.168.122.217
		name: vm1
		nodeid: 101
	}
	node {
		ring0_addr: 192.168.122.218
		name: vm2
		nodeid: 102
	}
	node {
		ring0_addr: 192.168.122.157
		name: vm3
		nodeid: 103
	}
}

quorum {
	provider: corosync_votequorum
}
```

### 2.2 分发配置

```bash
scp -r /etc/corosync/* root@vm2:/etc/corosync/
scp -r /etc/corosync/* root@vm3:/etc/corosync/
```



## 3 启动 pacemaker corosync

```basj
systemctl start pacemaker corosync

crm_mon 查看集群状态
```



## 4 准备nexus脚本及service

```bash
cat > /data/nexus/nexus.sh << 'EOF'
#!/bin/bash

case $1 in
    start)
        docker-compose -f /data/nexus/docker-compose.yaml up -d
        sleep 10
        while :
        do
            docker ps -a | grep nexus | grep Up
            if [[ $? != 0 ]];then
                break
            else
                sleep 10
            fi
        done
        ;;
    stop)
        docker-compose -f /data/nexus/docker-compose.yaml down
        ;;
    reload)
        docker-compose -f /data/nexus/docker-compose.yaml down
        docker-compose -f /data/nexus/docker-compose.yaml up -d
esac
EOF

# 分发到3台
cat > /lib/systemd/system/nexus.service << 'EOF'
[Unit]
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/data/nexus/nexus.sh start
ExecReload=/data/nexus/nexus.sh reload
ExecStop=/data/nexus/nexus.sh stop

[Install]
WantedBy=multi-user.target
EOF
```



## 5 配置crm

```bash
crm configure property stonith-enabled=false
crm configure property no-quorum-policy=ignore

crm configure primitive VIP \
              ocf:heartbeat:IPaddr2 params ip="192.168.122.251" 
              cidr_netmask="24" op monitor interval="10s" \
              meta migration-threshold="10"

crm configure primitive nexus systemd:nexus \
	          op start interval=0 timeout=100 \
	          op stop interval=0 timeout=100 \
	          op monitor interval=10s \
              meta migration-threshold=10 target-role=Started
              
group HA VIP nexus
```



## 6 验证

```bash
crm_mon 
查看当前 VIP 和 nexus 的启动状态

模拟一台失联，在任一台执行
crm cluster stop

在余下2台上执行 crm_mon 观察 VIP和 nexus 的启动状态
```



## 7 ...

```bash
资料太少，存在问题未知

参考
https://www.howtoforge.com/tutorial/how-to-set-up-nginx-high-availability-with-pacemaker-corosync-and-crmsh-on-ubuntu-1604/

https://clusterlabs.org/quickstart-ubuntu.html
```

