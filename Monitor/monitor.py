from jtop import jtop, JtopException
import csv
# import matplotlib as mp
import argparse
import psutil
import time

import tools as liunx

process_list = ["fusion_localize", "vehicle_control"]
count = 10

class SystemMonitor(object):
    def __init__(self) -> None:
        self.time = []
        self.processCpuList = []
        self.processRssList = []
        self.processMemList = []
        self.processGpuList = []

    def GetProcessName(self):
        for i in process_list:
            for ts in range(count):
                self.time.append(time.time())
                self.processCpuList.append(self.GetCpuInfo(i))
                self.processRssList.append(self.GetMemInfo(i)[0])
                self.processMemList.append(self.GetMemInfo(i)[1])

    def GetCpuInfo(self,process):
        return liunx.cpuExec(process) 
        
    def GetMemInfo(self,process):
        return liunx.memExec(process) 

    def GetGpu(self):
        parser = argparse.ArgumentParser(description='Simple jtop logger')
        # Standard file to store the logs
        parser.add_argument('--file', action="store", dest="file", default="log.csv")
        args = parser.parse_args()
    
        print("Simple jtop logger")
        print("Saving log on {file}".format(file=args.file))
    
        try:
            with jtop() as jetson:
            #  notes: jetson.ok() will provide the proper update frequency
                # with open(args.file, 'w') as csvfile:
                    while jetson.ok():
                        # Print all cpu
                        for process in jetson.processes:
                            print(process)
    
        except JtopException as e:
            print(e)
        except KeyboardInterrupt:
            print("Closed with CTRL-C")
        except IOError:
            print("I/O error")
    def flamegraph(self):
        # TODO  perf cmd 
        pass
    
    def View(self):
        print(self.time)
        print(self.processCpuList)
        print(self.processRssList)
        print(self.processMemList)

    def Free(self):
        self.time.clear
        self.processCpuList.clear
        self.processRssList.clear
        self.processMemList.clear 

if __name__ == "__main__":
    sm = SystemMonitor()
    # sm.flamegraph()
    sm.GetProcessName()
    sm.View()
    sm.Free()