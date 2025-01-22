# docker images build 
```bash
 docker build -t dutyofficer:$(cat ./.env | awk -F "=" '{print$NF}') \
    --build-arg HTTP_PROXY=http://proxy.qomolo.com:8123/ \
    --build-arg HTTPS_PROXY=http://proxy.qomolo.com:8123/ \
    --build-arg ALL_PROXY=http://proxy.qomolo.com:8123/ \
    -f ./Dockerfile .
```

## compress & uncompress
```bash
docker save gateway_show_information:0.2 | xz > gateway_show.tar.xz
xz -d < gateway_show.tar.xz | docker load
```

## deploy auto add iptables
```bash
bash deploy.sh enable
```