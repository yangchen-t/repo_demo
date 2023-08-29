package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/cierdes/supervisor-api/supervisor"
	"gopkg.in/yaml.v2"
)

const (
	ColorBlack  Color = "\u001b[30m"
	ColorRed    Color = "\u001b[31m"
	ColorGreen  Color = "\u001b[32m"
	ColorYellow Color = "\u001b[33m"
	ColorBlue   Color = "\u001b[34m"
	ColorReset  Color = "\u001b[0m"
)

// TODO 测试使用 192.168.103.169 或者 192.168.103.105
const URL string = "qomolo:123@localhost:9001"
const PROFILE string = "conf.yaml"

type Color string

// yaml struct
type Conf struct {
	Project string            `yaml:"project"`
	Devices int               `yaml:"device"`
	Dcu1    []map[string]bool `yaml:"dcu1"`
	Dcu2    []map[string]bool `yaml:"dcu2"`
}

// status compare struct
type CurModule struct {
	Cur  map[string]bool `map:"cur"`
	Base map[string]bool `map:"Base"`
}

var moduleStats CurModule
var CurStats bool

func PrintColor(color Color, msg ...any) {
	fmt.Println(string(color), msg, string(ColorReset))
}

func getCurModuleStats() {
	client, _ := supervisor.NewSupervisor(URL)
	defer client.Close()

	CurStatsAllInfo, _ := client.GetAllProcessInfo()
	moduleStats.Cur = make(map[string]bool)
	for i := 0; i < len(CurStatsAllInfo); i++ {
		if CurStatsAllInfo[i].StateName == "RUNNING" {
			CurStats = true
		} else {
			CurStats = false
		}
		moduleStats.Cur[CurStatsAllInfo[i].ProcessName] = CurStats
	}
}
func readConf() {
	_, err := os.Stat(PROFILE)
	if os.IsNotExist(err) {
		PrintColor(ColorRed, "file is not exist: ", PROFILE)
		os.Exit(-1)
	}
	file, err := ioutil.ReadFile(PROFILE)
	if err != nil {
		log.Fatal(err)
	}
	var data []Conf
	err2 := yaml.Unmarshal(file, &data)

	if err2 != nil {
		log.Fatal(err2)
	}
	moduleStats.Base = make(map[string]bool)
	for _, v := range data {
		// TODO 这里需要提供一个变量区分项目. 或者传入一个变量均可
		if v.Project == "wuhan" {
			// TODO 这里需要环境变量区分不同的dcu， 或者切割entrypoint_105模块取得，或者传入变量
			if os.Getenv("device_type") == "105" {
				for _, m := range v.Dcu1 {
					for name, stats := range m {
						moduleStats.Base[name] = stats
					}

				}
			} else {
				for _, m := range v.Dcu2 {
					for name, stats := range m {
						moduleStats.Base[name] = stats
					}
				}
			}
		}
	}
}

func ExistInMap(m1, m2 map[string]bool) bool {
	for v1, _ := range m1 {
		if _, ok := m2[v1]; !ok {
			return false
		}
	}
	return true
}

func compareDiff(moduleStats CurModule) bool {
	PrintColor(ColorYellow, "开始对比模块名称")
	keys1ExistInMap2 := ExistInMap(moduleStats.Cur, moduleStats.Base)
	keys2ExistInMap1 := ExistInMap(moduleStats.Base, moduleStats.Cur)

	if keys1ExistInMap2 && keys2ExistInMap1 {
		PrintColor(ColorGreen, "模块名对比没有差异")
		PrintColor(ColorYellow, "开始检查模块状态")
		if compareStatsDiff(moduleStats) {
			PrintColor(ColorGreen, "模块状态对比没有差异")
			return true
		}
		return false

	}
	PrintColor(ColorYellow, "以下模块与标准模板相比缺少的模块，请重点关注")
	for v, _ := range moduleStats.Base {
		if _, ok := moduleStats.Cur[v]; !ok {
			PrintColor(ColorRed, v)
		}
	}
	PrintColor(ColorYellow, "以下模块与标准模板相比多出的模块，请重点关注")
	for v, _ := range moduleStats.Cur {
		if _, ok := moduleStats.Base[v]; !ok {
			PrintColor(ColorRed, v)
		}
	}
	return false

}

func compareStatsDiff(moduleStats CurModule) bool {
	flags := true
	for v, _ := range moduleStats.Base {
		if moduleStats.Cur[v] != moduleStats.Base[v] {
			PrintColor(ColorRed, "[模块", v, "状态异常]  '正常状态是:", moduleStats.Base[v], "当前的状态是:", moduleStats.Cur[v], "'")
			flags = false
		}
	}
	return flags
}

func main() {
	getCurModuleStats()
	readConf()
	if compareDiff(moduleStats) {
		PrintColor(ColorGreen, "一切正常")
		return
	}
	os.Exit(-1)
}
