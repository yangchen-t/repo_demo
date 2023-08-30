package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"sync"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
	"gonum.org/v1/plot/vg"
	"gopkg.in/yaml.v2"

	"github.com/jung-kurt/gofpdf"
)

const PROFILE string = "conf.yaml"
const JOURNALCTL string = "/bin/journalctl"
const STARTTIME string = "2023-08-30 07:15:00"
const ENDTIME string = "2023-08-30 07:25:00"
const CPUSERVICE string = "qomolo_pidstat"
const ALLSERVICE string = "qomolo_sar_monitor"
const PDFFILE string = "cpu.pdf"
const IMAGEPATH string = "png/"

var (
	mutex      sync.Mutex
	modules    ModulesList
	subModules Modules
	filelist   []string
)

type ModulesList struct {
	MODULESLIST []string `yaml:"moduleslist"`
}

type Modules struct {
	Time  []string
	Cpu   []float64
	Total []float64
	Name  string
}

// StringTicks 是自定义的 X 轴标签类型
type StringTicks struct {
	Values plotter.XYs
	Labels []string
}

func execShell(s string) (string, error) {
	cmd := exec.Command("/bin/bash", "-c", s)
	var out bytes.Buffer
	cmd.Stdout = &out //把执行命令的标准输出定向到out
	cmd.Stderr = &out //把命令的错误输出定向到out

	err := cmd.Run()
	if err != nil {
		return s + " --> error", err
	}
	Str := strings.TrimRight(out.String(), "\n") // remote string enter
	return Str, err
}

func checkPath(dirPath string) {
	// 使用 os.Stat 检查路径是否存在
	_, err := os.Stat(dirPath)

	// 检查错误
	if err != nil {
		// 如果路径不存在，创建它
		if os.IsNotExist(err) {
			err := os.MkdirAll(dirPath, os.ModePerm)
			if err != nil {
				fmt.Println("创建路径失败:", err)
				return
			}
		} else {
			fmt.Println("检查路径时发生错误:", err)
		}
	} else {
		fmt.Println(dirPath, "is exist")
		return
	}
}

func readConf() {
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

func writeFile(str string, file string) {
	f, err := os.Create(file)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		_, _ = f.WriteString(str)
	}
	defer f.Close()
}

func getFileLineCount(file string) int {
	linecmd := "wc -l " + file + "| awk '{print$1}'"
	lineCount, _ := execShell(linecmd)
	Count, err := strconv.Atoi(lineCount)
	if err != nil {
		fmt.Println("转换失败:", err)
	}
	return Count
}

func visitFile(fp string, fi os.DirEntry, err error) error {
	if err != nil {
		fmt.Println(err) // 可以根据实际情况处理错误
		return nil
	}
	if fi.IsDir() {
		return nil // 忽略目录
	}
	filelist = append(filelist, fp) // 处理文件，加入文件列表
	return nil
}

func Handle(source []float64, vtype string) (plotter.XYs, plotter.XYs, []string) {
	data := make(plotter.XYs, len(source))
	xLabels := make([]string, 0)
	for i := 0; i < len(source); i++ {
		data[i].X = float64(i)
		data[i].Y = float64(i * i)
	}
	// 创建一个包含数据点的数据集
	pts := make(plotter.XYs, 0)
	for i, v := range source {
		pts = append(pts, plotter.XY{X: float64(i + 1), Y: v})
		xLabels = append(xLabels, fmt.Sprintf("%d", i))
	}
	return data, pts, xLabels
}

func MakePng(source []float64, save_png string, vtype string) {

	mutex.Lock()         // 申请互斥锁
	defer mutex.Unlock() // 在函数结束时释放互斥锁

	pngName := save_png + ".png"

	// 创建一个新的绘图
	p := plot.New()

	// 设置绘图的标题和轴标签
	// p.Title.Text = "示例折线图"
	p.X.Label.Text = "time"
	p.Y.Label.Text = "cpu"

	data, pts, xLabels := Handle(source, vtype)
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
	if err := p.Save(20*vg.Inch, 10*vg.Inch, IMAGEPATH+pngName); err != nil {
		log.Fatal(err)
	}

	log.Println("save: ", IMAGEPATH+pngName)
}

func CpuSplitInformation(filename string) Modules {

	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("无法打开文件:", err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	size := getFileLineCount(filename)
	subModules.Time = make([]string, 0)
	subModules.Cpu = make([]float64, 0)
	for i := 0; i < size; i++ {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		// arm
		// cpu, _ := strconv.ParseFloat(strings.Join(strings.Split(line, " ")[6:7], " "), 64)
		cpu, _ := strconv.ParseFloat(strings.Join(strings.Split(line, " ")[7:8], " "), 64)
		time := strings.Join(strings.Split(line, " ")[2:3], " ")
		// TODO debug  fmt.Println(cpu, time, filename)
		subModules.Time = append(subModules.Time, time)
		subModules.Cpu = append(subModules.Cpu, cpu)
	}
	subModules.Name = filename
	return subModules
}

func fullSplitInformation(filename string) Modules {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("无法打开文件:", err)
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	size := getFileLineCount(filename)
	subModules.Total = make([]float64, 0)
	for i := 0; i < size; i++ {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		cmd := "echo '" + line + "' | awk '{print$NF}'"
		total, _ := execShell(cmd)
		ret, _ := strconv.ParseFloat(total, 64)
		subModules.Total = append(subModules.Total, ret)
	}
	return subModules
}

func createPdf() {

	// 创建pdf  页面尺寸为A4
	pdf := gofpdf.New("P", "mm", "A4", "") //

	// 添加一页新的页面
	pdf.AddPage()

	// 设置字体
	pdf.SetFont("Arial", "B", 10)

	// 遍历的目录路径 IMAGEPATH
	err := filepath.WalkDir(IMAGEPATH, visitFile)
	if err != nil {
		fmt.Printf("error walking the path %v: %v\n", IMAGEPATH, err)
	}
	txtOffset := 100
	imagesOffset := 50
	for i, file := range filelist {
		// 添加文本 参数依次是宽度、高度、文本内容
		pdf.Cell(10, float64(10+txtOffset*i), file[len(IMAGEPATH):len(file)-4])
		// 插入图片 参数依次是 X、Y 坐标、宽度、高度、图片文件路径、链接
		pdf.Image(file, 10, float64(20+imagesOffset*i), 80, 40, false, "", 0, "")
	}
	// save
	err = pdf.OutputFileAndClose(PDFFILE)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("save", PDFFILE)
}

func cpuInfo() {
	checkPath(IMAGEPATH)
	const FILE string = "syslog.log"
	cmd := fmt.Sprintf("%s -u %s --since '%s' --until '%s'", JOURNALCTL, CPUSERVICE, STARTTIME, ENDTIME)
	ret, _ := execShell(cmd)
	writeFile(ret, FILE)
	for _, v := range modules.MODULESLIST {
		getinfo := fmt.Sprintf("cat %s | grep %s", FILE, v)
		v_info, err := execShell(getinfo)
		subfile := v + ".log"
		if v_info == "" { // is empty skip
			continue
		}
		if err != nil {
			fmt.Println(err.Error())
		} else {
			writeFile(v_info, subfile)
			MakePng(CpuSplitInformation(subfile).Cpu, v, "cpu")
		}
	}
	const fullinfofile string = "sar.log"
	cmd = fmt.Sprintf("%s -u %s --since '%s' --until '%s'", JOURNALCTL, ALLSERVICE, STARTTIME, ENDTIME)
	ret, _ = execShell(cmd)
	writeFile(ret, fullinfofile)
	cpucmd := fmt.Sprintf("cat %s | grep %s", fullinfofile, "all")
	cpuinfo, err := execShell(cpucmd)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		writeFile(cpuinfo, fullinfofile+"info.log")
		MakePng(fullSplitInformation(fullinfofile+"info.log").Total, "cpuinfo", "total")
	}
}

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

func clearTmp() {
	execShell("rm -rv *.log")
	execShell("rm -rv png/")
}

func main() {
	readConf()
	cpuInfo()
	createPdf()
	clearTmp()
}
