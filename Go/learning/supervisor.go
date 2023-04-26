package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"strings"

	"github.com/cierdes/supervisor-api/supervisor"
)

const URL string = "qomolo:123@localhost:9001"

type Color string

const (
	ColorBlack  Color = "\u001b[30m"
	ColorRed          = "\u001b[31m"
	ColorGreen        = "\u001b[32m"
	ColorYellow       = "\u001b[33m"
	ColorBlue         = "\u001b[34m"
	ColorReset        = "\u001b[0m"
)

var (
	s = flag.String("f", "nil", "go flag -f s/supervisor")
)

type ModuleList struct {
	CurList  []string
	RealList []string
}

var modulelist ModuleList

func colorize(color Color, message string) {
	fmt.Println(string(color), message, string(ColorReset))
}
func execShell(s string) (string, error) {
	cmd := exec.Command("/bin/bash", "-c", s)
	var out bytes.Buffer
	cmd.Stdout = &out //把执行命令的标准输出定向到out
	cmd.Stderr = &out //把命令的错误输出定向到out

	//启动一个子进程执行命令,阻塞到子进程结束退出
	err := cmd.Run()
	if err != nil {
		return "", err
	}
	return out.String(), err
}

func Arrcmp(src []string, dest []string) ([]string, []string) {
	msrc := make(map[string]byte) //按源数组建索引
	mall := make(map[string]byte) //源+目所有元素建索引

	var set []string //交集

	//1.源数组建立map
	for _, v := range src {
		msrc[v] = 0
		mall[v] = 0
	}
	//2.目数组中，存不进去，即重复元素，所有存不进去的集合就是并集
	for _, v := range dest {
		l := len(mall)
		mall[v] = 1
		if l != len(mall) { //长度变化，即可以存
			l = len(mall)
		} else { //存不了，进并集
			set = append(set, v)
		}
	}
	//3.遍历交集，在并集中找，找到就从并集中删，删完后就是补集（即并-交=所有变化的元素）
	for _, v := range set {
		delete(mall, v)
	}
	//4.此时，mall是补集，所有元素去源中找，找到就是删除的，找不到的必定能在目数组中找到，即新加的
	var added, deleted []string
	for v, _ := range mall {
		_, exist := msrc[v]
		if exist {
			deleted = append(deleted, v)
		} else {
			added = append(added, v)
		}
	}
	return added, deleted
}

func UselessLogClean(diff []string) string {
	for _, v := range diff {
		logname := "sudo rm -rv /data/code/all_ws/ws/" + v
		_, err := execShell(logname)
		if err != nil {
			return "operation error"
		}
	}
	return "clear finish"
}

func supervisorCompare() {
	client, _ := supervisor.NewSupervisor(URL)
	defer client.Close()

	ret, _ := client.GetAllProcessInfo()
	for i := 0; i < len(ret); i++ {
		modulelist.CurList = append(modulelist.CurList, ret[i].ProcessName+".log")
	}
	local_file_ret, _ := execShell("cd /data/code/all_ws/ws && ls *.log")
	modulelist.RealList = strings.Fields(local_file_ret)
	diff, _ := Arrcmp(modulelist.CurList, modulelist.RealList)
	if *s == "s" || *s == "supervisor" {
		for i := 0; i < len(ret); i++ {
			colorize(ColorYellow, ret[i].ProcessName)
		}
		return
	}
	colorize(ColorBlue, "----------------diff----------------")
	if diff == nil {
		fmt.Println("no diff")
		return
	} else {
		for _, v := range diff {
			fmt.Println(v)
		}
	}
	inputReader := bufio.NewReader(os.Stdin)
	colorize(ColorBlue, "----------DEL(y) or IGNORE----------")
	input, err := inputReader.ReadString('\n')
	if err != nil {
		colorize(ColorRed, "There were errors reading, exiting program.")
		return
	}
	switch input {
	case "y\n":
		fmt.Println(UselessLogClean(diff))
	default:
		colorize(ColorRed, "You are not welcome here! Goodbye!")
	}
}
func main() {
	flag.Parse()
	supervisorCompare()
}
