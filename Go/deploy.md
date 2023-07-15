# golang 环境搭建

[TOC]



## install golang  source code 

```bash
官网： https://go.dev/dl/
wget https://go.dev/dl/go1.20.6.linux-amd64.tar.gz
```

## deploy to ubuntu 

```bash
sudo tar -C /usr/local -xzf go1.20.6.linux-amd64.tar.gz
sudo vim ~/.bashrc .zshrc 
add this line 
export PATH=$PATH:/home/cy/tools/:/usr/local/go/bin
```

## adapt env 

```bash
go env -w GO111MODULE=
# disable GOPATH use go mod 

template:
GO111MODULE=""
GOARCH="arm64"
GOBIN=""
GOCACHE="/home/nvidia/.cache/go-build"
GOENV="/home/nvidia/.config/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="arm64"
GOHOSTOS="linux"
GOINSECURE=""
GOMODCACHE="/home/nvidia/pkg/mod"
GONOPROXY=""
GONOSUMDB=""
GOOS="linux"
GOPATH="/home/nvidia/"
GOPRIVATE=""
GOPROXY="https://goproxy.cn,direct"
GOROOT="/usr/local/go"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/linux_arm64"
GOVCS=""
GOVERSION="go1.20.3"
GCCGO="gccgo"
AR="ar"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
GOMOD="/home/nvidia/go/go.mod"
GOWORK=""
CGO_CFLAGS="-O2 -g"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-O2 -g"
CGO_FFLAGS="-O2 -g"
CGO_LDFLAGS="-O2 -g"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -pthread -Wl,--no-gc-sections -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build1203509320=/tmp/go-build -gno-record-gcc-switches"
bin path: /usr/local/go
worksapce: /home/nvidia/go/
```

## init mod modules

```bash
cd ${workspace}
go mod init ${workspace}
go mod tidy 
```