FROM ubuntu

RUN apt-get update && \
apt install -y net-tools vim tree python3 python3-paramiko supervisor python3-flask && \
apt-get install -f 




COPY scripts/* /scripts/

EXPOSE 80 
 

