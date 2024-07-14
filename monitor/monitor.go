package main

import (
	"fmt"
	"time"

	"github.com/dhamith93/systats"
	"github.com/shirou/gopsutil/process"
)

type Process struct {
	Name string `json:"name"`
	Pid  int32  `json:"pid"`
}

var defualtProcess = []string{"fusion_localizer2_node", "gst-launch-1.0"}
var ret []int32

func ProcessName() []Process {
	pids, _ := process.Pids()
	Parray := make([]Process, len(pids))
	for i, pid := range pids {
		pn, _ := process.NewProcess(pid)
		name, _ := pn.Name()
		Parray[i] = Process{
			Name: name,
			Pid:  pid,
		}
	}
	return Parray
}

func print(P []Process) []int32 {
	for _, process := range P {
		for _, p := range defualtProcess {
			if process.Name == p {
				ret = append(ret, process.Pid)
			}
		}
	}
	return ret
}

func Monitor(pid int32) {
	for {
		// 根据进程ID获取进程对象
		p, err := process.NewProcess(pid)
		if err != nil {
			fmt.Println("获取进程失败:", err)
			return
		}

		// 获取进程的CPU使用率
		cpuPercent, err := p.CPUPercent()
		if err != nil {
			fmt.Println("获取CPU使用率失败:", err)
			return
		}

		// 获取进程的内存使用情况
		memInfo, err := p.MemoryInfo() // memInfo.Rss(Bytes)
		if err != nil {
			fmt.Println("获取内存使用情况失败:", err)
			return
		}

		fmt.Printf("pid: %v CPU使用率: %.2f%% 内存使用: %vMB\n", pid, cpuPercent, memInfo.RSS/1024)

		time.Sleep(time.Second) // 每秒更新一次
	}
}

func TestMonitor(pid int32) {
	p, err := process.NewProcess(int32(pid))
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	for {
		cpuPercent, err := p.CPUPercent()
		if err != nil {
			fmt.Println("Error:", err)
			break
		}

		fmt.Printf("CPU Usage: %.2f%%\n", cpuPercent)

		time.Sleep(time.Second)
	}
}

func main() {
	// test := ProcessName()
	// pid := print(test)
	// for _, v := range pid {
	// 	go Monitor(v)
	// }
	for {
		syStats := systats.New()
		// cpu, _ := syStats.GetCPU()
		// fmt.Println(syStats)
		// fmt.Println(cpu)
		ret, _ := syStats.GetTopProcesses(20, "cpu")

		for i := 0; i < 20; i++ {
			fmt.Println(ret[i].Pid, ret[i].CPUUsage)
		}
		fmt.Println("-----------")
		// fmt.Println(float32(cpu.LoadAvg))
		time.Sleep(time.Second * 1)
	}
}
