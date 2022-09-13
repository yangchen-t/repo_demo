#!/usr/bin/env python3

import time,sys
import subprocess
from watchdog.events import *
from watchdog.observers import Observer
import os 

subprocess.getoutput("echo nvidia | sudo -S chown -R nvidia /home/nvidia/.env")
subprocess.getoutput("source /opt/qomolo/utils/qpilot_setup/all_supervisord/.env || true")
ROBOT_ID = os.environ.get('ROBOT_ID')

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def git_cmd_remote(self):
        print("start cmd")
        print(subprocess.getoutput("echo nvidia | sudo -S chown -R nvidia /opt/qomolo/qpilot-hw-param"))
        print(subprocess.getoutput("cd /opt/qomolo/qpilot-hw-param && sshpass -p xijingkeji git pull origin {0}-param ".format(ROBOT_ID) ))
        print(subprocess.getoutput("cd /opt/qomolo/qpilot-hw-param && sudo git add . && sudo git commit -m '{0}'".format(name_str)))
        print(subprocess.getoutput("cd /opt/qomolo/qpilot-hw-param && sshpass -p xijingkeji  git push origin {0}-param ".format(ROBOT_ID)))
        print("git push finish")
        time.sleep(5)
        print(subprocess.getoutput("echo 1 | sudo -S echo "" > /home/nvidia/.env"))


if __name__ == "__main__":

    while True:
        flag = False
        name_str = subprocess.getoutput("echo 1 | sudo -S cat /home/nvidia/.env")
        time.sleep(1)
        print(name_str)
        if name_str == "xiangyang.chen" and name_str == "ning.xu":
                subprocess.getoutput("echo 1 | sudo -S chattr -R -i /opt/qomolo/qpilot-hw-param")
                print("1")
                observer = Observer()
                event_handler = FileEventHandler()
                observer.schedule(event_handler, sys.argv[1], True)
                time.sleep(300)
                event_handler.git_cmd_remote()
                observer.start()

                ##sleep
                # try:
                    # while True:
                        # time.sleep(1)
                # except KeyboardInterrupt:
                    # observer.stop()
                    # observer.join()

        else :
                subprocess.getoutput("echo 1 | sudo -S chattr -R +i /opt/qomolo/qpilot-hw-param")
                print("lock")
