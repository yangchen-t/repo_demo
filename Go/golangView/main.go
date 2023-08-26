package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
	"gonum.org/v1/plot/vg"
	"gopkg.in/yaml.v2"
)

const FILE string = "syslog"
const PROFILE string = "conf.yaml"
const JOURNALCTL string = "/bin/journalctl"
const STARTTIME string = "2023-08-25 04:00:00"
const ENDTIME string = "2023-08-25 05:00:00"
const CPUSERVICE string = "qomolo_pidstat"
const ALLSERVICE string = "qomolo_sar_monitor"

type ModulesList struct {
	MODULESLIST []string `yaml:"moduleslist"`
}

type Modules struct {
	Time []string
	Cpu  []float64
	Name string
}

// StringTicks 是自定义的 X 轴标签类型
type StringTicks struct {
	Values plotter.XYs
	Labels []string
}

var modules ModulesList
var subModules Modules

// liunx cmd
func execShell(s string) (string, error) {
	cmd := exec.Command("/bin/bash", "-c", s)
	var out bytes.Buffer
	cmd.Stdout = &out //把执行命令的标准输出定向到out
	cmd.Stderr = &out //把命令的错误输出定向到out

	err := cmd.Run()
	if err != nil {
		return s + " --> error", err
	}
	return out.String(), err
}

func ReadConf() {
	_, err := os.Stat(PROFILE)
	if os.IsNotExist(err) {
		fmt.Println("file is not exist: ", PROFILE)
		os.Exit(-1)
	}
	file, err := ioutil.ReadFile(PROFILE)
	if err != nil {
		log.Fatal(err)
	}
	err2 := yaml.Unmarshal(file, &modules)
	if err2 != nil {
		log.Fatal(err2)
	}
}

func WriteFile(str string, file string) {
	f, err := os.Create(file)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		_, err = f.WriteString(str)
	}
	defer f.Close()
}

func GetFileLineCount(file string) int {
	linecmd := "wc -l " + file + "| awk '{print$1}'"
	lineCount, _ := execShell(linecmd)
	Count, _ := strconv.Atoi(lineCount)
	return Count
}

func MakePng(sub Modules, save_png string) {
	// 创建一个新的绘图
	p := plot.New()

	// 设置绘图的标题和轴标签
	// p.Title.Text = "示例折线图"
	p.X.Label.Text = "time"
	p.Y.Label.Text = "cpu"

	// 创建一个包含数据点的数据集
	pts := make(plotter.XYs, 0)
	for i, v := range sub.Cpu {
			pts = append(pts, plotter.XY{X: i, Y: v})
		}
	}

	// 创建一个折线图
	line, err := plotter.NewLine(pts)

	if err != nil {
		log.Fatal(err)
	}
	line.Color = plotutil.Color(0)
	p.X.Tick.Marker = StringTicks{
		Values: data,
		Labels: xLabels,
	}
	// 添加折线图到绘图
	p.Add(line)

	// 保存绘图到文件
	if err := p.Save(15*vg.Inch, 15*vg.Inch, save_png+".png"); err != nil {
		log.Fatal(err)
	}

	log.Println("折线图已保存为: ", save_png+".png")
}

// func png(sub Modules, save_png string) {
// 	p := plot.New()

// 	// 创建一个包含数据点的数据集
// 	data := make(plotter.XYs, 0)
// 	// xLabels := []string{"Jan", "Feb", "Mar", "Apr", "May"}
// 	xLabels := sub.Time

// 	for i := 0; i < len(xLabels); i++ {
// 		data[i].X = float64(i)
// 		data[i].Y = float64(i * i)
// 	}

// 	// 创建折线图
// 	line, err := plotter.NewLine(data)
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	line.LineStyle.Width = vg.Points(1) // 设置线条宽度

// 	// 设置 X 轴标签
// 	p.X.Tick.Marker = StringTicks{
// 		Values: data,
// 		Labels: xLabels,
// 	}

// 	p.Add(line)

// 	// 保存绘图到文件
// 	if err := p.Save(4*vg.Inch, 4*vg.Inch, "custom_x_axis_line_plot.png"); err != nil {
// 		fmt.Println(err)
// 		return
// 	}

// 	fmt.Println("折线图已保存为 custom_x_axis_line_plot.png")
// }

// Ticks 实现 plot.Ticker 接口
func (s StringTicks) Ticks(min, max float64) []plot.Tick {
	ticks := []plot.Tick{}
	for i, v := range s.Values {
		// 将数值转换为字符串标签
		tick := plot.Tick{
			Value: v.X,
			Label: s.Labels[i],
		}
		ticks = append(ticks, tick)
	}
	return ticks
}

func CpuInfo() {
	cmd := fmt.Sprintf("%s -u %s --since '%s' --until '%s'", JOURNALCTL, CPUSERVICE, STARTTIME, ENDTIME)
	ret, _ := execShell(cmd)
	WriteFile(ret, FILE)
	for _, v := range modules.MODULESLIST {
		getinfo := fmt.Sprintf("cat %s | grep %s", FILE, v)
		v_info, err := execShell(getinfo)
		subfile := FILE + "-" + v + ".log"
		if v_info == "" {
			continue
		}
		WriteFile(v_info, subfile)
		if err != nil {
			fmt.Println(err.Error())
		} else {
			// MakePng(SplitInformation(subfile), v)
			// SplitInformation(subfile)
			png(SplitInformation(subfile), v)
		}
	}
}

// split informatin
func SplitInformation(filename string) Modules {

	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("无法打开文件:", err)
	}
	defer file.Close() // 在函数结束时关闭文件

	reader := bufio.NewReader(file)
	subModules.Time = make([]string, 1476)
	subModules.Cpu = make([]float64, 1476)

	for i := 0; i < 1476; i++ {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		// 输出行内容
		cpu, _ := strconv.ParseFloat(strings.Join(strings.Split(line, " ")[7:8], " "), 64)
		time := strings.Join(strings.Split(line, " ")[2:3], " ")
		subModules.Time = append(subModules.Time, time)
		subModules.Cpu = append(subModules.Cpu, cpu)
	}
	// subModules.Name = filename
	return subModules
}

func ClearTmp() {
	for _, m := range modules.MODULESLIST {
		rmFile := "rm -rv " + FILE + "-" + m + ".log"
		execShell(rmFile)
	}
	execShell("rm -rv " + FILE)
}

func main() {
	ReadConf()
	CpuInfo()
	time.Sleep(time.Second * 2)
	// ClearTmp()
	// execShell("rm -r *.png")
}
