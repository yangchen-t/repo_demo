package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
	"gonum.org/v1/plot/vg"
)

var Sync struct {
	wg sync.WaitGroup
	mu sync.Mutex
}

var (
	mutex          sync.Mutex
	filelist       []string
	ERRORFILE      map[string]string
	flameGraphList map[string]string
)

const IMAGEPATH string = "png/"

type StringTicks struct {
	Values plotter.XYs
	Labels []string
}

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

func main() {

	file, err := os.Open("tj-28-105.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var columnData []float64
	colIndex := 9 // 第八列索引为7（从0开始）

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fields := strings.Fields(line)
		if len(fields) > colIndex {
			value, err := strconv.ParseFloat(fields[colIndex], 64)
			if err == nil {
				columnData = append(columnData, value)
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	// for _, data := range columnData {
	// 	fmt.Println(data)
	// }
	MakePng(columnData, "tj-28-105")
}
