# 手动搭建git_server 

### 初始化仓库(server)

```shell
git init 

sudo apt-get update
sudo apt-get install openssh-client
sudo apt-get install openssh-server

# 修改配置文件
sudo vim /etc/ssh/sshd_config
# 添加以下配置
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PermitRootLogin yes
port=22

# 重启ssh服务
sudo /etc/init.d/ssh restart
```

### 添加必备配置信息 (server)

```shell
# vi  .git/config
[core]
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[receive]
        denyCurrentBranch = ignore
```

### 本地拉取远端repo (本地)

```shell
# 这次是git用户连接的ssh
git clone ssh://hostname@ip:22/xxx/xx/.git           #注意此时还是一个空的repo
```

### 本地repo配置  （本地）

```shell
# vi .git/config
#add 一下内容

[user]
    name = xx
    email = xx@xx.com                  #可以解决每次push是需要提交的用户名和email账号
```

### 示例 （本地）

```shell
touch test_git.txt
git add .
git commit -m "init"
git push --set-upstream origin master
git check -b xx-param                                                     #切换新的分支
```

git push 成功即可。





