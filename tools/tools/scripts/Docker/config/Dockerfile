FROM ubuntu

RUN apt-get update && \
apt install -y net-tools vim tree python3 python3-paramiko supervisor python3-flask && \
apt-get install -f 


COPY ./config/cyclonedds.xml /cyclonedds.xml
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 
COPY scripts/* /scripts/

EXPOSE 80 
 

