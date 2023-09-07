package main

import (
	"bufio"
	"bytes"
	"flag"
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

var (
	mutex          sync.Mutex
	modules        ModulesList
	subModules     Modules
	filelist       []string
	ERRORFILE      map[string]string
	flameGraphList map[string]string
)
var (
	STARTTIME string
	ENDTIME   string
)

const PROFILE string = "conf.yaml"
const JOURNALCTL string = "/bin/journalctl"
const CPUSERVICE string = "qomolo_pidstat"
const MEMSERVICE string = "qomolo_mem_monitor"
const ALLSERVICE string = "qomolo_sar_monitor"
const PDFFILE string = "cpu.pdf"
const IMAGEPATH string = "png/"
const CPUINFO string = "cpuinfo"
const FLAG string = "1"

var Sync struct {
	wg sync.WaitGroup
	mu sync.Mutex
}

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

func checkParam() {
	if STARTTIME == "" || ENDTIME == "" {
		fmt.Println("template: ./flag -s '2023-08-31 14:20:00' -e '2023-08-31 14:30:00'")
		os.Exit(-1)
	}
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
	Str := strings.TrimRight(out.String(), "\n") // remove string enter
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

func getPID(Pname string, done func()) {
	defer done()
	var pid string
	cmd := "ps aux | grep " + Pname + " | grep -v grep | awk '{print $2}'"
	ret, _ := execShell(cmd)
	Plist := strings.Split(ret, "\n")
	for _, p := range Plist {
		if ret, _ := execShell("ps -p " + p + "| wc -l"); ret != FLAG {
			pid = p
			break
		}
	}
	if pid != "" {
		flameGraphList[Pname] = pid
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

func Handle(source []float64) (plotter.XYs, plotter.XYs, []string) {
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

func MakePng(source []float64, save_png string) {

	mutex.Lock()         // 申请互斥锁
	defer mutex.Unlock() // 在函数结束时释放互斥锁

	pngName := save_png + ".png"

	// 创建一个新的绘图
	p := plot.New()

	// 设置绘图的标题和轴标签
	// p.Title.Text = "示例折线图"
	p.X.Label.Text = "time"
	p.Y.Label.Text = "cpu"

	data, pts, xLabels := Handle(source)
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
		//TODO auto switch
		var cpu float64
		if ret, _ := execShell("arch"); ret == "x86_64" {
			cpu, _ = strconv.ParseFloat(strings.Join(strings.Split(line, " ")[7:8], " "), 64)
		} else {
			cpu, _ = strconv.ParseFloat(strings.Join(strings.Split(line, " ")[6:7], " "), 64)
		}
		time := strings.Join(strings.Split(line, " ")[2:3], " ")
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
	pdf := gofpdf.New("P", "mm", "A5", "")

	// 添加一页新的页面
	pdf.AddPage()

	// 设置字体
	pdf.SetFont("Arial", "B", 10)

	// 遍历的目录路径 IMAGEPATH
	err := filepath.WalkDir(IMAGEPATH, visitFile)
	if err != nil {
		fmt.Printf("error walking the path %v: %v\n", IMAGEPATH, err)
	}
	txtOffset := 10
	imagesOffset := 30
	for i, file := range filelist {
		// 添加文本 参数依次是宽度、高度、文本内容
		pdf.Cell(10, float64(txtOffset*i+10), file[len(IMAGEPATH):len(file)-4])
		// 插入图片 参数依次是 X、Y 坐标、宽度、高度、图片文件路径、链接
		pdf.Image(file, 10, float64(imagesOffset*i+(len(filelist)*10)), 100, 20, false, "", 0, "")
	}
	// save
	err = pdf.OutputFileAndClose(PDFFILE)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("save", PDFFILE)
	clearTmp()
}

func Init() {
	checkParam()
	readConf()
}

func cpuInfo() {
	checkPath(IMAGEPATH)
	const FILE string = "syslog.log"
	cmd := fmt.Sprintf("%s -u %s --since '%s' --until '%s'", JOURNALCTL, CPUSERVICE, STARTTIME, ENDTIME)
	ret, _ := execShell(cmd)
	writeFile(ret, FILE)
	ERRORFILE = make(map[string]string, len(modules.MODULESLIST))
	for _, v := range modules.MODULESLIST {
		getinfo := fmt.Sprintf("cat %s | grep %s", FILE, v)
		v_info, err := execShell(getinfo)
		subfile := v + ".log"
		if v_info == "" { // is empty skip
			ERRORFILE[v] = err.Error()
			continue
		} else {
			writeFile(v_info, subfile)
			MakePng(CpuSplitInformation(subfile).Cpu, v)
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
		MakePng(fullSplitInformation(fullinfofile+"info.log").Total, CPUINFO)
	}
}

func makeFlameGraph() {
	Sync.wg.Add(len(modules.MODULESLIST))
	flameGraphList = make(map[string]string, len(modules.MODULESLIST))
	for _, v := range modules.MODULESLIST {
		go getPID(v, Sync.wg.Done)
	}

}

func clearTmp() {
	if os.Getenv("DELETE") == "false" {
		return
	} else {
		execShell("rm -rv *.log")
		execShell("rm -rv png/")
		failModules()
	}
}

func failModules() {
	if len(ERRORFILE) == 0 {
		return
	} else {
		fmt.Println("----- fail list -----")
		for name, error := range ERRORFILE {
			fmt.Printf("%-20s %s\n", name, error)
		}
		ERRORFILE = nil
	}
	fmt.Println("end ------ end")
}

func main() {
	flag.StringVar(&STARTTIME, "s", "", "")
	flag.StringVar(&ENDTIME, "e", "", "")
	flag.Parse()
	Init()
	cpuInfo()
	// memInfo()
	createPdf()
	makeFlameGraph()
	Sync.wg.Wait()
	fmt.Println(flameGraphList)
	for name, pid := range flameGraphList {
		go execShell("perf_record " + pid + " 1 " + name)
	}
	execShell("make_svg")
}

// func memInfo() {
// 	const FILE string = "memory.log"
// 	cmd := fmt.Sprintf("%s -u %s --since '%s' --until '%s'", JOURNALCTL, MEMSERVICE, STARTTIME, ENDTIME)
// 	ret, _ := execShell(cmd)
// 	writeFile(ret, FILE)
// 	ERRORFILE = make(map[string]string, len(modules.MODULESLIST))
// 	for _, v := range modules.MODULESLIST {
// 		getinfo := fmt.Sprintf("cat %s | grep %s", FILE, v)
// 		v_info, err := execShell(getinfo)
// 		subfile := v + "-mem.log"
// 		if v_info == "" { // is empty skip
// 			continue
// 		}
// 		if err != nil {
// 			fmt.Println(err)
// 			ERRORFILE[v] = err.Error()
// 		} else {
// 			writeFile(v_info, subfile)
// 		}
// 	}
// }
