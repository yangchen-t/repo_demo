# docker images build 
```bash
 docker build -t dutyofficer:$(cat ./.env | awk -F "=" '{print$NF}') \
    --build-arg HTTP_PROXY=http://proxy.qomolo.com:8123/ \
    --build-arg HTTPS_PROXY=http://proxy.qomolo.com:8123/ \
    --build-arg ALL_PROXY=http://proxy.qomolo.com:8123/ \
    -f ./Dockerfile .
```