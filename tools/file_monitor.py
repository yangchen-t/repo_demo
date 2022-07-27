#!/usr/bin/env python3

import time
import subprocess
from watchdog.events import *
from watchdog.observers import Observer


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def git_cmd_remote(self):
        name_str = subprocess.getoutput("cat ~/.env")
        subprocess.getoutput('cd /home/westwell/Desktop/qpilot_setup && git pull && git add . && git commit -m "{}" && git push '.format(name_str))
        print(subprocess.getoutput("sudo echo "" > ~/.env"))
        print("git push finish")

    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "/home/westwell/Downloads", True)
    time.sleep(60)
    event_handler.git_cmd_remote()
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

