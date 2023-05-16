# #!/usr/bin/env python3

import matplotlib.pyplot as plt
import subprocess
import sys


plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

timelist = []
datalist = []


def DataAllocation(datacmd, timecmd, ret):
    for i in range(int(ret)):
        i = i+1
        ret = subprocess.getoutput(
            timecmd + "| head -n {0} | tail -n 1".format(i))
        DataRet = subprocess.getoutput(
            datacmd + "|head -n {0} | tail -n 1".format(i))
        ret = subprocess.getoutput("date -d '{0}' +%s".format(ret))      # unix time
        timelist.append(ret)
        datalist.append(float(DataRet))
    return 0


def cpuidledata(FILENAME):
    timecmd = "cat {0}| grep all | awk '{1}'".format(
        FILENAME, "{print$1,$2,$3}")
    datacmd = "cat {0} | grep all | awk '{1}'".format(FILENAME, "{print$13}")
    ret = subprocess.getoutput(timecmd + "| wc -l")
    if int(ret) == 0:
        print(FILENAME + " is not all cpu info, please check")
        exit(-1)
    DataAllocation(datacmd, timecmd, ret)


def unitcpudata(FILENAME, MODULE):
    if subprocess.getoutput("cat {0} | grep {1}".format(FILENAME, MODULE)) != "":
        pass
    else:
        print(MODULE + "is not exist <<{0}>>, please check".format(FILENAME))
        exit(-1)
    time = "cat {0}| grep {1} | awk '{2}'".format(
        FILENAME, MODULE, "{print$1,$2,$3}")
    data = "cat {0}| grep {1} | awk '{2}'".format(
        FILENAME, MODULE, "{print$6}")
    ret = subprocess.getoutput(time + "| wc -l")
    DataAllocation(data, time, ret)


def dataview(msg):
    x = range(len(timelist))
    plt.figure(figsize=(10, 4))
    plt.grid()
    plt.plot(x, datalist, 'o-')
    plt.legend([msg])
    plt.xticks(x, timelist, rotation=45)
    # for xy in zip(x,datalist):                               #给每个点加标注
    #     plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
    # plt.savefig('curentlosschange',bbox_inches = 'tight',pad_inches = 0,dpi =1050)
    plt.show()


def main():
    if len(sys.argv) < 2:
        print("please input log path")
        exit(-1)
    elif sys.argv[2] == "-a":
        cpuidledata(str(sys.argv[1]))
        dataview(msg="all cpu idle")
    elif sys.argv[2] == "-c":
        if len(sys.argv) < 4:
            print("please input module")
            exit(-1)
        unitcpudata(str(sys.argv[1]), str(sys.argv[3]))
        dataview(msg=str(sys.argv[3]))
    else:
        print("args error")

    return 0


if __name__ == '__main__':
    main()
    # print(datalist)
    # print(timelist)
    print("avg: ", sum(datalist)/len(datalist))

