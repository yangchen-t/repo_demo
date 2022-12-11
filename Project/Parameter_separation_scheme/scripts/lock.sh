#!/bin/bash



source /opt/qomolo/utils/qpilot_setup/all_supervisord/.env || true

while :
do
	sleep 1
	key=`cat /home/nvidia/.env`
      key_list="/opt/qomolo/utils/qpilot_setup/tools/.git_namelist"

      if [[ $key == "westwell-lab" ]];then
            # echo nvidia | sudo -S sudo chattr -R -i /opt/qomolo/qpilot-hw-param
            echo nvidia | sudo -S sudo chattr -R -i /opt/qomolo/qpilot-param
            sleep 300
      # 判断匹配函数，匹配函数不为0，则包含给定字符
      elif [ `grep -c "$key" $key_list` -ne '0' ];then
		echo "ok"
	    sudo chattr -R -i /opt/qomolo/qpilot-hw-param
            sleep 1
            cd /opt/qomolo/qpilot-hw-param/ && sshpass -p xijingkeji git pull
	    sleep 300
            change_msg=`cd /opt/qomolo/qpilot-hw-param/ && git status -s`
            sleep 10
	    cd /opt/qomolo/qpilot-hw-param/ && git add . && git commit -m "$key-$change_msg" && sshpass -p xijingkeji git push
            sleep 100
	else
	    echo "lock"
	    echo nvidia | sudo -S chattr -R +i /opt/qomolo/qpilot-hw-param
          echo nvidia | sudo -S chattr -R +i /opt/qomolo/qpilot-param
	fi
         echo "@" > /home/nvidia/.env
      #   done
done
