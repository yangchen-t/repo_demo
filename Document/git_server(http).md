

服务器：Ubuntu18.04

## 准备工作：

1、安装Git

```bash 
apt-get install git
```

2、安装nginx

```bash
apt-get install nginx
```

3、安装 fcgiwrap

```bash
apt-get install fcgiwrap
```

4、新建裸仓库

```bash
sudo git init --bare /opt/config/
```

修改仓库权限，让所有用户均可修改

```bash
sudo chmod -R a+w /opt/config/
```

5、Nginx配置访问路径
我的目的是在 nginx 的默认网站下添加一个虚拟目录 /git/ ， 通过访问 /git/xxx 的形式来访问服务器上的 xxx.git 代码库， 这就需要修改一下 nginx 默认网站的配置文件 /etc/nginx/sites-available/default ， 添加下面的信息：

## 配置以 /git 开始的虚拟目录
```c++
location ~ /git(/.*) {
使用 Basic 认证
    auth_basic "Restricted";
    # 认证的用户文件
    auth_basic_user_file /etc/nginx/passwd;
    # FastCGI 参数
    fastcgi_pass  unix:/var/run/fcgiwrap.socket;
    fastcgi_param SCRIPT_FILENAME /usr/lib/git-core/git-http-backend;
    fastcgi_param GIT_HTTP_EXPORT_ALL "";
    # git 库在服务器上的跟目录
    fastcgi_param GIT_PROJECT_ROOT    /opt;
    fastcgi_param PATH_INFO           $1;
    # 将认证用户信息传递给 fastcgi 程序
    fastcgi_param REMOTE_USER $remote_user;
    # 包涵默认的 fastcgi 参数；
    include       fastcgi_params;
    # 将允许客户端 post 的最大值调整为 100 兆
    max_client_body_size 100M;
}
```

重新加载nginx配置

```bash
nginx -s reload
```

6、Nginx鉴权
让Nginx来管理访问时的用户鉴权，用以下命令增加一个git用户并按提示设置密码，可以创建多个用户。

```bash
htpasswd  /etc/nginx/passwd git
```

如果提示没有htpasswd命令，需要先安装apache2-utils包：apt-get install apache2-utils。

/etc/nginx/passwd为用户名和密码文件，-c 参数表示创建一个新的密码文件，原来没有这个文件时必须要带，已经存在这个文件了就不要带-c参数了。

7、结束
可以使用 git clone https://server-name/git/config 克隆仓库。

若仓库接收git push时报错403，可在仓库中设置git config http.receivepack true
