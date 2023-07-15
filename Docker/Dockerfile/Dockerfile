FROM ubuntu:20.04

ENV HTTP_PROXY=proxy.qomolo.com:8123
ENV HTTPS_PROXY=proxy.qomolo.com:8123

RUN apt-get update && apt install vim  git wget sudo -y  
RUN wget -q https://go.dev/dl/go1.20.6.linux-amd64.tar.gz  &&\
    tar -C /usr/local -xzf go1.20.6.linux-amd64.tar.gz 

ENV PATH=$PATH:/usr/local/go/bin 
