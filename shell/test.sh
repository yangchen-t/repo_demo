# if [[ ! -d  /opt/qomolo/gst-plugin/plugin ]];then
#         sudo mkdir -p /opt/qomolo/gst-plugin/plugin
# else    
#         sudo scp qomolo@10.159.101.1:~/0618.tar.gz .
# fi	

#!/bin/bash

QOMOLO_IP=$1
QOMOLO_ROBOT_ID=$2${QOMOLO_IP:7:1}-${QOMOLO_IP:9}




echo ${QOMOLO_IP:7:1}
echo $QOMOLO_ROBOT_ID