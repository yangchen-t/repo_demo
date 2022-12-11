#FROM osrf/ros:foxy-desktop as ros
FROM ubuntu
RUN apt-get update && \
apt install -y net-tools vim curl gnupg2 lsb-release sudo tree python3 python3-paramiko supervisor python3-flask && \
apt-get install -f 

COPY ./Dockerfile /scripts/
EXPOSE 80 8080 5000 



