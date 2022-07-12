if [[ ! -d  /opt/qomolo/gst-plugin/plugin ]];then
        sudo mkdir -p /opt/qomolo/gst-plugin/plugin
else    
        sudo scp qomolo@10.159.101.1:~/0618.tar.gz .
fi	
