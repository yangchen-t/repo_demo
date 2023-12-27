package main

import (
	"fmt"
	"time"
)

type Bar struct {
	percent int    //百分比
	cur     int    //当前进度位置
	total   int    //总进度
	rate    string //进度条
	graph   string //显示符号
}

func (bar *Bar) NewOption(start, total int) {
	bar.cur = start
	bar.total = total
	if bar.graph == "" {
		bar.graph = "#"
	}
	bar.percent = bar.getPercent(total)
	for i := 0; i < int(bar.percent); i += 1 {
		bar.rate += bar.graph //初始化进度条位置
	}
}
func (bar *Bar) getPercent(totalSize int) int {
	return int(float32(bar.cur) / float32(bar.total) * float32(totalSize))
}

func (bar *Bar) NewOptionWithGraph(start, total int, graph string, totalSize int) {
	bar.graph = graph
	bar.NewOption(start, total)
}

func (bar *Bar) Play(cur int, totalSize int) {
	bar.cur = cur
	last := bar.percent
	bar.percent = bar.getPercent(totalSize)
	if bar.percent != last && bar.percent%2 == 0 {
		bar.rate += bar.graph
	}
	fmt.Printf("\r[%-50s]%3d%%  %8d/%d", bar.rate, bar.percent, bar.cur, bar.total)
}
func (bar *Bar) Finish() {
	fmt.Println()
}

func main() {
	var bar Bar
	// TODO get file size
	const totalSize int = 10000
	bar.graph = "="
	bar.NewOption(0, totalSize)
	var runtimeSize = 0
	for {
		if runtimeSize <= totalSize {
			time.Sleep(100 * time.Millisecond)
			bar.Play(int(runtimeSize), totalSize)

		} else if runtimeSize > totalSize {
			break
		}
		runtimeSize = runtimeSize + 10
	}
	bar.Finish()
}
