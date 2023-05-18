[TOC]

# Ubuntu18.04

## Server

### 1.install

```bash
sudo apt update ;sudo apt install nginx git fcgiwrap -y 
```

### 2.Create Git Repositories

```bash
workspace = "/data/repo.git"
sudo mkdir ${workspace}
sudo chown -R ${USER}:${USER} ${workspace}
```

### 3.Set configure Nginx

```bash
sudo vim /etc/nginx/sites-available/default

Look for the following section:

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }

Under that section, paste the following:
# add below this line 
location ~ (/.*) {
    client_max_body_size 0; # Git pushes can be massive, just to make sure nginx doesn't suddenly cut the connection add this.
    auth_basic "Git Login"; # Whatever text will do.
    auth_basic_user_file "${workspace}/htpasswd";
    include /etc/nginx/fastcgi_params; # Include the default fastcgi configs
    fastcgi_param SCRIPT_FILENAME /usr/lib/git-core/git-http-backend; # Tells fastcgi to pass the request to the git http backend executable
    fastcgi_param GIT_HTTP_EXPORT_ALL "";
    fastcgi_param GIT_PROJECT_ROOT ${workspace}; # /var/www/git is the location of all of your git repositories.
    fastcgi_param REMOTE_USER $remote_user;
    fastcgi_param PATH_INFO $1; # Takes the capture group from our location directive and gives git that.
    fastcgi_pass  unix:/var/run/fcgiwrap.socket; # Pass the request to fastcgi
}

sudo nginx -t     # check configuration
# normal output 
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### 4.Create a User Account

```bash
sudo htpasswd -c ${workspace}/htpasswd new_account   
sudo systemctl restart nginx
```

### 5.Create Your First Repositories

```bash
cd ${workspace}
sudo mkdir work.git 
cd work.git 
sudo git init
sudo git update-server-info 
sudo chown -R ${USER}:${USER} .
sudo chomod -R 755 . 
```

## Client

### push remote repositories

#### 	1.Connect to the Repositories

```bash
sudo apt update ;sudo apt install git -y 
mkdir ~/workspace 
cd ~/worksapce
git init 
git remote add origin http://new_account@SERVER_IP/work.git 
# test 
mkdir test1 test2 test3 
touch test1/1 test2/2 test3/3
git add . && git commit -am "test directories and files added"
git push origin master 
```

### pull remote repositories

#### 	1.Clone the New Repositories

```bash
git clone http://new_account@SERVER_IP:/${workspace}/work.git 
```

>reference:
>
>https://thenewstack.io/how-to-set-up-the-http-git-server-for-private-projects/



## Q&A

- nginx  [Failed to start A high performance web server and a reverse proxy server](https://stackoverflow.com/questions/51525710/nginx-failed-to-start-a-high-performance-web-server-and-a-reverse-proxy-server)

try this first

```bash
sudo service apache2 stop
sudo systemctl restart nginx
```

- git push  error: remote unpack failed: unable to create temporary object directory

try this first 

```bash
in server 
sudo chmod -R 777 ${workspace}
```

