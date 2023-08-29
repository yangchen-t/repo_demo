import sys
import os
import folium
import subprocess


class GpsView(object):

    def __init__(self, gps, iperf) -> None:
        self.gpsData = gps
        self.iperfData = iperf

        self.globalgps = []
        self.disconnet=[]
        self.arr={}

        self.tmp = "zreo_hang"
        self.tmpcsv = "bad-gps.csv"
        self.tmplog = "net.log"
        self.tmpgpscsv = "gps.csv"
        self.output = "gps.HTML"
        self.ignore = ['0.00000000000', '0.00000000000']

        self.hang= 1
        self.dir=os.getcwd()

    #数据处理
    def DataAnalysis(self):
        cmd = "cat {0} | sed -e '/00*.*.sec/!d'  | sed -e '/SUM/d' -e '/sender/d' -e '/receiver/d' | sed -e '/-/!d' > net.log".\
                    format(self.gpsData)
        subprocess.getoutput(cmd)
        cmd = "cat {0} | sed -e '/^#BESTPOSA/!d' | awk -F ',' '{1}'  >  gps.csv" .\
                    format(self.iperfData, """{print $12","$13}""")
        subprocess.getoutput(cmd)

        #获取断连gps坐标文件
        print(subprocess.getoutput("""awk -F " " '{0}' {1} | cat -n | grep 0.00 | awk -F " " '{2}' > {3}"""\
                                    .format("{print $7}", self.tmplog, "{print $1}", self.tmp)))
        numbers = int(subprocess.getoutput("cat {0} | wc -l".format(self.tmp)))
        numbers -= 1
        for i in range(numbers):
            self.arr[i] = subprocess.getoutput("""sed -n "{0} p" {1}""".format(self.hang, self.tmp))
            self.hang += 1

        for i,p in self.arr.items():
            subprocess.getoutput("""sed -n "{0} p" {1} >> {2}""".format(p, self.tmpgpscsv, self.tmpcsv))

        
        # globalgps 全局坐标区间的变量赋值
        with open("{0}/{1}".format(self.dir, self.tmpgpscsv), "r") as f :
            for line in f :
                self.globalgps.append(list(line.strip("\n").split(",")))
        f.close()

        i = 0
        while i < len(self.globalgps):
            if self.globalgps[i] != self.ignore:
                self.globalgps[i] = list(map(float, self.globalgps[i]))
            else:
                pass
            i+=1

        # 如果没有断连情况则 disconnet 为空
        file = "{0}/{1}" .format(self.dir, self.tmp)
        if not os.path.getsize(file):
            self.disconnet.clear()
        else:
            # disconnet 断连坐标区别的变量赋值
            with open("{0}/{1}" .format(self.dir, self.tmpcsv), "r") as f :   
                for line in f :
                    self.disconnet.append(list(line.strip("\n").split(",")))
                self.disconnet[0] = list(map(float, self.disconnet[0]))
            f.close()  
    
    def draw_gps(self):
        m1 = folium.Map(self.globalgps[0], 
                    zoom_start=15, 
                    tiles='https://mt.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', ## google
                    attr='default'
                    )  # 中心区域的确定

        folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
            self.globalgps,  # 将坐标点连接起来
            weight=3,  # 线的大小为3
            color='green',  # 颜色
            opacity=0.8  # 线的透明度
        ).add_to(m1)  # 将这条线添加到刚才的区域m内

        if self.disconnet != "" :
            i=0
            while i < len(self.disconnet):
                folium.Marker(   # marker方法将坐标在地图标出来
                    self.disconnet[i],
                    weight=3,
                    icon=folium.Icon(color="red")
                ).add_to(m1)
                i+=1

        m1.save(os.path.join('{0}'.format(self.dir) ,self.output))  # 将结果以HTML形式保存到指定路径
    
    #删除多余文件
    def CleanUseless(self): 
        os.system("rm -rf {0} {1} {2} {3}" .format(self.tmp, self.tmplog, self.tmpcsv, self.tmpgpscsv) )

    def Start(self):
        self.DataAnalysis()
        self.draw_gps()
        self.CleanUseless()
        if os.path.exists(self.output):
            print("文件生成成功： {0}/{1}" .format(self.dir, self.output))
        else:
            print("error")
            exit(-1)
            
if __name__ == '__main__':
    if len(sys.argv) >= 3:
                     #网络数据     #坐标数据 
        gv = GpsView(sys.argv[1], sys.argv[2])
        gv.Start()
    else:    
        print("请输入两个参数,前一个是网络测试log,后一个是坐标log\n请把文件放在同级目录下")
















